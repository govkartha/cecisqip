var slider = document.getElementById("myRange");
var slider1 = document.getElementById("myRange1");
var output = document.getElementById("demo");
var output1 = document.getElementById("demo1");
output.innerHTML = slider.value;
output1.innerHTML = slider1.value;

slider.oninput = function() {
    output.innerHTML = this.value;
}

slider1.oninput = function() {
    output1.innerHTML = this.value;
}