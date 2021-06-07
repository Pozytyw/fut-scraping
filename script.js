() => {
	x = document.getElementsByClassName("table-row")
	list = [];
	for(elem of x){
		var link = elem.getElementsByTagName("a")[0].href;
		var name = elem.getElementsByClassName("name")[0].innerText;
		list.push([link, name])
	}
	
	return list
}