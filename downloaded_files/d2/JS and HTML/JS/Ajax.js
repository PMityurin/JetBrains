setTimeout(function() {
    console.log(7);
}, 2000);

console.log(1);
console.log(2);
console.log(3);
console.log(4);
console.log(5);
console.log(6);

let load = function(url, callback) {
    let ajax = new XMLHttpRequest();
    ajax.open('GET', url);
    ajax.onload = function() {
        callback(this.responseText);
    };
    ajax.send();
};

load('JS/text.txt', function(data) {
    console.log(data);
});

