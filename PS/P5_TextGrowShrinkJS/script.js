let size = 5;
let interval;
let is_growing = true;

function interval() {
    if (is_growing) {
        let text = document.getElementById("text");
        text.style.fontSize = (size++) + "pt";
        text.style.color = "red";
        text.innerHTML = "TEXT-GROWING"
        if (size > 50) {
            is_growing = false;
        }
    } else {
        let text = document.getElementById("text");
        text.style.fontSize = (size--) + "pt";
        text.style.color = "blue";
        text.innerHTML = "TEXT-SHRINKING"
        if (size < 5) {
            is_growing = true;
        }
    }
}


interval = setInterval(interval, 100);
setTimeout(() => {
    clearInterval(interval);
}, 10000)

