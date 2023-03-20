let text = document.querySelector(".full-text");

text.onkeydown = function(e) { // oninput позволяет отследить даже вставку текста
    console.log('onkeydown:' + text.value);
};

text.onkeypress = function(e) { 
    console.log('onkeypress: ' + text.value);
};

text.onkeyup = function(e) { 
    console.log("onkeyup: " + text.value);
};

let boldText = document.querySelectorAll("p > b.bold-txt");

boldText.forEach((item, i) => {
    item.onmousedown = function() {
        item.style.color = "red";
    };
    
    item.onmouseup = function() {
        item.style.color = "blue";
    };
    
    item.oncontextmenu = function() {
        item.style.color = "green";
    };
});



let inputField = document.querySelector('.input');
let helpField = document.querySelector('.hint');

inputField.onmouseenter = function() {
    helpField.style.display = "block";
};

inputField.onmousemove = function(e) {
    helpField.style.left = e.offsetX + "px";
    helpField.style.top = e.offsetY + "px";
}

inputField.onmouseleave = function() {
    helpField.style.display = "none";
};