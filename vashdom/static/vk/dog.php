<?
header("Content-Type: text/html; charset=UTF-8");

set_time_limit(14400); //Макс. время выполнения 2 часа
include "config.php";

$path_parts = pathinfo($_SERVER['SCRIPT_FILENAME']); // определяем директорию скрипта
chdir($path_parts['dirname']); // задаем директорию выполнение скрипта

//Подключение к БД
mysql_connect($SQL_HOST, $SQL_USER, $SQL_PASS) or die ("Ошибка подключения к БД: ".mysql_error());
mysql_select_db($SQL_DB_NAME);

$ch = curl_init(); //Создание нового ресурса cURL
curl_setopt($ch, CURLOPT_RETURNTRANSFER, True); //Возврат результата в строковую переменную
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, False); //Отключение сертификата
curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, False); //Отключение сертификата
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Accept-Language: ru,en-us')); //Заголовок языковой поддержки
curl_setopt($ch, CURLOPT_USERAGENT, "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0)"); //Тип броузера

//Обработка черного списка Питер
$bl = array(); //Массив черного списка
$dog = array(); //Массив собак на удаление

$sql = "SELECT user_id FROM ca_spb WHERE type = 'bl'";
$result = mysql_query($sql);

while ($row = mysql_fetch_array($result))
{
	$bl[] = $row["user_id"];
}

//Получение данных пользователей
while (count($bl) > 0)
{
	if (count($bl) > 1000) {$j = 1000;} else {$j = count($bl);}
	
	$uid = array(); //Массив пользователей для запроса
	
	for ($i = 0; $i < $j; $i++)
	{
		$uid[] = $bl[0];
		array_shift($bl);
	}
	
	$uid_str = implode(",", $uid); //Строка ID пользователей

	//Запрос к VK
	$url = "https://api.vk.com/method/users.get.xml?user_ids=".$uid_str;
	curl_setopt($ch, CURLOPT_URL, $url); //Установка URL
	$content = curl_exec($ch); //Загрузка страницы

	$dog_xml = new SimpleXMLElement($content);
	foreach ($dog_xml->user as $user)
	{
	if (isset($user->deactivated))
	{
		$dog[] = (int)$user->uid;
	}
	}
	unset($dog_xml);
}

//Удаление собак
foreach ($dog as $dg)
{
	$sql = "DELETE FROM ca_spb WHERE user_id = ".$dg;
	mysql_query($sql);
}


//Обработка черного списка Москва
$bl = array(); //Массив черного списка
$dog = array(); //Массив собак на удаление

$sql = "SELECT user_id FROM ca_msk WHERE type = 'bl'";
$result = mysql_query($sql);

while ($row = mysql_fetch_array($result))
{
	$bl[] = $row["user_id"];
}

//Получение данных пользователей
while (count($bl) > 0)
{
	if (count($bl) > 1000) {$j = 1000;} else {$j = count($bl);}
	
	$uid = array(); //Массив пользователей для запроса
	
	for ($i = 0; $i < $j; $i++)
	{
		$uid[] = $bl[0];
		array_shift($bl);
	}
	
	$uid_str = implode(",", $uid); //Строка ID пользователей

	//Запрос к VK
	$url = "https://api.vk.com/method/users.get.xml?user_ids=".$uid_str;
	curl_setopt($ch, CURLOPT_URL, $url); //Установка URL
	echo $content = curl_exec($ch); //Загрузка страницы

	$dog_xml = new SimpleXMLElement($content);
	foreach ($dog_xml->user as $user)
	{
	if (isset($user->deactivated))
	{
		$dog[] = (int)$user->uid;
	}
	}
	unset($dog_xml);
}

//Удаление собак
foreach ($dog as $dg)
{
	$sql = "DELETE FROM ca_msk WHERE user_id = ".$dg;
	mysql_query($sql);
}

curl_close($ch);
?>