() => {
	profile = document.getElementsByClassName("playerprofile-item")[0];
	rare = document.getElementsByClassName("card-21")[0].className.split("-");
	rare = rare[rare.length - 1];
	
    html2canvas(profile).then(canvas => {
        canvas.id = "output";
        document.body.appendChild(canvas);
    });

    profile = document.getElementsByClassName("playerprofile-hbar-ttl")[0];
    name = profile.getElementsByTagName("h1")[0].innerText;
    profile = document.getElementsByClassName("playerprofile-hbar-ttl")[0].getElementsByTagName("div")[0];
    profile = profile.innerText.split("|");
    nationality = profile[1];
    club = profile[2];
    league = profile[3];
    rating = document.getElementsByClassName("card-21-rating")[0].innerText;
    position = document.getElementsByClassName("card-21-position")[0].innerText
    file_name = (rare+"_"+ name + ".png");
	file_name = file_name.replace(" ", "_");
    file_name = file_name.replace("\n", "");

    return {
        name : name,
        nationality : nationality,
        club : club,
        rating : rating,
        position : position,
        league : league,
		rare : rare,
        file_name: file_name
    }
}
