(function(){
	var a_re = /[cdu]\_\d+\_[cdu]/, a_color = 1
	function hc(s, c) {return (" " + s + " ").indexOf(" " + c + " ") !== -1}
	function ac(e, c) {var s = e.className; if (!hc(s, c)) e.className += " " + c}
	prepTabs = function (t){
		var el, th, cs, c, cell, axis, ts = (t && t.className) ? [t] : document.getElementsByTagName("table")
		for (var e in ts) {
			el = ts[e]
			if (hc(el.className, "sortable")) {
				if (!el.tHead) {
					th = document.createElement("thead")
					th.appendChild(el.rows[0])
					el.appendChild(th)
				}
				th = el.tHead
				ac(th, "c_0_c")
				th.title = "Сортировать"
				th.onclick = clicktab
				el.sorted = NaN
			}
		}
	}
	var clicktab = function (e) {
		e = e || window.event
		var obj = e.target || e.srcElement
		while (!obj.tagName.match(/^(th|td)$/i)) obj = obj.parentNode
		var i = obj.cellIndex, t = obj.parentNode
		while (!t.tagName.match(/^table$/i)) t = t.parentNode
		
		var cn = obj.className, verse = /d\_\d+\_d/.test(cn),
		dir = (verse) ? "u" : "d", new_cls = dir + "_" + a_color + "_" + dir
		if (a_color < 8) a_color++
		if (a_re.test(cn)) obj.className = cn.replace(a_re, new_cls)
		else obj.className = new_cls
		
		var j = 0, tb = t.tBodies[0], rows = tb.rows, l = rows.length, c, v, vi
		if (i !== t.sorted) {
			t.sarr = []
			for (j; j < l; j++) {
				c = rows[j].cells[i]
				v = (c) ? (c.innerHTML.replace(/\<[^<>]+?\>/g, "")) : ""
				vi = Math.round(100 * parseFloat(v)).toString()
				if (!isNaN(vi)) while (vi.length < 10) vi = "0" + vi
				else vi = v
				t.sarr[j] = [vi + (j/1000000000).toFixed(10), rows[j]]
			}
		}
		t.sarr = t.sarr.sort()
		if (verse) t.sarr = t.sarr.reverse()
		t.sorted = i
		for (j = 0; j < l; j++) tb.appendChild(t.sarr[j][1])
		obj.title = "Отсортировано по " + ((verse) ? "убыванию" : "возрастанию")
	}
	window.onload = prepTabs
})()
