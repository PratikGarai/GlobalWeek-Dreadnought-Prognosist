$(document).ready(function(){
	var state = "unselect";
	var data = "";
	$(".field").click(function(){
		if (state==="select"){
			this.value = data;
			state = "unselect";
		}
	});
	$(".disease").click(function(){
		if(state==="select"){
			data = this.innerText;
		}
		else{
			state = "select";
			data = this.innerText;
		}
	});
});

