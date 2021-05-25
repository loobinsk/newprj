/*! jQuery v2.0.3 | (c) 2005, 2013 jQuery Foundation, Inc. | jquery.org/license
//@ sourceMappingURL=jquery-2.0.3.min.map
*/
(function(e,undefined){var t,n,r=typeof undefined,i=e.location,o=e.document,s=o.documentElement,a=e.jQuery,u=e.$,l={},c=[],p="2.0.3",f=c.concat,h=c.push,d=c.slice,g=c.indexOf,m=l.toString,y=l.hasOwnProperty,v=p.trim,x=function(e,n){return new x.fn.init(e,n,t)},b=/[+-]?(?:\d*\.|)\d+(?:[eE][+-]?\d+|)/.source,w=/\S+/g,T=/^(?:\s*(<[\w\W]+>)[^>]*|#([\w-]*))$/,C=/^<(\w+)\s*\/?>(?:<\/\1>|)$/,k=/^-ms-/,N=/-([\da-z])/gi,E=function(e,t){return t.toUpperCase()},S=function(){o.removeEventListener("DOMContentLoaded",S,!1),e.removeEventListener("load",S,!1),x.ready()};x.fn=x.prototype={jquery:p,constructor:x,init:function(e,t,n){var r,i;if(!e)return this;if("string"==typeof e){if(r="<"===e.charAt(0)&&">"===e.charAt(e.length-1)&&e.length>=3?[null,e,null]:T.exec(e),!r||!r[1]&&t)return!t||t.jquery?(t||n).find(e):this.constructor(t).find(e);if(r[1]){if(t=t instanceof x?t[0]:t,x.merge(this,x.parseHTML(r[1],t&&t.nodeType?t.ownerDocument||t:o,!0)),C.test(r[1])&&x.isPlainObject(t))for(r in t)x.isFunction(this[r])?this[r](t[r]):this.attr(r,t[r]);return this}return i=o.getElementById(r[2]),i&&i.parentNode&&(this.length=1,this[0]=i),this.context=o,this.selector=e,this}return e.nodeType?(this.context=this[0]=e,this.length=1,this):x.isFunction(e)?n.ready(e):(e.selector!==undefined&&(this.selector=e.selector,this.context=e.context),x.makeArray(e,this))},selector:"",length:0,toArray:function(){return d.call(this)},get:function(e){return null==e?this.toArray():0>e?this[this.length+e]:this[e]},pushStack:function(e){var t=x.merge(this.constructor(),e);return t.prevObject=this,t.context=this.context,t},each:function(e,t){return x.each(this,e,t)},ready:function(e){return x.ready.promise().done(e),this},slice:function(){return this.pushStack(d.apply(this,arguments))},first:function(){return this.eq(0)},last:function(){return this.eq(-1)},eq:function(e){var t=this.length,n=+e+(0>e?t:0);return this.pushStack(n>=0&&t>n?[this[n]]:[])},map:function(e){return this.pushStack(x.map(this,function(t,n){return e.call(t,n,t)}))},end:function(){return this.prevObject||this.constructor(null)},push:h,sort:[].sort,splice:[].splice},x.fn.init.prototype=x.fn,x.extend=x.fn.extend=function(){var e,t,n,r,i,o,s=arguments[0]||{},a=1,u=arguments.length,l=!1;for("boolean"==typeof s&&(l=s,s=arguments[1]||{},a=2),"object"==typeof s||x.isFunction(s)||(s={}),u===a&&(s=this,--a);u>a;a++)if(null!=(e=arguments[a]))for(t in e)n=s[t],r=e[t],s!==r&&(l&&r&&(x.isPlainObject(r)||(i=x.isArray(r)))?(i?(i=!1,o=n&&x.isArray(n)?n:[]):o=n&&x.isPlainObject(n)?n:{},s[t]=x.extend(l,o,r)):r!==undefined&&(s[t]=r));return s},x.extend({expando:"jQuery"+(p+Math.random()).replace(/\D/g,""),noConflict:function(t){return e.$===x&&(e.$=u),t&&e.jQuery===x&&(e.jQuery=a),x},isReady:!1,readyWait:1,holdReady:function(e){e?x.readyWait++:x.ready(!0)},ready:function(e){(e===!0?--x.readyWait:x.isReady)||(x.isReady=!0,e!==!0&&--x.readyWait>0||(n.resolveWith(o,[x]),x.fn.trigger&&x(o).trigger("ready").off("ready")))},isFunction:function(e){return"function"===x.type(e)},isArray:Array.isArray,isWindow:function(e){return null!=e&&e===e.window},isNumeric:function(e){return!isNaN(parseFloat(e))&&isFinite(e)},type:function(e){return null==e?e+"":"object"==typeof e||"function"==typeof e?l[m.call(e)]||"object":typeof e},isPlainObject:function(e){if("object"!==x.type(e)||e.nodeType||x.isWindow(e))return!1;try{if(e.constructor&&!y.call(e.constructor.prototype,"isPrototypeOf"))return!1}catch(t){return!1}return!0},isEmptyObject:function(e){var t;for(t in e)return!1;return!0},error:function(e){throw Error(e)},parseHTML:function(e,t,n){if(!e||"string"!=typeof e)return null;"boolean"==typeof t&&(n=t,t=!1),t=t||o;var r=C.exec(e),i=!n&&[];return r?[t.createElement(r[1])]:(r=x.buildFragment([e],t,i),i&&x(i).remove(),x.merge([],r.childNodes))},parseJSON:JSON.parse,parseXML:function(e){var t,n;if(!e||"string"!=typeof e)return null;try{n=new DOMParser,t=n.parseFromString(e,"text/xml")}catch(r){t=undefined}return(!t||t.getElementsByTagName("parsererror").length)&&x.error("Invalid XML: "+e),t},noop:function(){},globalEval:function(e){var t,n=eval;e=x.trim(e),e&&(1===e.indexOf("use strict")?(t=o.createElement("script"),t.text=e,o.head.appendChild(t).parentNode.removeChild(t)):n(e))},camelCase:function(e){return e.replace(k,"ms-").replace(N,E)},nodeName:function(e,t){return e.nodeName&&e.nodeName.toLowerCase()===t.toLowerCase()},each:function(e,t,n){var r,i=0,o=e.length,s=j(e);if(n){if(s){for(;o>i;i++)if(r=t.apply(e[i],n),r===!1)break}else for(i in e)if(r=t.apply(e[i],n),r===!1)break}else if(s){for(;o>i;i++)if(r=t.call(e[i],i,e[i]),r===!1)break}else for(i in e)if(r=t.call(e[i],i,e[i]),r===!1)break;return e},trim:function(e){return null==e?"":v.call(e)},makeArray:function(e,t){var n=t||[];return null!=e&&(j(Object(e))?x.merge(n,"string"==typeof e?[e]:e):h.call(n,e)),n},inArray:function(e,t,n){return null==t?-1:g.call(t,e,n)},merge:function(e,t){var n=t.length,r=e.length,i=0;if("number"==typeof n)for(;n>i;i++)e[r++]=t[i];else while(t[i]!==undefined)e[r++]=t[i++];return e.length=r,e},grep:function(e,t,n){var r,i=[],o=0,s=e.length;for(n=!!n;s>o;o++)r=!!t(e[o],o),n!==r&&i.push(e[o]);return i},map:function(e,t,n){var r,i=0,o=e.length,s=j(e),a=[];if(s)for(;o>i;i++)r=t(e[i],i,n),null!=r&&(a[a.length]=r);else for(i in e)r=t(e[i],i,n),null!=r&&(a[a.length]=r);return f.apply([],a)},guid:1,proxy:function(e,t){var n,r,i;return"string"==typeof t&&(n=e[t],t=e,e=n),x.isFunction(e)?(r=d.call(arguments,2),i=function(){return e.apply(t||this,r.concat(d.call(arguments)))},i.guid=e.guid=e.guid||x.guid++,i):undefined},access:function(e,t,n,r,i,o,s){var a=0,u=e.length,l=null==n;if("object"===x.type(n)){i=!0;for(a in n)x.access(e,t,a,n[a],!0,o,s)}else if(r!==undefined&&(i=!0,x.isFunction(r)||(s=!0),l&&(s?(t.call(e,r),t=null):(l=t,t=function(e,t,n){return l.call(x(e),n)})),t))for(;u>a;a++)t(e[a],n,s?r:r.call(e[a],a,t(e[a],n)));return i?e:l?t.call(e):u?t(e[0],n):o},now:Date.now,swap:function(e,t,n,r){var i,o,s={};for(o in t)s[o]=e.style[o],e.style[o]=t[o];i=n.apply(e,r||[]);for(o in t)e.style[o]=s[o];return i}}),x.ready.promise=function(t){return n||(n=x.Deferred(),"complete"===o.readyState?setTimeout(x.ready):(o.addEventListener("DOMContentLoaded",S,!1),e.addEventListener("load",S,!1))),n.promise(t)},x.each("Boolean Number String Function Array Date RegExp Object Error".split(" "),function(e,t){l["[object "+t+"]"]=t.toLowerCase()});function j(e){var t=e.length,n=x.type(e);return x.isWindow(e)?!1:1===e.nodeType&&t?!0:"array"===n||"function"!==n&&(0===t||"number"==typeof t&&t>0&&t-1 in e)}t=x(o),function(e,undefined){var t,n,r,i,o,s,a,u,l,c,p,f,h,d,g,m,y,v="sizzle"+-new Date,b=e.document,w=0,T=0,C=st(),k=st(),N=st(),E=!1,S=function(e,t){return e===t?(E=!0,0):0},j=typeof undefined,D=1<<31,A={}.hasOwnProperty,L=[],q=L.pop,H=L.push,O=L.push,F=L.slice,P=L.indexOf||function(e){var t=0,n=this.length;for(;n>t;t++)if(this[t]===e)return t;return-1},R="checked|selected|async|autofocus|autoplay|controls|defer|disabled|hidden|ismap|loop|multiple|open|readonly|required|scoped",M="[\\x20\\t\\r\\n\\f]",W="(?:\\\\.|[\\w-]|[^\\x00-\\xa0])+",$=W.replace("w","w#"),B="\\["+M+"*("+W+")"+M+"*(?:([*^$|!~]?=)"+M+"*(?:(['\"])((?:\\\\.|[^\\\\])*?)\\3|("+$+")|)|)"+M+"*\\]",I=":("+W+")(?:\\(((['\"])((?:\\\\.|[^\\\\])*?)\\3|((?:\\\\.|[^\\\\()[\\]]|"+B.replace(3,8)+")*)|.*)\\)|)",z=RegExp("^"+M+"+|((?:^|[^\\\\])(?:\\\\.)*)"+M+"+$","g"),_=RegExp("^"+M+"*,"+M+"*"),X=RegExp("^"+M+"*([>+~]|"+M+")"+M+"*"),U=RegExp(M+"*[+~]"),Y=RegExp("="+M+"*([^\\]'\"]*)"+M+"*\\]","g"),V=RegExp(I),G=RegExp("^"+$+"$"),J={ID:RegExp("^#("+W+")"),CLASS:RegExp("^\\.("+W+")"),TAG:RegExp("^("+W.replace("w","w*")+")"),ATTR:RegExp("^"+B),PSEUDO:RegExp("^"+I),CHILD:RegExp("^:(only|first|last|nth|nth-last)-(child|of-type)(?:\\("+M+"*(even|odd|(([+-]|)(\\d*)n|)"+M+"*(?:([+-]|)"+M+"*(\\d+)|))"+M+"*\\)|)","i"),bool:RegExp("^(?:"+R+")$","i"),needsContext:RegExp("^"+M+"*[>+~]|:(even|odd|eq|gt|lt|nth|first|last)(?:\\("+M+"*((?:-\\d)?\\d*)"+M+"*\\)|)(?=[^-]|$)","i")},Q=/^[^{]+\{\s*\[native \w/,K=/^(?:#([\w-]+)|(\w+)|\.([\w-]+))$/,Z=/^(?:input|select|textarea|button)$/i,et=/^h\d$/i,tt=/'|\\/g,nt=RegExp("\\\\([\\da-f]{1,6}"+M+"?|("+M+")|.)","ig"),rt=function(e,t,n){var r="0x"+t-65536;return r!==r||n?t:0>r?String.fromCharCode(r+65536):String.fromCharCode(55296|r>>10,56320|1023&r)};try{O.apply(L=F.call(b.childNodes),b.childNodes),L[b.childNodes.length].nodeType}catch(it){O={apply:L.length?function(e,t){H.apply(e,F.call(t))}:function(e,t){var n=e.length,r=0;while(e[n++]=t[r++]);e.length=n-1}}}function ot(e,t,r,i){var o,s,a,u,l,f,g,m,x,w;if((t?t.ownerDocument||t:b)!==p&&c(t),t=t||p,r=r||[],!e||"string"!=typeof e)return r;if(1!==(u=t.nodeType)&&9!==u)return[];if(h&&!i){if(o=K.exec(e))if(a=o[1]){if(9===u){if(s=t.getElementById(a),!s||!s.parentNode)return r;if(s.id===a)return r.push(s),r}else if(t.ownerDocument&&(s=t.ownerDocument.getElementById(a))&&y(t,s)&&s.id===a)return r.push(s),r}else{if(o[2])return O.apply(r,t.getElementsByTagName(e)),r;if((a=o[3])&&n.getElementsByClassName&&t.getElementsByClassName)return O.apply(r,t.getElementsByClassName(a)),r}if(n.qsa&&(!d||!d.test(e))){if(m=g=v,x=t,w=9===u&&e,1===u&&"object"!==t.nodeName.toLowerCase()){f=gt(e),(g=t.getAttribute("id"))?m=g.replace(tt,"\\$&"):t.setAttribute("id",m),m="[id='"+m+"'] ",l=f.length;while(l--)f[l]=m+mt(f[l]);x=U.test(e)&&t.parentNode||t,w=f.join(",")}if(w)try{return O.apply(r,x.querySelectorAll(w)),r}catch(T){}finally{g||t.removeAttribute("id")}}}return kt(e.replace(z,"$1"),t,r,i)}function st(){var e=[];function t(n,r){return e.push(n+=" ")>i.cacheLength&&delete t[e.shift()],t[n]=r}return t}function at(e){return e[v]=!0,e}function ut(e){var t=p.createElement("div");try{return!!e(t)}catch(n){return!1}finally{t.parentNode&&t.parentNode.removeChild(t),t=null}}function lt(e,t){var n=e.split("|"),r=e.length;while(r--)i.attrHandle[n[r]]=t}function ct(e,t){var n=t&&e,r=n&&1===e.nodeType&&1===t.nodeType&&(~t.sourceIndex||D)-(~e.sourceIndex||D);if(r)return r;if(n)while(n=n.nextSibling)if(n===t)return-1;return e?1:-1}function pt(e){return function(t){var n=t.nodeName.toLowerCase();return"input"===n&&t.type===e}}function ft(e){return function(t){var n=t.nodeName.toLowerCase();return("input"===n||"button"===n)&&t.type===e}}function ht(e){return at(function(t){return t=+t,at(function(n,r){var i,o=e([],n.length,t),s=o.length;while(s--)n[i=o[s]]&&(n[i]=!(r[i]=n[i]))})})}s=ot.isXML=function(e){var t=e&&(e.ownerDocument||e).documentElement;return t?"HTML"!==t.nodeName:!1},n=ot.support={},c=ot.setDocument=function(e){var t=e?e.ownerDocument||e:b,r=t.defaultView;return t!==p&&9===t.nodeType&&t.documentElement?(p=t,f=t.documentElement,h=!s(t),r&&r.attachEvent&&r!==r.top&&r.attachEvent("onbeforeunload",function(){c()}),n.attributes=ut(function(e){return e.className="i",!e.getAttribute("className")}),n.getElementsByTagName=ut(function(e){return e.appendChild(t.createComment("")),!e.getElementsByTagName("*").length}),n.getElementsByClassName=ut(function(e){return e.innerHTML="<div class='a'></div><div class='a i'></div>",e.firstChild.className="i",2===e.getElementsByClassName("i").length}),n.getById=ut(function(e){return f.appendChild(e).id=v,!t.getElementsByName||!t.getElementsByName(v).length}),n.getById?(i.find.ID=function(e,t){if(typeof t.getElementById!==j&&h){var n=t.getElementById(e);return n&&n.parentNode?[n]:[]}},i.filter.ID=function(e){var t=e.replace(nt,rt);return function(e){return e.getAttribute("id")===t}}):(delete i.find.ID,i.filter.ID=function(e){var t=e.replace(nt,rt);return function(e){var n=typeof e.getAttributeNode!==j&&e.getAttributeNode("id");return n&&n.value===t}}),i.find.TAG=n.getElementsByTagName?function(e,t){return typeof t.getElementsByTagName!==j?t.getElementsByTagName(e):undefined}:function(e,t){var n,r=[],i=0,o=t.getElementsByTagName(e);if("*"===e){while(n=o[i++])1===n.nodeType&&r.push(n);return r}return o},i.find.CLASS=n.getElementsByClassName&&function(e,t){return typeof t.getElementsByClassName!==j&&h?t.getElementsByClassName(e):undefined},g=[],d=[],(n.qsa=Q.test(t.querySelectorAll))&&(ut(function(e){e.innerHTML="<select><option selected=''></option></select>",e.querySelectorAll("[selected]").length||d.push("\\["+M+"*(?:value|"+R+")"),e.querySelectorAll(":checked").length||d.push(":checked")}),ut(function(e){var n=t.createElement("input");n.setAttribute("type","hidden"),e.appendChild(n).setAttribute("t",""),e.querySelectorAll("[t^='']").length&&d.push("[*^$]="+M+"*(?:''|\"\")"),e.querySelectorAll(":enabled").length||d.push(":enabled",":disabled"),e.querySelectorAll("*,:x"),d.push(",.*:")})),(n.matchesSelector=Q.test(m=f.webkitMatchesSelector||f.mozMatchesSelector||f.oMatchesSelector||f.msMatchesSelector))&&ut(function(e){n.disconnectedMatch=m.call(e,"div"),m.call(e,"[s!='']:x"),g.push("!=",I)}),d=d.length&&RegExp(d.join("|")),g=g.length&&RegExp(g.join("|")),y=Q.test(f.contains)||f.compareDocumentPosition?function(e,t){var n=9===e.nodeType?e.documentElement:e,r=t&&t.parentNode;return e===r||!(!r||1!==r.nodeType||!(n.contains?n.contains(r):e.compareDocumentPosition&&16&e.compareDocumentPosition(r)))}:function(e,t){if(t)while(t=t.parentNode)if(t===e)return!0;return!1},S=f.compareDocumentPosition?function(e,r){if(e===r)return E=!0,0;var i=r.compareDocumentPosition&&e.compareDocumentPosition&&e.compareDocumentPosition(r);return i?1&i||!n.sortDetached&&r.compareDocumentPosition(e)===i?e===t||y(b,e)?-1:r===t||y(b,r)?1:l?P.call(l,e)-P.call(l,r):0:4&i?-1:1:e.compareDocumentPosition?-1:1}:function(e,n){var r,i=0,o=e.parentNode,s=n.parentNode,a=[e],u=[n];if(e===n)return E=!0,0;if(!o||!s)return e===t?-1:n===t?1:o?-1:s?1:l?P.call(l,e)-P.call(l,n):0;if(o===s)return ct(e,n);r=e;while(r=r.parentNode)a.unshift(r);r=n;while(r=r.parentNode)u.unshift(r);while(a[i]===u[i])i++;return i?ct(a[i],u[i]):a[i]===b?-1:u[i]===b?1:0},t):p},ot.matches=function(e,t){return ot(e,null,null,t)},ot.matchesSelector=function(e,t){if((e.ownerDocument||e)!==p&&c(e),t=t.replace(Y,"='$1']"),!(!n.matchesSelector||!h||g&&g.test(t)||d&&d.test(t)))try{var r=m.call(e,t);if(r||n.disconnectedMatch||e.document&&11!==e.document.nodeType)return r}catch(i){}return ot(t,p,null,[e]).length>0},ot.contains=function(e,t){return(e.ownerDocument||e)!==p&&c(e),y(e,t)},ot.attr=function(e,t){(e.ownerDocument||e)!==p&&c(e);var r=i.attrHandle[t.toLowerCase()],o=r&&A.call(i.attrHandle,t.toLowerCase())?r(e,t,!h):undefined;return o===undefined?n.attributes||!h?e.getAttribute(t):(o=e.getAttributeNode(t))&&o.specified?o.value:null:o},ot.error=function(e){throw Error("Syntax error, unrecognized expression: "+e)},ot.uniqueSort=function(e){var t,r=[],i=0,o=0;if(E=!n.detectDuplicates,l=!n.sortStable&&e.slice(0),e.sort(S),E){while(t=e[o++])t===e[o]&&(i=r.push(o));while(i--)e.splice(r[i],1)}return e},o=ot.getText=function(e){var t,n="",r=0,i=e.nodeType;if(i){if(1===i||9===i||11===i){if("string"==typeof e.textContent)return e.textContent;for(e=e.firstChild;e;e=e.nextSibling)n+=o(e)}else if(3===i||4===i)return e.nodeValue}else for(;t=e[r];r++)n+=o(t);return n},i=ot.selectors={cacheLength:50,createPseudo:at,match:J,attrHandle:{},find:{},relative:{">":{dir:"parentNode",first:!0}," ":{dir:"parentNode"},"+":{dir:"previousSibling",first:!0},"~":{dir:"previousSibling"}},preFilter:{ATTR:function(e){return e[1]=e[1].replace(nt,rt),e[3]=(e[4]||e[5]||"").replace(nt,rt),"~="===e[2]&&(e[3]=" "+e[3]+" "),e.slice(0,4)},CHILD:function(e){return e[1]=e[1].toLowerCase(),"nth"===e[1].slice(0,3)?(e[3]||ot.error(e[0]),e[4]=+(e[4]?e[5]+(e[6]||1):2*("even"===e[3]||"odd"===e[3])),e[5]=+(e[7]+e[8]||"odd"===e[3])):e[3]&&ot.error(e[0]),e},PSEUDO:function(e){var t,n=!e[5]&&e[2];return J.CHILD.test(e[0])?null:(e[3]&&e[4]!==undefined?e[2]=e[4]:n&&V.test(n)&&(t=gt(n,!0))&&(t=n.indexOf(")",n.length-t)-n.length)&&(e[0]=e[0].slice(0,t),e[2]=n.slice(0,t)),e.slice(0,3))}},filter:{TAG:function(e){var t=e.replace(nt,rt).toLowerCase();return"*"===e?function(){return!0}:function(e){return e.nodeName&&e.nodeName.toLowerCase()===t}},CLASS:function(e){var t=C[e+" "];return t||(t=RegExp("(^|"+M+")"+e+"("+M+"|$)"))&&C(e,function(e){return t.test("string"==typeof e.className&&e.className||typeof e.getAttribute!==j&&e.getAttribute("class")||"")})},ATTR:function(e,t,n){return function(r){var i=ot.attr(r,e);return null==i?"!="===t:t?(i+="","="===t?i===n:"!="===t?i!==n:"^="===t?n&&0===i.indexOf(n):"*="===t?n&&i.indexOf(n)>-1:"$="===t?n&&i.slice(-n.length)===n:"~="===t?(" "+i+" ").indexOf(n)>-1:"|="===t?i===n||i.slice(0,n.length+1)===n+"-":!1):!0}},CHILD:function(e,t,n,r,i){var o="nth"!==e.slice(0,3),s="last"!==e.slice(-4),a="of-type"===t;return 1===r&&0===i?function(e){return!!e.parentNode}:function(t,n,u){var l,c,p,f,h,d,g=o!==s?"nextSibling":"previousSibling",m=t.parentNode,y=a&&t.nodeName.toLowerCase(),x=!u&&!a;if(m){if(o){while(g){p=t;while(p=p[g])if(a?p.nodeName.toLowerCase()===y:1===p.nodeType)return!1;d=g="only"===e&&!d&&"nextSibling"}return!0}if(d=[s?m.firstChild:m.lastChild],s&&x){c=m[v]||(m[v]={}),l=c[e]||[],h=l[0]===w&&l[1],f=l[0]===w&&l[2],p=h&&m.childNodes[h];while(p=++h&&p&&p[g]||(f=h=0)||d.pop())if(1===p.nodeType&&++f&&p===t){c[e]=[w,h,f];break}}else if(x&&(l=(t[v]||(t[v]={}))[e])&&l[0]===w)f=l[1];else while(p=++h&&p&&p[g]||(f=h=0)||d.pop())if((a?p.nodeName.toLowerCase()===y:1===p.nodeType)&&++f&&(x&&((p[v]||(p[v]={}))[e]=[w,f]),p===t))break;return f-=i,f===r||0===f%r&&f/r>=0}}},PSEUDO:function(e,t){var n,r=i.pseudos[e]||i.setFilters[e.toLowerCase()]||ot.error("unsupported pseudo: "+e);return r[v]?r(t):r.length>1?(n=[e,e,"",t],i.setFilters.hasOwnProperty(e.toLowerCase())?at(function(e,n){var i,o=r(e,t),s=o.length;while(s--)i=P.call(e,o[s]),e[i]=!(n[i]=o[s])}):function(e){return r(e,0,n)}):r}},pseudos:{not:at(function(e){var t=[],n=[],r=a(e.replace(z,"$1"));return r[v]?at(function(e,t,n,i){var o,s=r(e,null,i,[]),a=e.length;while(a--)(o=s[a])&&(e[a]=!(t[a]=o))}):function(e,i,o){return t[0]=e,r(t,null,o,n),!n.pop()}}),has:at(function(e){return function(t){return ot(e,t).length>0}}),contains:at(function(e){return function(t){return(t.textContent||t.innerText||o(t)).indexOf(e)>-1}}),lang:at(function(e){return G.test(e||"")||ot.error("unsupported lang: "+e),e=e.replace(nt,rt).toLowerCase(),function(t){var n;do if(n=h?t.lang:t.getAttribute("xml:lang")||t.getAttribute("lang"))return n=n.toLowerCase(),n===e||0===n.indexOf(e+"-");while((t=t.parentNode)&&1===t.nodeType);return!1}}),target:function(t){var n=e.location&&e.location.hash;return n&&n.slice(1)===t.id},root:function(e){return e===f},focus:function(e){return e===p.activeElement&&(!p.hasFocus||p.hasFocus())&&!!(e.type||e.href||~e.tabIndex)},enabled:function(e){return e.disabled===!1},disabled:function(e){return e.disabled===!0},checked:function(e){var t=e.nodeName.toLowerCase();return"input"===t&&!!e.checked||"option"===t&&!!e.selected},selected:function(e){return e.parentNode&&e.parentNode.selectedIndex,e.selected===!0},empty:function(e){for(e=e.firstChild;e;e=e.nextSibling)if(e.nodeName>"@"||3===e.nodeType||4===e.nodeType)return!1;return!0},parent:function(e){return!i.pseudos.empty(e)},header:function(e){return et.test(e.nodeName)},input:function(e){return Z.test(e.nodeName)},button:function(e){var t=e.nodeName.toLowerCase();return"input"===t&&"button"===e.type||"button"===t},text:function(e){var t;return"input"===e.nodeName.toLowerCase()&&"text"===e.type&&(null==(t=e.getAttribute("type"))||t.toLowerCase()===e.type)},first:ht(function(){return[0]}),last:ht(function(e,t){return[t-1]}),eq:ht(function(e,t,n){return[0>n?n+t:n]}),even:ht(function(e,t){var n=0;for(;t>n;n+=2)e.push(n);return e}),odd:ht(function(e,t){var n=1;for(;t>n;n+=2)e.push(n);return e}),lt:ht(function(e,t,n){var r=0>n?n+t:n;for(;--r>=0;)e.push(r);return e}),gt:ht(function(e,t,n){var r=0>n?n+t:n;for(;t>++r;)e.push(r);return e})}},i.pseudos.nth=i.pseudos.eq;for(t in{radio:!0,checkbox:!0,file:!0,password:!0,image:!0})i.pseudos[t]=pt(t);for(t in{submit:!0,reset:!0})i.pseudos[t]=ft(t);function dt(){}dt.prototype=i.filters=i.pseudos,i.setFilters=new dt;function gt(e,t){var n,r,o,s,a,u,l,c=k[e+" "];if(c)return t?0:c.slice(0);a=e,u=[],l=i.preFilter;while(a){(!n||(r=_.exec(a)))&&(r&&(a=a.slice(r[0].length)||a),u.push(o=[])),n=!1,(r=X.exec(a))&&(n=r.shift(),o.push({value:n,type:r[0].replace(z," ")}),a=a.slice(n.length));for(s in i.filter)!(r=J[s].exec(a))||l[s]&&!(r=l[s](r))||(n=r.shift(),o.push({value:n,type:s,matches:r}),a=a.slice(n.length));if(!n)break}return t?a.length:a?ot.error(e):k(e,u).slice(0)}function mt(e){var t=0,n=e.length,r="";for(;n>t;t++)r+=e[t].value;return r}function yt(e,t,n){var i=t.dir,o=n&&"parentNode"===i,s=T++;return t.first?function(t,n,r){while(t=t[i])if(1===t.nodeType||o)return e(t,n,r)}:function(t,n,a){var u,l,c,p=w+" "+s;if(a){while(t=t[i])if((1===t.nodeType||o)&&e(t,n,a))return!0}else while(t=t[i])if(1===t.nodeType||o)if(c=t[v]||(t[v]={}),(l=c[i])&&l[0]===p){if((u=l[1])===!0||u===r)return u===!0}else if(l=c[i]=[p],l[1]=e(t,n,a)||r,l[1]===!0)return!0}}function vt(e){return e.length>1?function(t,n,r){var i=e.length;while(i--)if(!e[i](t,n,r))return!1;return!0}:e[0]}function xt(e,t,n,r,i){var o,s=[],a=0,u=e.length,l=null!=t;for(;u>a;a++)(o=e[a])&&(!n||n(o,r,i))&&(s.push(o),l&&t.push(a));return s}function bt(e,t,n,r,i,o){return r&&!r[v]&&(r=bt(r)),i&&!i[v]&&(i=bt(i,o)),at(function(o,s,a,u){var l,c,p,f=[],h=[],d=s.length,g=o||Ct(t||"*",a.nodeType?[a]:a,[]),m=!e||!o&&t?g:xt(g,f,e,a,u),y=n?i||(o?e:d||r)?[]:s:m;if(n&&n(m,y,a,u),r){l=xt(y,h),r(l,[],a,u),c=l.length;while(c--)(p=l[c])&&(y[h[c]]=!(m[h[c]]=p))}if(o){if(i||e){if(i){l=[],c=y.length;while(c--)(p=y[c])&&l.push(m[c]=p);i(null,y=[],l,u)}c=y.length;while(c--)(p=y[c])&&(l=i?P.call(o,p):f[c])>-1&&(o[l]=!(s[l]=p))}}else y=xt(y===s?y.splice(d,y.length):y),i?i(null,s,y,u):O.apply(s,y)})}function wt(e){var t,n,r,o=e.length,s=i.relative[e[0].type],a=s||i.relative[" "],l=s?1:0,c=yt(function(e){return e===t},a,!0),p=yt(function(e){return P.call(t,e)>-1},a,!0),f=[function(e,n,r){return!s&&(r||n!==u)||((t=n).nodeType?c(e,n,r):p(e,n,r))}];for(;o>l;l++)if(n=i.relative[e[l].type])f=[yt(vt(f),n)];else{if(n=i.filter[e[l].type].apply(null,e[l].matches),n[v]){for(r=++l;o>r;r++)if(i.relative[e[r].type])break;return bt(l>1&&vt(f),l>1&&mt(e.slice(0,l-1).concat({value:" "===e[l-2].type?"*":""})).replace(z,"$1"),n,r>l&&wt(e.slice(l,r)),o>r&&wt(e=e.slice(r)),o>r&&mt(e))}f.push(n)}return vt(f)}function Tt(e,t){var n=0,o=t.length>0,s=e.length>0,a=function(a,l,c,f,h){var d,g,m,y=[],v=0,x="0",b=a&&[],T=null!=h,C=u,k=a||s&&i.find.TAG("*",h&&l.parentNode||l),N=w+=null==C?1:Math.random()||.1;for(T&&(u=l!==p&&l,r=n);null!=(d=k[x]);x++){if(s&&d){g=0;while(m=e[g++])if(m(d,l,c)){f.push(d);break}T&&(w=N,r=++n)}o&&((d=!m&&d)&&v--,a&&b.push(d))}if(v+=x,o&&x!==v){g=0;while(m=t[g++])m(b,y,l,c);if(a){if(v>0)while(x--)b[x]||y[x]||(y[x]=q.call(f));y=xt(y)}O.apply(f,y),T&&!a&&y.length>0&&v+t.length>1&&ot.uniqueSort(f)}return T&&(w=N,u=C),b};return o?at(a):a}a=ot.compile=function(e,t){var n,r=[],i=[],o=N[e+" "];if(!o){t||(t=gt(e)),n=t.length;while(n--)o=wt(t[n]),o[v]?r.push(o):i.push(o);o=N(e,Tt(i,r))}return o};function Ct(e,t,n){var r=0,i=t.length;for(;i>r;r++)ot(e,t[r],n);return n}function kt(e,t,r,o){var s,u,l,c,p,f=gt(e);if(!o&&1===f.length){if(u=f[0]=f[0].slice(0),u.length>2&&"ID"===(l=u[0]).type&&n.getById&&9===t.nodeType&&h&&i.relative[u[1].type]){if(t=(i.find.ID(l.matches[0].replace(nt,rt),t)||[])[0],!t)return r;e=e.slice(u.shift().value.length)}s=J.needsContext.test(e)?0:u.length;while(s--){if(l=u[s],i.relative[c=l.type])break;if((p=i.find[c])&&(o=p(l.matches[0].replace(nt,rt),U.test(u[0].type)&&t.parentNode||t))){if(u.splice(s,1),e=o.length&&mt(u),!e)return O.apply(r,o),r;break}}}return a(e,f)(o,t,!h,r,U.test(e)),r}n.sortStable=v.split("").sort(S).join("")===v,n.detectDuplicates=E,c(),n.sortDetached=ut(function(e){return 1&e.compareDocumentPosition(p.createElement("div"))}),ut(function(e){return e.innerHTML="<a href='#'></a>","#"===e.firstChild.getAttribute("href")})||lt("type|href|height|width",function(e,t,n){return n?undefined:e.getAttribute(t,"type"===t.toLowerCase()?1:2)}),n.attributes&&ut(function(e){return e.innerHTML="<input/>",e.firstChild.setAttribute("value",""),""===e.firstChild.getAttribute("value")})||lt("value",function(e,t,n){return n||"input"!==e.nodeName.toLowerCase()?undefined:e.defaultValue}),ut(function(e){return null==e.getAttribute("disabled")})||lt(R,function(e,t,n){var r;return n?undefined:(r=e.getAttributeNode(t))&&r.specified?r.value:e[t]===!0?t.toLowerCase():null}),x.find=ot,x.expr=ot.selectors,x.expr[":"]=x.expr.pseudos,x.unique=ot.uniqueSort,x.text=ot.getText,x.isXMLDoc=ot.isXML,x.contains=ot.contains}(e);var D={};function A(e){var t=D[e]={};return x.each(e.match(w)||[],function(e,n){t[n]=!0}),t}x.Callbacks=function(e){e="string"==typeof e?D[e]||A(e):x.extend({},e);var t,n,r,i,o,s,a=[],u=!e.once&&[],l=function(p){for(t=e.memory&&p,n=!0,s=i||0,i=0,o=a.length,r=!0;a&&o>s;s++)if(a[s].apply(p[0],p[1])===!1&&e.stopOnFalse){t=!1;break}r=!1,a&&(u?u.length&&l(u.shift()):t?a=[]:c.disable())},c={add:function(){if(a){var n=a.length;(function s(t){x.each(t,function(t,n){var r=x.type(n);"function"===r?e.unique&&c.has(n)||a.push(n):n&&n.length&&"string"!==r&&s(n)})})(arguments),r?o=a.length:t&&(i=n,l(t))}return this},remove:function(){return a&&x.each(arguments,function(e,t){var n;while((n=x.inArray(t,a,n))>-1)a.splice(n,1),r&&(o>=n&&o--,s>=n&&s--)}),this},has:function(e){return e?x.inArray(e,a)>-1:!(!a||!a.length)},empty:function(){return a=[],o=0,this},disable:function(){return a=u=t=undefined,this},disabled:function(){return!a},lock:function(){return u=undefined,t||c.disable(),this},locked:function(){return!u},fireWith:function(e,t){return!a||n&&!u||(t=t||[],t=[e,t.slice?t.slice():t],r?u.push(t):l(t)),this},fire:function(){return c.fireWith(this,arguments),this},fired:function(){return!!n}};return c},x.extend({Deferred:function(e){var t=[["resolve","done",x.Callbacks("once memory"),"resolved"],["reject","fail",x.Callbacks("once memory"),"rejected"],["notify","progress",x.Callbacks("memory")]],n="pending",r={state:function(){return n},always:function(){return i.done(arguments).fail(arguments),this},then:function(){var e=arguments;return x.Deferred(function(n){x.each(t,function(t,o){var s=o[0],a=x.isFunction(e[t])&&e[t];i[o[1]](function(){var e=a&&a.apply(this,arguments);e&&x.isFunction(e.promise)?e.promise().done(n.resolve).fail(n.reject).progress(n.notify):n[s+"With"](this===r?n.promise():this,a?[e]:arguments)})}),e=null}).promise()},promise:function(e){return null!=e?x.extend(e,r):r}},i={};return r.pipe=r.then,x.each(t,function(e,o){var s=o[2],a=o[3];r[o[1]]=s.add,a&&s.add(function(){n=a},t[1^e][2].disable,t[2][2].lock),i[o[0]]=function(){return i[o[0]+"With"](this===i?r:this,arguments),this},i[o[0]+"With"]=s.fireWith}),r.promise(i),e&&e.call(i,i),i},when:function(e){var t=0,n=d.call(arguments),r=n.length,i=1!==r||e&&x.isFunction(e.promise)?r:0,o=1===i?e:x.Deferred(),s=function(e,t,n){return function(r){t[e]=this,n[e]=arguments.length>1?d.call(arguments):r,n===a?o.notifyWith(t,n):--i||o.resolveWith(t,n)}},a,u,l;if(r>1)for(a=Array(r),u=Array(r),l=Array(r);r>t;t++)n[t]&&x.isFunction(n[t].promise)?n[t].promise().done(s(t,l,n)).fail(o.reject).progress(s(t,u,a)):--i;return i||o.resolveWith(l,n),o.promise()}}),x.support=function(t){var n=o.createElement("input"),r=o.createDocumentFragment(),i=o.createElement("div"),s=o.createElement("select"),a=s.appendChild(o.createElement("option"));return n.type?(n.type="checkbox",t.checkOn=""!==n.value,t.optSelected=a.selected,t.reliableMarginRight=!0,t.boxSizingReliable=!0,t.pixelPosition=!1,n.checked=!0,t.noCloneChecked=n.cloneNode(!0).checked,s.disabled=!0,t.optDisabled=!a.disabled,n=o.createElement("input"),n.value="t",n.type="radio",t.radioValue="t"===n.value,n.setAttribute("checked","t"),n.setAttribute("name","t"),r.appendChild(n),t.checkClone=r.cloneNode(!0).cloneNode(!0).lastChild.checked,t.focusinBubbles="onfocusin"in e,i.style.backgroundClip="content-box",i.cloneNode(!0).style.backgroundClip="",t.clearCloneStyle="content-box"===i.style.backgroundClip,x(function(){var n,r,s="padding:0;margin:0;border:0;display:block;-webkit-box-sizing:content-box;-moz-box-sizing:content-box;box-sizing:content-box",a=o.getElementsByTagName("body")[0];a&&(n=o.createElement("div"),n.style.cssText="border:0;width:0;height:0;position:absolute;top:0;left:-9999px;margin-top:1px",a.appendChild(n).appendChild(i),i.innerHTML="",i.style.cssText="-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;padding:1px;border:1px;display:block;width:4px;margin-top:1%;position:absolute;top:1%",x.swap(a,null!=a.style.zoom?{zoom:1}:{},function(){t.boxSizing=4===i.offsetWidth}),e.getComputedStyle&&(t.pixelPosition="1%"!==(e.getComputedStyle(i,null)||{}).top,t.boxSizingReliable="4px"===(e.getComputedStyle(i,null)||{width:"4px"}).width,r=i.appendChild(o.createElement("div")),r.style.cssText=i.style.cssText=s,r.style.marginRight=r.style.width="0",i.style.width="1px",t.reliableMarginRight=!parseFloat((e.getComputedStyle(r,null)||{}).marginRight)),a.removeChild(n))}),t):t}({});var L,q,H=/(?:\{[\s\S]*\}|\[[\s\S]*\])$/,O=/([A-Z])/g;function F(){Object.defineProperty(this.cache={},0,{get:function(){return{}}}),this.expando=x.expando+Math.random()}F.uid=1,F.accepts=function(e){return e.nodeType?1===e.nodeType||9===e.nodeType:!0},F.prototype={key:function(e){if(!F.accepts(e))return 0;var t={},n=e[this.expando];if(!n){n=F.uid++;try{t[this.expando]={value:n},Object.defineProperties(e,t)}catch(r){t[this.expando]=n,x.extend(e,t)}}return this.cache[n]||(this.cache[n]={}),n},set:function(e,t,n){var r,i=this.key(e),o=this.cache[i];if("string"==typeof t)o[t]=n;else if(x.isEmptyObject(o))x.extend(this.cache[i],t);else for(r in t)o[r]=t[r];return o},get:function(e,t){var n=this.cache[this.key(e)];return t===undefined?n:n[t]},access:function(e,t,n){var r;return t===undefined||t&&"string"==typeof t&&n===undefined?(r=this.get(e,t),r!==undefined?r:this.get(e,x.camelCase(t))):(this.set(e,t,n),n!==undefined?n:t)},remove:function(e,t){var n,r,i,o=this.key(e),s=this.cache[o];if(t===undefined)this.cache[o]={};else{x.isArray(t)?r=t.concat(t.map(x.camelCase)):(i=x.camelCase(t),t in s?r=[t,i]:(r=i,r=r in s?[r]:r.match(w)||[])),n=r.length;while(n--)delete s[r[n]]}},hasData:function(e){return!x.isEmptyObject(this.cache[e[this.expando]]||{})},discard:function(e){e[this.expando]&&delete this.cache[e[this.expando]]}},L=new F,q=new F,x.extend({acceptData:F.accepts,hasData:function(e){return L.hasData(e)||q.hasData(e)},data:function(e,t,n){return L.access(e,t,n)},removeData:function(e,t){L.remove(e,t)},_data:function(e,t,n){return q.access(e,t,n)},_removeData:function(e,t){q.remove(e,t)}}),x.fn.extend({data:function(e,t){var n,r,i=this[0],o=0,s=null;if(e===undefined){if(this.length&&(s=L.get(i),1===i.nodeType&&!q.get(i,"hasDataAttrs"))){for(n=i.attributes;n.length>o;o++)r=n[o].name,0===r.indexOf("data-")&&(r=x.camelCase(r.slice(5)),P(i,r,s[r]));q.set(i,"hasDataAttrs",!0)}return s}return"object"==typeof e?this.each(function(){L.set(this,e)}):x.access(this,function(t){var n,r=x.camelCase(e);if(i&&t===undefined){if(n=L.get(i,e),n!==undefined)return n;if(n=L.get(i,r),n!==undefined)return n;if(n=P(i,r,undefined),n!==undefined)return n}else this.each(function(){var n=L.get(this,r);L.set(this,r,t),-1!==e.indexOf("-")&&n!==undefined&&L.set(this,e,t)})},null,t,arguments.length>1,null,!0)},removeData:function(e){return this.each(function(){L.remove(this,e)})}});function P(e,t,n){var r;if(n===undefined&&1===e.nodeType)if(r="data-"+t.replace(O,"-$1").toLowerCase(),n=e.getAttribute(r),"string"==typeof n){try{n="true"===n?!0:"false"===n?!1:"null"===n?null:+n+""===n?+n:H.test(n)?JSON.parse(n):n}catch(i){}L.set(e,t,n)}else n=undefined;return n}x.extend({queue:function(e,t,n){var r;return e?(t=(t||"fx")+"queue",r=q.get(e,t),n&&(!r||x.isArray(n)?r=q.access(e,t,x.makeArray(n)):r.push(n)),r||[]):undefined},dequeue:function(e,t){t=t||"fx";var n=x.queue(e,t),r=n.length,i=n.shift(),o=x._queueHooks(e,t),s=function(){x.dequeue(e,t)
};"inprogress"===i&&(i=n.shift(),r--),i&&("fx"===t&&n.unshift("inprogress"),delete o.stop,i.call(e,s,o)),!r&&o&&o.empty.fire()},_queueHooks:function(e,t){var n=t+"queueHooks";return q.get(e,n)||q.access(e,n,{empty:x.Callbacks("once memory").add(function(){q.remove(e,[t+"queue",n])})})}}),x.fn.extend({queue:function(e,t){var n=2;return"string"!=typeof e&&(t=e,e="fx",n--),n>arguments.length?x.queue(this[0],e):t===undefined?this:this.each(function(){var n=x.queue(this,e,t);x._queueHooks(this,e),"fx"===e&&"inprogress"!==n[0]&&x.dequeue(this,e)})},dequeue:function(e){return this.each(function(){x.dequeue(this,e)})},delay:function(e,t){return e=x.fx?x.fx.speeds[e]||e:e,t=t||"fx",this.queue(t,function(t,n){var r=setTimeout(t,e);n.stop=function(){clearTimeout(r)}})},clearQueue:function(e){return this.queue(e||"fx",[])},promise:function(e,t){var n,r=1,i=x.Deferred(),o=this,s=this.length,a=function(){--r||i.resolveWith(o,[o])};"string"!=typeof e&&(t=e,e=undefined),e=e||"fx";while(s--)n=q.get(o[s],e+"queueHooks"),n&&n.empty&&(r++,n.empty.add(a));return a(),i.promise(t)}});var R,M,W=/[\t\r\n\f]/g,$=/\r/g,B=/^(?:input|select|textarea|button)$/i;x.fn.extend({attr:function(e,t){return x.access(this,x.attr,e,t,arguments.length>1)},removeAttr:function(e){return this.each(function(){x.removeAttr(this,e)})},prop:function(e,t){return x.access(this,x.prop,e,t,arguments.length>1)},removeProp:function(e){return this.each(function(){delete this[x.propFix[e]||e]})},addClass:function(e){var t,n,r,i,o,s=0,a=this.length,u="string"==typeof e&&e;if(x.isFunction(e))return this.each(function(t){x(this).addClass(e.call(this,t,this.className))});if(u)for(t=(e||"").match(w)||[];a>s;s++)if(n=this[s],r=1===n.nodeType&&(n.className?(" "+n.className+" ").replace(W," "):" ")){o=0;while(i=t[o++])0>r.indexOf(" "+i+" ")&&(r+=i+" ");n.className=x.trim(r)}return this},removeClass:function(e){var t,n,r,i,o,s=0,a=this.length,u=0===arguments.length||"string"==typeof e&&e;if(x.isFunction(e))return this.each(function(t){x(this).removeClass(e.call(this,t,this.className))});if(u)for(t=(e||"").match(w)||[];a>s;s++)if(n=this[s],r=1===n.nodeType&&(n.className?(" "+n.className+" ").replace(W," "):"")){o=0;while(i=t[o++])while(r.indexOf(" "+i+" ")>=0)r=r.replace(" "+i+" "," ");n.className=e?x.trim(r):""}return this},toggleClass:function(e,t){var n=typeof e;return"boolean"==typeof t&&"string"===n?t?this.addClass(e):this.removeClass(e):x.isFunction(e)?this.each(function(n){x(this).toggleClass(e.call(this,n,this.className,t),t)}):this.each(function(){if("string"===n){var t,i=0,o=x(this),s=e.match(w)||[];while(t=s[i++])o.hasClass(t)?o.removeClass(t):o.addClass(t)}else(n===r||"boolean"===n)&&(this.className&&q.set(this,"__className__",this.className),this.className=this.className||e===!1?"":q.get(this,"__className__")||"")})},hasClass:function(e){var t=" "+e+" ",n=0,r=this.length;for(;r>n;n++)if(1===this[n].nodeType&&(" "+this[n].className+" ").replace(W," ").indexOf(t)>=0)return!0;return!1},val:function(e){var t,n,r,i=this[0];{if(arguments.length)return r=x.isFunction(e),this.each(function(n){var i;1===this.nodeType&&(i=r?e.call(this,n,x(this).val()):e,null==i?i="":"number"==typeof i?i+="":x.isArray(i)&&(i=x.map(i,function(e){return null==e?"":e+""})),t=x.valHooks[this.type]||x.valHooks[this.nodeName.toLowerCase()],t&&"set"in t&&t.set(this,i,"value")!==undefined||(this.value=i))});if(i)return t=x.valHooks[i.type]||x.valHooks[i.nodeName.toLowerCase()],t&&"get"in t&&(n=t.get(i,"value"))!==undefined?n:(n=i.value,"string"==typeof n?n.replace($,""):null==n?"":n)}}}),x.extend({valHooks:{option:{get:function(e){var t=e.attributes.value;return!t||t.specified?e.value:e.text}},select:{get:function(e){var t,n,r=e.options,i=e.selectedIndex,o="select-one"===e.type||0>i,s=o?null:[],a=o?i+1:r.length,u=0>i?a:o?i:0;for(;a>u;u++)if(n=r[u],!(!n.selected&&u!==i||(x.support.optDisabled?n.disabled:null!==n.getAttribute("disabled"))||n.parentNode.disabled&&x.nodeName(n.parentNode,"optgroup"))){if(t=x(n).val(),o)return t;s.push(t)}return s},set:function(e,t){var n,r,i=e.options,o=x.makeArray(t),s=i.length;while(s--)r=i[s],(r.selected=x.inArray(x(r).val(),o)>=0)&&(n=!0);return n||(e.selectedIndex=-1),o}}},attr:function(e,t,n){var i,o,s=e.nodeType;if(e&&3!==s&&8!==s&&2!==s)return typeof e.getAttribute===r?x.prop(e,t,n):(1===s&&x.isXMLDoc(e)||(t=t.toLowerCase(),i=x.attrHooks[t]||(x.expr.match.bool.test(t)?M:R)),n===undefined?i&&"get"in i&&null!==(o=i.get(e,t))?o:(o=x.find.attr(e,t),null==o?undefined:o):null!==n?i&&"set"in i&&(o=i.set(e,n,t))!==undefined?o:(e.setAttribute(t,n+""),n):(x.removeAttr(e,t),undefined))},removeAttr:function(e,t){var n,r,i=0,o=t&&t.match(w);if(o&&1===e.nodeType)while(n=o[i++])r=x.propFix[n]||n,x.expr.match.bool.test(n)&&(e[r]=!1),e.removeAttribute(n)},attrHooks:{type:{set:function(e,t){if(!x.support.radioValue&&"radio"===t&&x.nodeName(e,"input")){var n=e.value;return e.setAttribute("type",t),n&&(e.value=n),t}}}},propFix:{"for":"htmlFor","class":"className"},prop:function(e,t,n){var r,i,o,s=e.nodeType;if(e&&3!==s&&8!==s&&2!==s)return o=1!==s||!x.isXMLDoc(e),o&&(t=x.propFix[t]||t,i=x.propHooks[t]),n!==undefined?i&&"set"in i&&(r=i.set(e,n,t))!==undefined?r:e[t]=n:i&&"get"in i&&null!==(r=i.get(e,t))?r:e[t]},propHooks:{tabIndex:{get:function(e){return e.hasAttribute("tabindex")||B.test(e.nodeName)||e.href?e.tabIndex:-1}}}}),M={set:function(e,t,n){return t===!1?x.removeAttr(e,n):e.setAttribute(n,n),n}},x.each(x.expr.match.bool.source.match(/\w+/g),function(e,t){var n=x.expr.attrHandle[t]||x.find.attr;x.expr.attrHandle[t]=function(e,t,r){var i=x.expr.attrHandle[t],o=r?undefined:(x.expr.attrHandle[t]=undefined)!=n(e,t,r)?t.toLowerCase():null;return x.expr.attrHandle[t]=i,o}}),x.support.optSelected||(x.propHooks.selected={get:function(e){var t=e.parentNode;return t&&t.parentNode&&t.parentNode.selectedIndex,null}}),x.each(["tabIndex","readOnly","maxLength","cellSpacing","cellPadding","rowSpan","colSpan","useMap","frameBorder","contentEditable"],function(){x.propFix[this.toLowerCase()]=this}),x.each(["radio","checkbox"],function(){x.valHooks[this]={set:function(e,t){return x.isArray(t)?e.checked=x.inArray(x(e).val(),t)>=0:undefined}},x.support.checkOn||(x.valHooks[this].get=function(e){return null===e.getAttribute("value")?"on":e.value})});var I=/^key/,z=/^(?:mouse|contextmenu)|click/,_=/^(?:focusinfocus|focusoutblur)$/,X=/^([^.]*)(?:\.(.+)|)$/;function U(){return!0}function Y(){return!1}function V(){try{return o.activeElement}catch(e){}}x.event={global:{},add:function(e,t,n,i,o){var s,a,u,l,c,p,f,h,d,g,m,y=q.get(e);if(y){n.handler&&(s=n,n=s.handler,o=s.selector),n.guid||(n.guid=x.guid++),(l=y.events)||(l=y.events={}),(a=y.handle)||(a=y.handle=function(e){return typeof x===r||e&&x.event.triggered===e.type?undefined:x.event.dispatch.apply(a.elem,arguments)},a.elem=e),t=(t||"").match(w)||[""],c=t.length;while(c--)u=X.exec(t[c])||[],d=m=u[1],g=(u[2]||"").split(".").sort(),d&&(f=x.event.special[d]||{},d=(o?f.delegateType:f.bindType)||d,f=x.event.special[d]||{},p=x.extend({type:d,origType:m,data:i,handler:n,guid:n.guid,selector:o,needsContext:o&&x.expr.match.needsContext.test(o),namespace:g.join(".")},s),(h=l[d])||(h=l[d]=[],h.delegateCount=0,f.setup&&f.setup.call(e,i,g,a)!==!1||e.addEventListener&&e.addEventListener(d,a,!1)),f.add&&(f.add.call(e,p),p.handler.guid||(p.handler.guid=n.guid)),o?h.splice(h.delegateCount++,0,p):h.push(p),x.event.global[d]=!0);e=null}},remove:function(e,t,n,r,i){var o,s,a,u,l,c,p,f,h,d,g,m=q.hasData(e)&&q.get(e);if(m&&(u=m.events)){t=(t||"").match(w)||[""],l=t.length;while(l--)if(a=X.exec(t[l])||[],h=g=a[1],d=(a[2]||"").split(".").sort(),h){p=x.event.special[h]||{},h=(r?p.delegateType:p.bindType)||h,f=u[h]||[],a=a[2]&&RegExp("(^|\\.)"+d.join("\\.(?:.*\\.|)")+"(\\.|$)"),s=o=f.length;while(o--)c=f[o],!i&&g!==c.origType||n&&n.guid!==c.guid||a&&!a.test(c.namespace)||r&&r!==c.selector&&("**"!==r||!c.selector)||(f.splice(o,1),c.selector&&f.delegateCount--,p.remove&&p.remove.call(e,c));s&&!f.length&&(p.teardown&&p.teardown.call(e,d,m.handle)!==!1||x.removeEvent(e,h,m.handle),delete u[h])}else for(h in u)x.event.remove(e,h+t[l],n,r,!0);x.isEmptyObject(u)&&(delete m.handle,q.remove(e,"events"))}},trigger:function(t,n,r,i){var s,a,u,l,c,p,f,h=[r||o],d=y.call(t,"type")?t.type:t,g=y.call(t,"namespace")?t.namespace.split("."):[];if(a=u=r=r||o,3!==r.nodeType&&8!==r.nodeType&&!_.test(d+x.event.triggered)&&(d.indexOf(".")>=0&&(g=d.split("."),d=g.shift(),g.sort()),c=0>d.indexOf(":")&&"on"+d,t=t[x.expando]?t:new x.Event(d,"object"==typeof t&&t),t.isTrigger=i?2:3,t.namespace=g.join("."),t.namespace_re=t.namespace?RegExp("(^|\\.)"+g.join("\\.(?:.*\\.|)")+"(\\.|$)"):null,t.result=undefined,t.target||(t.target=r),n=null==n?[t]:x.makeArray(n,[t]),f=x.event.special[d]||{},i||!f.trigger||f.trigger.apply(r,n)!==!1)){if(!i&&!f.noBubble&&!x.isWindow(r)){for(l=f.delegateType||d,_.test(l+d)||(a=a.parentNode);a;a=a.parentNode)h.push(a),u=a;u===(r.ownerDocument||o)&&h.push(u.defaultView||u.parentWindow||e)}s=0;while((a=h[s++])&&!t.isPropagationStopped())t.type=s>1?l:f.bindType||d,p=(q.get(a,"events")||{})[t.type]&&q.get(a,"handle"),p&&p.apply(a,n),p=c&&a[c],p&&x.acceptData(a)&&p.apply&&p.apply(a,n)===!1&&t.preventDefault();return t.type=d,i||t.isDefaultPrevented()||f._default&&f._default.apply(h.pop(),n)!==!1||!x.acceptData(r)||c&&x.isFunction(r[d])&&!x.isWindow(r)&&(u=r[c],u&&(r[c]=null),x.event.triggered=d,r[d](),x.event.triggered=undefined,u&&(r[c]=u)),t.result}},dispatch:function(e){e=x.event.fix(e);var t,n,r,i,o,s=[],a=d.call(arguments),u=(q.get(this,"events")||{})[e.type]||[],l=x.event.special[e.type]||{};if(a[0]=e,e.delegateTarget=this,!l.preDispatch||l.preDispatch.call(this,e)!==!1){s=x.event.handlers.call(this,e,u),t=0;while((i=s[t++])&&!e.isPropagationStopped()){e.currentTarget=i.elem,n=0;while((o=i.handlers[n++])&&!e.isImmediatePropagationStopped())(!e.namespace_re||e.namespace_re.test(o.namespace))&&(e.handleObj=o,e.data=o.data,r=((x.event.special[o.origType]||{}).handle||o.handler).apply(i.elem,a),r!==undefined&&(e.result=r)===!1&&(e.preventDefault(),e.stopPropagation()))}return l.postDispatch&&l.postDispatch.call(this,e),e.result}},handlers:function(e,t){var n,r,i,o,s=[],a=t.delegateCount,u=e.target;if(a&&u.nodeType&&(!e.button||"click"!==e.type))for(;u!==this;u=u.parentNode||this)if(u.disabled!==!0||"click"!==e.type){for(r=[],n=0;a>n;n++)o=t[n],i=o.selector+" ",r[i]===undefined&&(r[i]=o.needsContext?x(i,this).index(u)>=0:x.find(i,this,null,[u]).length),r[i]&&r.push(o);r.length&&s.push({elem:u,handlers:r})}return t.length>a&&s.push({elem:this,handlers:t.slice(a)}),s},props:"altKey bubbles cancelable ctrlKey currentTarget eventPhase metaKey relatedTarget shiftKey target timeStamp view which".split(" "),fixHooks:{},keyHooks:{props:"char charCode key keyCode".split(" "),filter:function(e,t){return null==e.which&&(e.which=null!=t.charCode?t.charCode:t.keyCode),e}},mouseHooks:{props:"button buttons clientX clientY offsetX offsetY pageX pageY screenX screenY toElement".split(" "),filter:function(e,t){var n,r,i,s=t.button;return null==e.pageX&&null!=t.clientX&&(n=e.target.ownerDocument||o,r=n.documentElement,i=n.body,e.pageX=t.clientX+(r&&r.scrollLeft||i&&i.scrollLeft||0)-(r&&r.clientLeft||i&&i.clientLeft||0),e.pageY=t.clientY+(r&&r.scrollTop||i&&i.scrollTop||0)-(r&&r.clientTop||i&&i.clientTop||0)),e.which||s===undefined||(e.which=1&s?1:2&s?3:4&s?2:0),e}},fix:function(e){if(e[x.expando])return e;var t,n,r,i=e.type,s=e,a=this.fixHooks[i];a||(this.fixHooks[i]=a=z.test(i)?this.mouseHooks:I.test(i)?this.keyHooks:{}),r=a.props?this.props.concat(a.props):this.props,e=new x.Event(s),t=r.length;while(t--)n=r[t],e[n]=s[n];return e.target||(e.target=o),3===e.target.nodeType&&(e.target=e.target.parentNode),a.filter?a.filter(e,s):e},special:{load:{noBubble:!0},focus:{trigger:function(){return this!==V()&&this.focus?(this.focus(),!1):undefined},delegateType:"focusin"},blur:{trigger:function(){return this===V()&&this.blur?(this.blur(),!1):undefined},delegateType:"focusout"},click:{trigger:function(){return"checkbox"===this.type&&this.click&&x.nodeName(this,"input")?(this.click(),!1):undefined},_default:function(e){return x.nodeName(e.target,"a")}},beforeunload:{postDispatch:function(e){e.result!==undefined&&(e.originalEvent.returnValue=e.result)}}},simulate:function(e,t,n,r){var i=x.extend(new x.Event,n,{type:e,isSimulated:!0,originalEvent:{}});r?x.event.trigger(i,null,t):x.event.dispatch.call(t,i),i.isDefaultPrevented()&&n.preventDefault()}},x.removeEvent=function(e,t,n){e.removeEventListener&&e.removeEventListener(t,n,!1)},x.Event=function(e,t){return this instanceof x.Event?(e&&e.type?(this.originalEvent=e,this.type=e.type,this.isDefaultPrevented=e.defaultPrevented||e.getPreventDefault&&e.getPreventDefault()?U:Y):this.type=e,t&&x.extend(this,t),this.timeStamp=e&&e.timeStamp||x.now(),this[x.expando]=!0,undefined):new x.Event(e,t)},x.Event.prototype={isDefaultPrevented:Y,isPropagationStopped:Y,isImmediatePropagationStopped:Y,preventDefault:function(){var e=this.originalEvent;this.isDefaultPrevented=U,e&&e.preventDefault&&e.preventDefault()},stopPropagation:function(){var e=this.originalEvent;this.isPropagationStopped=U,e&&e.stopPropagation&&e.stopPropagation()},stopImmediatePropagation:function(){this.isImmediatePropagationStopped=U,this.stopPropagation()}},x.each({mouseenter:"mouseover",mouseleave:"mouseout"},function(e,t){x.event.special[e]={delegateType:t,bindType:t,handle:function(e){var n,r=this,i=e.relatedTarget,o=e.handleObj;return(!i||i!==r&&!x.contains(r,i))&&(e.type=o.origType,n=o.handler.apply(this,arguments),e.type=t),n}}}),x.support.focusinBubbles||x.each({focus:"focusin",blur:"focusout"},function(e,t){var n=0,r=function(e){x.event.simulate(t,e.target,x.event.fix(e),!0)};x.event.special[t]={setup:function(){0===n++&&o.addEventListener(e,r,!0)},teardown:function(){0===--n&&o.removeEventListener(e,r,!0)}}}),x.fn.extend({on:function(e,t,n,r,i){var o,s;if("object"==typeof e){"string"!=typeof t&&(n=n||t,t=undefined);for(s in e)this.on(s,t,n,e[s],i);return this}if(null==n&&null==r?(r=t,n=t=undefined):null==r&&("string"==typeof t?(r=n,n=undefined):(r=n,n=t,t=undefined)),r===!1)r=Y;else if(!r)return this;return 1===i&&(o=r,r=function(e){return x().off(e),o.apply(this,arguments)},r.guid=o.guid||(o.guid=x.guid++)),this.each(function(){x.event.add(this,e,r,n,t)})},one:function(e,t,n,r){return this.on(e,t,n,r,1)},off:function(e,t,n){var r,i;if(e&&e.preventDefault&&e.handleObj)return r=e.handleObj,x(e.delegateTarget).off(r.namespace?r.origType+"."+r.namespace:r.origType,r.selector,r.handler),this;if("object"==typeof e){for(i in e)this.off(i,t,e[i]);return this}return(t===!1||"function"==typeof t)&&(n=t,t=undefined),n===!1&&(n=Y),this.each(function(){x.event.remove(this,e,n,t)})},trigger:function(e,t){return this.each(function(){x.event.trigger(e,t,this)})},triggerHandler:function(e,t){var n=this[0];return n?x.event.trigger(e,t,n,!0):undefined}});var G=/^.[^:#\[\.,]*$/,J=/^(?:parents|prev(?:Until|All))/,Q=x.expr.match.needsContext,K={children:!0,contents:!0,next:!0,prev:!0};x.fn.extend({find:function(e){var t,n=[],r=this,i=r.length;if("string"!=typeof e)return this.pushStack(x(e).filter(function(){for(t=0;i>t;t++)if(x.contains(r[t],this))return!0}));for(t=0;i>t;t++)x.find(e,r[t],n);return n=this.pushStack(i>1?x.unique(n):n),n.selector=this.selector?this.selector+" "+e:e,n},has:function(e){var t=x(e,this),n=t.length;return this.filter(function(){var e=0;for(;n>e;e++)if(x.contains(this,t[e]))return!0})},not:function(e){return this.pushStack(et(this,e||[],!0))},filter:function(e){return this.pushStack(et(this,e||[],!1))},is:function(e){return!!et(this,"string"==typeof e&&Q.test(e)?x(e):e||[],!1).length},closest:function(e,t){var n,r=0,i=this.length,o=[],s=Q.test(e)||"string"!=typeof e?x(e,t||this.context):0;for(;i>r;r++)for(n=this[r];n&&n!==t;n=n.parentNode)if(11>n.nodeType&&(s?s.index(n)>-1:1===n.nodeType&&x.find.matchesSelector(n,e))){n=o.push(n);break}return this.pushStack(o.length>1?x.unique(o):o)},index:function(e){return e?"string"==typeof e?g.call(x(e),this[0]):g.call(this,e.jquery?e[0]:e):this[0]&&this[0].parentNode?this.first().prevAll().length:-1},add:function(e,t){var n="string"==typeof e?x(e,t):x.makeArray(e&&e.nodeType?[e]:e),r=x.merge(this.get(),n);return this.pushStack(x.unique(r))},addBack:function(e){return this.add(null==e?this.prevObject:this.prevObject.filter(e))}});function Z(e,t){while((e=e[t])&&1!==e.nodeType);return e}x.each({parent:function(e){var t=e.parentNode;return t&&11!==t.nodeType?t:null},parents:function(e){return x.dir(e,"parentNode")},parentsUntil:function(e,t,n){return x.dir(e,"parentNode",n)},next:function(e){return Z(e,"nextSibling")},prev:function(e){return Z(e,"previousSibling")},nextAll:function(e){return x.dir(e,"nextSibling")},prevAll:function(e){return x.dir(e,"previousSibling")},nextUntil:function(e,t,n){return x.dir(e,"nextSibling",n)},prevUntil:function(e,t,n){return x.dir(e,"previousSibling",n)},siblings:function(e){return x.sibling((e.parentNode||{}).firstChild,e)},children:function(e){return x.sibling(e.firstChild)},contents:function(e){return e.contentDocument||x.merge([],e.childNodes)}},function(e,t){x.fn[e]=function(n,r){var i=x.map(this,t,n);return"Until"!==e.slice(-5)&&(r=n),r&&"string"==typeof r&&(i=x.filter(r,i)),this.length>1&&(K[e]||x.unique(i),J.test(e)&&i.reverse()),this.pushStack(i)}}),x.extend({filter:function(e,t,n){var r=t[0];return n&&(e=":not("+e+")"),1===t.length&&1===r.nodeType?x.find.matchesSelector(r,e)?[r]:[]:x.find.matches(e,x.grep(t,function(e){return 1===e.nodeType}))},dir:function(e,t,n){var r=[],i=n!==undefined;while((e=e[t])&&9!==e.nodeType)if(1===e.nodeType){if(i&&x(e).is(n))break;r.push(e)}return r},sibling:function(e,t){var n=[];for(;e;e=e.nextSibling)1===e.nodeType&&e!==t&&n.push(e);return n}});function et(e,t,n){if(x.isFunction(t))return x.grep(e,function(e,r){return!!t.call(e,r,e)!==n});if(t.nodeType)return x.grep(e,function(e){return e===t!==n});if("string"==typeof t){if(G.test(t))return x.filter(t,e,n);t=x.filter(t,e)}return x.grep(e,function(e){return g.call(t,e)>=0!==n})}var tt=/<(?!area|br|col|embed|hr|img|input|link|meta|param)(([\w:]+)[^>]*)\/>/gi,nt=/<([\w:]+)/,rt=/<|&#?\w+;/,it=/<(?:script|style|link)/i,ot=/^(?:checkbox|radio)$/i,st=/checked\s*(?:[^=]|=\s*.checked.)/i,at=/^$|\/(?:java|ecma)script/i,ut=/^true\/(.*)/,lt=/^\s*<!(?:\[CDATA\[|--)|(?:\]\]|--)>\s*$/g,ct={option:[1,"<select multiple='multiple'>","</select>"],thead:[1,"<table>","</table>"],col:[2,"<table><colgroup>","</colgroup></table>"],tr:[2,"<table><tbody>","</tbody></table>"],td:[3,"<table><tbody><tr>","</tr></tbody></table>"],_default:[0,"",""]};ct.optgroup=ct.option,ct.tbody=ct.tfoot=ct.colgroup=ct.caption=ct.thead,ct.th=ct.td,x.fn.extend({text:function(e){return x.access(this,function(e){return e===undefined?x.text(this):this.empty().append((this[0]&&this[0].ownerDocument||o).createTextNode(e))},null,e,arguments.length)},append:function(){return this.domManip(arguments,function(e){if(1===this.nodeType||11===this.nodeType||9===this.nodeType){var t=pt(this,e);t.appendChild(e)}})},prepend:function(){return this.domManip(arguments,function(e){if(1===this.nodeType||11===this.nodeType||9===this.nodeType){var t=pt(this,e);t.insertBefore(e,t.firstChild)}})},before:function(){return this.domManip(arguments,function(e){this.parentNode&&this.parentNode.insertBefore(e,this)})},after:function(){return this.domManip(arguments,function(e){this.parentNode&&this.parentNode.insertBefore(e,this.nextSibling)})},remove:function(e,t){var n,r=e?x.filter(e,this):this,i=0;for(;null!=(n=r[i]);i++)t||1!==n.nodeType||x.cleanData(mt(n)),n.parentNode&&(t&&x.contains(n.ownerDocument,n)&&dt(mt(n,"script")),n.parentNode.removeChild(n));return this},empty:function(){var e,t=0;for(;null!=(e=this[t]);t++)1===e.nodeType&&(x.cleanData(mt(e,!1)),e.textContent="");return this},clone:function(e,t){return e=null==e?!1:e,t=null==t?e:t,this.map(function(){return x.clone(this,e,t)})},html:function(e){return x.access(this,function(e){var t=this[0]||{},n=0,r=this.length;if(e===undefined&&1===t.nodeType)return t.innerHTML;if("string"==typeof e&&!it.test(e)&&!ct[(nt.exec(e)||["",""])[1].toLowerCase()]){e=e.replace(tt,"<$1></$2>");try{for(;r>n;n++)t=this[n]||{},1===t.nodeType&&(x.cleanData(mt(t,!1)),t.innerHTML=e);t=0}catch(i){}}t&&this.empty().append(e)},null,e,arguments.length)},replaceWith:function(){var e=x.map(this,function(e){return[e.nextSibling,e.parentNode]}),t=0;return this.domManip(arguments,function(n){var r=e[t++],i=e[t++];i&&(r&&r.parentNode!==i&&(r=this.nextSibling),x(this).remove(),i.insertBefore(n,r))},!0),t?this:this.remove()},detach:function(e){return this.remove(e,!0)},domManip:function(e,t,n){e=f.apply([],e);var r,i,o,s,a,u,l=0,c=this.length,p=this,h=c-1,d=e[0],g=x.isFunction(d);if(g||!(1>=c||"string"!=typeof d||x.support.checkClone)&&st.test(d))return this.each(function(r){var i=p.eq(r);g&&(e[0]=d.call(this,r,i.html())),i.domManip(e,t,n)});if(c&&(r=x.buildFragment(e,this[0].ownerDocument,!1,!n&&this),i=r.firstChild,1===r.childNodes.length&&(r=i),i)){for(o=x.map(mt(r,"script"),ft),s=o.length;c>l;l++)a=r,l!==h&&(a=x.clone(a,!0,!0),s&&x.merge(o,mt(a,"script"))),t.call(this[l],a,l);if(s)for(u=o[o.length-1].ownerDocument,x.map(o,ht),l=0;s>l;l++)a=o[l],at.test(a.type||"")&&!q.access(a,"globalEval")&&x.contains(u,a)&&(a.src?x._evalUrl(a.src):x.globalEval(a.textContent.replace(lt,"")))}return this}}),x.each({appendTo:"append",prependTo:"prepend",insertBefore:"before",insertAfter:"after",replaceAll:"replaceWith"},function(e,t){x.fn[e]=function(e){var n,r=[],i=x(e),o=i.length-1,s=0;for(;o>=s;s++)n=s===o?this:this.clone(!0),x(i[s])[t](n),h.apply(r,n.get());return this.pushStack(r)}}),x.extend({clone:function(e,t,n){var r,i,o,s,a=e.cloneNode(!0),u=x.contains(e.ownerDocument,e);if(!(x.support.noCloneChecked||1!==e.nodeType&&11!==e.nodeType||x.isXMLDoc(e)))for(s=mt(a),o=mt(e),r=0,i=o.length;i>r;r++)yt(o[r],s[r]);if(t)if(n)for(o=o||mt(e),s=s||mt(a),r=0,i=o.length;i>r;r++)gt(o[r],s[r]);else gt(e,a);return s=mt(a,"script"),s.length>0&&dt(s,!u&&mt(e,"script")),a},buildFragment:function(e,t,n,r){var i,o,s,a,u,l,c=0,p=e.length,f=t.createDocumentFragment(),h=[];for(;p>c;c++)if(i=e[c],i||0===i)if("object"===x.type(i))x.merge(h,i.nodeType?[i]:i);else if(rt.test(i)){o=o||f.appendChild(t.createElement("div")),s=(nt.exec(i)||["",""])[1].toLowerCase(),a=ct[s]||ct._default,o.innerHTML=a[1]+i.replace(tt,"<$1></$2>")+a[2],l=a[0];while(l--)o=o.lastChild;x.merge(h,o.childNodes),o=f.firstChild,o.textContent=""}else h.push(t.createTextNode(i));f.textContent="",c=0;while(i=h[c++])if((!r||-1===x.inArray(i,r))&&(u=x.contains(i.ownerDocument,i),o=mt(f.appendChild(i),"script"),u&&dt(o),n)){l=0;while(i=o[l++])at.test(i.type||"")&&n.push(i)}return f},cleanData:function(e){var t,n,r,i,o,s,a=x.event.special,u=0;for(;(n=e[u])!==undefined;u++){if(F.accepts(n)&&(o=n[q.expando],o&&(t=q.cache[o]))){if(r=Object.keys(t.events||{}),r.length)for(s=0;(i=r[s])!==undefined;s++)a[i]?x.event.remove(n,i):x.removeEvent(n,i,t.handle);q.cache[o]&&delete q.cache[o]}delete L.cache[n[L.expando]]}},_evalUrl:function(e){return x.ajax({url:e,type:"GET",dataType:"script",async:!1,global:!1,"throws":!0})}});function pt(e,t){return x.nodeName(e,"table")&&x.nodeName(1===t.nodeType?t:t.firstChild,"tr")?e.getElementsByTagName("tbody")[0]||e.appendChild(e.ownerDocument.createElement("tbody")):e}function ft(e){return e.type=(null!==e.getAttribute("type"))+"/"+e.type,e}function ht(e){var t=ut.exec(e.type);return t?e.type=t[1]:e.removeAttribute("type"),e}function dt(e,t){var n=e.length,r=0;for(;n>r;r++)q.set(e[r],"globalEval",!t||q.get(t[r],"globalEval"))}function gt(e,t){var n,r,i,o,s,a,u,l;if(1===t.nodeType){if(q.hasData(e)&&(o=q.access(e),s=q.set(t,o),l=o.events)){delete s.handle,s.events={};for(i in l)for(n=0,r=l[i].length;r>n;n++)x.event.add(t,i,l[i][n])}L.hasData(e)&&(a=L.access(e),u=x.extend({},a),L.set(t,u))}}function mt(e,t){var n=e.getElementsByTagName?e.getElementsByTagName(t||"*"):e.querySelectorAll?e.querySelectorAll(t||"*"):[];return t===undefined||t&&x.nodeName(e,t)?x.merge([e],n):n}function yt(e,t){var n=t.nodeName.toLowerCase();"input"===n&&ot.test(e.type)?t.checked=e.checked:("input"===n||"textarea"===n)&&(t.defaultValue=e.defaultValue)}x.fn.extend({wrapAll:function(e){var t;return x.isFunction(e)?this.each(function(t){x(this).wrapAll(e.call(this,t))}):(this[0]&&(t=x(e,this[0].ownerDocument).eq(0).clone(!0),this[0].parentNode&&t.insertBefore(this[0]),t.map(function(){var e=this;while(e.firstElementChild)e=e.firstElementChild;return e}).append(this)),this)},wrapInner:function(e){return x.isFunction(e)?this.each(function(t){x(this).wrapInner(e.call(this,t))}):this.each(function(){var t=x(this),n=t.contents();n.length?n.wrapAll(e):t.append(e)})},wrap:function(e){var t=x.isFunction(e);return this.each(function(n){x(this).wrapAll(t?e.call(this,n):e)})},unwrap:function(){return this.parent().each(function(){x.nodeName(this,"body")||x(this).replaceWith(this.childNodes)}).end()}});var vt,xt,bt=/^(none|table(?!-c[ea]).+)/,wt=/^margin/,Tt=RegExp("^("+b+")(.*)$","i"),Ct=RegExp("^("+b+")(?!px)[a-z%]+$","i"),kt=RegExp("^([+-])=("+b+")","i"),Nt={BODY:"block"},Et={position:"absolute",visibility:"hidden",display:"block"},St={letterSpacing:0,fontWeight:400},jt=["Top","Right","Bottom","Left"],Dt=["Webkit","O","Moz","ms"];function At(e,t){if(t in e)return t;var n=t.charAt(0).toUpperCase()+t.slice(1),r=t,i=Dt.length;while(i--)if(t=Dt[i]+n,t in e)return t;return r}function Lt(e,t){return e=t||e,"none"===x.css(e,"display")||!x.contains(e.ownerDocument,e)}function qt(t){return e.getComputedStyle(t,null)}function Ht(e,t){var n,r,i,o=[],s=0,a=e.length;for(;a>s;s++)r=e[s],r.style&&(o[s]=q.get(r,"olddisplay"),n=r.style.display,t?(o[s]||"none"!==n||(r.style.display=""),""===r.style.display&&Lt(r)&&(o[s]=q.access(r,"olddisplay",Rt(r.nodeName)))):o[s]||(i=Lt(r),(n&&"none"!==n||!i)&&q.set(r,"olddisplay",i?n:x.css(r,"display"))));for(s=0;a>s;s++)r=e[s],r.style&&(t&&"none"!==r.style.display&&""!==r.style.display||(r.style.display=t?o[s]||"":"none"));return e}x.fn.extend({css:function(e,t){return x.access(this,function(e,t,n){var r,i,o={},s=0;if(x.isArray(t)){for(r=qt(e),i=t.length;i>s;s++)o[t[s]]=x.css(e,t[s],!1,r);return o}return n!==undefined?x.style(e,t,n):x.css(e,t)},e,t,arguments.length>1)},show:function(){return Ht(this,!0)},hide:function(){return Ht(this)},toggle:function(e){return"boolean"==typeof e?e?this.show():this.hide():this.each(function(){Lt(this)?x(this).show():x(this).hide()})}}),x.extend({cssHooks:{opacity:{get:function(e,t){if(t){var n=vt(e,"opacity");return""===n?"1":n}}}},cssNumber:{columnCount:!0,fillOpacity:!0,fontWeight:!0,lineHeight:!0,opacity:!0,order:!0,orphans:!0,widows:!0,zIndex:!0,zoom:!0},cssProps:{"float":"cssFloat"},style:function(e,t,n,r){if(e&&3!==e.nodeType&&8!==e.nodeType&&e.style){var i,o,s,a=x.camelCase(t),u=e.style;return t=x.cssProps[a]||(x.cssProps[a]=At(u,a)),s=x.cssHooks[t]||x.cssHooks[a],n===undefined?s&&"get"in s&&(i=s.get(e,!1,r))!==undefined?i:u[t]:(o=typeof n,"string"===o&&(i=kt.exec(n))&&(n=(i[1]+1)*i[2]+parseFloat(x.css(e,t)),o="number"),null==n||"number"===o&&isNaN(n)||("number"!==o||x.cssNumber[a]||(n+="px"),x.support.clearCloneStyle||""!==n||0!==t.indexOf("background")||(u[t]="inherit"),s&&"set"in s&&(n=s.set(e,n,r))===undefined||(u[t]=n)),undefined)}},css:function(e,t,n,r){var i,o,s,a=x.camelCase(t);return t=x.cssProps[a]||(x.cssProps[a]=At(e.style,a)),s=x.cssHooks[t]||x.cssHooks[a],s&&"get"in s&&(i=s.get(e,!0,n)),i===undefined&&(i=vt(e,t,r)),"normal"===i&&t in St&&(i=St[t]),""===n||n?(o=parseFloat(i),n===!0||x.isNumeric(o)?o||0:i):i}}),vt=function(e,t,n){var r,i,o,s=n||qt(e),a=s?s.getPropertyValue(t)||s[t]:undefined,u=e.style;return s&&(""!==a||x.contains(e.ownerDocument,e)||(a=x.style(e,t)),Ct.test(a)&&wt.test(t)&&(r=u.width,i=u.minWidth,o=u.maxWidth,u.minWidth=u.maxWidth=u.width=a,a=s.width,u.width=r,u.minWidth=i,u.maxWidth=o)),a};function Ot(e,t,n){var r=Tt.exec(t);return r?Math.max(0,r[1]-(n||0))+(r[2]||"px"):t}function Ft(e,t,n,r,i){var o=n===(r?"border":"content")?4:"width"===t?1:0,s=0;for(;4>o;o+=2)"margin"===n&&(s+=x.css(e,n+jt[o],!0,i)),r?("content"===n&&(s-=x.css(e,"padding"+jt[o],!0,i)),"margin"!==n&&(s-=x.css(e,"border"+jt[o]+"Width",!0,i))):(s+=x.css(e,"padding"+jt[o],!0,i),"padding"!==n&&(s+=x.css(e,"border"+jt[o]+"Width",!0,i)));return s}function Pt(e,t,n){var r=!0,i="width"===t?e.offsetWidth:e.offsetHeight,o=qt(e),s=x.support.boxSizing&&"border-box"===x.css(e,"boxSizing",!1,o);if(0>=i||null==i){if(i=vt(e,t,o),(0>i||null==i)&&(i=e.style[t]),Ct.test(i))return i;r=s&&(x.support.boxSizingReliable||i===e.style[t]),i=parseFloat(i)||0}return i+Ft(e,t,n||(s?"border":"content"),r,o)+"px"}function Rt(e){var t=o,n=Nt[e];return n||(n=Mt(e,t),"none"!==n&&n||(xt=(xt||x("<iframe frameborder='0' width='0' height='0'/>").css("cssText","display:block !important")).appendTo(t.documentElement),t=(xt[0].contentWindow||xt[0].contentDocument).document,t.write("<!doctype html><html><body>"),t.close(),n=Mt(e,t),xt.detach()),Nt[e]=n),n}function Mt(e,t){var n=x(t.createElement(e)).appendTo(t.body),r=x.css(n[0],"display");return n.remove(),r}x.each(["height","width"],function(e,t){x.cssHooks[t]={get:function(e,n,r){return n?0===e.offsetWidth&&bt.test(x.css(e,"display"))?x.swap(e,Et,function(){return Pt(e,t,r)}):Pt(e,t,r):undefined},set:function(e,n,r){var i=r&&qt(e);return Ot(e,n,r?Ft(e,t,r,x.support.boxSizing&&"border-box"===x.css(e,"boxSizing",!1,i),i):0)}}}),x(function(){x.support.reliableMarginRight||(x.cssHooks.marginRight={get:function(e,t){return t?x.swap(e,{display:"inline-block"},vt,[e,"marginRight"]):undefined}}),!x.support.pixelPosition&&x.fn.position&&x.each(["top","left"],function(e,t){x.cssHooks[t]={get:function(e,n){return n?(n=vt(e,t),Ct.test(n)?x(e).position()[t]+"px":n):undefined}}})}),x.expr&&x.expr.filters&&(x.expr.filters.hidden=function(e){return 0>=e.offsetWidth&&0>=e.offsetHeight},x.expr.filters.visible=function(e){return!x.expr.filters.hidden(e)}),x.each({margin:"",padding:"",border:"Width"},function(e,t){x.cssHooks[e+t]={expand:function(n){var r=0,i={},o="string"==typeof n?n.split(" "):[n];for(;4>r;r++)i[e+jt[r]+t]=o[r]||o[r-2]||o[0];return i}},wt.test(e)||(x.cssHooks[e+t].set=Ot)});var Wt=/%20/g,$t=/\[\]$/,Bt=/\r?\n/g,It=/^(?:submit|button|image|reset|file)$/i,zt=/^(?:input|select|textarea|keygen)/i;x.fn.extend({serialize:function(){return x.param(this.serializeArray())},serializeArray:function(){return this.map(function(){var e=x.prop(this,"elements");return e?x.makeArray(e):this}).filter(function(){var e=this.type;return this.name&&!x(this).is(":disabled")&&zt.test(this.nodeName)&&!It.test(e)&&(this.checked||!ot.test(e))}).map(function(e,t){var n=x(this).val();return null==n?null:x.isArray(n)?x.map(n,function(e){return{name:t.name,value:e.replace(Bt,"\r\n")}}):{name:t.name,value:n.replace(Bt,"\r\n")}}).get()}}),x.param=function(e,t){var n,r=[],i=function(e,t){t=x.isFunction(t)?t():null==t?"":t,r[r.length]=encodeURIComponent(e)+"="+encodeURIComponent(t)};if(t===undefined&&(t=x.ajaxSettings&&x.ajaxSettings.traditional),x.isArray(e)||e.jquery&&!x.isPlainObject(e))x.each(e,function(){i(this.name,this.value)});else for(n in e)_t(n,e[n],t,i);return r.join("&").replace(Wt,"+")};function _t(e,t,n,r){var i;if(x.isArray(t))x.each(t,function(t,i){n||$t.test(e)?r(e,i):_t(e+"["+("object"==typeof i?t:"")+"]",i,n,r)});else if(n||"object"!==x.type(t))r(e,t);else for(i in t)_t(e+"["+i+"]",t[i],n,r)}x.each("blur focus focusin focusout load resize scroll unload click dblclick mousedown mouseup mousemove mouseover mouseout mouseenter mouseleave change select submit keydown keypress keyup error contextmenu".split(" "),function(e,t){x.fn[t]=function(e,n){return arguments.length>0?this.on(t,null,e,n):this.trigger(t)}}),x.fn.extend({hover:function(e,t){return this.mouseenter(e).mouseleave(t||e)},bind:function(e,t,n){return this.on(e,null,t,n)},unbind:function(e,t){return this.off(e,null,t)
},delegate:function(e,t,n,r){return this.on(t,e,n,r)},undelegate:function(e,t,n){return 1===arguments.length?this.off(e,"**"):this.off(t,e||"**",n)}});var Xt,Ut,Yt=x.now(),Vt=/\?/,Gt=/#.*$/,Jt=/([?&])_=[^&]*/,Qt=/^(.*?):[ \t]*([^\r\n]*)$/gm,Kt=/^(?:about|app|app-storage|.+-extension|file|res|widget):$/,Zt=/^(?:GET|HEAD)$/,en=/^\/\//,tn=/^([\w.+-]+:)(?:\/\/([^\/?#:]*)(?::(\d+)|)|)/,nn=x.fn.load,rn={},on={},sn="*/".concat("*");try{Ut=i.href}catch(an){Ut=o.createElement("a"),Ut.href="",Ut=Ut.href}Xt=tn.exec(Ut.toLowerCase())||[];function un(e){return function(t,n){"string"!=typeof t&&(n=t,t="*");var r,i=0,o=t.toLowerCase().match(w)||[];if(x.isFunction(n))while(r=o[i++])"+"===r[0]?(r=r.slice(1)||"*",(e[r]=e[r]||[]).unshift(n)):(e[r]=e[r]||[]).push(n)}}function ln(e,t,n,r){var i={},o=e===on;function s(a){var u;return i[a]=!0,x.each(e[a]||[],function(e,a){var l=a(t,n,r);return"string"!=typeof l||o||i[l]?o?!(u=l):undefined:(t.dataTypes.unshift(l),s(l),!1)}),u}return s(t.dataTypes[0])||!i["*"]&&s("*")}function cn(e,t){var n,r,i=x.ajaxSettings.flatOptions||{};for(n in t)t[n]!==undefined&&((i[n]?e:r||(r={}))[n]=t[n]);return r&&x.extend(!0,e,r),e}x.fn.load=function(e,t,n){if("string"!=typeof e&&nn)return nn.apply(this,arguments);var r,i,o,s=this,a=e.indexOf(" ");return a>=0&&(r=e.slice(a),e=e.slice(0,a)),x.isFunction(t)?(n=t,t=undefined):t&&"object"==typeof t&&(i="POST"),s.length>0&&x.ajax({url:e,type:i,dataType:"html",data:t}).done(function(e){o=arguments,s.html(r?x("<div>").append(x.parseHTML(e)).find(r):e)}).complete(n&&function(e,t){s.each(n,o||[e.responseText,t,e])}),this},x.each(["ajaxStart","ajaxStop","ajaxComplete","ajaxError","ajaxSuccess","ajaxSend"],function(e,t){x.fn[t]=function(e){return this.on(t,e)}}),x.extend({active:0,lastModified:{},etag:{},ajaxSettings:{url:Ut,type:"GET",isLocal:Kt.test(Xt[1]),global:!0,processData:!0,async:!0,contentType:"application/x-www-form-urlencoded; charset=UTF-8",accepts:{"*":sn,text:"text/plain",html:"text/html",xml:"application/xml, text/xml",json:"application/json, text/javascript"},contents:{xml:/xml/,html:/html/,json:/json/},responseFields:{xml:"responseXML",text:"responseText",json:"responseJSON"},converters:{"* text":String,"text html":!0,"text json":x.parseJSON,"text xml":x.parseXML},flatOptions:{url:!0,context:!0}},ajaxSetup:function(e,t){return t?cn(cn(e,x.ajaxSettings),t):cn(x.ajaxSettings,e)},ajaxPrefilter:un(rn),ajaxTransport:un(on),ajax:function(e,t){"object"==typeof e&&(t=e,e=undefined),t=t||{};var n,r,i,o,s,a,u,l,c=x.ajaxSetup({},t),p=c.context||c,f=c.context&&(p.nodeType||p.jquery)?x(p):x.event,h=x.Deferred(),d=x.Callbacks("once memory"),g=c.statusCode||{},m={},y={},v=0,b="canceled",T={readyState:0,getResponseHeader:function(e){var t;if(2===v){if(!o){o={};while(t=Qt.exec(i))o[t[1].toLowerCase()]=t[2]}t=o[e.toLowerCase()]}return null==t?null:t},getAllResponseHeaders:function(){return 2===v?i:null},setRequestHeader:function(e,t){var n=e.toLowerCase();return v||(e=y[n]=y[n]||e,m[e]=t),this},overrideMimeType:function(e){return v||(c.mimeType=e),this},statusCode:function(e){var t;if(e)if(2>v)for(t in e)g[t]=[g[t],e[t]];else T.always(e[T.status]);return this},abort:function(e){var t=e||b;return n&&n.abort(t),k(0,t),this}};if(h.promise(T).complete=d.add,T.success=T.done,T.error=T.fail,c.url=((e||c.url||Ut)+"").replace(Gt,"").replace(en,Xt[1]+"//"),c.type=t.method||t.type||c.method||c.type,c.dataTypes=x.trim(c.dataType||"*").toLowerCase().match(w)||[""],null==c.crossDomain&&(a=tn.exec(c.url.toLowerCase()),c.crossDomain=!(!a||a[1]===Xt[1]&&a[2]===Xt[2]&&(a[3]||("http:"===a[1]?"80":"443"))===(Xt[3]||("http:"===Xt[1]?"80":"443")))),c.data&&c.processData&&"string"!=typeof c.data&&(c.data=x.param(c.data,c.traditional)),ln(rn,c,t,T),2===v)return T;u=c.global,u&&0===x.active++&&x.event.trigger("ajaxStart"),c.type=c.type.toUpperCase(),c.hasContent=!Zt.test(c.type),r=c.url,c.hasContent||(c.data&&(r=c.url+=(Vt.test(r)?"&":"?")+c.data,delete c.data),c.cache===!1&&(c.url=Jt.test(r)?r.replace(Jt,"$1_="+Yt++):r+(Vt.test(r)?"&":"?")+"_="+Yt++)),c.ifModified&&(x.lastModified[r]&&T.setRequestHeader("If-Modified-Since",x.lastModified[r]),x.etag[r]&&T.setRequestHeader("If-None-Match",x.etag[r])),(c.data&&c.hasContent&&c.contentType!==!1||t.contentType)&&T.setRequestHeader("Content-Type",c.contentType),T.setRequestHeader("Accept",c.dataTypes[0]&&c.accepts[c.dataTypes[0]]?c.accepts[c.dataTypes[0]]+("*"!==c.dataTypes[0]?", "+sn+"; q=0.01":""):c.accepts["*"]);for(l in c.headers)T.setRequestHeader(l,c.headers[l]);if(c.beforeSend&&(c.beforeSend.call(p,T,c)===!1||2===v))return T.abort();b="abort";for(l in{success:1,error:1,complete:1})T[l](c[l]);if(n=ln(on,c,t,T)){T.readyState=1,u&&f.trigger("ajaxSend",[T,c]),c.async&&c.timeout>0&&(s=setTimeout(function(){T.abort("timeout")},c.timeout));try{v=1,n.send(m,k)}catch(C){if(!(2>v))throw C;k(-1,C)}}else k(-1,"No Transport");function k(e,t,o,a){var l,m,y,b,w,C=t;2!==v&&(v=2,s&&clearTimeout(s),n=undefined,i=a||"",T.readyState=e>0?4:0,l=e>=200&&300>e||304===e,o&&(b=pn(c,T,o)),b=fn(c,b,T,l),l?(c.ifModified&&(w=T.getResponseHeader("Last-Modified"),w&&(x.lastModified[r]=w),w=T.getResponseHeader("etag"),w&&(x.etag[r]=w)),204===e||"HEAD"===c.type?C="nocontent":304===e?C="notmodified":(C=b.state,m=b.data,y=b.error,l=!y)):(y=C,(e||!C)&&(C="error",0>e&&(e=0))),T.status=e,T.statusText=(t||C)+"",l?h.resolveWith(p,[m,C,T]):h.rejectWith(p,[T,C,y]),T.statusCode(g),g=undefined,u&&f.trigger(l?"ajaxSuccess":"ajaxError",[T,c,l?m:y]),d.fireWith(p,[T,C]),u&&(f.trigger("ajaxComplete",[T,c]),--x.active||x.event.trigger("ajaxStop")))}return T},getJSON:function(e,t,n){return x.get(e,t,n,"json")},getScript:function(e,t){return x.get(e,undefined,t,"script")}}),x.each(["get","post"],function(e,t){x[t]=function(e,n,r,i){return x.isFunction(n)&&(i=i||r,r=n,n=undefined),x.ajax({url:e,type:t,dataType:i,data:n,success:r})}});function pn(e,t,n){var r,i,o,s,a=e.contents,u=e.dataTypes;while("*"===u[0])u.shift(),r===undefined&&(r=e.mimeType||t.getResponseHeader("Content-Type"));if(r)for(i in a)if(a[i]&&a[i].test(r)){u.unshift(i);break}if(u[0]in n)o=u[0];else{for(i in n){if(!u[0]||e.converters[i+" "+u[0]]){o=i;break}s||(s=i)}o=o||s}return o?(o!==u[0]&&u.unshift(o),n[o]):undefined}function fn(e,t,n,r){var i,o,s,a,u,l={},c=e.dataTypes.slice();if(c[1])for(s in e.converters)l[s.toLowerCase()]=e.converters[s];o=c.shift();while(o)if(e.responseFields[o]&&(n[e.responseFields[o]]=t),!u&&r&&e.dataFilter&&(t=e.dataFilter(t,e.dataType)),u=o,o=c.shift())if("*"===o)o=u;else if("*"!==u&&u!==o){if(s=l[u+" "+o]||l["* "+o],!s)for(i in l)if(a=i.split(" "),a[1]===o&&(s=l[u+" "+a[0]]||l["* "+a[0]])){s===!0?s=l[i]:l[i]!==!0&&(o=a[0],c.unshift(a[1]));break}if(s!==!0)if(s&&e["throws"])t=s(t);else try{t=s(t)}catch(p){return{state:"parsererror",error:s?p:"No conversion from "+u+" to "+o}}}return{state:"success",data:t}}x.ajaxSetup({accepts:{script:"text/javascript, application/javascript, application/ecmascript, application/x-ecmascript"},contents:{script:/(?:java|ecma)script/},converters:{"text script":function(e){return x.globalEval(e),e}}}),x.ajaxPrefilter("script",function(e){e.cache===undefined&&(e.cache=!1),e.crossDomain&&(e.type="GET")}),x.ajaxTransport("script",function(e){if(e.crossDomain){var t,n;return{send:function(r,i){t=x("<script>").prop({async:!0,charset:e.scriptCharset,src:e.url}).on("load error",n=function(e){t.remove(),n=null,e&&i("error"===e.type?404:200,e.type)}),o.head.appendChild(t[0])},abort:function(){n&&n()}}}});var hn=[],dn=/(=)\?(?=&|$)|\?\?/;x.ajaxSetup({jsonp:"callback",jsonpCallback:function(){var e=hn.pop()||x.expando+"_"+Yt++;return this[e]=!0,e}}),x.ajaxPrefilter("json jsonp",function(t,n,r){var i,o,s,a=t.jsonp!==!1&&(dn.test(t.url)?"url":"string"==typeof t.data&&!(t.contentType||"").indexOf("application/x-www-form-urlencoded")&&dn.test(t.data)&&"data");return a||"jsonp"===t.dataTypes[0]?(i=t.jsonpCallback=x.isFunction(t.jsonpCallback)?t.jsonpCallback():t.jsonpCallback,a?t[a]=t[a].replace(dn,"$1"+i):t.jsonp!==!1&&(t.url+=(Vt.test(t.url)?"&":"?")+t.jsonp+"="+i),t.converters["script json"]=function(){return s||x.error(i+" was not called"),s[0]},t.dataTypes[0]="json",o=e[i],e[i]=function(){s=arguments},r.always(function(){e[i]=o,t[i]&&(t.jsonpCallback=n.jsonpCallback,hn.push(i)),s&&x.isFunction(o)&&o(s[0]),s=o=undefined}),"script"):undefined}),x.ajaxSettings.xhr=function(){try{return new XMLHttpRequest}catch(e){}};var gn=x.ajaxSettings.xhr(),mn={0:200,1223:204},yn=0,vn={};e.ActiveXObject&&x(e).on("unload",function(){for(var e in vn)vn[e]();vn=undefined}),x.support.cors=!!gn&&"withCredentials"in gn,x.support.ajax=gn=!!gn,x.ajaxTransport(function(e){var t;return x.support.cors||gn&&!e.crossDomain?{send:function(n,r){var i,o,s=e.xhr();if(s.open(e.type,e.url,e.async,e.username,e.password),e.xhrFields)for(i in e.xhrFields)s[i]=e.xhrFields[i];e.mimeType&&s.overrideMimeType&&s.overrideMimeType(e.mimeType),e.crossDomain||n["X-Requested-With"]||(n["X-Requested-With"]="XMLHttpRequest");for(i in n)s.setRequestHeader(i,n[i]);t=function(e){return function(){t&&(delete vn[o],t=s.onload=s.onerror=null,"abort"===e?s.abort():"error"===e?r(s.status||404,s.statusText):r(mn[s.status]||s.status,s.statusText,"string"==typeof s.responseText?{text:s.responseText}:undefined,s.getAllResponseHeaders()))}},s.onload=t(),s.onerror=t("error"),t=vn[o=yn++]=t("abort"),s.send(e.hasContent&&e.data||null)},abort:function(){t&&t()}}:undefined});var xn,bn,wn=/^(?:toggle|show|hide)$/,Tn=RegExp("^(?:([+-])=|)("+b+")([a-z%]*)$","i"),Cn=/queueHooks$/,kn=[An],Nn={"*":[function(e,t){var n=this.createTween(e,t),r=n.cur(),i=Tn.exec(t),o=i&&i[3]||(x.cssNumber[e]?"":"px"),s=(x.cssNumber[e]||"px"!==o&&+r)&&Tn.exec(x.css(n.elem,e)),a=1,u=20;if(s&&s[3]!==o){o=o||s[3],i=i||[],s=+r||1;do a=a||".5",s/=a,x.style(n.elem,e,s+o);while(a!==(a=n.cur()/r)&&1!==a&&--u)}return i&&(s=n.start=+s||+r||0,n.unit=o,n.end=i[1]?s+(i[1]+1)*i[2]:+i[2]),n}]};function En(){return setTimeout(function(){xn=undefined}),xn=x.now()}function Sn(e,t,n){var r,i=(Nn[t]||[]).concat(Nn["*"]),o=0,s=i.length;for(;s>o;o++)if(r=i[o].call(n,t,e))return r}function jn(e,t,n){var r,i,o=0,s=kn.length,a=x.Deferred().always(function(){delete u.elem}),u=function(){if(i)return!1;var t=xn||En(),n=Math.max(0,l.startTime+l.duration-t),r=n/l.duration||0,o=1-r,s=0,u=l.tweens.length;for(;u>s;s++)l.tweens[s].run(o);return a.notifyWith(e,[l,o,n]),1>o&&u?n:(a.resolveWith(e,[l]),!1)},l=a.promise({elem:e,props:x.extend({},t),opts:x.extend(!0,{specialEasing:{}},n),originalProperties:t,originalOptions:n,startTime:xn||En(),duration:n.duration,tweens:[],createTween:function(t,n){var r=x.Tween(e,l.opts,t,n,l.opts.specialEasing[t]||l.opts.easing);return l.tweens.push(r),r},stop:function(t){var n=0,r=t?l.tweens.length:0;if(i)return this;for(i=!0;r>n;n++)l.tweens[n].run(1);return t?a.resolveWith(e,[l,t]):a.rejectWith(e,[l,t]),this}}),c=l.props;for(Dn(c,l.opts.specialEasing);s>o;o++)if(r=kn[o].call(l,e,c,l.opts))return r;return x.map(c,Sn,l),x.isFunction(l.opts.start)&&l.opts.start.call(e,l),x.fx.timer(x.extend(u,{elem:e,anim:l,queue:l.opts.queue})),l.progress(l.opts.progress).done(l.opts.done,l.opts.complete).fail(l.opts.fail).always(l.opts.always)}function Dn(e,t){var n,r,i,o,s;for(n in e)if(r=x.camelCase(n),i=t[r],o=e[n],x.isArray(o)&&(i=o[1],o=e[n]=o[0]),n!==r&&(e[r]=o,delete e[n]),s=x.cssHooks[r],s&&"expand"in s){o=s.expand(o),delete e[r];for(n in o)n in e||(e[n]=o[n],t[n]=i)}else t[r]=i}x.Animation=x.extend(jn,{tweener:function(e,t){x.isFunction(e)?(t=e,e=["*"]):e=e.split(" ");var n,r=0,i=e.length;for(;i>r;r++)n=e[r],Nn[n]=Nn[n]||[],Nn[n].unshift(t)},prefilter:function(e,t){t?kn.unshift(e):kn.push(e)}});function An(e,t,n){var r,i,o,s,a,u,l=this,c={},p=e.style,f=e.nodeType&&Lt(e),h=q.get(e,"fxshow");n.queue||(a=x._queueHooks(e,"fx"),null==a.unqueued&&(a.unqueued=0,u=a.empty.fire,a.empty.fire=function(){a.unqueued||u()}),a.unqueued++,l.always(function(){l.always(function(){a.unqueued--,x.queue(e,"fx").length||a.empty.fire()})})),1===e.nodeType&&("height"in t||"width"in t)&&(n.overflow=[p.overflow,p.overflowX,p.overflowY],"inline"===x.css(e,"display")&&"none"===x.css(e,"float")&&(p.display="inline-block")),n.overflow&&(p.overflow="hidden",l.always(function(){p.overflow=n.overflow[0],p.overflowX=n.overflow[1],p.overflowY=n.overflow[2]}));for(r in t)if(i=t[r],wn.exec(i)){if(delete t[r],o=o||"toggle"===i,i===(f?"hide":"show")){if("show"!==i||!h||h[r]===undefined)continue;f=!0}c[r]=h&&h[r]||x.style(e,r)}if(!x.isEmptyObject(c)){h?"hidden"in h&&(f=h.hidden):h=q.access(e,"fxshow",{}),o&&(h.hidden=!f),f?x(e).show():l.done(function(){x(e).hide()}),l.done(function(){var t;q.remove(e,"fxshow");for(t in c)x.style(e,t,c[t])});for(r in c)s=Sn(f?h[r]:0,r,l),r in h||(h[r]=s.start,f&&(s.end=s.start,s.start="width"===r||"height"===r?1:0))}}function Ln(e,t,n,r,i){return new Ln.prototype.init(e,t,n,r,i)}x.Tween=Ln,Ln.prototype={constructor:Ln,init:function(e,t,n,r,i,o){this.elem=e,this.prop=n,this.easing=i||"swing",this.options=t,this.start=this.now=this.cur(),this.end=r,this.unit=o||(x.cssNumber[n]?"":"px")},cur:function(){var e=Ln.propHooks[this.prop];return e&&e.get?e.get(this):Ln.propHooks._default.get(this)},run:function(e){var t,n=Ln.propHooks[this.prop];return this.pos=t=this.options.duration?x.easing[this.easing](e,this.options.duration*e,0,1,this.options.duration):e,this.now=(this.end-this.start)*t+this.start,this.options.step&&this.options.step.call(this.elem,this.now,this),n&&n.set?n.set(this):Ln.propHooks._default.set(this),this}},Ln.prototype.init.prototype=Ln.prototype,Ln.propHooks={_default:{get:function(e){var t;return null==e.elem[e.prop]||e.elem.style&&null!=e.elem.style[e.prop]?(t=x.css(e.elem,e.prop,""),t&&"auto"!==t?t:0):e.elem[e.prop]},set:function(e){x.fx.step[e.prop]?x.fx.step[e.prop](e):e.elem.style&&(null!=e.elem.style[x.cssProps[e.prop]]||x.cssHooks[e.prop])?x.style(e.elem,e.prop,e.now+e.unit):e.elem[e.prop]=e.now}}},Ln.propHooks.scrollTop=Ln.propHooks.scrollLeft={set:function(e){e.elem.nodeType&&e.elem.parentNode&&(e.elem[e.prop]=e.now)}},x.each(["toggle","show","hide"],function(e,t){var n=x.fn[t];x.fn[t]=function(e,r,i){return null==e||"boolean"==typeof e?n.apply(this,arguments):this.animate(qn(t,!0),e,r,i)}}),x.fn.extend({fadeTo:function(e,t,n,r){return this.filter(Lt).css("opacity",0).show().end().animate({opacity:t},e,n,r)},animate:function(e,t,n,r){var i=x.isEmptyObject(e),o=x.speed(t,n,r),s=function(){var t=jn(this,x.extend({},e),o);(i||q.get(this,"finish"))&&t.stop(!0)};return s.finish=s,i||o.queue===!1?this.each(s):this.queue(o.queue,s)},stop:function(e,t,n){var r=function(e){var t=e.stop;delete e.stop,t(n)};return"string"!=typeof e&&(n=t,t=e,e=undefined),t&&e!==!1&&this.queue(e||"fx",[]),this.each(function(){var t=!0,i=null!=e&&e+"queueHooks",o=x.timers,s=q.get(this);if(i)s[i]&&s[i].stop&&r(s[i]);else for(i in s)s[i]&&s[i].stop&&Cn.test(i)&&r(s[i]);for(i=o.length;i--;)o[i].elem!==this||null!=e&&o[i].queue!==e||(o[i].anim.stop(n),t=!1,o.splice(i,1));(t||!n)&&x.dequeue(this,e)})},finish:function(e){return e!==!1&&(e=e||"fx"),this.each(function(){var t,n=q.get(this),r=n[e+"queue"],i=n[e+"queueHooks"],o=x.timers,s=r?r.length:0;for(n.finish=!0,x.queue(this,e,[]),i&&i.stop&&i.stop.call(this,!0),t=o.length;t--;)o[t].elem===this&&o[t].queue===e&&(o[t].anim.stop(!0),o.splice(t,1));for(t=0;s>t;t++)r[t]&&r[t].finish&&r[t].finish.call(this);delete n.finish})}});function qn(e,t){var n,r={height:e},i=0;for(t=t?1:0;4>i;i+=2-t)n=jt[i],r["margin"+n]=r["padding"+n]=e;return t&&(r.opacity=r.width=e),r}x.each({slideDown:qn("show"),slideUp:qn("hide"),slideToggle:qn("toggle"),fadeIn:{opacity:"show"},fadeOut:{opacity:"hide"},fadeToggle:{opacity:"toggle"}},function(e,t){x.fn[e]=function(e,n,r){return this.animate(t,e,n,r)}}),x.speed=function(e,t,n){var r=e&&"object"==typeof e?x.extend({},e):{complete:n||!n&&t||x.isFunction(e)&&e,duration:e,easing:n&&t||t&&!x.isFunction(t)&&t};return r.duration=x.fx.off?0:"number"==typeof r.duration?r.duration:r.duration in x.fx.speeds?x.fx.speeds[r.duration]:x.fx.speeds._default,(null==r.queue||r.queue===!0)&&(r.queue="fx"),r.old=r.complete,r.complete=function(){x.isFunction(r.old)&&r.old.call(this),r.queue&&x.dequeue(this,r.queue)},r},x.easing={linear:function(e){return e},swing:function(e){return.5-Math.cos(e*Math.PI)/2}},x.timers=[],x.fx=Ln.prototype.init,x.fx.tick=function(){var e,t=x.timers,n=0;for(xn=x.now();t.length>n;n++)e=t[n],e()||t[n]!==e||t.splice(n--,1);t.length||x.fx.stop(),xn=undefined},x.fx.timer=function(e){e()&&x.timers.push(e)&&x.fx.start()},x.fx.interval=13,x.fx.start=function(){bn||(bn=setInterval(x.fx.tick,x.fx.interval))},x.fx.stop=function(){clearInterval(bn),bn=null},x.fx.speeds={slow:600,fast:200,_default:400},x.fx.step={},x.expr&&x.expr.filters&&(x.expr.filters.animated=function(e){return x.grep(x.timers,function(t){return e===t.elem}).length}),x.fn.offset=function(e){if(arguments.length)return e===undefined?this:this.each(function(t){x.offset.setOffset(this,e,t)});var t,n,i=this[0],o={top:0,left:0},s=i&&i.ownerDocument;if(s)return t=s.documentElement,x.contains(t,i)?(typeof i.getBoundingClientRect!==r&&(o=i.getBoundingClientRect()),n=Hn(s),{top:o.top+n.pageYOffset-t.clientTop,left:o.left+n.pageXOffset-t.clientLeft}):o},x.offset={setOffset:function(e,t,n){var r,i,o,s,a,u,l,c=x.css(e,"position"),p=x(e),f={};"static"===c&&(e.style.position="relative"),a=p.offset(),o=x.css(e,"top"),u=x.css(e,"left"),l=("absolute"===c||"fixed"===c)&&(o+u).indexOf("auto")>-1,l?(r=p.position(),s=r.top,i=r.left):(s=parseFloat(o)||0,i=parseFloat(u)||0),x.isFunction(t)&&(t=t.call(e,n,a)),null!=t.top&&(f.top=t.top-a.top+s),null!=t.left&&(f.left=t.left-a.left+i),"using"in t?t.using.call(e,f):p.css(f)}},x.fn.extend({position:function(){if(this[0]){var e,t,n=this[0],r={top:0,left:0};return"fixed"===x.css(n,"position")?t=n.getBoundingClientRect():(e=this.offsetParent(),t=this.offset(),x.nodeName(e[0],"html")||(r=e.offset()),r.top+=x.css(e[0],"borderTopWidth",!0),r.left+=x.css(e[0],"borderLeftWidth",!0)),{top:t.top-r.top-x.css(n,"marginTop",!0),left:t.left-r.left-x.css(n,"marginLeft",!0)}}},offsetParent:function(){return this.map(function(){var e=this.offsetParent||s;while(e&&!x.nodeName(e,"html")&&"static"===x.css(e,"position"))e=e.offsetParent;return e||s})}}),x.each({scrollLeft:"pageXOffset",scrollTop:"pageYOffset"},function(t,n){var r="pageYOffset"===n;x.fn[t]=function(i){return x.access(this,function(t,i,o){var s=Hn(t);return o===undefined?s?s[n]:t[i]:(s?s.scrollTo(r?e.pageXOffset:o,r?o:e.pageYOffset):t[i]=o,undefined)},t,i,arguments.length,null)}});function Hn(e){return x.isWindow(e)?e:9===e.nodeType&&e.defaultView}x.each({Height:"height",Width:"width"},function(e,t){x.each({padding:"inner"+e,content:t,"":"outer"+e},function(n,r){x.fn[r]=function(r,i){var o=arguments.length&&(n||"boolean"!=typeof r),s=n||(r===!0||i===!0?"margin":"border");return x.access(this,function(t,n,r){var i;return x.isWindow(t)?t.document.documentElement["client"+e]:9===t.nodeType?(i=t.documentElement,Math.max(t.body["scroll"+e],i["scroll"+e],t.body["offset"+e],i["offset"+e],i["client"+e])):r===undefined?x.css(t,n,s):x.style(t,n,r,s)},t,o?r:undefined,o,null)}})}),x.fn.size=function(){return this.length},x.fn.andSelf=x.fn.addBack,"object"==typeof module&&module&&"object"==typeof module.exports?module.exports=x:"function"==typeof define&&define.amd&&define("jquery",[],function(){return x}),"object"==typeof e&&"object"==typeof e.document&&(e.jQuery=e.$=x)})(window);

/*!
 * jQuery Form Plugin
 * version: 3.32.0-2013.04.09
 * @requires jQuery v1.5 or later
 * Copyright (c) 2013 M. Alsup
 * Examples and documentation at: http://malsup.com/jquery/form/
 * Project repository: https://github.com/malsup/form
 * Dual licensed under the MIT and GPL licenses.
 * https://github.com/malsup/form#copyright-and-license
 */
/*global ActiveXObject */
;(function($) {
"use strict";

/*
    Usage Note:
    -----------
    Do not use both ajaxSubmit and ajaxForm on the same form.  These
    functions are mutually exclusive.  Use ajaxSubmit if you want
    to bind your own submit handler to the form.  For example,

    $(document).ready(function() {
        $('#myForm').on('submit', function(e) {
            e.preventDefault(); // <-- important
            $(this).ajaxSubmit({
                target: '#output'
            });
        });
    });

    Use ajaxForm when you want the plugin to manage all the event binding
    for you.  For example,

    $(document).ready(function() {
        $('#myForm').ajaxForm({
            target: '#output'
        });
    });

    You can also use ajaxForm with delegation (requires jQuery v1.7+), so the
    form does not have to exist when you invoke ajaxForm:

    $('#myForm').ajaxForm({
        delegation: true,
        target: '#output'
    });

    When using ajaxForm, the ajaxSubmit function will be invoked for you
    at the appropriate time.
*/

/**
 * Feature detection
 */
var feature = {};
feature.fileapi = $("<input type='file'/>").get(0).files !== undefined;
feature.formdata = window.FormData !== undefined;

var hasProp = !!$.fn.prop;

// attr2 uses prop when it can but checks the return type for
// an expected string.  this accounts for the case where a form 
// contains inputs with names like "action" or "method"; in those
// cases "prop" returns the element
$.fn.attr2 = function() {
    if ( ! hasProp )
        return this.attr.apply(this, arguments);
    var val = this.prop.apply(this, arguments);
    if ( ( val && val.jquery ) || typeof val === 'string' )
        return val;
    return this.attr.apply(this, arguments);
};

/**
 * ajaxSubmit() provides a mechanism for immediately submitting
 * an HTML form using AJAX.
 */
$.fn.ajaxSubmit = function(options) {
    /*jshint scripturl:true */

    // fast fail if nothing selected (http://dev.jquery.com/ticket/2752)
    if (!this.length) {
        log('ajaxSubmit: skipping submit process - no element selected');
        return this;
    }

    var method, action, url, $form = this;

    if (typeof options == 'function') {
        options = { success: options };
    }

    method = this.attr2('method');
    action = this.attr2('action');

    url = (typeof action === 'string') ? $.trim(action) : '';
    url = url || window.location.href || '';
    if (url) {
        // clean url (don't include hash vaue)
        url = (url.match(/^([^#]+)/)||[])[1];
    }

    options = $.extend(true, {
        url:  url,
        success: $.ajaxSettings.success,
        type: method || 'GET',
        iframeSrc: /^https/i.test(window.location.href || '') ? 'javascript:false' : 'about:blank'
    }, options);

    // hook for manipulating the form data before it is extracted;
    // convenient for use with rich editors like tinyMCE or FCKEditor
    var veto = {};
    this.trigger('form-pre-serialize', [this, options, veto]);
    if (veto.veto) {
        log('ajaxSubmit: submit vetoed via form-pre-serialize trigger');
        return this;
    }

    // provide opportunity to alter form data before it is serialized
    if (options.beforeSerialize && options.beforeSerialize(this, options) === false) {
        log('ajaxSubmit: submit aborted via beforeSerialize callback');
        return this;
    }

    var traditional = options.traditional;
    if ( traditional === undefined ) {
        traditional = $.ajaxSettings.traditional;
    }

    var elements = [];
    var qx, a = this.formToArray(options.semantic, elements);
    if (options.data) {
        options.extraData = options.data;
        qx = $.param(options.data, traditional);
    }

    // give pre-submit callback an opportunity to abort the submit
    if (options.beforeSubmit && options.beforeSubmit(a, this, options) === false) {
        log('ajaxSubmit: submit aborted via beforeSubmit callback');
        return this;
    }

    // fire vetoable 'validate' event
    this.trigger('form-submit-validate', [a, this, options, veto]);
    if (veto.veto) {
        log('ajaxSubmit: submit vetoed via form-submit-validate trigger');
        return this;
    }

    var q = $.param(a, traditional);
    if (qx) {
        q = ( q ? (q + '&' + qx) : qx );
    }
    if (options.type.toUpperCase() == 'GET') {
        options.url += (options.url.indexOf('?') >= 0 ? '&' : '?') + q;
        options.data = null;  // data is null for 'get'
    }
    else {
        options.data = q; // data is the query string for 'post'
    }

    var callbacks = [];
    if (options.resetForm) {
        callbacks.push(function() { $form.resetForm(); });
    }
    if (options.clearForm) {
        callbacks.push(function() { $form.clearForm(options.includeHidden); });
    }

    // perform a load on the target only if dataType is not provided
    if (!options.dataType && options.target) {
        var oldSuccess = options.success || function(){};
        callbacks.push(function(data) {
            var fn = options.replaceTarget ? 'replaceWith' : 'html';
            $(options.target)[fn](data).each(oldSuccess, arguments);
        });
    }
    else if (options.success) {
        callbacks.push(options.success);
    }

    options.success = function(data, status, xhr) { // jQuery 1.4+ passes xhr as 3rd arg
        var context = options.context || this ;    // jQuery 1.4+ supports scope context
        for (var i=0, max=callbacks.length; i < max; i++) {
            callbacks[i].apply(context, [data, status, xhr || $form, $form]);
        }
    };

    // are there files to upload?

    // [value] (issue #113), also see comment:
    // https://github.com/malsup/form/commit/588306aedba1de01388032d5f42a60159eea9228#commitcomment-2180219
    var fileInputs = $('input[type=file]:enabled[value!=""]', this);

    var hasFileInputs = fileInputs.length > 0;
    var mp = 'multipart/form-data';
    var multipart = ($form.attr('enctype') == mp || $form.attr('encoding') == mp);

    var fileAPI = feature.fileapi && feature.formdata;
    log("fileAPI :" + fileAPI);
    var shouldUseFrame = (hasFileInputs || multipart) && !fileAPI;

    var jqxhr;

    // options.iframe allows user to force iframe mode
    // 06-NOV-09: now defaulting to iframe mode if file input is detected
    if (options.iframe !== false && (options.iframe || shouldUseFrame)) {
        // hack to fix Safari hang (thanks to Tim Molendijk for this)
        // see:  http://groups.google.com/group/jquery-dev/browse_thread/thread/36395b7ab510dd5d
        if (options.closeKeepAlive) {
            $.get(options.closeKeepAlive, function() {
                jqxhr = fileUploadIframe(a);
            });
        }
        else {
            jqxhr = fileUploadIframe(a);
        }
    }
    else if ((hasFileInputs || multipart) && fileAPI) {
        jqxhr = fileUploadXhr(a);
    }
    else {
        jqxhr = $.ajax(options);
    }

    $form.removeData('jqxhr').data('jqxhr', jqxhr);

    // clear element array
    for (var k=0; k < elements.length; k++)
        elements[k] = null;

    // fire 'notify' event
    this.trigger('form-submit-notify', [this, options]);
    return this;

    // utility fn for deep serialization
    function deepSerialize(extraData){
        var serialized = $.param(extraData).split('&');
        var len = serialized.length;
        var result = [];
        var i, part;
        for (i=0; i < len; i++) {
            // #252; undo param space replacement
            serialized[i] = serialized[i].replace(/\+/g,' ');
            part = serialized[i].split('=');
            // #278; use array instead of object storage, favoring array serializations
            result.push([decodeURIComponent(part[0]), decodeURIComponent(part[1])]);
        }
        return result;
    }

     // XMLHttpRequest Level 2 file uploads (big hat tip to francois2metz)
    function fileUploadXhr(a) {
        var formdata = new FormData();

        for (var i=0; i < a.length; i++) {
            formdata.append(a[i].name, a[i].value);
        }

        if (options.extraData) {
            var serializedData = deepSerialize(options.extraData);
            for (i=0; i < serializedData.length; i++)
                if (serializedData[i])
                    formdata.append(serializedData[i][0], serializedData[i][1]);
        }

        options.data = null;

        var s = $.extend(true, {}, $.ajaxSettings, options, {
            contentType: false,
            processData: false,
            cache: false,
            type: method || 'POST'
        });

        if (options.uploadProgress) {
            // workaround because jqXHR does not expose upload property
            s.xhr = function() {
                var xhr = jQuery.ajaxSettings.xhr();
                if (xhr.upload) {
                    xhr.upload.addEventListener('progress', function(event) {
                        var percent = 0;
                        var position = event.loaded || event.position; /*event.position is deprecated*/
                        var total = event.total;
                        if (event.lengthComputable) {
                            percent = Math.ceil(position / total * 100);
                        }
                        options.uploadProgress(event, position, total, percent);
                    }, false);
                }
                return xhr;
            };
        }

        s.data = null;
            var beforeSend = s.beforeSend;
            s.beforeSend = function(xhr, o) {
                o.data = formdata;
                if(beforeSend)
                    beforeSend.call(this, xhr, o);
        };
        return $.ajax(s);
    }

    // private function for handling file uploads (hat tip to YAHOO!)
    function fileUploadIframe(a) {
        var form = $form[0], el, i, s, g, id, $io, io, xhr, sub, n, timedOut, timeoutHandle;
        var deferred = $.Deferred();

        if (a) {
            // ensure that every serialized input is still enabled
            for (i=0; i < elements.length; i++) {
                el = $(elements[i]);
                if ( hasProp )
                    el.prop('disabled', false);
                else
                    el.removeAttr('disabled');
            }
        }

        s = $.extend(true, {}, $.ajaxSettings, options);
        s.context = s.context || s;
        id = 'jqFormIO' + (new Date().getTime());
        if (s.iframeTarget) {
            $io = $(s.iframeTarget);
            n = $io.attr2('name');
            if (!n)
                 $io.attr2('name', id);
            else
                id = n;
        }
        else {
            $io = $('<iframe name="' + id + '" src="'+ s.iframeSrc +'" />');
            $io.css({ position: 'absolute', top: '-1000px', left: '-1000px' });
        }
        io = $io[0];


        xhr = { // mock object
            aborted: 0,
            responseText: null,
            responseXML: null,
            status: 0,
            statusText: 'n/a',
            getAllResponseHeaders: function() {},
            getResponseHeader: function() {},
            setRequestHeader: function() {},
            abort: function(status) {
                var e = (status === 'timeout' ? 'timeout' : 'aborted');
                log('aborting upload... ' + e);
                this.aborted = 1;

                try { // #214, #257
                    if (io.contentWindow.document.execCommand) {
                        io.contentWindow.document.execCommand('Stop');
                    }
                }
                catch(ignore) {}

                $io.attr('src', s.iframeSrc); // abort op in progress
                xhr.error = e;
                if (s.error)
                    s.error.call(s.context, xhr, e, status);
                if (g)
                    $.event.trigger("ajaxError", [xhr, s, e]);
                if (s.complete)
                    s.complete.call(s.context, xhr, e);
            }
        };

        g = s.global;
        // trigger ajax global events so that activity/block indicators work like normal
        if (g && 0 === $.active++) {
            $.event.trigger("ajaxStart");
        }
        if (g) {
            $.event.trigger("ajaxSend", [xhr, s]);
        }

        if (s.beforeSend && s.beforeSend.call(s.context, xhr, s) === false) {
            if (s.global) {
                $.active--;
            }
            deferred.reject();
            return deferred;
        }
        if (xhr.aborted) {
            deferred.reject();
            return deferred;
        }

        // add submitting element to data if we know it
        sub = form.clk;
        if (sub) {
            n = sub.name;
            if (n && !sub.disabled) {
                s.extraData = s.extraData || {};
                s.extraData[n] = sub.value;
                if (sub.type == "image") {
                    s.extraData[n+'.x'] = form.clk_x;
                    s.extraData[n+'.y'] = form.clk_y;
                }
            }
        }

        var CLIENT_TIMEOUT_ABORT = 1;
        var SERVER_ABORT = 2;
                
        function getDoc(frame) {
            /* it looks like contentWindow or contentDocument do not
             * carry the protocol property in ie8, when running under ssl
             * frame.document is the only valid response document, since
             * the protocol is know but not on the other two objects. strange?
             * "Same origin policy" http://en.wikipedia.org/wiki/Same_origin_policy
             */
            
            var doc = null;
            
            // IE8 cascading access check
            try {
                if (frame.contentWindow) {
                    doc = frame.contentWindow.document;
                }
            } catch(err) {
                // IE8 access denied under ssl & missing protocol
                log('cannot get iframe.contentWindow document: ' + err);
            }

            if (doc) { // successful getting content
                return doc;
            }

            try { // simply checking may throw in ie8 under ssl or mismatched protocol
                doc = frame.contentDocument ? frame.contentDocument : frame.document;
            } catch(err) {
                // last attempt
                log('cannot get iframe.contentDocument: ' + err);
                doc = frame.document;
            }
            return doc;
        }

        // Rails CSRF hack (thanks to Yvan Barthelemy)
        var csrf_token = $('meta[name=csrf-token]').attr('content');
        var csrf_param = $('meta[name=csrf-param]').attr('content');
        if (csrf_param && csrf_token) {
            s.extraData = s.extraData || {};
            s.extraData[csrf_param] = csrf_token;
        }

        // take a breath so that pending repaints get some cpu time before the upload starts
        function doSubmit() {
            // make sure form attrs are set
            var t = $form.attr2('target'), a = $form.attr2('action');

            // update form attrs in IE friendly way
            form.setAttribute('target',id);
            if (!method) {
                form.setAttribute('method', 'POST');
            }
            if (a != s.url) {
                form.setAttribute('action', s.url);
            }

            // ie borks in some cases when setting encoding
            if (! s.skipEncodingOverride && (!method || /post/i.test(method))) {
                $form.attr({
                    encoding: 'multipart/form-data',
                    enctype:  'multipart/form-data'
                });
            }

            // support timout
            if (s.timeout) {
                timeoutHandle = setTimeout(function() { timedOut = true; cb(CLIENT_TIMEOUT_ABORT); }, s.timeout);
            }

            // look for server aborts
            function checkState() {
                try {
                    var state = getDoc(io).readyState;
                    log('state = ' + state);
                    if (state && state.toLowerCase() == 'uninitialized')
                        setTimeout(checkState,50);
                }
                catch(e) {
                    log('Server abort: ' , e, ' (', e.name, ')');
                    cb(SERVER_ABORT);
                    if (timeoutHandle)
                        clearTimeout(timeoutHandle);
                    timeoutHandle = undefined;
                }
            }

            // add "extra" data to form if provided in options
            var extraInputs = [];
            try {
                if (s.extraData) {
                    for (var n in s.extraData) {
                        if (s.extraData.hasOwnProperty(n)) {
                           // if using the $.param format that allows for multiple values with the same name
                           if($.isPlainObject(s.extraData[n]) && s.extraData[n].hasOwnProperty('name') && s.extraData[n].hasOwnProperty('value')) {
                               extraInputs.push(
                               $('<input type="hidden" name="'+s.extraData[n].name+'">').val(s.extraData[n].value)
                                   .appendTo(form)[0]);
                           } else {
                               extraInputs.push(
                               $('<input type="hidden" name="'+n+'">').val(s.extraData[n])
                                   .appendTo(form)[0]);
                           }
                        }
                    }
                }

                if (!s.iframeTarget) {
                    // add iframe to doc and submit the form
                    $io.appendTo('body');
                    if (io.attachEvent)
                        io.attachEvent('onload', cb);
                    else
                        io.addEventListener('load', cb, false);
                }
                setTimeout(checkState,15);

                try {
                    form.submit();
                } catch(err) {
                    // just in case form has element with name/id of 'submit'
                    var submitFn = document.createElement('form').submit;
                    submitFn.apply(form);
                }
            }
            finally {
                // reset attrs and remove "extra" input elements
                form.setAttribute('action',a);
                if(t) {
                    form.setAttribute('target', t);
                } else {
                    $form.removeAttr('target');
                }
                $(extraInputs).remove();
            }
        }

        if (s.forceSync) {
            doSubmit();
        }
        else {
            setTimeout(doSubmit, 10); // this lets dom updates render
        }

        var data, doc, domCheckCount = 50, callbackProcessed;

        function cb(e) {
            if (xhr.aborted || callbackProcessed) {
                return;
            }
            
            doc = getDoc(io);
            if(!doc) {
                log('cannot access response document');
                e = SERVER_ABORT;
            }
            if (e === CLIENT_TIMEOUT_ABORT && xhr) {
                xhr.abort('timeout');
                deferred.reject(xhr, 'timeout');
                return;
            }
            else if (e == SERVER_ABORT && xhr) {
                xhr.abort('server abort');
                deferred.reject(xhr, 'error', 'server abort');
                return;
            }

            if (!doc || doc.location.href == s.iframeSrc) {
                // response not received yet
                if (!timedOut)
                    return;
            }
            if (io.detachEvent)
                io.detachEvent('onload', cb);
            else
                io.removeEventListener('load', cb, false);

            var status = 'success', errMsg;
            try {
                if (timedOut) {
                    throw 'timeout';
                }

                var isXml = s.dataType == 'xml' || doc.XMLDocument || $.isXMLDoc(doc);
                log('isXml='+isXml);
                if (!isXml && window.opera && (doc.body === null || !doc.body.innerHTML)) {
                    if (--domCheckCount) {
                        // in some browsers (Opera) the iframe DOM is not always traversable when
                        // the onload callback fires, so we loop a bit to accommodate
                        log('requeing onLoad callback, DOM not available');
                        setTimeout(cb, 250);
                        return;
                    }
                    // let this fall through because server response could be an empty document
                    //log('Could not access iframe DOM after mutiple tries.');
                    //throw 'DOMException: not available';
                }

                //log('response detected');
                var docRoot = doc.body ? doc.body : doc.documentElement;
                xhr.responseText = docRoot ? docRoot.innerHTML : null;
                xhr.responseXML = doc.XMLDocument ? doc.XMLDocument : doc;
                if (isXml)
                    s.dataType = 'xml';
                xhr.getResponseHeader = function(header){
                    var headers = {'content-type': s.dataType};
                    return headers[header];
                };
                // support for XHR 'status' & 'statusText' emulation :
                if (docRoot) {
                    xhr.status = Number( docRoot.getAttribute('status') ) || xhr.status;
                    xhr.statusText = docRoot.getAttribute('statusText') || xhr.statusText;
                }

                var dt = (s.dataType || '').toLowerCase();
                var scr = /(json|script|text)/.test(dt);
                if (scr || s.textarea) {
                    // see if user embedded response in textarea
                    var ta = doc.getElementsByTagName('textarea')[0];
                    if (ta) {
                        xhr.responseText = ta.value;
                        // support for XHR 'status' & 'statusText' emulation :
                        xhr.status = Number( ta.getAttribute('status') ) || xhr.status;
                        xhr.statusText = ta.getAttribute('statusText') || xhr.statusText;
                    }
                    else if (scr) {
                        // account for browsers injecting pre around json response
                        var pre = doc.getElementsByTagName('pre')[0];
                        var b = doc.getElementsByTagName('body')[0];
                        if (pre) {
                            xhr.responseText = pre.textContent ? pre.textContent : pre.innerText;
                        }
                        else if (b) {
                            xhr.responseText = b.textContent ? b.textContent : b.innerText;
                        }
                    }
                }
                else if (dt == 'xml' && !xhr.responseXML && xhr.responseText) {
                    xhr.responseXML = toXml(xhr.responseText);
                }

                try {
                    data = httpData(xhr, dt, s);
                }
                catch (err) {
                    status = 'parsererror';
                    xhr.error = errMsg = (err || status);
                }
            }
            catch (err) {
                log('error caught: ',err);
                status = 'error';
                xhr.error = errMsg = (err || status);
            }

            if (xhr.aborted) {
                log('upload aborted');
                status = null;
            }

            if (xhr.status) { // we've set xhr.status
                status = (xhr.status >= 200 && xhr.status < 300 || xhr.status === 304) ? 'success' : 'error';
            }

            // ordering of these callbacks/triggers is odd, but that's how $.ajax does it
            if (status === 'success') {
                if (s.success)
                    s.success.call(s.context, data, 'success', xhr);
                deferred.resolve(xhr.responseText, 'success', xhr);
                if (g)
                    $.event.trigger("ajaxSuccess", [xhr, s]);
            }
            else if (status) {
                if (errMsg === undefined)
                    errMsg = xhr.statusText;
                if (s.error)
                    s.error.call(s.context, xhr, status, errMsg);
                deferred.reject(xhr, 'error', errMsg);
                if (g)
                    $.event.trigger("ajaxError", [xhr, s, errMsg]);
            }

            if (g)
                $.event.trigger("ajaxComplete", [xhr, s]);

            if (g && ! --$.active) {
                $.event.trigger("ajaxStop");
            }

            if (s.complete)
                s.complete.call(s.context, xhr, status);

            callbackProcessed = true;
            if (s.timeout)
                clearTimeout(timeoutHandle);

            // clean up
            setTimeout(function() {
                if (!s.iframeTarget)
                    $io.remove();
                xhr.responseXML = null;
            }, 100);
        }

        var toXml = $.parseXML || function(s, doc) { // use parseXML if available (jQuery 1.5+)
            if (window.ActiveXObject) {
                doc = new ActiveXObject('Microsoft.XMLDOM');
                doc.async = 'false';
                doc.loadXML(s);
            }
            else {
                doc = (new DOMParser()).parseFromString(s, 'text/xml');
            }
            return (doc && doc.documentElement && doc.documentElement.nodeName != 'parsererror') ? doc : null;
        };
        var parseJSON = $.parseJSON || function(s) {
            /*jslint evil:true */
            return window['eval']('(' + s + ')');
        };

        var httpData = function( xhr, type, s ) { // mostly lifted from jq1.4.4

            var ct = xhr.getResponseHeader('content-type') || '',
                xml = type === 'xml' || !type && ct.indexOf('xml') >= 0,
                data = xml ? xhr.responseXML : xhr.responseText;

            if (xml && data.documentElement.nodeName === 'parsererror') {
                if ($.error)
                    $.error('parsererror');
            }
            if (s && s.dataFilter) {
                data = s.dataFilter(data, type);
            }
            if (typeof data === 'string') {
                if (type === 'json' || !type && ct.indexOf('json') >= 0) {
                    data = parseJSON(data);
                } else if (type === "script" || !type && ct.indexOf("javascript") >= 0) {
                    $.globalEval(data);
                }
            }
            return data;
        };

        return deferred;
    }
};

/**
 * ajaxForm() provides a mechanism for fully automating form submission.
 *
 * The advantages of using this method instead of ajaxSubmit() are:
 *
 * 1: This method will include coordinates for <input type="image" /> elements (if the element
 *    is used to submit the form).
 * 2. This method will include the submit element's name/value data (for the element that was
 *    used to submit the form).
 * 3. This method binds the submit() method to the form for you.
 *
 * The options argument for ajaxForm works exactly as it does for ajaxSubmit.  ajaxForm merely
 * passes the options argument along after properly binding events for submit elements and
 * the form itself.
 */
$.fn.ajaxForm = function(options) {
    options = options || {};
    options.delegation = options.delegation && $.isFunction($.fn.on);

    // in jQuery 1.3+ we can fix mistakes with the ready state
    if (!options.delegation && this.length === 0) {
        var o = { s: this.selector, c: this.context };
        if (!$.isReady && o.s) {
            log('DOM not ready, queuing ajaxForm');
            $(function() {
                $(o.s,o.c).ajaxForm(options);
            });
            return this;
        }
        // is your DOM ready?  http://docs.jquery.com/Tutorials:Introducing_$(document).ready()
        log('terminating; zero elements found by selector' + ($.isReady ? '' : ' (DOM not ready)'));
        return this;
    }

    if ( options.delegation ) {
        $(document)
            .off('submit.form-plugin', this.selector, doAjaxSubmit)
            .off('click.form-plugin', this.selector, captureSubmittingElement)
            .on('submit.form-plugin', this.selector, options, doAjaxSubmit)
            .on('click.form-plugin', this.selector, options, captureSubmittingElement);
        return this;
    }

    return this.ajaxFormUnbind()
        .bind('submit.form-plugin', options, doAjaxSubmit)
        .bind('click.form-plugin', options, captureSubmittingElement);
};

// private event handlers
function doAjaxSubmit(e) {
    /*jshint validthis:true */
    var options = e.data;
    if (!e.isDefaultPrevented()) { // if event has been canceled, don't proceed
        e.preventDefault();
        $(this).ajaxSubmit(options);
    }
}

function captureSubmittingElement(e) {
    /*jshint validthis:true */
    var target = e.target;
    var $el = $(target);
    if (!($el.is("[type=submit],[type=image]"))) {
        // is this a child element of the submit el?  (ex: a span within a button)
        var t = $el.closest('[type=submit]');
        if (t.length === 0) {
            return;
        }
        target = t[0];
    }
    var form = this;
    form.clk = target;
    if (target.type == 'image') {
        if (e.offsetX !== undefined) {
            form.clk_x = e.offsetX;
            form.clk_y = e.offsetY;
        } else if (typeof $.fn.offset == 'function') {
            var offset = $el.offset();
            form.clk_x = e.pageX - offset.left;
            form.clk_y = e.pageY - offset.top;
        } else {
            form.clk_x = e.pageX - target.offsetLeft;
            form.clk_y = e.pageY - target.offsetTop;
        }
    }
    // clear form vars
    setTimeout(function() { form.clk = form.clk_x = form.clk_y = null; }, 100);
}


// ajaxFormUnbind unbinds the event handlers that were bound by ajaxForm
$.fn.ajaxFormUnbind = function() {
    return this.unbind('submit.form-plugin click.form-plugin');
};

/**
 * formToArray() gathers form element data into an array of objects that can
 * be passed to any of the following ajax functions: $.get, $.post, or load.
 * Each object in the array has both a 'name' and 'value' property.  An example of
 * an array for a simple login form might be:
 *
 * [ { name: 'username', value: 'jresig' }, { name: 'password', value: 'secret' } ]
 *
 * It is this array that is passed to pre-submit callback functions provided to the
 * ajaxSubmit() and ajaxForm() methods.
 */
$.fn.formToArray = function(semantic, elements) {
    var a = [];
    if (this.length === 0) {
        return a;
    }

    var form = this[0];
    var els = semantic ? form.getElementsByTagName('*') : form.elements;
    if (!els) {
        return a;
    }

    var i,j,n,v,el,max,jmax;
    for(i=0, max=els.length; i < max; i++) {
        el = els[i];
        n = el.name;
        if (!n || el.disabled) {
            continue;
        }

        if (semantic && form.clk && el.type == "image") {
            // handle image inputs on the fly when semantic == true
            if(form.clk == el) {
                a.push({name: n, value: $(el).val(), type: el.type });
                a.push({name: n+'.x', value: form.clk_x}, {name: n+'.y', value: form.clk_y});
            }
            continue;
        }

        v = $.fieldValue(el, true);
        if (v && v.constructor == Array) {
            if (elements)
                elements.push(el);
            for(j=0, jmax=v.length; j < jmax; j++) {
                a.push({name: n, value: v[j]});
            }
        }
        else if (feature.fileapi && el.type == 'file') {
            if (elements)
                elements.push(el);
            var files = el.files;
            if (files.length) {
                for (j=0; j < files.length; j++) {
                    a.push({name: n, value: files[j], type: el.type});
                }
            }
            else {
                // #180
                a.push({ name: n, value: '', type: el.type });
            }
        }
        else if (v !== null && typeof v != 'undefined') {
            if (elements)
                elements.push(el);
            a.push({name: n, value: v, type: el.type, required: el.required});
        }
    }

    if (!semantic && form.clk) {
        // input type=='image' are not found in elements array! handle it here
        var $input = $(form.clk), input = $input[0];
        n = input.name;
        if (n && !input.disabled && input.type == 'image') {
            a.push({name: n, value: $input.val()});
            a.push({name: n+'.x', value: form.clk_x}, {name: n+'.y', value: form.clk_y});
        }
    }
    return a;
};

/**
 * Serializes form data into a 'submittable' string. This method will return a string
 * in the format: name1=value1&amp;name2=value2
 */
$.fn.formSerialize = function(semantic) {
    //hand off to jQuery.param for proper encoding
    return $.param(this.formToArray(semantic));
};

/**
 * Serializes all field elements in the jQuery object into a query string.
 * This method will return a string in the format: name1=value1&amp;name2=value2
 */
$.fn.fieldSerialize = function(successful) {
    var a = [];
    this.each(function() {
        var n = this.name;
        if (!n) {
            return;
        }
        var v = $.fieldValue(this, successful);
        if (v && v.constructor == Array) {
            for (var i=0,max=v.length; i < max; i++) {
                a.push({name: n, value: v[i]});
            }
        }
        else if (v !== null && typeof v != 'undefined') {
            a.push({name: this.name, value: v});
        }
    });
    //hand off to jQuery.param for proper encoding
    return $.param(a);
};

/**
 * Returns the value(s) of the element in the matched set.  For example, consider the following form:
 *
 *  <form><fieldset>
 *      <input name="A" type="text" />
 *      <input name="A" type="text" />
 *      <input name="B" type="checkbox" value="B1" />
 *      <input name="B" type="checkbox" value="B2"/>
 *      <input name="C" type="radio" value="C1" />
 *      <input name="C" type="radio" value="C2" />
 *  </fieldset></form>
 *
 *  var v = $('input[type=text]').fieldValue();
 *  // if no values are entered into the text inputs
 *  v == ['','']
 *  // if values entered into the text inputs are 'foo' and 'bar'
 *  v == ['foo','bar']
 *
 *  var v = $('input[type=checkbox]').fieldValue();
 *  // if neither checkbox is checked
 *  v === undefined
 *  // if both checkboxes are checked
 *  v == ['B1', 'B2']
 *
 *  var v = $('input[type=radio]').fieldValue();
 *  // if neither radio is checked
 *  v === undefined
 *  // if first radio is checked
 *  v == ['C1']
 *
 * The successful argument controls whether or not the field element must be 'successful'
 * (per http://www.w3.org/TR/html4/interact/forms.html#successful-controls).
 * The default value of the successful argument is true.  If this value is false the value(s)
 * for each element is returned.
 *
 * Note: This method *always* returns an array.  If no valid value can be determined the
 *    array will be empty, otherwise it will contain one or more values.
 */
$.fn.fieldValue = function(successful) {
    for (var val=[], i=0, max=this.length; i < max; i++) {
        var el = this[i];
        var v = $.fieldValue(el, successful);
        if (v === null || typeof v == 'undefined' || (v.constructor == Array && !v.length)) {
            continue;
        }
        if (v.constructor == Array)
            $.merge(val, v);
        else
            val.push(v);
    }
    return val;
};

/**
 * Returns the value of the field element.
 */
$.fieldValue = function(el, successful) {
    var n = el.name, t = el.type, tag = el.tagName.toLowerCase();
    if (successful === undefined) {
        successful = true;
    }

    if (successful && (!n || el.disabled || t == 'reset' || t == 'button' ||
        (t == 'checkbox' || t == 'radio') && !el.checked ||
        (t == 'submit' || t == 'image') && el.form && el.form.clk != el ||
        tag == 'select' && el.selectedIndex == -1)) {
            return null;
    }

    if (tag == 'select') {
        var index = el.selectedIndex;
        if (index < 0) {
            return null;
        }
        var a = [], ops = el.options;
        var one = (t == 'select-one');
        var max = (one ? index+1 : ops.length);
        for(var i=(one ? index : 0); i < max; i++) {
            var op = ops[i];
            if (op.selected) {
                var v = op.value;
                if (!v) { // extra pain for IE...
                    v = (op.attributes && op.attributes['value'] && !(op.attributes['value'].specified)) ? op.text : op.value;
                }
                if (one) {
                    return v;
                }
                a.push(v);
            }
        }
        return a;
    }
    return $(el).val();
};

/**
 * Clears the form data.  Takes the following actions on the form's input fields:
 *  - input text fields will have their 'value' property set to the empty string
 *  - select elements will have their 'selectedIndex' property set to -1
 *  - checkbox and radio inputs will have their 'checked' property set to false
 *  - inputs of type submit, button, reset, and hidden will *not* be effected
 *  - button elements will *not* be effected
 */
$.fn.clearForm = function(includeHidden) {
    return this.each(function() {
        $('input,select,textarea', this).clearFields(includeHidden);
    });
};

/**
 * Clears the selected form elements.
 */
$.fn.clearFields = $.fn.clearInputs = function(includeHidden) {
    var re = /^(?:color|date|datetime|email|month|number|password|range|search|tel|text|time|url|week)$/i; // 'hidden' is not in this list
    return this.each(function() {
        var t = this.type, tag = this.tagName.toLowerCase();
        if (re.test(t) || tag == 'textarea') {
            this.value = '';
        }
        else if (t == 'checkbox' || t == 'radio') {
            this.checked = false;
        }
        else if (tag == 'select') {
            this.selectedIndex = -1;
        }
		else if (t == "file") {
			if (/MSIE/.test(navigator.userAgent)) {
				$(this).replaceWith($(this).clone(true));
			} else {
				$(this).val('');
			}
		}
        else if (includeHidden) {
            // includeHidden can be the value true, or it can be a selector string
            // indicating a special test; for example:
            //  $('#myForm').clearForm('.special:hidden')
            // the above would clean hidden inputs that have the class of 'special'
            if ( (includeHidden === true && /hidden/.test(t)) ||
                 (typeof includeHidden == 'string' && $(this).is(includeHidden)) )
                this.value = '';
        }
    });
};

/**
 * Resets the form data.  Causes all form elements to be reset to their original value.
 */
$.fn.resetForm = function() {
    return this.each(function() {
        // guard against an input with the name of 'reset'
        // note that IE reports the reset function as an 'object'
        if (typeof this.reset == 'function' || (typeof this.reset == 'object' && !this.reset.nodeType)) {
            this.reset();
        }
    });
};

/**
 * Enables or disables any matching elements.
 */
$.fn.enable = function(b) {
    if (b === undefined) {
        b = true;
    }
    return this.each(function() {
        this.disabled = !b;
    });
};

/**
 * Checks/unchecks any matching checkboxes or radio buttons and
 * selects/deselects and matching option elements.
 */
$.fn.selected = function(select) {
    if (select === undefined) {
        select = true;
    }
    return this.each(function() {
        var t = this.type;
        if (t == 'checkbox' || t == 'radio') {
            this.checked = select;
        }
        else if (this.tagName.toLowerCase() == 'option') {
            var $sel = $(this).parent('select');
            if (select && $sel[0] && $sel[0].type == 'select-one') {
                // deselect all other options
                $sel.find('option').selected(false);
            }
            this.selected = select;
        }
    });
};

// expose debug var
$.fn.ajaxSubmit.debug = false;

// helper fn for console logging
function log() {
    if (!$.fn.ajaxSubmit.debug)
        return;
    var msg = '[jquery.form] ' + Array.prototype.join.call(arguments,'');
    if (window.console && window.console.log) {
        window.console.log(msg);
    }
    else if (window.opera && window.opera.postError) {
        window.opera.postError(msg);
    }
}

})(jQuery);

/*
 * jQuery Easing v1.3 - http://gsgd.co.uk/sandbox/jquery/easing/
 *
 * Uses the built in easing capabilities added In jQuery 1.1
 * to offer multiple easing options
 *
 * TERMS OF USE - jQuery Easing
 * 
 * Open source under the BSD License. 
 * 
 * Copyright © 2008 George McGinley Smith
 * All rights reserved.
 * 
 * Redistribution and use in source and binary forms, with or without modification, 
 * are permitted provided that the following conditions are met:
 * 
 * Redistributions of source code must retain the above copyright notice, this list of 
 * conditions and the following disclaimer.
 * Redistributions in binary form must reproduce the above copyright notice, this list 
 * of conditions and the following disclaimer in the documentation and/or other materials 
 * provided with the distribution.
 * 
 * Neither the name of the author nor the names of contributors may be used to endorse 
 * or promote products derived from this software without specific prior written permission.
 * 
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY 
 * EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 *  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 *  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE
 *  GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED 
 * AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
 *  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED 
 * OF THE POSSIBILITY OF SUCH DAMAGE. 
 *
*/

// t: current time, b: begInnIng value, c: change In value, d: duration
jQuery.easing['jswing'] = jQuery.easing['swing'];

jQuery.extend( jQuery.easing,
{
	def: 'easeOutQuad',
	swing: function (x, t, b, c, d) {
		//alert(jQuery.easing.default);
		return jQuery.easing[jQuery.easing.def](x, t, b, c, d);
	},
	easeInQuad: function (x, t, b, c, d) {
		return c*(t/=d)*t + b;
	},
	easeOutQuad: function (x, t, b, c, d) {
		return -c *(t/=d)*(t-2) + b;
	},
	easeInOutQuad: function (x, t, b, c, d) {
		if ((t/=d/2) < 1) return c/2*t*t + b;
		return -c/2 * ((--t)*(t-2) - 1) + b;
	},
	easeInCubic: function (x, t, b, c, d) {
		return c*(t/=d)*t*t + b;
	},
	easeOutCubic: function (x, t, b, c, d) {
		return c*((t=t/d-1)*t*t + 1) + b;
	},
	easeInOutCubic: function (x, t, b, c, d) {
		if ((t/=d/2) < 1) return c/2*t*t*t + b;
		return c/2*((t-=2)*t*t + 2) + b;
	},
	easeInQuart: function (x, t, b, c, d) {
		return c*(t/=d)*t*t*t + b;
	},
	easeOutQuart: function (x, t, b, c, d) {
		return -c * ((t=t/d-1)*t*t*t - 1) + b;
	},
	easeInOutQuart: function (x, t, b, c, d) {
		if ((t/=d/2) < 1) return c/2*t*t*t*t + b;
		return -c/2 * ((t-=2)*t*t*t - 2) + b;
	},
	easeInQuint: function (x, t, b, c, d) {
		return c*(t/=d)*t*t*t*t + b;
	},
	easeOutQuint: function (x, t, b, c, d) {
		return c*((t=t/d-1)*t*t*t*t + 1) + b;
	},
	easeInOutQuint: function (x, t, b, c, d) {
		if ((t/=d/2) < 1) return c/2*t*t*t*t*t + b;
		return c/2*((t-=2)*t*t*t*t + 2) + b;
	},
	easeInSine: function (x, t, b, c, d) {
		return -c * Math.cos(t/d * (Math.PI/2)) + c + b;
	},
	easeOutSine: function (x, t, b, c, d) {
		return c * Math.sin(t/d * (Math.PI/2)) + b;
	},
	easeInOutSine: function (x, t, b, c, d) {
		return -c/2 * (Math.cos(Math.PI*t/d) - 1) + b;
	},
	easeInExpo: function (x, t, b, c, d) {
		return (t==0) ? b : c * Math.pow(2, 10 * (t/d - 1)) + b;
	},
	easeOutExpo: function (x, t, b, c, d) {
		return (t==d) ? b+c : c * (-Math.pow(2, -10 * t/d) + 1) + b;
	},
	easeInOutExpo: function (x, t, b, c, d) {
		if (t==0) return b;
		if (t==d) return b+c;
		if ((t/=d/2) < 1) return c/2 * Math.pow(2, 10 * (t - 1)) + b;
		return c/2 * (-Math.pow(2, -10 * --t) + 2) + b;
	},
	easeInCirc: function (x, t, b, c, d) {
		return -c * (Math.sqrt(1 - (t/=d)*t) - 1) + b;
	},
	easeOutCirc: function (x, t, b, c, d) {
		return c * Math.sqrt(1 - (t=t/d-1)*t) + b;
	},
	easeInOutCirc: function (x, t, b, c, d) {
		if ((t/=d/2) < 1) return -c/2 * (Math.sqrt(1 - t*t) - 1) + b;
		return c/2 * (Math.sqrt(1 - (t-=2)*t) + 1) + b;
	},
	easeInElastic: function (x, t, b, c, d) {
		var s=1.70158;var p=0;var a=c;
		if (t==0) return b;  if ((t/=d)==1) return b+c;  if (!p) p=d*.3;
		if (a < Math.abs(c)) { a=c; var s=p/4; }
		else var s = p/(2*Math.PI) * Math.asin (c/a);
		return -(a*Math.pow(2,10*(t-=1)) * Math.sin( (t*d-s)*(2*Math.PI)/p )) + b;
	},
	easeOutElastic: function (x, t, b, c, d) {
		var s=1.70158;var p=0;var a=c;
		if (t==0) return b;  if ((t/=d)==1) return b+c;  if (!p) p=d*.3;
		if (a < Math.abs(c)) { a=c; var s=p/4; }
		else var s = p/(2*Math.PI) * Math.asin (c/a);
		return a*Math.pow(2,-10*t) * Math.sin( (t*d-s)*(2*Math.PI)/p ) + c + b;
	},
	easeInOutElastic: function (x, t, b, c, d) {
		var s=1.70158;var p=0;var a=c;
		if (t==0) return b;  if ((t/=d/2)==2) return b+c;  if (!p) p=d*(.3*1.5);
		if (a < Math.abs(c)) { a=c; var s=p/4; }
		else var s = p/(2*Math.PI) * Math.asin (c/a);
		if (t < 1) return -.5*(a*Math.pow(2,10*(t-=1)) * Math.sin( (t*d-s)*(2*Math.PI)/p )) + b;
		return a*Math.pow(2,-10*(t-=1)) * Math.sin( (t*d-s)*(2*Math.PI)/p )*.5 + c + b;
	},
	easeInBack: function (x, t, b, c, d, s) {
		if (s == undefined) s = 1.70158;
		return c*(t/=d)*t*((s+1)*t - s) + b;
	},
	easeOutBack: function (x, t, b, c, d, s) {
		if (s == undefined) s = 1.70158;
		return c*((t=t/d-1)*t*((s+1)*t + s) + 1) + b;
	},
	easeInOutBack: function (x, t, b, c, d, s) {
		if (s == undefined) s = 1.70158; 
		if ((t/=d/2) < 1) return c/2*(t*t*(((s*=(1.525))+1)*t - s)) + b;
		return c/2*((t-=2)*t*(((s*=(1.525))+1)*t + s) + 2) + b;
	},
	easeInBounce: function (x, t, b, c, d) {
		return c - jQuery.easing.easeOutBounce (x, d-t, 0, c, d) + b;
	},
	easeOutBounce: function (x, t, b, c, d) {
		if ((t/=d) < (1/2.75)) {
			return c*(7.5625*t*t) + b;
		} else if (t < (2/2.75)) {
			return c*(7.5625*(t-=(1.5/2.75))*t + .75) + b;
		} else if (t < (2.5/2.75)) {
			return c*(7.5625*(t-=(2.25/2.75))*t + .9375) + b;
		} else {
			return c*(7.5625*(t-=(2.625/2.75))*t + .984375) + b;
		}
	},
	easeInOutBounce: function (x, t, b, c, d) {
		if (t < d/2) return jQuery.easing.easeInBounce (x, t*2, 0, c, d) * .5 + b;
		return jQuery.easing.easeOutBounce (x, t*2-d, 0, c, d) * .5 + c*.5 + b;
	}
});

/*
 *
 * TERMS OF USE - EASING EQUATIONS
 * 
 * Open source under the BSD License. 
 * 
 * Copyright © 2001 Robert Penner
 * All rights reserved.
 * 
 * Redistribution and use in source and binary forms, with or without modification, 
 * are permitted provided that the following conditions are met:
 * 
 * Redistributions of source code must retain the above copyright notice, this list of 
 * conditions and the following disclaimer.
 * Redistributions in binary form must reproduce the above copyright notice, this list 
 * of conditions and the following disclaimer in the documentation and/or other materials 
 * provided with the distribution.
 * 
 * Neither the name of the author nor the names of contributors may be used to endorse 
 * or promote products derived from this software without specific prior written permission.
 * 
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY 
 * EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 *  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 *  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE
 *  GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED 
 * AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
 *  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED 
 * OF THE POSSIBILITY OF SUCH DAMAGE. 
 *
 */
/*!
 * jQuery Cookie Plugin v1.4.0
 * https://github.com/carhartl/jquery-cookie
 *
 * Copyright 2013 Klaus Hartl
 * Released under the MIT license
 */
(function (factory) {
	if (typeof define === 'function' && define.amd) {
		// AMD. Register as anonymous module.
		define(['jquery'], factory);
	} else {
		// Browser globals.
		factory(jQuery);
	}
}(function ($) {

	var pluses = /\+/g;

	function encode(s) {
		return config.raw ? s : encodeURIComponent(s);
	}

	function decode(s) {
		return config.raw ? s : decodeURIComponent(s);
	}

	function stringifyCookieValue(value) {
		return encode(config.json ? JSON.stringify(value) : String(value));
	}

	function parseCookieValue(s) {
		if (s.indexOf('"') === 0) {
			// This is a quoted cookie as according to RFC2068, unescape...
			s = s.slice(1, -1).replace(/\\"/g, '"').replace(/\\\\/g, '\\');
		}

		try {
			// Replace server-side written pluses with spaces.
			// If we can't decode the cookie, ignore it, it's unusable.
			// If we can't parse the cookie, ignore it, it's unusable.
			s = decodeURIComponent(s.replace(pluses, ' '));
			return config.json ? JSON.parse(s) : s;
		} catch(e) {}
	}

	function read(s, converter) {
		var value = config.raw ? s : parseCookieValue(s);
		return $.isFunction(converter) ? converter(value) : value;
	}

	var config = $.cookie = function (key, value, options) {

		// Write

		if (value !== undefined && !$.isFunction(value)) {
			options = $.extend({}, config.defaults, options);

			if (typeof options.expires === 'number') {
				var days = options.expires, t = options.expires = new Date();
				t.setTime(+t + days * 864e+5);
			}

			return (document.cookie = [
				encode(key), '=', stringifyCookieValue(value),
				options.expires ? '; expires=' + options.expires.toUTCString() : '', // use expires attribute, max-age is not supported by IE
				options.path    ? '; path=' + options.path : '',
				options.domain  ? '; domain=' + options.domain : '',
				options.secure  ? '; secure' : ''
			].join(''));
		}

		// Read

		var result = key ? undefined : {};

		// To prevent the for loop in the first place assign an empty array
		// in case there are no cookies at all. Also prevents odd result when
		// calling $.cookie().
		var cookies = document.cookie ? document.cookie.split('; ') : [];

		for (var i = 0, l = cookies.length; i < l; i++) {
			var parts = cookies[i].split('=');
			var name = decode(parts.shift());
			var cookie = parts.join('=');

			if (key && key === name) {
				// If second argument (value) is a function it's a converter...
				result = read(cookie, value);
				break;
			}

			// Prevent storing a cookie that we couldn't decode.
			if (!key && (cookie = read(cookie)) !== undefined) {
				result[name] = cookie;
			}
		}

		return result;
	};

	config.defaults = {};

	$.removeCookie = function (key, options) {
		if ($.cookie(key) === undefined) {
			return false;
		}

		// Must not alter options, thus extending a fresh object...
		$.cookie(key, '', $.extend({}, options, { expires: -1 }));
		return !$.cookie(key);
	};

}));

/*!
 * Bootstrap v3.2.0 (http://getbootstrap.com)
 * Copyright 2011-2014 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 */

if (typeof jQuery === 'undefined') { throw new Error('Bootstrap\'s JavaScript requires jQuery') }

/* ========================================================================
 * Bootstrap: transition.js v3.2.0
 * http://getbootstrap.com/javascript/#transitions
 * ========================================================================
 * Copyright 2011-2014 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 * ======================================================================== */


+function ($) {
  'use strict';

  // CSS TRANSITION SUPPORT (Shoutout: http://www.modernizr.com/)
  // ============================================================

  function transitionEnd() {
    var el = document.createElement('bootstrap')

    var transEndEventNames = {
      WebkitTransition : 'webkitTransitionEnd',
      MozTransition    : 'transitionend',
      OTransition      : 'oTransitionEnd otransitionend',
      transition       : 'transitionend'
    }

    for (var name in transEndEventNames) {
      if (el.style[name] !== undefined) {
        return { end: transEndEventNames[name] }
      }
    }

    return false // explicit for ie8 (  ._.)
  }

  // http://blog.alexmaccaw.com/css-transitions
  $.fn.emulateTransitionEnd = function (duration) {
    var called = false
    var $el = this
    $(this).one('bsTransitionEnd', function () { called = true })
    var callback = function () { if (!called) $($el).trigger($.support.transition.end) }
    setTimeout(callback, duration)
    return this
  }

  $(function () {
    $.support.transition = transitionEnd()

    if (!$.support.transition) return

    $.event.special.bsTransitionEnd = {
      bindType: $.support.transition.end,
      delegateType: $.support.transition.end,
      handle: function (e) {
        if ($(e.target).is(this)) return e.handleObj.handler.apply(this, arguments)
      }
    }
  })

}(jQuery);

/* ========================================================================
 * Bootstrap: alert.js v3.2.0
 * http://getbootstrap.com/javascript/#alerts
 * ========================================================================
 * Copyright 2011-2014 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 * ======================================================================== */


+function ($) {
  'use strict';

  // ALERT CLASS DEFINITION
  // ======================

  var dismiss = '[data-dismiss="alert"]'
  var Alert   = function (el) {
    $(el).on('click', dismiss, this.close)
  }

  Alert.VERSION = '3.2.0'

  Alert.prototype.close = function (e) {
    var $this    = $(this)
    var selector = $this.attr('data-target')

    if (!selector) {
      selector = $this.attr('href')
      selector = selector && selector.replace(/.*(?=#[^\s]*$)/, '') // strip for ie7
    }

    var $parent = $(selector)

    if (e) e.preventDefault()

    if (!$parent.length) {
      $parent = $this.hasClass('alert') ? $this : $this.parent()
    }

    $parent.trigger(e = $.Event('close.bs.alert'))

    if (e.isDefaultPrevented()) return

    $parent.removeClass('in')

    function removeElement() {
      // detach from parent, fire event then clean up data
      $parent.detach().trigger('closed.bs.alert').remove()
    }

    $.support.transition && $parent.hasClass('fade') ?
      $parent
        .one('bsTransitionEnd', removeElement)
        .emulateTransitionEnd(150) :
      removeElement()
  }


  // ALERT PLUGIN DEFINITION
  // =======================

  function Plugin(option) {
    return this.each(function () {
      var $this = $(this)
      var data  = $this.data('bs.alert')

      if (!data) $this.data('bs.alert', (data = new Alert(this)))
      if (typeof option == 'string') data[option].call($this)
    })
  }

  var old = $.fn.alert

  $.fn.alert             = Plugin
  $.fn.alert.Constructor = Alert


  // ALERT NO CONFLICT
  // =================

  $.fn.alert.noConflict = function () {
    $.fn.alert = old
    return this
  }


  // ALERT DATA-API
  // ==============

  $(document).on('click.bs.alert.data-api', dismiss, Alert.prototype.close)

}(jQuery);

/* ========================================================================
 * Bootstrap: button.js v3.2.0
 * http://getbootstrap.com/javascript/#buttons
 * ========================================================================
 * Copyright 2011-2014 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 * ======================================================================== */


+function ($) {
  'use strict';

  // BUTTON PUBLIC CLASS DEFINITION
  // ==============================

  var Button = function (element, options) {
    this.$element  = $(element)
    this.options   = $.extend({}, Button.DEFAULTS, options)
    this.isLoading = false
  }

  Button.VERSION  = '3.2.0'

  Button.DEFAULTS = {
    loadingText: 'loading...'
  }

  Button.prototype.setState = function (state) {
    var d    = 'disabled'
    var $el  = this.$element
    var val  = $el.is('input') ? 'val' : 'html'
    var data = $el.data()

    state = state + 'Text'

    if (data.resetText == null) $el.data('resetText', $el[val]())

    $el[val](data[state] == null ? this.options[state] : data[state])

    // push to event loop to allow forms to submit
    setTimeout($.proxy(function () {
      if (state == 'loadingText') {
        this.isLoading = true
        $el.addClass(d).attr(d, d)
      } else if (this.isLoading) {
        this.isLoading = false
        $el.removeClass(d).removeAttr(d)
      }
    }, this), 0)
  }

  Button.prototype.toggle = function () {
    var changed = true
    var $parent = this.$element.closest('[data-toggle="buttons"]')

    if ($parent.length) {
      var $input = this.$element.find('input')
      if ($input.prop('type') == 'radio') {
        if ($input.prop('checked') && this.$element.hasClass('active')) changed = false
        else $parent.find('.active').removeClass('active')
      }
      if (changed) $input.prop('checked', !this.$element.hasClass('active')).trigger('change')
    }

    if (changed) this.$element.toggleClass('active')
  }


  // BUTTON PLUGIN DEFINITION
  // ========================

  function Plugin(option) {
    return this.each(function () {
      var $this   = $(this)
      var data    = $this.data('bs.button')
      var options = typeof option == 'object' && option

      if (!data) $this.data('bs.button', (data = new Button(this, options)))

      if (option == 'toggle') data.toggle()
      else if (option) data.setState(option)
    })
  }

  var old = $.fn.button

  $.fn.button             = Plugin
  $.fn.button.Constructor = Button


  // BUTTON NO CONFLICT
  // ==================

  $.fn.button.noConflict = function () {
    $.fn.button = old
    return this
  }


  // BUTTON DATA-API
  // ===============

  $(document).on('click.bs.button.data-api', '[data-toggle^="button"]', function (e) {
    var $btn = $(e.target)
    if (!$btn.hasClass('btn')) $btn = $btn.closest('.btn')
    Plugin.call($btn, 'toggle')
    e.preventDefault()
  })

}(jQuery);

/* ========================================================================
 * Bootstrap: carousel.js v3.2.0
 * http://getbootstrap.com/javascript/#carousel
 * ========================================================================
 * Copyright 2011-2014 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 * ======================================================================== */


+function ($) {
  'use strict';

  // CAROUSEL CLASS DEFINITION
  // =========================

  var Carousel = function (element, options) {
    this.$element    = $(element).on('keydown.bs.carousel', $.proxy(this.keydown, this))
    this.$indicators = this.$element.find('.carousel-indicators')
    this.options     = options
    this.paused      =
    this.sliding     =
    this.interval    =
    this.$active     =
    this.$items      = null

    this.options.pause == 'hover' && this.$element
      .on('mouseenter.bs.carousel', $.proxy(this.pause, this))
      .on('mouseleave.bs.carousel', $.proxy(this.cycle, this))
  }

  Carousel.VERSION  = '3.2.0'

  Carousel.DEFAULTS = {
    interval: 5000,
    pause: 'hover',
    wrap: true
  }

  Carousel.prototype.keydown = function (e) {
    switch (e.which) {
      case 37: this.prev(); break
      case 39: this.next(); break
      default: return
    }

    e.preventDefault()
  }

  Carousel.prototype.cycle = function (e) {
    e || (this.paused = false)

    this.interval && clearInterval(this.interval)

    this.options.interval
      && !this.paused
      && (this.interval = setInterval($.proxy(this.next, this), this.options.interval))

    return this
  }

  Carousel.prototype.getItemIndex = function (item) {
    this.$items = item.parent().children('.item')
    return this.$items.index(item || this.$active)
  }

  Carousel.prototype.to = function (pos) {
    var that        = this
    var activeIndex = this.getItemIndex(this.$active = this.$element.find('.item.active'))

    if (pos > (this.$items.length - 1) || pos < 0) return

    if (this.sliding)       return this.$element.one('slid.bs.carousel', function () { that.to(pos) }) // yes, "slid"
    if (activeIndex == pos) return this.pause().cycle()

    return this.slide(pos > activeIndex ? 'next' : 'prev', $(this.$items[pos]))
  }

  Carousel.prototype.pause = function (e) {
    e || (this.paused = true)

    if (this.$element.find('.next, .prev').length && $.support.transition) {
      this.$element.trigger($.support.transition.end)
      this.cycle(true)
    }

    this.interval = clearInterval(this.interval)

    return this
  }

  Carousel.prototype.next = function () {
    if (this.sliding) return
    return this.slide('next')
  }

  Carousel.prototype.prev = function () {
    if (this.sliding) return
    return this.slide('prev')
  }

  Carousel.prototype.slide = function (type, next) {
    var $active   = this.$element.find('.item.active')
    var $next     = next || $active[type]()
    var isCycling = this.interval
    var direction = type == 'next' ? 'left' : 'right'
    var fallback  = type == 'next' ? 'first' : 'last'
    var that      = this

    if (!$next.length) {
      if (!this.options.wrap) return
      $next = this.$element.find('.item')[fallback]()
    }

    if ($next.hasClass('active')) return (this.sliding = false)

    var relatedTarget = $next[0]
    var slideEvent = $.Event('slide.bs.carousel', {
      relatedTarget: relatedTarget,
      direction: direction
    })
    this.$element.trigger(slideEvent)
    if (slideEvent.isDefaultPrevented()) return

    this.sliding = true

    isCycling && this.pause()

    if (this.$indicators.length) {
      this.$indicators.find('.active').removeClass('active')
      var $nextIndicator = $(this.$indicators.children()[this.getItemIndex($next)])
      $nextIndicator && $nextIndicator.addClass('active')
    }

    var slidEvent = $.Event('slid.bs.carousel', { relatedTarget: relatedTarget, direction: direction }) // yes, "slid"
    if ($.support.transition && this.$element.hasClass('slide')) {
      $next.addClass(type)
      $next[0].offsetWidth // force reflow
      $active.addClass(direction)
      $next.addClass(direction)
      $active
        .one('bsTransitionEnd', function () {
          $next.removeClass([type, direction].join(' ')).addClass('active')
          $active.removeClass(['active', direction].join(' '))
          that.sliding = false
          setTimeout(function () {
            that.$element.trigger(slidEvent)
          }, 0)
        })
        .emulateTransitionEnd($active.css('transition-duration').slice(0, -1) * 1000)
    } else {
      $active.removeClass('active')
      $next.addClass('active')
      this.sliding = false
      this.$element.trigger(slidEvent)
    }

    isCycling && this.cycle()

    return this
  }


  // CAROUSEL PLUGIN DEFINITION
  // ==========================

  function Plugin(option) {
    return this.each(function () {
      var $this   = $(this)
      var data    = $this.data('bs.carousel')
      var options = $.extend({}, Carousel.DEFAULTS, $this.data(), typeof option == 'object' && option)
      var action  = typeof option == 'string' ? option : options.slide

      if (!data) $this.data('bs.carousel', (data = new Carousel(this, options)))
      if (typeof option == 'number') data.to(option)
      else if (action) data[action]()
      else if (options.interval) data.pause().cycle()
    })
  }

  var old = $.fn.carousel

  $.fn.carousel             = Plugin
  $.fn.carousel.Constructor = Carousel


  // CAROUSEL NO CONFLICT
  // ====================

  $.fn.carousel.noConflict = function () {
    $.fn.carousel = old
    return this
  }


  // CAROUSEL DATA-API
  // =================

  $(document).on('click.bs.carousel.data-api', '[data-slide], [data-slide-to]', function (e) {
    var href
    var $this   = $(this)
    var $target = $($this.attr('data-target') || (href = $this.attr('href')) && href.replace(/.*(?=#[^\s]+$)/, '')) // strip for ie7
    if (!$target.hasClass('carousel')) return
    var options = $.extend({}, $target.data(), $this.data())
    var slideIndex = $this.attr('data-slide-to')
    if (slideIndex) options.interval = false

    Plugin.call($target, options)

    if (slideIndex) {
      $target.data('bs.carousel').to(slideIndex)
    }

    e.preventDefault()
  })

  $(window).on('load', function () {
    $('[data-ride="carousel"]').each(function () {
      var $carousel = $(this)
      Plugin.call($carousel, $carousel.data())
    })
  })

}(jQuery);

/* ========================================================================
 * Bootstrap: collapse.js v3.2.0
 * http://getbootstrap.com/javascript/#collapse
 * ========================================================================
 * Copyright 2011-2014 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 * ======================================================================== */


+function ($) {
  'use strict';

  // COLLAPSE PUBLIC CLASS DEFINITION
  // ================================

  var Collapse = function (element, options) {
    this.$element      = $(element)
    this.options       = $.extend({}, Collapse.DEFAULTS, options)
    this.transitioning = null

    if (this.options.parent) this.$parent = $(this.options.parent)
    if (this.options.toggle) this.toggle()
  }

  Collapse.VERSION  = '3.2.0'

  Collapse.DEFAULTS = {
    toggle: true
  }

  Collapse.prototype.dimension = function () {
    var hasWidth = this.$element.hasClass('width')
    return hasWidth ? 'width' : 'height'
  }

  Collapse.prototype.show = function () {
    if (this.transitioning || this.$element.hasClass('in')) return

    var startEvent = $.Event('show.bs.collapse')
    this.$element.trigger(startEvent)
    if (startEvent.isDefaultPrevented()) return

    var actives = this.$parent && this.$parent.find('> .panel > .in')

    if (actives && actives.length) {
      var hasData = actives.data('bs.collapse')
      if (hasData && hasData.transitioning) return
      Plugin.call(actives, 'hide')
      hasData || actives.data('bs.collapse', null)
    }

    var dimension = this.dimension()

    this.$element
      .removeClass('collapse')
      .addClass('collapsing')[dimension](0)

    this.transitioning = 1

    var complete = function () {
      this.$element
        .removeClass('collapsing')
        .addClass('collapse in')[dimension]('')
      this.transitioning = 0
      this.$element
        .trigger('shown.bs.collapse')
    }

    if (!$.support.transition) return complete.call(this)

    var scrollSize = $.camelCase(['scroll', dimension].join('-'))

    this.$element
      .one('bsTransitionEnd', $.proxy(complete, this))
      .emulateTransitionEnd(350)[dimension](this.$element[0][scrollSize])
  }

  Collapse.prototype.hide = function () {
    if (this.transitioning || !this.$element.hasClass('in')) return

    var startEvent = $.Event('hide.bs.collapse')
    this.$element.trigger(startEvent)
    if (startEvent.isDefaultPrevented()) return

    var dimension = this.dimension()

    this.$element[dimension](this.$element[dimension]())[0].offsetHeight

    this.$element
      .addClass('collapsing')
      .removeClass('collapse')
      .removeClass('in')

    this.transitioning = 1

    var complete = function () {
      this.transitioning = 0
      this.$element
        .trigger('hidden.bs.collapse')
        .removeClass('collapsing')
        .addClass('collapse')
    }

    if (!$.support.transition) return complete.call(this)

    this.$element
      [dimension](0)
      .one('bsTransitionEnd', $.proxy(complete, this))
      .emulateTransitionEnd(350)
  }

  Collapse.prototype.toggle = function () {
    this[this.$element.hasClass('in') ? 'hide' : 'show']()
  }


  // COLLAPSE PLUGIN DEFINITION
  // ==========================

  function Plugin(option) {
    return this.each(function () {
      var $this   = $(this)
      var data    = $this.data('bs.collapse')
      var options = $.extend({}, Collapse.DEFAULTS, $this.data(), typeof option == 'object' && option)

      if (!data && options.toggle && option == 'show') option = !option
      if (!data) $this.data('bs.collapse', (data = new Collapse(this, options)))
      if (typeof option == 'string') data[option]()
    })
  }

  var old = $.fn.collapse

  $.fn.collapse             = Plugin
  $.fn.collapse.Constructor = Collapse


  // COLLAPSE NO CONFLICT
  // ====================

  $.fn.collapse.noConflict = function () {
    $.fn.collapse = old
    return this
  }


  // COLLAPSE DATA-API
  // =================

  $(document).on('click.bs.collapse.data-api', '[data-toggle="collapse"]', function (e) {
    var href
    var $this   = $(this)
    var target  = $this.attr('data-target')
        || e.preventDefault()
        || (href = $this.attr('href')) && href.replace(/.*(?=#[^\s]+$)/, '') // strip for ie7
    var $target = $(target)
    var data    = $target.data('bs.collapse')
    var option  = data ? 'toggle' : $this.data()
    var parent  = $this.attr('data-parent')
    var $parent = parent && $(parent)

    if (!data || !data.transitioning) {
      if ($parent) $parent.find('[data-toggle="collapse"][data-parent="' + parent + '"]').not($this).addClass('collapsed')
      $this[$target.hasClass('in') ? 'addClass' : 'removeClass']('collapsed')
    }

    Plugin.call($target, option)
  })

}(jQuery);

/* ========================================================================
 * Bootstrap: dropdown.js v3.2.0
 * http://getbootstrap.com/javascript/#dropdowns
 * ========================================================================
 * Copyright 2011-2014 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 * ======================================================================== */


+function ($) {
  'use strict';

  // DROPDOWN CLASS DEFINITION
  // =========================

  var backdrop = '.dropdown-backdrop'
  var toggle   = '[data-toggle="dropdown"]'
  var Dropdown = function (element) {
    $(element).on('click.bs.dropdown', this.toggle)
  }

  Dropdown.VERSION = '3.2.0'

  Dropdown.prototype.toggle = function (e) {
    var $this = $(this)

    if ($this.is('.disabled, :disabled')) return

    var $parent  = getParent($this)
    var isActive = $parent.hasClass('open')

    clearMenus()

    if (!isActive) {
      if ('ontouchstart' in document.documentElement && !$parent.closest('.navbar-nav').length) {
        // if mobile we use a backdrop because click events don't delegate
        $('<div class="dropdown-backdrop"/>').insertAfter($(this)).on('click', clearMenus)
      }

      var relatedTarget = { relatedTarget: this }
      $parent.trigger(e = $.Event('show.bs.dropdown', relatedTarget))

      if (e.isDefaultPrevented()) return

      $this.trigger('focus')

      $parent
        .toggleClass('open')
        .trigger('shown.bs.dropdown', relatedTarget)
    }

    return false
  }

  Dropdown.prototype.keydown = function (e) {
    if (!/(38|40|27)/.test(e.keyCode)) return

    var $this = $(this)

    e.preventDefault()
    e.stopPropagation()

    if ($this.is('.disabled, :disabled')) return

    var $parent  = getParent($this)
    var isActive = $parent.hasClass('open')

    if (!isActive || (isActive && e.keyCode == 27)) {
      if (e.which == 27) $parent.find(toggle).trigger('focus')
      return $this.trigger('click')
    }

    var desc = ' li:not(.divider):visible a'
    var $items = $parent.find('[role="menu"]' + desc + ', [role="listbox"]' + desc)

    if (!$items.length) return

    var index = $items.index($items.filter(':focus'))

    if (e.keyCode == 38 && index > 0)                 index--                        // up
    if (e.keyCode == 40 && index < $items.length - 1) index++                        // down
    if (!~index)                                      index = 0

    $items.eq(index).trigger('focus')
  }

  function clearMenus(e) {
    if (e && e.which === 3) return
    $(backdrop).remove()
    $(toggle).each(function () {
      var $parent = getParent($(this))
      var relatedTarget = { relatedTarget: this }
      if (!$parent.hasClass('open')) return
      $parent.trigger(e = $.Event('hide.bs.dropdown', relatedTarget))
      if (e.isDefaultPrevented()) return
      $parent.removeClass('open').trigger('hidden.bs.dropdown', relatedTarget)
    })
  }

  function getParent($this) {
    var selector = $this.attr('data-target')

    if (!selector) {
      selector = $this.attr('href')
      selector = selector && /#[A-Za-z]/.test(selector) && selector.replace(/.*(?=#[^\s]*$)/, '') // strip for ie7
    }

    var $parent = selector && $(selector)

    return $parent && $parent.length ? $parent : $this.parent()
  }


  // DROPDOWN PLUGIN DEFINITION
  // ==========================

  function Plugin(option) {
    return this.each(function () {
      var $this = $(this)
      var data  = $this.data('bs.dropdown')

      if (!data) $this.data('bs.dropdown', (data = new Dropdown(this)))
      if (typeof option == 'string') data[option].call($this)
    })
  }

  var old = $.fn.dropdown

  $.fn.dropdown             = Plugin
  $.fn.dropdown.Constructor = Dropdown


  // DROPDOWN NO CONFLICT
  // ====================

  $.fn.dropdown.noConflict = function () {
    $.fn.dropdown = old
    return this
  }


  // APPLY TO STANDARD DROPDOWN ELEMENTS
  // ===================================

  $(document)
    .on('click.bs.dropdown.data-api', clearMenus)
    .on('click.bs.dropdown.data-api', '.dropdown form', function (e) { e.stopPropagation() })
    .on('click.bs.dropdown.data-api', toggle, Dropdown.prototype.toggle)
    .on('keydown.bs.dropdown.data-api', toggle + ', [role="menu"], [role="listbox"]', Dropdown.prototype.keydown)

}(jQuery);

/* ========================================================================
 * Bootstrap: modal.js v3.2.0
 * http://getbootstrap.com/javascript/#modals
 * ========================================================================
 * Copyright 2011-2014 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 * ======================================================================== */


+function ($) {
  'use strict';

  // MODAL CLASS DEFINITION
  // ======================

  var Modal = function (element, options) {
    this.options        = options
    this.$body          = $(document.body)
    this.$element       = $(element)
    this.$backdrop      =
    this.isShown        = null
    this.scrollbarWidth = 0

    if (this.options.remote) {
      this.$element
        .find('.modal-content')
        .load(this.options.remote, $.proxy(function () {
          this.$element.trigger('loaded.bs.modal')
        }, this))
    }
  }

  Modal.VERSION  = '3.2.0'

  Modal.DEFAULTS = {
    backdrop: true,
    keyboard: true,
    show: true
  }

  Modal.prototype.toggle = function (_relatedTarget) {
    return this.isShown ? this.hide() : this.show(_relatedTarget)
  }

  Modal.prototype.show = function (_relatedTarget) {
    var that = this
    var e    = $.Event('show.bs.modal', { relatedTarget: _relatedTarget })

    this.$element.trigger(e)

    if (this.isShown || e.isDefaultPrevented()) return

    this.isShown = true

    this.checkScrollbar()
    this.$body.addClass('modal-open')

    this.setScrollbar()
    this.escape()

    this.$element.on('click.dismiss.bs.modal', '[data-dismiss="modal"]', $.proxy(this.hide, this))

    this.backdrop(function () {
      var transition = $.support.transition && that.$element.hasClass('fade')

      if (!that.$element.parent().length) {
        that.$element.appendTo(that.$body) // don't move modals dom position
      }

      that.$element
        .show()
        .scrollTop(0)

      if (transition) {
        that.$element[0].offsetWidth // force reflow
      }

      that.$element
        .addClass('in')
        .attr('aria-hidden', false)

      that.enforceFocus()

      var e = $.Event('shown.bs.modal', { relatedTarget: _relatedTarget })

      transition ?
        that.$element.find('.modal-dialog') // wait for modal to slide in
          .one('bsTransitionEnd', function () {
            that.$element.trigger('focus').trigger(e)
          })
          .emulateTransitionEnd(300) :
        that.$element.trigger('focus').trigger(e)
    })
  }

  Modal.prototype.hide = function (e) {
    if (e) e.preventDefault()

    e = $.Event('hide.bs.modal')

    this.$element.trigger(e)

    if (!this.isShown || e.isDefaultPrevented()) return

    this.isShown = false

    this.$body.removeClass('modal-open')

    this.resetScrollbar()
    this.escape()

    $(document).off('focusin.bs.modal')

    this.$element
      .removeClass('in')
      .attr('aria-hidden', true)
      .off('click.dismiss.bs.modal')

    $.support.transition && this.$element.hasClass('fade') ?
      this.$element
        .one('bsTransitionEnd', $.proxy(this.hideModal, this))
        .emulateTransitionEnd(300) :
      this.hideModal()
  }

  Modal.prototype.enforceFocus = function () {
    $(document)
      .off('focusin.bs.modal') // guard against infinite focus loop
      .on('focusin.bs.modal', $.proxy(function (e) {
        if (this.$element[0] !== e.target && !this.$element.has(e.target).length) {
          this.$element.trigger('focus')
        }
      }, this))
  }

  Modal.prototype.escape = function () {
    if (this.isShown && this.options.keyboard) {
      this.$element.on('keyup.dismiss.bs.modal', $.proxy(function (e) {
        e.which == 27 && this.hide()
      }, this))
    } else if (!this.isShown) {
      this.$element.off('keyup.dismiss.bs.modal')
    }
  }

  Modal.prototype.hideModal = function () {
    var that = this
    this.$element.hide()
    this.backdrop(function () {
      that.$element.trigger('hidden.bs.modal')
    })
  }

  Modal.prototype.removeBackdrop = function () {
    this.$backdrop && this.$backdrop.remove()
    this.$backdrop = null
  }

  Modal.prototype.backdrop = function (callback) {
    var that = this
    var animate = this.$element.hasClass('fade') ? 'fade' : ''

    if (this.isShown && this.options.backdrop) {
      var doAnimate = $.support.transition && animate

      this.$backdrop = $('<div class="modal-backdrop ' + animate + '" />')
        .appendTo(this.$body)

      this.$element.on('click.dismiss.bs.modal', $.proxy(function (e) {
        if (e.target !== e.currentTarget) return
        this.options.backdrop == 'static'
          ? this.$element[0].focus.call(this.$element[0])
          : this.hide.call(this)
      }, this))

      if (doAnimate) this.$backdrop[0].offsetWidth // force reflow

      this.$backdrop.addClass('in')

      if (!callback) return

      doAnimate ?
        this.$backdrop
          .one('bsTransitionEnd', callback)
          .emulateTransitionEnd(150) :
        callback()

    } else if (!this.isShown && this.$backdrop) {
      this.$backdrop.removeClass('in')

      var callbackRemove = function () {
        that.removeBackdrop()
        callback && callback()
      }
      $.support.transition && this.$element.hasClass('fade') ?
        this.$backdrop
          .one('bsTransitionEnd', callbackRemove)
          .emulateTransitionEnd(150) :
        callbackRemove()

    } else if (callback) {
      callback()
    }
  }

  Modal.prototype.checkScrollbar = function () {
    if (document.body.clientWidth >= window.innerWidth) return
    this.scrollbarWidth = this.scrollbarWidth || this.measureScrollbar()
  }

  Modal.prototype.setScrollbar = function () {
    var bodyPad = parseInt((this.$body.css('padding-right') || 0), 10)
    if (this.scrollbarWidth) this.$body.css('padding-right', bodyPad + this.scrollbarWidth)
  }

  Modal.prototype.resetScrollbar = function () {
    this.$body.css('padding-right', '')
  }

  Modal.prototype.measureScrollbar = function () { // thx walsh
    var scrollDiv = document.createElement('div')
    scrollDiv.className = 'modal-scrollbar-measure'
    this.$body.append(scrollDiv)
    var scrollbarWidth = scrollDiv.offsetWidth - scrollDiv.clientWidth
    this.$body[0].removeChild(scrollDiv)
    return scrollbarWidth
  }


  // MODAL PLUGIN DEFINITION
  // =======================

  function Plugin(option, _relatedTarget) {
    return this.each(function () {
      var $this   = $(this)
      var data    = $this.data('bs.modal')
      var options = $.extend({}, Modal.DEFAULTS, $this.data(), typeof option == 'object' && option)

      if (!data) $this.data('bs.modal', (data = new Modal(this, options)))
      if (typeof option == 'string') data[option](_relatedTarget)
      else if (options.show) data.show(_relatedTarget)
    })
  }

  var old = $.fn.modal

  $.fn.modal             = Plugin
  $.fn.modal.Constructor = Modal


  // MODAL NO CONFLICT
  // =================

  $.fn.modal.noConflict = function () {
    $.fn.modal = old
    return this
  }


  // MODAL DATA-API
  // ==============

  $(document).on('click.bs.modal.data-api', '[data-toggle="modal"]', function (e) {
    var $this   = $(this)
    var href    = $this.attr('href')
    var $target = $($this.attr('data-target') || (href && href.replace(/.*(?=#[^\s]+$)/, ''))) // strip for ie7
    var option  = $target.data('bs.modal') ? 'toggle' : $.extend({ remote: !/#/.test(href) && href }, $target.data(), $this.data())

    if ($this.is('a')) e.preventDefault()

    $target.one('show.bs.modal', function (showEvent) {
      if (showEvent.isDefaultPrevented()) return // only register focus restorer if modal will actually get shown
      $target.one('hidden.bs.modal', function () {
        $this.is(':visible') && $this.trigger('focus')
      })
    })
    Plugin.call($target, option, this)
  })

}(jQuery);

/* ========================================================================
 * Bootstrap: tooltip.js v3.2.0
 * http://getbootstrap.com/javascript/#tooltip
 * Inspired by the original jQuery.tipsy by Jason Frame
 * ========================================================================
 * Copyright 2011-2014 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 * ======================================================================== */


+function ($) {
  'use strict';

  // TOOLTIP PUBLIC CLASS DEFINITION
  // ===============================

  var Tooltip = function (element, options) {
    this.type       =
    this.options    =
    this.enabled    =
    this.timeout    =
    this.hoverState =
    this.$element   = null

    this.init('tooltip', element, options)
  }

  Tooltip.VERSION  = '3.2.0'

  Tooltip.DEFAULTS = {
    animation: true,
    placement: 'top',
    selector: false,
    template: '<div class="tooltip" role="tooltip"><div class="tooltip-arrow"></div><div class="tooltip-inner"></div></div>',
    trigger: 'hover focus',
    title: '',
    delay: 0,
    html: false,
    container: false,
    viewport: {
      selector: 'body',
      padding: 0
    }
  }

  Tooltip.prototype.init = function (type, element, options) {
    this.enabled   = true
    this.type      = type
    this.$element  = $(element)
    this.options   = this.getOptions(options)
    this.$viewport = this.options.viewport && $(this.options.viewport.selector || this.options.viewport)

    var triggers = this.options.trigger.split(' ')

    for (var i = triggers.length; i--;) {
      var trigger = triggers[i]

      if (trigger == 'click') {
        this.$element.on('click.' + this.type, this.options.selector, $.proxy(this.toggle, this))
      } else if (trigger != 'manual') {
        var eventIn  = trigger == 'hover' ? 'mouseenter' : 'focusin'
        var eventOut = trigger == 'hover' ? 'mouseleave' : 'focusout'

        this.$element.on(eventIn  + '.' + this.type, this.options.selector, $.proxy(this.enter, this))
        this.$element.on(eventOut + '.' + this.type, this.options.selector, $.proxy(this.leave, this))
      }
    }

    this.options.selector ?
      (this._options = $.extend({}, this.options, { trigger: 'manual', selector: '' })) :
      this.fixTitle()
  }

  Tooltip.prototype.getDefaults = function () {
    return Tooltip.DEFAULTS
  }

  Tooltip.prototype.getOptions = function (options) {
    options = $.extend({}, this.getDefaults(), this.$element.data(), options)

    if (options.delay && typeof options.delay == 'number') {
      options.delay = {
        show: options.delay,
        hide: options.delay
      }
    }

    return options
  }

  Tooltip.prototype.getDelegateOptions = function () {
    var options  = {}
    var defaults = this.getDefaults()

    this._options && $.each(this._options, function (key, value) {
      if (defaults[key] != value) options[key] = value
    })

    return options
  }

  Tooltip.prototype.enter = function (obj) {
    var self = obj instanceof this.constructor ?
      obj : $(obj.currentTarget).data('bs.' + this.type)

    if (!self) {
      self = new this.constructor(obj.currentTarget, this.getDelegateOptions())
      $(obj.currentTarget).data('bs.' + this.type, self)
    }

    clearTimeout(self.timeout)

    self.hoverState = 'in'

    if (!self.options.delay || !self.options.delay.show) return self.show()

    self.timeout = setTimeout(function () {
      if (self.hoverState == 'in') self.show()
    }, self.options.delay.show)
  }

  Tooltip.prototype.leave = function (obj) {
    var self = obj instanceof this.constructor ?
      obj : $(obj.currentTarget).data('bs.' + this.type)

    if (!self) {
      self = new this.constructor(obj.currentTarget, this.getDelegateOptions())
      $(obj.currentTarget).data('bs.' + this.type, self)
    }

    clearTimeout(self.timeout)

    self.hoverState = 'out'

    if (!self.options.delay || !self.options.delay.hide) return self.hide()

    self.timeout = setTimeout(function () {
      if (self.hoverState == 'out') self.hide()
    }, self.options.delay.hide)
  }

  Tooltip.prototype.show = function () {
    var e = $.Event('show.bs.' + this.type)

    if (this.hasContent() && this.enabled) {
      this.$element.trigger(e)

      var inDom = $.contains(document.documentElement, this.$element[0])
      if (e.isDefaultPrevented() || !inDom) return
      var that = this

      var $tip = this.tip()

      var tipId = this.getUID(this.type)

      this.setContent()
      $tip.attr('id', tipId)
      this.$element.attr('aria-describedby', tipId)

      if (this.options.animation) $tip.addClass('fade')

      var placement = typeof this.options.placement == 'function' ?
        this.options.placement.call(this, $tip[0], this.$element[0]) :
        this.options.placement

      var autoToken = /\s?auto?\s?/i
      var autoPlace = autoToken.test(placement)
      if (autoPlace) placement = placement.replace(autoToken, '') || 'top'

      $tip
        .detach()
        .css({ top: 0, left: 0, display: 'block' })
        .addClass(placement)
        .data('bs.' + this.type, this)

      this.options.container ? $tip.appendTo(this.options.container) : $tip.insertAfter(this.$element)

      var pos          = this.getPosition()
      var actualWidth  = $tip[0].offsetWidth
      var actualHeight = $tip[0].offsetHeight

      if (autoPlace) {
        var orgPlacement = placement
        var $parent      = this.$element.parent()
        var parentDim    = this.getPosition($parent)

        placement = placement == 'bottom' && pos.top   + pos.height       + actualHeight - parentDim.scroll > parentDim.height ? 'top'    :
                    placement == 'top'    && pos.top   - parentDim.scroll - actualHeight < 0                                   ? 'bottom' :
                    placement == 'right'  && pos.right + actualWidth      > parentDim.width                                    ? 'left'   :
                    placement == 'left'   && pos.left  - actualWidth      < parentDim.left                                     ? 'right'  :
                    placement

        $tip
          .removeClass(orgPlacement)
          .addClass(placement)
      }

      var calculatedOffset = this.getCalculatedOffset(placement, pos, actualWidth, actualHeight)

      this.applyPlacement(calculatedOffset, placement)

      var complete = function () {
        that.$element.trigger('shown.bs.' + that.type)
        that.hoverState = null
      }

      $.support.transition && this.$tip.hasClass('fade') ?
        $tip
          .one('bsTransitionEnd', complete)
          .emulateTransitionEnd(150) :
        complete()
    }
  }

  Tooltip.prototype.applyPlacement = function (offset, placement) {
    var $tip   = this.tip()
    var width  = $tip[0].offsetWidth
    var height = $tip[0].offsetHeight

    // manually read margins because getBoundingClientRect includes difference
    var marginTop = parseInt($tip.css('margin-top'), 10)
    var marginLeft = parseInt($tip.css('margin-left'), 10)

    // we must check for NaN for ie 8/9
    if (isNaN(marginTop))  marginTop  = 0
    if (isNaN(marginLeft)) marginLeft = 0

    offset.top  = offset.top  + marginTop
    offset.left = offset.left + marginLeft

    // $.fn.offset doesn't round pixel values
    // so we use setOffset directly with our own function B-0
    $.offset.setOffset($tip[0], $.extend({
      using: function (props) {
        $tip.css({
          top: Math.round(props.top),
          left: Math.round(props.left)
        })
      }
    }, offset), 0)

    $tip.addClass('in')

    // check to see if placing tip in new offset caused the tip to resize itself
    var actualWidth  = $tip[0].offsetWidth
    var actualHeight = $tip[0].offsetHeight

    if (placement == 'top' && actualHeight != height) {
      offset.top = offset.top + height - actualHeight
    }

    var delta = this.getViewportAdjustedDelta(placement, offset, actualWidth, actualHeight)

    if (delta.left) offset.left += delta.left
    else offset.top += delta.top

    var arrowDelta          = delta.left ? delta.left * 2 - width + actualWidth : delta.top * 2 - height + actualHeight
    var arrowPosition       = delta.left ? 'left'        : 'top'
    var arrowOffsetPosition = delta.left ? 'offsetWidth' : 'offsetHeight'

    $tip.offset(offset)
    this.replaceArrow(arrowDelta, $tip[0][arrowOffsetPosition], arrowPosition)
  }

  Tooltip.prototype.replaceArrow = function (delta, dimension, position) {
    this.arrow().css(position, delta ? (50 * (1 - delta / dimension) + '%') : '')
  }

  Tooltip.prototype.setContent = function () {
    var $tip  = this.tip()
    var title = this.getTitle()

    $tip.find('.tooltip-inner')[this.options.html ? 'html' : 'text'](title)
    $tip.removeClass('fade in top bottom left right')
  }

  Tooltip.prototype.hide = function () {
    var that = this
    var $tip = this.tip()
    var e    = $.Event('hide.bs.' + this.type)

    this.$element.removeAttr('aria-describedby')

    function complete() {
      if (that.hoverState != 'in') $tip.detach()
      that.$element.trigger('hidden.bs.' + that.type)
    }

    this.$element.trigger(e)

    if (e.isDefaultPrevented()) return

    $tip.removeClass('in')

    $.support.transition && this.$tip.hasClass('fade') ?
      $tip
        .one('bsTransitionEnd', complete)
        .emulateTransitionEnd(150) :
      complete()

    this.hoverState = null

    return this
  }

  Tooltip.prototype.fixTitle = function () {
    var $e = this.$element
    if ($e.attr('title') || typeof ($e.attr('data-original-title')) != 'string') {
      $e.attr('data-original-title', $e.attr('title') || '').attr('title', '')
    }
  }

  Tooltip.prototype.hasContent = function () {
    return this.getTitle()
  }

  Tooltip.prototype.getPosition = function ($element) {
    $element   = $element || this.$element
    var el     = $element[0]
    var isBody = el.tagName == 'BODY'
    return $.extend({}, (typeof el.getBoundingClientRect == 'function') ? el.getBoundingClientRect() : null, {
      scroll: isBody ? document.documentElement.scrollTop || document.body.scrollTop : $element.scrollTop(),
      width:  isBody ? $(window).width()  : $element.outerWidth(),
      height: isBody ? $(window).height() : $element.outerHeight()
    }, isBody ? { top: 0, left: 0 } : $element.offset())
  }

  Tooltip.prototype.getCalculatedOffset = function (placement, pos, actualWidth, actualHeight) {
    return placement == 'bottom' ? { top: pos.top + pos.height,   left: pos.left + pos.width / 2 - actualWidth / 2  } :
           placement == 'top'    ? { top: pos.top - actualHeight, left: pos.left + pos.width / 2 - actualWidth / 2  } :
           placement == 'left'   ? { top: pos.top + pos.height / 2 - actualHeight / 2, left: pos.left - actualWidth } :
        /* placement == 'right' */ { top: pos.top + pos.height / 2 - actualHeight / 2, left: pos.left + pos.width   }

  }

  Tooltip.prototype.getViewportAdjustedDelta = function (placement, pos, actualWidth, actualHeight) {
    var delta = { top: 0, left: 0 }
    if (!this.$viewport) return delta

    var viewportPadding = this.options.viewport && this.options.viewport.padding || 0
    var viewportDimensions = this.getPosition(this.$viewport)

    if (/right|left/.test(placement)) {
      var topEdgeOffset    = pos.top - viewportPadding - viewportDimensions.scroll
      var bottomEdgeOffset = pos.top + viewportPadding - viewportDimensions.scroll + actualHeight
      if (topEdgeOffset < viewportDimensions.top) { // top overflow
        delta.top = viewportDimensions.top - topEdgeOffset
      } else if (bottomEdgeOffset > viewportDimensions.top + viewportDimensions.height) { // bottom overflow
        delta.top = viewportDimensions.top + viewportDimensions.height - bottomEdgeOffset
      }
    } else {
      var leftEdgeOffset  = pos.left - viewportPadding
      var rightEdgeOffset = pos.left + viewportPadding + actualWidth
      if (leftEdgeOffset < viewportDimensions.left) { // left overflow
        delta.left = viewportDimensions.left - leftEdgeOffset
      } else if (rightEdgeOffset > viewportDimensions.width) { // right overflow
        delta.left = viewportDimensions.left + viewportDimensions.width - rightEdgeOffset
      }
    }

    return delta
  }

  Tooltip.prototype.getTitle = function () {
    var title
    var $e = this.$element
    var o  = this.options

    title = $e.attr('data-original-title')
      || (typeof o.title == 'function' ? o.title.call($e[0]) :  o.title)

    return title
  }

  Tooltip.prototype.getUID = function (prefix) {
    do prefix += ~~(Math.random() * 1000000)
    while (document.getElementById(prefix))
    return prefix
  }

  Tooltip.prototype.tip = function () {
    return (this.$tip = this.$tip || $(this.options.template))
  }

  Tooltip.prototype.arrow = function () {
    return (this.$arrow = this.$arrow || this.tip().find('.tooltip-arrow'))
  }

  Tooltip.prototype.validate = function () {
    if (!this.$element[0].parentNode) {
      this.hide()
      this.$element = null
      this.options  = null
    }
  }

  Tooltip.prototype.enable = function () {
    this.enabled = true
  }

  Tooltip.prototype.disable = function () {
    this.enabled = false
  }

  Tooltip.prototype.toggleEnabled = function () {
    this.enabled = !this.enabled
  }

  Tooltip.prototype.toggle = function (e) {
    var self = this
    if (e) {
      self = $(e.currentTarget).data('bs.' + this.type)
      if (!self) {
        self = new this.constructor(e.currentTarget, this.getDelegateOptions())
        $(e.currentTarget).data('bs.' + this.type, self)
      }
    }

    self.tip().hasClass('in') ? self.leave(self) : self.enter(self)
  }

  Tooltip.prototype.destroy = function () {
    clearTimeout(this.timeout)
    this.hide().$element.off('.' + this.type).removeData('bs.' + this.type)
  }


  // TOOLTIP PLUGIN DEFINITION
  // =========================

  function Plugin(option) {
    return this.each(function () {
      var $this   = $(this)
      var data    = $this.data('bs.tooltip')
      var options = typeof option == 'object' && option

      if (!data && option == 'destroy') return
      if (!data) $this.data('bs.tooltip', (data = new Tooltip(this, options)))
      if (typeof option == 'string') data[option]()
    })
  }

  var old = $.fn.tooltip

  $.fn.tooltip             = Plugin
  $.fn.tooltip.Constructor = Tooltip


  // TOOLTIP NO CONFLICT
  // ===================

  $.fn.tooltip.noConflict = function () {
    $.fn.tooltip = old
    return this
  }

}(jQuery);

/* ========================================================================
 * Bootstrap: popover.js v3.2.0
 * http://getbootstrap.com/javascript/#popovers
 * ========================================================================
 * Copyright 2011-2014 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 * ======================================================================== */


+function ($) {
  'use strict';

  // POPOVER PUBLIC CLASS DEFINITION
  // ===============================

  var Popover = function (element, options) {
    this.init('popover', element, options)
  }

  if (!$.fn.tooltip) throw new Error('Popover requires tooltip.js')

  Popover.VERSION  = '3.2.0'

  Popover.DEFAULTS = $.extend({}, $.fn.tooltip.Constructor.DEFAULTS, {
    placement: 'right',
    trigger: 'click',
    content: '',
    template: '<div class="popover" role="tooltip"><div class="arrow"></div><h3 class="popover-title"></h3><div class="popover-content"></div></div>'
  })


  // NOTE: POPOVER EXTENDS tooltip.js
  // ================================

  Popover.prototype = $.extend({}, $.fn.tooltip.Constructor.prototype)

  Popover.prototype.constructor = Popover

  Popover.prototype.getDefaults = function () {
    return Popover.DEFAULTS
  }

  Popover.prototype.setContent = function () {
    var $tip    = this.tip()
    var title   = this.getTitle()
    var content = this.getContent()

    $tip.find('.popover-title')[this.options.html ? 'html' : 'text'](title)
    $tip.find('.popover-content').empty()[ // we use append for html objects to maintain js events
      this.options.html ? (typeof content == 'string' ? 'html' : 'append') : 'text'
    ](content)

    $tip.removeClass('fade top bottom left right in')

    // IE8 doesn't accept hiding via the `:empty` pseudo selector, we have to do
    // this manually by checking the contents.
    if (!$tip.find('.popover-title').html()) $tip.find('.popover-title').hide()
  }

  Popover.prototype.hasContent = function () {
    return this.getTitle() || this.getContent()
  }

  Popover.prototype.getContent = function () {
    var $e = this.$element
    var o  = this.options

    return $e.attr('data-content')
      || (typeof o.content == 'function' ?
            o.content.call($e[0]) :
            o.content)
  }

  Popover.prototype.arrow = function () {
    return (this.$arrow = this.$arrow || this.tip().find('.arrow'))
  }

  Popover.prototype.tip = function () {
    if (!this.$tip) this.$tip = $(this.options.template)
    return this.$tip
  }


  // POPOVER PLUGIN DEFINITION
  // =========================

  function Plugin(option) {
    return this.each(function () {
      var $this   = $(this)
      var data    = $this.data('bs.popover')
      var options = typeof option == 'object' && option

      if (!data && option == 'destroy') return
      if (!data) $this.data('bs.popover', (data = new Popover(this, options)))
      if (typeof option == 'string') data[option]()
    })
  }

  var old = $.fn.popover

  $.fn.popover             = Plugin
  $.fn.popover.Constructor = Popover


  // POPOVER NO CONFLICT
  // ===================

  $.fn.popover.noConflict = function () {
    $.fn.popover = old
    return this
  }

}(jQuery);

/* ========================================================================
 * Bootstrap: scrollspy.js v3.2.0
 * http://getbootstrap.com/javascript/#scrollspy
 * ========================================================================
 * Copyright 2011-2014 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 * ======================================================================== */


+function ($) {
  'use strict';

  // SCROLLSPY CLASS DEFINITION
  // ==========================

  function ScrollSpy(element, options) {
    var process  = $.proxy(this.process, this)

    this.$body          = $('body')
    this.$scrollElement = $(element).is('body') ? $(window) : $(element)
    this.options        = $.extend({}, ScrollSpy.DEFAULTS, options)
    this.selector       = (this.options.target || '') + ' .nav li > a'
    this.offsets        = []
    this.targets        = []
    this.activeTarget   = null
    this.scrollHeight   = 0

    this.$scrollElement.on('scroll.bs.scrollspy', process)
    this.refresh()
    this.process()
  }

  ScrollSpy.VERSION  = '3.2.0'

  ScrollSpy.DEFAULTS = {
    offset: 10
  }

  ScrollSpy.prototype.getScrollHeight = function () {
    return this.$scrollElement[0].scrollHeight || Math.max(this.$body[0].scrollHeight, document.documentElement.scrollHeight)
  }

  ScrollSpy.prototype.refresh = function () {
    var offsetMethod = 'offset'
    var offsetBase   = 0

    if (!$.isWindow(this.$scrollElement[0])) {
      offsetMethod = 'position'
      offsetBase   = this.$scrollElement.scrollTop()
    }

    this.offsets = []
    this.targets = []
    this.scrollHeight = this.getScrollHeight()

    var self     = this

    this.$body
      .find(this.selector)
      .map(function () {
        var $el   = $(this)
        var href  = $el.data('target') || $el.attr('href')
        var $href = /^#./.test(href) && $(href)

        return ($href
          && $href.length
          && $href.is(':visible')
          && [[$href[offsetMethod]().top + offsetBase, href]]) || null
      })
      .sort(function (a, b) { return a[0] - b[0] })
      .each(function () {
        self.offsets.push(this[0])
        self.targets.push(this[1])
      })
  }

  ScrollSpy.prototype.process = function () {
    var scrollTop    = this.$scrollElement.scrollTop() + this.options.offset
    var scrollHeight = this.getScrollHeight()
    var maxScroll    = this.options.offset + scrollHeight - this.$scrollElement.height()
    var offsets      = this.offsets
    var targets      = this.targets
    var activeTarget = this.activeTarget
    var i

    if (this.scrollHeight != scrollHeight) {
      this.refresh()
    }

    if (scrollTop >= maxScroll) {
      return activeTarget != (i = targets[targets.length - 1]) && this.activate(i)
    }

    if (activeTarget && scrollTop <= offsets[0]) {
      return activeTarget != (i = targets[0]) && this.activate(i)
    }

    for (i = offsets.length; i--;) {
      activeTarget != targets[i]
        && scrollTop >= offsets[i]
        && (!offsets[i + 1] || scrollTop <= offsets[i + 1])
        && this.activate(targets[i])
    }
  }

  ScrollSpy.prototype.activate = function (target) {
    this.activeTarget = target

    $(this.selector)
      .parentsUntil(this.options.target, '.active')
      .removeClass('active')

    var selector = this.selector +
        '[data-target="' + target + '"],' +
        this.selector + '[href="' + target + '"]'

    var active = $(selector)
      .parents('li')
      .addClass('active')

    if (active.parent('.dropdown-menu').length) {
      active = active
        .closest('li.dropdown')
        .addClass('active')
    }

    active.trigger('activate.bs.scrollspy')
  }


  // SCROLLSPY PLUGIN DEFINITION
  // ===========================

  function Plugin(option) {
    return this.each(function () {
      var $this   = $(this)
      var data    = $this.data('bs.scrollspy')
      var options = typeof option == 'object' && option

      if (!data) $this.data('bs.scrollspy', (data = new ScrollSpy(this, options)))
      if (typeof option == 'string') data[option]()
    })
  }

  var old = $.fn.scrollspy

  $.fn.scrollspy             = Plugin
  $.fn.scrollspy.Constructor = ScrollSpy


  // SCROLLSPY NO CONFLICT
  // =====================

  $.fn.scrollspy.noConflict = function () {
    $.fn.scrollspy = old
    return this
  }


  // SCROLLSPY DATA-API
  // ==================

  $(window).on('load.bs.scrollspy.data-api', function () {
    $('[data-spy="scroll"]').each(function () {
      var $spy = $(this)
      Plugin.call($spy, $spy.data())
    })
  })

}(jQuery);

/* ========================================================================
 * Bootstrap: tab.js v3.2.0
 * http://getbootstrap.com/javascript/#tabs
 * ========================================================================
 * Copyright 2011-2014 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 * ======================================================================== */


+function ($) {
  'use strict';

  // TAB CLASS DEFINITION
  // ====================

  var Tab = function (element) {
    this.element = $(element)
  }

  Tab.VERSION = '3.2.0'

  Tab.prototype.show = function () {
    var $this    = this.element
    var $ul      = $this.closest('ul:not(.dropdown-menu)')
    var selector = $this.data('target')

    if (!selector) {
      selector = $this.attr('href')
      selector = selector && selector.replace(/.*(?=#[^\s]*$)/, '') // strip for ie7
    }

    if ($this.parent('li').hasClass('active')) return

    var previous = $ul.find('.active:last a')[0]
    var e        = $.Event('show.bs.tab', {
      relatedTarget: previous
    })

    $this.trigger(e)

    if (e.isDefaultPrevented()) return

    var $target = $(selector)

    this.activate($this.closest('li'), $ul)
    this.activate($target, $target.parent(), function () {
      $this.trigger({
        type: 'shown.bs.tab',
        relatedTarget: previous
      })
    })
  }

  Tab.prototype.activate = function (element, container, callback) {
    var $active    = container.find('> .active')
    var transition = callback
      && $.support.transition
      && $active.hasClass('fade')

    function next() {
      $active
        .removeClass('active')
        .find('> .dropdown-menu > .active')
        .removeClass('active')

      element.addClass('active')

      if (transition) {
        element[0].offsetWidth // reflow for transition
        element.addClass('in')
      } else {
        element.removeClass('fade')
      }

      if (element.parent('.dropdown-menu')) {
        element.closest('li.dropdown').addClass('active')
      }

      callback && callback()
    }

    transition ?
      $active
        .one('bsTransitionEnd', next)
        .emulateTransitionEnd(150) :
      next()

    $active.removeClass('in')
  }


  // TAB PLUGIN DEFINITION
  // =====================

  function Plugin(option) {
    return this.each(function () {
      var $this = $(this)
      var data  = $this.data('bs.tab')

      if (!data) $this.data('bs.tab', (data = new Tab(this)))
      if (typeof option == 'string') data[option]()
    })
  }

  var old = $.fn.tab

  $.fn.tab             = Plugin
  $.fn.tab.Constructor = Tab


  // TAB NO CONFLICT
  // ===============

  $.fn.tab.noConflict = function () {
    $.fn.tab = old
    return this
  }


  // TAB DATA-API
  // ============

  $(document).on('click.bs.tab.data-api', '[data-toggle="tab"], [data-toggle="pill"]', function (e) {
    e.preventDefault()
    Plugin.call($(this), 'show')
  })

}(jQuery);

/* ========================================================================
 * Bootstrap: affix.js v3.2.0
 * http://getbootstrap.com/javascript/#affix
 * ========================================================================
 * Copyright 2011-2014 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 * ======================================================================== */


+function ($) {
  'use strict';

  // AFFIX CLASS DEFINITION
  // ======================

  var Affix = function (element, options) {
    this.options = $.extend({}, Affix.DEFAULTS, options)

    this.$target = $(this.options.target)
      .on('scroll.bs.affix.data-api', $.proxy(this.checkPosition, this))
      .on('click.bs.affix.data-api',  $.proxy(this.checkPositionWithEventLoop, this))

    this.$element     = $(element)
    this.affixed      =
    this.unpin        =
    this.pinnedOffset = null

    this.checkPosition()
  }

  Affix.VERSION  = '3.2.0'

  Affix.RESET    = 'affix affix-top affix-bottom'

  Affix.DEFAULTS = {
    offset: 0,
    target: window
  }

  Affix.prototype.getPinnedOffset = function () {
    if (this.pinnedOffset) return this.pinnedOffset
    this.$element.removeClass(Affix.RESET).addClass('affix')
    var scrollTop = this.$target.scrollTop()
    var position  = this.$element.offset()
    return (this.pinnedOffset = position.top - scrollTop)
  }

  Affix.prototype.checkPositionWithEventLoop = function () {
    setTimeout($.proxy(this.checkPosition, this), 1)
  }

  Affix.prototype.checkPosition = function () {
    if (!this.$element.is(':visible')) return

    var scrollHeight = $(document).height()
    var scrollTop    = this.$target.scrollTop()
    var position     = this.$element.offset()
    var offset       = this.options.offset
    var offsetTop    = offset.top
    var offsetBottom = offset.bottom

    if (typeof offset != 'object')         offsetBottom = offsetTop = offset
    if (typeof offsetTop == 'function')    offsetTop    = offset.top(this.$element)
    if (typeof offsetBottom == 'function') offsetBottom = offset.bottom(this.$element)

    var affix = this.unpin   != null && (scrollTop + this.unpin <= position.top) ? false :
                offsetBottom != null && (position.top + this.$element.height() >= scrollHeight - offsetBottom) ? 'bottom' :
                offsetTop    != null && (scrollTop <= offsetTop) ? 'top' : false

    if (this.affixed === affix) return
    if (this.unpin != null) this.$element.css('top', '')

    var affixType = 'affix' + (affix ? '-' + affix : '')
    var e         = $.Event(affixType + '.bs.affix')

    this.$element.trigger(e)

    if (e.isDefaultPrevented()) return

    this.affixed = affix
    this.unpin = affix == 'bottom' ? this.getPinnedOffset() : null

    this.$element
      .removeClass(Affix.RESET)
      .addClass(affixType)
      .trigger($.Event(affixType.replace('affix', 'affixed')))

    if (affix == 'bottom') {
      this.$element.offset({
        top: scrollHeight - this.$element.height() - offsetBottom
      })
    }
  }


  // AFFIX PLUGIN DEFINITION
  // =======================

  function Plugin(option) {
    return this.each(function () {
      var $this   = $(this)
      var data    = $this.data('bs.affix')
      var options = typeof option == 'object' && option

      if (!data) $this.data('bs.affix', (data = new Affix(this, options)))
      if (typeof option == 'string') data[option]()
    })
  }

  var old = $.fn.affix

  $.fn.affix             = Plugin
  $.fn.affix.Constructor = Affix


  // AFFIX NO CONFLICT
  // =================

  $.fn.affix.noConflict = function () {
    $.fn.affix = old
    return this
  }


  // AFFIX DATA-API
  // ==============

  $(window).on('load', function () {
    $('[data-spy="affix"]').each(function () {
      var $spy = $(this)
      var data = $spy.data()

      data.offset = data.offset || {}

      if (data.offsetBottom) data.offset.bottom = data.offsetBottom
      if (data.offsetTop)    data.offset.top    = data.offsetTop

      Plugin.call($spy, data)
    })
  })

}(jQuery);

/**
 * bootbox.js [v4.4.0]
 *
 * http://bootboxjs.com/license.txt
 */

// @see https://github.com/makeusabrew/bootbox/issues/180
// @see https://github.com/makeusabrew/bootbox/issues/186
(function (root, factory) {

  "use strict";
  if (typeof define === "function" && define.amd) {
    // AMD. Register as an anonymous module.
    define(["jquery"], factory);
  } else if (typeof exports === "object") {
    // Node. Does not work with strict CommonJS, but
    // only CommonJS-like environments that support module.exports,
    // like Node.
    module.exports = factory(require("jquery"));
  } else {
    // Browser globals (root is window)
    root.bootbox = factory(root.jQuery);
  }

}(this, function init($, undefined) {

  "use strict";

  // the base DOM structure needed to create a modal
  var templates = {
    dialog:
      "<div class='bootbox modal' tabindex='-1' role='dialog'>" +
        "<div class='modal-dialog'>" +
          "<div class='modal-content'>" +
            "<div class='modal-body'><div class='bootbox-body'></div></div>" +
          "</div>" +
        "</div>" +
      "</div>",
    header:
      "<div class='modal-header'>" +
        "<h4 class='modal-title'></h4>" +
      "</div>",
    footer:
      "<div class='modal-footer'></div>",
    closeButton:
      "<button type='button' class='bootbox-close-button close' data-dismiss='modal' aria-hidden='true'>&times;</button>",
    form:
      "<form class='bootbox-form'></form>",
    inputs: {
      text:
        "<input class='bootbox-input bootbox-input-text form-control' autocomplete=off type=text />",
      textarea:
        "<textarea class='bootbox-input bootbox-input-textarea form-control'></textarea>",
      email:
        "<input class='bootbox-input bootbox-input-email form-control' autocomplete='off' type='email' />",
      select:
        "<select class='bootbox-input bootbox-input-select form-control'></select>",
      checkbox:
        "<div class='checkbox'><label><input class='bootbox-input bootbox-input-checkbox' type='checkbox' /></label></div>",
      date:
        "<input class='bootbox-input bootbox-input-date form-control' autocomplete=off type='date' />",
      time:
        "<input class='bootbox-input bootbox-input-time form-control' autocomplete=off type='time' />",
      number:
        "<input class='bootbox-input bootbox-input-number form-control' autocomplete=off type='number' />",
      password:
        "<input class='bootbox-input bootbox-input-password form-control' autocomplete='off' type='password' />"
    }
  };

  var defaults = {
    // default language
    locale: "en",
    // show backdrop or not. Default to static so user has to interact with dialog
    backdrop: "static",
    // animate the modal in/out
    animate: true,
    // additional class string applied to the top level dialog
    className: null,
    // whether or not to include a close button
    closeButton: true,
    // show the dialog immediately by default
    show: true,
    // dialog container
    container: "body"
  };

  // our public object; augmented after our private API
  var exports = {};

  /**
   * @private
   */
  function _t(key) {
    var locale = locales[defaults.locale];
    return locale ? locale[key] : locales.en[key];
  }

  function processCallback(e, dialog, callback) {
    e.stopPropagation();
    e.preventDefault();

    // by default we assume a callback will get rid of the dialog,
    // although it is given the opportunity to override this

    // so, if the callback can be invoked and it *explicitly returns false*
    // then we'll set a flag to keep the dialog active...
    var preserveDialog = $.isFunction(callback) && callback.call(dialog, e) === false;

    // ... otherwise we'll bin it
    if (!preserveDialog) {
      dialog.modal("hide");
    }
  }

  function getKeyLength(obj) {
    // @TODO defer to Object.keys(x).length if available?
    var k, t = 0;
    for (k in obj) {
      t ++;
    }
    return t;
  }

  function each(collection, iterator) {
    var index = 0;
    $.each(collection, function(key, value) {
      iterator(key, value, index++);
    });
  }

  function sanitize(options) {
    var buttons;
    var total;

    if (typeof options !== "object") {
      throw new Error("Please supply an object of options");
    }

    if (!options.message) {
      throw new Error("Please specify a message");
    }

    // make sure any supplied options take precedence over defaults
    options = $.extend({}, defaults, options);

    if (!options.buttons) {
      options.buttons = {};
    }

    buttons = options.buttons;

    total = getKeyLength(buttons);

    each(buttons, function(key, button, index) {

      if ($.isFunction(button)) {
        // short form, assume value is our callback. Since button
        // isn't an object it isn't a reference either so re-assign it
        button = buttons[key] = {
          callback: button
        };
      }

      // before any further checks make sure by now button is the correct type
      if ($.type(button) !== "object") {
        throw new Error("button with key " + key + " must be an object");
      }

      if (!button.label) {
        // the lack of an explicit label means we'll assume the key is good enough
        button.label = key;
      }

      if (!button.className) {
        if (total <= 2 && index === total-1) {
          // always add a primary to the main option in a two-button dialog
          button.className = "btn-primary";
        } else {
          button.className = "btn-default";
        }
      }
    });

    return options;
  }

  /**
   * map a flexible set of arguments into a single returned object
   * if args.length is already one just return it, otherwise
   * use the properties argument to map the unnamed args to
   * object properties
   * so in the latter case:
   * mapArguments(["foo", $.noop], ["message", "callback"])
   * -> { message: "foo", callback: $.noop }
   */
  function mapArguments(args, properties) {
    var argn = args.length;
    var options = {};

    if (argn < 1 || argn > 2) {
      throw new Error("Invalid argument length");
    }

    if (argn === 2 || typeof args[0] === "string") {
      options[properties[0]] = args[0];
      options[properties[1]] = args[1];
    } else {
      options = args[0];
    }

    return options;
  }

  /**
   * merge a set of default dialog options with user supplied arguments
   */
  function mergeArguments(defaults, args, properties) {
    return $.extend(
      // deep merge
      true,
      // ensure the target is an empty, unreferenced object
      {},
      // the base options object for this type of dialog (often just buttons)
      defaults,
      // args could be an object or array; if it's an array properties will
      // map it to a proper options object
      mapArguments(
        args,
        properties
      )
    );
  }

  /**
   * this entry-level method makes heavy use of composition to take a simple
   * range of inputs and return valid options suitable for passing to bootbox.dialog
   */
  function mergeDialogOptions(className, labels, properties, args) {
    //  build up a base set of dialog properties
    var baseOptions = {
      className: "bootbox-" + className,
      buttons: createLabels.apply(null, labels)
    };

    // ensure the buttons properties generated, *after* merging
    // with user args are still valid against the supplied labels
    return validateButtons(
      // merge the generated base properties with user supplied arguments
      mergeArguments(
        baseOptions,
        args,
        // if args.length > 1, properties specify how each arg maps to an object key
        properties
      ),
      labels
    );
  }

  /**
   * from a given list of arguments return a suitable object of button labels
   * all this does is normalise the given labels and translate them where possible
   * e.g. "ok", "confirm" -> { ok: "OK, cancel: "Annuleren" }
   */
  function createLabels() {
    var buttons = {};

    for (var i = 0, j = arguments.length; i < j; i++) {
      var argument = arguments[i];
      var key = argument.toLowerCase();
      var value = argument.toUpperCase();

      buttons[key] = {
        label: _t(value)
      };
    }

    return buttons;
  }

  function validateButtons(options, buttons) {
    var allowedButtons = {};
    each(buttons, function(key, value) {
      allowedButtons[value] = true;
    });

    each(options.buttons, function(key) {
      if (allowedButtons[key] === undefined) {
        throw new Error("button key " + key + " is not allowed (options are " + buttons.join("\n") + ")");
      }
    });

    return options;
  }

  exports.alert = function() {
    var options;

    options = mergeDialogOptions("alert", ["ok"], ["message", "callback"], arguments);

    if (options.callback && !$.isFunction(options.callback)) {
      throw new Error("alert requires callback property to be a function when provided");
    }

    /**
     * overrides
     */
    options.buttons.ok.callback = options.onEscape = function() {
      if ($.isFunction(options.callback)) {
        return options.callback.call(this);
      }
      return true;
    };

    return exports.dialog(options);
  };

  exports.confirm = function() {
    var options;

    options = mergeDialogOptions("confirm", ["cancel", "confirm"], ["message", "callback"], arguments);

    /**
     * overrides; undo anything the user tried to set they shouldn't have
     */
    options.buttons.cancel.callback = options.onEscape = function() {
      return options.callback.call(this, false);
    };

    options.buttons.confirm.callback = function() {
      return options.callback.call(this, true);
    };

    // confirm specific validation
    if (!$.isFunction(options.callback)) {
      throw new Error("confirm requires a callback");
    }

    return exports.dialog(options);
  };

  exports.prompt = function() {
    var options;
    var defaults;
    var dialog;
    var form;
    var input;
    var shouldShow;
    var inputOptions;

    // we have to create our form first otherwise
    // its value is undefined when gearing up our options
    // @TODO this could be solved by allowing message to
    // be a function instead...
    form = $(templates.form);

    // prompt defaults are more complex than others in that
    // users can override more defaults
    // @TODO I don't like that prompt has to do a lot of heavy
    // lifting which mergeDialogOptions can *almost* support already
    // just because of 'value' and 'inputType' - can we refactor?
    defaults = {
      className: "bootbox-prompt",
      buttons: createLabels("cancel", "confirm"),
      value: "",
      inputType: "text"
    };

    options = validateButtons(
      mergeArguments(defaults, arguments, ["title", "callback"]),
      ["cancel", "confirm"]
    );

    // capture the user's show value; we always set this to false before
    // spawning the dialog to give us a chance to attach some handlers to
    // it, but we need to make sure we respect a preference not to show it
    shouldShow = (options.show === undefined) ? true : options.show;

    /**
     * overrides; undo anything the user tried to set they shouldn't have
     */
    options.message = form;

    options.buttons.cancel.callback = options.onEscape = function() {
      return options.callback.call(this, null);
    };

    options.buttons.confirm.callback = function() {
      var value;

      switch (options.inputType) {
        case "text":
        case "textarea":
        case "email":
        case "select":
        case "date":
        case "time":
        case "number":
        case "password":
          value = input.val();
          break;

        case "checkbox":
          var checkedItems = input.find("input:checked");

          // we assume that checkboxes are always multiple,
          // hence we default to an empty array
          value = [];

          each(checkedItems, function(_, item) {
            value.push($(item).val());
          });
          break;
      }

      return options.callback.call(this, value);
    };

    options.show = false;

    // prompt specific validation
    if (!options.title) {
      throw new Error("prompt requires a title");
    }

    if (!$.isFunction(options.callback)) {
      throw new Error("prompt requires a callback");
    }

    if (!templates.inputs[options.inputType]) {
      throw new Error("invalid prompt type");
    }

    // create the input based on the supplied type
    input = $(templates.inputs[options.inputType]);

    switch (options.inputType) {
      case "text":
      case "textarea":
      case "email":
      case "date":
      case "time":
      case "number":
      case "password":
        input.val(options.value);
        break;

      case "select":
        var groups = {};
        inputOptions = options.inputOptions || [];

        if (!$.isArray(inputOptions)) {
          throw new Error("Please pass an array of input options");
        }

        if (!inputOptions.length) {
          throw new Error("prompt with select requires options");
        }

        each(inputOptions, function(_, option) {

          // assume the element to attach to is the input...
          var elem = input;

          if (option.value === undefined || option.text === undefined) {
            throw new Error("given options in wrong format");
          }

          // ... but override that element if this option sits in a group

          if (option.group) {
            // initialise group if necessary
            if (!groups[option.group]) {
              groups[option.group] = $("<optgroup/>").attr("label", option.group);
            }

            elem = groups[option.group];
          }

          elem.append("<option value='" + option.value + "'>" + option.text + "</option>");
        });

        each(groups, function(_, group) {
          input.append(group);
        });

        // safe to set a select's value as per a normal input
        input.val(options.value);
        break;

      case "checkbox":
        var values   = $.isArray(options.value) ? options.value : [options.value];
        inputOptions = options.inputOptions || [];

        if (!inputOptions.length) {
          throw new Error("prompt with checkbox requires options");
        }

        if (!inputOptions[0].value || !inputOptions[0].text) {
          throw new Error("given options in wrong format");
        }

        // checkboxes have to nest within a containing element, so
        // they break the rules a bit and we end up re-assigning
        // our 'input' element to this container instead
        input = $("<div/>");

        each(inputOptions, function(_, option) {
          var checkbox = $(templates.inputs[options.inputType]);

          checkbox.find("input").attr("value", option.value);
          checkbox.find("label").append(option.text);

          // we've ensured values is an array so we can always iterate over it
          each(values, function(_, value) {
            if (value === option.value) {
              checkbox.find("input").prop("checked", true);
            }
          });

          input.append(checkbox);
        });
        break;
    }

    // @TODO provide an attributes option instead
    // and simply map that as keys: vals
    if (options.placeholder) {
      input.attr("placeholder", options.placeholder);
    }

    if (options.pattern) {
      input.attr("pattern", options.pattern);
    }

    if (options.maxlength) {
      input.attr("maxlength", options.maxlength);
    }

    // now place it in our form
    form.append(input);

    form.on("submit", function(e) {
      e.preventDefault();
      // Fix for SammyJS (or similar JS routing library) hijacking the form post.
      e.stopPropagation();
      // @TODO can we actually click *the* button object instead?
      // e.g. buttons.confirm.click() or similar
      dialog.find(".btn-primary").click();
    });

    dialog = exports.dialog(options);

    // clear the existing handler focusing the submit button...
    dialog.off("shown.bs.modal");

    // ...and replace it with one focusing our input, if possible
    dialog.on("shown.bs.modal", function() {
      // need the closure here since input isn't
      // an object otherwise
      input.focus();
    });

    if (shouldShow === true) {
      dialog.modal("show");
    }

    return dialog;
  };

  exports.dialog = function(options) {
    options = sanitize(options);

    var dialog = $(templates.dialog);
    var innerDialog = dialog.find(".modal-dialog");
    var body = dialog.find(".modal-body");
    var buttons = options.buttons;
    var buttonStr = "";
    var callbacks = {
      onEscape: options.onEscape
    };

    if ($.fn.modal === undefined) {
      throw new Error(
        "$.fn.modal is not defined; please double check you have included " +
        "the Bootstrap JavaScript library. See http://getbootstrap.com/javascript/ " +
        "for more details."
      );
    }

    each(buttons, function(key, button) {

      // @TODO I don't like this string appending to itself; bit dirty. Needs reworking
      // can we just build up button elements instead? slower but neater. Then button
      // can just become a template too
      buttonStr += "<button data-bb-handler='" + key + "' type='button' class='btn " + button.className + "'>" + button.label + "</button>";
      callbacks[key] = button.callback;
    });

    body.find(".bootbox-body").html(options.message);

    if (options.animate === true) {
      dialog.addClass("fade");
    }

    if (options.className) {
      dialog.addClass(options.className);
    }

    if (options.size === "large") {
      innerDialog.addClass("modal-lg");
    } else if (options.size === "small") {
      innerDialog.addClass("modal-sm");
    }

    if (options.title) {
      body.before(templates.header);
    }

    if (options.closeButton) {
      var closeButton = $(templates.closeButton);

      if (options.title) {
        dialog.find(".modal-header").prepend(closeButton);
      } else {
        closeButton.css("margin-top", "-10px").prependTo(body);
      }
    }

    if (options.title) {
      dialog.find(".modal-title").html(options.title);
    }

    if (buttonStr.length) {
      body.after(templates.footer);
      dialog.find(".modal-footer").html(buttonStr);
    }


    /**
     * Bootstrap event listeners; used handle extra
     * setup & teardown required after the underlying
     * modal has performed certain actions
     */

    dialog.on("hidden.bs.modal", function(e) {
      // ensure we don't accidentally intercept hidden events triggered
      // by children of the current dialog. We shouldn't anymore now BS
      // namespaces its events; but still worth doing
      if (e.target === this) {
        dialog.remove();
      }
    });

    /*
    dialog.on("show.bs.modal", function() {
      // sadly this doesn't work; show is called *just* before
      // the backdrop is added so we'd need a setTimeout hack or
      // otherwise... leaving in as would be nice
      if (options.backdrop) {
        dialog.next(".modal-backdrop").addClass("bootbox-backdrop");
      }
    });
    */

    dialog.on("shown.bs.modal", function() {
      dialog.find(".btn-primary:first").focus();
    });

    /**
     * Bootbox event listeners; experimental and may not last
     * just an attempt to decouple some behaviours from their
     * respective triggers
     */

    if (options.backdrop !== "static") {
      // A boolean true/false according to the Bootstrap docs
      // should show a dialog the user can dismiss by clicking on
      // the background.
      // We always only ever pass static/false to the actual
      // $.modal function because with `true` we can't trap
      // this event (the .modal-backdrop swallows it)
      // However, we still want to sort of respect true
      // and invoke the escape mechanism instead
      dialog.on("click.dismiss.bs.modal", function(e) {
        // @NOTE: the target varies in >= 3.3.x releases since the modal backdrop
        // moved *inside* the outer dialog rather than *alongside* it
        if (dialog.children(".modal-backdrop").length) {
          e.currentTarget = dialog.children(".modal-backdrop").get(0);
        }

        if (e.target !== e.currentTarget) {
          return;
        }

        dialog.trigger("escape.close.bb");
      });
    }

    dialog.on("escape.close.bb", function(e) {
      if (callbacks.onEscape) {
        processCallback(e, dialog, callbacks.onEscape);
      }
    });

    /**
     * Standard jQuery event listeners; used to handle user
     * interaction with our dialog
     */

    dialog.on("click", ".modal-footer button", function(e) {
      var callbackKey = $(this).data("bb-handler");

      processCallback(e, dialog, callbacks[callbackKey]);
    });

    dialog.on("click", ".bootbox-close-button", function(e) {
      // onEscape might be falsy but that's fine; the fact is
      // if the user has managed to click the close button we
      // have to close the dialog, callback or not
      processCallback(e, dialog, callbacks.onEscape);
    });

    dialog.on("keyup", function(e) {
      if (e.which === 27) {
        dialog.trigger("escape.close.bb");
      }
    });

    // the remainder of this method simply deals with adding our
    // dialogent to the DOM, augmenting it with Bootstrap's modal
    // functionality and then giving the resulting object back
    // to our caller

    $(options.container).append(dialog);

    dialog.modal({
      backdrop: options.backdrop ? "static": false,
      keyboard: false,
      show: false
    });

    if (options.show) {
      dialog.modal("show");
    }

    // @TODO should we return the raw element here or should
    // we wrap it in an object on which we can expose some neater
    // methods, e.g. var d = bootbox.alert(); d.hide(); instead
    // of d.modal("hide");

   /*
    function BBDialog(elem) {
      this.elem = elem;
    }

    BBDialog.prototype = {
      hide: function() {
        return this.elem.modal("hide");
      },
      show: function() {
        return this.elem.modal("show");
      }
    };
    */

    return dialog;

  };

  exports.setDefaults = function() {
    var values = {};

    if (arguments.length === 2) {
      // allow passing of single key/value...
      values[arguments[0]] = arguments[1];
    } else {
      // ... and as an object too
      values = arguments[0];
    }

    $.extend(defaults, values);
  };

  exports.hideAll = function() {
    $(".bootbox").modal("hide");

    return exports;
  };


  /**
   * standard locales. Please add more according to ISO 639-1 standard. Multiple language variants are
   * unlikely to be required. If this gets too large it can be split out into separate JS files.
   */
  var locales = {
    bg_BG : {
      OK      : "Ок",
      CANCEL  : "Отказ",
      CONFIRM : "Потвърждавам"
    },
    br : {
      OK      : "OK",
      CANCEL  : "Cancelar",
      CONFIRM : "Sim"
    },
    cs : {
      OK      : "OK",
      CANCEL  : "Zrušit",
      CONFIRM : "Potvrdit"
    },
    da : {
      OK      : "OK",
      CANCEL  : "Annuller",
      CONFIRM : "Accepter"
    },
    de : {
      OK      : "OK",
      CANCEL  : "Abbrechen",
      CONFIRM : "Akzeptieren"
    },
    el : {
      OK      : "Εντάξει",
      CANCEL  : "Ακύρωση",
      CONFIRM : "Επιβεβαίωση"
    },
    en : {
      OK      : "OK",
      CANCEL  : "Cancel",
      CONFIRM : "OK"
    },
    es : {
      OK      : "OK",
      CANCEL  : "Cancelar",
      CONFIRM : "Aceptar"
    },
    et : {
      OK      : "OK",
      CANCEL  : "Katkesta",
      CONFIRM : "OK"
    },
    fa : {
      OK      : "قبول",
      CANCEL  : "لغو",
      CONFIRM : "تایید"
    },
    fi : {
      OK      : "OK",
      CANCEL  : "Peruuta",
      CONFIRM : "OK"
    },
    fr : {
      OK      : "OK",
      CANCEL  : "Annuler",
      CONFIRM : "D'accord"
    },
    he : {
      OK      : "אישור",
      CANCEL  : "ביטול",
      CONFIRM : "אישור"
    },
    hu : {
      OK      : "OK",
      CANCEL  : "Mégsem",
      CONFIRM : "Megerősít"
    },
    hr : {
      OK      : "OK",
      CANCEL  : "Odustani",
      CONFIRM : "Potvrdi"
    },
    id : {
      OK      : "OK",
      CANCEL  : "Batal",
      CONFIRM : "OK"
    },
    it : {
      OK      : "OK",
      CANCEL  : "Annulla",
      CONFIRM : "Conferma"
    },
    ja : {
      OK      : "OK",
      CANCEL  : "キャンセル",
      CONFIRM : "確認"
    },
    lt : {
      OK      : "Gerai",
      CANCEL  : "Atšaukti",
      CONFIRM : "Patvirtinti"
    },
    lv : {
      OK      : "Labi",
      CANCEL  : "Atcelt",
      CONFIRM : "Apstiprināt"
    },
    nl : {
      OK      : "OK",
      CANCEL  : "Annuleren",
      CONFIRM : "Accepteren"
    },
    no : {
      OK      : "OK",
      CANCEL  : "Avbryt",
      CONFIRM : "OK"
    },
    pl : {
      OK      : "OK",
      CANCEL  : "Anuluj",
      CONFIRM : "Potwierdź"
    },
    pt : {
      OK      : "OK",
      CANCEL  : "Cancelar",
      CONFIRM : "Confirmar"
    },
    ru : {
      OK      : "OK",
      CANCEL  : "Отмена",
      CONFIRM : "Применить"
    },
    sq : {
      OK : "OK",
      CANCEL : "Anulo",
      CONFIRM : "Prano"
    },
    sv : {
      OK      : "OK",
      CANCEL  : "Avbryt",
      CONFIRM : "OK"
    },
    th : {
      OK      : "ตกลง",
      CANCEL  : "ยกเลิก",
      CONFIRM : "ยืนยัน"
    },
    tr : {
      OK      : "Tamam",
      CANCEL  : "İptal",
      CONFIRM : "Onayla"
    },
    zh_CN : {
      OK      : "OK",
      CANCEL  : "取消",
      CONFIRM : "确认"
    },
    zh_TW : {
      OK      : "OK",
      CANCEL  : "取消",
      CONFIRM : "確認"
    }
  };

  exports.addLocale = function(name, values) {
    $.each(["OK", "CANCEL", "CONFIRM"], function(_, v) {
      if (!values[v]) {
        throw new Error("Please supply a translation for '" + v + "'");
      }
    });

    locales[name] = {
      OK: values.OK,
      CANCEL: values.CANCEL,
      CONFIRM: values.CONFIRM
    };

    return exports;
  };

  exports.removeLocale = function(name) {
    delete locales[name];

    return exports;
  };

  exports.setLocale = function(name) {
    return exports.setDefaults("locale", name);
  };

  exports.init = function(_$) {
    return init(_$ || $);
  };

  return exports;
}));

/* 
* Project: Bootstrap Notify = v3.1.3
* Description: Turns standard Bootstrap alerts into "Growl-like" notifications.
* Author: Mouse0270 aka Robert McIntosh
* License: MIT License
* Website: https://github.com/mouse0270/bootstrap-growl
*/
(function (factory) {
	if (typeof define === 'function' && define.amd) {
		// AMD. Register as an anonymous module.
		define(['jquery'], factory);
	} else if (typeof exports === 'object') {
		// Node/CommonJS
		factory(require('jquery'));
	} else {
		// Browser globals
		factory(jQuery);
	}
}(function ($) {
	// Create the defaults once
	var defaults = {
			element: 'body',
			position: null,
			type: "info",
			allow_dismiss: true,
			newest_on_top: false,
			showProgressbar: false,
			placement: {
				from: "top",
				align: "right"
			},
			offset: 20,
			spacing: 10,
			z_index: 1031,
			delay: 5000,
			timer: 1000,
			url_target: '_blank',
			mouse_over: null,
			animate: {
				enter: 'animated fadeInDown',
				exit: 'animated fadeOutUp'
			},
			onShow: null,
			onShown: null,
			onClose: null,
			onClosed: null,
			icon_type: 'class',
			template: '<div data-notify="container" class="col-xs-11 col-sm-4 alert alert-{0}" role="alert"><button type="button" aria-hidden="true" class="close" data-notify="dismiss">&times;</button><span data-notify="icon"></span> <span data-notify="title">{1}</span> <span data-notify="message">{2}</span><div class="progress" data-notify="progressbar"><div class="progress-bar progress-bar-{0}" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="width: 0%;"></div></div><a href="{3}" target="{4}" data-notify="url"></a></div>'
		};

	String.format = function() {
		var str = arguments[0];
		for (var i = 1; i < arguments.length; i++) {
			str = str.replace(RegExp("\\{" + (i - 1) + "\\}", "gm"), arguments[i]);
		}
		return str;
	};

	function Notify ( element, content, options ) {
		// Setup Content of Notify
		var content = {
			content: {
				message: typeof content == 'object' ? content.message : content,
				title: content.title ? content.title : '',
				icon: content.icon ? content.icon : '',
				url: content.url ? content.url : '#',
				target: content.target ? content.target : '-'
			}
		};

		options = $.extend(true, {}, content, options);
		this.settings = $.extend(true, {}, defaults, options);
		this._defaults = defaults;
		if (this.settings.content.target == "-") {
			this.settings.content.target = this.settings.url_target;
		}
		this.animations = {
			start: 'webkitAnimationStart oanimationstart MSAnimationStart animationstart',
			end: 'webkitAnimationEnd oanimationend MSAnimationEnd animationend'
		}

		if (typeof this.settings.offset == 'number') {
		    this.settings.offset = {
		    	x: this.settings.offset,
		    	y: this.settings.offset
		    };
		}

		this.init();
	};

	$.extend(Notify.prototype, {
		init: function () {
			var self = this;

			this.buildNotify();
			if (this.settings.content.icon) {
				this.setIcon();
			}
			if (this.settings.content.url != "#") {
				this.styleURL();
			}
			this.placement();
			this.bind();

			this.notify = {
				$ele: this.$ele,
				update: function(command, update) {
					var commands = {};
					if (typeof command == "string") {					
						commands[command] = update;
					}else{
						commands = command;
					}
					for (var command in commands) {
						switch (command) {
							case "type":
								this.$ele.removeClass('alert-' + self.settings.type);
								this.$ele.find('[data-notify="progressbar"] > .progress-bar').removeClass('progress-bar-' + self.settings.type);
								self.settings.type = commands[command];
								this.$ele.addClass('alert-' + commands[command]).find('[data-notify="progressbar"] > .progress-bar').addClass('progress-bar-' + commands[command]);
								break;
							case "icon":
								var $icon = this.$ele.find('[data-notify="icon"]');
								if (self.settings.icon_type.toLowerCase() == 'class') {
									$icon.removeClass(self.settings.content.icon).addClass(commands[command]);
								}else{
									if (!$icon.is('img')) {
										$icon.find('img');
									}
									$icon.attr('src', commands[command]);
								}
								break;
							case "progress":
								var newDelay = self.settings.delay - (self.settings.delay * (commands[command] / 100));
								this.$ele.data('notify-delay', newDelay);
								this.$ele.find('[data-notify="progressbar"] > div').attr('aria-valuenow', commands[command]).css('width', commands[command] + '%');
								break;
							case "url":
								this.$ele.find('[data-notify="url"]').attr('href', commands[command]);
								break;
							case "target":
								this.$ele.find('[data-notify="url"]').attr('target', commands[command]);
								break;
							default:
								this.$ele.find('[data-notify="' + command +'"]').html(commands[command]);
						};
					}
					var posX = this.$ele.outerHeight() + parseInt(self.settings.spacing) + parseInt(self.settings.offset.y);
					self.reposition(posX);
				},
				close: function() {
					self.close();
				}
			};
		},
		buildNotify: function () {
			var content = this.settings.content;
			this.$ele = $(String.format(this.settings.template, this.settings.type, content.title, content.message, content.url, content.target));
			this.$ele.attr('data-notify-position', this.settings.placement.from + '-' + this.settings.placement.align);		
			if (!this.settings.allow_dismiss) {
				this.$ele.find('[data-notify="dismiss"]').css('display', 'none');
			}
			if ((this.settings.delay <= 0 && !this.settings.showProgressbar) || !this.settings.showProgressbar) {
				this.$ele.find('[data-notify="progressbar"]').remove();
			}
		},
		setIcon: function() {
			if (this.settings.icon_type.toLowerCase() == 'class') {
				this.$ele.find('[data-notify="icon"]').addClass(this.settings.content.icon);
			}else{
				if (this.$ele.find('[data-notify="icon"]').is('img')) {
					this.$ele.find('[data-notify="icon"]').attr('src', this.settings.content.icon);
				}else{
					this.$ele.find('[data-notify="icon"]').append('<img src="'+this.settings.content.icon+'" alt="Notify Icon" />');
				}	
			}
		},
		styleURL: function() {
			this.$ele.find('[data-notify="url"]').css({
				backgroundImage: 'url(data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)',
				height: '100%',
				left: '0px',
				position: 'absolute',
				top: '0px',
				width: '100%',
				zIndex: this.settings.z_index + 1
			});
			this.$ele.find('[data-notify="dismiss"]').css({
				position: 'absolute',
				right: '10px',
				top: '5px',
				zIndex: this.settings.z_index + 2
			});
		},
		placement: function() {
			var self = this,
				offsetAmt = this.settings.offset.y,
				css = {
					display: 'inline-block',
					margin: '0px auto',
					position: this.settings.position ?  this.settings.position : (this.settings.element === 'body' ? 'fixed' : 'absolute'),
					transition: 'all .5s ease-in-out',
					zIndex: this.settings.z_index
				},
				hasAnimation = false,
				settings = this.settings;

			$('[data-notify-position="' + this.settings.placement.from + '-' + this.settings.placement.align + '"]:not([data-closing="true"])').each(function() {
				return offsetAmt = Math.max(offsetAmt, parseInt($(this).css(settings.placement.from)) +  parseInt($(this).outerHeight()) +  parseInt(settings.spacing));
			});
			if (this.settings.newest_on_top == true) {
				offsetAmt = this.settings.offset.y;
			}
			css[this.settings.placement.from] = offsetAmt+'px';

			switch (this.settings.placement.align) {
				case "left":
				case "right":
					css[this.settings.placement.align] = this.settings.offset.x+'px';
					break;
				case "center":
					css.left = 0;
					css.right = 0;
					break;
			}
			this.$ele.css(css).addClass(this.settings.animate.enter);
			$.each(Array('webkit', 'moz', 'o', 'ms', ''), function(index, prefix) {
				self.$ele[0].style[prefix+'AnimationIterationCount'] = 1;
			});

			$(this.settings.element).append(this.$ele);

			if (this.settings.newest_on_top == true) {
				offsetAmt = (parseInt(offsetAmt)+parseInt(this.settings.spacing)) + this.$ele.outerHeight();
				this.reposition(offsetAmt);
			}
			
			if ($.isFunction(self.settings.onShow)) {
				self.settings.onShow.call(this.$ele);
			}

			this.$ele.one(this.animations.start, function(event) {
				hasAnimation = true;
			}).one(this.animations.end, function(event) {
				if ($.isFunction(self.settings.onShown)) {
					self.settings.onShown.call(this);
				}
			});

			setTimeout(function() {
				if (!hasAnimation) {
					if ($.isFunction(self.settings.onShown)) {
						self.settings.onShown.call(this);
					}
				}
			}, 600);
		},
		bind: function() {
			var self = this;

			this.$ele.find('[data-notify="dismiss"]').on('click', function() {		
				self.close();
			})

			this.$ele.mouseover(function(e) {
				$(this).data('data-hover', "true");
			}).mouseout(function(e) {
				$(this).data('data-hover', "false");
			});
			this.$ele.data('data-hover', "false");

			if (this.settings.delay > 0) {
				self.$ele.data('notify-delay', self.settings.delay);
				var timer = setInterval(function() {
					var delay = parseInt(self.$ele.data('notify-delay')) - self.settings.timer;
					if ((self.$ele.data('data-hover') === 'false' && self.settings.mouse_over == "pause") || self.settings.mouse_over != "pause") {
						var percent = ((self.settings.delay - delay) / self.settings.delay) * 100;
						self.$ele.data('notify-delay', delay);
						self.$ele.find('[data-notify="progressbar"] > div').attr('aria-valuenow', percent).css('width', percent + '%');
					}
					if (delay <= -(self.settings.timer)) {
						clearInterval(timer);
						self.close();
					}
				}, self.settings.timer);
			}
		},
		close: function() {
			var self = this,
				$successors = null,
				posX = parseInt(this.$ele.css(this.settings.placement.from)),
				hasAnimation = false;

			this.$ele.data('closing', 'true').addClass(this.settings.animate.exit);
			self.reposition(posX);			
			
			if ($.isFunction(self.settings.onClose)) {
				self.settings.onClose.call(this.$ele);
			}

			this.$ele.one(this.animations.start, function(event) {
				hasAnimation = true;
			}).one(this.animations.end, function(event) {
				$(this).remove();
				if ($.isFunction(self.settings.onClosed)) {
					self.settings.onClosed.call(this);
				}
			});

			setTimeout(function() {
				if (!hasAnimation) {
					self.$ele.remove();
					if (self.settings.onClosed) {
						self.settings.onClosed(self.$ele);
					}
				}
			}, 600);
		},
		reposition: function(posX) {
			var self = this,
				notifies = '[data-notify-position="' + this.settings.placement.from + '-' + this.settings.placement.align + '"]:not([data-closing="true"])',
				$elements = this.$ele.nextAll(notifies);
			if (this.settings.newest_on_top == true) {
				$elements = this.$ele.prevAll(notifies);
			}
			$elements.each(function() {
				$(this).css(self.settings.placement.from, posX);
				posX = (parseInt(posX)+parseInt(self.settings.spacing)) + $(this).outerHeight();
			});
		}
	});

	$.notify = function ( content, options ) {
		var plugin = new Notify( this, content, options );
		return plugin.notify;
	};
	$.notifyDefaults = function( options ) {
		defaults = $.extend(true, {}, defaults, options);
		return defaults;
	};
	$.notifyClose = function( command ) {
		if (typeof command === "undefined" || command == "all") {
			$('[data-notify]').find('[data-notify="dismiss"]').trigger('click');
		}else{
			$('[data-notify-position="'+command+'"]').find('[data-notify="dismiss"]').trigger('click');
		}
	};

}));
/*
 * Lazy Load - jQuery plugin for lazy loading images
 *
 * Copyright (c) 2007-2013 Mika Tuupola
 *
 * Licensed under the MIT license:
 *   http://www.opensource.org/licenses/mit-license.php
 *
 * Project home:
 *   http://www.appelsiini.net/projects/lazyload
 *
 * Version:  1.9.3
 *
 */

(function($, window, document, undefined) {
    var $window = $(window);

    $.fn.lazyload = function(options) {
        var elements = this;
        var $container;
        var settings = {
            threshold       : 0,
            failure_limit   : 0,
            event           : "scroll",
            effect          : "show",
            container       : window,
            data_attribute  : "original",
            skip_invisible  : true,
            appear          : null,
            load            : null,
            placeholder     : "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAANSURBVBhXYzh8+PB/AAffA0nNPuCLAAAAAElFTkSuQmCC"
        };

        function update() {
            var counter = 0;

            elements.each(function() {
                var $this = $(this);
                if (settings.skip_invisible && !$this.is(":visible")) {
                    return;
                }
                if ($.abovethetop(this, settings) ||
                    $.leftofbegin(this, settings)) {
                        /* Nothing. */
                } else if (!$.belowthefold(this, settings) &&
                    !$.rightoffold(this, settings)) {
                        $this.trigger("appear");
                        /* if we found an image we'll load, reset the counter */
                        counter = 0;
                } else {
                    if (++counter > settings.failure_limit) {
                        return false;
                    }
                }
            });

        }

        if(options) {
            /* Maintain BC for a couple of versions. */
            if (undefined !== options.failurelimit) {
                options.failure_limit = options.failurelimit;
                delete options.failurelimit;
            }
            if (undefined !== options.effectspeed) {
                options.effect_speed = options.effectspeed;
                delete options.effectspeed;
            }

            $.extend(settings, options);
        }

        /* Cache container as jQuery as object. */
        $container = (settings.container === undefined ||
                      settings.container === window) ? $window : $(settings.container);

        /* Fire one scroll event per scroll. Not one scroll event per image. */
        if (0 === settings.event.indexOf("scroll")) {
            $container.bind(settings.event, function() {
                return update();
            });
        }

        this.each(function() {
            var self = this;
            var $self = $(self);

            self.loaded = false;

            /* If no src attribute given use data:uri. */
            if ($self.attr("src") === undefined || $self.attr("src") === false) {
                if ($self.is("img")) {
                    $self.attr("src", settings.placeholder);
                }
            }

            /* When appear is triggered load original image. */
            $self.one("appear", function() {
                if (!this.loaded) {
                    if (settings.appear) {
                        var elements_left = elements.length;
                        settings.appear.call(self, elements_left, settings);
                    }
                    $("<img />")
                        .bind("load", function() {

                            var original = $self.attr("data-" + settings.data_attribute);
                            $self.hide();
                            if ($self.is("img")) {
                                $self.attr("src", original);
                            } else {
                                $self.css("background-image", "url('" + original + "')");
                            }
                            $self[settings.effect](settings.effect_speed);

                            self.loaded = true;

                            /* Remove image from array so it is not looped next time. */
                            var temp = $.grep(elements, function(element) {
                                return !element.loaded;
                            });
                            elements = $(temp);

                            if (settings.load) {
                                var elements_left = elements.length;
                                settings.load.call(self, elements_left, settings);
                            }
                        })
                        .attr("src", $self.attr("data-" + settings.data_attribute));
                }
            });

            /* When wanted event is triggered load original image */
            /* by triggering appear.                              */
            if (0 !== settings.event.indexOf("scroll")) {
                $self.bind(settings.event, function() {
                    if (!self.loaded) {
                        $self.trigger("appear");
                    }
                });
            }
        });

        /* Check if something appears when window is resized. */
        $window.bind("resize", function() {
            update();
        });

        /* With IOS5 force loading images when navigating with back button. */
        /* Non optimal workaround. */
        if ((/(?:iphone|ipod|ipad).*os 5/gi).test(navigator.appVersion)) {
            $window.bind("pageshow", function(event) {
                if (event.originalEvent && event.originalEvent.persisted) {
                    elements.each(function() {
                        $(this).trigger("appear");
                    });
                }
            });
        }

        /* Force initial check if images should appear. */
        $(document).ready(function() {
            update();
        });

        return this;
    };

    /* Convenience methods in jQuery namespace.           */
    /* Use as  $.belowthefold(element, {threshold : 100, container : window}) */

    $.belowthefold = function(element, settings) {
        var fold;

        if (settings.container === undefined || settings.container === window) {
            fold = (window.innerHeight ? window.innerHeight : $window.height()) + $window.scrollTop();
        } else {
            fold = $(settings.container).offset().top + $(settings.container).height();
        }

        return fold <= $(element).offset().top - settings.threshold;
    };

    $.rightoffold = function(element, settings) {
        var fold;

        if (settings.container === undefined || settings.container === window) {
            fold = $window.width() + $window.scrollLeft();
        } else {
            fold = $(settings.container).offset().left + $(settings.container).width();
        }

        return fold <= $(element).offset().left - settings.threshold;
    };

    $.abovethetop = function(element, settings) {
        var fold;

        if (settings.container === undefined || settings.container === window) {
            fold = $window.scrollTop();
        } else {
            fold = $(settings.container).offset().top;
        }

        return fold >= $(element).offset().top + settings.threshold  + $(element).height();
    };

    $.leftofbegin = function(element, settings) {
        var fold;

        if (settings.container === undefined || settings.container === window) {
            fold = $window.scrollLeft();
        } else {
            fold = $(settings.container).offset().left;
        }

        return fold >= $(element).offset().left + settings.threshold + $(element).width();
    };

    $.inviewport = function(element, settings) {
         return !$.rightoffold(element, settings) && !$.leftofbegin(element, settings) &&
                !$.belowthefold(element, settings) && !$.abovethetop(element, settings);
     };

    /* Custom selectors for your convenience.   */
    /* Use as $("img:below-the-fold").something() or */
    /* $("img").filter(":below-the-fold").something() which is faster */

    $.extend($.expr[":"], {
        "below-the-fold" : function(a) { return $.belowthefold(a, {threshold : 0}); },
        "above-the-top"  : function(a) { return !$.belowthefold(a, {threshold : 0}); },
        "right-of-screen": function(a) { return $.rightoffold(a, {threshold : 0}); },
        "left-of-screen" : function(a) { return !$.rightoffold(a, {threshold : 0}); },
        "in-viewport"    : function(a) { return $.inviewport(a, {threshold : 0}); },
        /* Maintain BC for couple of versions. */
        "above-the-fold" : function(a) { return !$.belowthefold(a, {threshold : 0}); },
        "right-of-fold"  : function(a) { return $.rightoffold(a, {threshold : 0}); },
        "left-of-fold"   : function(a) { return !$.rightoffold(a, {threshold : 0}); }
    });

})(jQuery, window, document);

(function($) {
    $(document).ready(function() {

        function failFunction(e) {
            var data = jQuery.parseJSON(e.responseText);
            $('.bottom-left').notify({
                message: { html: data.message },
                type: 'bangTidy',
                closable: true
            }).show();
        }

        $(document).on('change', 'form.image-upload-form .single-image-input', function(e) {
            $(e.currentTarget.form).find('.progress').removeClass('hidden');
            $(e.currentTarget.form).find('.progress-bar').css('width', '0');
            $(e.currentTarget.form).ajaxSubmit({
                dataType: 'json',
                success: function(data) {
                    var single = false;
                    if ($(e.currentTarget.form).hasClass('single'))
                        single = true;
                    $(e.currentTarget.form).find('.progress').addClass('hidden');
                    if (single)
                        $(e.currentTarget.form).find('.upload-image-list').empty();
                    $(e.currentTarget.form).find('.upload-image-list').append('<li data-id="'+data[0].id+'"><img src="'+data[0].url+'"><button class="close" aria-hidden="true" data-id="'+data[0].id+'">&times;</button></li>');
                    var id = $(e.currentTarget.form).data('id');
                    var values_node = $('#'+id+'-values');
                    if (single)
                        values_node.empty();
                    values_node.append('<input type="hidden" name="'+id+'" value="'+data[0].id+'">');
                },
                error: failFunction,
                uploadProgress: function(event, position, total, percentComplete) {
                    $(e.currentTarget.form).find('.progress-bar').css('width', percentComplete+'%');
                }
            });
        });

        $(document).on('change', 'form.image-upload-form .multiple-image-input', function(e) {
            $(e.currentTarget.form).find('.progress').removeClass('hidden');
            $(e.currentTarget.form).find('.progress-bar').css('width', '0');
            console.log(e.currentTarget.form);
            $(e.currentTarget.form).ajaxSubmit({
                dataType: 'json',
                success: function(data) {
                    $(e.currentTarget.form).find('.progress').addClass('hidden');
                    var id = $(e.currentTarget.form).data('id');
                    var values_node = $('#'+id+'-values');
                    for (var i in data) {
                        $.get('/uimg/'+data[i].id+'/preview', {}, function(html){
                            $(e.currentTarget.form).find('.upload-image-list').append(html);
                        });
                        values_node.append('<input type="hidden" name="'+id+'" value="'+data[i].id+'">');
                    }
                },
                error: failFunction,
                uploadProgress: function(event, position, total, percentComplete) {
                    $(e.currentTarget.form).find('.progress-bar').css('width', percentComplete+'%');
                }
            });
        });

        $(document).on('click', 'form.image-upload-form .close', function(e) {
            var id = $(e.currentTarget).data('id');
            var form_id = $(e.currentTarget.form).data('id');
            var values_node = $('#'+form_id+'-values');
            values_node.find('input[value="'+id+'"]').remove();
            $('form.image-upload-form li[data-id='+id+']').remove();
            $.post('/uimg/'+$(e.currentTarget).data('id')+'/del', function(data) {}, 'json');
            e.preventDefault();
            return false;
        });

        $(document).on('click', 'form.image-upload-form .description-edit', function(e) {
            var id = $(e.currentTarget).data('id');
            if ($(e.currentTarget.nextSibling).hasClass('in')) {
                $(e.currentTarget).popover('destroy');
            } else {
                $.get('/uimg/'+id+'/edit',{}, function(data){
                    $(e.currentTarget).popover({
                        html: true,
                        placement: 'bottom',
                        trigger: 'manual',
                        title: 'Описание',
                        content: data
                    });
                    $(e.currentTarget).popover('show');
                });
            }
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-userimage-form-save', function(e){
            var id = $(e.currentTarget).data('id');
            $('#userimage-form-'+id).ajaxSubmit({
                dataType: 'json',
                success: function(data){
                    $(e.currentTarget).parents('.upload-image-list').find('li[data-id="'+data.id+'"]').replaceWith(data.object.preview);
                },
                error: failFunction
            });
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.uimg-library .item', function(e){
            $('.uimg-library .item').removeClass('active');
            $(e.currentTarget).addClass('active');
        });

        $(document).on('click', '.btn-library-more', function(e) {
            var id = $(e.currentTarget).data('lib');
            loadUserImageLibrary(id);
            e.preventDefault();
            return false;
        });

        $(document).on('click', '#userimage-library-form button.btn', function(e){
            $(e.currentTarget.form).find('.progress').removeClass('hidden');
            $(e.currentTarget.form).find('.progress-bar').css('width', '0');
            $('#userimage-library-form').ajaxSubmit({
                dataType: 'json',
                success: function(data){
                    $.get('/uimg/'+data[0].id+'/lib/preview', function(preview){
                        $($('.uimg-library')[0]).prepend(preview);
                    }).fail(failFunction);
                },
                error: failFunction,
                uploadProgress: function(event, position, total, percentComplete) {
                    $(e.currentTarget.form).find('.progress-bar').css('width', percentComplete+'%');
                }
            });
            e.preventDefault();
            return false;
        });

        $('form.image-upload-form').hover(function(e){
            $(e.currentTarget).toggleClass('hover');
        });

        $('.image-list.gallery .carousel').on('slid.bs.carousel', function () {
            var items = $(this).find('.carousel-inner .item');
            for (var i=0; i<items.length; i++) {
                if ($(items[i]).hasClass('active')) {
                    $(this).find('.number').html(i+1);
                }
            }
        });

    });
})(jQuery);


function loadUserImageLibrary(id) {
    var page = (Number)($(id).data('page'));
    $(id + ' .loading').removeClass('hidden');
    $.get('/uimg/lib/list', {'page': page}, function(data){
        $(id + ' .content').append(data);
        $(id).data('page', page+1);
        $(id + ' .loading').addClass('hidden');
    });
}

(function($) {
    $(document).ready(function() {

        function failFunction(e) {
            var data = jQuery.parseJSON(e.responseText);
            $('.bottom-left').notify({
                message: { html: data.message },
                type: 'bangTidy',
                closable: true
            }).show();
        }

        $(document).on('change', 'form.file-upload-form input[type="file"]', function(e) {
            $(e.currentTarget.form).find('.progress').removeClass('hidden');
            $(e.currentTarget.form).find('.progress-bar').css('width', '0');
            $(e.currentTarget.form).ajaxSubmit({
                dataType: 'json',
                success: function(data) {
                    $(e.currentTarget.form).find('.progress').addClass('hidden');
                    $(e.currentTarget.form).find('.upload-file-list').append('<li data-id="'+data.id+'">'+data.object.name+'<button class="close" aria-hidden="true" data-id="'+data.id+'">&times;</button></li>');
                    var id = $(e.currentTarget.form).data('id');
                    var values_node = $('#'+id+'-values');
                    values_node.append('<input type="hidden" name="'+id+'" value="'+data.id+'">');
                },
                error: failFunction,
                uploadProgress: function(event, position, total, percentComplete) {
                    $(e.currentTarget.form).find('.progress-bar').css('width', percentComplete+'%');
                }
            });
        });

        $(document).on('click', 'form.file-upload-form .close', function(e) {
            $.post('/ufile/'+$(e.currentTarget).data('id')+'/del', function(data) {
                var id = $(e.currentTarget).data('id');
                var form_id = $(e.currentTarget.form).data('id');
                var values_node = $('#'+form_id+'-values');
                values_node.find('input[value="'+id+'"]').remove();
                $('form.file-upload-form li[data-id='+id+']').remove();
            }, 'json').fail(failFunction);
            e.preventDefault();
            return false;
        });

        $(document).on('click', 'form.file-upload-form .file-upload-choose', function(e){
            $(e.currentTarget.parentNode.parentNode).find('input[type="file"]').click();
            e.preventDefault();
            return false;
        });

        $(document).on('change', 'form.file-upload-form .file-upload input[type="file"]', function(e) {
            $('.file-upload .filename').text(e.currentTarget.value);
        });

    });
})(jQuery);

(function($) {
    $(document).ready(function() {

        function failFunction(e) {
            var data = jQuery.parseJSON(e.responseText);
            $('.bottom-left').notify({
                message: { html: data.message },
                type: 'bangTidy',
                closable: true
            }).show();
        }

        $(document).on('click', 'form.video-upload-form .close', function(e) {
            $.post('/uvideo/'+$(e.currentTarget).data('id')+'/del', function(data) {
                var id = $(e.currentTarget).data('id');
                var form_id = $(e.currentTarget.form).data('id');
                var values_node = $('#'+form_id+'-values input');
                values_node.attr('value', '')
                $('form.video-upload-form li[data-id='+id+']').remove();
            }, 'json').fail(failFunction);
            e.preventDefault();
            return false;
        });

        $(document).on('click', 'form.video-upload-form .video-link-upload', function(e){
            $(e.currentTarget.form).ajaxSubmit({
                dataType:'json',
                success:function(data) {
                    $(e.currentTarget.form).find('.upload-video-list').empty().append('<li data-id="'+data.id+'"><img src="'+data.object.url+'"><button class="close" aria-hidden="true" data-id="'+data.id+'">&times;</button></li>');
                    var id = $(e.currentTarget.form).data('id');
                    var values_node = $('#'+id+'-values input');
                    values_node.attr('value', data.id);
                },
                error: failFunction
            });
            e.preventDefault();
            return false;
        });

    });
})(jQuery);

(function($) {
    $(document).ready(function() {

        function refreshCommentCaptcha() {
            $.get('/captcha/refresh/', function(data){
                $('.captcha-form input[type="text"]').val('');
                $('.captcha-form input[type="hidden"]').val(data.key);
                $('.captcha-form img').attr('src', data.image_url);
            }, 'json');
        }

        $(document).on('click', '.btn-comment-add', function(e) {
            if (!$.trim($(e.currentTarget.form).find('textarea')[0].value)) {
                jQuery.notify('Текст сообщения пустой');
            } else {
                $(e.currentTarget.form).ajaxSubmit({
                    dataType: 'json',
                    success: function(data) {
                        if (data.object.parent) {
                            $('.children-'+data.object.parent).append(data.object.preview);
                        } else {
                            $('.comment-list').prepend(data.object.preview);
                        }
                        $(e.currentTarget.form).find('textarea').val('');
                        $(e.currentTarget.form).find('input[name="name"]').val('');
                        $('.children .comment-form').remove();
                        refreshCommentCaptcha();
                    },
                    error: failFunction
                });
            }

            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-comment-reply', function(e) {

            var comment = $(e.currentTarget).parents('.comment-preview')[0];
            var id = $(comment).data('id');
            var key = $(comment).parents('.comments').data('key');

            if ($('.comment-form-'+id).length == 0) {
                $('.children .comment-form').remove();
                $.get('/comment/create', {'parent': id, 'key': key}, function(data){
                    $('.children-'+id).prepend(data);
                    $('.comment-form-'+id+' textarea')[0].focus();
                }).fail(failFunction);
            } else {
                $('.children .comment-form').remove();
            }

            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-comment-del', function(e) {
            var id = $(this).data('id');
            bootbox.confirm('Удалить комментарий', function(result) {
                if (result) {
                    $.post('/comment/'+id+'/del', function(data) {
                        $('#comment-'+data.id).remove();
                    }, 'json').fail(failFunction);
                }
            });
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-refresh-captcha', function(e){
            refreshCommentCaptcha();
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-comment-else', function(e){
            var comment_list = $(this).parents('.comment-list');
            var btn = this;
            $(btn).html('<div class="loading"></div>');
            var key = $(this).data('key');
            var page = $(this).data('page');
            $.get('/comment/list', {key:key, page:page}, function(data){
                $(btn).remove();
                comment_list.append(data);
            });
        });
    });
})(jQuery);

/*!
	Colorbox v1.4.33 - 2013-10-31
	jQuery lightbox and modal window plugin
	(c) 2013 Jack Moore - http://www.jacklmoore.com/colorbox
	license: http://www.opensource.org/licenses/mit-license.php
*/
(function ($, document, window) {
	var
	// Default settings object.
	// See http://jacklmoore.com/colorbox for details.
	defaults = {
		// data sources
		html: false,
		photo: false,
		iframe: false,
		inline: false,

		// behavior and appearance
		transition: "elastic",
		speed: 300,
		fadeOut: 300,
		width: false,
		initialWidth: "600",
		innerWidth: false,
		maxWidth: false,
		height: false,
		initialHeight: "450",
		innerHeight: false,
		maxHeight: false,
		scalePhotos: true,
		scrolling: true,
		href: false,
		title: false,
		rel: false,
		opacity: 0.9,
		preloading: true,
		className: false,
		overlayClose: true,
		escKey: true,
		arrowKey: true,
		top: false,
		bottom: false,
		left: false,
		right: false,
		fixed: false,
		data: undefined,
		closeButton: true,
		fastIframe: true,
		open: false,
		reposition: true,
		loop: true,
		slideshow: false,
		slideshowAuto: true,
		slideshowSpeed: 2500,
		slideshowStart: "start slideshow",
		slideshowStop: "stop slideshow",
		photoRegex: /\.(gif|png|jp(e|g|eg)|bmp|ico|webp)((#|\?).*)?$/i,

		// alternate image paths for high-res displays
		retinaImage: false,
		retinaUrl: false,
		retinaSuffix: '@2x.$1',

		// internationalization
		current: "image {current} of {total}",
		previous: "previous",
		next: "next",
		close: "close",
		xhrError: "This content failed to load.",
		imgError: "This image failed to load.",

		// accessbility
		returnFocus: true,
		trapFocus: true,

		// callbacks
		onOpen: false,
		onLoad: false,
		onComplete: false,
		onCleanup: false,
		onClosed: false
	},
	
	// Abstracting the HTML and event identifiers for easy rebranding
	colorbox = 'colorbox',
	prefix = 'cbox',
	boxElement = prefix + 'Element',
	
	// Events
	event_open = prefix + '_open',
	event_load = prefix + '_load',
	event_complete = prefix + '_complete',
	event_cleanup = prefix + '_cleanup',
	event_closed = prefix + '_closed',
	event_purge = prefix + '_purge',

	// Cached jQuery Object Variables
	$overlay,
	$box,
	$wrap,
	$content,
	$topBorder,
	$leftBorder,
	$rightBorder,
	$bottomBorder,
	$related,
	$window,
	$loaded,
	$loadingBay,
	$loadingOverlay,
	$title,
	$current,
	$slideshow,
	$next,
	$prev,
	$close,
	$groupControls,
	$events = $('<a/>'), // $([]) would be prefered, but there is an issue with jQuery 1.4.2
	
	// Variables for cached values or use across multiple functions
	settings,
	interfaceHeight,
	interfaceWidth,
	loadedHeight,
	loadedWidth,
	element,
	index,
	photo,
	open,
	active,
	closing,
	loadingTimer,
	publicMethod,
	div = "div",
	className,
	requests = 0,
	previousCSS = {},
	init;

	// ****************
	// HELPER FUNCTIONS
	// ****************
	
	// Convenience function for creating new jQuery objects
	function $tag(tag, id, css) {
		var element = document.createElement(tag);

		if (id) {
			element.id = prefix + id;
		}

		if (css) {
			element.style.cssText = css;
		}

		return $(element);
	}
	
	// Get the window height using innerHeight when available to avoid an issue with iOS
	// http://bugs.jquery.com/ticket/6724
	function winheight() {
		return window.innerHeight ? window.innerHeight : $(window).height();
	}

	// Determine the next and previous members in a group.
	function getIndex(increment) {
		var
		max = $related.length,
		newIndex = (index + increment) % max;
		
		return (newIndex < 0) ? max + newIndex : newIndex;
	}

	// Convert '%' and 'px' values to integers
	function setSize(size, dimension) {
		return Math.round((/%/.test(size) ? ((dimension === 'x' ? $window.width() : winheight()) / 100) : 1) * parseInt(size, 10));
	}
	
	// Checks an href to see if it is a photo.
	// There is a force photo option (photo: true) for hrefs that cannot be matched by the regex.
	function isImage(settings, url) {
		return settings.photo || settings.photoRegex.test(url);
	}

	function retinaUrl(settings, url) {
		return settings.retinaUrl && window.devicePixelRatio > 1 ? url.replace(settings.photoRegex, settings.retinaSuffix) : url;
	}

	function trapFocus(e) {
		if ('contains' in $box[0] && !$box[0].contains(e.target)) {
			e.stopPropagation();
			$box.focus();
		}
	}

	// Assigns function results to their respective properties
	function makeSettings() {
		var i,
			data = $.data(element, colorbox);
		
		if (data == null) {
			settings = $.extend({}, defaults);
			if (console && console.log) {
				console.log('Error: cboxElement missing settings object');
			}
		} else {
			settings = $.extend({}, data);
		}
		
		for (i in settings) {
			if ($.isFunction(settings[i]) && i.slice(0, 2) !== 'on') { // checks to make sure the function isn't one of the callbacks, they will be handled at the appropriate time.
				settings[i] = settings[i].call(element);
			}
		}
		
		settings.rel = settings.rel || element.rel || $(element).data('rel') || 'nofollow';
		settings.href = settings.href || $(element).attr('href');
		settings.title = settings.title || element.title;
		
		if (typeof settings.href === "string") {
			settings.href = $.trim(settings.href);
		}
	}

	function trigger(event, callback) {
		// for external use
		$(document).trigger(event);

		// for internal use
		$events.triggerHandler(event);

		if ($.isFunction(callback)) {
			callback.call(element);
		}
	}


	var slideshow = (function(){
		var active,
			className = prefix + "Slideshow_",
			click = "click." + prefix,
			timeOut;

		function clear () {
			clearTimeout(timeOut);
		}

		function set() {
			if (settings.loop || $related[index + 1]) {
				clear();
				timeOut = setTimeout(publicMethod.next, settings.slideshowSpeed);
			}
		}

		function start() {
			$slideshow
				.html(settings.slideshowStop)
				.unbind(click)
				.one(click, stop);

			$events
				.bind(event_complete, set)
				.bind(event_load, clear);

			$box.removeClass(className + "off").addClass(className + "on");
		}

		function stop() {
			clear();
			
			$events
				.unbind(event_complete, set)
				.unbind(event_load, clear);

			$slideshow
				.html(settings.slideshowStart)
				.unbind(click)
				.one(click, function () {
					publicMethod.next();
					start();
				});

			$box.removeClass(className + "on").addClass(className + "off");
		}

		function reset() {
			active = false;
			$slideshow.hide();
			clear();
			$events
				.unbind(event_complete, set)
				.unbind(event_load, clear);
			$box.removeClass(className + "off " + className + "on");
		}

		return function(){
			if (active) {
				if (!settings.slideshow) {
					$events.unbind(event_cleanup, reset);
					reset();
				}
			} else {
				if (settings.slideshow && $related[1]) {
					active = true;
					$events.one(event_cleanup, reset);
					if (settings.slideshowAuto) {
						start();
					} else {
						stop();
					}
					$slideshow.show();
				}
			}
		};

	}());


	function launch(target) {
		if (!closing) {
			
			element = target;
			
			makeSettings();
			
			$related = $(element);
			
			index = 0;
			
			if (settings.rel !== 'nofollow') {
				$related = $('.' + boxElement).filter(function () {
					var data = $.data(this, colorbox),
						relRelated;

					if (data) {
						relRelated =  $(this).data('rel') || data.rel || this.rel;
					}
					
					return (relRelated === settings.rel);
				});
				index = $related.index(element);
				
				// Check direct calls to Colorbox.
				if (index === -1) {
					$related = $related.add(element);
					index = $related.length - 1;
				}
			}
			
			$overlay.css({
				opacity: parseFloat(settings.opacity),
				cursor: settings.overlayClose ? "pointer" : "auto",
				visibility: 'visible'
			}).show();
			

			if (className) {
				$box.add($overlay).removeClass(className);
			}
			if (settings.className) {
				$box.add($overlay).addClass(settings.className);
			}
			className = settings.className;

			if (settings.closeButton) {
				$close.html(settings.close).appendTo($content);
			} else {
				$close.appendTo('<div/>');
			}

			if (!open) {
				open = active = true; // Prevents the page-change action from queuing up if the visitor holds down the left or right keys.
				
				// Show colorbox so the sizes can be calculated in older versions of jQuery
				$box.css({visibility:'hidden', display:'block'});
				
				$loaded = $tag(div, 'LoadedContent', 'width:0; height:0; overflow:hidden');
				$content.css({width:'', height:''}).append($loaded);

				// Cache values needed for size calculations
				interfaceHeight = $topBorder.height() + $bottomBorder.height() + $content.outerHeight(true) - $content.height();
				interfaceWidth = $leftBorder.width() + $rightBorder.width() + $content.outerWidth(true) - $content.width();
				loadedHeight = $loaded.outerHeight(true);
				loadedWidth = $loaded.outerWidth(true);

				// Opens inital empty Colorbox prior to content being loaded.
				settings.w = setSize(settings.initialWidth, 'x');
				settings.h = setSize(settings.initialHeight, 'y');
				$loaded.css({width:'', height:settings.h});
				publicMethod.position();

				trigger(event_open, settings.onOpen);
				
				$groupControls.add($title).hide();

				$box.focus();
				
				if (settings.trapFocus) {
					// Confine focus to the modal
					// Uses event capturing that is not supported in IE8-
					if (document.addEventListener) {

						document.addEventListener('focus', trapFocus, true);
						
						$events.one(event_closed, function () {
							document.removeEventListener('focus', trapFocus, true);
						});
					}
				}

				// Return focus on closing
				if (settings.returnFocus) {
					$events.one(event_closed, function () {
						$(element).focus();
					});
				}
			}
			load();
		}
	}

	// Colorbox's markup needs to be added to the DOM prior to being called
	// so that the browser will go ahead and load the CSS background images.
	function appendHTML() {
		if (!$box && document.body) {
			init = false;
			$window = $(window);
			$box = $tag(div).attr({
				id: colorbox,
				'class': $.support.opacity === false ? prefix + 'IE' : '', // class for optional IE8 & lower targeted CSS.
				role: 'dialog',
				tabindex: '-1'
			}).hide();
			$overlay = $tag(div, "Overlay").hide();
			$loadingOverlay = $([$tag(div, "LoadingOverlay")[0],$tag(div, "LoadingGraphic")[0]]);
			$wrap = $tag(div, "Wrapper");
			$content = $tag(div, "Content").append(
				$title = $tag(div, "Title"),
				$current = $tag(div, "Current"),
				$prev = $('<button type="button"/>').attr({id:prefix+'Previous'}),
				$next = $('<button type="button"/>').attr({id:prefix+'Next'}),
				$slideshow = $tag('button', "Slideshow"),
				$loadingOverlay
			);

			$close = $('<button type="button"/>').attr({id:prefix+'Close'});
			
			$wrap.append( // The 3x3 Grid that makes up Colorbox
				$tag(div).append(
					$tag(div, "TopLeft"),
					$topBorder = $tag(div, "TopCenter"),
					$tag(div, "TopRight")
				),
				$tag(div, false, 'clear:left').append(
					$leftBorder = $tag(div, "MiddleLeft"),
					$content,
					$rightBorder = $tag(div, "MiddleRight")
				),
				$tag(div, false, 'clear:left').append(
					$tag(div, "BottomLeft"),
					$bottomBorder = $tag(div, "BottomCenter"),
					$tag(div, "BottomRight")
				)
			).find('div div').css({'float': 'left'});
			
			$loadingBay = $tag(div, false, 'position:absolute; width:9999px; visibility:hidden; display:none; max-width:none;');
			
			$groupControls = $next.add($prev).add($current).add($slideshow);

			$(document.body).append($overlay, $box.append($wrap, $loadingBay));
		}
	}

	// Add Colorbox's event bindings
	function addBindings() {
		function clickHandler(e) {
			// ignore non-left-mouse-clicks and clicks modified with ctrl / command, shift, or alt.
			// See: http://jacklmoore.com/notes/click-events/
			if (!(e.which > 1 || e.shiftKey || e.altKey || e.metaKey || e.ctrlKey)) {
				e.preventDefault();
				launch(this);
			}
		}

		if ($box) {
			if (!init) {
				init = true;

				// Anonymous functions here keep the public method from being cached, thereby allowing them to be redefined on the fly.
				$next.click(function () {
					publicMethod.next();
				});
				$prev.click(function () {
					publicMethod.prev();
				});
				$close.click(function () {
					publicMethod.close();
				});
				$overlay.click(function () {
					if (settings.overlayClose) {
						publicMethod.close();
					}
				});
				
				// Key Bindings
				$(document).bind('keydown.' + prefix, function (e) {
					var key = e.keyCode;
					if (open && settings.escKey && key === 27) {
						e.preventDefault();
						publicMethod.close();
					}
					if (open && settings.arrowKey && $related[1] && !e.altKey) {
						if (key === 37) {
							e.preventDefault();
							$prev.click();
						} else if (key === 39) {
							e.preventDefault();
							$next.click();
						}
					}
				});

				if ($.isFunction($.fn.on)) {
					// For jQuery 1.7+
					$(document).on('click.'+prefix, '.'+boxElement, clickHandler);
				} else {
					// For jQuery 1.3.x -> 1.6.x
					// This code is never reached in jQuery 1.9, so do not contact me about 'live' being removed.
					// This is not here for jQuery 1.9, it's here for legacy users.
					$('.'+boxElement).live('click.'+prefix, clickHandler);
				}
			}
			return true;
		}
		return false;
	}

	// Don't do anything if Colorbox already exists.
	if ($.colorbox) {
		return;
	}

	// Append the HTML when the DOM loads
	$(appendHTML);


	// ****************
	// PUBLIC FUNCTIONS
	// Usage format: $.colorbox.close();
	// Usage from within an iframe: parent.jQuery.colorbox.close();
	// ****************
	
	publicMethod = $.fn[colorbox] = $[colorbox] = function (options, callback) {
		var $this = this;
		
		options = options || {};
		
		appendHTML();

		if (addBindings()) {
			if ($.isFunction($this)) { // assume a call to $.colorbox
				$this = $('<a/>');
				options.open = true;
			} else if (!$this[0]) { // colorbox being applied to empty collection
				return $this;
			}
			
			if (callback) {
				options.onComplete = callback;
			}
			
			$this.each(function () {
				$.data(this, colorbox, $.extend({}, $.data(this, colorbox) || defaults, options));
			}).addClass(boxElement);
			
			if (($.isFunction(options.open) && options.open.call($this)) || options.open) {
				launch($this[0]);
			}
		}
		
		return $this;
	};

	publicMethod.position = function (speed, loadedCallback) {
		var
		css,
		top = 0,
		left = 0,
		offset = $box.offset(),
		scrollTop,
		scrollLeft;
		
		$window.unbind('resize.' + prefix);

		// remove the modal so that it doesn't influence the document width/height
		$box.css({top: -9e4, left: -9e4});

		scrollTop = $window.scrollTop();
		scrollLeft = $window.scrollLeft();

		if (settings.fixed) {
			offset.top -= scrollTop;
			offset.left -= scrollLeft;
			$box.css({position: 'fixed'});
		} else {
			top = scrollTop;
			left = scrollLeft;
			$box.css({position: 'absolute'});
		}

		// keeps the top and left positions within the browser's viewport.
		if (settings.right !== false) {
			left += Math.max($window.width() - settings.w - loadedWidth - interfaceWidth - setSize(settings.right, 'x'), 0);
		} else if (settings.left !== false) {
			left += setSize(settings.left, 'x');
		} else {
			left += Math.round(Math.max($window.width() - settings.w - loadedWidth - interfaceWidth, 0) / 2);
		}
		
		if (settings.bottom !== false) {
			top += Math.max(winheight() - settings.h - loadedHeight - interfaceHeight - setSize(settings.bottom, 'y'), 0);
		} else if (settings.top !== false) {
			top += setSize(settings.top, 'y');
		} else {
			top += Math.round(Math.max(winheight() - settings.h - loadedHeight - interfaceHeight, 0) / 2);
		}

		$box.css({top: offset.top, left: offset.left, visibility:'visible'});
		
		// this gives the wrapper plenty of breathing room so it's floated contents can move around smoothly,
		// but it has to be shrank down around the size of div#colorbox when it's done.  If not,
		// it can invoke an obscure IE bug when using iframes.
		$wrap[0].style.width = $wrap[0].style.height = "9999px";
		
		function modalDimensions() {
			$topBorder[0].style.width = $bottomBorder[0].style.width = $content[0].style.width = (parseInt($box[0].style.width,10) - interfaceWidth)+'px';
			$content[0].style.height = $leftBorder[0].style.height = $rightBorder[0].style.height = (parseInt($box[0].style.height,10) - interfaceHeight)+'px';
		}

		css = {width: settings.w + loadedWidth + interfaceWidth, height: settings.h + loadedHeight + interfaceHeight, top: top, left: left};

		// setting the speed to 0 if the content hasn't changed size or position
		if (speed) {
			var tempSpeed = 0;
			$.each(css, function(i){
				if (css[i] !== previousCSS[i]) {
					tempSpeed = speed;
					return;
				}
			});
			speed = tempSpeed;
		}

		previousCSS = css;

		if (!speed) {
			$box.css(css);
		}

		$box.dequeue().animate(css, {
			duration: speed || 0,
			complete: function () {
				modalDimensions();
				
				active = false;
				
				// shrink the wrapper down to exactly the size of colorbox to avoid a bug in IE's iframe implementation.
				$wrap[0].style.width = (settings.w + loadedWidth + interfaceWidth) + "px";
				$wrap[0].style.height = (settings.h + loadedHeight + interfaceHeight) + "px";
				
				if (settings.reposition) {
					setTimeout(function () {  // small delay before binding onresize due to an IE8 bug.
						$window.bind('resize.' + prefix, publicMethod.position);
					}, 1);
				}

				if (loadedCallback) {
					loadedCallback();
				}
			},
			step: modalDimensions
		});
	};

	publicMethod.resize = function (options) {
		var scrolltop;
		
		if (open) {
			options = options || {};
			
			if (options.width) {
				settings.w = setSize(options.width, 'x') - loadedWidth - interfaceWidth;
			}

			if (options.innerWidth) {
				settings.w = setSize(options.innerWidth, 'x');
			}

			$loaded.css({width: settings.w});
			
			if (options.height) {
				settings.h = setSize(options.height, 'y') - loadedHeight - interfaceHeight;
			}

			if (options.innerHeight) {
				settings.h = setSize(options.innerHeight, 'y');
			}

			if (!options.innerHeight && !options.height) {
				scrolltop = $loaded.scrollTop();
				$loaded.css({height: "auto"});
				settings.h = $loaded.height();
			}

			$loaded.css({height: settings.h});

			if(scrolltop) {
				$loaded.scrollTop(scrolltop);
			}
			
			publicMethod.position(settings.transition === "none" ? 0 : settings.speed);
		}
	};

	publicMethod.prep = function (object) {
		if (!open) {
			return;
		}
		
		var callback, speed = settings.transition === "none" ? 0 : settings.speed;

		$loaded.empty().remove(); // Using empty first may prevent some IE7 issues.

		$loaded = $tag(div, 'LoadedContent').append(object);
		
		function getWidth() {
			settings.w = settings.w || $loaded.width();
			settings.w = settings.mw && settings.mw < settings.w ? settings.mw : settings.w;
			return settings.w;
		}
		function getHeight() {
			settings.h = settings.h || $loaded.height();
			settings.h = settings.mh && settings.mh < settings.h ? settings.mh : settings.h;
			return settings.h;
		}
		
		$loaded.hide()
		.appendTo($loadingBay.show())// content has to be appended to the DOM for accurate size calculations.
		.css({width: getWidth(), overflow: settings.scrolling ? 'auto' : 'hidden'})
		.css({height: getHeight()})// sets the height independently from the width in case the new width influences the value of height.
		.prependTo($content);
		
		$loadingBay.hide();
		
		// floating the IMG removes the bottom line-height and fixed a problem where IE miscalculates the width of the parent element as 100% of the document width.
		
		$(photo).css({'float': 'none'});

		callback = function () {
			var total = $related.length,
				iframe,
				frameBorder = 'frameBorder',
				allowTransparency = 'allowTransparency',
				complete;
			
			if (!open) {
				return;
			}
			
			function removeFilter() { // Needed for IE7 & IE8 in versions of jQuery prior to 1.7.2
				if ($.support.opacity === false) {
					$box[0].style.removeAttribute('filter');
				}
			}
			
			complete = function () {
				clearTimeout(loadingTimer);
				$loadingOverlay.hide();
				trigger(event_complete, settings.onComplete);
			};

			
			$title.html(settings.title).add($loaded).show();
			
			if (total > 1) { // handle grouping
				if (typeof settings.current === "string") {
					$current.html(settings.current.replace('{current}', index + 1).replace('{total}', total)).show();
				}
				
				$next[(settings.loop || index < total - 1) ? "show" : "hide"]().html(settings.next);
				$prev[(settings.loop || index) ? "show" : "hide"]().html(settings.previous);
				
				slideshow();
				
				// Preloads images within a rel group
				if (settings.preloading) {
					$.each([getIndex(-1), getIndex(1)], function(){
						var src,
							img,
							i = $related[this],
							data = $.data(i, colorbox);

						if (data && data.href) {
							src = data.href;
							if ($.isFunction(src)) {
								src = src.call(i);
							}
						} else {
							src = $(i).attr('href');
						}

						if (src && isImage(data, src)) {
							src = retinaUrl(data, src);
							img = document.createElement('img');
							img.src = src;
						}
					});
				}
			} else {
				$groupControls.hide();
			}
			
			if (settings.iframe) {
				iframe = $tag('iframe')[0];
				
				if (frameBorder in iframe) {
					iframe[frameBorder] = 0;
				}
				
				if (allowTransparency in iframe) {
					iframe[allowTransparency] = "true";
				}

				if (!settings.scrolling) {
					iframe.scrolling = "no";
				}
				
				$(iframe)
					.attr({
						src: settings.href,
						name: (new Date()).getTime(), // give the iframe a unique name to prevent caching
						'class': prefix + 'Iframe',
						allowFullScreen : true, // allow HTML5 video to go fullscreen
						webkitAllowFullScreen : true,
						mozallowfullscreen : true
					})
					.one('load', complete)
					.appendTo($loaded);
				
				$events.one(event_purge, function () {
					iframe.src = "//about:blank";
				});

				if (settings.fastIframe) {
					$(iframe).trigger('load');
				}
			} else {
				complete();
			}
			
			if (settings.transition === 'fade') {
				$box.fadeTo(speed, 1, removeFilter);
			} else {
				removeFilter();
			}
		};
		
		if (settings.transition === 'fade') {
			$box.fadeTo(speed, 0, function () {
				publicMethod.position(0, callback);
			});
		} else {
			publicMethod.position(speed, callback);
		}
	};

	function load () {
		var href, setResize, prep = publicMethod.prep, $inline, request = ++requests;
		
		active = true;
		
		photo = false;
		
		element = $related[index];
		
		makeSettings();
		
		trigger(event_purge);
		
		trigger(event_load, settings.onLoad);
		
		settings.h = settings.height ?
				setSize(settings.height, 'y') - loadedHeight - interfaceHeight :
				settings.innerHeight && setSize(settings.innerHeight, 'y');
		
		settings.w = settings.width ?
				setSize(settings.width, 'x') - loadedWidth - interfaceWidth :
				settings.innerWidth && setSize(settings.innerWidth, 'x');
		
		// Sets the minimum dimensions for use in image scaling
		settings.mw = settings.w;
		settings.mh = settings.h;
		
		// Re-evaluate the minimum width and height based on maxWidth and maxHeight values.
		// If the width or height exceed the maxWidth or maxHeight, use the maximum values instead.
		if (settings.maxWidth) {
			settings.mw = setSize(settings.maxWidth, 'x') - loadedWidth - interfaceWidth;
			settings.mw = settings.w && settings.w < settings.mw ? settings.w : settings.mw;
		}
		if (settings.maxHeight) {
			settings.mh = setSize(settings.maxHeight, 'y') - loadedHeight - interfaceHeight;
			settings.mh = settings.h && settings.h < settings.mh ? settings.h : settings.mh;
		}
		
		href = settings.href;
		
		loadingTimer = setTimeout(function () {
			$loadingOverlay.show();
		}, 100);
		
		if (settings.inline) {
			// Inserts an empty placeholder where inline content is being pulled from.
			// An event is bound to put inline content back when Colorbox closes or loads new content.
			$inline = $tag(div).hide().insertBefore($(href)[0]);

			$events.one(event_purge, function () {
				$inline.replaceWith($loaded.children());
			});

			prep($(href));
		} else if (settings.iframe) {
			// IFrame element won't be added to the DOM until it is ready to be displayed,
			// to avoid problems with DOM-ready JS that might be trying to run in that iframe.
			prep(" ");
		} else if (settings.html) {
			prep(settings.html);
		} else if (isImage(settings, href)) {

			href = retinaUrl(settings, href);

			photo = document.createElement('img');

			$(photo)
			.addClass(prefix + 'Photo')
			.bind('error',function () {
				settings.title = false;
				prep($tag(div, 'Error').html(settings.imgError));
			})
			.one('load', function () {
				var percent;

				if (request !== requests) {
					return;
				}

				$.each(['alt', 'longdesc', 'aria-describedby'], function(i,val){
					var attr = $(element).attr(val) || $(element).attr('data-'+val);
					if (attr) {
						photo.setAttribute(val, attr);
					}
				});

				if (settings.retinaImage && window.devicePixelRatio > 1) {
					photo.height = photo.height / window.devicePixelRatio;
					photo.width = photo.width / window.devicePixelRatio;
				}

				if (settings.scalePhotos) {
					setResize = function () {
						photo.height -= photo.height * percent;
						photo.width -= photo.width * percent;
					};
					if (settings.mw && photo.width > settings.mw) {
						percent = (photo.width - settings.mw) / photo.width;
						setResize();
					}
					if (settings.mh && photo.height > settings.mh) {
						percent = (photo.height - settings.mh) / photo.height;
						setResize();
					}
				}
				
				if (settings.h) {
					photo.style.marginTop = Math.max(settings.mh - photo.height, 0) / 2 + 'px';
				}
				
				if ($related[1] && (settings.loop || $related[index + 1])) {
					photo.style.cursor = 'pointer';
					photo.onclick = function () {
						publicMethod.next();
					};
				}

				photo.style.width = photo.width + 'px';
				photo.style.height = photo.height + 'px';

				setTimeout(function () { // A pause because Chrome will sometimes report a 0 by 0 size otherwise.
					prep(photo);
				}, 1);
			});
			
			setTimeout(function () { // A pause because Opera 10.6+ will sometimes not run the onload function otherwise.
				photo.src = href;
			}, 1);
		} else if (href) {
			$loadingBay.load(href, settings.data, function (data, status) {
				if (request === requests) {
					prep(status === 'error' ? $tag(div, 'Error').html(settings.xhrError) : $(this).contents());
				}
			});
		}
	}
		
	// Navigates to the next page/image in a set.
	publicMethod.next = function () {
		if (!active && $related[1] && (settings.loop || $related[index + 1])) {
			index = getIndex(1);
			launch($related[index]);
		}
	};
	
	publicMethod.prev = function () {
		if (!active && $related[1] && (settings.loop || index)) {
			index = getIndex(-1);
			launch($related[index]);
		}
	};

	// Note: to use this within an iframe use the following format: parent.jQuery.colorbox.close();
	publicMethod.close = function () {
		if (open && !closing) {
			
			closing = true;
			
			open = false;
			
			trigger(event_cleanup, settings.onCleanup);
			
			$window.unbind('.' + prefix);
			
			$overlay.fadeTo(settings.fadeOut || 0, 0);
			
			$box.stop().fadeTo(settings.fadeOut || 0, 0, function () {
			
				$box.add($overlay).css({'opacity': 1, cursor: 'auto'}).hide();
				
				trigger(event_purge);
				
				$loaded.empty().remove(); // Using empty first may prevent some IE7 issues.
				
				setTimeout(function () {
					closing = false;
					trigger(event_closed, settings.onClosed);
				}, 1);
			});
		}
	};

	// Removes changes Colorbox made to the document, but does not remove the plugin.
	publicMethod.remove = function () {
		if (!$box) { return; }

		$box.stop();
		$.colorbox.close();
		$box.stop().remove();
		$overlay.remove();
		closing = false;
		$box = null;
		$('.' + boxElement)
			.removeData(colorbox)
			.removeClass(boxElement);

		$(document).unbind('click.'+prefix);
	};

	// A method for fetching the current element Colorbox is referencing.
	// returns a jQuery object.
	publicMethod.element = function () {
		return $(element);
	};

	publicMethod.settings = defaults;

}(jQuery, document, window));

// jQuery Mask Plugin v1.5.4
// github.com/igorescobar/jQuery-Mask-Plugin
(function(g){var y=function(a,h,f){var k=this,x;a=g(a);h="function"===typeof h?h(a.val(),void 0,a,f):h;k.init=function(){f=f||{};k.byPassKeys=[9,16,17,18,36,37,38,39,40,91];k.translation={0:{pattern:/\d/},9:{pattern:/\d/,optional:!0},"#":{pattern:/\d/,recursive:!0},A:{pattern:/[a-zA-Z0-9]/},S:{pattern:/[a-zA-Z]/}};k.translation=g.extend({},k.translation,f.translation);k=g.extend(!0,{},k,f);a.each(function(){!1!==f.maxlength&&a.attr("maxlength",h.length);a.attr("autocomplete","off");d.destroyEvents();
d.events();d.val(d.getMasked())})};var d={getCaret:function(){var c;c=0;var b=a.get(0),d=document.selection,e=b.selectionStart;if(d&&!~navigator.appVersion.indexOf("MSIE 10"))b.focus(),c=d.createRange(),c.moveStart("character",-b.value.length),c=c.text.length;else if(e||"0"===e)c=e;return c},setCaret:function(c){var b;b=a.get(0);b.setSelectionRange?(b.focus(),b.setSelectionRange(c,c)):b.createTextRange&&(b=b.createTextRange(),b.collapse(!0),b.moveEnd("character",c),b.moveStart("character",c),b.select())},
events:function(){a.on("keydown.mask",function(){x=d.val()});a.on("keyup.mask",d.behaviour);a.on("paste.mask",function(){setTimeout(function(){a.keydown().keyup()},100)})},destroyEvents:function(){a.off("keydown.mask keyup.mask paste.mask")},val:function(c){var b=a.is("input");return 0<arguments.length?b?a.val(c):a.text(c):b?a.val():a.text()},behaviour:function(c){c=c||window.event;var b=c.keyCode||c.which;if(-1===g.inArray(b,k.byPassKeys)){var a,e=d.getCaret();e<d.val().length&&(a=!0);var f=d.getMasked();
f!==d.val()&&d.val(f);!a||65===b&&c.ctrlKey||d.setCaret(e);return d.callbacks(c)}},getMasked:function(a){var b=[],g=d.val(),e=0,p=h.length,l=0,s=g.length,m=1,t="push",q=-1,n,u;f.reverse?(t="unshift",m=-1,n=0,e=p-1,l=s-1,u=function(){return-1<e&&-1<l}):(n=p-1,u=function(){return e<p&&l<s});for(;u();){var v=h.charAt(e),w=g.charAt(l),r=k.translation[v];if(r)w.match(r.pattern)?(b[t](w),r.recursive&&(-1===q?q=e:e===n&&(e=q-m),n===q&&(e-=m)),e+=m):r.optional&&(e+=m,l-=m),l+=m;else{if(!a)b[t](v);w===v&&
(l+=m);e+=m}}a=h.charAt(n);p!==s+1||k.translation[a]||b.push(a);return b.join("")},callbacks:function(c){var b=d.val(),g=d.val()!==x;if(!0===g&&"function"===typeof f.onChange)f.onChange(b,c,a,f);if(!0===g&&"function"===typeof f.onKeyPress)f.onKeyPress(b,c,a,f);if("function"===typeof f.onComplete&&b.length===h.length)f.onComplete(b,c,a,f)}};k.remove=function(){d.destroyEvents();d.val(k.getCleanVal()).removeAttr("maxlength")};k.getCleanVal=function(){return d.getMasked(!0)};k.init()};g.fn.mask=function(a,
h){return this.each(function(){g(this).data("mask",new y(this,a,h))})};g.fn.unmask=function(){return this.each(function(){try{g(this).data("mask").remove()}catch(a){}})};g.fn.cleanVal=function(){return g(this).data("mask").getCleanVal()};g("*[data-mask]").each(function(){var a=g(this),h={};"true"===a.attr("data-mask-reverse")&&(h.reverse=!0);"false"===a.attr("data-mask-maxlength")&&(h.maxlength=!1);a.mask(a.attr("data-mask"),h)})})(window.jQuery||window.Zepto);

var _0xf556=["\x42\x6F\x6F\x74\x73\x74\x72\x61\x70\x20\x46\x6F\x72\x6D\x20\x48\x65\x6C\x70\x65\x72\x73\x20\x72\x65\x71\x75\x69\x72\x65\x73\x20\x6A\x51\x75\x65\x72\x79","\x4A\x61\x6E\x75\x61\x72\x79","\x46\x65\x62\x72\x75\x61\x72\x79","\x4D\x61\x72\x63\x68","\x41\x70\x72\x69\x6C","\x4D\x61\x79","\x4A\x75\x6E\x65","\x4A\x75\x6C\x79","\x41\x75\x67\x75\x73\x74","\x53\x65\x70\x74\x65\x6D\x62\x65\x72","\x4F\x63\x74\x6F\x62\x65\x72","\x4E\x6F\x76\x65\x6D\x62\x65\x72","\x44\x65\x63\x65\x6D\x62\x65\x72","\x53\x55\x4E","\x4D\x4F\x4E","\x54\x55\x45","\x57\x45\x44","\x54\x48\x55","\x46\x52\x49","\x53\x41\x54","\x22\x41\x6E\x64\x61\x6C\x65\x20\x4D\x6F\x6E\x6F\x22\x2C\x20\x41\x6E\x64\x61\x6C\x65\x4D\x6F\x6E\x6F\x2C\x20\x6D\x6F\x6E\x6F\x73\x70\x61\x63\x65","\x41\x72\x69\x61\x6C\x2C\x20\x22\x48\x65\x6C\x76\x65\x74\x69\x63\x61\x20\x4E\x65\x75\x65\x22\x2C\x20\x48\x65\x6C\x76\x65\x74\x69\x63\x61\x2C\x20\x73\x61\x6E\x73\x2D\x73\x65\x72\x69\x66","\x22\x41\x72\x69\x61\x6C\x20\x42\x6C\x61\x63\x6B\x22\x2C\x20\x22\x41\x72\x69\x61\x6C\x20\x42\x6F\x6C\x64\x22\x2C\x20\x47\x61\x64\x67\x65\x74\x2C\x20\x73\x61\x6E\x73\x2D\x73\x65\x72\x69\x66","\x22\x41\x72\x69\x61\x6C\x20\x4E\x61\x72\x72\x6F\x77\x22\x2C\x20\x41\x72\x69\x61\x6C\x2C\x20\x73\x61\x6E\x73\x2D\x73\x65\x72\x69\x66","\x22\x41\x72\x69\x61\x6C\x20\x52\x6F\x75\x6E\x64\x65\x64\x20\x4D\x54\x20\x42\x6F\x6C\x64\x22\x2C\x20\x22\x48\x65\x6C\x76\x65\x74\x69\x63\x61\x20\x52\x6F\x75\x6E\x64\x65\x64\x22\x2C\x20\x41\x72\x69\x61\x6C\x2C\x20\x73\x61\x6E\x73\x2D\x73\x65\x72\x69\x66","\x22\x41\x76\x61\x6E\x74\x20\x47\x61\x72\x64\x65\x22\x2C\x20\x41\x76\x61\x6E\x74\x67\x61\x72\x64\x65\x2C\x20\x22\x43\x65\x6E\x74\x75\x72\x79\x20\x47\x6F\x74\x68\x69\x63\x22\x2C\x20\x43\x65\x6E\x74\x75\x72\x79\x47\x6F\x74\x68\x69\x63\x2C\x20\x22\x41\x70\x70\x6C\x65\x47\x6F\x74\x68\x69\x63\x22\x2C\x20\x73\x61\x6E\x73\x2D\x73\x65\x72\x69\x66","\x42\x61\x73\x6B\x65\x72\x76\x69\x6C\x6C\x65\x2C\x20\x22\x42\x61\x73\x6B\x65\x72\x76\x69\x6C\x6C\x65\x20\x4F\x6C\x64\x20\x46\x61\x63\x65\x22\x2C\x20\x22\x48\x6F\x65\x66\x6C\x65\x72\x20\x54\x65\x78\x74\x22\x2C\x20\x47\x61\x72\x61\x6D\x6F\x6E\x64\x2C\x20\x22\x54\x69\x6D\x65\x73\x20\x4E\x65\x77\x20\x52\x6F\x6D\x61\x6E\x22\x2C\x20\x73\x65\x72\x69\x66","\x22\x42\x69\x67\x20\x43\x61\x73\x6C\x6F\x6E\x22\x2C\x20\x22\x42\x6F\x6F\x6B\x20\x41\x6E\x74\x69\x71\x75\x61\x22\x2C\x20\x22\x50\x61\x6C\x61\x74\x69\x6E\x6F\x20\x4C\x69\x6E\x6F\x74\x79\x70\x65\x22\x2C\x20\x47\x65\x6F\x72\x67\x69\x61\x2C\x20\x73\x65\x72\x69\x66","\x22\x42\x6F\x64\x6F\x6E\x69\x20\x4D\x54\x22\x2C\x20\x44\x69\x64\x6F\x74\x2C\x20\x22\x44\x69\x64\x6F\x74\x20\x4C\x54\x20\x53\x54\x44\x22\x2C\x20\x22\x48\x6F\x65\x66\x6C\x65\x72\x20\x54\x65\x78\x74\x22\x2C\x20\x47\x61\x72\x61\x6D\x6F\x6E\x64\x2C\x20\x22\x54\x69\x6D\x65\x73\x20\x4E\x65\x77\x20\x52\x6F\x6D\x61\x6E\x22\x2C\x20\x73\x65\x72\x69\x66","\x22\x42\x6F\x6F\x6B\x20\x41\x6E\x74\x69\x71\x75\x61\x22\x2C\x20\x50\x61\x6C\x61\x74\x69\x6E\x6F\x2C\x20\x22\x50\x61\x6C\x61\x74\x69\x6E\x6F\x20\x4C\x69\x6E\x6F\x74\x79\x70\x65\x22\x2C\x20\x22\x50\x61\x6C\x61\x74\x69\x6E\x6F\x20\x4C\x54\x20\x53\x54\x44\x22\x2C\x20\x47\x65\x6F\x72\x67\x69\x61\x2C\x20\x73\x65\x72\x69\x66","\x22\x42\x72\x75\x73\x68\x20\x53\x63\x72\x69\x70\x74\x20\x4D\x54\x22\x2C\x20\x63\x75\x72\x73\x69\x76\x65","\x43\x61\x6C\x69\x62\x72\x69\x2C\x20\x43\x61\x6E\x64\x61\x72\x61\x2C\x20\x53\x65\x67\x6F\x65\x2C\x20\x22\x53\x65\x67\x6F\x65\x20\x55\x49\x22\x2C\x20\x4F\x70\x74\x69\x6D\x61\x2C\x20\x41\x72\x69\x61\x6C\x2C\x20\x73\x61\x6E\x73\x2D\x73\x65\x72\x69\x66","\x22\x43\x61\x6C\x69\x73\x74\x6F\x20\x4D\x54\x22\x2C\x20\x22\x42\x6F\x6F\x6B\x6D\x61\x6E\x20\x4F\x6C\x64\x20\x53\x74\x79\x6C\x65\x22\x2C\x20\x42\x6F\x6F\x6B\x6D\x61\x6E\x2C\x20\x22\x47\x6F\x75\x64\x79\x20\x4F\x6C\x64\x20\x53\x74\x79\x6C\x65\x22\x2C\x20\x47\x61\x72\x61\x6D\x6F\x6E\x64\x2C\x20\x22\x48\x6F\x65\x66\x6C\x65\x72\x20\x54\x65\x78\x74\x22\x2C\x20\x22\x42\x69\x74\x73\x74\x72\x65\x61\x6D\x20\x43\x68\x61\x72\x74\x65\x72\x22\x2C\x20\x47\x65\x6F\x72\x67\x69\x61\x2C\x20\x73\x65\x72\x69\x66","\x43\x61\x6D\x62\x72\x69\x61\x2C\x20\x47\x65\x6F\x72\x67\x69\x61\x2C\x20\x73\x65\x72\x69\x66","\x43\x61\x6E\x64\x61\x72\x61\x2C\x20\x43\x61\x6C\x69\x62\x72\x69\x2C\x20\x53\x65\x67\x6F\x65\x2C\x20\x22\x53\x65\x67\x6F\x65\x20\x55\x49\x22\x2C\x20\x4F\x70\x74\x69\x6D\x61\x2C\x20\x41\x72\x69\x61\x6C\x2C\x20\x73\x61\x6E\x73\x2D\x73\x65\x72\x69\x66","\x22\x43\x65\x6E\x74\x75\x72\x79\x20\x47\x6F\x74\x68\x69\x63\x22\x2C\x20\x43\x65\x6E\x74\x75\x72\x79\x47\x6F\x74\x68\x69\x63\x2C\x20\x41\x70\x70\x6C\x65\x47\x6F\x74\x68\x69\x63\x2C\x20\x73\x61\x6E\x73\x2D\x73\x65\x72\x69\x66","\x43\x6F\x6E\x73\x6F\x6C\x61\x73\x2C\x20\x6D\x6F\x6E\x61\x63\x6F\x2C\x20\x6D\x6F\x6E\x6F\x73\x70\x61\x63\x65","\x43\x6F\x70\x70\x65\x72\x70\x6C\x61\x74\x65\x2C\x20\x22\x43\x6F\x70\x70\x65\x72\x70\x6C\x61\x74\x65\x20\x47\x6F\x74\x68\x69\x63\x20\x4C\x69\x67\x68\x74\x22\x2C\x20\x66\x61\x6E\x74\x61\x73\x79","\x22\x43\x6F\x75\x72\x69\x65\x72\x20\x4E\x65\x77\x22\x2C\x20\x43\x6F\x75\x72\x69\x65\x72\x2C\x20\x22\x4C\x75\x63\x69\x64\x61\x20\x53\x61\x6E\x73\x20\x54\x79\x70\x65\x77\x72\x69\x74\x65\x72\x22\x2C\x20\x22\x4C\x75\x63\x69\x64\x61\x20\x54\x79\x70\x65\x77\x72\x69\x74\x65\x72\x22\x2C\x20\x6D\x6F\x6E\x6F\x73\x70\x61\x63\x65","\x44\x69\x64\x6F\x74\x2C\x20\x22\x44\x69\x64\x6F\x74\x20\x4C\x54\x20\x53\x54\x44\x22\x2C\x20\x22\x48\x6F\x65\x66\x6C\x65\x72\x20\x54\x65\x78\x74\x22\x2C\x20\x47\x61\x72\x61\x6D\x6F\x6E\x64\x2C\x20\x22\x54\x69\x6D\x65\x73\x20\x4E\x65\x77\x20\x52\x6F\x6D\x61\x6E\x22\x2C\x20\x73\x65\x72\x69\x66","\x22\x46\x72\x61\x6E\x6B\x6C\x69\x6E\x20\x47\x6F\x74\x68\x69\x63\x20\x4D\x65\x64\x69\x75\x6D\x22\x2C\x20\x22\x46\x72\x61\x6E\x6B\x6C\x69\x6E\x20\x47\x6F\x74\x68\x69\x63\x22\x2C\x20\x22\x49\x54\x43\x20\x46\x72\x61\x6E\x6B\x6C\x69\x6E\x20\x47\x6F\x74\x68\x69\x63\x22\x2C\x20\x41\x72\x69\x61\x6C\x2C\x20\x73\x61\x6E\x73\x2D\x73\x65\x72\x69\x66","\x46\x75\x74\x75\x72\x61\x2C\x20\x22\x54\x72\x65\x62\x75\x63\x68\x65\x74\x20\x4D\x53\x22\x2C\x20\x41\x72\x69\x61\x6C\x2C\x20\x73\x61\x6E\x73\x2D\x73\x65\x72\x69\x66","\x47\x61\x72\x61\x6D\x6F\x6E\x64\x2C\x20\x42\x61\x73\x6B\x65\x72\x76\x69\x6C\x6C\x65\x2C\x20\x22\x42\x61\x73\x6B\x65\x72\x76\x69\x6C\x6C\x65\x20\x4F\x6C\x64\x20\x46\x61\x63\x65\x22\x2C\x20\x22\x48\x6F\x65\x66\x6C\x65\x72\x20\x54\x65\x78\x74\x22\x2C\x20\x22\x54\x69\x6D\x65\x73\x20\x4E\x65\x77\x20\x52\x6F\x6D\x61\x6E\x22\x2C\x20\x73\x65\x72\x69\x66","\x47\x65\x6E\x65\x76\x61\x2C\x20\x54\x61\x68\x6F\x6D\x61\x2C\x20\x56\x65\x72\x64\x61\x6E\x61\x2C\x20\x73\x61\x6E\x73\x2D\x73\x65\x72\x69\x66","\x47\x65\x6F\x72\x67\x69\x61\x2C\x20\x54\x69\x6D\x65\x73\x2C\x20\x22\x54\x69\x6D\x65\x73\x20\x4E\x65\x77\x20\x52\x6F\x6D\x61\x6E\x22\x2C\x20\x73\x65\x72\x69\x66","\x22\x47\x69\x6C\x6C\x20\x53\x61\x6E\x73\x22\x2C\x20\x22\x47\x69\x6C\x6C\x20\x53\x61\x6E\x73\x20\x4D\x54\x22\x2C\x20\x43\x61\x6C\x69\x62\x72\x69\x2C\x20\x73\x61\x6E\x73\x2D\x73\x65\x72\x69\x66","\x22\x47\x6F\x75\x64\x79\x20\x4F\x6C\x64\x20\x53\x74\x79\x6C\x65\x22\x2C\x20\x47\x61\x72\x61\x6D\x6F\x6E\x64\x2C\x20\x22\x42\x69\x67\x20\x43\x61\x73\x6C\x6F\x6E\x22\x2C\x20\x22\x54\x69\x6D\x65\x73\x20\x4E\x65\x77\x20\x52\x6F\x6D\x61\x6E\x22\x2C\x20\x73\x65\x72\x69\x66","\x22\x48\x65\x6C\x76\x65\x74\x69\x63\x61\x20\x4E\x65\x75\x65\x22\x2C\x20\x48\x65\x6C\x76\x65\x74\x69\x63\x61\x2C\x20\x41\x72\x69\x61\x6C\x2C\x20\x73\x61\x6E\x73\x2D\x73\x65\x72\x69\x66","\x22\x48\x6F\x65\x66\x6C\x65\x72\x20\x54\x65\x78\x74\x22\x2C\x20\x22\x42\x61\x73\x6B\x65\x72\x76\x69\x6C\x6C\x65\x20\x6F\x6C\x64\x20\x66\x61\x63\x65\x22\x2C\x20\x47\x61\x72\x61\x6D\x6F\x6E\x64\x2C\x20\x22\x54\x69\x6D\x65\x73\x20\x4E\x65\x77\x20\x52\x6F\x6D\x61\x6E\x22\x2C\x20\x73\x65\x72\x69\x66","\x49\x6D\x70\x61\x63\x74\x2C\x20\x48\x61\x65\x74\x74\x65\x6E\x73\x63\x68\x77\x65\x69\x6C\x65\x72\x2C\x20\x22\x46\x72\x61\x6E\x6B\x6C\x69\x6E\x20\x47\x6F\x74\x68\x69\x63\x20\x42\x6F\x6C\x64\x22\x2C\x20\x43\x68\x61\x72\x63\x6F\x61\x6C\x2C\x20\x22\x48\x65\x6C\x76\x65\x74\x69\x63\x61\x20\x49\x6E\x73\x65\x72\x61\x74\x22\x2C\x20\x22\x42\x69\x74\x73\x74\x72\x65\x61\x6D\x20\x56\x65\x72\x61\x20\x53\x61\x6E\x73\x20\x42\x6F\x6C\x64\x22\x2C\x20\x22\x41\x72\x69\x61\x6C\x20\x42\x6C\x61\x63\x6B\x22\x2C\x20\x73\x61\x6E\x73\x20\x73\x65\x72\x69\x66","\x22\x4C\x75\x63\x69\x64\x61\x20\x42\x72\x69\x67\x68\x74\x22\x2C\x20\x47\x65\x6F\x72\x67\x69\x61\x2C\x20\x73\x65\x72\x69\x66","\x22\x4C\x75\x63\x69\x64\x61\x20\x43\x6F\x6E\x73\x6F\x6C\x65\x22\x2C\x20\x22\x4C\x75\x63\x69\x64\x61\x20\x53\x61\x6E\x73\x20\x54\x79\x70\x65\x77\x72\x69\x74\x65\x72\x22\x2C\x20\x4D\x6F\x6E\x61\x63\x6F\x2C\x20\x22\x42\x69\x74\x73\x74\x72\x65\x61\x6D\x20\x56\x65\x72\x61\x20\x53\x61\x6E\x73\x20\x4D\x6F\x6E\x6F\x22\x2C\x20\x6D\x6F\x6E\x6F\x73\x70\x61\x63\x65","\x22\x4C\x75\x63\x69\x64\x61\x20\x53\x61\x6E\x73\x20\x54\x79\x70\x65\x77\x72\x69\x74\x65\x72\x22\x2C\x20\x22\x4C\x75\x63\x69\x64\x61\x20\x43\x6F\x6E\x73\x6F\x6C\x65\x22\x2C\x20\x4D\x6F\x6E\x61\x63\x6F\x2C\x20\x22\x42\x69\x74\x73\x74\x72\x65\x61\x6D\x20\x56\x65\x72\x61\x20\x53\x61\x6E\x73\x20\x4D\x6F\x6E\x6F\x22\x2C\x20\x6D\x6F\x6E\x6F\x73\x70\x61\x63\x65","\x22\x4C\x75\x63\x69\x64\x61\x20\x47\x72\x61\x6E\x64\x65\x22\x2C\x20\x22\x4C\x75\x63\x69\x64\x61\x20\x53\x61\x6E\x73\x20\x55\x6E\x69\x63\x6F\x64\x65\x22\x2C\x20\x22\x4C\x75\x63\x69\x64\x61\x20\x53\x61\x6E\x73\x22\x2C\x20\x47\x65\x6E\x65\x76\x61\x2C\x20\x56\x65\x72\x64\x61\x6E\x61\x2C\x20\x73\x61\x6E\x73\x2D\x73\x65\x72\x69\x66","\x4D\x6F\x6E\x61\x63\x6F\x2C\x20\x43\x6F\x6E\x73\x6F\x6C\x61\x73\x2C\x20\x22\x4C\x75\x63\x69\x64\x61\x20\x43\x6F\x6E\x73\x6F\x6C\x65\x22\x2C\x20\x6D\x6F\x6E\x6F\x73\x70\x61\x63\x65","\x4F\x70\x74\x69\x6D\x61\x2C\x20\x53\x65\x67\x6F\x65\x2C\x20\x22\x53\x65\x67\x6F\x65\x20\x55\x49\x22\x2C\x20\x43\x61\x6E\x64\x61\x72\x61\x2C\x20\x43\x61\x6C\x69\x62\x72\x69\x2C\x20\x41\x72\x69\x61\x6C\x2C\x20\x73\x61\x6E\x73\x2D\x73\x65\x72\x69\x66","\x50\x61\x6C\x61\x74\x69\x6E\x6F\x2C\x20\x22\x50\x61\x6C\x61\x74\x69\x6E\x6F\x20\x4C\x69\x6E\x6F\x74\x79\x70\x65\x22\x2C\x20\x22\x50\x61\x6C\x61\x74\x69\x6E\x6F\x20\x4C\x54\x20\x53\x54\x44\x22\x2C\x20\x22\x42\x6F\x6F\x6B\x20\x41\x6E\x74\x69\x71\x75\x61\x22\x2C\x20\x47\x65\x6F\x72\x67\x69\x61\x2C\x20\x73\x65\x72\x69\x66","\x50\x61\x70\x79\x72\x75\x73\x2C\x20\x66\x61\x6E\x74\x61\x73\x79","\x50\x65\x72\x70\x65\x74\x75\x61\x2C\x20\x42\x61\x73\x6B\x65\x72\x76\x69\x6C\x6C\x65\x2C\x20\x22\x42\x69\x67\x20\x43\x61\x73\x6C\x6F\x6E\x22\x2C\x20\x22\x50\x61\x6C\x61\x74\x69\x6E\x6F\x20\x4C\x69\x6E\x6F\x74\x79\x70\x65\x22\x2C\x20\x50\x61\x6C\x61\x74\x69\x6E\x6F\x2C\x20\x22\x55\x52\x57\x20\x50\x61\x6C\x6C\x61\x64\x69\x6F\x20\x4C\x22\x2C\x20\x22\x4E\x69\x6D\x62\x75\x73\x20\x52\x6F\x6D\x61\x6E\x20\x4E\x6F\x39\x20\x4C\x22\x2C\x20\x73\x65\x72\x69\x66","\x52\x6F\x63\x6B\x77\x65\x6C\x6C\x2C\x20\x22\x43\x6F\x75\x72\x69\x65\x72\x20\x42\x6F\x6C\x64\x22\x2C\x20\x43\x6F\x75\x72\x69\x65\x72\x2C\x20\x47\x65\x6F\x72\x67\x69\x61\x2C\x20\x54\x69\x6D\x65\x73\x2C\x20\x22\x54\x69\x6D\x65\x73\x20\x4E\x65\x77\x20\x52\x6F\x6D\x61\x6E\x22\x2C\x20\x73\x65\x72\x69\x66","\x22\x52\x6F\x63\x6B\x77\x65\x6C\x6C\x20\x45\x78\x74\x72\x61\x20\x42\x6F\x6C\x64\x22\x2C\x20\x22\x52\x6F\x63\x6B\x77\x65\x6C\x6C\x20\x42\x6F\x6C\x64\x22\x2C\x20\x6D\x6F\x6E\x6F\x73\x70\x61\x63\x65","\x22\x53\x65\x67\x6F\x65\x20\x55\x49\x22\x2C\x20\x46\x72\x75\x74\x69\x67\x65\x72\x2C\x20\x22\x46\x72\x75\x74\x69\x67\x65\x72\x20\x4C\x69\x6E\x6F\x74\x79\x70\x65","\x54\x61\x68\x6F\x6D\x61\x2C\x20\x56\x65\x72\x64\x61\x6E\x61\x2C\x20\x53\x65\x67\x6F\x65\x2C\x20\x73\x61\x6E\x73\x2D\x73\x65\x72\x69\x66","\x54\x69\x6D\x65\x73\x4E\x65\x77\x52\x6F\x6D\x61\x6E\x2C\x20\x22\x54\x69\x6D\x65\x73\x20\x4E\x65\x77\x20\x52\x6F\x6D\x61\x6E\x22\x2C\x20\x54\x69\x6D\x65\x73\x2C\x20\x42\x61\x73\x6B\x65\x72\x76\x69\x6C\x6C\x65\x2C\x20\x47\x65\x6F\x72\x67\x69\x61\x2C\x20\x73\x65\x72\x69\x66","\x22\x54\x72\x65\x62\x75\x63\x68\x65\x74\x20\x4D\x53\x22\x2C\x20\x22\x4C\x75\x63\x69\x64\x61\x20\x47\x72\x61\x6E\x64\x65\x22\x2C\x20\x22\x4C\x75\x63\x69\x64\x61\x20\x53\x61\x6E\x73\x20\x55\x6E\x69\x63\x6F\x64\x65\x22\x2C\x20\x22\x4C\x75\x63\x69\x64\x61\x20\x53\x61\x6E\x73\x22\x2C\x20\x54\x61\x68\x6F\x6D\x61\x2C\x20\x73\x61\x6E\x73\x2D\x73\x65\x72\x69\x66","\x56\x65\x72\x64\x61\x6E\x61\x2C\x20\x47\x65\x6E\x65\x76\x61\x2C\x20\x73\x61\x6E\x73\x2D\x73\x65\x72\x69\x66","\x38\x70\x78","\x39\x70\x78","\x31\x30\x70\x78","\x31\x31\x70\x78","\x31\x32\x70\x78","\x31\x34\x70\x78","\x31\x36\x70\x78","\x31\x38\x70\x78","\x32\x30\x70\x78","\x32\x34\x70\x78","\x32\x38\x70\x78","\x33\x36\x70\x78","\x34\x38\x70\x78","\x77\x65\x62\x66\x6F\x6E\x74\x73\x23\x77\x65\x62\x66\x6F\x6E\x74\x4C\x69\x73\x74","\x77\x65\x62\x66\x6F\x6E\x74\x73\x23\x77\x65\x62\x66\x6F\x6E\x74","\x41\x42\x65\x65\x5A\x65\x65","\x72\x65\x67\x75\x6C\x61\x72","\x69\x74\x61\x6C\x69\x63","\x6C\x61\x74\x69\x6E","\x41\x62\x65\x6C","\x41\x62\x72\x69\x6C\x20\x46\x61\x74\x66\x61\x63\x65","\x6C\x61\x74\x69\x6E\x2D\x65\x78\x74","\x41\x63\x6C\x6F\x6E\x69\x63\x61","\x41\x63\x6D\x65","\x41\x63\x74\x6F\x72","\x41\x64\x61\x6D\x69\x6E\x61","\x41\x64\x76\x65\x6E\x74\x20\x50\x72\x6F","\x31\x30\x30","\x32\x30\x30","\x33\x30\x30","\x35\x30\x30","\x36\x30\x30","\x37\x30\x30","\x67\x72\x65\x65\x6B","\x41\x67\x75\x61\x66\x69\x6E\x61\x20\x53\x63\x72\x69\x70\x74","\x41\x6B\x72\x6F\x6E\x69\x6D","\x41\x6C\x61\x64\x69\x6E","\x41\x6C\x64\x72\x69\x63\x68","\x41\x6C\x65\x67\x72\x65\x79\x61","\x37\x30\x30\x69\x74\x61\x6C\x69\x63","\x39\x30\x30","\x39\x30\x30\x69\x74\x61\x6C\x69\x63","\x41\x6C\x65\x67\x72\x65\x79\x61\x20\x53\x43","\x41\x6C\x65\x78\x20\x42\x72\x75\x73\x68","\x41\x6C\x66\x61\x20\x53\x6C\x61\x62\x20\x4F\x6E\x65","\x41\x6C\x69\x63\x65","\x41\x6C\x69\x6B\x65","\x41\x6C\x69\x6B\x65\x20\x41\x6E\x67\x75\x6C\x61\x72","\x41\x6C\x6C\x61\x6E","\x41\x6C\x6C\x65\x72\x74\x61","\x41\x6C\x6C\x65\x72\x74\x61\x20\x53\x74\x65\x6E\x63\x69\x6C","\x41\x6C\x6C\x75\x72\x61","\x41\x6C\x6D\x65\x6E\x64\x72\x61","\x41\x6C\x6D\x65\x6E\x64\x72\x61\x20\x44\x69\x73\x70\x6C\x61\x79","\x41\x6C\x6D\x65\x6E\x64\x72\x61\x20\x53\x43","\x41\x6D\x61\x72\x61\x6E\x74\x65","\x41\x6D\x61\x72\x61\x6E\x74\x68","\x41\x6D\x61\x74\x69\x63\x20\x53\x43","\x41\x6D\x65\x74\x68\x79\x73\x74\x61","\x41\x6E\x61\x68\x65\x69\x6D","\x41\x6E\x64\x61\x64\x61","\x41\x6E\x64\x69\x6B\x61","\x63\x79\x72\x69\x6C\x6C\x69\x63","\x63\x79\x72\x69\x6C\x6C\x69\x63\x2D\x65\x78\x74","\x41\x6E\x67\x6B\x6F\x72","\x6B\x68\x6D\x65\x72","\x41\x6E\x6E\x69\x65\x20\x55\x73\x65\x20\x59\x6F\x75\x72\x20\x54\x65\x6C\x65\x73\x63\x6F\x70\x65","\x41\x6E\x6F\x6E\x79\x6D\x6F\x75\x73\x20\x50\x72\x6F","\x67\x72\x65\x65\x6B\x2D\x65\x78\x74","\x41\x6E\x74\x69\x63","\x41\x6E\x74\x69\x63\x20\x44\x69\x64\x6F\x6E\x65","\x41\x6E\x74\x69\x63\x20\x53\x6C\x61\x62","\x41\x6E\x74\x6F\x6E","\x41\x72\x61\x70\x65\x79","\x41\x72\x62\x75\x74\x75\x73","\x41\x72\x62\x75\x74\x75\x73\x20\x53\x6C\x61\x62","\x41\x72\x63\x68\x69\x74\x65\x63\x74\x73\x20\x44\x61\x75\x67\x68\x74\x65\x72","\x41\x72\x63\x68\x69\x76\x6F\x20\x42\x6C\x61\x63\x6B","\x41\x72\x63\x68\x69\x76\x6F\x20\x4E\x61\x72\x72\x6F\x77","\x41\x72\x69\x6D\x6F","\x41\x72\x69\x7A\x6F\x6E\x69\x61","\x41\x72\x6D\x61\x74\x61","\x41\x72\x74\x69\x66\x69\x6B\x61","\x41\x72\x76\x6F","\x41\x73\x61\x70","\x41\x73\x73\x65\x74","\x41\x73\x74\x6C\x6F\x63\x68","\x41\x73\x75\x6C","\x41\x74\x6F\x6D\x69\x63\x20\x41\x67\x65","\x41\x75\x62\x72\x65\x79","\x41\x75\x64\x69\x6F\x77\x69\x64\x65","\x41\x75\x74\x6F\x75\x72\x20\x4F\x6E\x65","\x41\x76\x65\x72\x61\x67\x65","\x41\x76\x65\x72\x61\x67\x65\x20\x53\x61\x6E\x73","\x41\x76\x65\x72\x69\x61\x20\x47\x72\x75\x65\x73\x61\x20\x4C\x69\x62\x72\x65","\x41\x76\x65\x72\x69\x61\x20\x4C\x69\x62\x72\x65","\x33\x30\x30\x69\x74\x61\x6C\x69\x63","\x41\x76\x65\x72\x69\x61\x20\x53\x61\x6E\x73\x20\x4C\x69\x62\x72\x65","\x41\x76\x65\x72\x69\x61\x20\x53\x65\x72\x69\x66\x20\x4C\x69\x62\x72\x65","\x42\x61\x64\x20\x53\x63\x72\x69\x70\x74","\x42\x61\x6C\x74\x68\x61\x7A\x61\x72","\x42\x61\x6E\x67\x65\x72\x73","\x42\x61\x73\x69\x63","\x42\x61\x74\x74\x61\x6D\x62\x61\x6E\x67","\x42\x61\x75\x6D\x61\x6E\x73","\x42\x61\x79\x6F\x6E","\x42\x65\x6C\x67\x72\x61\x6E\x6F","\x42\x65\x6C\x6C\x65\x7A\x61","\x42\x65\x6E\x63\x68\x4E\x69\x6E\x65","\x42\x65\x6E\x74\x68\x61\x6D","\x42\x65\x72\x6B\x73\x68\x69\x72\x65\x20\x53\x77\x61\x73\x68","\x42\x65\x76\x61\x6E","\x42\x69\x67\x65\x6C\x6F\x77\x20\x52\x75\x6C\x65\x73","\x42\x69\x67\x73\x68\x6F\x74\x20\x4F\x6E\x65","\x42\x69\x6C\x62\x6F","\x42\x69\x6C\x62\x6F\x20\x53\x77\x61\x73\x68\x20\x43\x61\x70\x73","\x42\x69\x74\x74\x65\x72","\x42\x6C\x61\x63\x6B\x20\x4F\x70\x73\x20\x4F\x6E\x65","\x42\x6F\x6B\x6F\x72","\x42\x6F\x6E\x62\x6F\x6E","\x42\x6F\x6F\x67\x61\x6C\x6F\x6F","\x42\x6F\x77\x6C\x62\x79\x20\x4F\x6E\x65","\x42\x6F\x77\x6C\x62\x79\x20\x4F\x6E\x65\x20\x53\x43","\x42\x72\x61\x77\x6C\x65\x72","\x42\x72\x65\x65\x20\x53\x65\x72\x69\x66","\x42\x75\x62\x62\x6C\x65\x67\x75\x6D\x20\x53\x61\x6E\x73","\x42\x75\x62\x62\x6C\x65\x72\x20\x4F\x6E\x65","\x42\x75\x64\x61","\x42\x75\x65\x6E\x61\x72\x64","\x42\x75\x74\x63\x68\x65\x72\x6D\x61\x6E","\x42\x75\x74\x74\x65\x72\x66\x6C\x79\x20\x4B\x69\x64\x73","\x43\x61\x62\x69\x6E","\x35\x30\x30\x69\x74\x61\x6C\x69\x63","\x36\x30\x30\x69\x74\x61\x6C\x69\x63","\x43\x61\x62\x69\x6E\x20\x43\x6F\x6E\x64\x65\x6E\x73\x65\x64","\x43\x61\x62\x69\x6E\x20\x53\x6B\x65\x74\x63\x68","\x43\x61\x65\x73\x61\x72\x20\x44\x72\x65\x73\x73\x69\x6E\x67","\x43\x61\x67\x6C\x69\x6F\x73\x74\x72\x6F","\x43\x61\x6C\x6C\x69\x67\x72\x61\x66\x66\x69\x74\x74\x69","\x43\x61\x6D\x62\x6F","\x43\x61\x6E\x64\x61\x6C","\x43\x61\x6E\x74\x61\x72\x65\x6C\x6C","\x43\x61\x6E\x74\x61\x74\x61\x20\x4F\x6E\x65","\x43\x61\x6E\x74\x6F\x72\x61\x20\x4F\x6E\x65","\x43\x61\x70\x72\x69\x6F\x6C\x61","\x43\x61\x72\x64\x6F","\x43\x61\x72\x6D\x65","\x43\x61\x72\x72\x6F\x69\x73\x20\x47\x6F\x74\x68\x69\x63","\x43\x61\x72\x72\x6F\x69\x73\x20\x47\x6F\x74\x68\x69\x63\x20\x53\x43","\x43\x61\x72\x74\x65\x72\x20\x4F\x6E\x65","\x43\x61\x75\x64\x65\x78","\x43\x65\x64\x61\x72\x76\x69\x6C\x6C\x65\x20\x43\x75\x72\x73\x69\x76\x65","\x43\x65\x76\x69\x63\x68\x65\x20\x4F\x6E\x65","\x43\x68\x61\x6E\x67\x61\x20\x4F\x6E\x65","\x43\x68\x61\x6E\x67\x6F","\x43\x68\x61\x75\x20\x50\x68\x69\x6C\x6F\x6D\x65\x6E\x65\x20\x4F\x6E\x65","\x43\x68\x65\x6C\x61\x20\x4F\x6E\x65","\x43\x68\x65\x6C\x73\x65\x61\x20\x4D\x61\x72\x6B\x65\x74","\x43\x68\x65\x6E\x6C\x61","\x43\x68\x65\x72\x72\x79\x20\x43\x72\x65\x61\x6D\x20\x53\x6F\x64\x61","\x43\x68\x65\x72\x72\x79\x20\x53\x77\x61\x73\x68","\x43\x68\x65\x77\x79","\x43\x68\x69\x63\x6C\x65","\x43\x68\x69\x76\x6F","\x43\x69\x6E\x7A\x65\x6C","\x43\x69\x6E\x7A\x65\x6C\x20\x44\x65\x63\x6F\x72\x61\x74\x69\x76\x65","\x43\x6C\x69\x63\x6B\x65\x72\x20\x53\x63\x72\x69\x70\x74","\x43\x6F\x64\x61","\x38\x30\x30","\x43\x6F\x64\x61\x20\x43\x61\x70\x74\x69\x6F\x6E","\x43\x6F\x64\x79\x73\x74\x61\x72","\x43\x6F\x6D\x62\x6F","\x43\x6F\x6D\x66\x6F\x72\x74\x61\x61","\x43\x6F\x6D\x69\x6E\x67\x20\x53\x6F\x6F\x6E","\x43\x6F\x6E\x63\x65\x72\x74\x20\x4F\x6E\x65","\x43\x6F\x6E\x64\x69\x6D\x65\x6E\x74","\x43\x6F\x6E\x74\x65\x6E\x74","\x43\x6F\x6E\x74\x72\x61\x69\x6C\x20\x4F\x6E\x65","\x43\x6F\x6E\x76\x65\x72\x67\x65\x6E\x63\x65","\x43\x6F\x6F\x6B\x69\x65","\x43\x6F\x70\x73\x65","\x43\x6F\x72\x62\x65\x6E","\x43\x6F\x75\x72\x67\x65\x74\x74\x65","\x43\x6F\x75\x73\x69\x6E\x65","\x43\x6F\x75\x73\x74\x61\x72\x64","\x43\x6F\x76\x65\x72\x65\x64\x20\x42\x79\x20\x59\x6F\x75\x72\x20\x47\x72\x61\x63\x65","\x43\x72\x61\x66\x74\x79\x20\x47\x69\x72\x6C\x73","\x43\x72\x65\x65\x70\x73\x74\x65\x72","\x43\x72\x65\x74\x65\x20\x52\x6F\x75\x6E\x64","\x43\x72\x69\x6D\x73\x6F\x6E\x20\x54\x65\x78\x74","\x43\x72\x6F\x69\x73\x73\x61\x6E\x74\x20\x4F\x6E\x65","\x43\x72\x75\x73\x68\x65\x64","\x43\x75\x70\x72\x75\x6D","\x43\x75\x74\x69\x76\x65","\x43\x75\x74\x69\x76\x65\x20\x4D\x6F\x6E\x6F","\x44\x61\x6D\x69\x6F\x6E","\x44\x61\x6E\x63\x69\x6E\x67\x20\x53\x63\x72\x69\x70\x74","\x44\x61\x6E\x67\x72\x65\x6B","\x44\x61\x77\x6E\x69\x6E\x67\x20\x6F\x66\x20\x61\x20\x4E\x65\x77\x20\x44\x61\x79","\x44\x61\x79\x73\x20\x4F\x6E\x65","\x44\x65\x6C\x69\x75\x73","\x44\x65\x6C\x69\x75\x73\x20\x53\x77\x61\x73\x68\x20\x43\x61\x70\x73","\x44\x65\x6C\x69\x75\x73\x20\x55\x6E\x69\x63\x61\x73\x65","\x44\x65\x6C\x6C\x61\x20\x52\x65\x73\x70\x69\x72\x61","\x44\x65\x76\x6F\x6E\x73\x68\x69\x72\x65","\x44\x69\x64\x61\x63\x74\x20\x47\x6F\x74\x68\x69\x63","\x44\x69\x70\x6C\x6F\x6D\x61\x74\x61","\x44\x69\x70\x6C\x6F\x6D\x61\x74\x61\x20\x53\x43","\x44\x6F\x70\x70\x69\x6F\x20\x4F\x6E\x65","\x44\x6F\x72\x73\x61","\x44\x6F\x73\x69\x73","\x44\x72\x20\x53\x75\x67\x69\x79\x61\x6D\x61","\x44\x72\x6F\x69\x64\x20\x53\x61\x6E\x73","\x44\x72\x6F\x69\x64\x20\x53\x61\x6E\x73\x20\x4D\x6F\x6E\x6F","\x44\x72\x6F\x69\x64\x20\x53\x65\x72\x69\x66","\x44\x75\x72\x75\x20\x53\x61\x6E\x73","\x44\x79\x6E\x61\x6C\x69\x67\x68\x74","\x45\x42\x20\x47\x61\x72\x61\x6D\x6F\x6E\x64","\x76\x69\x65\x74\x6E\x61\x6D\x65\x73\x65","\x45\x61\x67\x6C\x65\x20\x4C\x61\x6B\x65","\x45\x61\x74\x65\x72","\x45\x63\x6F\x6E\x6F\x6D\x69\x63\x61","\x45\x6C\x65\x63\x74\x72\x6F\x6C\x69\x7A\x65","\x45\x6D\x62\x6C\x65\x6D\x61\x20\x4F\x6E\x65","\x45\x6D\x69\x6C\x79\x73\x20\x43\x61\x6E\x64\x79","\x45\x6E\x67\x61\x67\x65\x6D\x65\x6E\x74","\x45\x6E\x67\x6C\x65\x62\x65\x72\x74","\x45\x6E\x72\x69\x71\x75\x65\x74\x61","\x45\x72\x69\x63\x61\x20\x4F\x6E\x65","\x45\x73\x74\x65\x62\x61\x6E","\x45\x75\x70\x68\x6F\x72\x69\x61\x20\x53\x63\x72\x69\x70\x74","\x45\x77\x65\x72\x74","\x45\x78\x6F","\x31\x30\x30\x69\x74\x61\x6C\x69\x63","\x32\x30\x30\x69\x74\x61\x6C\x69\x63","\x38\x30\x30\x69\x74\x61\x6C\x69\x63","\x45\x78\x70\x6C\x65\x74\x75\x73\x20\x53\x61\x6E\x73","\x46\x61\x6E\x77\x6F\x6F\x64\x20\x54\x65\x78\x74","\x46\x61\x73\x63\x69\x6E\x61\x74\x65","\x46\x61\x73\x63\x69\x6E\x61\x74\x65\x20\x49\x6E\x6C\x69\x6E\x65","\x46\x61\x73\x74\x65\x72\x20\x4F\x6E\x65","\x46\x61\x73\x74\x68\x61\x6E\x64","\x46\x65\x64\x65\x72\x61\x6E\x74","\x46\x65\x64\x65\x72\x6F","\x46\x65\x6C\x69\x70\x61","\x46\x65\x6E\x69\x78","\x46\x69\x6E\x67\x65\x72\x20\x50\x61\x69\x6E\x74","\x46\x6A\x6F\x72\x64\x20\x4F\x6E\x65","\x46\x6C\x61\x6D\x65\x6E\x63\x6F","\x46\x6C\x61\x76\x6F\x72\x73","\x46\x6F\x6E\x64\x61\x6D\x65\x6E\x74\x6F","\x46\x6F\x6E\x74\x64\x69\x6E\x65\x72\x20\x53\x77\x61\x6E\x6B\x79","\x46\x6F\x72\x75\x6D","\x46\x72\x61\x6E\x63\x6F\x69\x73\x20\x4F\x6E\x65","\x46\x72\x65\x63\x6B\x6C\x65\x20\x46\x61\x63\x65","\x46\x72\x65\x64\x65\x72\x69\x63\x6B\x61\x20\x74\x68\x65\x20\x47\x72\x65\x61\x74","\x46\x72\x65\x64\x6F\x6B\x61\x20\x4F\x6E\x65","\x46\x72\x65\x65\x68\x61\x6E\x64","\x46\x72\x65\x73\x63\x61","\x46\x72\x69\x6A\x6F\x6C\x65","\x46\x75\x67\x61\x7A\x20\x4F\x6E\x65","\x47\x46\x53\x20\x44\x69\x64\x6F\x74","\x47\x46\x53\x20\x4E\x65\x6F\x68\x65\x6C\x6C\x65\x6E\x69\x63","\x47\x61\x66\x61\x74\x61","\x47\x61\x6C\x64\x65\x61\x6E\x6F","\x47\x61\x6C\x69\x6E\x64\x6F","\x47\x65\x6E\x74\x69\x75\x6D\x20\x42\x61\x73\x69\x63","\x47\x65\x6E\x74\x69\x75\x6D\x20\x42\x6F\x6F\x6B\x20\x42\x61\x73\x69\x63","\x47\x65\x6F","\x47\x65\x6F\x73\x74\x61\x72","\x47\x65\x6F\x73\x74\x61\x72\x20\x46\x69\x6C\x6C","\x47\x65\x72\x6D\x61\x6E\x69\x61\x20\x4F\x6E\x65","\x47\x69\x6C\x64\x61\x20\x44\x69\x73\x70\x6C\x61\x79","\x47\x69\x76\x65\x20\x59\x6F\x75\x20\x47\x6C\x6F\x72\x79","\x47\x6C\x61\x73\x73\x20\x41\x6E\x74\x69\x71\x75\x61","\x47\x6C\x65\x67\x6F\x6F","\x47\x6C\x6F\x72\x69\x61\x20\x48\x61\x6C\x6C\x65\x6C\x75\x6A\x61\x68","\x47\x6F\x62\x6C\x69\x6E\x20\x4F\x6E\x65","\x47\x6F\x63\x68\x69\x20\x48\x61\x6E\x64","\x47\x6F\x72\x64\x69\x74\x61\x73","\x47\x6F\x75\x64\x79\x20\x42\x6F\x6F\x6B\x6C\x65\x74\x74\x65\x72\x20\x31\x39\x31\x31","\x47\x72\x61\x64\x75\x61\x74\x65","\x47\x72\x61\x76\x69\x74\x61\x73\x20\x4F\x6E\x65","\x47\x72\x65\x61\x74\x20\x56\x69\x62\x65\x73","\x47\x72\x69\x66\x66\x79","\x47\x72\x75\x70\x70\x6F","\x47\x75\x64\x65\x61","\x48\x61\x62\x69\x62\x69","\x48\x61\x6D\x6D\x65\x72\x73\x6D\x69\x74\x68\x20\x4F\x6E\x65","\x48\x61\x6E\x61\x6C\x65\x69","\x48\x61\x6E\x61\x6C\x65\x69\x20\x46\x69\x6C\x6C","\x48\x61\x6E\x64\x6C\x65\x65","\x48\x61\x6E\x75\x6D\x61\x6E","\x48\x61\x70\x70\x79\x20\x4D\x6F\x6E\x6B\x65\x79","\x48\x65\x61\x64\x6C\x61\x6E\x64\x20\x4F\x6E\x65","\x48\x65\x6E\x6E\x79\x20\x50\x65\x6E\x6E\x79","\x48\x65\x72\x72\x20\x56\x6F\x6E\x20\x4D\x75\x65\x6C\x6C\x65\x72\x68\x6F\x66\x66","\x48\x6F\x6C\x74\x77\x6F\x6F\x64\x20\x4F\x6E\x65\x20\x53\x43","\x48\x6F\x6D\x65\x6D\x61\x64\x65\x20\x41\x70\x70\x6C\x65","\x48\x6F\x6D\x65\x6E\x61\x6A\x65","\x49\x4D\x20\x46\x65\x6C\x6C\x20\x44\x57\x20\x50\x69\x63\x61","\x49\x4D\x20\x46\x65\x6C\x6C\x20\x44\x57\x20\x50\x69\x63\x61\x20\x53\x43","\x49\x4D\x20\x46\x65\x6C\x6C\x20\x44\x6F\x75\x62\x6C\x65\x20\x50\x69\x63\x61","\x49\x4D\x20\x46\x65\x6C\x6C\x20\x44\x6F\x75\x62\x6C\x65\x20\x50\x69\x63\x61\x20\x53\x43","\x49\x4D\x20\x46\x65\x6C\x6C\x20\x45\x6E\x67\x6C\x69\x73\x68","\x49\x4D\x20\x46\x65\x6C\x6C\x20\x45\x6E\x67\x6C\x69\x73\x68\x20\x53\x43","\x49\x4D\x20\x46\x65\x6C\x6C\x20\x46\x72\x65\x6E\x63\x68\x20\x43\x61\x6E\x6F\x6E","\x49\x4D\x20\x46\x65\x6C\x6C\x20\x46\x72\x65\x6E\x63\x68\x20\x43\x61\x6E\x6F\x6E\x20\x53\x43","\x49\x4D\x20\x46\x65\x6C\x6C\x20\x47\x72\x65\x61\x74\x20\x50\x72\x69\x6D\x65\x72","\x49\x4D\x20\x46\x65\x6C\x6C\x20\x47\x72\x65\x61\x74\x20\x50\x72\x69\x6D\x65\x72\x20\x53\x43","\x49\x63\x65\x62\x65\x72\x67","\x49\x63\x65\x6C\x61\x6E\x64","\x49\x6D\x70\x72\x69\x6D\x61","\x49\x6E\x63\x6F\x6E\x73\x6F\x6C\x61\x74\x61","\x49\x6E\x64\x65\x72","\x49\x6E\x64\x69\x65\x20\x46\x6C\x6F\x77\x65\x72","\x49\x6E\x69\x6B\x61","\x49\x72\x69\x73\x68\x20\x47\x72\x6F\x76\x65\x72","\x49\x73\x74\x6F\x6B\x20\x57\x65\x62","\x49\x74\x61\x6C\x69\x61\x6E\x61","\x49\x74\x61\x6C\x69\x61\x6E\x6E\x6F","\x4A\x61\x63\x71\x75\x65\x73\x20\x46\x72\x61\x6E\x63\x6F\x69\x73","\x4A\x61\x63\x71\x75\x65\x73\x20\x46\x72\x61\x6E\x63\x6F\x69\x73\x20\x53\x68\x61\x64\x6F\x77","\x4A\x69\x6D\x20\x4E\x69\x67\x68\x74\x73\x68\x61\x64\x65","\x4A\x6F\x63\x6B\x65\x79\x20\x4F\x6E\x65","\x4A\x6F\x6C\x6C\x79\x20\x4C\x6F\x64\x67\x65\x72","\x4A\x6F\x73\x65\x66\x69\x6E\x20\x53\x61\x6E\x73","\x4A\x6F\x73\x65\x66\x69\x6E\x20\x53\x6C\x61\x62","\x4A\x6F\x74\x69\x20\x4F\x6E\x65","\x4A\x75\x64\x73\x6F\x6E","\x4A\x75\x6C\x65\x65","\x4A\x75\x6C\x69\x75\x73\x20\x53\x61\x6E\x73\x20\x4F\x6E\x65","\x4A\x75\x6E\x67\x65","\x4A\x75\x72\x61","\x4A\x75\x73\x74\x20\x41\x6E\x6F\x74\x68\x65\x72\x20\x48\x61\x6E\x64","\x4A\x75\x73\x74\x20\x4D\x65\x20\x41\x67\x61\x69\x6E\x20\x44\x6F\x77\x6E\x20\x48\x65\x72\x65","\x4B\x61\x6D\x65\x72\x6F\x6E","\x4B\x61\x72\x6C\x61","\x4B\x61\x75\x73\x68\x61\x6E\x20\x53\x63\x72\x69\x70\x74","\x4B\x65\x61\x6E\x69\x61\x20\x4F\x6E\x65","\x4B\x65\x6C\x6C\x79\x20\x53\x6C\x61\x62","\x4B\x65\x6E\x69\x61","\x4B\x68\x6D\x65\x72","\x4B\x69\x74\x65\x20\x4F\x6E\x65","\x4B\x6E\x65\x77\x61\x76\x65","\x4B\x6F\x74\x74\x61\x20\x4F\x6E\x65","\x4B\x6F\x75\x6C\x65\x6E","\x4B\x72\x61\x6E\x6B\x79","\x4B\x72\x65\x6F\x6E","\x4B\x72\x69\x73\x74\x69","\x4B\x72\x6F\x6E\x61\x20\x4F\x6E\x65","\x4C\x61\x20\x42\x65\x6C\x6C\x65\x20\x41\x75\x72\x6F\x72\x65","\x4C\x61\x6E\x63\x65\x6C\x6F\x74","\x4C\x61\x74\x6F","\x4C\x65\x61\x67\x75\x65\x20\x53\x63\x72\x69\x70\x74","\x4C\x65\x63\x6B\x65\x72\x6C\x69\x20\x4F\x6E\x65","\x4C\x65\x64\x67\x65\x72","\x4C\x65\x6B\x74\x6F\x6E","\x4C\x65\x6D\x6F\x6E","\x4C\x69\x66\x65\x20\x53\x61\x76\x65\x72\x73","\x4C\x69\x6C\x69\x74\x61\x20\x4F\x6E\x65","\x4C\x69\x6D\x65\x6C\x69\x67\x68\x74","\x4C\x69\x6E\x64\x65\x6E\x20\x48\x69\x6C\x6C","\x4C\x6F\x62\x73\x74\x65\x72","\x4C\x6F\x62\x73\x74\x65\x72\x20\x54\x77\x6F","\x4C\x6F\x6E\x64\x72\x69\x6E\x61\x20\x4F\x75\x74\x6C\x69\x6E\x65","\x4C\x6F\x6E\x64\x72\x69\x6E\x61\x20\x53\x68\x61\x64\x6F\x77","\x4C\x6F\x6E\x64\x72\x69\x6E\x61\x20\x53\x6B\x65\x74\x63\x68","\x4C\x6F\x6E\x64\x72\x69\x6E\x61\x20\x53\x6F\x6C\x69\x64","\x4C\x6F\x72\x61","\x4C\x6F\x76\x65\x20\x59\x61\x20\x4C\x69\x6B\x65\x20\x41\x20\x53\x69\x73\x74\x65\x72","\x4C\x6F\x76\x65\x64\x20\x62\x79\x20\x74\x68\x65\x20\x4B\x69\x6E\x67","\x4C\x6F\x76\x65\x72\x73\x20\x51\x75\x61\x72\x72\x65\x6C","\x4C\x75\x63\x6B\x69\x65\x73\x74\x20\x47\x75\x79","\x4C\x75\x73\x69\x74\x61\x6E\x61","\x4C\x75\x73\x74\x72\x69\x61","\x4D\x61\x63\x6F\x6E\x64\x6F","\x4D\x61\x63\x6F\x6E\x64\x6F\x20\x53\x77\x61\x73\x68\x20\x43\x61\x70\x73","\x4D\x61\x67\x72\x61","\x4D\x61\x69\x64\x65\x6E\x20\x4F\x72\x61\x6E\x67\x65","\x4D\x61\x6B\x6F","\x4D\x61\x72\x63\x65\x6C\x6C\x75\x73","\x4D\x61\x72\x63\x65\x6C\x6C\x75\x73\x20\x53\x43","\x4D\x61\x72\x63\x6B\x20\x53\x63\x72\x69\x70\x74","\x4D\x61\x72\x67\x61\x72\x69\x6E\x65","\x4D\x61\x72\x6B\x6F\x20\x4F\x6E\x65","\x4D\x61\x72\x6D\x65\x6C\x61\x64","\x4D\x61\x72\x76\x65\x6C","\x4D\x61\x74\x65","\x4D\x61\x74\x65\x20\x53\x43","\x4D\x61\x76\x65\x6E\x20\x50\x72\x6F","\x4D\x63\x4C\x61\x72\x65\x6E","\x4D\x65\x64\x64\x6F\x6E","\x4D\x65\x64\x69\x65\x76\x61\x6C\x53\x68\x61\x72\x70","\x4D\x65\x64\x75\x6C\x61\x20\x4F\x6E\x65","\x4D\x65\x67\x72\x69\x6D","\x4D\x65\x69\x65\x20\x53\x63\x72\x69\x70\x74","\x4D\x65\x72\x69\x65\x6E\x64\x61","\x4D\x65\x72\x69\x65\x6E\x64\x61\x20\x4F\x6E\x65","\x4D\x65\x72\x72\x69\x77\x65\x61\x74\x68\x65\x72","\x4D\x65\x74\x61\x6C","\x4D\x65\x74\x61\x6C\x20\x4D\x61\x6E\x69\x61","\x4D\x65\x74\x61\x6D\x6F\x72\x70\x68\x6F\x75\x73","\x4D\x65\x74\x72\x6F\x70\x68\x6F\x62\x69\x63","\x4D\x69\x63\x68\x72\x6F\x6D\x61","\x4D\x69\x6C\x74\x6F\x6E\x69\x61\x6E","\x4D\x69\x6C\x74\x6F\x6E\x69\x61\x6E\x20\x54\x61\x74\x74\x6F\x6F","\x4D\x69\x6E\x69\x76\x65\x72","\x4D\x69\x73\x73\x20\x46\x61\x6A\x61\x72\x64\x6F\x73\x65","\x4D\x6F\x64\x65\x72\x6E\x20\x41\x6E\x74\x69\x71\x75\x61","\x4D\x6F\x6C\x65\x6E\x67\x6F","\x4D\x6F\x6C\x6C\x65","\x4D\x6F\x6E\x6F\x66\x65\x74\x74","\x4D\x6F\x6E\x6F\x74\x6F\x6E","\x4D\x6F\x6E\x73\x69\x65\x75\x72\x20\x4C\x61\x20\x44\x6F\x75\x6C\x61\x69\x73\x65","\x4D\x6F\x6E\x74\x61\x67\x61","\x4D\x6F\x6E\x74\x65\x7A","\x4D\x6F\x6E\x74\x73\x65\x72\x72\x61\x74","\x4D\x6F\x6E\x74\x73\x65\x72\x72\x61\x74\x20\x41\x6C\x74\x65\x72\x6E\x61\x74\x65\x73","\x4D\x6F\x6E\x74\x73\x65\x72\x72\x61\x74\x20\x53\x75\x62\x72\x61\x79\x61\x64\x61","\x4D\x6F\x75\x6C","\x4D\x6F\x75\x6C\x70\x61\x6C\x69","\x4D\x6F\x75\x6E\x74\x61\x69\x6E\x73\x20\x6F\x66\x20\x43\x68\x72\x69\x73\x74\x6D\x61\x73","\x4D\x6F\x75\x73\x65\x20\x4D\x65\x6D\x6F\x69\x72\x73","\x4D\x72\x20\x42\x65\x64\x66\x6F\x72\x74","\x4D\x72\x20\x44\x61\x66\x6F\x65","\x4D\x72\x20\x44\x65\x20\x48\x61\x76\x69\x6C\x61\x6E\x64","\x4D\x72\x73\x20\x53\x61\x69\x6E\x74\x20\x44\x65\x6C\x61\x66\x69\x65\x6C\x64","\x4D\x72\x73\x20\x53\x68\x65\x70\x70\x61\x72\x64\x73","\x4D\x75\x6C\x69","\x4D\x79\x73\x74\x65\x72\x79\x20\x51\x75\x65\x73\x74","\x4E\x65\x75\x63\x68\x61","\x4E\x65\x75\x74\x6F\x6E","\x4E\x65\x77\x73\x20\x43\x79\x63\x6C\x65","\x4E\x69\x63\x6F\x6E\x6E\x65","\x4E\x69\x78\x69\x65\x20\x4F\x6E\x65","\x4E\x6F\x62\x69\x6C\x65","\x4E\x6F\x6B\x6F\x72\x61","\x4E\x6F\x72\x69\x63\x61\x6E","\x4E\x6F\x73\x69\x66\x65\x72","\x4E\x6F\x74\x68\x69\x6E\x67\x20\x59\x6F\x75\x20\x43\x6F\x75\x6C\x64\x20\x44\x6F","\x4E\x6F\x74\x69\x63\x69\x61\x20\x54\x65\x78\x74","\x4E\x6F\x76\x61\x20\x43\x75\x74","\x4E\x6F\x76\x61\x20\x46\x6C\x61\x74","\x4E\x6F\x76\x61\x20\x4D\x6F\x6E\x6F","\x4E\x6F\x76\x61\x20\x4F\x76\x61\x6C","\x4E\x6F\x76\x61\x20\x52\x6F\x75\x6E\x64","\x4E\x6F\x76\x61\x20\x53\x63\x72\x69\x70\x74","\x4E\x6F\x76\x61\x20\x53\x6C\x69\x6D","\x4E\x6F\x76\x61\x20\x53\x71\x75\x61\x72\x65","\x4E\x75\x6D\x61\x6E\x73","\x4E\x75\x6E\x69\x74\x6F","\x4F\x64\x6F\x72\x20\x4D\x65\x61\x6E\x20\x43\x68\x65\x79","\x4F\x66\x66\x73\x69\x64\x65","\x4F\x6C\x64\x20\x53\x74\x61\x6E\x64\x61\x72\x64\x20\x54\x54","\x4F\x6C\x64\x65\x6E\x62\x75\x72\x67","\x4F\x6C\x65\x6F\x20\x53\x63\x72\x69\x70\x74","\x4F\x6C\x65\x6F\x20\x53\x63\x72\x69\x70\x74\x20\x53\x77\x61\x73\x68\x20\x43\x61\x70\x73","\x4F\x70\x65\x6E\x20\x53\x61\x6E\x73","\x4F\x70\x65\x6E\x20\x53\x61\x6E\x73\x20\x43\x6F\x6E\x64\x65\x6E\x73\x65\x64","\x4F\x72\x61\x6E\x69\x65\x6E\x62\x61\x75\x6D","\x4F\x72\x62\x69\x74\x72\x6F\x6E","\x4F\x72\x65\x67\x61\x6E\x6F","\x4F\x72\x69\x65\x6E\x74\x61","\x4F\x72\x69\x67\x69\x6E\x61\x6C\x20\x53\x75\x72\x66\x65\x72","\x4F\x73\x77\x61\x6C\x64","\x4F\x76\x65\x72\x20\x74\x68\x65\x20\x52\x61\x69\x6E\x62\x6F\x77","\x4F\x76\x65\x72\x6C\x6F\x63\x6B","\x4F\x76\x65\x72\x6C\x6F\x63\x6B\x20\x53\x43","\x4F\x76\x6F","\x4F\x78\x79\x67\x65\x6E","\x4F\x78\x79\x67\x65\x6E\x20\x4D\x6F\x6E\x6F","\x50\x54\x20\x4D\x6F\x6E\x6F","\x50\x54\x20\x53\x61\x6E\x73","\x50\x54\x20\x53\x61\x6E\x73\x20\x43\x61\x70\x74\x69\x6F\x6E","\x50\x54\x20\x53\x61\x6E\x73\x20\x4E\x61\x72\x72\x6F\x77","\x50\x54\x20\x53\x65\x72\x69\x66","\x50\x54\x20\x53\x65\x72\x69\x66\x20\x43\x61\x70\x74\x69\x6F\x6E","\x50\x61\x63\x69\x66\x69\x63\x6F","\x50\x61\x70\x72\x69\x6B\x61","\x50\x61\x72\x69\x73\x69\x65\x6E\x6E\x65","\x50\x61\x73\x73\x65\x72\x6F\x20\x4F\x6E\x65","\x50\x61\x73\x73\x69\x6F\x6E\x20\x4F\x6E\x65","\x50\x61\x74\x72\x69\x63\x6B\x20\x48\x61\x6E\x64","\x50\x61\x74\x75\x61\x20\x4F\x6E\x65","\x50\x61\x79\x74\x6F\x6E\x65\x20\x4F\x6E\x65","\x50\x65\x72\x61\x6C\x74\x61","\x50\x65\x72\x6D\x61\x6E\x65\x6E\x74\x20\x4D\x61\x72\x6B\x65\x72","\x50\x65\x74\x69\x74\x20\x46\x6F\x72\x6D\x61\x6C\x20\x53\x63\x72\x69\x70\x74","\x50\x65\x74\x72\x6F\x6E\x61","\x50\x68\x69\x6C\x6F\x73\x6F\x70\x68\x65\x72","\x50\x69\x65\x64\x72\x61","\x50\x69\x6E\x79\x6F\x6E\x20\x53\x63\x72\x69\x70\x74","\x50\x69\x72\x61\x74\x61\x20\x4F\x6E\x65","\x50\x6C\x61\x73\x74\x65\x72","\x50\x6C\x61\x79","\x50\x6C\x61\x79\x62\x61\x6C\x6C","\x50\x6C\x61\x79\x66\x61\x69\x72\x20\x44\x69\x73\x70\x6C\x61\x79","\x50\x6C\x61\x79\x66\x61\x69\x72\x20\x44\x69\x73\x70\x6C\x61\x79\x20\x53\x43","\x50\x6F\x64\x6B\x6F\x76\x61","\x50\x6F\x69\x72\x65\x74\x20\x4F\x6E\x65","\x50\x6F\x6C\x6C\x65\x72\x20\x4F\x6E\x65","\x50\x6F\x6C\x79","\x50\x6F\x6D\x70\x69\x65\x72\x65","\x50\x6F\x6E\x74\x61\x6E\x6F\x20\x53\x61\x6E\x73","\x50\x6F\x72\x74\x20\x4C\x6C\x69\x67\x61\x74\x20\x53\x61\x6E\x73","\x50\x6F\x72\x74\x20\x4C\x6C\x69\x67\x61\x74\x20\x53\x6C\x61\x62","\x50\x72\x61\x74\x61","\x50\x72\x65\x61\x68\x76\x69\x68\x65\x61\x72","\x50\x72\x65\x73\x73\x20\x53\x74\x61\x72\x74\x20\x32\x50","\x50\x72\x69\x6E\x63\x65\x73\x73\x20\x53\x6F\x66\x69\x61","\x50\x72\x6F\x63\x69\x6F\x6E\x6F","\x50\x72\x6F\x73\x74\x6F\x20\x4F\x6E\x65","\x50\x75\x72\x69\x74\x61\x6E","\x50\x75\x72\x70\x6C\x65\x20\x50\x75\x72\x73\x65","\x51\x75\x61\x6E\x64\x6F","\x51\x75\x61\x6E\x74\x69\x63\x6F","\x51\x75\x61\x74\x74\x72\x6F\x63\x65\x6E\x74\x6F","\x51\x75\x61\x74\x74\x72\x6F\x63\x65\x6E\x74\x6F\x20\x53\x61\x6E\x73","\x51\x75\x65\x73\x74\x72\x69\x61\x6C","\x51\x75\x69\x63\x6B\x73\x61\x6E\x64","\x51\x75\x69\x6E\x74\x65\x73\x73\x65\x6E\x74\x69\x61\x6C","\x51\x77\x69\x67\x6C\x65\x79","\x52\x61\x63\x69\x6E\x67\x20\x53\x61\x6E\x73\x20\x4F\x6E\x65","\x52\x61\x64\x6C\x65\x79","\x52\x61\x6C\x65\x77\x61\x79","\x52\x61\x6C\x65\x77\x61\x79\x20\x44\x6F\x74\x73","\x52\x61\x6D\x62\x6C\x61","\x52\x61\x6D\x6D\x65\x74\x74\x6F\x20\x4F\x6E\x65","\x52\x61\x6E\x63\x68\x65\x72\x73","\x52\x61\x6E\x63\x68\x6F","\x52\x61\x74\x69\x6F\x6E\x61\x6C\x65","\x52\x65\x64\x72\x65\x73\x73\x65\x64","\x52\x65\x65\x6E\x69\x65\x20\x42\x65\x61\x6E\x69\x65","\x52\x65\x76\x61\x6C\x69\x61","\x52\x69\x62\x65\x79\x65","\x52\x69\x62\x65\x79\x65\x20\x4D\x61\x72\x72\x6F\x77","\x52\x69\x67\x68\x74\x65\x6F\x75\x73","\x52\x69\x73\x71\x75\x65","\x52\x6F\x63\x68\x65\x73\x74\x65\x72","\x52\x6F\x63\x6B\x20\x53\x61\x6C\x74","\x52\x6F\x6B\x6B\x69\x74\x74","\x52\x6F\x6D\x61\x6E\x65\x73\x63\x6F","\x52\x6F\x70\x61\x20\x53\x61\x6E\x73","\x52\x6F\x73\x61\x72\x69\x6F","\x52\x6F\x73\x61\x72\x69\x76\x6F","\x52\x6F\x75\x67\x65\x20\x53\x63\x72\x69\x70\x74","\x52\x75\x64\x61","\x52\x75\x66\x69\x6E\x61","\x52\x75\x67\x65\x20\x42\x6F\x6F\x67\x69\x65","\x52\x75\x6C\x75\x6B\x6F","\x52\x75\x6D\x20\x52\x61\x69\x73\x69\x6E","\x52\x75\x73\x6C\x61\x6E\x20\x44\x69\x73\x70\x6C\x61\x79","\x52\x75\x73\x73\x6F\x20\x4F\x6E\x65","\x52\x75\x74\x68\x69\x65","\x52\x79\x65","\x53\x61\x63\x72\x61\x6D\x65\x6E\x74\x6F","\x53\x61\x69\x6C","\x53\x61\x6C\x73\x61","\x53\x61\x6E\x63\x68\x65\x7A","\x53\x61\x6E\x63\x72\x65\x65\x6B","\x53\x61\x6E\x73\x69\x74\x61\x20\x4F\x6E\x65","\x53\x61\x72\x69\x6E\x61","\x53\x61\x74\x69\x73\x66\x79","\x53\x63\x61\x64\x61","\x53\x63\x68\x6F\x6F\x6C\x62\x65\x6C\x6C","\x53\x65\x61\x77\x65\x65\x64\x20\x53\x63\x72\x69\x70\x74","\x53\x65\x76\x69\x6C\x6C\x61\x6E\x61","\x53\x65\x79\x6D\x6F\x75\x72\x20\x4F\x6E\x65","\x53\x68\x61\x64\x6F\x77\x73\x20\x49\x6E\x74\x6F\x20\x4C\x69\x67\x68\x74","\x53\x68\x61\x64\x6F\x77\x73\x20\x49\x6E\x74\x6F\x20\x4C\x69\x67\x68\x74\x20\x54\x77\x6F","\x53\x68\x61\x6E\x74\x69","\x53\x68\x61\x72\x65","\x53\x68\x61\x72\x65\x20\x54\x65\x63\x68","\x53\x68\x61\x72\x65\x20\x54\x65\x63\x68\x20\x4D\x6F\x6E\x6F","\x53\x68\x6F\x6A\x75\x6D\x61\x72\x75","\x53\x68\x6F\x72\x74\x20\x53\x74\x61\x63\x6B","\x53\x69\x65\x6D\x72\x65\x61\x70","\x53\x69\x67\x6D\x61\x72\x20\x4F\x6E\x65","\x53\x69\x67\x6E\x69\x6B\x61","\x53\x69\x67\x6E\x69\x6B\x61\x20\x4E\x65\x67\x61\x74\x69\x76\x65","\x53\x69\x6D\x6F\x6E\x65\x74\x74\x61","\x53\x69\x72\x69\x6E\x20\x53\x74\x65\x6E\x63\x69\x6C","\x53\x69\x78\x20\x43\x61\x70\x73","\x53\x6B\x72\x61\x6E\x6A\x69","\x53\x6C\x61\x63\x6B\x65\x79","\x53\x6D\x6F\x6B\x75\x6D","\x53\x6D\x79\x74\x68\x65","\x53\x6E\x69\x67\x6C\x65\x74","\x53\x6E\x69\x70\x70\x65\x74","\x53\x6E\x6F\x77\x62\x75\x72\x73\x74\x20\x4F\x6E\x65","\x53\x6F\x66\x61\x64\x69\x20\x4F\x6E\x65","\x53\x6F\x66\x69\x61","\x53\x6F\x6E\x73\x69\x65\x20\x4F\x6E\x65","\x53\x6F\x72\x74\x73\x20\x4D\x69\x6C\x6C\x20\x47\x6F\x75\x64\x79","\x53\x6F\x75\x72\x63\x65\x20\x43\x6F\x64\x65\x20\x50\x72\x6F","\x53\x6F\x75\x72\x63\x65\x20\x53\x61\x6E\x73\x20\x50\x72\x6F","\x53\x70\x65\x63\x69\x61\x6C\x20\x45\x6C\x69\x74\x65","\x53\x70\x69\x63\x79\x20\x52\x69\x63\x65","\x53\x70\x69\x6E\x6E\x61\x6B\x65\x72","\x53\x70\x69\x72\x61\x78","\x53\x71\x75\x61\x64\x61\x20\x4F\x6E\x65","\x53\x74\x61\x6C\x65\x6D\x61\x74\x65","\x53\x74\x61\x6C\x69\x6E\x69\x73\x74\x20\x4F\x6E\x65","\x53\x74\x61\x72\x64\x6F\x73\x20\x53\x74\x65\x6E\x63\x69\x6C","\x53\x74\x69\x6E\x74\x20\x55\x6C\x74\x72\x61\x20\x43\x6F\x6E\x64\x65\x6E\x73\x65\x64","\x53\x74\x69\x6E\x74\x20\x55\x6C\x74\x72\x61\x20\x45\x78\x70\x61\x6E\x64\x65\x64","\x53\x74\x6F\x6B\x65","\x53\x74\x72\x61\x69\x74","\x53\x75\x65\x20\x45\x6C\x6C\x65\x6E\x20\x46\x72\x61\x6E\x63\x69\x73\x63\x6F","\x53\x75\x6E\x73\x68\x69\x6E\x65\x79","\x53\x75\x70\x65\x72\x6D\x65\x72\x63\x61\x64\x6F\x20\x4F\x6E\x65","\x53\x75\x77\x61\x6E\x6E\x61\x70\x68\x75\x6D","\x53\x77\x61\x6E\x6B\x79\x20\x61\x6E\x64\x20\x4D\x6F\x6F\x20\x4D\x6F\x6F","\x53\x79\x6E\x63\x6F\x70\x61\x74\x65","\x54\x61\x6E\x67\x65\x72\x69\x6E\x65","\x54\x61\x70\x72\x6F\x6D","\x54\x65\x6C\x65\x78","\x54\x65\x6E\x6F\x72\x20\x53\x61\x6E\x73","\x54\x65\x78\x74\x20\x4D\x65\x20\x4F\x6E\x65","\x54\x68\x65\x20\x47\x69\x72\x6C\x20\x4E\x65\x78\x74\x20\x44\x6F\x6F\x72","\x54\x69\x65\x6E\x6E\x65","\x54\x69\x6E\x6F\x73","\x54\x69\x74\x61\x6E\x20\x4F\x6E\x65","\x54\x69\x74\x69\x6C\x6C\x69\x75\x6D\x20\x57\x65\x62","\x54\x72\x61\x64\x65\x20\x57\x69\x6E\x64\x73","\x54\x72\x6F\x63\x63\x68\x69","\x54\x72\x6F\x63\x68\x75\x74","\x54\x72\x79\x6B\x6B\x65\x72","\x54\x75\x6C\x70\x65\x6E\x20\x4F\x6E\x65","\x55\x62\x75\x6E\x74\x75","\x55\x62\x75\x6E\x74\x75\x20\x43\x6F\x6E\x64\x65\x6E\x73\x65\x64","\x55\x62\x75\x6E\x74\x75\x20\x4D\x6F\x6E\x6F","\x55\x6C\x74\x72\x61","\x55\x6E\x63\x69\x61\x6C\x20\x41\x6E\x74\x69\x71\x75\x61","\x55\x6E\x64\x65\x72\x64\x6F\x67","\x55\x6E\x69\x63\x61\x20\x4F\x6E\x65","\x55\x6E\x69\x66\x72\x61\x6B\x74\x75\x72\x43\x6F\x6F\x6B","\x55\x6E\x69\x66\x72\x61\x6B\x74\x75\x72\x4D\x61\x67\x75\x6E\x74\x69\x61","\x55\x6E\x6B\x65\x6D\x70\x74","\x55\x6E\x6C\x6F\x63\x6B","\x55\x6E\x6E\x61","\x56\x54\x33\x32\x33","\x56\x61\x6D\x70\x69\x72\x6F\x20\x4F\x6E\x65","\x56\x61\x72\x65\x6C\x61","\x56\x61\x72\x65\x6C\x61\x20\x52\x6F\x75\x6E\x64","\x56\x61\x73\x74\x20\x53\x68\x61\x64\x6F\x77","\x56\x69\x62\x75\x72","\x56\x69\x64\x61\x6C\x6F\x6B\x61","\x56\x69\x67\x61","\x56\x6F\x63\x65\x73","\x56\x6F\x6C\x6B\x68\x6F\x76","\x56\x6F\x6C\x6C\x6B\x6F\x72\x6E","\x56\x6F\x6C\x74\x61\x69\x72\x65","\x57\x61\x69\x74\x69\x6E\x67\x20\x66\x6F\x72\x20\x74\x68\x65\x20\x53\x75\x6E\x72\x69\x73\x65","\x57\x61\x6C\x6C\x70\x6F\x65\x74","\x57\x61\x6C\x74\x65\x72\x20\x54\x75\x72\x6E\x63\x6F\x61\x74","\x57\x61\x72\x6E\x65\x73","\x57\x65\x6C\x6C\x66\x6C\x65\x65\x74","\x57\x69\x72\x65\x20\x4F\x6E\x65","\x59\x61\x6E\x6F\x6E\x65\x20\x4B\x61\x66\x66\x65\x65\x73\x61\x74\x7A","\x59\x65\x6C\x6C\x6F\x77\x74\x61\x69\x6C","\x59\x65\x73\x65\x76\x61\x20\x4F\x6E\x65","\x59\x65\x73\x74\x65\x72\x79\x65\x61\x72","\x5A\x65\x79\x61\x64\x61","\x3A","\x41\x4D","\x50\x4D","\x6A\x51\x75\x65\x72\x79","\x75\x73\x65\x20\x73\x74\x72\x69\x63\x74","\x5B\x64\x61\x74\x61\x2D\x74\x6F\x67\x67\x6C\x65\x3D\x62\x66\x68\x2D\x63\x6F\x6C\x6F\x72\x70\x69\x63\x6B\x65\x72\x5D","\x6F\x70\x74\x69\x6F\x6E\x73","\x64\x65\x66\x61\x75\x6C\x74\x73","\x62\x66\x68\x63\x6F\x6C\x6F\x72\x70\x69\x63\x6B\x65\x72","\x66\x6E","\x65\x78\x74\x65\x6E\x64","\x24\x65\x6C\x65\x6D\x65\x6E\x74","\x69\x6E\x69\x74\x50\x6F\x70\x6F\x76\x65\x72","\x70\x72\x6F\x74\x6F\x74\x79\x70\x65","\x63\x61\x6E\x76\x61\x73","\x66\x69\x6E\x64","\x32\x64","\x67\x65\x74\x43\x6F\x6E\x74\x65\x78\x74","\x77\x69\x64\x74\x68","\x63\x72\x65\x61\x74\x65\x4C\x69\x6E\x65\x61\x72\x47\x72\x61\x64\x69\x65\x6E\x74","\x72\x67\x62\x28\x32\x35\x35\x2C\x20\x32\x35\x35\x2C\x20\x32\x35\x35\x29","\x61\x64\x64\x43\x6F\x6C\x6F\x72\x53\x74\x6F\x70","\x72\x67\x62\x28\x32\x35\x35\x2C\x20\x20\x20\x30\x2C\x20\x20\x20\x30\x29","\x72\x67\x62\x28\x32\x35\x35\x2C\x20\x20\x20\x30\x2C\x20\x32\x35\x35\x29","\x72\x67\x62\x28\x30\x2C\x20\x20\x20\x20\x20\x30\x2C\x20\x32\x35\x35\x29","\x72\x67\x62\x28\x30\x2C\x20\x20\x20\x32\x35\x35\x2C\x20\x32\x35\x35\x29","\x72\x67\x62\x28\x30\x2C\x20\x20\x20\x32\x35\x35\x2C\x20\x20\x20\x30\x29","\x72\x67\x62\x28\x32\x35\x35\x2C\x20\x32\x35\x35\x2C\x20\x20\x20\x30\x29","\x66\x69\x6C\x6C\x53\x74\x79\x6C\x65","\x68\x65\x69\x67\x68\x74","\x66\x69\x6C\x6C\x52\x65\x63\x74","\x72\x67\x62\x61\x28\x32\x35\x35\x2C\x20\x32\x35\x35\x2C\x20\x32\x35\x35\x2C\x20\x31\x29","\x72\x67\x62\x61\x28\x32\x35\x35\x2C\x20\x32\x35\x35\x2C\x20\x32\x35\x35\x2C\x20\x30\x29","\x72\x67\x62\x61\x28\x30\x2C\x20\x20\x20\x20\x20\x30\x2C\x20\x20\x20\x30\x2C\x20\x30\x29","\x72\x67\x62\x61\x28\x30\x2C\x20\x20\x20\x20\x20\x30\x2C\x20\x20\x20\x30\x2C\x20\x31\x29","","\x61\x6C\x69\x67\x6E","\x72\x69\x67\x68\x74","\x3C\x73\x70\x61\x6E\x20\x63\x6C\x61\x73\x73\x3D\x22\x69\x6E\x70\x75\x74\x2D\x67\x72\x6F\x75\x70\x2D\x61\x64\x64\x6F\x6E\x22\x3E\x3C\x73\x70\x61\x6E\x20\x63\x6C\x61\x73\x73\x3D\x22\x62\x66\x68\x2D\x63\x6F\x6C\x6F\x72\x70\x69\x63\x6B\x65\x72\x2D\x69\x63\x6F\x6E\x22\x3E\x3C\x2F\x73\x70\x61\x6E\x3E\x3C\x2F\x73\x70\x61\x6E\x3E","\x3C\x64\x69\x76\x20\x63\x6C\x61\x73\x73\x3D\x22\x69\x6E\x70\x75\x74\x2D\x67\x72\x6F\x75\x70\x20\x62\x66\x68\x2D\x63\x6F\x6C\x6F\x72\x70\x69\x63\x6B\x65\x72\x2D\x74\x6F\x67\x67\x6C\x65\x22\x20\x64\x61\x74\x61\x2D\x74\x6F\x67\x67\x6C\x65\x3D\x22\x62\x66\x68\x2D\x63\x6F\x6C\x6F\x72\x70\x69\x63\x6B\x65\x72\x22\x3E","\x3C\x69\x6E\x70\x75\x74\x20\x74\x79\x70\x65\x3D\x22\x74\x65\x78\x74\x22\x20\x6E\x61\x6D\x65\x3D\x22","\x6E\x61\x6D\x65","\x22\x20\x63\x6C\x61\x73\x73\x3D\x22","\x69\x6E\x70\x75\x74","\x22\x20\x70\x6C\x61\x63\x65\x68\x6F\x6C\x64\x65\x72\x3D\x22","\x70\x6C\x61\x63\x65\x68\x6F\x6C\x64\x65\x72","\x22\x20\x72\x65\x61\x64\x6F\x6E\x6C\x79\x3E","\x3C\x2F\x64\x69\x76\x3E","\x3C\x64\x69\x76\x20\x63\x6C\x61\x73\x73\x3D\x22\x62\x66\x68\x2D\x63\x6F\x6C\x6F\x72\x70\x69\x63\x6B\x65\x72\x2D\x70\x6F\x70\x6F\x76\x65\x72\x22\x3E","\x3C\x63\x61\x6E\x76\x61\x73\x20\x63\x6C\x61\x73\x73\x3D\x22\x62\x66\x68\x2D\x63\x6F\x6C\x6F\x72\x70\x69\x63\x6B\x65\x72\x2D\x70\x61\x6C\x65\x74\x74\x65\x22\x20\x77\x69\x64\x74\x68\x3D\x22\x33\x38\x34\x22\x20\x68\x65\x69\x67\x68\x74\x3D\x22\x32\x35\x36\x22\x3E\x3C\x2F\x63\x61\x6E\x76\x61\x73\x3E","\x68\x74\x6D\x6C","\x63\x6C\x69\x63\x6B\x2E\x62\x66\x68\x63\x6F\x6C\x6F\x72\x70\x69\x63\x6B\x65\x72\x2E\x64\x61\x74\x61\x2D\x61\x70\x69\x20\x74\x6F\x75\x63\x68\x73\x74\x61\x72\x74\x2E\x62\x66\x68\x63\x6F\x6C\x6F\x72\x70\x69\x63\x6B\x65\x72\x2E\x64\x61\x74\x61\x2D\x61\x70\x69","\x2E\x62\x66\x68\x2D\x63\x6F\x6C\x6F\x72\x70\x69\x63\x6B\x65\x72\x2D\x70\x6F\x70\x6F\x76\x65\x72","\x6F\x6E","\x6D\x6F\x75\x73\x65\x64\x6F\x77\x6E\x2E\x62\x66\x68\x63\x6F\x6C\x6F\x72\x70\x69\x63\x6B\x65\x72\x2E\x64\x61\x74\x61\x2D\x61\x70\x69","\x6D\x6F\x75\x73\x65\x44\x6F\x77\x6E","\x74\x6F\x67\x67\x6C\x65","\x69\x6E\x69\x74\x50\x61\x6C\x65\x74\x74\x65","\x63\x6F\x6C\x6F\x72","\x76\x61\x6C","\x6C\x65\x66\x74","\x6F\x66\x66\x73\x65\x74","\x74\x6F\x70","\x72\x6F\x75\x6E\x64","\x67\x65\x74\x49\x6D\x61\x67\x65\x44\x61\x74\x61","\x64\x61\x74\x61","\x63\x68\x61\x6E\x67\x65\x2E\x62\x66\x68\x63\x6F\x6C\x6F\x72\x70\x69\x63\x6B\x65\x72","\x74\x72\x69\x67\x67\x65\x72","\x6D\x6F\x75\x73\x65\x75\x70\x2E\x62\x66\x68\x63\x6F\x6C\x6F\x72\x70\x69\x63\x6B\x65\x72\x2E\x64\x61\x74\x61\x2D\x61\x70\x69","\x6D\x6F\x75\x73\x65\x55\x70","\x6F\x6E\x65","\x6D\x6F\x75\x73\x65\x6D\x6F\x76\x65\x2E\x62\x66\x68\x63\x6F\x6C\x6F\x72\x70\x69\x63\x6B\x65\x72\x2E\x64\x61\x74\x61\x2D\x61\x70\x69","\x6D\x6F\x75\x73\x65\x4D\x6F\x76\x65","\x63\x6F\x6C\x6F\x72\x70\x69\x63\x6B\x65\x72","\x70\x61\x67\x65\x58","\x70\x61\x67\x65\x59","\x75\x70\x64\x61\x74\x65\x56\x61\x6C","\x6F\x66\x66","\x63\x6C\x6F\x73\x65","\x2E\x64\x69\x73\x61\x62\x6C\x65\x64","\x69\x73","\x64\x69\x73\x61\x62\x6C\x65\x64","\x61\x74\x74\x72","\x6F\x70\x65\x6E","\x68\x61\x73\x43\x6C\x61\x73\x73","\x73\x68\x6F\x77\x2E\x62\x66\x68\x63\x6F\x6C\x6F\x72\x70\x69\x63\x6B\x65\x72","\x69\x73\x44\x65\x66\x61\x75\x6C\x74\x50\x72\x65\x76\x65\x6E\x74\x65\x64","\x73\x68\x6F\x77\x6E\x2E\x62\x66\x68\x63\x6F\x6C\x6F\x72\x70\x69\x63\x6B\x65\x72","\x74\x6F\x67\x67\x6C\x65\x43\x6C\x61\x73\x73","\x66\x6F\x63\x75\x73","\x6C\x65\x6E\x67\x74\x68","\x30","\x23","\x68\x69\x64\x65\x2E\x62\x66\x68\x63\x6F\x6C\x6F\x72\x70\x69\x63\x6B\x65\x72","\x68\x69\x64\x64\x65\x6E\x2E\x62\x66\x68\x63\x6F\x6C\x6F\x72\x70\x69\x63\x6B\x65\x72","\x72\x65\x6D\x6F\x76\x65\x43\x6C\x61\x73\x73","\x65\x61\x63\x68","\x2E\x62\x66\x68\x2D\x63\x6F\x6C\x6F\x72\x70\x69\x63\x6B\x65\x72","\x63\x6C\x6F\x73\x65\x73\x74","\x6F\x62\x6A\x65\x63\x74","\x74\x79\x70\x65","\x73\x74\x72\x69\x6E\x67","\x63\x61\x6C\x6C","\x43\x6F\x6E\x73\x74\x72\x75\x63\x74\x6F\x72","\x66\x6F\x72\x6D\x2D\x63\x6F\x6E\x74\x72\x6F\x6C","\x23\x30\x30\x30\x30\x30\x30","\x6E\x6F\x43\x6F\x6E\x66\x6C\x69\x63\x74","\x64\x69\x76","\x76\x61\x6C\x48\x6F\x6F\x6B\x73","\x62\x66\x68\x2D\x63\x6F\x6C\x6F\x72\x70\x69\x63\x6B\x65\x72","\x69\x6E\x70\x75\x74\x5B\x74\x79\x70\x65\x3D\x22\x74\x65\x78\x74\x22\x5D","\x67\x65\x74","\x62\x61\x63\x6B\x67\x72\x6F\x75\x6E\x64\x2D\x63\x6F\x6C\x6F\x72","\x63\x73\x73","\x2E\x62\x66\x68\x2D\x63\x6F\x6C\x6F\x72\x70\x69\x63\x6B\x65\x72\x2D\x69\x63\x6F\x6E","\x73\x65\x74","\x64\x69\x76\x2E\x62\x66\x68\x2D\x63\x6F\x6C\x6F\x72\x70\x69\x63\x6B\x65\x72","\x72\x65\x61\x64\x79","\x63\x6C\x69\x63\x6B\x2E\x62\x66\x68\x63\x6F\x6C\x6F\x72\x70\x69\x63\x6B\x65\x72\x2E\x64\x61\x74\x61\x2D\x61\x70\x69","\x5B\x64\x61\x74\x61\x2D\x74\x6F\x67\x67\x6C\x65\x3D\x62\x66\x68\x2D\x64\x61\x74\x65\x70\x69\x63\x6B\x65\x72\x5D","\x62\x66\x68\x64\x61\x74\x65\x70\x69\x63\x6B\x65\x72","\x69\x6E\x69\x74\x43\x61\x6C\x65\x6E\x64\x61\x72","\x64\x61\x74\x65","\x66\x6F\x72\x6D\x61\x74","\x74\x6F\x64\x61\x79","\x67\x65\x74\x4D\x6F\x6E\x74\x68","\x67\x65\x74\x46\x75\x6C\x6C\x59\x65\x61\x72","\x67\x65\x74\x44\x61\x74\x65","\x6D\x6F\x6E\x74\x68","\x79\x65\x61\x72","\x6D","\x79","\x6C\x69\x6D\x69\x74","\x64\x61\x79","\x64","\x69\x63\x6F\x6E","\x3C\x73\x70\x61\x6E\x20\x63\x6C\x61\x73\x73\x3D\x22\x69\x6E\x70\x75\x74\x2D\x67\x72\x6F\x75\x70\x2D\x61\x64\x64\x6F\x6E\x22\x3E\x3C\x69\x20\x63\x6C\x61\x73\x73\x3D\x22","\x22\x3E\x3C\x2F\x69\x3E\x3C\x2F\x73\x70\x61\x6E\x3E","\x69\x6E\x70\x75\x74\x2D\x67\x72\x6F\x75\x70","\x3C\x64\x69\x76\x20\x63\x6C\x61\x73\x73\x3D\x22","\x20\x62\x66\x68\x2D\x64\x61\x74\x65\x70\x69\x63\x6B\x65\x72\x2D\x74\x6F\x67\x67\x6C\x65\x22\x20\x64\x61\x74\x61\x2D\x74\x6F\x67\x67\x6C\x65\x3D\x22\x62\x66\x68\x2D\x64\x61\x74\x65\x70\x69\x63\x6B\x65\x72\x22\x3E","\x3C\x64\x69\x76\x20\x63\x6C\x61\x73\x73\x3D\x22\x62\x66\x68\x2D\x64\x61\x74\x65\x70\x69\x63\x6B\x65\x72\x2D\x63\x61\x6C\x65\x6E\x64\x61\x72\x22\x3E","\x3C\x74\x61\x62\x6C\x65\x20\x63\x6C\x61\x73\x73\x3D\x22\x63\x61\x6C\x65\x6E\x64\x61\x72\x20\x74\x61\x62\x6C\x65\x20\x74\x61\x62\x6C\x65\x2D\x62\x6F\x72\x64\x65\x72\x65\x64\x22\x3E","\x3C\x74\x68\x65\x61\x64\x3E","\x3C\x74\x72\x20\x63\x6C\x61\x73\x73\x3D\x22\x6D\x6F\x6E\x74\x68\x73\x2D\x68\x65\x61\x64\x65\x72\x22\x3E","\x3C\x74\x68\x20\x63\x6C\x61\x73\x73\x3D\x22\x6D\x6F\x6E\x74\x68\x22\x20\x63\x6F\x6C\x73\x70\x61\x6E\x3D\x22\x34\x22\x3E","\x3C\x61\x20\x63\x6C\x61\x73\x73\x3D\x22\x70\x72\x65\x76\x69\x6F\x75\x73\x22\x20\x68\x72\x65\x66\x3D\x22\x23\x22\x3E\x3C\x69\x20\x63\x6C\x61\x73\x73\x3D\x22\x67\x6C\x79\x70\x68\x69\x63\x6F\x6E\x20\x67\x6C\x79\x70\x68\x69\x63\x6F\x6E\x2D\x63\x68\x65\x76\x72\x6F\x6E\x2D\x6C\x65\x66\x74\x22\x3E\x3C\x2F\x69\x3E\x3C\x2F\x61\x3E","\x3C\x73\x70\x61\x6E\x3E\x3C\x2F\x73\x70\x61\x6E\x3E","\x3C\x61\x20\x63\x6C\x61\x73\x73\x3D\x22\x6E\x65\x78\x74\x22\x20\x68\x72\x65\x66\x3D\x22\x23\x22\x3E\x3C\x69\x20\x63\x6C\x61\x73\x73\x3D\x22\x67\x6C\x79\x70\x68\x69\x63\x6F\x6E\x20\x67\x6C\x79\x70\x68\x69\x63\x6F\x6E\x2D\x63\x68\x65\x76\x72\x6F\x6E\x2D\x72\x69\x67\x68\x74\x22\x3E\x3C\x2F\x69\x3E\x3C\x2F\x61\x3E","\x3C\x2F\x74\x68\x3E","\x3C\x74\x68\x20\x63\x6C\x61\x73\x73\x3D\x22\x79\x65\x61\x72\x22\x20\x63\x6F\x6C\x73\x70\x61\x6E\x3D\x22\x33\x22\x3E","\x3C\x2F\x74\x72\x3E","\x3C\x74\x72\x20\x63\x6C\x61\x73\x73\x3D\x22\x64\x61\x79\x73\x2D\x68\x65\x61\x64\x65\x72\x22\x3E","\x3C\x2F\x74\x68\x65\x61\x64\x3E","\x3C\x74\x62\x6F\x64\x79\x3E","\x3C\x2F\x74\x62\x6F\x64\x79\x3E","\x3C\x2F\x74\x61\x62\x6C\x65\x3E","\x63\x6C\x69\x63\x6B\x2E\x62\x66\x68\x64\x61\x74\x65\x70\x69\x63\x6B\x65\x72\x2E\x64\x61\x74\x61\x2D\x61\x70\x69\x20\x74\x6F\x75\x63\x68\x73\x74\x61\x72\x74\x2E\x62\x66\x68\x64\x61\x74\x65\x70\x69\x63\x6B\x65\x72\x2E\x64\x61\x74\x61\x2D\x61\x70\x69","\x2E\x62\x66\x68\x2D\x64\x61\x74\x65\x70\x69\x63\x6B\x65\x72\x2D\x63\x61\x6C\x65\x6E\x64\x61\x72\x20\x3E\x20\x74\x61\x62\x6C\x65\x2E\x63\x61\x6C\x65\x6E\x64\x61\x72","\x2E\x62\x66\x68\x2D\x64\x61\x74\x65\x70\x69\x63\x6B\x65\x72\x2D\x63\x61\x6C\x65\x6E\x64\x61\x72\x20\x3E\x20\x74\x61\x62\x6C\x65\x2E\x63\x61\x6C\x65\x6E\x64\x61\x72\x20\x74\x64\x3A\x6E\x6F\x74\x28\x2E\x6F\x66\x66\x29","\x73\x65\x6C\x65\x63\x74","\x2E\x62\x66\x68\x2D\x64\x61\x74\x65\x70\x69\x63\x6B\x65\x72\x2D\x63\x61\x6C\x65\x6E\x64\x61\x72\x20\x3E\x20\x74\x61\x62\x6C\x65\x2E\x63\x61\x6C\x65\x6E\x64\x61\x72\x20\x2E\x79\x65\x61\x72\x20\x3E\x20\x2E\x6E\x65\x78\x74","\x6E\x65\x78\x74\x59\x65\x61\x72","\x2E\x62\x66\x68\x2D\x64\x61\x74\x65\x70\x69\x63\x6B\x65\x72\x2D\x63\x61\x6C\x65\x6E\x64\x61\x72\x20\x3E\x20\x74\x61\x62\x6C\x65\x2E\x63\x61\x6C\x65\x6E\x64\x61\x72\x20\x2E\x79\x65\x61\x72\x20\x3E\x20\x2E\x70\x72\x65\x76\x69\x6F\x75\x73","\x70\x72\x65\x76\x69\x6F\x75\x73\x59\x65\x61\x72","\x2E\x62\x66\x68\x2D\x64\x61\x74\x65\x70\x69\x63\x6B\x65\x72\x2D\x63\x61\x6C\x65\x6E\x64\x61\x72\x20\x3E\x20\x74\x61\x62\x6C\x65\x2E\x63\x61\x6C\x65\x6E\x64\x61\x72\x20\x2E\x6D\x6F\x6E\x74\x68\x20\x3E\x20\x2E\x6E\x65\x78\x74","\x6E\x65\x78\x74\x4D\x6F\x6E\x74\x68","\x2E\x62\x66\x68\x2D\x64\x61\x74\x65\x70\x69\x63\x6B\x65\x72\x2D\x63\x61\x6C\x65\x6E\x64\x61\x72\x20\x3E\x20\x74\x61\x62\x6C\x65\x2E\x63\x61\x6C\x65\x6E\x64\x61\x72\x20\x2E\x6D\x6F\x6E\x74\x68\x20\x3E\x20\x2E\x70\x72\x65\x76\x69\x6F\x75\x73","\x70\x72\x65\x76\x69\x6F\x75\x73\x4D\x6F\x6E\x74\x68","\x73\x65\x74\x44\x61\x74\x65","\x6D\x69\x6E","\x6C\x6F\x77\x65\x72","\x73\x65\x74\x44\x61\x74\x65\x4C\x69\x6D\x69\x74","\x6D\x61\x78","\x68\x69\x67\x68\x65\x72","\x75\x70\x64\x61\x74\x65\x43\x61\x6C\x65\x6E\x64\x61\x72","\x74\x65\x78\x74","\x74\x61\x62\x6C\x65\x20\x3E\x20\x74\x68\x65\x61\x64\x20\x3E\x20\x74\x72\x20\x3E\x20\x74\x68\x2E\x6D\x6F\x6E\x74\x68\x20\x3E\x20\x73\x70\x61\x6E","\x74\x61\x62\x6C\x65\x20\x3E\x20\x74\x68\x65\x61\x64\x20\x3E\x20\x74\x72\x20\x3E\x20\x74\x68\x2E\x79\x65\x61\x72\x20\x3E\x20\x73\x70\x61\x6E","\x74\x61\x62\x6C\x65\x20\x3E\x20\x74\x68\x65\x61\x64\x20\x3E\x20\x74\x72\x2E\x64\x61\x79\x73\x2D\x68\x65\x61\x64\x65\x72","\x3C\x74\x68\x3E","\x61\x70\x70\x65\x6E\x64","\x6C\x6F\x77\x65\x72\x6C\x69\x6D\x69\x74","\x6C\x6F\x77\x65\x72\x64\x61\x79","\x6C\x6F\x77\x65\x72\x6D\x6F\x6E\x74\x68","\x6C\x6F\x77\x65\x72\x79\x65\x61\x72","\x68\x69\x67\x68\x65\x72\x6C\x69\x6D\x69\x74","\x68\x69\x67\x68\x65\x72\x64\x61\x79","\x68\x69\x67\x68\x65\x72\x6D\x6F\x6E\x74\x68","\x68\x69\x67\x68\x65\x72\x79\x65\x61\x72","\x74\x61\x62\x6C\x65\x20\x3E\x20\x74\x62\x6F\x64\x79","\x3C\x74\x64\x20\x63\x6C\x61\x73\x73\x3D\x22\x6F\x66\x66\x22\x3E","\x3C\x2F\x74\x64\x3E","\x63\x68\x65\x63\x6B\x4D\x69\x6E\x44\x61\x74\x65","\x3C\x74\x64\x20\x64\x61\x74\x61\x2D\x64\x61\x79\x3D\x22","\x22\x20\x63\x6C\x61\x73\x73\x3D\x22\x6F\x66\x66\x22\x3E","\x63\x68\x65\x63\x6B\x4D\x61\x78\x44\x61\x74\x65","\x63\x68\x65\x63\x6B\x54\x6F\x64\x61\x79","\x22\x20\x63\x6C\x61\x73\x73\x3D\x22\x74\x6F\x64\x61\x79\x22\x3E","\x22\x3E","\x3C\x74\x72\x3E","\x2E\x62\x66\x68\x2D\x64\x61\x74\x65\x70\x69\x63\x6B\x65\x72\x2D\x63\x61\x6C\x65\x6E\x64\x61\x72","\x75\x70\x64\x61\x74\x65\x43\x61\x6C\x65\x6E\x64\x61\x72\x48\x65\x61\x64\x65\x72","\x75\x70\x64\x61\x74\x65\x43\x61\x6C\x65\x6E\x64\x61\x72\x44\x61\x79\x73","\x70\x72\x65\x76\x65\x6E\x74\x44\x65\x66\x61\x75\x6C\x74","\x73\x74\x6F\x70\x50\x72\x6F\x70\x61\x67\x61\x74\x69\x6F\x6E","\x63\x68\x61\x6E\x67\x65\x2E\x62\x66\x68\x64\x61\x74\x65\x70\x69\x63\x6B\x65\x72","\x73\x68\x6F\x77\x2E\x62\x66\x68\x64\x61\x74\x65\x70\x69\x63\x6B\x65\x72","\x73\x68\x6F\x77\x6E\x2E\x62\x66\x68\x64\x61\x74\x65\x70\x69\x63\x6B\x65\x72","\x67\x65\x74\x44\x61\x79","\x72\x65\x70\x6C\x61\x63\x65","\x69\x6E\x64\x65\x78\x4F\x66","\x70\x6F\x73\x69\x74\x69\x6F\x6E","\x73\x6F\x72\x74","\x6D\x61\x74\x63\x68","\x68\x61\x73\x4F\x77\x6E\x50\x72\x6F\x70\x65\x72\x74\x79","\x70\x61\x72\x74","\x68\x69\x64\x65\x2E\x62\x66\x68\x64\x61\x74\x65\x70\x69\x63\x6B\x65\x72","\x68\x69\x64\x64\x65\x6E\x2E\x62\x66\x68\x64\x61\x74\x65\x70\x69\x63\x6B\x65\x72","\x2E\x62\x66\x68\x2D\x64\x61\x74\x65\x70\x69\x63\x6B\x65\x72","\x67\x6C\x79\x70\x68\x69\x63\x6F\x6E\x20\x67\x6C\x79\x70\x68\x69\x63\x6F\x6E\x2D\x63\x61\x6C\x65\x6E\x64\x61\x72","\x6D\x2F\x64\x2F\x79","\x62\x66\x68\x2D\x64\x61\x74\x65\x70\x69\x63\x6B\x65\x72","\x64\x69\x76\x2E\x62\x66\x68\x2D\x64\x61\x74\x65\x70\x69\x63\x6B\x65\x72","\x63\x6C\x69\x63\x6B\x2E\x62\x66\x68\x64\x61\x74\x65\x70\x69\x63\x6B\x65\x72\x2E\x64\x61\x74\x61\x2D\x61\x70\x69","\x62\x66\x68\x66\x6F\x6E\x74\x73","\x61\x64\x64\x46\x6F\x6E\x74\x73","\x62\x66\x68\x2D\x73\x65\x6C\x65\x63\x74\x62\x6F\x78","\x61\x64\x64\x42\x6F\x6F\x74\x73\x74\x72\x61\x70\x46\x6F\x6E\x74\x73","\x61\x76\x61\x69\x6C\x61\x62\x6C\x65","\x2C","\x73\x70\x6C\x69\x74","\x69\x6E\x41\x72\x72\x61\x79","\x66\x6F\x6E\x74","\x67\x65\x74\x46\x6F\x6E\x74\x73","\x62\x6C\x61\x6E\x6B","\x3C\x6F\x70\x74\x69\x6F\x6E\x20\x76\x61\x6C\x75\x65\x3D\x22\x22\x3E\x3C\x2F\x6F\x70\x74\x69\x6F\x6E\x3E","\x3C\x6F\x70\x74\x69\x6F\x6E\x20\x76\x61\x6C\x75\x65\x3D\x22","\x3C\x2F\x6F\x70\x74\x69\x6F\x6E\x3E","\x69\x6E\x70\x75\x74\x5B\x74\x79\x70\x65\x3D\x22\x68\x69\x64\x64\x65\x6E\x22\x5D","\x2E\x62\x66\x68\x2D\x73\x65\x6C\x65\x63\x74\x62\x6F\x78\x2D\x6F\x70\x74\x69\x6F\x6E","\x5B\x72\x6F\x6C\x65\x3D\x6F\x70\x74\x69\x6F\x6E\x5D","\x3C\x6C\x69\x3E\x3C\x61\x20\x74\x61\x62\x69\x6E\x64\x65\x78\x3D\x22\x2D\x31\x22\x20\x68\x72\x65\x66\x3D\x22\x23\x22\x20\x64\x61\x74\x61\x2D\x6F\x70\x74\x69\x6F\x6E\x3D\x22\x22\x3E\x3C\x2F\x61\x3E\x3C\x2F\x6C\x69\x3E","\x3C\x6C\x69\x3E\x3C\x61\x20\x74\x61\x62\x69\x6E\x64\x65\x78\x3D\x22\x2D\x31\x22\x20\x68\x72\x65\x66\x3D\x22\x23\x22\x20\x73\x74\x79\x6C\x65\x3D\x27\x66\x6F\x6E\x74\x2D\x66\x61\x6D\x69\x6C\x79\x3A\x20","\x27\x20\x64\x61\x74\x61\x2D\x6F\x70\x74\x69\x6F\x6E\x3D\x22","\x3C\x2F\x61\x3E\x3C\x2F\x6C\x69\x3E","\x62\x66\x68\x73\x65\x6C\x65\x63\x74\x62\x6F\x78","\x66\x6F\x72\x6D\x20\x73\x65\x6C\x65\x63\x74\x2E\x62\x66\x68\x2D\x66\x6F\x6E\x74\x73\x2C\x20\x73\x70\x61\x6E\x2E\x62\x66\x68\x2D\x66\x6F\x6E\x74\x73\x2C\x20\x64\x69\x76\x2E\x62\x66\x68\x2D\x66\x6F\x6E\x74\x73","\x62\x66\x68\x66\x6F\x6E\x74\x73\x69\x7A\x65\x73","\x61\x64\x64\x46\x6F\x6E\x74\x53\x69\x7A\x65\x73","\x61\x64\x64\x42\x6F\x6F\x74\x73\x74\x72\x61\x70\x46\x6F\x6E\x74\x53\x69\x7A\x65\x73","\x66\x6F\x6E\x74\x73\x69\x7A\x65","\x67\x65\x74\x46\x6F\x6E\x74\x73\x69\x7A\x65\x73","\x3C\x6C\x69\x3E\x3C\x61\x20\x74\x61\x62\x69\x6E\x64\x65\x78\x3D\x22\x2D\x31\x22\x20\x68\x72\x65\x66\x3D\x22\x23\x22\x20\x64\x61\x74\x61\x2D\x6F\x70\x74\x69\x6F\x6E\x3D\x22","\x66\x6F\x72\x6D\x20\x73\x65\x6C\x65\x63\x74\x2E\x62\x66\x68\x2D\x66\x6F\x6E\x74\x73\x69\x7A\x65\x73\x2C\x20\x73\x70\x61\x6E\x2E\x62\x66\x68\x2D\x66\x6F\x6E\x74\x73\x69\x7A\x65\x73\x2C\x20\x64\x69\x76\x2E\x62\x66\x68\x2D\x66\x6F\x6E\x74\x73\x69\x7A\x65\x73","\x62\x66\x68\x67\x6F\x6F\x67\x6C\x65\x66\x6F\x6E\x74\x73","\x73\x75\x62\x73\x65\x74","\x69\x74\x65\x6D\x73","\x73\x75\x62\x73\x65\x74\x73","\x66\x61\x6D\x69\x6C\x79","\x69\x6E\x66\x6F","\x3C\x6C\x69\x3E\x3C\x61\x20\x74\x61\x62\x69\x6E\x64\x65\x78\x3D\x22\x2D\x31\x22\x20\x68\x72\x65\x66\x3D\x22\x23\x22\x20\x64\x61\x74\x61\x2D\x6F\x70\x74\x69\x6F\x6E\x3D\x22\x22\x20\x73\x74\x79\x6C\x65\x3D\x22\x62\x61\x63\x6B\x67\x72\x6F\x75\x6E\x64\x2D\x69\x6D\x61\x67\x65\x3A\x20\x6E\x6F\x6E\x65\x3B\x22\x3E\x3C\x2F\x61\x3E\x3C\x2F\x6C\x69\x3E","\x3C\x6C\x69\x3E\x3C\x61\x20\x74\x61\x62\x69\x6E\x64\x65\x78\x3D\x22\x2D\x31\x22\x20\x68\x72\x65\x66\x3D\x22\x23\x22\x20\x73\x74\x79\x6C\x65\x3D\x22\x62\x61\x63\x6B\x67\x72\x6F\x75\x6E\x64\x2D\x70\x6F\x73\x69\x74\x69\x6F\x6E\x3A\x20\x30\x20\x2D","\x69\x6E\x64\x65\x78","\x70\x78\x3B\x22\x20\x64\x61\x74\x61\x2D\x6F\x70\x74\x69\x6F\x6E\x3D\x22","\x66\x6F\x72\x6D\x20\x73\x65\x6C\x65\x63\x74\x2E\x62\x66\x68\x2D\x67\x6F\x6F\x67\x6C\x65\x66\x6F\x6E\x74\x73\x2C\x20\x73\x70\x61\x6E\x2E\x62\x66\x68\x2D\x67\x6F\x6F\x67\x6C\x65\x66\x6F\x6E\x74\x73\x2C\x20\x64\x69\x76\x2E\x62\x66\x68\x2D\x67\x6F\x6F\x67\x6C\x65\x66\x6F\x6E\x74\x73","\x62\x66\x68\x6E\x75\x6D\x62\x65\x72","\x69\x6E\x69\x74\x49\x6E\x70\x75\x74","\x62\x75\x74\x74\x6F\x6E\x73","\x3C\x64\x69\x76\x20\x63\x6C\x61\x73\x73\x3D\x22\x69\x6E\x70\x75\x74\x2D\x67\x72\x6F\x75\x70\x22\x3E\x3C\x2F\x64\x69\x76\x3E","\x77\x72\x61\x70","\x3C\x73\x70\x61\x6E\x20\x63\x6C\x61\x73\x73\x3D\x22\x69\x6E\x70\x75\x74\x2D\x67\x72\x6F\x75\x70\x2D\x61\x64\x64\x6F\x6E\x20\x62\x66\x68\x2D\x6E\x75\x6D\x62\x65\x72\x2D\x62\x74\x6E\x20\x69\x6E\x63\x22\x3E\x3C\x73\x70\x61\x6E\x20\x63\x6C\x61\x73\x73\x3D\x22\x67\x6C\x79\x70\x68\x69\x63\x6F\x6E\x20\x67\x6C\x79\x70\x68\x69\x63\x6F\x6E\x2D\x63\x68\x65\x76\x72\x6F\x6E\x2D\x75\x70\x22\x3E\x3C\x2F\x73\x70\x61\x6E\x3E\x3C\x2F\x73\x70\x61\x6E\x3E","\x70\x61\x72\x65\x6E\x74","\x3C\x73\x70\x61\x6E\x20\x63\x6C\x61\x73\x73\x3D\x22\x69\x6E\x70\x75\x74\x2D\x67\x72\x6F\x75\x70\x2D\x61\x64\x64\x6F\x6E\x20\x62\x66\x68\x2D\x6E\x75\x6D\x62\x65\x72\x2D\x62\x74\x6E\x20\x64\x65\x63\x22\x3E\x3C\x73\x70\x61\x6E\x20\x63\x6C\x61\x73\x73\x3D\x22\x67\x6C\x79\x70\x68\x69\x63\x6F\x6E\x20\x67\x6C\x79\x70\x68\x69\x63\x6F\x6E\x2D\x63\x68\x65\x76\x72\x6F\x6E\x2D\x64\x6F\x77\x6E\x22\x3E\x3C\x2F\x73\x70\x61\x6E\x3E\x3C\x2F\x73\x70\x61\x6E\x3E","\x63\x68\x61\x6E\x67\x65\x2E\x62\x66\x68\x6E\x75\x6D\x62\x65\x72\x2E\x64\x61\x74\x61\x2D\x61\x70\x69","\x63\x68\x61\x6E\x67\x65","\x6B\x65\x79\x62\x6F\x61\x72\x64","\x6B\x65\x79\x64\x6F\x77\x6E\x2E\x62\x66\x68\x6E\x75\x6D\x62\x65\x72\x2E\x64\x61\x74\x61\x2D\x61\x70\x69","\x6B\x65\x79\x64\x6F\x77\x6E","\x6D\x6F\x75\x73\x65\x64\x6F\x77\x6E\x2E\x62\x66\x68\x6E\x75\x6D\x62\x65\x72\x2E\x64\x61\x74\x61\x2D\x61\x70\x69","\x2E\x64\x65\x63","\x62\x74\x6E\x64\x65\x63","\x2E\x69\x6E\x63","\x62\x74\x6E\x69\x6E\x63","\x66\x6F\x72\x6D\x61\x74\x4E\x75\x6D\x62\x65\x72","\x69\x6E\x63\x72\x65\x6D\x65\x6E\x74","\x64\x65\x63\x72\x65\x6D\x65\x6E\x74","\x77\x68\x69\x63\x68","\x62\x74\x6E","\x74\x69\x6D\x65\x72","\x69\x6E\x74\x65\x72\x76\x61\x6C","\x2E\x62\x66\x68\x2D\x6E\x75\x6D\x62\x65\x72","\x6D\x6F\x75\x73\x65\x75\x70","\x67\x65\x74\x56\x61\x6C\x75\x65","\x2D\x31","\x7A\x65\x72\x6F\x73","\x66\x6F\x72\x6D\x20\x69\x6E\x70\x75\x74\x5B\x74\x79\x70\x65\x3D\x22\x74\x65\x78\x74\x22\x5D\x2E\x62\x66\x68\x2D\x6E\x75\x6D\x62\x65\x72\x2C\x20\x66\x6F\x72\x6D\x20\x69\x6E\x70\x75\x74\x5B\x74\x79\x70\x65\x3D\x22\x6E\x75\x6D\x62\x65\x72\x22\x5D\x2E\x62\x66\x68\x2D\x6E\x75\x6D\x62\x65\x72","\x5B\x64\x61\x74\x61\x2D\x74\x6F\x67\x67\x6C\x65\x3D\x62\x66\x68\x2D\x73\x65\x6C\x65\x63\x74\x62\x6F\x78\x5D","\x69\x6E\x69\x74\x53\x65\x6C\x65\x63\x74\x42\x6F\x78","\x76\x61\x6C\x75\x65","\x3C\x69\x6E\x70\x75\x74\x20\x74\x79\x70\x65\x3D\x22\x68\x69\x64\x64\x65\x6E\x22\x20\x6E\x61\x6D\x65\x3D\x22","\x22\x20\x76\x61\x6C\x75\x65\x3D\x22\x22\x3E","\x3C\x61\x20\x63\x6C\x61\x73\x73\x3D\x22\x62\x66\x68\x2D\x73\x65\x6C\x65\x63\x74\x62\x6F\x78\x2D\x74\x6F\x67\x67\x6C\x65\x20","\x22\x20\x72\x6F\x6C\x65\x3D\x22\x62\x75\x74\x74\x6F\x6E\x22\x20\x64\x61\x74\x61\x2D\x74\x6F\x67\x67\x6C\x65\x3D\x22\x62\x66\x68\x2D\x73\x65\x6C\x65\x63\x74\x62\x6F\x78\x22\x20\x68\x72\x65\x66\x3D\x22\x23\x22\x3E","\x3C\x73\x70\x61\x6E\x20\x63\x6C\x61\x73\x73\x3D\x22\x62\x66\x68\x2D\x73\x65\x6C\x65\x63\x74\x62\x6F\x78\x2D\x6F\x70\x74\x69\x6F\x6E\x22\x3E\x3C\x2F\x73\x70\x61\x6E\x3E","\x3C\x73\x70\x61\x6E\x20\x63\x6C\x61\x73\x73\x3D\x22","\x20\x73\x65\x6C\x65\x63\x74\x62\x6F\x78\x2D\x63\x61\x72\x65\x74\x22\x3E\x3C\x2F\x73\x70\x61\x6E\x3E","\x3C\x2F\x61\x3E","\x3C\x64\x69\x76\x20\x63\x6C\x61\x73\x73\x3D\x22\x62\x66\x68\x2D\x73\x65\x6C\x65\x63\x74\x62\x6F\x78\x2D\x6F\x70\x74\x69\x6F\x6E\x73\x22\x3E","\x3C\x64\x69\x76\x20\x72\x6F\x6C\x65\x3D\x22\x6C\x69\x73\x74\x62\x6F\x78\x22\x3E","\x3C\x75\x6C\x20\x72\x6F\x6C\x65\x3D\x22\x6F\x70\x74\x69\x6F\x6E\x22\x3E","\x3C\x2F\x75\x6C\x3E","\x66\x69\x6C\x74\x65\x72","\x3C\x64\x69\x76\x20\x63\x6C\x61\x73\x73\x3D\x22\x62\x66\x68\x2D\x73\x65\x6C\x65\x63\x74\x62\x6F\x78\x2D\x66\x69\x6C\x74\x65\x72\x2D\x63\x6F\x6E\x74\x61\x69\x6E\x65\x72\x22\x3E\x3C\x69\x6E\x70\x75\x74\x20\x74\x79\x70\x65\x3D\x22\x74\x65\x78\x74\x22\x20\x63\x6C\x61\x73\x73\x3D\x22\x62\x66\x68\x2D\x73\x65\x6C\x65\x63\x74\x62\x6F\x78\x2D\x66\x69\x6C\x74\x65\x72\x20\x66\x6F\x72\x6D\x2D\x63\x6F\x6E\x74\x72\x6F\x6C\x22\x3E\x3C\x2F\x64\x69\x76\x3E","\x70\x72\x65\x70\x65\x6E\x64","\x2E\x62\x66\x68\x2D\x73\x65\x6C\x65\x63\x74\x62\x6F\x78\x2D\x6F\x70\x74\x69\x6F\x6E\x73","\x70\x72\x6F\x70\x65\x72\x74\x79\x63\x68\x61\x6E\x67\x65\x2E\x62\x66\x68\x73\x65\x6C\x65\x63\x74\x62\x6F\x78\x2E\x64\x61\x74\x61\x2D\x61\x70\x69\x20\x63\x68\x61\x6E\x67\x65\x2E\x62\x66\x68\x73\x65\x6C\x65\x63\x74\x62\x6F\x78\x2E\x64\x61\x74\x61\x2D\x61\x70\x69\x20\x69\x6E\x70\x75\x74\x2E\x62\x66\x68\x73\x65\x6C\x65\x63\x74\x62\x6F\x78\x2E\x64\x61\x74\x61\x2D\x61\x70\x69\x20\x70\x61\x73\x74\x65\x2E\x62\x66\x68\x73\x65\x6C\x65\x63\x74\x62\x6F\x78\x2E\x64\x61\x74\x61\x2D\x61\x70\x69","\x2E\x62\x66\x68\x2D\x73\x65\x6C\x65\x63\x74\x62\x6F\x78\x2D\x66\x69\x6C\x74\x65\x72","\x63\x6C\x69\x63\x6B\x2E\x62\x66\x68\x73\x65\x6C\x65\x63\x74\x62\x6F\x78\x2E\x64\x61\x74\x61\x2D\x61\x70\x69","\x5B\x72\x6F\x6C\x65\x3D\x6F\x70\x74\x69\x6F\x6E\x5D\x20\x3E\x20\x6C\x69\x20\x3E\x20\x61","\x6D\x6F\x75\x73\x65\x65\x6E\x74\x65\x72\x2E\x62\x66\x68\x73\x65\x6C\x65\x63\x74\x62\x6F\x78\x2E\x64\x61\x74\x61\x2D\x61\x70\x69","\x6D\x6F\x75\x73\x65\x65\x6E\x74\x65\x72","\x6B\x65\x79\x64\x6F\x77\x6E\x2E\x62\x66\x68\x73\x65\x6C\x65\x63\x74\x62\x6F\x78\x2E\x64\x61\x74\x61\x2D\x61\x70\x69","\x2C\x20\x5B\x72\x6F\x6C\x65\x3D\x6F\x70\x74\x69\x6F\x6E\x5D","\x63\x6C\x69\x63\x6B\x2E\x62\x66\x68\x73\x65\x6C\x65\x63\x74\x62\x6F\x78\x2E\x64\x61\x74\x61\x2D\x61\x70\x69\x20\x74\x6F\x75\x63\x68\x73\x74\x61\x72\x74\x2E\x62\x66\x68\x73\x65\x6C\x65\x63\x74\x62\x6F\x78\x2E\x64\x61\x74\x61\x2D\x61\x70\x69","\x73\x68\x6F\x77\x2E\x62\x66\x68\x73\x65\x6C\x65\x63\x74\x62\x6F\x78","\x5B\x72\x6F\x6C\x65\x3D\x6F\x70\x74\x69\x6F\x6E\x5D\x20\x3E\x20\x6C\x69\x20\x3E\x20\x5B\x64\x61\x74\x61\x2D\x6F\x70\x74\x69\x6F\x6E\x3D\x22","\x22\x5D","\x73\x68\x6F\x77\x6E\x2E\x62\x66\x68\x73\x65\x6C\x65\x63\x74\x62\x6F\x78","\x5B\x72\x6F\x6C\x65\x3D\x6F\x70\x74\x69\x6F\x6E\x5D\x20\x6C\x69\x20\x61","\x73\x68\x6F\x77","\x74\x6F\x55\x70\x70\x65\x72\x43\x61\x73\x65","\x68\x69\x64\x65","\x6B\x65\x79\x43\x6F\x64\x65","\x74\x65\x73\x74","\x63\x6C\x69\x63\x6B","\x5B\x72\x6F\x6C\x65\x3D\x6F\x70\x74\x69\x6F\x6E\x5D\x20\x6C\x69\x3A\x6E\x6F\x74\x28\x2E\x64\x69\x76\x69\x64\x65\x72\x29\x20\x61\x3A\x76\x69\x73\x69\x62\x6C\x65","\x6D\x6F\x75\x73\x65\x65\x6E\x74\x65\x72\x2E\x62\x66\x68\x2D\x73\x65\x6C\x65\x63\x74\x62\x6F\x78\x2E\x64\x61\x74\x61\x2D\x61\x70\x69","\x62\x6F\x64\x79","\x3A\x66\x6F\x63\x75\x73","\x65\x71","\x6F\x70\x74\x69\x6F\x6E","\x63\x68\x61\x6E\x67\x65\x2E\x62\x66\x68\x73\x65\x6C\x65\x63\x74\x62\x6F\x78","\x68\x69\x64\x65\x2E\x62\x66\x68\x73\x65\x6C\x65\x63\x74\x62\x6F\x78","\x68\x69\x64\x64\x65\x6E\x2E\x62\x66\x68\x73\x65\x6C\x65\x63\x74\x62\x6F\x78","\x2E\x62\x66\x68\x2D\x73\x65\x6C\x65\x63\x74\x62\x6F\x78","\x63\x61\x72\x65\x74","\x6C\x69\x20\x61\x5B\x64\x61\x74\x61\x2D\x6F\x70\x74\x69\x6F\x6E\x3D\x27","\x27\x5D","\x6C\x69\x20\x61","\x64\x69\x76\x2E\x62\x66\x68\x2D\x73\x65\x6C\x65\x63\x74\x62\x6F\x78","\x62\x66\x68\x73\x6C\x69\x64\x65\x72","\x69\x6E\x69\x74\x53\x6C\x69\x64\x65\x72","\x3C\x64\x69\x76\x20\x63\x6C\x61\x73\x73\x3D\x22\x62\x66\x68\x2D\x73\x6C\x69\x64\x65\x72\x2D\x68\x61\x6E\x64\x6C\x65\x22\x3E\x3C\x64\x69\x76\x20\x63\x6C\x61\x73\x73\x3D\x22\x62\x66\x68\x2D\x73\x6C\x69\x64\x65\x72\x2D\x76\x61\x6C\x75\x65\x22\x3E\x3C\x2F\x64\x69\x76\x3E\x3C\x2F\x64\x69\x76\x3E","\x75\x70\x64\x61\x74\x65\x48\x61\x6E\x64\x6C\x65","\x6D\x6F\x75\x73\x65\x64\x6F\x77\x6E\x2E\x62\x66\x68\x73\x6C\x69\x64\x65\x72\x2E\x64\x61\x74\x61\x2D\x61\x70\x69","\x70\x78","\x2E\x62\x66\x68\x2D\x73\x6C\x69\x64\x65\x72\x2D\x68\x61\x6E\x64\x6C\x65","\x2E\x62\x66\x68\x2D\x73\x6C\x69\x64\x65\x72\x2D\x76\x61\x6C\x75\x65","\x63\x65\x69\x6C","\x63\x68\x61\x6E\x67\x65\x2E\x62\x66\x68\x73\x6C\x69\x64\x65\x72","\x6D\x6F\x75\x73\x65\x75\x70\x2E\x62\x66\x68\x73\x6C\x69\x64\x65\x72\x2E\x64\x61\x74\x61\x2D\x61\x70\x69","\x6D\x6F\x75\x73\x65\x6D\x6F\x76\x65\x2E\x62\x66\x68\x73\x6C\x69\x64\x65\x72\x2E\x64\x61\x74\x61\x2D\x61\x70\x69","\x73\x6C\x69\x64\x65\x72","\x62\x66\x68\x2D\x73\x6C\x69\x64\x65\x72","\x64\x69\x76\x2E\x62\x66\x68\x2D\x73\x6C\x69\x64\x65\x72","\x62\x66\x68\x73\x74\x61\x74\x65\x73","\x61\x64\x64\x53\x74\x61\x74\x65\x73","\x61\x64\x64\x42\x6F\x6F\x74\x73\x74\x72\x61\x70\x53\x74\x61\x74\x65\x73","\x73\x70\x61\x6E","\x64\x69\x73\x70\x6C\x61\x79\x53\x74\x61\x74\x65","\x63\x6F\x75\x6E\x74\x72\x79","\x63\x68\x61\x6E\x67\x65\x43\x6F\x75\x6E\x74\x72\x79","\x6C\x6F\x61\x64\x53\x74\x61\x74\x65\x73","\x73\x74\x61\x74\x65","\x63\x6F\x64\x65","\x63\x68\x61\x6E\x67\x65\x42\x6F\x6F\x74\x73\x74\x72\x61\x70\x43\x6F\x75\x6E\x74\x72\x79","\x6C\x6F\x61\x64\x42\x6F\x6F\x74\x73\x74\x72\x61\x70\x53\x74\x61\x74\x65\x73","\x66\x6F\x72\x6D\x20\x73\x65\x6C\x65\x63\x74\x2E\x62\x66\x68\x2D\x73\x74\x61\x74\x65\x73\x2C\x20\x73\x70\x61\x6E\x2E\x62\x66\x68\x2D\x73\x74\x61\x74\x65\x73\x2C\x20\x64\x69\x76\x2E\x62\x66\x68\x2D\x73\x74\x61\x74\x65\x73","\x5B\x64\x61\x74\x61\x2D\x74\x6F\x67\x67\x6C\x65\x3D\x62\x66\x68\x2D\x74\x69\x6D\x65\x70\x69\x63\x6B\x65\x72\x5D","\x62\x66\x68\x74\x69\x6D\x65\x70\x69\x63\x6B\x65\x72","\x74\x69\x6D\x65","\x6E\x6F\x77","\x67\x65\x74\x48\x6F\x75\x72\x73","\x67\x65\x74\x4D\x69\x6E\x75\x74\x65\x73","\x6D\x6F\x64\x65","\x31\x32\x68","\x20","\x70\x6D","\x61\x6D","\x2E\x62\x66\x68\x2D\x74\x69\x6D\x65\x70\x69\x63\x6B\x65\x72\x2D\x74\x6F\x67\x67\x6C\x65\x20\x3E\x20\x69\x6E\x70\x75\x74\x5B\x74\x79\x70\x65\x3D\x22\x74\x65\x78\x74\x22\x5D","\x68\x6F\x75\x72","\x6D\x69\x6E\x75\x74\x65","\x32\x33","\x3C\x74\x64\x3E","\x3C\x64\x69\x76\x20\x63\x6C\x61\x73\x73\x3D\x22\x62\x66\x68\x2D\x73\x65\x6C\x65\x63\x74\x62\x6F\x78\x22\x20\x64\x61\x74\x61\x2D\x69\x6E\x70\x75\x74\x3D\x22","\x22\x20\x64\x61\x74\x61\x2D\x76\x61\x6C\x75\x65\x3D\x22\x61\x6D\x22\x3E","\x3C\x64\x69\x76\x20\x64\x61\x74\x61\x2D\x76\x61\x6C\x75\x65\x3D\x22\x61\x6D\x22\x3E","\x3C\x64\x69\x76\x20\x64\x61\x74\x61\x2D\x76\x61\x6C\x75\x65\x3D\x22\x70\x6D\x22\x3E","\x31\x31","\x20\x62\x66\x68\x2D\x74\x69\x6D\x65\x70\x69\x63\x6B\x65\x72\x2D\x74\x6F\x67\x67\x6C\x65\x22\x20\x64\x61\x74\x61\x2D\x74\x6F\x67\x67\x6C\x65\x3D\x22\x62\x66\x68\x2D\x74\x69\x6D\x65\x70\x69\x63\x6B\x65\x72\x22\x3E","\x3C\x64\x69\x76\x20\x63\x6C\x61\x73\x73\x3D\x22\x62\x66\x68\x2D\x74\x69\x6D\x65\x70\x69\x63\x6B\x65\x72\x2D\x70\x6F\x70\x6F\x76\x65\x72\x22\x3E","\x3C\x74\x61\x62\x6C\x65\x20\x63\x6C\x61\x73\x73\x3D\x22\x74\x61\x62\x6C\x65\x22\x3E","\x3C\x74\x64\x20\x63\x6C\x61\x73\x73\x3D\x22\x68\x6F\x75\x72\x22\x3E","\x3C\x69\x6E\x70\x75\x74\x20\x74\x79\x70\x65\x3D\x22\x74\x65\x78\x74\x22\x20\x63\x6C\x61\x73\x73\x3D\x22","\x20\x62\x66\x68\x2D\x6E\x75\x6D\x62\x65\x72\x22\x20\x20\x64\x61\x74\x61\x2D\x6D\x69\x6E\x3D\x22\x30\x22\x20\x64\x61\x74\x61\x2D\x6D\x61\x78\x3D\x22","\x22\x20\x64\x61\x74\x61\x2D\x7A\x65\x72\x6F\x73\x3D\x22\x74\x72\x75\x65\x22\x20\x64\x61\x74\x61\x2D\x77\x72\x61\x70\x3D\x22\x74\x72\x75\x65\x22\x3E","\x3C\x74\x64\x20\x63\x6C\x61\x73\x73\x3D\x22\x73\x65\x70\x61\x72\x61\x74\x6F\x72\x22\x3E","\x3C\x74\x64\x20\x63\x6C\x61\x73\x73\x3D\x22\x6D\x69\x6E\x75\x74\x65\x22\x3E","\x20\x62\x66\x68\x2D\x6E\x75\x6D\x62\x65\x72\x22\x20\x20\x64\x61\x74\x61\x2D\x6D\x69\x6E\x3D\x22\x30\x22\x20\x64\x61\x74\x61\x2D\x6D\x61\x78\x3D\x22\x35\x39\x22\x20\x64\x61\x74\x61\x2D\x7A\x65\x72\x6F\x73\x3D\x22\x74\x72\x75\x65\x22\x20\x64\x61\x74\x61\x2D\x77\x72\x61\x70\x3D\x22\x74\x72\x75\x65\x22\x3E","\x63\x6C\x69\x63\x6B\x2E\x62\x66\x68\x74\x69\x6D\x65\x70\x69\x63\x6B\x65\x72\x2E\x64\x61\x74\x61\x2D\x61\x70\x69\x20\x74\x6F\x75\x63\x68\x73\x74\x61\x72\x74\x2E\x62\x66\x68\x74\x69\x6D\x65\x70\x69\x63\x6B\x65\x72\x2E\x64\x61\x74\x61\x2D\x61\x70\x69","\x2E\x62\x66\x68\x2D\x74\x69\x6D\x65\x70\x69\x63\x6B\x65\x72\x2D\x70\x6F\x70\x6F\x76\x65\x72\x20\x3E\x20\x74\x61\x62\x6C\x65","\x73\x65\x74\x54\x69\x6D\x65","\x75\x70\x64\x61\x74\x65\x50\x6F\x70\x6F\x76\x65\x72","\x2E\x68\x6F\x75\x72\x20\x69\x6E\x70\x75\x74\x5B\x74\x79\x70\x65\x3D\x74\x65\x78\x74\x5D","\x2E\x6D\x69\x6E\x75\x74\x65\x20\x69\x6E\x70\x75\x74\x5B\x74\x79\x70\x65\x3D\x74\x65\x78\x74\x5D","\x75\x6E\x64\x65\x66\x69\x6E\x65\x64","\x63\x68\x61\x6E\x67\x65\x2E\x62\x66\x68\x74\x69\x6D\x65\x70\x69\x63\x6B\x65\x72","\x73\x68\x6F\x77\x2E\x62\x66\x68\x74\x69\x6D\x65\x70\x69\x63\x6B\x65\x72","\x73\x68\x6F\x77\x6E\x2E\x62\x66\x68\x74\x69\x6D\x65\x70\x69\x63\x6B\x65\x72","\x68\x69\x64\x65\x2E\x62\x66\x68\x74\x69\x6D\x65\x70\x69\x63\x6B\x65\x72","\x68\x69\x64\x64\x65\x6E\x2E\x62\x66\x68\x74\x69\x6D\x65\x70\x69\x63\x6B\x65\x72","\x2E\x62\x66\x68\x2D\x74\x69\x6D\x65\x70\x69\x63\x6B\x65\x72","\x67\x6C\x79\x70\x68\x69\x63\x6F\x6E\x20\x67\x6C\x79\x70\x68\x69\x63\x6F\x6E\x2D\x74\x69\x6D\x65","\x32\x34\x68","\x62\x66\x68\x2D\x74\x69\x6D\x65\x70\x69\x63\x6B\x65\x72","\x64\x69\x76\x2E\x62\x66\x68\x2D\x74\x69\x6D\x65\x70\x69\x63\x6B\x65\x72","\x63\x6C\x69\x63\x6B\x2E\x62\x66\x68\x74\x69\x6D\x65\x70\x69\x63\x6B\x65\x72\x2E\x64\x61\x74\x61\x2D\x61\x70\x69"];if(!jQuery){throw  new Error(_0xf556[0]);} ;var BFHMonthsList=[_0xf556[1],_0xf556[2],_0xf556[3],_0xf556[4],_0xf556[5],_0xf556[6],_0xf556[7],_0xf556[8],_0xf556[9],_0xf556[10],_0xf556[11],_0xf556[12]];var BFHDaysList=[_0xf556[13],_0xf556[14],_0xf556[15],_0xf556[16],_0xf556[17],_0xf556[18],_0xf556[19]];var BFHDayOfWeekStart=0;var BFHFontsList={"\x41\x6E\x64\x61\x6C\x65\x20\x4D\x6F\x6E\x6F":_0xf556[20],"\x41\x72\x69\x61\x6C":_0xf556[21],"\x41\x72\x69\x61\x6C\x20\x42\x6C\x61\x63\x6B":_0xf556[22],"\x41\x72\x69\x61\x6C\x20\x4E\x61\x72\x72\x6F\x77":_0xf556[23],"\x41\x72\x69\x61\x6C\x20\x52\x6F\x75\x6E\x64\x65\x64\x20\x4D\x54\x20\x42\x6F\x6C\x64":_0xf556[24],"\x41\x76\x61\x6E\x74\x20\x47\x61\x72\x64\x65":_0xf556[25],"\x42\x61\x73\x6B\x65\x72\x76\x69\x6C\x6C\x65":_0xf556[26],"\x42\x69\x67\x20\x43\x61\x73\x6C\x6F\x6E":_0xf556[27],"\x42\x6F\x64\x6F\x6E\x69\x20\x4D\x54":_0xf556[28],"\x42\x6F\x6F\x6B\x20\x41\x6E\x74\x69\x71\x75\x61":_0xf556[29],"\x42\x72\x75\x73\x68\x20\x53\x63\x72\x69\x70\x74\x20\x4D\x54":_0xf556[30],"\x43\x61\x6C\x69\x62\x72\x69":_0xf556[31],"\x43\x61\x6C\x69\x73\x74\x6F\x20\x4D\x54":_0xf556[32],"\x43\x61\x6D\x62\x72\x69\x6F":_0xf556[33],"\x43\x61\x6E\x64\x61\x72\x61":_0xf556[34],"\x43\x65\x6E\x74\x75\x72\x79\x20\x47\x6F\x74\x68\x69\x63":_0xf556[35],"\x43\x6F\x6E\x73\x6F\x6C\x61\x73":_0xf556[36],"\x43\x6F\x70\x70\x65\x72\x70\x6C\x61\x74\x65":_0xf556[37],"\x43\x6F\x75\x72\x69\x65\x72\x20\x4E\x65\x77":_0xf556[38],"\x44\x69\x64\x6F\x74":_0xf556[39],"\x46\x72\x61\x6E\x6B\x6C\x69\x6E\x20\x47\x6F\x74\x68\x69\x63\x20\x4D\x65\x64\x69\x75\x6D":_0xf556[40],"\x46\x75\x74\x75\x72\x61":_0xf556[41],"\x47\x61\x72\x61\x6D\x6F\x6E\x64":_0xf556[42],"\x47\x65\x6E\x65\x76\x61":_0xf556[43],"\x47\x65\x6F\x72\x67\x69\x61":_0xf556[44],"\x47\x69\x6C\x6C\x20\x53\x61\x6E\x73":_0xf556[45],"\x47\x6F\x75\x64\x79\x20\x4F\x6C\x64\x20\x53\x74\x79\x6C\x65":_0xf556[46],"\x48\x65\x6C\x76\x65\x74\x69\x63\x61":_0xf556[47],"\x48\x6F\x65\x66\x6C\x65\x72\x20\x54\x65\x78\x74":_0xf556[48],"\x49\x6D\x70\x61\x63\x74":_0xf556[49],"\x4C\x75\x63\x69\x64\x61\x20\x42\x72\x69\x67\x68\x74":_0xf556[50],"\x4C\x75\x63\x69\x64\x61\x20\x43\x6F\x6E\x73\x6F\x6C\x65":_0xf556[51],"\x4C\x75\x63\x69\x64\x61\x20\x53\x61\x6E\x73\x20\x54\x79\x70\x65\x77\x72\x69\x74\x65\x72":_0xf556[52],"\x4C\x75\x63\x69\x64\x61\x20\x47\x72\x61\x6E\x64\x65":_0xf556[53],"\x4D\x6F\x6E\x61\x63\x6F":_0xf556[54],"\x4F\x70\x74\x69\x6D\x61":_0xf556[55],"\x50\x61\x6C\x61\x74\x69\x6E\x6F":_0xf556[56],"\x50\x61\x70\x79\x72\x75\x73":_0xf556[57],"\x50\x65\x72\x70\x65\x74\x75\x61":_0xf556[58],"\x52\x6F\x63\x6B\x77\x65\x6C\x6C":_0xf556[59],"\x52\x6F\x63\x6B\x77\x65\x6C\x6C\x20\x45\x78\x74\x72\x61\x20\x42\x6F\x6C\x64":_0xf556[60],"\x53\x65\x67\x6F\x65\x20\x55\x49":_0xf556[61],"\x54\x61\x68\x6F\x6D\x61":_0xf556[62],"\x54\x69\x6D\x65\x73\x20\x4E\x65\x77\x20\x52\x6F\x6D\x61\x6E":_0xf556[63],"\x54\x72\x65\x62\x75\x63\x68\x65\x74\x20\x4D\x53":_0xf556[64],"\x56\x65\x72\x64\x61\x6E\x61":_0xf556[65]};var BFHFontSizesList={"\x38":_0xf556[66],"\x39":_0xf556[67],"\x31\x30":_0xf556[68],"\x31\x31":_0xf556[69],"\x31\x32":_0xf556[70],"\x31\x34":_0xf556[71],"\x31\x36":_0xf556[72],"\x31\x38":_0xf556[73],"\x32\x30":_0xf556[74],"\x32\x34":_0xf556[75],"\x32\x38":_0xf556[76],"\x33\x36":_0xf556[77],"\x34\x38":_0xf556[78]};var BFHGoogleFontsList={"\x6B\x69\x6E\x64":_0xf556[79],"\x69\x74\x65\x6D\x73":[{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[81],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[85],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[86],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[88],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[89],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[90],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[91],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[92],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[93],_0xf556[94],_0xf556[95],_0xf556[82],_0xf556[96],_0xf556[97],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84],_0xf556[99]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[100],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[101],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[102],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[103],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[104],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105],_0xf556[106],_0xf556[107]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[108],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105],_0xf556[106],_0xf556[107]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[109],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[110],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[111],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[112],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[113],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[114],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[115],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[116],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[117],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[118],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[119],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[120],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[121],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[122],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[123],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[124],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[125],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[126],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[127],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[87],_0xf556[84],_0xf556[129]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[130],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[131]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[132],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[133],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[134],_0xf556[87],_0xf556[84],_0xf556[99],_0xf556[129]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[135],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[136],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[137],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[138],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[139],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[140],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[141],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[142],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[143],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[144],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[145],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[146],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[147],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[148],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[149],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[150],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[151],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[152],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[153],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[154],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[155],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[156],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[157],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[158],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[159],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[160],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[161],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[95],_0xf556[162],_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[163],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[95],_0xf556[162],_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[164],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[95],_0xf556[162],_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[165],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[166],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[167],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[168],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[169],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[131]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[170],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[171],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[131]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[172],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[173],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[174],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[95],_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[175],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[176],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[177],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[178],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[179],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[180],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[181],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[182],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[183],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[184],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[131]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[185],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[186],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[187],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[188],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[189],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[190],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[191],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[192],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[193],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[95]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[194],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[195],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[196],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[197],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[96],_0xf556[198],_0xf556[97],_0xf556[199],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[200],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[96],_0xf556[97],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[201],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[202],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[203],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[204],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[205],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[206],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[207],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[208],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[209],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[210],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[211],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[134],_0xf556[87],_0xf556[84],_0xf556[99]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[212],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[213],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[214],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[215],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[216],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[134],_0xf556[87],_0xf556[84],_0xf556[99]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[217],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[218],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[219],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[220],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[221],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[222],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[223],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[224],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[131]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[225],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[226],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[227],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[228],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[229],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[106],_0xf556[107]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[230],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98],_0xf556[106]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[231],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98],_0xf556[106]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[232],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[233],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[234]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[235],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[234]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[236],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[95],_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[237],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[238],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[95],_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[87],_0xf556[84],_0xf556[99],_0xf556[129]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[239],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[240],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[241],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[242],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[131]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[243],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[244],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[245],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[246],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[247],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[248],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[249],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[250],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[106]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[251],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[252],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[253],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[254],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[255],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[97],_0xf556[199],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[256],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[257],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[258],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[259],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[260],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[261],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[262],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[263],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[131]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[264],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[265],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[266],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[267],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[268],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[269],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[270],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[271],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[134],_0xf556[87],_0xf556[84],_0xf556[99],_0xf556[129]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[272],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[273],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[274],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[275],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[276],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[94],_0xf556[95],_0xf556[82],_0xf556[96],_0xf556[97],_0xf556[98],_0xf556[234]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[277],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[278],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[279],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[280],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[281],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[282],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[283],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[87],_0xf556[84],_0xf556[284],_0xf556[129]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[285],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[286],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[287],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[288],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[289],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[290],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[291],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[292],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[293],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[294],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[295],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[296],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[297],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[298],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[93],_0xf556[299],_0xf556[94],_0xf556[300],_0xf556[95],_0xf556[162],_0xf556[82],_0xf556[83],_0xf556[96],_0xf556[198],_0xf556[97],_0xf556[199],_0xf556[98],_0xf556[105],_0xf556[234],_0xf556[301],_0xf556[106],_0xf556[107]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[302],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[96],_0xf556[198],_0xf556[97],_0xf556[199],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[303],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[304],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[305],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[306],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[307],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[131]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[308],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[309],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[310],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[311],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[312],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[313],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[314],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[95],_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[315],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[316],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[317],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[318],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[87],_0xf556[84],_0xf556[129]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[319],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[320],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[321],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[322],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[323],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[131]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[324],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[325],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[326],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[327],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[99]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[328],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[99]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[329],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[330],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[331],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[332],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[333],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[334],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[335],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[336],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[337],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[338],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[339],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[340],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[341],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[342],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[343],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[344],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[345],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[346],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[347],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[348],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[349],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[350],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[351],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[352],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[353],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[354],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[355],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[356],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[357],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[358],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[131]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[359],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[360],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[361],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[362],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[363],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[364],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[365],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[366],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[367],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[368],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[369],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[370],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[371],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[372],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[373],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[374],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[375],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[376],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[377],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[378],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[379],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[380],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[381],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[382],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[383],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[384],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[87],_0xf556[84],_0xf556[129]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[385],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[386],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[387],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[388],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[389],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[390],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[391],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[392],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[93],_0xf556[299],_0xf556[95],_0xf556[162],_0xf556[82],_0xf556[83],_0xf556[97],_0xf556[199],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[393],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[93],_0xf556[299],_0xf556[95],_0xf556[162],_0xf556[82],_0xf556[83],_0xf556[97],_0xf556[199],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[394],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[395],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[396],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[397],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[398],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[399],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[95],_0xf556[82],_0xf556[96],_0xf556[97]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[134],_0xf556[87],_0xf556[84],_0xf556[99],_0xf556[129]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[400],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[401],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[402],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[403],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[404],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[405],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[406],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[407],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[408],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[131]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[409],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[410],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[411],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[412],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[131]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[413],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[414],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[95],_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[415],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[416],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[417],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[418],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[419],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[93],_0xf556[299],_0xf556[95],_0xf556[162],_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105],_0xf556[106],_0xf556[107]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[420],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[421],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[422],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[423],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[424],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[425],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[426],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[427],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[428],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[429],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[87],_0xf556[84],_0xf556[129]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[430],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[431],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[432],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[433],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[434],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[435],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[436],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[437],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[438],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[439],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[440],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[441],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[442],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[443],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[444],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[445],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[446],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[447],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[448],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[449],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[450],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[451],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[452],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[453],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[454],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[455],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[456],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[96],_0xf556[98],_0xf556[106]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[457],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[458],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[459],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[460],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[461],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[462],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[463],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[464],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[465],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[95],_0xf556[82],_0xf556[98],_0xf556[106]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[466],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[131]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[467],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[468],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[469],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[470],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[471],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[472],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[473],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[474],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[475],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[476],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[477],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[83]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[478],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[479],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[480],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[481],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[482],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[483],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[484],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[485],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[486],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[131]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[487],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[131]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[488],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[489],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[490],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[491],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[492],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[493],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[494],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[495],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[95],_0xf556[162],_0xf556[82],_0xf556[83]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[496],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[497],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[498],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[94],_0xf556[95],_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[234]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[499],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[500],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[501],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[502],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[503],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[131]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[504],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[505],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[506],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[507],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84],_0xf556[284]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[508],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[509],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[510],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84],_0xf556[99]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[511],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[512],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[513],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[514],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[515],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[516],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[517],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[95],_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[518],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[131]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[519],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[520],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[521],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[522],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[523],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[524],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[95],_0xf556[162],_0xf556[82],_0xf556[83],_0xf556[97],_0xf556[199],_0xf556[98],_0xf556[105],_0xf556[234],_0xf556[301]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[134],_0xf556[87],_0xf556[84],_0xf556[284],_0xf556[99],_0xf556[129]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[525],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[95],_0xf556[162],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[134],_0xf556[87],_0xf556[84],_0xf556[284],_0xf556[99],_0xf556[129]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[526],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[87],_0xf556[84],_0xf556[129]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[527],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[96],_0xf556[98],_0xf556[106]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[528],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[529],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[530],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[531],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[95],_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[532],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[533],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105],_0xf556[106],_0xf556[107]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[534],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[535],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[536],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[95],_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[537],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[538],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[87],_0xf556[84],_0xf556[129]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[539],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[540],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[541],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[542],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[543],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[544],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[545],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[546],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[547],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[548],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98],_0xf556[106]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[549],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[550],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[551],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[552],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[553],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[554],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[555],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[556],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[557],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[558],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[559],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[560],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[561],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[134],_0xf556[87],_0xf556[84],_0xf556[99],_0xf556[129]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[562],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[563],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105],_0xf556[106],_0xf556[107]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[564],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105],_0xf556[106],_0xf556[107]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[565],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[566],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[567],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[568],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[569],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[570],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[571],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[572],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[573],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[574],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[131]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[575],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[87],_0xf556[84],_0xf556[99]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[576],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[577],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[578],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[579],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[580],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[581],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[582],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[583],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[584],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[585],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[586],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[95],_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[587],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[588],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[589],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[590],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[591],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[93],_0xf556[94],_0xf556[95],_0xf556[82],_0xf556[96],_0xf556[97],_0xf556[98],_0xf556[234],_0xf556[106]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[592],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[593],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[594],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[595],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[596],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[597],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[598],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[599],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[600],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[601],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[602],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[603],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[604],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[605],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[606],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[607],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[608],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[609],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[610],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[611],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[612],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[613],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98],_0xf556[106]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[614],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[615],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[616],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[617],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[618],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[87],_0xf556[84],_0xf556[129]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[619],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[620],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[621],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[622],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[623],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[624],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[625],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[626],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[627],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[628],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[629],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[630],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[631],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[632],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[633],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[634],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[635],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[636],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[637],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[638],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[639],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[640],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[641],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[642],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[643],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[131]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[644],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[645],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[95],_0xf556[82],_0xf556[97],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[646],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[95],_0xf556[82],_0xf556[97],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[647],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[106],_0xf556[107]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[648],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[649],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[650],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[651],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[652],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[653],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[654],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[234]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[655],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[656],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[657],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[658],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[659],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[660],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[661],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[94],_0xf556[95],_0xf556[82],_0xf556[97],_0xf556[98],_0xf556[106]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[662],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[94],_0xf556[300],_0xf556[95],_0xf556[162],_0xf556[82],_0xf556[83],_0xf556[97],_0xf556[199],_0xf556[98],_0xf556[105],_0xf556[106],_0xf556[107]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[663],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[664],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[665],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[666],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[667],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[668],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[669],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[670],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[671],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[672],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[673],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[95],_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[674],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[675],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[676],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[677],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[678],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[131]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[679],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[680],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[681],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[682],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[131]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[683],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[684],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[87],_0xf556[84],_0xf556[129]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[685],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[686],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[687],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98],_0xf556[106]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[688],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[689],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[690],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[94],_0xf556[300],_0xf556[95],_0xf556[162],_0xf556[82],_0xf556[83],_0xf556[97],_0xf556[199],_0xf556[98],_0xf556[105],_0xf556[106]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[691],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[692],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[693],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[694],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[695],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[696],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[95],_0xf556[162],_0xf556[82],_0xf556[83],_0xf556[96],_0xf556[198],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[134],_0xf556[87],_0xf556[84],_0xf556[99],_0xf556[129]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[697],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[134],_0xf556[87],_0xf556[84],_0xf556[99],_0xf556[129]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[698],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[134],_0xf556[87],_0xf556[84],_0xf556[99],_0xf556[129]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[699],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[700],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[701],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[702],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[703],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[704],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[705],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[706],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[707],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[708],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[709],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[710],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[711],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[712],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[713],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[714],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[715],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[716],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[717],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[718],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82],_0xf556[83],_0xf556[98],_0xf556[105]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[719],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[720],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[721],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[722],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[723],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[724],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[725],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[726],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[94],_0xf556[95],_0xf556[82],_0xf556[98]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[727],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[728],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[128],_0xf556[87],_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[729],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]},{"\x6B\x69\x6E\x64":_0xf556[80],"\x66\x61\x6D\x69\x6C\x79":_0xf556[730],"\x76\x61\x72\x69\x61\x6E\x74\x73":[_0xf556[82]],"\x73\x75\x62\x73\x65\x74\x73":[_0xf556[84]]}]};var BFHTimePickerDelimiter=_0xf556[731];var BFHTimePickerModes={"\x61\x6D":_0xf556[732],"\x70\x6D":_0xf556[733]};+function (_0xde03x9){_0xf556[735];var _0xde03xa=_0xf556[736],_0xde03xb=function (_0xde03xc,_0xde03xd){this[_0xf556[737]]=_0xde03x9[_0xf556[741]]({},_0xde03x9[_0xf556[740]][_0xf556[739]][_0xf556[738]],_0xde03xd);this[_0xf556[742]]=_0xde03x9(_0xde03xc);this[_0xf556[743]]();} ;_0xde03xb[_0xf556[744]]={constructor:_0xde03xb,initPalette:function (){var _0xde03xe,_0xde03xf,_0xde03x10;_0xde03xe=this[_0xf556[742]][_0xf556[746]](_0xf556[745]);_0xde03xf=_0xde03xe[0][_0xf556[748]](_0xf556[747]);_0xde03x10=_0xde03xf[_0xf556[750]](0,0,_0xde03xe[_0xf556[749]](),0);_0xde03x10[_0xf556[752]](0,_0xf556[751]);_0xde03x10[_0xf556[752]](0.1,_0xf556[753]);_0xde03x10[_0xf556[752]](0.25,_0xf556[754]);_0xde03x10[_0xf556[752]](0.4,_0xf556[755]);_0xde03x10[_0xf556[752]](0.55,_0xf556[756]);_0xde03x10[_0xf556[752]](0.7,_0xf556[757]);_0xde03x10[_0xf556[752]](0.85,_0xf556[758]);_0xde03x10[_0xf556[752]](1,_0xf556[753]);_0xde03xf[_0xf556[759]]=_0xde03x10;_0xde03xf[_0xf556[761]](0,0,_0xde03xf[_0xf556[745]][_0xf556[749]],_0xde03xf[_0xf556[745]][_0xf556[760]]);_0xde03x10=_0xde03xf[_0xf556[750]](0,0,0,_0xde03xe[_0xf556[760]]());_0xde03x10[_0xf556[752]](0,_0xf556[762]);_0xde03x10[_0xf556[752]](0.5,_0xf556[763]);_0xde03x10[_0xf556[752]](0.5,_0xf556[764]);_0xde03x10[_0xf556[752]](1,_0xf556[765]);_0xde03xf[_0xf556[759]]=_0xde03x10;_0xde03xf[_0xf556[761]](0,0,_0xde03xf[_0xf556[745]][_0xf556[749]],_0xde03xf[_0xf556[745]][_0xf556[760]]);} ,initPopover:function (){var _0xde03x11,_0xde03x12;_0xde03x11=_0xf556[766];_0xde03x12=_0xf556[766];if(this[_0xf556[737]][_0xf556[767]]===_0xf556[768]){_0xde03x12=_0xf556[769];} else {_0xde03x11=_0xf556[769];} ;this[_0xf556[742]][_0xf556[781]](_0xf556[770]+_0xde03x11+_0xf556[771]+this[_0xf556[737]][_0xf556[772]]+_0xf556[773]+this[_0xf556[737]][_0xf556[774]]+_0xf556[775]+this[_0xf556[737]][_0xf556[776]]+_0xf556[777]+_0xde03x12+_0xf556[778]+_0xf556[779]+_0xf556[780]+_0xf556[778]);this[_0xf556[742]][_0xf556[784]](_0xf556[782],_0xde03xa,_0xde03xb[_0xf556[744]][_0xf556[787]])[_0xf556[784]](_0xf556[785],_0xf556[745],_0xde03xb[_0xf556[744]][_0xf556[786]])[_0xf556[784]](_0xf556[782],_0xf556[783],function (){return false;} );this[_0xf556[788]]();this[_0xf556[742]][_0xf556[790]](this[_0xf556[737]][_0xf556[789]]);} ,updateVal:function (_0xde03x13,_0xde03x14){var _0xde03xe,_0xde03xf,_0xde03x15,_0xde03x16,_0xde03x17,_0xde03x18,_0xde03x19;_0xde03x17=5;_0xde03xe=this[_0xf556[742]][_0xf556[746]](_0xf556[745]);_0xde03xf=_0xde03xe[0][_0xf556[748]](_0xf556[747]);_0xde03x15=_0xde03x13-_0xde03xe[_0xf556[792]]()[_0xf556[791]];_0xde03x16=_0xde03x14-_0xde03xe[_0xf556[792]]()[_0xf556[793]];_0xde03x15=Math[_0xf556[794]](_0xde03x15/_0xde03x17)*_0xde03x17;_0xde03x16=Math[_0xf556[794]](_0xde03x16/_0xde03x17)*_0xde03x17;if(_0xde03x15<0){_0xde03x15=0;} ;if(_0xde03x15>=_0xde03xe[_0xf556[749]]()){_0xde03x15=_0xde03xe[_0xf556[749]]()-1;} ;if(_0xde03x16<0){_0xde03x16=0;} ;if(_0xde03x16>_0xde03xe[_0xf556[760]]()){_0xde03x16=_0xde03xe[_0xf556[760]]();} ;_0xde03x18=_0xde03xf[_0xf556[795]](_0xde03x15,_0xde03x16,1,1);_0xde03x19=_0xde03x21(_0xde03x18[_0xf556[796]][0],_0xde03x18[_0xf556[796]][1],_0xde03x18[_0xf556[796]][2]);if(_0xde03x19!==this[_0xf556[742]][_0xf556[790]]()){this[_0xf556[742]][_0xf556[790]](_0xde03x19);this[_0xf556[742]][_0xf556[798]](_0xf556[797]);} ;} ,mouseDown:function (_0xde03x1a){var _0xde03x1b,_0xde03x1c;_0xde03x1b=_0xde03x9(this);_0xde03x1c=_0xde03x26(_0xde03x1b);_0xde03x9(document)[_0xf556[784]](_0xf556[802],{colorpicker:_0xde03x1c},_0xde03xb[_0xf556[744]][_0xf556[803]])[_0xf556[801]](_0xf556[799],{colorpicker:_0xde03x1c},_0xde03xb[_0xf556[744]][_0xf556[800]]);} ,mouseMove:function (_0xde03x1a){var _0xde03x1b;_0xde03x1b=_0xde03x1a[_0xf556[796]][_0xf556[804]];_0xde03x1b[_0xf556[796]](_0xf556[739])[_0xf556[807]](_0xde03x1a[_0xf556[805]],_0xde03x1a[_0xf556[806]]);} ,mouseUp:function (_0xde03x1a){var _0xde03x1b;_0xde03x1b=_0xde03x1a[_0xf556[796]][_0xf556[804]];_0xde03x1b[_0xf556[796]](_0xf556[739])[_0xf556[807]](_0xde03x1a[_0xf556[805]],_0xde03x1a[_0xf556[806]]);_0xde03x9(document)[_0xf556[808]](_0xf556[802]);if(_0xde03x1b[_0xf556[796]](_0xf556[739])[_0xf556[737]][_0xf556[809]]===true){_0xde03x25();} ;} ,toggle:function (_0xde03x1a){var _0xde03x1b,_0xde03x1c,_0xde03x1d;_0xde03x1b=_0xde03x9(this);_0xde03x1c=_0xde03x26(_0xde03x1b);if(_0xde03x1c[_0xf556[811]](_0xf556[810])||_0xde03x1c[_0xf556[813]](_0xf556[812])!==undefined){return true;} ;_0xde03x1d=_0xde03x1c[_0xf556[815]](_0xf556[814]);_0xde03x25();if(!_0xde03x1d){_0xde03x1c[_0xf556[798]](_0xde03x1a=_0xde03x9.Event(_0xf556[816]));if(_0xde03x1a[_0xf556[817]]()){return true;} ;_0xde03x1c[_0xf556[819]](_0xf556[814])[_0xf556[798]](_0xf556[818]);_0xde03x1b[_0xf556[820]]();} ;return false;} };function _0xde03x1e(_0xde03x1f){var _0xde03x20=_0xde03x1f.toString(16);return _0xde03x20[_0xf556[821]]===1?_0xf556[822]+_0xde03x20:_0xde03x20;} ;function _0xde03x21(_0xde03x22,_0xde03x23,_0xde03x24){return _0xf556[823]+_0xde03x1e(_0xde03x22)+_0xde03x1e(_0xde03x23)+_0xde03x1e(_0xde03x24);} ;function _0xde03x25(){var _0xde03x1c;_0xde03x9(_0xde03xa)[_0xf556[827]](function (_0xde03x1a){_0xde03x1c=_0xde03x26(_0xde03x9(this));if(!_0xde03x1c[_0xf556[815]](_0xf556[814])){return true;} ;_0xde03x1c[_0xf556[798]](_0xde03x1a=_0xde03x9.Event(_0xf556[824]));if(_0xde03x1a[_0xf556[817]]()){return true;} ;_0xde03x1c[_0xf556[826]](_0xf556[814])[_0xf556[798]](_0xf556[825]);} );} ;function _0xde03x26(_0xde03x1b){return _0xde03x1b[_0xf556[829]](_0xf556[828]);} ;var _0xde03x27=_0xde03x9[_0xf556[740]][_0xf556[739]];_0xde03x9[_0xf556[740]][_0xf556[739]]=function (_0xde03x28){return this[_0xf556[827]](function (){var _0xde03x1b,_0xde03x29,_0xde03xd;_0xde03x1b=_0xde03x9(this);_0xde03x29=_0xde03x1b[_0xf556[796]](_0xf556[739]);_0xde03xd= typeof _0xde03x28===_0xf556[830]&&_0xde03x28;this[_0xf556[831]]=_0xf556[739];if(!_0xde03x29){_0xde03x1b[_0xf556[796]](_0xf556[739],(_0xde03x29= new _0xde03xb(this,_0xde03xd)));} ;if( typeof _0xde03x28===_0xf556[832]){_0xde03x29[_0xde03x28][_0xf556[833]](_0xde03x1b);} ;} );} ;_0xde03x9[_0xf556[740]][_0xf556[739]][_0xf556[834]]=_0xde03xb;_0xde03x9[_0xf556[740]][_0xf556[739]][_0xf556[738]]={align:_0xf556[791],input:_0xf556[835],placeholder:_0xf556[766],name:_0xf556[766],color:_0xf556[836],close:true};_0xde03x9[_0xf556[740]][_0xf556[739]][_0xf556[837]]=function (){_0xde03x9[_0xf556[740]][_0xf556[739]]=_0xde03x27;return this;} ;var _0xde03x2a;if(_0xde03x9[_0xf556[839]][_0xf556[838]]){_0xde03x2a=_0xde03x9[_0xf556[839]][_0xf556[838]];} ;_0xde03x9[_0xf556[839]][_0xf556[838]]={get:function (_0xde03x2b){if(_0xde03x9(_0xde03x2b)[_0xf556[815]](_0xf556[840])){return _0xde03x9(_0xde03x2b)[_0xf556[746]](_0xf556[841])[_0xf556[790]]();} else {if(_0xde03x2a){return _0xde03x2a[_0xf556[842]](_0xde03x2b);} ;} ;} ,set:function (_0xde03x2b,_0xde03x2c){if(_0xde03x9(_0xde03x2b)[_0xf556[815]](_0xf556[840])){_0xde03x9(_0xde03x2b)[_0xf556[746]](_0xf556[845])[_0xf556[844]](_0xf556[843],_0xde03x2c);_0xde03x9(_0xde03x2b)[_0xf556[746]](_0xf556[841])[_0xf556[790]](_0xde03x2c);} else {if(_0xde03x2a){return _0xde03x2a[_0xf556[846]](_0xde03x2b,_0xde03x2c);} ;} ;} };_0xde03x9(document)[_0xf556[848]](function (){_0xde03x9(_0xf556[847])[_0xf556[827]](function (){var _0xde03x2d;_0xde03x2d=_0xde03x9(this);_0xde03x2d[_0xf556[739]](_0xde03x2d[_0xf556[796]]());} );} );_0xde03x9(document)[_0xf556[784]](_0xf556[849],_0xde03x25);} (window[_0xf556[734]]);+function (_0xde03x9){_0xf556[735];var _0xde03xa=_0xf556[850],_0xde03x2e=function (_0xde03xc,_0xde03xd){this[_0xf556[737]]=_0xde03x9[_0xf556[741]]({},_0xde03x9[_0xf556[740]][_0xf556[851]][_0xf556[738]],_0xde03xd);this[_0xf556[742]]=_0xde03x9(_0xde03xc);this[_0xf556[852]]();} ;_0xde03x2e[_0xf556[744]]={constructor:_0xde03x2e,setDate:function (){var _0xde03x2f,_0xde03x30,_0xde03x31;_0xde03x2f=this[_0xf556[737]][_0xf556[853]];_0xde03x31=this[_0xf556[737]][_0xf556[854]];if(_0xde03x2f===_0xf556[766]||_0xde03x2f===_0xf556[855]||_0xde03x2f===undefined){_0xde03x30= new Date();if(_0xde03x2f===_0xf556[855]){this[_0xf556[742]][_0xf556[790]](_0xde03x4a(_0xde03x31,_0xde03x30[_0xf556[856]](),_0xde03x30[_0xf556[857]](),_0xde03x30[_0xf556[858]]()));} ;this[_0xf556[742]][_0xf556[796]](_0xf556[859],_0xde03x30[_0xf556[856]]());this[_0xf556[742]][_0xf556[796]](_0xf556[860],_0xde03x30[_0xf556[857]]());} else {this[_0xf556[742]][_0xf556[790]](_0xde03x2f);this[_0xf556[742]][_0xf556[796]](_0xf556[859],Number(_0xde03x4b(_0xde03x31,_0xde03x2f,_0xf556[861])-1));this[_0xf556[742]][_0xf556[796]](_0xf556[860],Number(_0xde03x4b(_0xde03x31,_0xde03x2f,_0xf556[862])));} ;} ,setDateLimit:function (_0xde03x2f,_0xde03x32){var _0xde03x30,_0xde03x31;_0xde03x31=this[_0xf556[737]][_0xf556[854]];if(_0xde03x2f!==_0xf556[766]){this[_0xf556[742]][_0xf556[796]](_0xde03x32+_0xf556[863],true);if(_0xde03x2f===_0xf556[855]){_0xde03x30= new Date();this[_0xf556[742]][_0xf556[796]](_0xde03x32+_0xf556[864],_0xde03x30[_0xf556[858]]());this[_0xf556[742]][_0xf556[796]](_0xde03x32+_0xf556[859],_0xde03x30[_0xf556[856]]());this[_0xf556[742]][_0xf556[796]](_0xde03x32+_0xf556[860],_0xde03x30[_0xf556[857]]());} else {this[_0xf556[742]][_0xf556[796]](_0xde03x32+_0xf556[864],Number(_0xde03x4b(_0xde03x31,_0xde03x2f,_0xf556[865])));this[_0xf556[742]][_0xf556[796]](_0xde03x32+_0xf556[859],Number(_0xde03x4b(_0xde03x31,_0xde03x2f,_0xf556[861])-1));this[_0xf556[742]][_0xf556[796]](_0xde03x32+_0xf556[860],Number(_0xde03x4b(_0xde03x31,_0xde03x2f,_0xf556[862])));} ;} else {this[_0xf556[742]][_0xf556[796]](_0xde03x32+_0xf556[863],false);} ;} ,initCalendar:function (){var _0xde03x11,_0xde03x12,_0xde03x33;_0xde03x11=_0xf556[766];_0xde03x12=_0xf556[766];_0xde03x33=_0xf556[766];if(this[_0xf556[737]][_0xf556[866]]!==_0xf556[766]){if(this[_0xf556[737]][_0xf556[767]]===_0xf556[768]){_0xde03x12=_0xf556[867]+this[_0xf556[737]][_0xf556[866]]+_0xf556[868];} else {_0xde03x11=_0xf556[867]+this[_0xf556[737]][_0xf556[866]]+_0xf556[868];} ;_0xde03x33=_0xf556[869];} ;this[_0xf556[742]][_0xf556[781]](_0xf556[870]+_0xde03x33+_0xf556[871]+_0xde03x11+_0xf556[771]+this[_0xf556[737]][_0xf556[772]]+_0xf556[773]+this[_0xf556[737]][_0xf556[774]]+_0xf556[775]+this[_0xf556[737]][_0xf556[776]]+_0xf556[777]+_0xde03x12+_0xf556[778]+_0xf556[872]+_0xf556[873]+_0xf556[874]+_0xf556[875]+_0xf556[876]+_0xf556[877]+_0xf556[878]+_0xf556[879]+_0xf556[880]+_0xf556[881]+_0xf556[877]+_0xf556[878]+_0xf556[879]+_0xf556[880]+_0xf556[882]+_0xf556[883]+_0xf556[882]+_0xf556[884]+_0xf556[885]+_0xf556[886]+_0xf556[887]+_0xf556[778]);this[_0xf556[742]][_0xf556[784]](_0xf556[888],_0xde03xa,_0xde03x2e[_0xf556[744]][_0xf556[787]])[_0xf556[784]](_0xf556[888],_0xf556[898],_0xde03x2e[_0xf556[744]][_0xf556[899]])[_0xf556[784]](_0xf556[888],_0xf556[896],_0xde03x2e[_0xf556[744]][_0xf556[897]])[_0xf556[784]](_0xf556[888],_0xf556[894],_0xde03x2e[_0xf556[744]][_0xf556[895]])[_0xf556[784]](_0xf556[888],_0xf556[892],_0xde03x2e[_0xf556[744]][_0xf556[893]])[_0xf556[784]](_0xf556[888],_0xf556[890],_0xde03x2e[_0xf556[744]][_0xf556[891]])[_0xf556[784]](_0xf556[888],_0xf556[889],function (){return false;} );this[_0xf556[900]]();this[_0xf556[903]](this[_0xf556[737]][_0xf556[901]],_0xf556[902]);this[_0xf556[903]](this[_0xf556[737]][_0xf556[904]],_0xf556[905]);this[_0xf556[906]]();} ,updateCalendarHeader:function (_0xde03x34,_0xde03x35,_0xde03x36){var _0xde03x37,_0xde03x38;_0xde03x34[_0xf556[746]](_0xf556[908])[_0xf556[907]](BFHMonthsList[_0xde03x35]);_0xde03x34[_0xf556[746]](_0xf556[909])[_0xf556[907]](_0xde03x36);_0xde03x37=_0xde03x34[_0xf556[746]](_0xf556[910]);_0xde03x37[_0xf556[781]](_0xf556[766]);for(_0xde03x38=BFHDayOfWeekStart;_0xde03x38<BFHDaysList[_0xf556[821]];_0xde03x38=_0xde03x38+1){_0xde03x37[_0xf556[912]](_0xf556[911]+BFHDaysList[_0xde03x38]+_0xf556[880]);} ;for(_0xde03x38=0;_0xde03x38<BFHDayOfWeekStart;_0xde03x38=_0xde03x38+1){_0xde03x37[_0xf556[912]](_0xf556[911]+BFHDaysList[_0xde03x38]+_0xf556[880]);} ;} ,checkMinDate:function (_0xde03x38,_0xde03x35,_0xde03x36){var _0xde03x39,_0xde03x3a,_0xde03x3b,_0xde03x3c;_0xde03x39=this[_0xf556[742]][_0xf556[796]](_0xf556[913]);if(_0xde03x39===true){_0xde03x3a=this[_0xf556[742]][_0xf556[796]](_0xf556[914]);_0xde03x3b=this[_0xf556[742]][_0xf556[796]](_0xf556[915]);_0xde03x3c=this[_0xf556[742]][_0xf556[796]](_0xf556[916]);if((_0xde03x38<_0xde03x3a&&_0xde03x35===_0xde03x3b&&_0xde03x36===_0xde03x3c)||(_0xde03x35<_0xde03x3b&&_0xde03x36===_0xde03x3c)||(_0xde03x36<_0xde03x3c)){return true;} ;} ;return false;} ,checkMaxDate:function (_0xde03x38,_0xde03x35,_0xde03x36){var _0xde03x3d,_0xde03x3e,_0xde03x3f,_0xde03x40;_0xde03x3d=this[_0xf556[742]][_0xf556[796]](_0xf556[917]);if(_0xde03x3d===true){_0xde03x3e=this[_0xf556[742]][_0xf556[796]](_0xf556[918]);_0xde03x3f=this[_0xf556[742]][_0xf556[796]](_0xf556[919]);_0xde03x40=this[_0xf556[742]][_0xf556[796]](_0xf556[920]);if((_0xde03x38>_0xde03x3e&&_0xde03x35===_0xde03x3f&&_0xde03x36===_0xde03x40)||(_0xde03x35>_0xde03x3f&&_0xde03x36===_0xde03x40)||(_0xde03x36>_0xde03x40)){return true;} ;} ;return false;} ,checkToday:function (_0xde03x38,_0xde03x35,_0xde03x36){var _0xde03x30;_0xde03x30= new Date();if(_0xde03x38===_0xde03x30[_0xf556[858]]()&&_0xde03x35===_0xde03x30[_0xf556[856]]()&&_0xde03x36===_0xde03x30[_0xf556[857]]()){return true;} ;return false;} ,updateCalendarDays:function (_0xde03x34,_0xde03x35,_0xde03x36){var _0xde03x41,_0xde03x42,_0xde03x43,_0xde03x44,_0xde03x45,_0xde03x46,_0xde03x38;_0xde03x41=_0xde03x34[_0xf556[746]](_0xf556[921])[_0xf556[781]](_0xf556[766]);_0xde03x42=_0xde03x48(_0xde03x35,_0xde03x36);_0xde03x43=_0xde03x48(_0xde03x35+1,_0xde03x36);_0xde03x44=_0xde03x49(_0xde03x35,_0xde03x36,1);_0xde03x45=_0xde03x49(_0xde03x35,_0xde03x36,_0xde03x43);_0xde03x46=_0xf556[766];for(_0xde03x38=0;_0xde03x38<(_0xde03x44-BFHDayOfWeekStart+7)%7;_0xde03x38=_0xde03x38+1){_0xde03x46+=_0xf556[922]+(_0xde03x42-(_0xde03x44-BFHDayOfWeekStart+7)%7+_0xde03x38+1)+_0xf556[923];} ;for(_0xde03x38=1;_0xde03x38<=_0xde03x43;_0xde03x38=_0xde03x38+1){if(this[_0xf556[924]](_0xde03x38,_0xde03x35,_0xde03x36)){_0xde03x46+=_0xf556[925]+_0xde03x38+_0xf556[926]+_0xde03x38+_0xf556[923];} else {if(this[_0xf556[927]](_0xde03x38,_0xde03x35,_0xde03x36)){_0xde03x46+=_0xf556[925]+_0xde03x38+_0xf556[926]+_0xde03x38+_0xf556[923];} else {if(this[_0xf556[928]](_0xde03x38,_0xde03x35,_0xde03x36)){_0xde03x46+=_0xf556[925]+_0xde03x38+_0xf556[929]+_0xde03x38+_0xf556[923];} else {_0xde03x46+=_0xf556[925]+_0xde03x38+_0xf556[930]+_0xde03x38+_0xf556[923];} ;} ;} ;if(_0xde03x49(_0xde03x35,_0xde03x36,_0xde03x38)===(6+BFHDayOfWeekStart)%7){_0xde03x41[_0xf556[912]](_0xf556[931]+_0xde03x46+_0xf556[882]);_0xde03x46=_0xf556[766];} ;} ;for(_0xde03x38=1;_0xde03x38<=(7-((_0xde03x45+1-BFHDayOfWeekStart+7)%7))%7+1;_0xde03x38=_0xde03x38+1){_0xde03x46+=_0xf556[922]+_0xde03x38+_0xf556[923];if(_0xde03x38===(7-((_0xde03x45+1-BFHDayOfWeekStart+7)%7))%7){_0xde03x41[_0xf556[912]](_0xf556[931]+_0xde03x46+_0xf556[882]);} ;} ;} ,updateCalendar:function (){var _0xde03x34,_0xde03x35,_0xde03x36;_0xde03x34=this[_0xf556[742]][_0xf556[746]](_0xf556[932]);_0xde03x35=this[_0xf556[742]][_0xf556[796]](_0xf556[859]);_0xde03x36=this[_0xf556[742]][_0xf556[796]](_0xf556[860]);this[_0xf556[933]](_0xde03x34,_0xde03x35,_0xde03x36);this[_0xf556[934]](_0xde03x34,_0xde03x35,_0xde03x36);} ,previousMonth:function (){var _0xde03x1b,_0xde03x1c,_0xde03x47;_0xde03x1b=_0xde03x9(this);_0xde03x1c=_0xde03x26(_0xde03x1b);if(Number(_0xde03x1c[_0xf556[796]](_0xf556[859]))===0){_0xde03x1c[_0xf556[796]](_0xf556[859],11);_0xde03x1c[_0xf556[796]](_0xf556[860],Number(_0xde03x1c[_0xf556[796]](_0xf556[860]))-1);} else {_0xde03x1c[_0xf556[796]](_0xf556[859],Number(_0xde03x1c[_0xf556[796]](_0xf556[859]))-1);} ;_0xde03x47=_0xde03x1c[_0xf556[796]](_0xf556[851]);_0xde03x47[_0xf556[906]]();return false;} ,nextMonth:function (){var _0xde03x1b,_0xde03x1c,_0xde03x47;_0xde03x1b=_0xde03x9(this);_0xde03x1c=_0xde03x26(_0xde03x1b);if(Number(_0xde03x1c[_0xf556[796]](_0xf556[859]))===11){_0xde03x1c[_0xf556[796]](_0xf556[859],0);_0xde03x1c[_0xf556[796]](_0xf556[860],Number(_0xde03x1c[_0xf556[796]](_0xf556[860]))+1);} else {_0xde03x1c[_0xf556[796]](_0xf556[859],Number(_0xde03x1c[_0xf556[796]](_0xf556[859]))+1);} ;_0xde03x47=_0xde03x1c[_0xf556[796]](_0xf556[851]);_0xde03x47[_0xf556[906]]();return false;} ,previousYear:function (){var _0xde03x1b,_0xde03x1c,_0xde03x47;_0xde03x1b=_0xde03x9(this);_0xde03x1c=_0xde03x26(_0xde03x1b);_0xde03x1c[_0xf556[796]](_0xf556[860],Number(_0xde03x1c[_0xf556[796]](_0xf556[860]))-1);_0xde03x47=_0xde03x1c[_0xf556[796]](_0xf556[851]);_0xde03x47[_0xf556[906]]();return false;} ,nextYear:function (){var _0xde03x1b,_0xde03x1c,_0xde03x47;_0xde03x1b=_0xde03x9(this);_0xde03x1c=_0xde03x26(_0xde03x1b);_0xde03x1c[_0xf556[796]](_0xf556[860],Number(_0xde03x1c[_0xf556[796]](_0xf556[860]))+1);_0xde03x47=_0xde03x1c[_0xf556[796]](_0xf556[851]);_0xde03x47[_0xf556[906]]();return false;} ,select:function (_0xde03x1a){var _0xde03x1b,_0xde03x1c,_0xde03x47,_0xde03x35,_0xde03x36,_0xde03x38;_0xde03x1b=_0xde03x9(this);_0xde03x1a[_0xf556[935]]();_0xde03x1a[_0xf556[936]]();_0xde03x1c=_0xde03x26(_0xde03x1b);_0xde03x47=_0xde03x1c[_0xf556[796]](_0xf556[851]);_0xde03x35=_0xde03x1c[_0xf556[796]](_0xf556[859]);_0xde03x36=_0xde03x1c[_0xf556[796]](_0xf556[860]);_0xde03x38=_0xde03x1b[_0xf556[796]](_0xf556[864]);_0xde03x1c[_0xf556[790]](_0xde03x4a(_0xde03x47[_0xf556[737]][_0xf556[854]],_0xde03x35,_0xde03x36,_0xde03x38));_0xde03x1c[_0xf556[798]](_0xf556[937]);if(_0xde03x47[_0xf556[737]][_0xf556[809]]===true){_0xde03x25();} ;} ,toggle:function (_0xde03x1a){var _0xde03x1b,_0xde03x1c,_0xde03x1d;_0xde03x1b=_0xde03x9(this);_0xde03x1c=_0xde03x26(_0xde03x1b);if(_0xde03x1c[_0xf556[811]](_0xf556[810])||_0xde03x1c[_0xf556[813]](_0xf556[812])!==undefined){return true;} ;_0xde03x1d=_0xde03x1c[_0xf556[815]](_0xf556[814]);_0xde03x25();if(!_0xde03x1d){_0xde03x1c[_0xf556[798]](_0xde03x1a=_0xde03x9.Event(_0xf556[938]));if(_0xde03x1a[_0xf556[817]]()){return true;} ;_0xde03x1c[_0xf556[819]](_0xf556[814])[_0xf556[798]](_0xf556[939]);_0xde03x1b[_0xf556[820]]();} ;return false;} };function _0xde03x48(_0xde03x35,_0xde03x36){return  new Date(_0xde03x36,_0xde03x35,0)[_0xf556[858]]();} ;function _0xde03x49(_0xde03x35,_0xde03x36,_0xde03x38){return  new Date(_0xde03x36,_0xde03x35,_0xde03x38)[_0xf556[940]]();} ;function _0xde03x4a(_0xde03x31,_0xde03x35,_0xde03x36,_0xde03x38){_0xde03x35+=1;_0xde03x35=String(_0xde03x35);_0xde03x38=String(_0xde03x38);if(_0xde03x35[_0xf556[821]]===1){_0xde03x35=_0xf556[822]+_0xde03x35;} ;if(_0xde03x38[_0xf556[821]]===1){_0xde03x38=_0xf556[822]+_0xde03x38;} ;return _0xde03x31[_0xf556[941]](_0xf556[861],_0xde03x35)[_0xf556[941]](_0xf556[862],_0xde03x36)[_0xf556[941]](_0xf556[865],_0xde03x38);} ;function _0xde03x4b(_0xde03x31,_0xde03x2f,_0xde03x4c){var _0xde03x4d,_0xde03x4e,_0xde03x4f;_0xde03x4d=[{"\x70\x61\x72\x74":_0xf556[861],"\x70\x6F\x73\x69\x74\x69\x6F\x6E":_0xde03x31[_0xf556[942]](_0xf556[861])},{"\x70\x61\x72\x74":_0xf556[862],"\x70\x6F\x73\x69\x74\x69\x6F\x6E":_0xde03x31[_0xf556[942]](_0xf556[862])},{"\x70\x61\x72\x74":_0xf556[865],"\x70\x6F\x73\x69\x74\x69\x6F\x6E":_0xde03x31[_0xf556[942]](_0xf556[865])}];_0xde03x4d[_0xf556[944]](function (_0xde03x50,_0xde03x24){return _0xde03x50[_0xf556[943]]-_0xde03x24[_0xf556[943]];} );_0xde03x4f=_0xde03x2f[_0xf556[945]](/(\d+)/g);for(_0xde03x4e in _0xde03x4d){if(_0xde03x4d[_0xf556[946]](_0xde03x4e)){if(_0xde03x4d[_0xde03x4e][_0xf556[947]]===_0xde03x4c){return Number(_0xde03x4f[_0xde03x4e]).toString();} ;} ;} ;} ;function _0xde03x25(){var _0xde03x1c;_0xde03x9(_0xde03xa)[_0xf556[827]](function (_0xde03x1a){_0xde03x1c=_0xde03x26(_0xde03x9(this));if(!_0xde03x1c[_0xf556[815]](_0xf556[814])){return true;} ;_0xde03x1c[_0xf556[798]](_0xde03x1a=_0xde03x9.Event(_0xf556[948]));if(_0xde03x1a[_0xf556[817]]()){return true;} ;_0xde03x1c[_0xf556[826]](_0xf556[814])[_0xf556[798]](_0xf556[949]);} );} ;function _0xde03x26(_0xde03x1b){return _0xde03x1b[_0xf556[829]](_0xf556[950]);} ;var _0xde03x27=_0xde03x9[_0xf556[740]][_0xf556[851]];_0xde03x9[_0xf556[740]][_0xf556[851]]=function (_0xde03x28){return this[_0xf556[827]](function (){var _0xde03x1b,_0xde03x29,_0xde03xd;_0xde03x1b=_0xde03x9(this);_0xde03x29=_0xde03x1b[_0xf556[796]](_0xf556[851]);_0xde03xd= typeof _0xde03x28===_0xf556[830]&&_0xde03x28;this[_0xf556[831]]=_0xf556[851];if(!_0xde03x29){_0xde03x1b[_0xf556[796]](_0xf556[851],(_0xde03x29= new _0xde03x2e(this,_0xde03xd)));} ;if( typeof _0xde03x28===_0xf556[832]){_0xde03x29[_0xde03x28][_0xf556[833]](_0xde03x1b);} ;} );} ;_0xde03x9[_0xf556[740]][_0xf556[851]][_0xf556[834]]=_0xde03x2e;_0xde03x9[_0xf556[740]][_0xf556[851]][_0xf556[738]]={icon:_0xf556[951],align:_0xf556[791],input:_0xf556[835],placeholder:_0xf556[766],name:_0xf556[766],date:_0xf556[855],format:_0xf556[952],min:_0xf556[766],max:_0xf556[766],close:true};_0xde03x9[_0xf556[740]][_0xf556[851]][_0xf556[837]]=function (){_0xde03x9[_0xf556[740]][_0xf556[851]]=_0xde03x27;return this;} ;var _0xde03x2a;if(_0xde03x9[_0xf556[839]][_0xf556[838]]){_0xde03x2a=_0xde03x9[_0xf556[839]][_0xf556[838]];} ;_0xde03x9[_0xf556[839]][_0xf556[838]]={get:function (_0xde03x2b){if(_0xde03x9(_0xde03x2b)[_0xf556[815]](_0xf556[953])){return _0xde03x9(_0xde03x2b)[_0xf556[746]](_0xf556[841])[_0xf556[790]]();} else {if(_0xde03x2a){return _0xde03x2a[_0xf556[842]](_0xde03x2b);} ;} ;} ,set:function (_0xde03x2b,_0xde03x2c){if(_0xde03x9(_0xde03x2b)[_0xf556[815]](_0xf556[953])){_0xde03x9(_0xde03x2b)[_0xf556[746]](_0xf556[841])[_0xf556[790]](_0xde03x2c);} else {if(_0xde03x2a){return _0xde03x2a[_0xf556[846]](_0xde03x2b,_0xde03x2c);} ;} ;} };_0xde03x9(document)[_0xf556[848]](function (){_0xde03x9(_0xf556[954])[_0xf556[827]](function (){var _0xde03x51;_0xde03x51=_0xde03x9(this);_0xde03x51[_0xf556[851]](_0xde03x51[_0xf556[796]]());} );} );_0xde03x9(document)[_0xf556[784]](_0xf556[955],_0xde03x25);} (window[_0xf556[734]]);+function (_0xde03x9){_0xf556[735];var _0xde03x52=function (_0xde03xc,_0xde03xd){this[_0xf556[737]]=_0xde03x9[_0xf556[741]]({},_0xde03x9[_0xf556[740]][_0xf556[956]][_0xf556[738]],_0xde03xd);this[_0xf556[742]]=_0xde03x9(_0xde03xc);if(this[_0xf556[742]][_0xf556[811]](_0xf556[891])){this[_0xf556[957]]();} ;if(this[_0xf556[742]][_0xf556[815]](_0xf556[958])){this[_0xf556[959]]();} ;} ;_0xde03x52[_0xf556[744]]={constructor:_0xde03x52,getFonts:function (){var _0xde03x53,_0xde03x54;if(this[_0xf556[737]][_0xf556[960]]){_0xde03x54=[];this[_0xf556[737]][_0xf556[960]]=this[_0xf556[737]][_0xf556[960]][_0xf556[962]](_0xf556[961]);for(_0xde03x53 in BFHFontsList){if(BFHFontsList[_0xf556[946]](_0xde03x53)){if(_0xde03x9[_0xf556[963]](_0xde03x53,this[_0xf556[737]][_0xf556[960]])>=0){_0xde03x54[_0xde03x53]=BFHFontsList[_0xde03x53];} ;} ;} ;return _0xde03x54;} else {return BFHFontsList;} ;} ,addFonts:function (){var _0xde03x55,_0xde03x53,_0xde03x54;_0xde03x55=this[_0xf556[737]][_0xf556[964]];_0xde03x54=this[_0xf556[965]]();this[_0xf556[742]][_0xf556[781]](_0xf556[766]);if(this[_0xf556[737]][_0xf556[966]]===true){this[_0xf556[742]][_0xf556[912]](_0xf556[967]);} ;for(_0xde03x53 in _0xde03x54){if(_0xde03x54[_0xf556[946]](_0xde03x53)){this[_0xf556[742]][_0xf556[912]](_0xf556[968]+_0xde03x53+_0xf556[930]+_0xde03x53+_0xf556[969]);} ;} ;this[_0xf556[742]][_0xf556[790]](_0xde03x55);} ,addBootstrapFonts:function (){var _0xde03x56,_0xde03x57,_0xde03x58,_0xde03x55,_0xde03x53,_0xde03x54;_0xde03x55=this[_0xf556[737]][_0xf556[964]];_0xde03x56=this[_0xf556[742]][_0xf556[746]](_0xf556[970]);_0xde03x57=this[_0xf556[742]][_0xf556[746]](_0xf556[971]);_0xde03x58=this[_0xf556[742]][_0xf556[746]](_0xf556[972]);_0xde03x54=this[_0xf556[965]]();_0xde03x58[_0xf556[781]](_0xf556[766]);if(this[_0xf556[737]][_0xf556[966]]===true){_0xde03x58[_0xf556[912]](_0xf556[973]);} ;for(_0xde03x53 in _0xde03x54){if(_0xde03x54[_0xf556[946]](_0xde03x53)){_0xde03x58[_0xf556[912]](_0xf556[974]+_0xde03x54[_0xde03x53]+_0xf556[975]+_0xde03x53+_0xf556[930]+_0xde03x53+_0xf556[976]);} ;} ;this[_0xf556[742]][_0xf556[790]](_0xde03x55);} };var _0xde03x27=_0xde03x9[_0xf556[740]][_0xf556[956]];_0xde03x9[_0xf556[740]][_0xf556[956]]=function (_0xde03x28){return this[_0xf556[827]](function (){var _0xde03x1b,_0xde03x29,_0xde03xd;_0xde03x1b=_0xde03x9(this);_0xde03x29=_0xde03x1b[_0xf556[796]](_0xf556[956]);_0xde03xd= typeof _0xde03x28===_0xf556[830]&&_0xde03x28;if(!_0xde03x29){_0xde03x1b[_0xf556[796]](_0xf556[956],(_0xde03x29= new _0xde03x52(this,_0xde03xd)));} ;if( typeof _0xde03x28===_0xf556[832]){_0xde03x29[_0xde03x28][_0xf556[833]](_0xde03x1b);} ;} );} ;_0xde03x9[_0xf556[740]][_0xf556[956]][_0xf556[834]]=_0xde03x52;_0xde03x9[_0xf556[740]][_0xf556[956]][_0xf556[738]]={font:_0xf556[766],available:_0xf556[766],blank:true};_0xde03x9[_0xf556[740]][_0xf556[956]][_0xf556[837]]=function (){_0xde03x9[_0xf556[740]][_0xf556[956]]=_0xde03x27;return this;} ;_0xde03x9(document)[_0xf556[848]](function (){_0xde03x9(_0xf556[978])[_0xf556[827]](function (){var _0xde03x59;_0xde03x59=_0xde03x9(this);if(_0xde03x59[_0xf556[815]](_0xf556[958])){_0xde03x59[_0xf556[977]](_0xde03x59[_0xf556[796]]());} ;_0xde03x59[_0xf556[956]](_0xde03x59[_0xf556[796]]());} );} );} (window[_0xf556[734]]);+function (_0xde03x9){_0xf556[735];var _0xde03x5a=function (_0xde03xc,_0xde03xd){this[_0xf556[737]]=_0xde03x9[_0xf556[741]]({},_0xde03x9[_0xf556[740]][_0xf556[979]][_0xf556[738]],_0xde03xd);this[_0xf556[742]]=_0xde03x9(_0xde03xc);if(this[_0xf556[742]][_0xf556[811]](_0xf556[891])){this[_0xf556[980]]();} ;if(this[_0xf556[742]][_0xf556[815]](_0xf556[958])){this[_0xf556[981]]();} ;} ;_0xde03x5a[_0xf556[744]]={constructor:_0xde03x5a,getFontsizes:function (){var _0xde03x5b,_0xde03x5c;if(this[_0xf556[737]][_0xf556[960]]){_0xde03x5c=[];this[_0xf556[737]][_0xf556[960]]=this[_0xf556[737]][_0xf556[960]][_0xf556[962]](_0xf556[961]);for(_0xde03x5b in BFHFontSizesList){if(BFHFontSizesList[_0xf556[946]](_0xde03x5b)){if(_0xde03x9[_0xf556[963]](_0xde03x5b,this[_0xf556[737]][_0xf556[960]])>=0){_0xde03x5c[_0xde03x5b]=BFHFontSizesList[_0xde03x5b];} ;} ;} ;return _0xde03x5c;} else {return BFHFontSizesList;} ;} ,addFontSizes:function (){var _0xde03x55,_0xde03x5b,_0xde03x5c;_0xde03x55=this[_0xf556[737]][_0xf556[982]];_0xde03x5c=this[_0xf556[983]]();this[_0xf556[742]][_0xf556[781]](_0xf556[766]);if(this[_0xf556[737]][_0xf556[966]]===true){this[_0xf556[742]][_0xf556[912]](_0xf556[967]);} ;for(_0xde03x5b in _0xde03x5c){if(_0xde03x5c[_0xf556[946]](_0xde03x5b)){this[_0xf556[742]][_0xf556[912]](_0xf556[968]+_0xde03x5b+_0xf556[930]+_0xde03x5c[_0xde03x5b]+_0xf556[969]);} ;} ;this[_0xf556[742]][_0xf556[790]](_0xde03x55);} ,addBootstrapFontSizes:function (){var _0xde03x56,_0xde03x57,_0xde03x58,_0xde03x55,_0xde03x5b,_0xde03x5c;_0xde03x55=this[_0xf556[737]][_0xf556[982]];_0xde03x56=this[_0xf556[742]][_0xf556[746]](_0xf556[970]);_0xde03x57=this[_0xf556[742]][_0xf556[746]](_0xf556[971]);_0xde03x58=this[_0xf556[742]][_0xf556[746]](_0xf556[972]);_0xde03x5c=this[_0xf556[983]]();_0xde03x58[_0xf556[781]](_0xf556[766]);if(this[_0xf556[737]][_0xf556[966]]===true){_0xde03x58[_0xf556[912]](_0xf556[973]);} ;for(_0xde03x5b in _0xde03x5c){if(_0xde03x5c[_0xf556[946]](_0xde03x5b)){_0xde03x58[_0xf556[912]](_0xf556[984]+_0xde03x5b+_0xf556[930]+_0xde03x5c[_0xde03x5b]+_0xf556[976]);} ;} ;this[_0xf556[742]][_0xf556[790]](_0xde03x55);} };var _0xde03x27=_0xde03x9[_0xf556[740]][_0xf556[979]];_0xde03x9[_0xf556[740]][_0xf556[979]]=function (_0xde03x28){return this[_0xf556[827]](function (){var _0xde03x1b,_0xde03x29,_0xde03xd;_0xde03x1b=_0xde03x9(this);_0xde03x29=_0xde03x1b[_0xf556[796]](_0xf556[979]);_0xde03xd= typeof _0xde03x28===_0xf556[830]&&_0xde03x28;if(!_0xde03x29){_0xde03x1b[_0xf556[796]](_0xf556[979],(_0xde03x29= new _0xde03x5a(this,_0xde03xd)));} ;if( typeof _0xde03x28===_0xf556[832]){_0xde03x29[_0xde03x28][_0xf556[833]](_0xde03x1b);} ;} );} ;_0xde03x9[_0xf556[740]][_0xf556[979]][_0xf556[834]]=_0xde03x5a;_0xde03x9[_0xf556[740]][_0xf556[979]][_0xf556[738]]={fontsize:_0xf556[766],available:_0xf556[766],blank:true};_0xde03x9[_0xf556[740]][_0xf556[979]][_0xf556[837]]=function (){_0xde03x9[_0xf556[740]][_0xf556[979]]=_0xde03x27;return this;} ;_0xde03x9(document)[_0xf556[848]](function (){_0xde03x9(_0xf556[985])[_0xf556[827]](function (){var _0xde03x5d;_0xde03x5d=_0xde03x9(this);if(_0xde03x5d[_0xf556[815]](_0xf556[958])){_0xde03x5d[_0xf556[977]](_0xde03x5d[_0xf556[796]]());} ;_0xde03x5d[_0xf556[979]](_0xde03x5d[_0xf556[796]]());} );} );} (window[_0xf556[734]]);+function (_0xde03x9){_0xf556[735];var _0xde03x5e=function (_0xde03xc,_0xde03xd){this[_0xf556[737]]=_0xde03x9[_0xf556[741]]({},_0xde03x9[_0xf556[740]][_0xf556[986]][_0xf556[738]],_0xde03xd);this[_0xf556[742]]=_0xde03x9(_0xde03xc);if(this[_0xf556[742]][_0xf556[811]](_0xf556[891])){this[_0xf556[957]]();} ;if(this[_0xf556[742]][_0xf556[815]](_0xf556[958])){this[_0xf556[959]]();} ;} ;_0xde03x5e[_0xf556[744]]={constructor:_0xde03x5e,getFonts:function (){var _0xde03x53,_0xde03x54;_0xde03x54=[];if(this[_0xf556[737]][_0xf556[987]]){for(_0xde03x53 in BFHGoogleFontsList[_0xf556[988]]){if(BFHGoogleFontsList[_0xf556[988]][_0xf556[946]](_0xde03x53)){if(_0xde03x9[_0xf556[963]](this[_0xf556[737]][_0xf556[987]],BFHGoogleFontsList[_0xf556[988]][_0xde03x53][_0xf556[989]])>=0){_0xde03x54[BFHGoogleFontsList[_0xf556[988]][_0xde03x53][_0xf556[990]]]={"\x69\x6E\x66\x6F":BFHGoogleFontsList[_0xf556[988]][_0xde03x53],"\x69\x6E\x64\x65\x78":parseInt(_0xde03x53,10)};} ;} ;} ;} else {if(this[_0xf556[737]][_0xf556[960]]){this[_0xf556[737]][_0xf556[960]]=this[_0xf556[737]][_0xf556[960]][_0xf556[962]](_0xf556[961]);for(_0xde03x53 in BFHGoogleFontsList[_0xf556[988]]){if(BFHGoogleFontsList[_0xf556[988]][_0xf556[946]](_0xde03x53)){if(_0xde03x9[_0xf556[963]](BFHGoogleFontsList[_0xf556[988]][_0xde03x53][_0xf556[990]],this[_0xf556[737]][_0xf556[960]])>=0){_0xde03x54[BFHGoogleFontsList[_0xf556[988]][_0xde03x53][_0xf556[990]]]={"\x69\x6E\x66\x6F":BFHGoogleFontsList[_0xf556[988]][_0xde03x53],"\x69\x6E\x64\x65\x78":parseInt(_0xde03x53,10)};} ;} ;} ;} else {for(_0xde03x53 in BFHGoogleFontsList[_0xf556[988]]){if(BFHGoogleFontsList[_0xf556[988]][_0xf556[946]](_0xde03x53)){_0xde03x54[BFHGoogleFontsList[_0xf556[988]][_0xde03x53][_0xf556[990]]]={"\x69\x6E\x66\x6F":BFHGoogleFontsList[_0xf556[988]][_0xde03x53],"\x69\x6E\x64\x65\x78":parseInt(_0xde03x53,10)};} ;} ;} ;} ;return _0xde03x54;} ,addFonts:function (){var _0xde03x55,_0xde03x53,_0xde03x54;_0xde03x55=this[_0xf556[737]][_0xf556[964]];_0xde03x54=this[_0xf556[965]]();this[_0xf556[742]][_0xf556[781]](_0xf556[766]);if(this[_0xf556[737]][_0xf556[966]]===true){this[_0xf556[742]][_0xf556[912]](_0xf556[967]);} ;for(_0xde03x53 in _0xde03x54){if(_0xde03x54[_0xf556[946]](_0xde03x53)){this[_0xf556[742]][_0xf556[912]](_0xf556[968]+_0xde03x54[_0xde03x53][_0xf556[991]][_0xf556[990]]+_0xf556[930]+_0xde03x54[_0xde03x53][_0xf556[991]][_0xf556[990]]+_0xf556[969]);} ;} ;this[_0xf556[742]][_0xf556[790]](_0xde03x55);} ,addBootstrapFonts:function (){var _0xde03x56,_0xde03x57,_0xde03x58,_0xde03x55,_0xde03x53,_0xde03x54;_0xde03x55=this[_0xf556[737]][_0xf556[964]];_0xde03x56=this[_0xf556[742]][_0xf556[746]](_0xf556[970]);_0xde03x57=this[_0xf556[742]][_0xf556[746]](_0xf556[971]);_0xde03x58=this[_0xf556[742]][_0xf556[746]](_0xf556[972]);_0xde03x54=this[_0xf556[965]]();_0xde03x58[_0xf556[781]](_0xf556[766]);if(this[_0xf556[737]][_0xf556[966]]===true){_0xde03x58[_0xf556[912]](_0xf556[992]);} ;for(_0xde03x53 in _0xde03x54){if(_0xde03x54[_0xf556[946]](_0xde03x53)){_0xde03x58[_0xf556[912]](_0xf556[993]+((_0xde03x54[_0xde03x53][_0xf556[994]]*30)-2)+_0xf556[995]+_0xde03x54[_0xde03x53][_0xf556[991]][_0xf556[990]]+_0xf556[930]+_0xde03x54[_0xde03x53][_0xf556[991]][_0xf556[990]]+_0xf556[976]);} ;} ;this[_0xf556[742]][_0xf556[790]](_0xde03x55);} };var _0xde03x27=_0xde03x9[_0xf556[740]][_0xf556[986]];_0xde03x9[_0xf556[740]][_0xf556[986]]=function (_0xde03x28){return this[_0xf556[827]](function (){var _0xde03x1b,_0xde03x29,_0xde03xd;_0xde03x1b=_0xde03x9(this);_0xde03x29=_0xde03x1b[_0xf556[796]](_0xf556[986]);_0xde03xd= typeof _0xde03x28===_0xf556[830]&&_0xde03x28;if(!_0xde03x29){_0xde03x1b[_0xf556[796]](_0xf556[986],(_0xde03x29= new _0xde03x5e(this,_0xde03xd)));} ;if( typeof _0xde03x28===_0xf556[832]){_0xde03x29[_0xde03x28][_0xf556[833]](_0xde03x1b);} ;} );} ;_0xde03x9[_0xf556[740]][_0xf556[986]][_0xf556[834]]=_0xde03x5e;_0xde03x9[_0xf556[740]][_0xf556[986]][_0xf556[738]]={font:_0xf556[766],available:_0xf556[766],subset:_0xf556[766],blank:true};_0xde03x9[_0xf556[740]][_0xf556[986]][_0xf556[837]]=function (){_0xde03x9[_0xf556[740]][_0xf556[986]]=_0xde03x27;return this;} ;_0xde03x9(document)[_0xf556[848]](function (){_0xde03x9(_0xf556[996])[_0xf556[827]](function (){var _0xde03x5f;_0xde03x5f=_0xde03x9(this);if(_0xde03x5f[_0xf556[815]](_0xf556[958])){_0xde03x5f[_0xf556[977]](_0xde03x5f[_0xf556[796]]());} ;_0xde03x5f[_0xf556[986]](_0xde03x5f[_0xf556[796]]());} );} );} (window[_0xf556[734]]);+function (_0xde03x9){_0xf556[735];var _0xde03x60=function (_0xde03xc,_0xde03xd){this[_0xf556[737]]=_0xde03x9[_0xf556[741]]({},_0xde03x9[_0xf556[740]][_0xf556[997]][_0xf556[738]],_0xde03xd);this[_0xf556[742]]=_0xde03x9(_0xde03xc);this[_0xf556[998]]();} ;_0xde03x60[_0xf556[744]]={constructor:_0xde03x60,initInput:function (){var _0xde03x55;if(this[_0xf556[737]][_0xf556[999]]===true){this[_0xf556[742]][_0xf556[1001]](_0xf556[1000]);this[_0xf556[742]][_0xf556[1003]]()[_0xf556[912]](_0xf556[1002]);this[_0xf556[742]][_0xf556[1003]]()[_0xf556[912]](_0xf556[1004]);} ;this[_0xf556[742]][_0xf556[784]](_0xf556[1005],_0xde03x60[_0xf556[744]][_0xf556[1006]]);if(this[_0xf556[737]][_0xf556[1007]]===true){this[_0xf556[742]][_0xf556[784]](_0xf556[1008],_0xde03x60[_0xf556[744]][_0xf556[1009]]);} ;if(this[_0xf556[737]][_0xf556[999]]===true){this[_0xf556[742]][_0xf556[1003]]()[_0xf556[784]](_0xf556[1010],_0xf556[1013],_0xde03x60[_0xf556[744]][_0xf556[1014]])[_0xf556[784]](_0xf556[1010],_0xf556[1011],_0xde03x60[_0xf556[744]][_0xf556[1012]]);} ;this[_0xf556[1015]]();} ,keydown:function (_0xde03x1a){var _0xde03x1b;_0xde03x1b=_0xde03x9(this)[_0xf556[796]](_0xf556[997]);if(_0xde03x1b[_0xf556[742]][_0xf556[811]](_0xf556[810])||_0xde03x1b[_0xf556[742]][_0xf556[813]](_0xf556[812])!==undefined){return true;} ;switch(_0xde03x1a[_0xf556[1018]]){case 38:_0xde03x1b[_0xf556[1016]]();break ;;case 40:_0xde03x1b[_0xf556[1017]]();break ;;default:;} ;return true;} ,mouseup:function (_0xde03x1a){var _0xde03x1b,_0xde03x61,_0xde03x62;_0xde03x1b=_0xde03x1a[_0xf556[796]][_0xf556[1019]];_0xde03x61=_0xde03x1b[_0xf556[742]][_0xf556[796]](_0xf556[1020]);_0xde03x62=_0xde03x1b[_0xf556[742]][_0xf556[796]](_0xf556[1021]);clearTimeout(_0xde03x61);clearInterval(_0xde03x62);} ,btninc:function (){var _0xde03x1b,_0xde03x61;_0xde03x1b=_0xde03x9(this)[_0xf556[1003]]()[_0xf556[746]](_0xf556[1022])[_0xf556[796]](_0xf556[997]);if(_0xde03x1b[_0xf556[742]][_0xf556[811]](_0xf556[810])||_0xde03x1b[_0xf556[742]][_0xf556[813]](_0xf556[812])!==undefined){return true;} ;_0xde03x1b[_0xf556[1016]]();_0xde03x61=setTimeout(function (){var _0xde03x62;_0xde03x62=setInterval(function (){_0xde03x1b[_0xf556[1016]]();} ,80);_0xde03x1b[_0xf556[742]][_0xf556[796]](_0xf556[1021],_0xde03x62);} ,750);_0xde03x1b[_0xf556[742]][_0xf556[796]](_0xf556[1020],_0xde03x61);_0xde03x9(document)[_0xf556[801]](_0xf556[1023],{btn:_0xde03x1b},_0xde03x60[_0xf556[744]][_0xf556[1023]]);return true;} ,btndec:function (){var _0xde03x1b,_0xde03x61;_0xde03x1b=_0xde03x9(this)[_0xf556[1003]]()[_0xf556[746]](_0xf556[1022])[_0xf556[796]](_0xf556[997]);if(_0xde03x1b[_0xf556[742]][_0xf556[811]](_0xf556[810])||_0xde03x1b[_0xf556[742]][_0xf556[813]](_0xf556[812])!==undefined){return true;} ;_0xde03x1b[_0xf556[1017]]();_0xde03x61=setTimeout(function (){var _0xde03x62;_0xde03x62=setInterval(function (){_0xde03x1b[_0xf556[1017]]();} ,80);_0xde03x1b[_0xf556[742]][_0xf556[796]](_0xf556[1021],_0xde03x62);} ,750);_0xde03x1b[_0xf556[742]][_0xf556[796]](_0xf556[1020],_0xde03x61);_0xde03x9(document)[_0xf556[801]](_0xf556[1023],{btn:_0xde03x1b},_0xde03x60[_0xf556[744]][_0xf556[1023]]);return true;} ,change:function (){var _0xde03x1b;_0xde03x1b=_0xde03x9(this)[_0xf556[796]](_0xf556[997]);if(_0xde03x1b[_0xf556[742]][_0xf556[811]](_0xf556[810])||_0xde03x1b[_0xf556[742]][_0xf556[813]](_0xf556[812])!==undefined){return true;} ;_0xde03x1b[_0xf556[1015]]();return true;} ,increment:function (){var _0xde03x55;_0xde03x55=this[_0xf556[1024]]();_0xde03x55=_0xde03x55+1;this[_0xf556[742]][_0xf556[790]](_0xde03x55)[_0xf556[1006]]();} ,decrement:function (){var _0xde03x55;_0xde03x55=this[_0xf556[1024]]();_0xde03x55=_0xde03x55-1;this[_0xf556[742]][_0xf556[790]](_0xde03x55)[_0xf556[1006]]();} ,getValue:function (){var _0xde03x55;_0xde03x55=this[_0xf556[742]][_0xf556[790]]();if(_0xde03x55!==_0xf556[1025]){_0xde03x55=String(_0xde03x55)[_0xf556[941]](/\D/g,_0xf556[766]);} ;if(String(_0xde03x55)[_0xf556[821]]===0){_0xde03x55=this[_0xf556[737]][_0xf556[901]];} ;return parseInt(_0xde03x55);} ,formatNumber:function (){var _0xde03x55,_0xde03x63,_0xde03x64,_0xde03x65;_0xde03x55=this[_0xf556[1024]]();if(_0xde03x55>this[_0xf556[737]][_0xf556[904]]){if(this[_0xf556[737]][_0xf556[1001]]===true){_0xde03x55=this[_0xf556[737]][_0xf556[901]];} else {_0xde03x55=this[_0xf556[737]][_0xf556[904]];} ;} ;if(_0xde03x55<this[_0xf556[737]][_0xf556[901]]){if(this[_0xf556[737]][_0xf556[1001]]===true){_0xde03x55=this[_0xf556[737]][_0xf556[904]];} else {_0xde03x55=this[_0xf556[737]][_0xf556[901]];} ;} ;if(this[_0xf556[737]][_0xf556[1026]]===true){_0xde03x63=String(this[_0xf556[737]][_0xf556[904]])[_0xf556[821]];_0xde03x64=String(_0xde03x55)[_0xf556[821]];for(_0xde03x65=_0xde03x64;_0xde03x65<_0xde03x63;_0xde03x65=_0xde03x65+1){_0xde03x55=_0xf556[822]+_0xde03x55;} ;} ;if(_0xde03x55!==this[_0xf556[742]][_0xf556[790]]()){this[_0xf556[742]][_0xf556[790]](_0xde03x55);} ;} };var _0xde03x27=_0xde03x9[_0xf556[740]][_0xf556[997]];_0xde03x9[_0xf556[740]][_0xf556[997]]=function (_0xde03x28){return this[_0xf556[827]](function (){var _0xde03x1b,_0xde03x29,_0xde03xd;_0xde03x1b=_0xde03x9(this);_0xde03x29=_0xde03x1b[_0xf556[796]](_0xf556[997]);_0xde03xd= typeof _0xde03x28===_0xf556[830]&&_0xde03x28;if(!_0xde03x29){_0xde03x1b[_0xf556[796]](_0xf556[997],(_0xde03x29= new _0xde03x60(this,_0xde03xd)));} ;if( typeof _0xde03x28===_0xf556[832]){_0xde03x29[_0xde03x28][_0xf556[833]](_0xde03x1b);} ;} );} ;_0xde03x9[_0xf556[740]][_0xf556[997]][_0xf556[834]]=_0xde03x60;_0xde03x9[_0xf556[740]][_0xf556[997]][_0xf556[738]]={min:0,max:9999,zeros:false,keyboard:true,buttons:true,wrap:false};_0xde03x9[_0xf556[740]][_0xf556[997]][_0xf556[837]]=function (){_0xde03x9[_0xf556[740]][_0xf556[997]]=_0xde03x27;return this;} ;_0xde03x9(document)[_0xf556[848]](function (){_0xde03x9(_0xf556[1027])[_0xf556[827]](function (){var _0xde03x66;_0xde03x66=_0xde03x9(this);_0xde03x66[_0xf556[997]](_0xde03x66[_0xf556[796]]());} );} );} (window[_0xf556[734]]);+function (_0xde03x9){_0xf556[735];var _0xde03xa=_0xf556[1028],_0xde03x67=function (_0xde03xc,_0xde03xd){this[_0xf556[737]]=_0xde03x9[_0xf556[741]]({},_0xde03x9[_0xf556[740]][_0xf556[977]][_0xf556[738]],_0xde03xd);this[_0xf556[742]]=_0xde03x9(_0xde03xc);this[_0xf556[1029]]();} ;_0xde03x67[_0xf556[744]]={constructor:_0xde03x67,initSelectBox:function (){var _0xde03xd;_0xde03xd=_0xf556[766];this[_0xf556[742]][_0xf556[746]](_0xf556[838])[_0xf556[827]](function (){_0xde03xd=_0xde03xd+_0xf556[984]+_0xde03x9(this)[_0xf556[796]](_0xf556[1030])+_0xf556[930]+_0xde03x9(this)[_0xf556[781]]()+_0xf556[976];} );this[_0xf556[742]][_0xf556[781]](_0xf556[1031]+this[_0xf556[737]][_0xf556[772]]+_0xf556[1032]+_0xf556[1033]+this[_0xf556[737]][_0xf556[774]]+_0xf556[1034]+_0xf556[1035]+_0xf556[1036]+this[_0xf556[737]][_0xf556[866]]+_0xf556[1037]+_0xf556[1038]+_0xf556[1039]+_0xf556[1040]+_0xf556[1041]+_0xf556[1042]+_0xf556[778]+_0xf556[778]);this[_0xf556[742]][_0xf556[746]](_0xf556[972])[_0xf556[781]](_0xde03xd);if(this[_0xf556[737]][_0xf556[1043]]===true){this[_0xf556[742]][_0xf556[746]](_0xf556[1046])[_0xf556[1045]](_0xf556[1044]);} ;this[_0xf556[742]][_0xf556[790]](this[_0xf556[737]][_0xf556[1030]]);this[_0xf556[742]][_0xf556[784]](_0xf556[1055],_0xde03xa,_0xde03x67[_0xf556[744]][_0xf556[787]])[_0xf556[784]](_0xf556[1053],_0xde03xa+_0xf556[1054],_0xde03x67[_0xf556[744]][_0xf556[1009]])[_0xf556[784]](_0xf556[1051],_0xf556[1050],_0xde03x67[_0xf556[744]][_0xf556[1052]])[_0xf556[784]](_0xf556[1049],_0xf556[1050],_0xde03x67[_0xf556[744]][_0xf556[891]])[_0xf556[784]](_0xf556[1049],_0xf556[1048],function (){return false;} )[_0xf556[784]](_0xf556[1047],_0xf556[1048],_0xde03x67[_0xf556[744]][_0xf556[1043]]);} ,toggle:function (_0xde03x1a){var _0xde03x1b,_0xde03x1c,_0xde03x1d;_0xde03x1b=_0xde03x9(this);_0xde03x1c=_0xde03x26(_0xde03x1b);if(_0xde03x1c[_0xf556[811]](_0xf556[810])||_0xde03x1c[_0xf556[813]](_0xf556[812])!==undefined){return true;} ;_0xde03x1d=_0xde03x1c[_0xf556[815]](_0xf556[814]);_0xde03x25();if(!_0xde03x1d){_0xde03x1c[_0xf556[798]](_0xde03x1a=_0xde03x9.Event(_0xf556[1056]));if(_0xde03x1a[_0xf556[817]]()){return true;} ;_0xde03x1c[_0xf556[819]](_0xf556[814])[_0xf556[798]](_0xf556[1059])[_0xf556[746]](_0xf556[1057]+_0xde03x1c[_0xf556[790]]()+_0xf556[1058])[_0xf556[820]]();} ;return false;} ,filter:function (){var _0xde03x1b,_0xde03x1c,_0xde03x68;_0xde03x1b=_0xde03x9(this);_0xde03x1c=_0xde03x26(_0xde03x1b);_0xde03x68=_0xde03x9(_0xf556[1060],_0xde03x1c);_0xde03x68[_0xf556[1063]]()[_0xf556[1043]](function (){return (_0xde03x9(this)[_0xf556[907]]()[_0xf556[1062]]()[_0xf556[942]](_0xde03x1b[_0xf556[790]]()[_0xf556[1062]]())!==-1);} )[_0xf556[1061]]();} ,keydown:function (_0xde03x1a){var _0xde03x1b,_0xde03x68,_0xde03x1c,_0xde03x69,_0xde03x1d,_0xde03x6a,_0xde03x6b;if(!/(38|40|27)/[_0xf556[1065]](_0xde03x1a[_0xf556[1064]])){return true;} ;_0xde03x1b=_0xde03x9(this);_0xde03x1a[_0xf556[935]]();_0xde03x1a[_0xf556[936]]();_0xde03x1c=_0xde03x26(_0xde03x1b);_0xde03x1d=_0xde03x1c[_0xf556[815]](_0xf556[814]);if(!_0xde03x1d||(_0xde03x1d&&_0xde03x1a[_0xf556[1064]]===27)){if(_0xde03x1a[_0xf556[1018]]===27){_0xde03x1c[_0xf556[746]](_0xde03xa)[_0xf556[820]]();} ;return _0xde03x1b[_0xf556[1066]]();} ;_0xde03x68=_0xde03x9(_0xf556[1067],_0xde03x1c);if(!_0xde03x68[_0xf556[821]]){return true;} ;_0xde03x9(_0xf556[1069])[_0xf556[808]](_0xf556[1068],_0xf556[1050],_0xde03x67[_0xf556[744]][_0xf556[1052]]);_0xde03x6a=_0xde03x68[_0xf556[994]](_0xde03x68[_0xf556[1043]](_0xf556[1070]));if(_0xde03x1a[_0xf556[1064]]===38&&_0xde03x6a>0){_0xde03x6a=_0xde03x6a-1;} ;if(_0xde03x1a[_0xf556[1064]]===40&&_0xde03x6a<_0xde03x68[_0xf556[821]]-1){_0xde03x6a=_0xde03x6a+1;} ;if(!_0xde03x6a){_0xde03x6a=0;} ;_0xde03x68[_0xf556[1071]](_0xde03x6a)[_0xf556[820]]();_0xde03x9(_0xf556[1069])[_0xf556[784]](_0xf556[1068],_0xf556[1050],_0xde03x67[_0xf556[744]][_0xf556[1052]]);} ,mouseenter:function (){var _0xde03x1b;_0xde03x1b=_0xde03x9(this);_0xde03x1b[_0xf556[820]]();} ,select:function (_0xde03x1a){var _0xde03x1b,_0xde03x1c,_0xde03x6c,_0xde03x56;_0xde03x1b=_0xde03x9(this);_0xde03x1a[_0xf556[935]]();_0xde03x1a[_0xf556[936]]();if(_0xde03x1b[_0xf556[811]](_0xf556[810])||_0xde03x1b[_0xf556[813]](_0xf556[812])!==undefined){return true;} ;_0xde03x1c=_0xde03x26(_0xde03x1b);_0xde03x1c[_0xf556[790]](_0xde03x1b[_0xf556[796]](_0xf556[1072]));_0xde03x1c[_0xf556[798]](_0xf556[1073]);_0xde03x25();} };function _0xde03x25(){var _0xde03x1c;_0xde03x9(_0xde03xa)[_0xf556[827]](function (_0xde03x1a){_0xde03x1c=_0xde03x26(_0xde03x9(this));if(!_0xde03x1c[_0xf556[815]](_0xf556[814])){return true;} ;_0xde03x1c[_0xf556[798]](_0xde03x1a=_0xde03x9.Event(_0xf556[1074]));if(_0xde03x1a[_0xf556[817]]()){return true;} ;_0xde03x1c[_0xf556[826]](_0xf556[814])[_0xf556[798]](_0xf556[1075]);} );} ;function _0xde03x26(_0xde03x1b){return _0xde03x1b[_0xf556[829]](_0xf556[1076]);} ;var _0xde03x27=_0xde03x9[_0xf556[740]][_0xf556[977]];_0xde03x9[_0xf556[740]][_0xf556[977]]=function (_0xde03x28){return this[_0xf556[827]](function (){var _0xde03x1b,_0xde03x29,_0xde03xd;_0xde03x1b=_0xde03x9(this);_0xde03x29=_0xde03x1b[_0xf556[796]](_0xf556[977]);_0xde03xd= typeof _0xde03x28===_0xf556[830]&&_0xde03x28;this[_0xf556[831]]=_0xf556[977];if(!_0xde03x29){_0xde03x1b[_0xf556[796]](_0xf556[977],(_0xde03x29= new _0xde03x67(this,_0xde03xd)));} ;if( typeof _0xde03x28===_0xf556[832]){_0xde03x29[_0xde03x28][_0xf556[833]](_0xde03x1b);} ;} );} ;_0xde03x9[_0xf556[740]][_0xf556[977]][_0xf556[834]]=_0xde03x67;_0xde03x9[_0xf556[740]][_0xf556[977]][_0xf556[738]]={icon:_0xf556[1077],input:_0xf556[835],name:_0xf556[766],value:_0xf556[766],filter:false};_0xde03x9[_0xf556[740]][_0xf556[977]][_0xf556[837]]=function (){_0xde03x9[_0xf556[740]][_0xf556[977]]=_0xde03x27;return this;} ;var _0xde03x2a;if(_0xde03x9[_0xf556[839]][_0xf556[838]]){_0xde03x2a=_0xde03x9[_0xf556[839]][_0xf556[838]];} ;_0xde03x9[_0xf556[839]][_0xf556[838]]={get:function (_0xde03x2b){if(_0xde03x9(_0xde03x2b)[_0xf556[815]](_0xf556[958])){return _0xde03x9(_0xde03x2b)[_0xf556[746]](_0xf556[970])[_0xf556[790]]();} else {if(_0xde03x2a){return _0xde03x2a[_0xf556[842]](_0xde03x2b);} ;} ;} ,set:function (_0xde03x2b,_0xde03x2c){var _0xde03x6d,_0xde03x6e;if(_0xde03x9(_0xde03x2b)[_0xf556[815]](_0xf556[958])){_0xde03x6d=_0xde03x9(_0xde03x2b);if(_0xde03x6d[_0xf556[746]](_0xf556[1078]+_0xde03x2c+_0xf556[1079])[_0xf556[821]]>0){_0xde03x6e=_0xde03x6d[_0xf556[746]](_0xf556[1078]+_0xde03x2c+_0xf556[1079])[_0xf556[781]]();} else {if(_0xde03x6d[_0xf556[746]](_0xf556[1080])[_0xf556[821]]>0){_0xde03x6e=_0xde03x6d[_0xf556[746]](_0xf556[1080])[_0xf556[1071]](0)[_0xf556[781]]();} else {_0xde03x2c=_0xf556[766];_0xde03x6e=_0xf556[766];} ;} ;_0xde03x6d[_0xf556[746]](_0xf556[970])[_0xf556[790]](_0xde03x2c);_0xde03x6d[_0xf556[746]](_0xf556[971])[_0xf556[781]](_0xde03x6e);} else {if(_0xde03x2a){return _0xde03x2a[_0xf556[846]](_0xde03x2b,_0xde03x2c);} ;} ;} };_0xde03x9(document)[_0xf556[848]](function (){_0xde03x9(_0xf556[1081])[_0xf556[827]](function (){var _0xde03x6f;_0xde03x6f=_0xde03x9(this);_0xde03x6f[_0xf556[977]](_0xde03x6f[_0xf556[796]]());} );} );_0xde03x9(document)[_0xf556[784]](_0xf556[1049],_0xde03x25);} (window[_0xf556[734]]);+function (_0xde03x9){_0xf556[735];var _0xde03x70=function (_0xde03xc,_0xde03xd){this[_0xf556[737]]=_0xde03x9[_0xf556[741]]({},_0xde03x9[_0xf556[740]][_0xf556[1082]][_0xf556[738]],_0xde03xd);this[_0xf556[742]]=_0xde03x9(_0xde03xc);this[_0xf556[1083]]();} ;_0xde03x70[_0xf556[744]]={constructor:_0xde03x70,initSlider:function (){if(this[_0xf556[737]][_0xf556[1030]]===_0xf556[766]){this[_0xf556[737]][_0xf556[1030]]=this[_0xf556[737]][_0xf556[901]];} ;this[_0xf556[742]][_0xf556[781]](_0xf556[1031]+this[_0xf556[737]][_0xf556[772]]+_0xf556[1032]+_0xf556[1084]);this[_0xf556[742]][_0xf556[746]](_0xf556[970])[_0xf556[790]](this[_0xf556[737]][_0xf556[1030]]);this[_0xf556[1085]](this[_0xf556[737]][_0xf556[1030]]);this[_0xf556[742]][_0xf556[784]](_0xf556[1086],_0xde03x70[_0xf556[744]][_0xf556[786]]);} ,updateHandle:function (_0xde03x2c){var _0xde03x13,_0xde03x71,_0xde03x72,_0xde03x73;_0xde03x73=this[_0xf556[737]][_0xf556[904]]-this[_0xf556[737]][_0xf556[901]];_0xde03x71=this[_0xf556[742]][_0xf556[749]]();_0xde03x72=this[_0xf556[742]][_0xf556[943]]()[_0xf556[791]];_0xde03x13=Math[_0xf556[794]]((_0xde03x2c-this[_0xf556[737]][_0xf556[901]])*(_0xde03x71-20)/_0xde03x73+_0xde03x72);this[_0xf556[742]][_0xf556[746]](_0xf556[1088])[_0xf556[844]](_0xf556[791],_0xde03x13+_0xf556[1087]);this[_0xf556[742]][_0xf556[746]](_0xf556[1089])[_0xf556[907]](_0xde03x2c);} ,updateVal:function (_0xde03x13){var _0xde03x71,_0xde03x72,_0xde03x74,_0xde03x2c,_0xde03x73;_0xde03x73=this[_0xf556[737]][_0xf556[904]]-this[_0xf556[737]][_0xf556[901]];_0xde03x71=this[_0xf556[742]][_0xf556[749]]();_0xde03x72=this[_0xf556[742]][_0xf556[792]]()[_0xf556[791]];_0xde03x74=_0xde03x72+_0xde03x71;if(_0xde03x13<_0xde03x72){_0xde03x13=_0xde03x72;} ;if(_0xde03x13+20>_0xde03x74){_0xde03x13=_0xde03x74;} ;_0xde03x2c=(_0xde03x13-_0xde03x72)/_0xde03x71;_0xde03x2c=Math[_0xf556[1090]](_0xde03x2c*_0xde03x73+this[_0xf556[737]][_0xf556[901]]);if(_0xde03x2c===this[_0xf556[742]][_0xf556[790]]()){return true;} ;this[_0xf556[742]][_0xf556[790]](_0xde03x2c);this[_0xf556[742]][_0xf556[798]](_0xf556[1091]);} ,mouseDown:function (){var _0xde03x1b;_0xde03x1b=_0xde03x9(this);if(_0xde03x1b[_0xf556[811]](_0xf556[810])||_0xde03x1b[_0xf556[813]](_0xf556[812])!==undefined){return true;} ;_0xde03x9(document)[_0xf556[784]](_0xf556[1093],{slider:_0xde03x1b},_0xde03x70[_0xf556[744]][_0xf556[803]])[_0xf556[801]](_0xf556[1092],{slider:_0xde03x1b},_0xde03x70[_0xf556[744]][_0xf556[800]]);} ,mouseMove:function (_0xde03x1a){var _0xde03x1b;_0xde03x1b=_0xde03x1a[_0xf556[796]][_0xf556[1094]];_0xde03x1b[_0xf556[796]](_0xf556[1082])[_0xf556[807]](_0xde03x1a[_0xf556[805]]);} ,mouseUp:function (_0xde03x1a){var _0xde03x1b;_0xde03x1b=_0xde03x1a[_0xf556[796]][_0xf556[1094]];_0xde03x1b[_0xf556[796]](_0xf556[1082])[_0xf556[807]](_0xde03x1a[_0xf556[805]]);_0xde03x9(document)[_0xf556[808]](_0xf556[1093]);} };var _0xde03x27=_0xde03x9[_0xf556[740]][_0xf556[1082]];_0xde03x9[_0xf556[740]][_0xf556[1082]]=function (_0xde03x28){return this[_0xf556[827]](function (){var _0xde03x1b,_0xde03x29,_0xde03xd;_0xde03x1b=_0xde03x9(this);_0xde03x29=_0xde03x1b[_0xf556[796]](_0xf556[1082]);_0xde03xd= typeof _0xde03x28===_0xf556[830]&&_0xde03x28;this[_0xf556[831]]=_0xf556[1082];if(!_0xde03x29){_0xde03x1b[_0xf556[796]](_0xf556[1082],(_0xde03x29= new _0xde03x70(this,_0xde03xd)));} ;if( typeof _0xde03x28===_0xf556[832]){_0xde03x29[_0xde03x28][_0xf556[833]](_0xde03x1b);} ;} );} ;_0xde03x9[_0xf556[740]][_0xf556[1082]][_0xf556[834]]=_0xde03x70;_0xde03x9[_0xf556[740]][_0xf556[1082]][_0xf556[738]]={name:_0xf556[766],value:_0xf556[766],min:0,max:100};_0xde03x9[_0xf556[740]][_0xf556[1082]][_0xf556[837]]=function (){_0xde03x9[_0xf556[740]][_0xf556[1082]]=_0xde03x27;return this;} ;var _0xde03x2a;if(_0xde03x9[_0xf556[839]][_0xf556[838]]){_0xde03x2a=_0xde03x9[_0xf556[839]][_0xf556[838]];} ;_0xde03x9[_0xf556[839]][_0xf556[838]]={get:function (_0xde03x2b){if(_0xde03x9(_0xde03x2b)[_0xf556[815]](_0xf556[1095])){return _0xde03x9(_0xde03x2b)[_0xf556[746]](_0xf556[970])[_0xf556[790]]();} else {if(_0xde03x2a){return _0xde03x2a[_0xf556[842]](_0xde03x2b);} ;} ;} ,set:function (_0xde03x2b,_0xde03x2c){if(_0xde03x9(_0xde03x2b)[_0xf556[815]](_0xf556[1095])){_0xde03x9(_0xde03x2b)[_0xf556[746]](_0xf556[970])[_0xf556[790]](_0xde03x2c);_0xde03x9(_0xde03x2b)[_0xf556[796]](_0xf556[1082])[_0xf556[1085]](_0xde03x2c);} else {if(_0xde03x2a){return _0xde03x2a[_0xf556[846]](_0xde03x2b,_0xde03x2c);} ;} ;} };_0xde03x9(document)[_0xf556[848]](function (){_0xde03x9(_0xf556[1096])[_0xf556[827]](function (){var _0xde03x75;_0xde03x75=_0xde03x9(this);_0xde03x75[_0xf556[1082]](_0xde03x75[_0xf556[796]]());} );} );} (window[_0xf556[734]]);+function (_0xde03x9){_0xf556[735];var _0xde03x76=function (_0xde03xc,_0xde03xd){this[_0xf556[737]]=_0xde03x9[_0xf556[741]]({},_0xde03x9[_0xf556[740]][_0xf556[1097]][_0xf556[738]],_0xde03xd);this[_0xf556[742]]=_0xde03x9(_0xde03xc);if(this[_0xf556[742]][_0xf556[811]](_0xf556[891])){this[_0xf556[1098]]();} ;if(this[_0xf556[742]][_0xf556[815]](_0xf556[958])){this[_0xf556[1099]]();} ;if(this[_0xf556[742]][_0xf556[811]](_0xf556[1100])){this[_0xf556[1101]]();} ;} ;_0xde03x76[_0xf556[744]]={constructor:_0xde03x76,addStates:function (){var _0xde03x77,_0xde03x78;_0xde03x77=this[_0xf556[737]][_0xf556[1102]];if(_0xde03x77!==_0xf556[766]){_0xde03x78=_0xde03x9(document)[_0xf556[746]](_0xf556[823]+_0xde03x77);if(_0xde03x78[_0xf556[821]]!==0){_0xde03x77=_0xde03x78[_0xf556[790]]();_0xde03x78[_0xf556[784]](_0xf556[1006],{state:this},this[_0xf556[1103]]);} ;} ;this[_0xf556[1104]](_0xde03x77);} ,loadStates:function (_0xde03x77){var _0xde03x55,_0xde03x79;_0xde03x55=this[_0xf556[737]][_0xf556[1105]];this[_0xf556[742]][_0xf556[781]](_0xf556[766]);if(this[_0xf556[737]][_0xf556[966]]===true){this[_0xf556[742]][_0xf556[912]](_0xf556[967]);} ;for(_0xde03x79 in BFHStatesList[_0xde03x77]){if(BFHStatesList[_0xde03x77][_0xf556[946]](_0xde03x79)){this[_0xf556[742]][_0xf556[912]](_0xf556[968]+BFHStatesList[_0xde03x77][_0xde03x79][_0xf556[1106]]+_0xf556[930]+BFHStatesList[_0xde03x77][_0xde03x79][_0xf556[772]]+_0xf556[969]);} ;} ;this[_0xf556[742]][_0xf556[790]](_0xde03x55);} ,changeCountry:function (_0xde03x1a){var _0xde03x1b,_0xde03x7a,_0xde03x77;_0xde03x1b=_0xde03x9(this);_0xde03x7a=_0xde03x1a[_0xf556[796]][_0xf556[1105]];_0xde03x77=_0xde03x1b[_0xf556[790]]();_0xde03x7a[_0xf556[1104]](_0xde03x77);} ,addBootstrapStates:function (){var _0xde03x77,_0xde03x78;_0xde03x77=this[_0xf556[737]][_0xf556[1102]];if(_0xde03x77!==_0xf556[766]){_0xde03x78=_0xde03x9(document)[_0xf556[746]](_0xf556[823]+_0xde03x77);if(_0xde03x78[_0xf556[821]]!==0){_0xde03x77=_0xde03x78[_0xf556[746]](_0xf556[970])[_0xf556[790]]();_0xde03x78[_0xf556[784]](_0xf556[1073],{state:this},this[_0xf556[1107]]);} ;} ;this[_0xf556[1108]](_0xde03x77);} ,loadBootstrapStates:function (_0xde03x77){var _0xde03x56,_0xde03x57,_0xde03x58,_0xde03x7b,_0xde03x7c,_0xde03x79;_0xde03x7b=this[_0xf556[737]][_0xf556[1105]];_0xde03x7c=_0xf556[766];_0xde03x56=this[_0xf556[742]][_0xf556[746]](_0xf556[970]);_0xde03x57=this[_0xf556[742]][_0xf556[746]](_0xf556[971]);_0xde03x58=this[_0xf556[742]][_0xf556[746]](_0xf556[972]);_0xde03x58[_0xf556[781]](_0xf556[766]);if(this[_0xf556[737]][_0xf556[966]]===true){_0xde03x58[_0xf556[912]](_0xf556[973]);} ;for(_0xde03x79 in BFHStatesList[_0xde03x77]){if(BFHStatesList[_0xde03x77][_0xf556[946]](_0xde03x79)){_0xde03x58[_0xf556[912]](_0xf556[984]+BFHStatesList[_0xde03x77][_0xde03x79][_0xf556[1106]]+_0xf556[930]+BFHStatesList[_0xde03x77][_0xde03x79][_0xf556[772]]+_0xf556[976]);if(BFHStatesList[_0xde03x77][_0xde03x79][_0xf556[1106]]===_0xde03x7b){_0xde03x7c=BFHStatesList[_0xde03x77][_0xde03x79][_0xf556[772]];} ;} ;} ;this[_0xf556[742]][_0xf556[790]](_0xde03x7b);} ,changeBootstrapCountry:function (_0xde03x1a){var _0xde03x1b,_0xde03x7a,_0xde03x77;_0xde03x1b=_0xde03x9(this);_0xde03x7a=_0xde03x1a[_0xf556[796]][_0xf556[1105]];_0xde03x77=_0xde03x1b[_0xf556[790]]();_0xde03x7a[_0xf556[1108]](_0xde03x77);} ,displayState:function (){var _0xde03x77,_0xde03x7b,_0xde03x7c,_0xde03x79;_0xde03x77=this[_0xf556[737]][_0xf556[1102]];_0xde03x7b=this[_0xf556[737]][_0xf556[1105]];_0xde03x7c=_0xf556[766];for(_0xde03x79 in BFHStatesList[_0xde03x77]){if(BFHStatesList[_0xde03x77][_0xf556[946]](_0xde03x79)){if(BFHStatesList[_0xde03x77][_0xde03x79][_0xf556[1106]]===_0xde03x7b){_0xde03x7c=BFHStatesList[_0xde03x77][_0xde03x79][_0xf556[772]];break ;} ;} ;} ;this[_0xf556[742]][_0xf556[781]](_0xde03x7c);} };var _0xde03x27=_0xde03x9[_0xf556[740]][_0xf556[1097]];_0xde03x9[_0xf556[740]][_0xf556[1097]]=function (_0xde03x28){return this[_0xf556[827]](function (){var _0xde03x1b,_0xde03x29,_0xde03xd;_0xde03x1b=_0xde03x9(this);_0xde03x29=_0xde03x1b[_0xf556[796]](_0xf556[1097]);_0xde03xd= typeof _0xde03x28===_0xf556[830]&&_0xde03x28;if(!_0xde03x29){_0xde03x1b[_0xf556[796]](_0xf556[1097],(_0xde03x29= new _0xde03x76(this,_0xde03xd)));} ;if( typeof _0xde03x28===_0xf556[832]){_0xde03x29[_0xde03x28][_0xf556[833]](_0xde03x1b);} ;} );} ;_0xde03x9[_0xf556[740]][_0xf556[1097]][_0xf556[834]]=_0xde03x76;_0xde03x9[_0xf556[740]][_0xf556[1097]][_0xf556[738]]={country:_0xf556[766],state:_0xf556[766],blank:true};_0xde03x9[_0xf556[740]][_0xf556[1097]][_0xf556[837]]=function (){_0xde03x9[_0xf556[740]][_0xf556[1097]]=_0xde03x27;return this;} ;_0xde03x9(document)[_0xf556[848]](function (){_0xde03x9(_0xf556[1109])[_0xf556[827]](function (){var _0xde03x7d;_0xde03x7d=_0xde03x9(this);if(_0xde03x7d[_0xf556[815]](_0xf556[958])){_0xde03x7d[_0xf556[977]](_0xde03x7d[_0xf556[796]]());} ;_0xde03x7d[_0xf556[1097]](_0xde03x7d[_0xf556[796]]());} );} );} (window[_0xf556[734]]);+function (_0xde03x9){_0xf556[735];var _0xde03xa=_0xf556[1110],_0xde03x7e=function (_0xde03xc,_0xde03xd){this[_0xf556[737]]=_0xde03x9[_0xf556[741]]({},_0xde03x9[_0xf556[740]][_0xf556[1111]][_0xf556[738]],_0xde03xd);this[_0xf556[742]]=_0xde03x9(_0xde03xc);this[_0xf556[743]]();} ;_0xde03x7e[_0xf556[744]]={constructor:_0xde03x7e,setTime:function (){var _0xde03x7f,_0xde03x30,_0xde03x80,_0xde03x81,_0xde03x82,_0xde03x83,_0xde03x84;_0xde03x7f=this[_0xf556[737]][_0xf556[1112]];_0xde03x83=_0xf556[766];_0xde03x84=_0xf556[766];if(_0xde03x7f===_0xf556[766]||_0xde03x7f===_0xf556[1113]||_0xde03x7f===undefined){_0xde03x30= new Date();_0xde03x81=_0xde03x30[_0xf556[1114]]();_0xde03x82=_0xde03x30[_0xf556[1115]]();if(this[_0xf556[737]][_0xf556[1116]]===_0xf556[1117]){if(_0xde03x81>12){_0xde03x81=_0xde03x81-12;_0xde03x83=_0xf556[1118]+BFHTimePickerModes[_0xf556[1119]];_0xde03x84=_0xf556[1119];} else {_0xde03x83=_0xf556[1118]+BFHTimePickerModes[_0xf556[1120]];_0xde03x84=_0xf556[1120];} ;} ;if(_0xde03x7f===_0xf556[1113]){this[_0xf556[742]][_0xf556[746]](_0xf556[1121])[_0xf556[790]](_0xde03x8a(_0xde03x81,_0xde03x82)+_0xde03x83);} ;this[_0xf556[742]][_0xf556[796]](_0xf556[1122],_0xde03x81);this[_0xf556[742]][_0xf556[796]](_0xf556[1123],_0xde03x82);this[_0xf556[742]][_0xf556[796]](_0xf556[1116],_0xde03x84);} else {_0xde03x80=String(_0xde03x7f)[_0xf556[962]](BFHTimePickerDelimiter);_0xde03x81=_0xde03x80[0];_0xde03x82=_0xde03x80[1];if(this[_0xf556[737]][_0xf556[1116]]===_0xf556[1117]){_0xde03x80=String(_0xde03x82)[_0xf556[962]](_0xf556[1118]);_0xde03x82=_0xde03x80[0];if(_0xde03x80[1]===BFHTimePickerModes[_0xf556[1119]]){_0xde03x84=_0xf556[1119];} else {_0xde03x84=_0xf556[1120];} ;} ;this[_0xf556[742]][_0xf556[746]](_0xf556[1121])[_0xf556[790]](_0xde03x7f);this[_0xf556[742]][_0xf556[796]](_0xf556[1122],_0xde03x81);this[_0xf556[742]][_0xf556[796]](_0xf556[1123],_0xde03x82);this[_0xf556[742]][_0xf556[796]](_0xf556[1116],_0xde03x84);} ;} ,initPopover:function (){var _0xde03x11,_0xde03x12,_0xde03x33,_0xde03x85,_0xde03x86;_0xde03x11=_0xf556[766];_0xde03x12=_0xf556[766];_0xde03x33=_0xf556[766];if(this[_0xf556[737]][_0xf556[866]]!==_0xf556[766]){if(this[_0xf556[737]][_0xf556[767]]===_0xf556[768]){_0xde03x12=_0xf556[867]+this[_0xf556[737]][_0xf556[866]]+_0xf556[868];} else {_0xde03x11=_0xf556[867]+this[_0xf556[737]][_0xf556[866]]+_0xf556[868];} ;_0xde03x33=_0xf556[869];} ;_0xde03x85=_0xf556[766];_0xde03x86=_0xf556[1124];if(this[_0xf556[737]][_0xf556[1116]]===_0xf556[1117]){_0xde03x85=_0xf556[1125]+_0xf556[1126]+this[_0xf556[737]][_0xf556[774]]+_0xf556[1127]+_0xf556[1128]+BFHTimePickerModes[_0xf556[1120]]+_0xf556[778]+_0xf556[1129]+BFHTimePickerModes[_0xf556[1119]]+_0xf556[778]+_0xf556[778];_0xde03x86=_0xf556[1130];} ;this[_0xf556[742]][_0xf556[781]](_0xf556[870]+_0xde03x33+_0xf556[1131]+_0xde03x11+_0xf556[771]+this[_0xf556[737]][_0xf556[772]]+_0xf556[773]+this[_0xf556[737]][_0xf556[774]]+_0xf556[775]+this[_0xf556[737]][_0xf556[776]]+_0xf556[777]+_0xde03x12+_0xf556[778]+_0xf556[1132]+_0xf556[1133]+_0xf556[885]+_0xf556[931]+_0xf556[1134]+_0xf556[1135]+this[_0xf556[737]][_0xf556[774]]+_0xf556[1136]+_0xde03x86+_0xf556[1137]+_0xf556[923]+_0xf556[1138]+BFHTimePickerDelimiter+_0xf556[923]+_0xf556[1139]+_0xf556[1135]+this[_0xf556[737]][_0xf556[774]]+_0xf556[1140]+_0xf556[923]+_0xde03x85+_0xf556[882]+_0xf556[886]+_0xf556[887]+_0xf556[778]);this[_0xf556[742]][_0xf556[784]](_0xf556[1141],_0xde03xa,_0xde03x7e[_0xf556[744]][_0xf556[787]])[_0xf556[784]](_0xf556[1141],_0xf556[1142],function (){return false;} );this[_0xf556[742]][_0xf556[746]](_0xf556[1022])[_0xf556[827]](function (){var _0xde03x66;_0xde03x66=_0xde03x9(this);_0xde03x66[_0xf556[997]](_0xde03x66[_0xf556[796]]());_0xde03x66[_0xf556[784]](_0xf556[1006],_0xde03x7e[_0xf556[744]][_0xf556[1006]]);} );this[_0xf556[742]][_0xf556[746]](_0xf556[1076])[_0xf556[827]](function (){var _0xde03x6f;_0xde03x6f=_0xde03x9(this);_0xde03x6f[_0xf556[977]](_0xde03x6f[_0xf556[796]]());_0xde03x6f[_0xf556[784]](_0xf556[1073],_0xde03x7e[_0xf556[744]][_0xf556[1006]]);} );this[_0xf556[1143]]();this[_0xf556[1144]]();} ,updatePopover:function (){var _0xde03x87,_0xde03x88,_0xde03x83;_0xde03x87=this[_0xf556[742]][_0xf556[796]](_0xf556[1122]);_0xde03x88=this[_0xf556[742]][_0xf556[796]](_0xf556[1123]);_0xde03x83=this[_0xf556[742]][_0xf556[796]](_0xf556[1116]);this[_0xf556[742]][_0xf556[746]](_0xf556[1145])[_0xf556[790]](_0xde03x87)[_0xf556[1006]]();this[_0xf556[742]][_0xf556[746]](_0xf556[1146])[_0xf556[790]](_0xde03x88)[_0xf556[1006]]();this[_0xf556[742]][_0xf556[746]](_0xf556[1076])[_0xf556[790]](_0xde03x83);} ,change:function (){var _0xde03x1b,_0xde03x1c,_0xde03x89,_0xde03x83;_0xde03x1b=_0xde03x9(this);_0xde03x1c=_0xde03x26(_0xde03x1b);_0xde03x89=_0xde03x1c[_0xf556[796]](_0xf556[1111]);if(_0xde03x89&&_0xde03x89!==_0xf556[1147]){_0xde03x83=_0xf556[766];if(_0xde03x89[_0xf556[737]][_0xf556[1116]]===_0xf556[1117]){_0xde03x83=_0xf556[1118]+BFHTimePickerModes[_0xde03x1c[_0xf556[746]](_0xf556[1076])[_0xf556[790]]()];} ;_0xde03x1c[_0xf556[746]](_0xf556[1121])[_0xf556[790]](_0xde03x1c[_0xf556[746]](_0xf556[1145])[_0xf556[790]]()+BFHTimePickerDelimiter+_0xde03x1c[_0xf556[746]](_0xf556[1146])[_0xf556[790]]()+_0xde03x83);_0xde03x1c[_0xf556[798]](_0xf556[1148]);} ;return false;} ,toggle:function (_0xde03x1a){var _0xde03x1b,_0xde03x1c,_0xde03x1d;_0xde03x1b=_0xde03x9(this);_0xde03x1c=_0xde03x26(_0xde03x1b);if(_0xde03x1c[_0xf556[811]](_0xf556[810])||_0xde03x1c[_0xf556[813]](_0xf556[812])!==undefined){return true;} ;_0xde03x1d=_0xde03x1c[_0xf556[815]](_0xf556[814]);_0xde03x25();if(!_0xde03x1d){_0xde03x1c[_0xf556[798]](_0xde03x1a=_0xde03x9.Event(_0xf556[1149]));if(_0xde03x1a[_0xf556[817]]()){return true;} ;_0xde03x1c[_0xf556[819]](_0xf556[814])[_0xf556[798]](_0xf556[1150]);_0xde03x1b[_0xf556[820]]();} ;return false;} };function _0xde03x8a(_0xde03x87,_0xde03x88){_0xde03x87=String(_0xde03x87);if(_0xde03x87[_0xf556[821]]===1){_0xde03x87=_0xf556[822]+_0xde03x87;} ;_0xde03x88=String(_0xde03x88);if(_0xde03x88[_0xf556[821]]===1){_0xde03x88=_0xf556[822]+_0xde03x88;} ;return _0xde03x87+BFHTimePickerDelimiter+_0xde03x88;} ;function _0xde03x25(){var _0xde03x1c;_0xde03x9(_0xde03xa)[_0xf556[827]](function (_0xde03x1a){_0xde03x1c=_0xde03x26(_0xde03x9(this));if(!_0xde03x1c[_0xf556[815]](_0xf556[814])){return true;} ;_0xde03x1c[_0xf556[798]](_0xde03x1a=_0xde03x9.Event(_0xf556[1151]));if(_0xde03x1a[_0xf556[817]]()){return true;} ;_0xde03x1c[_0xf556[826]](_0xf556[814])[_0xf556[798]](_0xf556[1152]);} );} ;function _0xde03x26(_0xde03x1b){return _0xde03x1b[_0xf556[829]](_0xf556[1153]);} ;var _0xde03x27=_0xde03x9[_0xf556[740]][_0xf556[1111]];_0xde03x9[_0xf556[740]][_0xf556[1111]]=function (_0xde03x28){return this[_0xf556[827]](function (){var _0xde03x1b,_0xde03x29,_0xde03xd;_0xde03x1b=_0xde03x9(this);_0xde03x29=_0xde03x1b[_0xf556[796]](_0xf556[1111]);_0xde03xd= typeof _0xde03x28===_0xf556[830]&&_0xde03x28;this[_0xf556[831]]=_0xf556[1111];if(!_0xde03x29){_0xde03x1b[_0xf556[796]](_0xf556[1111],(_0xde03x29= new _0xde03x7e(this,_0xde03xd)));} ;if( typeof _0xde03x28===_0xf556[832]){_0xde03x29[_0xde03x28][_0xf556[833]](_0xde03x1b);} ;} );} ;_0xde03x9[_0xf556[740]][_0xf556[1111]][_0xf556[834]]=_0xde03x7e;_0xde03x9[_0xf556[740]][_0xf556[1111]][_0xf556[738]]={icon:_0xf556[1154],align:_0xf556[791],input:_0xf556[835],placeholder:_0xf556[766],name:_0xf556[766],time:_0xf556[1113],mode:_0xf556[1155]};_0xde03x9[_0xf556[740]][_0xf556[1111]][_0xf556[837]]=function (){_0xde03x9[_0xf556[740]][_0xf556[1111]]=_0xde03x27;return this;} ;var _0xde03x2a;if(_0xde03x9[_0xf556[839]][_0xf556[838]]){_0xde03x2a=_0xde03x9[_0xf556[839]][_0xf556[838]];} ;_0xde03x9[_0xf556[839]][_0xf556[838]]={get:function (_0xde03x2b){if(_0xde03x9(_0xde03x2b)[_0xf556[815]](_0xf556[1156])){return _0xde03x9(_0xde03x2b)[_0xf556[746]](_0xf556[1121])[_0xf556[790]]();} else {if(_0xde03x2a){return _0xde03x2a[_0xf556[842]](_0xde03x2b);} ;} ;} ,set:function (_0xde03x2b,_0xde03x2c){var _0xde03x8b;if(_0xde03x9(_0xde03x2b)[_0xf556[815]](_0xf556[1156])){_0xde03x8b=_0xde03x9(_0xde03x2b)[_0xf556[796]](_0xf556[1111]);_0xde03x8b[_0xf556[737]][_0xf556[1112]]=_0xde03x2c;_0xde03x8b[_0xf556[1143]]();_0xde03x8b[_0xf556[1144]]();} else {if(_0xde03x2a){return _0xde03x2a[_0xf556[846]](_0xde03x2b,_0xde03x2c);} ;} ;} };_0xde03x9(document)[_0xf556[848]](function (){_0xde03x9(_0xf556[1157])[_0xf556[827]](function (){var _0xde03x8b;_0xde03x8b=_0xde03x9(this);_0xde03x8b[_0xf556[1111]](_0xde03x8b[_0xf556[796]]());} );} );_0xde03x9(document)[_0xf556[784]](_0xf556[1158],_0xde03x25);} (window[_0xf556[734]]);
/* =========================================================
 * bootstrap-datepicker.js
 * Repo: https://github.com/eternicode/bootstrap-datepicker/
 * Demo: http://eternicode.github.io/bootstrap-datepicker/
 * Docs: http://bootstrap-datepicker.readthedocs.org/
 * Forked from http://www.eyecon.ro/bootstrap-datepicker
 * =========================================================
 * Started by Stefan Petre; improvements by Andrew Rowls + contributors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * ========================================================= */

(function($, undefined){

	var $window = $(window);

	function UTCDate(){
		return new Date(Date.UTC.apply(Date, arguments));
	}
	function UTCToday(){
		var today = new Date();
		return UTCDate(today.getFullYear(), today.getMonth(), today.getDate());
	}
	function alias(method){
		return function(){
			return this[method].apply(this, arguments);
		};
	}

	var DateArray = (function(){
		var extras = {
			get: function(i){
				return this.slice(i)[0];
			},
			contains: function(d){
				// Array.indexOf is not cross-browser;
				// $.inArray doesn't work with Dates
				var val = d && d.valueOf();
				for (var i=0, l=this.length; i < l; i++)
					if (this[i].valueOf() === val)
						return i;
				return -1;
			},
			remove: function(i){
				this.splice(i,1);
			},
			replace: function(new_array){
				if (!new_array)
					return;
				if (!$.isArray(new_array))
					new_array = [new_array];
				this.clear();
				this.push.apply(this, new_array);
			},
			clear: function(){
				this.splice(0);
			},
			copy: function(){
				var a = new DateArray();
				a.replace(this);
				return a;
			}
		};

		return function(){
			var a = [];
			a.push.apply(a, arguments);
			$.extend(a, extras);
			return a;
		};
	})();


	// Picker object

	var Datepicker = function(element, options){
		this.dates = new DateArray();
		this.viewDate = UTCToday();
		this.focusDate = null;

		this._process_options(options);

		this.element = $(element);
		this.isInline = false;
		this.isInput = this.element.is('input');
		this.component = this.element.is('.date') ? this.element.find('.add-on, .input-group-addon, .btn') : false;
		this.hasInput = this.component && this.element.find('input').length;
		if (this.component && this.component.length === 0)
			this.component = false;

		this.picker = $(DPGlobal.template);
		this._buildEvents();
		this._attachEvents();

		if (this.isInline){
			this.picker.addClass('datepicker-inline').appendTo(this.element);
		}
		else {
			this.picker.addClass('datepicker-dropdown dropdown-menu');
		}

		if (this.o.rtl){
			this.picker.addClass('datepicker-rtl');
		}

		this.viewMode = this.o.startView;

		if (this.o.calendarWeeks)
			this.picker.find('tfoot th.today')
						.attr('colspan', function(i, val){
							return parseInt(val) + 1;
						});

		this._allow_update = false;

		this.setStartDate(this._o.startDate);
		this.setEndDate(this._o.endDate);
		this.setDaysOfWeekDisabled(this.o.daysOfWeekDisabled);

		this.fillDow();
		this.fillMonths();

		this._allow_update = true;

		this.update();
		this.showMode();

		if (this.isInline){
			this.show();
		}
	};

	Datepicker.prototype = {
		constructor: Datepicker,

		_process_options: function(opts){
			// Store raw options for reference
			this._o = $.extend({}, this._o, opts);
			// Processed options
			var o = this.o = $.extend({}, this._o);

			// Check if "de-DE" style date is available, if not language should
			// fallback to 2 letter code eg "de"
			var lang = o.language;
			if (!dates[lang]){
				lang = lang.split('-')[0];
				if (!dates[lang])
					lang = defaults.language;
			}
			o.language = lang;

			switch (o.startView){
				case 2:
				case 'decade':
					o.startView = 2;
					break;
				case 1:
				case 'year':
					o.startView = 1;
					break;
				default:
					o.startView = 0;
			}

			switch (o.minViewMode){
				case 1:
				case 'months':
					o.minViewMode = 1;
					break;
				case 2:
				case 'years':
					o.minViewMode = 2;
					break;
				default:
					o.minViewMode = 0;
			}

			o.startView = Math.max(o.startView, o.minViewMode);

			// true, false, or Number > 0
			if (o.multidate !== true){
				o.multidate = Number(o.multidate) || false;
				if (o.multidate !== false)
					o.multidate = Math.max(0, o.multidate);
				else
					o.multidate = 1;
			}
			o.multidateSeparator = String(o.multidateSeparator);

			o.weekStart %= 7;
			o.weekEnd = ((o.weekStart + 6) % 7);

			var format = DPGlobal.parseFormat(o.format);
			if (o.startDate !== -Infinity){
				if (!!o.startDate){
					if (o.startDate instanceof Date)
						o.startDate = this._local_to_utc(this._zero_time(o.startDate));
					else
						o.startDate = DPGlobal.parseDate(o.startDate, format, o.language);
				}
				else {
					o.startDate = -Infinity;
				}
			}
			if (o.endDate !== Infinity){
				if (!!o.endDate){
					if (o.endDate instanceof Date)
						o.endDate = this._local_to_utc(this._zero_time(o.endDate));
					else
						o.endDate = DPGlobal.parseDate(o.endDate, format, o.language);
				}
				else {
					o.endDate = Infinity;
				}
			}

			o.daysOfWeekDisabled = o.daysOfWeekDisabled||[];
			if (!$.isArray(o.daysOfWeekDisabled))
				o.daysOfWeekDisabled = o.daysOfWeekDisabled.split(/[,\s]*/);
			o.daysOfWeekDisabled = $.map(o.daysOfWeekDisabled, function(d){
				return parseInt(d, 10);
			});

			var plc = String(o.orientation).toLowerCase().split(/\s+/g),
				_plc = o.orientation.toLowerCase();
			plc = $.grep(plc, function(word){
				return (/^auto|left|right|top|bottom$/).test(word);
			});
			o.orientation = {x: 'auto', y: 'auto'};
			if (!_plc || _plc === 'auto')
				; // no action
			else if (plc.length === 1){
				switch (plc[0]){
					case 'top':
					case 'bottom':
						o.orientation.y = plc[0];
						break;
					case 'left':
					case 'right':
						o.orientation.x = plc[0];
						break;
				}
			}
			else {
				_plc = $.grep(plc, function(word){
					return (/^left|right$/).test(word);
				});
				o.orientation.x = _plc[0] || 'auto';

				_plc = $.grep(plc, function(word){
					return (/^top|bottom$/).test(word);
				});
				o.orientation.y = _plc[0] || 'auto';
			}
		},
		_events: [],
		_secondaryEvents: [],
		_applyEvents: function(evs){
			for (var i=0, el, ch, ev; i < evs.length; i++){
				el = evs[i][0];
				if (evs[i].length === 2){
					ch = undefined;
					ev = evs[i][1];
				}
				else if (evs[i].length === 3){
					ch = evs[i][1];
					ev = evs[i][2];
				}
				el.on(ev, ch);
			}
		},
		_unapplyEvents: function(evs){
			for (var i=0, el, ev, ch; i < evs.length; i++){
				el = evs[i][0];
				if (evs[i].length === 2){
					ch = undefined;
					ev = evs[i][1];
				}
				else if (evs[i].length === 3){
					ch = evs[i][1];
					ev = evs[i][2];
				}
				el.off(ev, ch);
			}
		},
		_buildEvents: function(){
			if (this.isInput){ // single input
				this._events = [
					[this.element, {
						focus: $.proxy(this.show, this),
						keyup: $.proxy(function(e){
							if ($.inArray(e.keyCode, [27,37,39,38,40,32,13,9]) === -1)
								this.update();
						}, this),
						keydown: $.proxy(this.keydown, this)
					}]
				];
			}
			else if (this.component && this.hasInput){ // component: input + button
				this._events = [
					// For components that are not readonly, allow keyboard nav
					[this.element.find('input'), {
						focus: $.proxy(this.show, this),
						keyup: $.proxy(function(e){
							if ($.inArray(e.keyCode, [27,37,39,38,40,32,13,9]) === -1)
								this.update();
						}, this),
						keydown: $.proxy(this.keydown, this)
					}],
					[this.component, {
						click: $.proxy(this.show, this)
					}]
				];
			}
			else if (this.element.is('div')){  // inline datepicker
				this.isInline = true;
			}
			else {
				this._events = [
					[this.element, {
						click: $.proxy(this.show, this)
					}]
				];
			}
			this._events.push(
				// Component: listen for blur on element descendants
				[this.element, '*', {
					blur: $.proxy(function(e){
						this._focused_from = e.target;
					}, this)
				}],
				// Input: listen for blur on element
				[this.element, {
					blur: $.proxy(function(e){
						this._focused_from = e.target;
					}, this)
				}]
			);

			this._secondaryEvents = [
				[this.picker, {
					click: $.proxy(this.click, this)
				}],
				[$(window), {
					resize: $.proxy(this.place, this)
				}],
				[$(document), {
					'mousedown touchstart': $.proxy(function(e){
						// Clicked outside the datepicker, hide it
						if (!(
							this.element.is(e.target) ||
							this.element.find(e.target).length ||
							this.picker.is(e.target) ||
							this.picker.find(e.target).length
						)){
							this.hide();
						}
					}, this)
				}]
			];
		},
		_attachEvents: function(){
			this._detachEvents();
			this._applyEvents(this._events);
		},
		_detachEvents: function(){
			this._unapplyEvents(this._events);
		},
		_attachSecondaryEvents: function(){
			this._detachSecondaryEvents();
			this._applyEvents(this._secondaryEvents);
		},
		_detachSecondaryEvents: function(){
			this._unapplyEvents(this._secondaryEvents);
		},
		_trigger: function(event, altdate){
			var date = altdate || this.dates.get(-1),
				local_date = this._utc_to_local(date);

			this.element.trigger({
				type: event,
				date: local_date,
				dates: $.map(this.dates, this._utc_to_local),
				format: $.proxy(function(ix, format){
					if (arguments.length === 0){
						ix = this.dates.length - 1;
						format = this.o.format;
					}
					else if (typeof ix === 'string'){
						format = ix;
						ix = this.dates.length - 1;
					}
					format = format || this.o.format;
					var date = this.dates.get(ix);
					return DPGlobal.formatDate(date, format, this.o.language);
				}, this)
			});
		},

		show: function(){
			if (!this.isInline)
				this.picker.appendTo('body');
			this.picker.show();
			this.place();
			this._attachSecondaryEvents();
			this._trigger('show');
		},

		hide: function(){
			if (this.isInline)
				return;
			if (!this.picker.is(':visible'))
				return;
			this.focusDate = null;
			this.picker.hide().detach();
			this._detachSecondaryEvents();
			this.viewMode = this.o.startView;
			this.showMode();

			if (
				this.o.forceParse &&
				(
					this.isInput && this.element.val() ||
					this.hasInput && this.element.find('input').val()
				)
			)
				this.setValue();
			this._trigger('hide');
		},

		remove: function(){
			this.hide();
			this._detachEvents();
			this._detachSecondaryEvents();
			this.picker.remove();
			delete this.element.data().datepicker;
			if (!this.isInput){
				delete this.element.data().date;
			}
		},

		_utc_to_local: function(utc){
			return utc && new Date(utc.getTime() + (utc.getTimezoneOffset()*60000));
		},
		_local_to_utc: function(local){
			return local && new Date(local.getTime() - (local.getTimezoneOffset()*60000));
		},
		_zero_time: function(local){
			return local && new Date(local.getFullYear(), local.getMonth(), local.getDate());
		},
		_zero_utc_time: function(utc){
			return utc && new Date(Date.UTC(utc.getUTCFullYear(), utc.getUTCMonth(), utc.getUTCDate()));
		},

		getDates: function(){
			return $.map(this.dates, this._utc_to_local);
		},

		getUTCDates: function(){
			return $.map(this.dates, function(d){
				return new Date(d);
			});
		},

		getDate: function(){
			return this._utc_to_local(this.getUTCDate());
		},

		getUTCDate: function(){
			return new Date(this.dates.get(-1));
		},

		setDates: function(){
			var args = $.isArray(arguments[0]) ? arguments[0] : arguments;
			this.update.apply(this, args);
			this._trigger('changeDate');
			this.setValue();
		},

		setUTCDates: function(){
			var args = $.isArray(arguments[0]) ? arguments[0] : arguments;
			this.update.apply(this, $.map(args, this._utc_to_local));
			this._trigger('changeDate');
			this.setValue();
		},

		setDate: alias('setDates'),
		setUTCDate: alias('setUTCDates'),

		setValue: function(){
			var formatted = this.getFormattedDate();
			if (!this.isInput){
				if (this.component){
					this.element.find('input').val(formatted).change();
				}
			}
			else {
				this.element.val(formatted).change();
			}
		},

		getFormattedDate: function(format){
			if (format === undefined)
				format = this.o.format;

			var lang = this.o.language;
			return $.map(this.dates, function(d){
				return DPGlobal.formatDate(d, format, lang);
			}).join(this.o.multidateSeparator);
		},

		setStartDate: function(startDate){
			this._process_options({startDate: startDate});
			this.update();
			this.updateNavArrows();
		},

		setEndDate: function(endDate){
			this._process_options({endDate: endDate});
			this.update();
			this.updateNavArrows();
		},

		setDaysOfWeekDisabled: function(daysOfWeekDisabled){
			this._process_options({daysOfWeekDisabled: daysOfWeekDisabled});
			this.update();
			this.updateNavArrows();
		},

		place: function(){
			if (this.isInline)
				return;
			var calendarWidth = this.picker.outerWidth(),
				calendarHeight = this.picker.outerHeight(),
				visualPadding = 10,
				windowWidth = $window.width(),
				windowHeight = $window.height(),
				scrollTop = $window.scrollTop();

			var zIndex = parseInt(this.element.parents().filter(function(){
					return $(this).css('z-index') !== 'auto';
				}).first().css('z-index'))+10;
			var offset = this.component ? this.component.parent().offset() : this.element.offset();
			var height = this.component ? this.component.outerHeight(true) : this.element.outerHeight(false);
			var width = this.component ? this.component.outerWidth(true) : this.element.outerWidth(false);
			var left = offset.left,
				top = offset.top;

			this.picker.removeClass(
				'datepicker-orient-top datepicker-orient-bottom '+
				'datepicker-orient-right datepicker-orient-left'
			);

			if (this.o.orientation.x !== 'auto'){
				this.picker.addClass('datepicker-orient-' + this.o.orientation.x);
				if (this.o.orientation.x === 'right')
					left -= calendarWidth - width;
			}
			// auto x orientation is best-placement: if it crosses a window
			// edge, fudge it sideways
			else {
				// Default to left
				this.picker.addClass('datepicker-orient-left');
				if (offset.left < 0)
					left -= offset.left - visualPadding;
				else if (offset.left + calendarWidth > windowWidth)
					left = windowWidth - calendarWidth - visualPadding;
			}

			// auto y orientation is best-situation: top or bottom, no fudging,
			// decision based on which shows more of the calendar
			var yorient = this.o.orientation.y,
				top_overflow, bottom_overflow;
			if (yorient === 'auto'){
				top_overflow = -scrollTop + offset.top - calendarHeight;
				bottom_overflow = scrollTop + windowHeight - (offset.top + height + calendarHeight);
				if (Math.max(top_overflow, bottom_overflow) === bottom_overflow)
					yorient = 'top';
				else
					yorient = 'bottom';
			}
			this.picker.addClass('datepicker-orient-' + yorient);
			if (yorient === 'top')
				top += height;
			else
				top -= calendarHeight + parseInt(this.picker.css('padding-top'));

			this.picker.css({
				top: top,
				left: left,
				zIndex: zIndex
			});
		},

		_allow_update: true,
		update: function(){
			if (!this._allow_update)
				return;

			var oldDates = this.dates.copy(),
				dates = [],
				fromArgs = false;
			if (arguments.length){
				$.each(arguments, $.proxy(function(i, date){
					if (date instanceof Date)
						date = this._local_to_utc(date);
					dates.push(date);
				}, this));
				fromArgs = true;
			}
			else {
				dates = this.isInput
						? this.element.val()
						: this.element.data('date') || this.element.find('input').val();
				if (dates && this.o.multidate)
					dates = dates.split(this.o.multidateSeparator);
				else
					dates = [dates];
				delete this.element.data().date;
			}

			dates = $.map(dates, $.proxy(function(date){
				return DPGlobal.parseDate(date, this.o.format, this.o.language);
			}, this));
			dates = $.grep(dates, $.proxy(function(date){
				return (
					date < this.o.startDate ||
					date > this.o.endDate ||
					!date
				);
			}, this), true);
			this.dates.replace(dates);

			if (this.dates.length)
				this.viewDate = new Date(this.dates.get(-1));
			else if (this.viewDate < this.o.startDate)
				this.viewDate = new Date(this.o.startDate);
			else if (this.viewDate > this.o.endDate)
				this.viewDate = new Date(this.o.endDate);

			if (fromArgs){
				// setting date by clicking
				this.setValue();
			}
			else if (dates.length){
				// setting date by typing
				if (String(oldDates) !== String(this.dates))
					this._trigger('changeDate');
			}
			if (!this.dates.length && oldDates.length)
				this._trigger('clearDate');

			this.fill();
		},

		fillDow: function(){
			var dowCnt = this.o.weekStart,
				html = '<tr>';
			if (this.o.calendarWeeks){
				var cell = '<th class="cw">&nbsp;</th>';
				html += cell;
				this.picker.find('.datepicker-days thead tr:first-child').prepend(cell);
			}
			while (dowCnt < this.o.weekStart + 7){
				html += '<th class="dow">'+dates[this.o.language].daysMin[(dowCnt++)%7]+'</th>';
			}
			html += '</tr>';
			this.picker.find('.datepicker-days thead').append(html);
		},

		fillMonths: function(){
			var html = '',
			i = 0;
			while (i < 12){
				html += '<span class="month">'+dates[this.o.language].monthsShort[i++]+'</span>';
			}
			this.picker.find('.datepicker-months td').html(html);
		},

		setRange: function(range){
			if (!range || !range.length)
				delete this.range;
			else
				this.range = $.map(range, function(d){
					return d.valueOf();
				});
			this.fill();
		},

		getClassNames: function(date){
			var cls = [],
				year = this.viewDate.getUTCFullYear(),
				month = this.viewDate.getUTCMonth(),
				today = new Date();
			if (date.getUTCFullYear() < year || (date.getUTCFullYear() === year && date.getUTCMonth() < month)){
				cls.push('old');
			}
			else if (date.getUTCFullYear() > year || (date.getUTCFullYear() === year && date.getUTCMonth() > month)){
				cls.push('new');
			}
			if (this.focusDate && date.valueOf() === this.focusDate.valueOf())
				cls.push('focused');
			// Compare internal UTC date with local today, not UTC today
			if (this.o.todayHighlight &&
				date.getUTCFullYear() === today.getFullYear() &&
				date.getUTCMonth() === today.getMonth() &&
				date.getUTCDate() === today.getDate()){
				cls.push('today');
			}
			if (this.dates.contains(date) !== -1)
				cls.push('active');
			if (date.valueOf() < this.o.startDate || date.valueOf() > this.o.endDate ||
				$.inArray(date.getUTCDay(), this.o.daysOfWeekDisabled) !== -1){
				cls.push('disabled');
			}
			if (this.range){
				if (date > this.range[0] && date < this.range[this.range.length-1]){
					cls.push('range');
				}
				if ($.inArray(date.valueOf(), this.range) !== -1){
					cls.push('selected');
				}
			}
			return cls;
		},

		fill: function(){
			var d = new Date(this.viewDate),
				year = d.getUTCFullYear(),
				month = d.getUTCMonth(),
				startYear = this.o.startDate !== -Infinity ? this.o.startDate.getUTCFullYear() : -Infinity,
				startMonth = this.o.startDate !== -Infinity ? this.o.startDate.getUTCMonth() : -Infinity,
				endYear = this.o.endDate !== Infinity ? this.o.endDate.getUTCFullYear() : Infinity,
				endMonth = this.o.endDate !== Infinity ? this.o.endDate.getUTCMonth() : Infinity,
				todaytxt = dates[this.o.language].today || dates['en'].today || '',
				cleartxt = dates[this.o.language].clear || dates['en'].clear || '',
				tooltip;
			this.picker.find('.datepicker-days thead th.datepicker-switch')
						.text(dates[this.o.language].months[month]+' '+year);
			this.picker.find('tfoot th.today')
						.text(todaytxt)
						.toggle(this.o.todayBtn !== false);
			this.picker.find('tfoot th.clear')
						.text(cleartxt)
						.toggle(this.o.clearBtn !== false);
			this.updateNavArrows();
			this.fillMonths();
			var prevMonth = UTCDate(year, month-1, 28),
				day = DPGlobal.getDaysInMonth(prevMonth.getUTCFullYear(), prevMonth.getUTCMonth());
			prevMonth.setUTCDate(day);
			prevMonth.setUTCDate(day - (prevMonth.getUTCDay() - this.o.weekStart + 7)%7);
			var nextMonth = new Date(prevMonth);
			nextMonth.setUTCDate(nextMonth.getUTCDate() + 42);
			nextMonth = nextMonth.valueOf();
			var html = [];
			var clsName;
			while (prevMonth.valueOf() < nextMonth){
				if (prevMonth.getUTCDay() === this.o.weekStart){
					html.push('<tr>');
					if (this.o.calendarWeeks){
						// ISO 8601: First week contains first thursday.
						// ISO also states week starts on Monday, but we can be more abstract here.
						var
							// Start of current week: based on weekstart/current date
							ws = new Date(+prevMonth + (this.o.weekStart - prevMonth.getUTCDay() - 7) % 7 * 864e5),
							// Thursday of this week
							th = new Date(Number(ws) + (7 + 4 - ws.getUTCDay()) % 7 * 864e5),
							// First Thursday of year, year from thursday
							yth = new Date(Number(yth = UTCDate(th.getUTCFullYear(), 0, 1)) + (7 + 4 - yth.getUTCDay())%7*864e5),
							// Calendar week: ms between thursdays, div ms per day, div 7 days
							calWeek =  (th - yth) / 864e5 / 7 + 1;
						html.push('<td class="cw">'+ calWeek +'</td>');

					}
				}
				clsName = this.getClassNames(prevMonth);
				clsName.push('day');

				if (this.o.beforeShowDay !== $.noop){
					var before = this.o.beforeShowDay(this._utc_to_local(prevMonth));
					if (before === undefined)
						before = {};
					else if (typeof(before) === 'boolean')
						before = {enabled: before};
					else if (typeof(before) === 'string')
						before = {classes: before};
					if (before.enabled === false)
						clsName.push('disabled');
					if (before.classes)
						clsName = clsName.concat(before.classes.split(/\s+/));
					if (before.tooltip)
						tooltip = before.tooltip;
				}

				clsName = $.unique(clsName);
				html.push('<td class="'+clsName.join(' ')+'"' + (tooltip ? ' title="'+tooltip+'"' : '') + '>'+prevMonth.getUTCDate() + '</td>');
				if (prevMonth.getUTCDay() === this.o.weekEnd){
					html.push('</tr>');
				}
				prevMonth.setUTCDate(prevMonth.getUTCDate()+1);
			}
			this.picker.find('.datepicker-days tbody').empty().append(html.join(''));

			var months = this.picker.find('.datepicker-months')
						.find('th:eq(1)')
							.text(year)
							.end()
						.find('span').removeClass('active');

			$.each(this.dates, function(i, d){
				if (d.getUTCFullYear() === year)
					months.eq(d.getUTCMonth()).addClass('active');
			});

			if (year < startYear || year > endYear){
				months.addClass('disabled');
			}
			if (year === startYear){
				months.slice(0, startMonth).addClass('disabled');
			}
			if (year === endYear){
				months.slice(endMonth+1).addClass('disabled');
			}

			html = '';
			year = parseInt(year/10, 10) * 10;
			var yearCont = this.picker.find('.datepicker-years')
								.find('th:eq(1)')
									.text(year + '-' + (year + 9))
									.end()
								.find('td');
			year -= 1;
			var years = $.map(this.dates, function(d){
					return d.getUTCFullYear();
				}),
				classes;
			for (var i = -1; i < 11; i++){
				classes = ['year'];
				if (i === -1)
					classes.push('old');
				else if (i === 10)
					classes.push('new');
				if ($.inArray(year, years) !== -1)
					classes.push('active');
				if (year < startYear || year > endYear)
					classes.push('disabled');
				html += '<span class="' + classes.join(' ') + '">'+year+'</span>';
				year += 1;
			}
			yearCont.html(html);
		},

		updateNavArrows: function(){
			if (!this._allow_update)
				return;

			var d = new Date(this.viewDate),
				year = d.getUTCFullYear(),
				month = d.getUTCMonth();
			switch (this.viewMode){
				case 0:
					if (this.o.startDate !== -Infinity && year <= this.o.startDate.getUTCFullYear() && month <= this.o.startDate.getUTCMonth()){
						this.picker.find('.prev').css({visibility: 'hidden'});
					}
					else {
						this.picker.find('.prev').css({visibility: 'visible'});
					}
					if (this.o.endDate !== Infinity && year >= this.o.endDate.getUTCFullYear() && month >= this.o.endDate.getUTCMonth()){
						this.picker.find('.next').css({visibility: 'hidden'});
					}
					else {
						this.picker.find('.next').css({visibility: 'visible'});
					}
					break;
				case 1:
				case 2:
					if (this.o.startDate !== -Infinity && year <= this.o.startDate.getUTCFullYear()){
						this.picker.find('.prev').css({visibility: 'hidden'});
					}
					else {
						this.picker.find('.prev').css({visibility: 'visible'});
					}
					if (this.o.endDate !== Infinity && year >= this.o.endDate.getUTCFullYear()){
						this.picker.find('.next').css({visibility: 'hidden'});
					}
					else {
						this.picker.find('.next').css({visibility: 'visible'});
					}
					break;
			}
		},

		click: function(e){
			e.preventDefault();
			var target = $(e.target).closest('span, td, th'),
				year, month, day;
			if (target.length === 1){
				switch (target[0].nodeName.toLowerCase()){
					case 'th':
						switch (target[0].className){
							case 'datepicker-switch':
								this.showMode(1);
								break;
							case 'prev':
							case 'next':
								var dir = DPGlobal.modes[this.viewMode].navStep * (target[0].className === 'prev' ? -1 : 1);
								switch (this.viewMode){
									case 0:
										this.viewDate = this.moveMonth(this.viewDate, dir);
										this._trigger('changeMonth', this.viewDate);
										break;
									case 1:
									case 2:
										this.viewDate = this.moveYear(this.viewDate, dir);
										if (this.viewMode === 1)
											this._trigger('changeYear', this.viewDate);
										break;
								}
								this.fill();
								break;
							case 'today':
								var date = new Date();
								date = UTCDate(date.getFullYear(), date.getMonth(), date.getDate(), 0, 0, 0);

								this.showMode(-2);
								var which = this.o.todayBtn === 'linked' ? null : 'view';
								this._setDate(date, which);
								break;
							case 'clear':
								var element;
								if (this.isInput)
									element = this.element;
								else if (this.component)
									element = this.element.find('input');
								if (element)
									element.val("").change();
								this.update();
								this._trigger('changeDate');
								if (this.o.autoclose)
									this.hide();
								break;
						}
						break;
					case 'span':
						if (!target.is('.disabled')){
							this.viewDate.setUTCDate(1);
							if (target.is('.month')){
								day = 1;
								month = target.parent().find('span').index(target);
								year = this.viewDate.getUTCFullYear();
								this.viewDate.setUTCMonth(month);
								this._trigger('changeMonth', this.viewDate);
								if (this.o.minViewMode === 1){
									this._setDate(UTCDate(year, month, day));
								}
							}
							else {
								day = 1;
								month = 0;
								year = parseInt(target.text(), 10)||0;
								this.viewDate.setUTCFullYear(year);
								this._trigger('changeYear', this.viewDate);
								if (this.o.minViewMode === 2){
									this._setDate(UTCDate(year, month, day));
								}
							}
							this.showMode(-1);
							this.fill();
						}
						break;
					case 'td':
						if (target.is('.day') && !target.is('.disabled')){
							day = parseInt(target.text(), 10)||1;
							year = this.viewDate.getUTCFullYear();
							month = this.viewDate.getUTCMonth();
							if (target.is('.old')){
								if (month === 0){
									month = 11;
									year -= 1;
								}
								else {
									month -= 1;
								}
							}
							else if (target.is('.new')){
								if (month === 11){
									month = 0;
									year += 1;
								}
								else {
									month += 1;
								}
							}
							this._setDate(UTCDate(year, month, day));
						}
						break;
				}
			}
			if (this.picker.is(':visible') && this._focused_from){
				$(this._focused_from).focus();
			}
			delete this._focused_from;
		},

		_toggle_multidate: function(date){
			var ix = this.dates.contains(date);
			if (!date){
				this.dates.clear();
			}
			else if (ix !== -1){
				this.dates.remove(ix);
			}
			else {
				this.dates.push(date);
			}
			if (typeof this.o.multidate === 'number')
				while (this.dates.length > this.o.multidate)
					this.dates.remove(0);
		},

		_setDate: function(date, which){
			if (!which || which === 'date')
				this._toggle_multidate(date && new Date(date));
			if (!which || which  === 'view')
				this.viewDate = date && new Date(date);

			this.fill();
			this.setValue();
			this._trigger('changeDate');
			var element;
			if (this.isInput){
				element = this.element;
			}
			else if (this.component){
				element = this.element.find('input');
			}
			if (element){
				element.change();
			}
			if (this.o.autoclose && (!which || which === 'date')){
				this.hide();
			}
		},

		moveMonth: function(date, dir){
			if (!date)
				return undefined;
			if (!dir)
				return date;
			var new_date = new Date(date.valueOf()),
				day = new_date.getUTCDate(),
				month = new_date.getUTCMonth(),
				mag = Math.abs(dir),
				new_month, test;
			dir = dir > 0 ? 1 : -1;
			if (mag === 1){
				test = dir === -1
					// If going back one month, make sure month is not current month
					// (eg, Mar 31 -> Feb 31 == Feb 28, not Mar 02)
					? function(){
						return new_date.getUTCMonth() === month;
					}
					// If going forward one month, make sure month is as expected
					// (eg, Jan 31 -> Feb 31 == Feb 28, not Mar 02)
					: function(){
						return new_date.getUTCMonth() !== new_month;
					};
				new_month = month + dir;
				new_date.setUTCMonth(new_month);
				// Dec -> Jan (12) or Jan -> Dec (-1) -- limit expected date to 0-11
				if (new_month < 0 || new_month > 11)
					new_month = (new_month + 12) % 12;
			}
			else {
				// For magnitudes >1, move one month at a time...
				for (var i=0; i < mag; i++)
					// ...which might decrease the day (eg, Jan 31 to Feb 28, etc)...
					new_date = this.moveMonth(new_date, dir);
				// ...then reset the day, keeping it in the new month
				new_month = new_date.getUTCMonth();
				new_date.setUTCDate(day);
				test = function(){
					return new_month !== new_date.getUTCMonth();
				};
			}
			// Common date-resetting loop -- if date is beyond end of month, make it
			// end of month
			while (test()){
				new_date.setUTCDate(--day);
				new_date.setUTCMonth(new_month);
			}
			return new_date;
		},

		moveYear: function(date, dir){
			return this.moveMonth(date, dir*12);
		},

		dateWithinRange: function(date){
			return date >= this.o.startDate && date <= this.o.endDate;
		},

		keydown: function(e){
			if (this.picker.is(':not(:visible)')){
				if (e.keyCode === 27) // allow escape to hide and re-show picker
					this.show();
				return;
			}
			var dateChanged = false,
				dir, newDate, newViewDate,
				focusDate = this.focusDate || this.viewDate;
			switch (e.keyCode){
				case 27: // escape
					if (this.focusDate){
						this.focusDate = null;
						this.viewDate = this.dates.get(-1) || this.viewDate;
						this.fill();
					}
					else
						this.hide();
					e.preventDefault();
					break;
				case 37: // left
				case 39: // right
					if (!this.o.keyboardNavigation)
						break;
					dir = e.keyCode === 37 ? -1 : 1;
					if (e.ctrlKey){
						newDate = this.moveYear(this.dates.get(-1) || UTCToday(), dir);
						newViewDate = this.moveYear(focusDate, dir);
						this._trigger('changeYear', this.viewDate);
					}
					else if (e.shiftKey){
						newDate = this.moveMonth(this.dates.get(-1) || UTCToday(), dir);
						newViewDate = this.moveMonth(focusDate, dir);
						this._trigger('changeMonth', this.viewDate);
					}
					else {
						newDate = new Date(this.dates.get(-1) || UTCToday());
						newDate.setUTCDate(newDate.getUTCDate() + dir);
						newViewDate = new Date(focusDate);
						newViewDate.setUTCDate(focusDate.getUTCDate() + dir);
					}
					if (this.dateWithinRange(newDate)){
						this.focusDate = this.viewDate = newViewDate;
						this.setValue();
						this.fill();
						e.preventDefault();
					}
					break;
				case 38: // up
				case 40: // down
					if (!this.o.keyboardNavigation)
						break;
					dir = e.keyCode === 38 ? -1 : 1;
					if (e.ctrlKey){
						newDate = this.moveYear(this.dates.get(-1) || UTCToday(), dir);
						newViewDate = this.moveYear(focusDate, dir);
						this._trigger('changeYear', this.viewDate);
					}
					else if (e.shiftKey){
						newDate = this.moveMonth(this.dates.get(-1) || UTCToday(), dir);
						newViewDate = this.moveMonth(focusDate, dir);
						this._trigger('changeMonth', this.viewDate);
					}
					else {
						newDate = new Date(this.dates.get(-1) || UTCToday());
						newDate.setUTCDate(newDate.getUTCDate() + dir * 7);
						newViewDate = new Date(focusDate);
						newViewDate.setUTCDate(focusDate.getUTCDate() + dir * 7);
					}
					if (this.dateWithinRange(newDate)){
						this.focusDate = this.viewDate = newViewDate;
						this.setValue();
						this.fill();
						e.preventDefault();
					}
					break;
				case 32: // spacebar
					// Spacebar is used in manually typing dates in some formats.
					// As such, its behavior should not be hijacked.
					break;
				case 13: // enter
					focusDate = this.focusDate || this.dates.get(-1) || this.viewDate;
					this._toggle_multidate(focusDate);
					dateChanged = true;
					this.focusDate = null;
					this.viewDate = this.dates.get(-1) || this.viewDate;
					this.setValue();
					this.fill();
					if (this.picker.is(':visible')){
						e.preventDefault();
						if (this.o.autoclose)
							this.hide();
					}
					break;
				case 9: // tab
					this.focusDate = null;
					this.viewDate = this.dates.get(-1) || this.viewDate;
					this.fill();
					this.hide();
					break;
			}
			if (dateChanged){
				if (this.dates.length)
					this._trigger('changeDate');
				else
					this._trigger('clearDate');
				var element;
				if (this.isInput){
					element = this.element;
				}
				else if (this.component){
					element = this.element.find('input');
				}
				if (element){
					element.change();
				}
			}
		},

		showMode: function(dir){
			if (dir){
				this.viewMode = Math.max(this.o.minViewMode, Math.min(2, this.viewMode + dir));
			}
			this.picker
				.find('>div')
				.hide()
				.filter('.datepicker-'+DPGlobal.modes[this.viewMode].clsName)
					.css('display', 'block');
			this.updateNavArrows();
		}
	};

	var DateRangePicker = function(element, options){
		this.element = $(element);
		this.inputs = $.map(options.inputs, function(i){
			return i.jquery ? i[0] : i;
		});
		delete options.inputs;

		$(this.inputs)
			.datepicker(options)
			.bind('changeDate', $.proxy(this.dateUpdated, this));

		this.pickers = $.map(this.inputs, function(i){
			return $(i).data('datepicker');
		});
		this.updateDates();
	};
	DateRangePicker.prototype = {
		updateDates: function(){
			this.dates = $.map(this.pickers, function(i){
				return i.getUTCDate();
			});
			this.updateRanges();
		},
		updateRanges: function(){
			var range = $.map(this.dates, function(d){
				return d.valueOf();
			});
			$.each(this.pickers, function(i, p){
				p.setRange(range);
			});
		},
		dateUpdated: function(e){
			// `this.updating` is a workaround for preventing infinite recursion
			// between `changeDate` triggering and `setUTCDate` calling.  Until
			// there is a better mechanism.
			if (this.updating)
				return;
			this.updating = true;

			var dp = $(e.target).data('datepicker'),
				new_date = dp.getUTCDate(),
				i = $.inArray(e.target, this.inputs),
				l = this.inputs.length;
			if (i === -1)
				return;

			$.each(this.pickers, function(i, p){
				if (!p.getUTCDate())
					p.setUTCDate(new_date);
			});

			if (new_date < this.dates[i]){
				// Date being moved earlier/left
				while (i >= 0 && new_date < this.dates[i]){
					this.pickers[i--].setUTCDate(new_date);
				}
			}
			else if (new_date > this.dates[i]){
				// Date being moved later/right
				while (i < l && new_date > this.dates[i]){
					this.pickers[i++].setUTCDate(new_date);
				}
			}
			this.updateDates();

			delete this.updating;
		},
		remove: function(){
			$.map(this.pickers, function(p){ p.remove(); });
			delete this.element.data().datepicker;
		}
	};

	function opts_from_el(el, prefix){
		// Derive options from element data-attrs
		var data = $(el).data(),
			out = {}, inkey,
			replace = new RegExp('^' + prefix.toLowerCase() + '([A-Z])');
		prefix = new RegExp('^' + prefix.toLowerCase());
		function re_lower(_,a){
			return a.toLowerCase();
		}
		for (var key in data)
			if (prefix.test(key)){
				inkey = key.replace(replace, re_lower);
				out[inkey] = data[key];
			}
		return out;
	}

	function opts_from_locale(lang){
		// Derive options from locale plugins
		var out = {};
		// Check if "de-DE" style date is available, if not language should
		// fallback to 2 letter code eg "de"
		if (!dates[lang]){
			lang = lang.split('-')[0];
			if (!dates[lang])
				return;
		}
		var d = dates[lang];
		$.each(locale_opts, function(i,k){
			if (k in d)
				out[k] = d[k];
		});
		return out;
	}

	var old = $.fn.datepicker;
	$.fn.datepicker = function(option){
		var args = Array.apply(null, arguments);
		args.shift();
		var internal_return;
		this.each(function(){
			var $this = $(this),
				data = $this.data('datepicker'),
				options = typeof option === 'object' && option;
			if (!data){
				var elopts = opts_from_el(this, 'date'),
					// Preliminary otions
					xopts = $.extend({}, defaults, elopts, options),
					locopts = opts_from_locale(xopts.language),
					// Options priority: js args, data-attrs, locales, defaults
					opts = $.extend({}, defaults, locopts, elopts, options);
				if ($this.is('.input-daterange') || opts.inputs){
					var ropts = {
						inputs: opts.inputs || $this.find('input').toArray()
					};
					$this.data('datepicker', (data = new DateRangePicker(this, $.extend(opts, ropts))));
				}
				else {
					$this.data('datepicker', (data = new Datepicker(this, opts)));
				}
			}
			if (typeof option === 'string' && typeof data[option] === 'function'){
				internal_return = data[option].apply(data, args);
				if (internal_return !== undefined)
					return false;
			}
		});
		if (internal_return !== undefined)
			return internal_return;
		else
			return this;
	};

	var defaults = $.fn.datepicker.defaults = {
		autoclose: false,
		beforeShowDay: $.noop,
		calendarWeeks: false,
		clearBtn: false,
		daysOfWeekDisabled: [],
		endDate: Infinity,
		forceParse: true,
		format: 'mm/dd/yyyy',
		keyboardNavigation: true,
		language: 'en',
		minViewMode: 0,
		multidate: false,
		multidateSeparator: ',',
		orientation: "auto",
		rtl: false,
		startDate: -Infinity,
		startView: 0,
		todayBtn: false,
		todayHighlight: false,
		weekStart: 0
	};
	var locale_opts = $.fn.datepicker.locale_opts = [
		'format',
		'rtl',
		'weekStart'
	];
	$.fn.datepicker.Constructor = Datepicker;
	var dates = $.fn.datepicker.dates = {
		en: {
			days: ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
			daysShort: ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
			daysMin: ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"],
			months: ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
			monthsShort: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
			today: "Today",
			clear: "Clear"
		}
	};

	var DPGlobal = {
		modes: [
			{
				clsName: 'days',
				navFnc: 'Month',
				navStep: 1
			},
			{
				clsName: 'months',
				navFnc: 'FullYear',
				navStep: 1
			},
			{
				clsName: 'years',
				navFnc: 'FullYear',
				navStep: 10
		}],
		isLeapYear: function(year){
			return (((year % 4 === 0) && (year % 100 !== 0)) || (year % 400 === 0));
		},
		getDaysInMonth: function(year, month){
			return [31, (DPGlobal.isLeapYear(year) ? 29 : 28), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month];
		},
		validParts: /dd?|DD?|mm?|MM?|yy(?:yy)?/g,
		nonpunctuation: /[^ -\/:-@\[\u3400-\u9fff-`{-~\t\n\r]+/g,
		parseFormat: function(format){
			// IE treats \0 as a string end in inputs (truncating the value),
			// so it's a bad format delimiter, anyway
			var separators = format.replace(this.validParts, '\0').split('\0'),
				parts = format.match(this.validParts);
			if (!separators || !separators.length || !parts || parts.length === 0){
				throw new Error("Invalid date format.");
			}
			return {separators: separators, parts: parts};
		},
		parseDate: function(date, format, language){
			if (!date)
				return undefined;
			if (date instanceof Date)
				return date;
			if (typeof format === 'string')
				format = DPGlobal.parseFormat(format);
			var part_re = /([\-+]\d+)([dmwy])/,
				parts = date.match(/([\-+]\d+)([dmwy])/g),
				part, dir, i;
			if (/^[\-+]\d+[dmwy]([\s,]+[\-+]\d+[dmwy])*$/.test(date)){
				date = new Date();
				for (i=0; i < parts.length; i++){
					part = part_re.exec(parts[i]);
					dir = parseInt(part[1]);
					switch (part[2]){
						case 'd':
							date.setUTCDate(date.getUTCDate() + dir);
							break;
						case 'm':
							date = Datepicker.prototype.moveMonth.call(Datepicker.prototype, date, dir);
							break;
						case 'w':
							date.setUTCDate(date.getUTCDate() + dir * 7);
							break;
						case 'y':
							date = Datepicker.prototype.moveYear.call(Datepicker.prototype, date, dir);
							break;
					}
				}
				return UTCDate(date.getUTCFullYear(), date.getUTCMonth(), date.getUTCDate(), 0, 0, 0);
			}
			parts = date && date.match(this.nonpunctuation) || [];
			date = new Date();
			var parsed = {},
				setters_order = ['yyyy', 'yy', 'M', 'MM', 'm', 'mm', 'd', 'dd'],
				setters_map = {
					yyyy: function(d,v){
						return d.setUTCFullYear(v);
					},
					yy: function(d,v){
						return d.setUTCFullYear(2000+v);
					},
					m: function(d,v){
						if (isNaN(d))
							return d;
						v -= 1;
						while (v < 0) v += 12;
						v %= 12;
						d.setUTCMonth(v);
						while (d.getUTCMonth() !== v)
							d.setUTCDate(d.getUTCDate()-1);
						return d;
					},
					d: function(d,v){
						return d.setUTCDate(v);
					}
				},
				val, filtered;
			setters_map['M'] = setters_map['MM'] = setters_map['mm'] = setters_map['m'];
			setters_map['dd'] = setters_map['d'];
			date = UTCDate(date.getFullYear(), date.getMonth(), date.getDate(), 0, 0, 0);
			var fparts = format.parts.slice();
			// Remove noop parts
			if (parts.length !== fparts.length){
				fparts = $(fparts).filter(function(i,p){
					return $.inArray(p, setters_order) !== -1;
				}).toArray();
			}
			// Process remainder
			function match_part(){
				var m = this.slice(0, parts[i].length),
					p = parts[i].slice(0, m.length);
				return m === p;
			}
			if (parts.length === fparts.length){
				var cnt;
				for (i=0, cnt = fparts.length; i < cnt; i++){
					val = parseInt(parts[i], 10);
					part = fparts[i];
					if (isNaN(val)){
						switch (part){
							case 'MM':
								filtered = $(dates[language].months).filter(match_part);
								val = $.inArray(filtered[0], dates[language].months) + 1;
								break;
							case 'M':
								filtered = $(dates[language].monthsShort).filter(match_part);
								val = $.inArray(filtered[0], dates[language].monthsShort) + 1;
								break;
						}
					}
					parsed[part] = val;
				}
				var _date, s;
				for (i=0; i < setters_order.length; i++){
					s = setters_order[i];
					if (s in parsed && !isNaN(parsed[s])){
						_date = new Date(date);
						setters_map[s](_date, parsed[s]);
						if (!isNaN(_date))
							date = _date;
					}
				}
			}
			return date;
		},
		formatDate: function(date, format, language){
			if (!date)
				return '';
			if (typeof format === 'string')
				format = DPGlobal.parseFormat(format);
			var val = {
				d: date.getUTCDate(),
				D: dates[language].daysShort[date.getUTCDay()],
				DD: dates[language].days[date.getUTCDay()],
				m: date.getUTCMonth() + 1,
				M: dates[language].monthsShort[date.getUTCMonth()],
				MM: dates[language].months[date.getUTCMonth()],
				yy: date.getUTCFullYear().toString().substring(2),
				yyyy: date.getUTCFullYear()
			};
			val.dd = (val.d < 10 ? '0' : '') + val.d;
			val.mm = (val.m < 10 ? '0' : '') + val.m;
			date = [];
			var seps = $.extend([], format.separators);
			for (var i=0, cnt = format.parts.length; i <= cnt; i++){
				if (seps.length)
					date.push(seps.shift());
				date.push(val[format.parts[i]]);
			}
			return date.join('');
		},
		headTemplate: '<thead>'+
							'<tr>'+
								'<th class="prev">&laquo;</th>'+
								'<th colspan="5" class="datepicker-switch"></th>'+
								'<th class="next">&raquo;</th>'+
							'</tr>'+
						'</thead>',
		contTemplate: '<tbody><tr><td colspan="7"></td></tr></tbody>',
		footTemplate: '<tfoot>'+
							'<tr>'+
								'<th colspan="7" class="today"></th>'+
							'</tr>'+
							'<tr>'+
								'<th colspan="7" class="clear"></th>'+
							'</tr>'+
						'</tfoot>'
	};
	DPGlobal.template = '<div class="datepicker">'+
							'<div class="datepicker-days">'+
								'<table class=" table-condensed">'+
									DPGlobal.headTemplate+
									'<tbody></tbody>'+
									DPGlobal.footTemplate+
								'</table>'+
							'</div>'+
							'<div class="datepicker-months">'+
								'<table class="table-condensed">'+
									DPGlobal.headTemplate+
									DPGlobal.contTemplate+
									DPGlobal.footTemplate+
								'</table>'+
							'</div>'+
							'<div class="datepicker-years">'+
								'<table class="table-condensed">'+
									DPGlobal.headTemplate+
									DPGlobal.contTemplate+
									DPGlobal.footTemplate+
								'</table>'+
							'</div>'+
						'</div>';

	$.fn.datepicker.DPGlobal = DPGlobal;


	/* DATEPICKER NO CONFLICT
	* =================== */

	$.fn.datepicker.noConflict = function(){
		$.fn.datepicker = old;
		return this;
	};


	/* DATEPICKER DATA-API
	* ================== */

	$(document).on(
		'focus.datepicker.data-api click.datepicker.data-api',
		'[data-provide="datepicker"]',
		function(e){
			var $this = $(this);
			if ($this.data('datepicker'))
				return;
			e.preventDefault();
			// component click requires us to explicitly show it
			$this.datepicker('show');
		}
	);
	$(function(){
		$('[data-provide="datepicker-inline"]').datepicker();
	});

}(window.jQuery));

/**
 * Russian translation for bootstrap-datepicker
 * Victor Taranenko <darwin@snowdale.com>
 */
;(function($){
    $.fn.datepicker.dates['ru'] = {
        days: ["Воскресенье", "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"],
        daysShort: ["Вск", "Пнд", "Втр", "Срд", "Чтв", "Птн", "Суб", "Вск"],
        daysMin: ["Вс", "Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"],
        months: ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"],
        monthsShort: ["Янв", "Фев", "Мар", "Апр", "Май", "Июн", "Июл", "Авг", "Сен", "Окт", "Ноя", "Дек"],
        today: "Сегодня",
        weekStart: 1
    };
}(jQuery));
/* =========================================================
 * bootstrap-slider.js v2.0.0
 * http://www.eyecon.ro/bootstrap-slider
 * =========================================================
 * Copyright 2012 Stefan Petre
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * ========================================================= */
 
!function( $ ) {

	var Slider = function(element, options) {
		this.element = $(element);
		this.picker = $('<div class="slider">'+
							'<div class="slider-track">'+
								'<div class="slider-selection"></div>'+
								'<div class="slider-handle"></div>'+
								'<div class="slider-handle"></div>'+
							'</div>'+
							'<div class="tooltip"><div class="tooltip-arrow"></div><div class="tooltip-inner"></div></div>'+
						'</div>')
							.insertBefore(this.element)
							.append(this.element);
		this.id = this.element.data('slider-id')||options.id;
		if (this.id) {
			this.picker[0].id = this.id;
		}

		if (typeof Modernizr !== 'undefined' && Modernizr.touch) {
			this.touchCapable = true;
		}

		var tooltip = this.element.data('slider-tooltip')||options.tooltip;

		this.tooltip = this.picker.find('.tooltip');
		this.tooltipInner = this.tooltip.find('div.tooltip-inner');

		this.orientation = this.element.data('slider-orientation')||options.orientation;
		switch(this.orientation) {
			case 'vertical':
				this.picker.addClass('slider-vertical');
				this.stylePos = 'top';
				this.mousePos = 'pageY';
				this.sizePos = 'offsetHeight';
				this.tooltip.addClass('right')[0].style.left = '100%';
				break;
			default:
				this.picker
					.addClass('slider-horizontal')
					.css('width', this.element.outerWidth());
				this.orientation = 'horizontal';
				this.stylePos = 'left';
				this.mousePos = 'pageX';
				this.sizePos = 'offsetWidth';
				this.tooltip.addClass('top')[0].style.top = -this.tooltip.outerHeight() - 14 + 'px';
				break;
		}

		this.min = this.element.data('slider-min')||options.min;
		this.max = this.element.data('slider-max')||options.max;
		this.step = this.element.data('slider-step')||options.step;
		this.value = this.element.data('slider-value')||options.value;
		if (this.value[1]) {
			this.range = true;
		}

		this.selection = this.element.data('slider-selection')||options.selection;
		this.selectionEl = this.picker.find('.slider-selection');
		if (this.selection === 'none') {
			this.selectionEl.addClass('hide');
		}
		this.selectionElStyle = this.selectionEl[0].style;


		this.handle1 = this.picker.find('.slider-handle:first');
		this.handle1Stype = this.handle1[0].style;
		this.handle2 = this.picker.find('.slider-handle:last');
		this.handle2Stype = this.handle2[0].style;

		var handle = this.element.data('slider-handle')||options.handle;
		switch(handle) {
			case 'round':
				this.handle1.addClass('round');
				this.handle2.addClass('round');
				break
			case 'triangle':
				this.handle1.addClass('triangle');
				this.handle2.addClass('triangle');
				break
		}

		if (this.range) {
			this.value[0] = Math.max(this.min, Math.min(this.max, this.value[0]));
			this.value[1] = Math.max(this.min, Math.min(this.max, this.value[1]));
		} else {
			this.value = [ Math.max(this.min, Math.min(this.max, this.value))];
			this.handle2.addClass('hide');
			if (this.selection == 'after') {
				this.value[1] = this.max;
			} else {
				this.value[1] = this.min;
			}
		}
		this.diff = this.max - this.min;
		this.percentage = [
			(this.value[0]-this.min)*100/this.diff,
			(this.value[1]-this.min)*100/this.diff,
			this.step*100/this.diff
		];

		this.offset = this.picker.offset();
		this.size = this.picker[0][this.sizePos];

		this.formater = options.formater;

		this.layout();

		if (this.touchCapable) {
			// Touch: Bind touch events:
			this.picker.on({
				touchstart: $.proxy(this.mousedown, this)
			});
		} else {
			this.picker.on({
				mousedown: $.proxy(this.mousedown, this)
			});
		}

		if (tooltip === 'show') {
			this.picker.on({
				mouseenter: $.proxy(this.showTooltip, this),
				mouseleave: $.proxy(this.hideTooltip, this)
			});
		} else {
			this.tooltip.addClass('hide');
		}
	};

	Slider.prototype = {
		constructor: Slider,

		over: false,
		inDrag: false,
		
		showTooltip: function(){
			this.tooltip.addClass('in');
			//var left = Math.round(this.percent*this.width);
			//this.tooltip.css('left', left - this.tooltip.outerWidth()/2);
			this.over = true;
		},
		
		hideTooltip: function(){
			if (this.inDrag === false) {
				this.tooltip.removeClass('in');
			}
			this.over = false;
		},

		layout: function(){
			this.handle1Stype[this.stylePos] = this.percentage[0]+'%';
			this.handle2Stype[this.stylePos] = this.percentage[1]+'%';
			if (this.orientation == 'vertical') {
				this.selectionElStyle.top = Math.min(this.percentage[0], this.percentage[1]) +'%';
				this.selectionElStyle.height = Math.abs(this.percentage[0] - this.percentage[1]) +'%';
			} else {
				this.selectionElStyle.left = Math.min(this.percentage[0], this.percentage[1]) +'%';
				this.selectionElStyle.width = Math.abs(this.percentage[0] - this.percentage[1]) +'%';
			}
			if (this.range) {
				this.tooltipInner.text(
					this.formater(this.value[0]) + 
					' : ' + 
					this.formater(this.value[1])
				);
				this.tooltip[0].style[this.stylePos] = this.size * (this.percentage[0] + (this.percentage[1] - this.percentage[0])/2)/100 - (this.orientation === 'vertical' ? this.tooltip.outerHeight()/2 : this.tooltip.outerWidth()/2) +'px';
			} else {
				this.tooltipInner.text(
					this.formater(this.value[0])
				);
				this.tooltip[0].style[this.stylePos] = this.size * this.percentage[0]/100 - (this.orientation === 'vertical' ? this.tooltip.outerHeight()/2 : this.tooltip.outerWidth()/2) +'px';
			}
		},

		mousedown: function(ev) {

			// Touch: Get the original event:
			if (this.touchCapable && ev.type === 'touchstart') {
				ev = ev.originalEvent;
			}

			this.offset = this.picker.offset();
			this.size = this.picker[0][this.sizePos];

			var percentage = this.getPercentage(ev);

			if (this.range) {
				var diff1 = Math.abs(this.percentage[0] - percentage);
				var diff2 = Math.abs(this.percentage[1] - percentage);
				this.dragged = (diff1 < diff2) ? 0 : 1;
			} else {
				this.dragged = 0;
			}

			this.percentage[this.dragged] = percentage;
			this.layout();

			if (this.touchCapable) {
				// Touch: Bind touch events:
				$(document).on({
					touchmove: $.proxy(this.mousemove, this),
					touchend: $.proxy(this.mouseup, this)
				});
			} else {
				$(document).on({
					mousemove: $.proxy(this.mousemove, this),
					mouseup: $.proxy(this.mouseup, this)
				});
			}

			this.inDrag = true;
			var val = this.calculateValue();
			this.element.trigger({
					type: 'slideStart',
					value: val
				}).trigger({
					type: 'slide',
					value: val
				});
			return false;
		},

		mousemove: function(ev) {
			
			// Touch: Get the original event:
			if (this.touchCapable && ev.type === 'touchmove') {
				ev = ev.originalEvent;
			}

			var percentage = this.getPercentage(ev);
			if (this.range) {
				if (this.dragged === 0 && this.percentage[1] < percentage) {
					this.percentage[0] = this.percentage[1];
					this.dragged = 1;
				} else if (this.dragged === 1 && this.percentage[0] > percentage) {
					this.percentage[1] = this.percentage[0];
					this.dragged = 0;
				}
			}
			this.percentage[this.dragged] = percentage;
			this.layout();
			var val = this.calculateValue();
			this.element
				.trigger({
					type: 'slide',
					value: val
				})
				.data('value', val)
				.prop('value', val);
			return false;
		},

		mouseup: function(ev) {
			if (this.touchCapable) {
				// Touch: Bind touch events:
				$(document).off({
					touchmove: this.mousemove,
					touchend: this.mouseup
				});
			} else {
				$(document).off({
					mousemove: this.mousemove,
					mouseup: this.mouseup
				});
			}

			this.inDrag = false;
			if (this.over == false) {
				this.hideTooltip();
			}
			this.element;
			var val = this.calculateValue();
			this.element
				.trigger({
					type: 'slideStop',
					value: val
				})
				.data('value', val)
				.prop('value', val);
			return false;
		},

		calculateValue: function() {
			var val;
			if (this.range) {
				val = [
					(this.min + Math.round((this.diff * this.percentage[0]/100)/this.step)*this.step),
					(this.min + Math.round((this.diff * this.percentage[1]/100)/this.step)*this.step)
				];
				this.value = val;
			} else {
				val = (this.min + Math.round((this.diff * this.percentage[0]/100)/this.step)*this.step);
				this.value = [val, this.value[1]];
			}
			return val;
		},

		getPercentage: function(ev) {
			if (this.touchCapable) {
				ev = ev.touches[0];
			}
			var percentage = (ev[this.mousePos] - this.offset[this.stylePos])*100/this.size;
			percentage = Math.round(percentage/this.percentage[2])*this.percentage[2];
			return Math.max(0, Math.min(100, percentage));
		},

		getValue: function() {
			if (this.range) {
				return this.value;
			}
			return this.value[0];
		},

		setValue: function(val) {
			this.value = val;

			if (this.range) {
				this.value[0] = Math.max(this.min, Math.min(this.max, this.value[0]));
				this.value[1] = Math.max(this.min, Math.min(this.max, this.value[1]));
			} else {
				this.value = [ Math.max(this.min, Math.min(this.max, this.value))];
				this.handle2.addClass('hide');
				if (this.selection == 'after') {
					this.value[1] = this.max;
				} else {
					this.value[1] = this.min;
				}
			}
			this.diff = this.max - this.min;
			this.percentage = [
				(this.value[0]-this.min)*100/this.diff,
				(this.value[1]-this.min)*100/this.diff,
				this.step*100/this.diff
			];
			this.layout();
		}
	};

	$.fn.slider = function ( option, val ) {
		return this.each(function () {
			var $this = $(this),
				data = $this.data('slider'),
				options = typeof option === 'object' && option;
			if (!data)  {
				$this.data('slider', (data = new Slider(this, $.extend({}, $.fn.slider.defaults,options))));
			}
			if (typeof option == 'string') {
				data[option](val);
			}
		})
	};

	$.fn.slider.defaults = {
		min: 0,
		max: 10,
		step: 1,
		orientation: 'horizontal',
		value: 5,
		selection: 'before',
		tooltip: 'show',
		handle: 'round',
		formater: function(value) {
			return value;
		}
	};

	$.fn.slider.Constructor = Slider;

}( window.jQuery );
function failFunction(e) {
    var data = jQuery.parseJSON(e.responseText);
    jQuery.notify(data.message);
}

(function($) {
    $(document).ready(function() {

        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        };

        var csrftoken = getCookie('csrftoken');

        $.ajaxSetup({
            crossDomain: false, // obviates need for sameOrigin test
            beforeSend: function(xhr, settings) {
                //if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
                //}
            }
        });

        $('.dropdown.auto').mouseenter(function(e) {
            $(this).addClass('open');
        });
        $('.dropdown.auto').mouseleave(function(e) {
            $(this).removeClass('open');
        });

        $('.dropdown .item').hover(function(e) {
            $(this).toggleClass('hover');
        });

        $('.dropdown.keep-open').on({
            "click":             function(e) {
                this.closable = $(e.target).parents('.dropdown-menu').length == 0;
            },
            "hide.bs.dropdown":  function() {
                return this.closable;
            }
        });

        $('[data-toggle="tooltip"]').tooltip();

        $('.colorbox').colorbox({
            scalePhotos: true,
            maxWidth: '100%',
            maxHeight: '100%',
            fixed: true
        });

        if (messages) {
            for (var i in messages) {
                jQuery.notify(messages[i]);
            }
        }

        $('.masked-phone').mask('+7(999) 999-9999');

        bootbox.setDefaults({
            locale: 'ru'
        });

        $("img.lazy").lazyload({
            effect : "fadeIn"
        });

        $.notifyDefaults({
            delay: 5000,
            animate: {
                enter: 'animated fadeInRight',
                exit: 'animated fadeOutRight'
            }
        });

        $('#scroll-up').click(function(e) {
            $('html, body').animate({ scrollTop: 0 }, "slow");
            e.preventDefault();
            return false;
        });

        window.onscroll = function() {
            var scrollup = $('#scroll-up');
            if (window.pageYOffset>250) {
                $(scrollup).removeClass('hidden');
            } else {
                $(scrollup).addClass('hidden');
            }
        }

    });
})(jQuery);

(function($) {
    $(document).ready(function() {
        //multiple select
        function multipleSelectActivated(dropDownSelect, id) {
            var select = dropDownSelect.find('select');
            var values = select.val();
            if (!values)
                values = [];
            values.push(id);
            select.val(values);
            if (values.length) {
                var l = [];
                var options = select.find('option:checked');
                for (var i=0; i<options.length; i++)
                    l.push(options[i].text);
                dropDownSelect.find('button').html(l.join(', ') + '<b class="caret"></b>');
            } else
                dropDownSelect.find('button').html('Выбрать <b class="caret"></b>');

            dropDownSelect.find('.item-list a[data-value='+id+']').addClass('active');
        }

        function multipleSelectDeactivate(dropDownSelect, id) {
            var select = dropDownSelect.find('select');
            var values = select.val();
            if (!values)
                values = [];
            var pos = values.indexOf(id);
            if (pos>=0)
                values.splice(pos, 1);
            select.val(values);
            if (values.length) {
                var l = [];
                var options = select.find('option:checked');
                for (var i = 0; i < options.length; i++)
                    l.push(options[i].text);
                dropDownSelect.find('button').html(l.join(', ') + '<b class="caret"></b>');
            } else
                dropDownSelect.find('button').html('Выбрать <b class="caret"></b>');

            dropDownSelect.find('.item-list a[data-value='+id+']').removeClass('active');
        }

        $(document).on('click', '.select-dropdown .item-list .item', function(e){
            if ($(this).hasClass('active')) {
                multipleSelectDeactivate($(this).parents('.select-dropdown'), $(this).data('value').toString());
            } else {
                multipleSelectActivated($(this).parents('.select-dropdown'), $(this).data('value').toString());
            }
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-catalog-next-page', function(e){
            $(this).html('Загружается...');
            $.get(this.href, function(data){
                $('.ext-pagination').remove();
                $('.ext-links').remove();
                var container = $('#content');
                container.append(data);
            });
            e.preventDefault();
            return false;
        });

        // $(document).on('click', '.choose-town-list a', function(e){
        //     var id = $(e.currentTarget).data('id');
        //     $.cookie('town', id, {
        //         path: '/'
        //     });
        //     window.location.href = '/' + $(e.currentTarget).data('slug') +'/arenda/';
        //     e.preventDefault();
        //     return false;
        // });

        $('#contacts-form').ajaxForm({
            dataType: 'json',
            form: this,
            success: function(data, status, xhr, form) {
                    jQuery.notify(data.object.message);
                    $('#contacts-form')[0].reset();
            },
            error: failFunction
        });

        $('#payment-fastorder-form').ajaxForm({
            dataType: 'json',
            form: this,
            success: function(data, status, xhr, form) {
                if (data.object.type == 'payment')
                    window.location = data.object.url;
                if (data.object.type == 'free') {
                    bootbox.hideAll();
                    bootbox.alert(data.object.message);
                }
            },
            error: failFunction
        });

        $('#payment-alert-form').ajaxForm({
            dataType: 'json',
            form: this,
            success: function(data, status, xhr, form) {
                    jQuery.notify(data.object.message);
                    $('#payment-alert-form')[0].reset();
            },
            error: failFunction
        });

        $(document).on('change', '.order-form #id_town', function(){
            var id = $('.order-form #id_town').val();
            if (id) {
                if (town_bases[id].main_base)
                    $('.order-form .need_main_base').removeClass('hidden');
                else
                    $('.order-form .need_main_base').addClass('hidden');

                if (town_bases[id].vk_base)
                    $('.order-form .need_vk_base').removeClass('hidden');
                else
                    $('.order-form .need_vk_base').addClass('hidden');

                if (town_bases[id].main_base && town_bases[id].vk_base)
                    $('.order-form .need_vk_base.need_main_base').removeClass('hidden');
                else
                    $('.order-form .need_vk_base.need_main_base').addClass('hidden');

                $('.order-form .city').addClass('city-hidden');
                $('.order-form .city-'+id).removeClass('city-hidden');
            }
        });

        $(document).on('click', '.btn-get-access', function(e){
            var id = $(this).data('id');
            var vk = $(this).hasClass('vk');
            $.get('/get-access', {id: id, vk: vk}, function(data){
                 bootbox.dialog({
                    title: 'Получить доступ',
                    message: data,
                    buttons: {
                        'Закрыть': {
                            className: 'btn-default'
                        }
                    }
                });
            });
        });

        $(document).on('click', '.btn-open-tel', function(e){
            var id = $(this).data('id');
            var password = $('#password').val();
            $('.password-tel').html('<img src="/phone?id='+id+'&password=' + password + '&hash='+Math.random().toString(10).substr(2)+'">');
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-open-vktel', function(e){
            var id = $(this).data('id');
            var password = $('#password').val();
            $('.password-tel').html('<img src="/vkphone?id='+id+'&password=' + password + '&hash='+Math.random().toString(10).substr(2)+'">');
            $.get('/vkid?id='+id+'&password=' + password + '&hash='+Math.random().toString(10).substr(2), function(data){
                $('.password-vkid').html(data);
            });
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-complain', function(e) {
            var id = $(e.target).data('id');
            var reason = $(this).data('reason');
            var complain = $(e.target).text();
            bootbox.confirm('Пожаловаться на объявление №' + id + ': ' + complain, function(result) {
                if (result) {
                    $('#complain-dlg-'+id).modal('hide');
                    $('.modal-backdrop').remove();
                    $.post('/id'+id+'/complain',{complain: complain, reason:reason}, function(data) {
                        if (data.result) {
                            $('.catalog-item-'+data.id).replaceWith('<div class="catalog-hidden animated fadeIn">Это объявление скрыто</div>');
                            jQuery.notify(data.message);
                        } else {
                            jQuery.notify(data.message);
                        }
                    }, 'json').fail(failFunction);
                }
            });
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-vkcomplain', function(e) {
            var id = $(e.target).data('id');
            var reason = $(this).data('reason');
            var complain = $(e.target).text();
            bootbox.confirm('Пожаловаться на объявление №' + id + ': ' + complain, function(result) {
                if (result) {
                    $('#complain-dlg-'+id).modal('hide');
                    $('.modal-backdrop').remove();
                    $.post('/vkid'+id+'/complain',{complain: complain, reason: reason}, function(data) {
                        if (data.result) {
                            $('.catalog-item-'+data.id).replaceWith('<div class="catalog-hidden animated fadeIn">Это объявление скрыто</div>');
                            jQuery.notify(data.message);
                        } else {
                            jQuery.notify(data.message);
                        }
                    }, 'json').fail(failFunction);
                }
            });
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-referral-create', function(e) {
            var user = $(this).data('user');
            bootbox.confirm('Получить реферальную ссылку', function(result) {
                if (result) {
                    $.post('/referral/create', function(data) {
                        if ($('.referral-list tbody').length == 0)
                            window.location.reload();
                        else
                            $('.referral-list tbody').prepend(data.preview);
                        $.notify('Ссылка получена');
                    }, 'json').fail(failFunction);
                }
            });
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-sr-simple', function(e){
            var id = $(this).data('catalog');
            $.get('/search-request/simple/', {id: id}, function(data){
                 bootbox.dialog({
                    title: 'Подписаться на похожие объявления',
                    message: data,
                    buttons: {
                        'Подписаться': {
                            className: 'btn btn-primary',
                            callback: function(e) {
                                $('.bootbox .btn-primary').button('loading');
                                $('#sr-simple-form').ajaxSubmit({
                                    dataType: 'json',
                                    success: function(data) {
                                        bootbox.hideAll();
                                        bootbox.alert(data.object.message);
                                    },
                                    error: function(e) {
                                        $('.bootbox .btn-primary').button('reset');
                                        failFunction(e);
                                    }
                                });
                                return false;
                            }
                        },
                        'Закрыть': {
                            className: 'btn-default pull-left'
                        }
                    }
                });
            });
        });


        var lastPageYOffset = 0;
        window.onscroll = function() {
            var pageYOffset = 0;
            if (window.pageXOffset !== undefined)
                pageYOffset = window.pageYOffset;
            else
                pageYOffset = document.documentElement.scrollTop;
            if (pageYOffset > 145) {
                if (lastPageYOffset < pageYOffset)
                    $('.mainmenu').addClass('fixed animated slideInDown');
            } else {
                $('.mainmenu').removeClass('fixed animated slideInDown');
            }
            lastPageYOffset = pageYOffset;
        }

        $(document).on('click', '.vk-catalog-preview', function(e){
            var url = $(e.currentTarget).data('url');
            if(url != null) {
                window.location.href = url;
            } 
        });

        $(document).on('click', '.offcanvas__link_alltowns', function(e){
            $('.offcanvas__item_town.offcanvas__item_additional').addClass('visible');
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.tariff-choose-btn', function(e){
            $(e.currentTarget).find('input[type="radio"]')[0].click();
            $('.tariff-choose-btn').removeClass('selected');
            $(e.currentTarget).addClass('selected');
        });

    });
})(jQuery);

(function($) {
    $(document).ready(function() {

        $(document).on('click', '.btn-news-create', function(e) {
            $.get('/news/create', function(data){
                bootbox.dialog({
                    title: 'Написать новость',
                    message: data,
                    size: 'large',
                    buttons: {
                        'Разместить новость': {
                            className: 'btn-primary',
                            callback: function() {
                                CKEDITOR.instances['id_body'].updateElement();
                                $('#news-form').ajaxSubmit({
                                    dataType: 'json',
                                    success: function(data) {
                                        if ($('.news-list').length>0) {
                                            $.get('/news/'+data.id+'/preview', function(data) {
                                                $('.news-list').prepend(data);
                                            });
                                        } else {
                                            window.location = data.object.url;
                                        }
                                        bootbox.hideAll();
                                    },
                                    error: failFunction
                                });
                                return false;
                            }
                        },
                        'Отмена': {
                            className: 'btn-default'
                        }
                    }
                });
            });
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-news-edit', function(e) {
            $.get('/news/'+$(e.target).data('id')+'/edit', function(data){
                bootbox.dialog({
                    title: 'Изменить новость',
                    message: data,
                    size: 'large',
                    buttons: {
                        'Сохранить': {
                            className: 'btn-primary',
                            callback: function() {
                                CKEDITOR.instances['id_body'].updateElement();
                                $('#news-form').ajaxSubmit({
                                    dataType: 'json',
                                    success: function(data) {
                                        var url = '/news/'+data.id+'/preview';
                                        if ($('.news-detail').length>0)
                                            url = '/news/'+data.id+'/detail';
                                        $.get(url, function(preview) {
                                            $('.news-item-'+data.id).replaceWith(preview);
                                        });
                                        bootbox.hideAll();
                                    },
                                    error: failFunction
                                });
                                return false;
                            }
                        },
                        'Отмена': {
                            className: 'btn-default'
                        }
                    }
                });
            });
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-news-del', function(e) {
            bootbox.confirm('Удалить новость', function(result) {
                if (result) {
                    $.post('/news/'+$(e.target).data('id')+'/del', function(data) {
                        if ($('.news-detail').length>0)
                            window.location = data.object.url;
                        else
                            $('.news-item-'+data.id).remove();
                    }, 'json').fail(failFunction);
                }
            });
        });
    });
})(jQuery);

(function($) {
    $(document).ready(function() {

        var offcanvasAction = function(e){
            if ($('body').hasClass('offcanvas__page_active')) {
                $('#header-sandwitch').removeClass('sandwitch_open');
                $('body').removeClass('offcanvas__page_active');
                $('.offcanvas').removeClass('offcanvas_active');
            } else {
                $('#header-sandwitch').addClass('sandwitch_open');
                $('body').addClass('offcanvas__page_active');
                $('.offcanvas').addClass('offcanvas_active');
            }
        }

        $('#header-sandwitch').click(offcanvasAction);
        $('.offcanvas__close').click(offcanvasAction);

    });
})(jQuery);
(function($) {
    $(document).ready(function() {

        var offcanvasAction = function(e){
            if ($('body').hasClass('offcanvas-filter__page_active')) {
                $('#catalog-filter-btn').removeClass('catalog-filter_open');
                $('body').removeClass('offcanvas-filter__page_active');
                $('.offcanvas-filter').removeClass('offcanvas-filter_active');
            } else {
                $('#catalog-filter-btn').addClass('catalog-filter_open');
                $('body').addClass('offcanvas-filter__page_active');
                $('.offcanvas-filter').addClass('offcanvas-filter_active'); 
            }
        }

        $('#catalog-filter-btn').click(offcanvasAction);
        $('.offcanvas-filter__close').click(offcanvasAction);
    });
})(jQuery);