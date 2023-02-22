const selectors = document.querySelectorAll(".selector");
for (j = 0; j < selectors.length; j++) {

	selectors[j].addEventListener("click", (e) => {
		e.preventDefault();
    })

    filterObjects("all");

    function filterObjects(c){
        var x, i;
        x = document.getElementsByClassName("products");
        if(c == "all") c = "";
        for(i = 0; i < x.length; i++) {
            x[i].addEventListener("click", (e) => {
                e.preventDefault();
            })
            removeClass(x[i], "show");
            if(x[i].className.indexOf(c) > -1) addClass(x[i], "show");
        }
    }

    function addClass(element, name) {
        var i, arr1, arr2;
        arr1 = element.className.split(" ");
        arr2 = name.split(" ");
        for(i = 0; i < arr2.length; i++){
            if(arr1.indexOf(arr2[i]) == -1){
                element.className += " " + arr2[i];
            }
        }
    }

    function removeClass(element, name){
        var i, arr1, arr2;
        arr1 = element.className.split(" ");
        arr2 = name.split(" ");
        for (i = 0; i < arr2.length; i++){
            while(arr1.indexOf(arr2[i]) > -1){
                arr1.splice(arr1.indexOf(arr2[i]), 1);
            }
        }
        element.className = arr1.join(" ");
    }
}


// Search Filter
function search_product() {
	let input = document.getElementById('search').value
	input=input.toLowerCase();
	let x = document.getElementsByClassName('product');
	
	for (i = 0; i < x.length; i++) {
		if (!x[i].innerHTML.toLowerCase().includes(input)) {
			x[i].style.display="none";
		}
		else {
			x[i].style.display="list-item";				
		}
	}
}

