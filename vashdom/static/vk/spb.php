<?
header("Content-Type: text/html; charset=UTF-8");

error_reporting(0);
set_time_limit(14400); //Макс. время выполнения 2 часа

include "config.php";

$path_parts = pathinfo($_SERVER['SCRIPT_FILENAME']); // определяем директорию скрипта
chdir($path_parts['dirname']); // задаем директорию выполнение скрипта

//Список групп
$groups = file("spb.txt");
$check_time = time() - $time_ago*60*60; //Время глубины парсинга

//Подключение к БД
mysql_connect($SQL_HOST, $SQL_USER, $SQL_PASS) or die ("Ошибка подключения к БД: ".mysql_error());
mysql_select_db($SQL_DB_NAME);

$ch = curl_init(); //Создание нового ресурса cURL
curl_setopt($ch, CURLOPT_RETURNTRANSFER, True); //Возврат результата в строковую переменную
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, False); //Отключение сертификата
curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, False); //Отключение сертификата
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Accept-Language: ru,en-us')); //Заголовок языковой поддержки
curl_setopt($ch, CURLOPT_USERAGENT, "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0)"); //Тип броузера

foreach ($groups as $group)
{
if (trim($group) == "")	{continue;}
	
$hot = array(); //ID Горячих
$warm = array(); //ID Теплых
$bl = array(); //ID Черного списка
$dogs = array(); //ID Собак

//Получение ID группы
$url = "https://api.vk.com/method/groups.getById.xml?group_ids=".trim($group);
curl_setopt($ch, CURLOPT_URL, $url); //Установка URL
$content = curl_exec($ch); //Загрузка страницы
preg_match("|<gid>(.*)</gid>|Uis", $content, $out);
$gid = $out[1]; //ID Группы

if ((int)$gid == 0) {continue;}

//Получение списка тем группы
$group_topic = array(); //Массив ID тем группы

$url = "https://api.vk.com/method/board.getTopics.xml?group_id=".$gid."&order=1&count=100";
curl_setopt($ch, CURLOPT_URL, $url); //Установка URL
$content = curl_exec($ch); //Загрузка страницы

$topic_xml = new SimpleXMLElement($content);

if ((int)$topic_xml->topics->count == 0) {unset($topic_xml); continue;}

foreach ($topic_xml->topics->topic as $topic)
{
if ((int)$topic->updated > $check_time)
{
	$group_topic[] = (int)$topic->tid;
}
}
unset($topic_xml);

//Обработка комментариев в темах группы
foreach ($group_topic as $gtopic)
{	
	$offset = 0;
	
	while (true)
	{	
		$url = "https://api.vk.com/method/board.getComments.xml?group_id=".$gid."&topic_id=".$gtopic."&count=100&extended=1&sort=desc&offset=".$offset*100; 
		curl_setopt($ch, CURLOPT_URL, $url); //Установка URL
		$content = curl_exec($ch); //Загрузка страницы
		
		//Проверка на ошибку получения запроса
		if (preg_match("|error|", $content))
		{
			echo $content;
			unset($wall_xml);
			break;
		}

		$gtopic_xml = new SimpleXMLElement($content);
		
		//Отлов собак
		foreach ($gtopic_xml->profiles->user as $dog)
		{
			if (isset($dog->deactivated))
			{
				$dog_id = (int)$dog->uid;
				if (!in_array($dog_id, $dogs))
				{
					$dogs[] = $dog_id;
				}
			}
		}
		
		//Парсинг текста комментов тем группы
		foreach ($gtopic_xml->comments->comment as $comment)
		{
		//Проверка даты публикации
		if ((int)$comment->date < $check_time)
		{
			unset($gtopic_xml);
			break(2);
		}
		
		//Проверка на собаку
		if (in_array((int)$comment->from_id, $dogs))
		{
			continue;
		}
			
		//Обработка текста коммента
		$from = array("<br>", "ё");
		$to = array(" ", "е");
		$text = mb_strtolower(str_replace($from, $to, (string)$comment->text), "UTF-8");
		
		//Проверка по горячему списку
		if (preg_match($hot_pattern, $text))
		{
			$hot["user_id"][] = (int)$comment->from_id;
			$hot["adress"][] = (int)$comment->id;
			$hot["date"][] = (int)$comment->date;
			$hot["action"][] = "comment";
		}
		
		//Проверка по черному списку
		if (preg_match($bl_pattern, $text))
		{
			$bl[] = (int)$comment->from_id;
		}		
		}

		unset($gtopic_xml);
		
		$offset++;
		sleep($pause);
	}
}

//Обработка постов на стене группы
	$offset = 0;
	
	while (true)
	{	
		$url = "https://api.vk.com/method/wall.get.xml?owner_id=-".$gid."&count=100&extended=1&offset=".$offset*100;
		curl_setopt($ch, CURLOPT_URL, $url); //Установка URL
		$content = curl_exec($ch); //Загрузка страницы
		
		//Проверка на ошибку получения запроса
		if (preg_match("|error|", $content))
		{
			echo $content;
			unset($wall_xml);
			break;
		}

		$wall_xml = new SimpleXMLElement($content);

		//Отлов собак
		foreach ($wall_xml->profiles->user as $dog)
		{
			if (isset($dog->deactivated))
			{
				$dog_id = (int)$dog->uid;
				if (!in_array($dog_id, $dogs))
				{
					$dogs[] = $dog_id;
				}
			}
		}		
		
		//Обработка постов
		foreach ($wall_xml->wall->post as $post)
		{		
		//Проверка на пост от имени группы
		if ((int)$post->from_id < 0)
		{	
			//Проверка закрепленной записи
			if (isset($post->is_pinned)) {continue;}
			
			//Проверка даты публикации
			if ((int)$post->date < $check_time)
			{
				unset($wall_xml);
				break(2);
			}
			
			//Обработка комментов к постам на стене
			if ((int)$post->comments->count > 0)
			{
				$url = "https://api.vk.com/method/wall.getComments.xml?owner_id=-".$gid."&post_id=".(int)$post->id."&count=100"; 
				curl_setopt($ch, CURLOPT_URL, $url); //Установка URL
				$content = curl_exec($ch); //Загрузка страницы

				$topic_xml = new SimpleXMLElement($content);
				foreach ($topic_xml->comment as $comment)
				{
				//Обработка текста поста
				$from = array("<br>", "ё");
				$to = array(" ", "е");
				$text = mb_strtolower(str_replace($from, $to, (string)$comment->text), "UTF-8");
		
				//Проверка по горячему списку
				if (preg_match($hot_pattern, $text))
				{
					$hot["user_id"][] = (int)$comment->from_id;
					$hot["adress"][] = (int)$post->id;
					$hot["date"][] = (int)$comment->date;
					$hot["action"][] = "comment";
				}
		
				//Проверка по черному списку
				if (preg_match($bl_pattern, $text))
				{
					$bl[] = (int)$comment->from_id;
				}		
				}
				unset($topic_xml);
			}
			
			//Проверка теплых по лайкам с отсечкой картинок c текстом короче 50 символов
			if (((int)$post->likes->count > 0) && (strlen((string)$post->text) > 50))
			{
				$url = "https://api.vk.com/method/likes.getList.xml?owner_id=-".$gid."&count=1000&type=post&item_id=".(int)$post->id; 
				curl_setopt($ch, CURLOPT_URL, $url); //Установка URL
				$content = curl_exec($ch); //Загрузка страницы
			
				$likes_xml = new SimpleXMLElement($content);
				foreach($likes_xml->users->uid as $uid)
				{
					$warm["user_id"][] = (int)$uid;
					$warm["adress"][] = (int)$post->id;
					$warm["date"][] = (int)$post->date;
					$warm["action"][] = "like";
				}
				unset($likes_xml);
			}
		continue;
		}
		
		//Проверка на собаку
		if (in_array((int)$post->from_id, $dogs))
		{
			continue;
		}
		
		//Проверка даты публикации
		if ((int)$post->date < $check_time)
		{
			unset($wall_xml);
			break(2);
		}
				
		//Обработка текста поста
		$from = array("<br>", "ё");
		$to = array(" ", "е");
		$text = mb_strtolower(str_replace($from, $to, (string)$post->text), "UTF-8");
		
		//Проверка по горячему списку
		if (preg_match($hot_pattern, $text))
		{
			$hot["user_id"][] = (int)$post->from_id;
			$hot["adress"][] = (int)$post->id;
			$hot["date"][] = (int)$post->date;
			$hot["action"][] = "post";
		}
		
		//Проверка по черному списку
		if (preg_match($bl_pattern, $text))
		{
			$bl[] = (int)$post->from_id;
		}		

		//Проверка теплых по лайкам
		if ((int)$post->likes->count > 0)
		{
			$url = "https://api.vk.com/method/likes.getList.xml?owner_id=-".$gid."&count=1000&type=post&item_id=".(int)$post->id; 
			curl_setopt($ch, CURLOPT_URL, $url); //Установка URL
			$content = curl_exec($ch); //Загрузка страницы
			
			$likes_xml = new SimpleXMLElement($content);
			foreach($likes_xml->users->uid as $uid)
			{
				$warm["user_id"][] = (int)$uid;
				$warm["adress"][] = (int)$post->id;
				$warm["date"][] = (int)$post->date;
				$warm["action"][] = "like";
			}
			unset($likes_xml);
		}
		}

		unset($wall_xml);

		$offset++;
		sleep($pause);
	}

//Уникализация черного списка
$bl = array_unique($bl);

//Запись в БД горячих
if (count($hot) > 0)
{
for ($i=0; $i<count($hot["user_id"]); $i++)
{
	//Формирование запросов
	$val = "(".quote_smart(date("Y-m-d H:i:s", $hot["date"][$i])).", ".quote_smart($hot["user_id"][$i]).", ".quote_smart($hot["action"][$i]).", ".quote_smart($hot["adress"][$i]).", 'hot')";
	$sql = "INSERT INTO ca_spb (date, user_id, action, adress, type) VALUES ".$val;
	mysql_query($sql);
}
}

//Запись в БД теплых
if (count($warm) > 0)
{
for ($i=0; $i<count($warm["user_id"]); $i++)
{
	//Формирование запросов
	$val = "(".quote_smart(date("Y-m-d H:i:s", $warm["date"][$i])).", ".quote_smart($warm["user_id"][$i]).", ".quote_smart($warm["action"][$i]).", ".quote_smart($warm["adress"][$i]).", 'warm')";
	$sql = "INSERT INTO ca_spb (date, user_id, action, adress, type) VALUES ".$val;
	mysql_query($sql);
}
}

//Запись в БД черного списка
foreach ($bl as $black_list)
{
	//Формирование запросов
	$val = "(NOW(), ".quote_smart($black_list).", 'bl')";
	$sql = "INSERT INTO ca_spb (date, user_id, type) VALUES ".$val;
	mysql_query($sql);
}
}

curl_close($ch);

//Удаление записей старше $days_to_delete дней
$sql = "DELETE FROM ca_spb WHERE (date < DATE_SUB(NOW(), INTERVAL ".$days_to_delete." DAY)) AND (type = 'warm' OR type = 'hot')";
mysql_query($sql);

//Подсчет активности для занесения в черный список
$sql = "UPDATE ca_spb SET type='bl' WHERE user_id IN (SELECT user_id FROM (SELECT user_id, COUNT(*) AS total FROM ca_spb WHERE (type='warm' OR type='hot') GROUP BY user_id ORDER BY total DESC) AS counted_table WHERE counted_table.total >= ".$action_count_for_bl.")";
mysql_query($sql);

//Удаление повторов из черного списка
$sql = "DELETE main_table FROM ca_spb main_table, ca_spb clone_table WHERE main_table.user_id = clone_table.user_id AND main_table.type='bl' AND main_table.id > clone_table.id";
mysql_query($sql);

//Выгрузка горячих
$sql = "SELECT DISTINCT user_id FROM ca_spb WHERE (date > DATE_SUB(NOW(), INTERVAL ".$days_to_upload." DAY)) AND (type = 'hot') AND (user_id NOT IN (SELECT user_id FROM ca_spb WHERE type = 'bl'))";
$result = mysql_query($sql);

$hot_str = "";
while ($row = mysql_fetch_array($result))
{
	$hot_str .= "".$row["user_id"]."\r\n";
}

file_put_contents("spb_hot.txt", $hot_str);

//Выгрузка теплых
$sql = "SELECT DISTINCT user_id FROM ca_spb WHERE (date > DATE_SUB(NOW(), INTERVAL ".$days_to_upload." DAY)) AND (type = 'warm') AND (user_id NOT IN (SELECT DISTINCT user_id FROM ca_spb WHERE (type = 'bl' OR type = 'hot')))";
$result = mysql_query($sql);

$warm_str = "";
while ($row = mysql_fetch_array($result))
{
	$warm_str .= "".$row["user_id"]."\r\n";
}

file_put_contents("spb_warm.txt", $warm_str);


////////////////////////////////////////////////////////////////////////////
function quote_smart($value)
{
    // если magic_quotes_gpc включена - используем stripslashes
	if (get_magic_quotes_gpc()) 
	{
		$value = stripslashes($value);
    }
	
    // окружем переменную кавычками и экранируем
	$value = "'" . mysql_real_escape_string($value) . "'";

	return $value;
}
?>