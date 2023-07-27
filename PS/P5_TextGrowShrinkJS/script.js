let size = 5;
let _interval;

function interval() {
    let text = document.getElementById("text");
    text.style.fontSize = (size++) + "pt";
    console.log(size);
    if (size > 50) {
        text.style.fontSize = "5pt";
        text.style.color = "blue";
        text.innerHTML = "TEXT-SHRINKING"
        clearInterval(_interval);
    }
}


_interval = setInterval(interval, 100);

