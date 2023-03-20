// console.log(document.body); 
// documentElement - <html>, body и head

// console.log(document.body.firstChild);
// firstChild - первыйй элемент, lastChild - последний элемент, childNodes - всё

// for(var i = 0; i < document.body.childNodes.length; i++) {
//     console.log(document.body.childNodes[i]);
// };

// let content = document.getElementById("content");

// let elements = content.getElementsByTagName("*");

// for(var i = 0; i < elements.length; i++) {
//     console.log(elements[i]);
// }
// console.log(content);

// let el = document.getElementsByName("fname")[0].tagName;
// console.log(el);

// let allclass = document.getElementsByClassName("some");

// console.log(allclass.length);

// let elemens = document.querySelectorAll("ul.test > li");
// тут нужно указывать теги как в  css класс через точку, id через #. querySelector выбирает только первый элемент
// console.log(elemens);

let ulItems = document.querySelector("#xer");

let parentEl = ulItems.closest("#xer"); // ближайший родительский элемент. тут нужно указывать теги как в  css

parentEl.innerHTML = "Новое значение";

let input = document.querySelector("input[type]");
if(input != null) {   
    console.log(input.value);
    input.value = "Что-то новое";

    input.setAttribute("data-bs-toggle", "some value");
    input.setAttribute("type", "text");

    if(input.hasAttribute("type")) // проверяет наличие атрибута
        alert(input.getAttribute('type')); // получаем значение атрибута
    input.className = "some new test"
    alert(input.getAttribute('class'));
    input.removeAttribute("class");
}


document.write("HTML");


input.style.backgroundColor = "red";
input.style.color = "#fff";
input.style.border = "2px solid silver";
input.style.borderRadius = "5px";
input.style.padding = "15px 10px";
