function change(idName) {
	if(getCookie("show_search") == "NO") {
		deleteCookie("show_search")
		setCookie("show_search","Yes","/")
    	document.getElementById(idName).style.display = '';
  	} 
  	else 
  	{
  		deleteCookie("show_search")
		  setCookie("show_search","NO","/")
    	document.getElementById(idName).style.display = 'none';
  	}
  	return false;
}


function setCookie(name, value, path) {
        var curCookie = name + "=" + escape(value) + "; path = /" 
        if ((name + "=" + escape(value)).length <= 4000)
                document.cookie = curCookie
        else
                if (confirm("Cookie превышает 4KB и будет вырезан !"))
                        document.cookie = curCookie
}

function deleteCookie(name, path) {
        if (getCookie(name)) {
                document.cookie = name + "=" + 
                 "; path = /" + "; expires=Thu, 01-Jan-70 00:00:01 GMT"
        }
}

function getCookie(name) {
        var prefix = name + "="
        var cookieStartIndex = document.cookie.indexOf(prefix)
        if (cookieStartIndex == -1)
                return null
        var cookieEndIndex = document.cookie.indexOf(";", cookieStartIndex + prefix.length)
        if (cookieEndIndex == -1)
                cookieEndIndex = document.cookie.length
        return unescape(document.cookie.substring(cookieStartIndex + prefix.length, cookieEndIndex))
}