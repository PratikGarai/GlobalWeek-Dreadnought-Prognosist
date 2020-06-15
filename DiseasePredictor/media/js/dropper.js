var max_n = 7;
$(document).ready(function(){
   $("#submit").click(function(event){
      var box = $("div#selections div");
      var inputs = $("input.field");
      for( var i=0;i<box.length;i++)
      {
         inputs[i].value = box[i].innerText;
      }
      $("#target-form").submit()
   });
   max_n = $(".field").length;
});
var count = 0;
function allowDrop(ev) {
   ev.preventDefault();
}
function drag(ev) {
   ev.dataTransfer.setData("text", ev.target.id);
}
function drop1(ev) {
   if(count===max_n)
   {
      alert ("All "+ max_n+ " elements selected");
      return ;
   }
   var _target = $("#" + ev.target.id);
   var data = ev.dataTransfer.getData("text");
     if ($(_target).hasClass("noDrop")) {
        console.log("no transfer");
        ev.preventDefault();
      } else {
        ev.preventDefault();
        ev.target.appendChild(document.getElementById(data));
	count++;
      }
}
function drop2(ev) {
  var _target = $("#" + ev.target.id);
  var data = ev.dataTransfer.getData("text");
  if ($(_target).hasClass("noDrop")) {
    console.log("no transfer");
    ev.preventDefault();
  } else {
    ev.preventDefault();
    ev.target.appendChild(document.getElementById(data));
    count--;
  }
}
