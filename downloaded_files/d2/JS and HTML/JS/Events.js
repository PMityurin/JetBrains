function clickHref() {
    alert('Привет всем');
    document.querySelector("a.href").style.color = "#333";
    document.querySelector("a.href").style.textDecoration = "none"; 
    // style.display = "none";
};

let input =  document.querySelector("input");
let textArea =  document.querySelector("#comment");

function clickText(selector) {
    alert('Привет всем');
    document.querySelector(selector).style.color = "red";
    document.querySelector(selector).style.backgroundColor = "black"; 
    // .style.display = "none";
};

function focusE() {
    input.style.backgroundColor = "#333";
    input.style.padding = "10px";
    input.style.border = "0px";
};

function blurE() {
    input.style.backgroundColor = "#fff";
    input.style.padding = "0px";
    input.style.border = "1px solid silver";
};

input.onclick = function() {
    console.log("Click");
};

input.onmouseover = function() {
    console.log("onmouseover");
};
window.ondblclick = function() {
    console.log("Click 2x");
};

window.onresize = function() {
    console.log("onresize");
};

window.onload = function() {
    console.log("Страница загружена");
};

window.onscroll = function() {
    console.log("Scroll");
};

textArea.onkeyup = function() {
    console.log("Что-то печатает..");
};

// --------------------------------

let block = document.querySelector("div.block");

function handlerOver() {
    block.innerHTML = "New text";
};

function handlerOut() {
    block.innerHTML = "Привет мир!";
}

block.addEventListener("mouseover", handlerOver);

block.addEventListener("mouseout", handlerOut);

block.removeEventListener("mouseout", handlerOut);