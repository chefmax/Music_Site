(function(){

        createCookie = function(){
        	if (getCookie("show_search") == null )
        		return setCookie("show_search","NO","/")
                else if (getCookie("show_search") == "NO") {
                                document.getElementById('head').style.display = 'none';
                                return "NO"
                        }
                        else {
                                document.getElementById('head').style.display = '';
                                return "Yes"  
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

        function setCookie(name, value, path) {
                var curCookie = name + "=" + escape(value) + "; path = /" 
                if ((name + "=" + escape(value)).length <= 4000)
                        document.cookie = curCookie
                else
                        if (confirm("Cookie превышает 4KB и будет вырезан !"))
                                document.cookie = curCookie

        }
        

        window.onload = createCookie 
})()