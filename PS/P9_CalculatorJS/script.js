// Display
const DIGITS_D = document.getElementById("digit-display");
const OPERATOR_D = document.getElementById("operator-display");

// State Machine Variables
let A = "";
let B = "";
let operator = "";


function buttonClick(ev) {
    // Go back to initial state
    if (ev.target.innerText === "CL") {
        A = "";
        B = "";
        operator = "";
        DIGITS_D.innerText = "";
        OPERATOR_D.innerText = "";
        return;
    }
    // Dot already present
    if (ev.target.innerText === "." && DIGITS_D.innerText.includes(".")) {
        return;
    }
    // Too long number
    if (DIGITS_D.innerText.length > 10) {
        return;
    }
    // Evaluate
    if (ev.target.innerText === "=") {
        let a = parseFloat(A);
        let b = parseFloat(B);
        if (isNaN(a) || isNaN(b)) {
            alert("Invalid input");
            buttonClick({ target: { innerText: "CL" } }) // Hacky way to reset
        }
        let result = 0;
        switch (operator) {
            case "+":
                result = a + b;
                break;
            case "-":
                result = a - b;
                break;
            case "*":
                result = a * b;
                break;
            case "/":
                result = a / b;
                break;
        }
        DIGITS_D.innerText = result.toString().slice(0, 10);
        A = result.toString();
        B = "";
        operator = "";
        OPERATOR_D.innerText = "";
        return;
    }
    // Number
    if (!isNaN(parseInt(ev.target.innerText))) {
        if (operator === "") {
            A += ev.target.innerText;
            DIGITS_D.innerText = A;
        } else {
            B += ev.target.innerText;
            DIGITS_D.innerText = B;
        }
        return;
    }
    // Dot
    if (ev.target.innerText === ".") {
        if (operator === "") {
            A += ev.target.innerText;
            DIGITS_D.innerText = A;
        } else {
            B += ev.target.innerText;
            DIGITS_D.innerText = B;
        }
        return;
    }
    // Operator
    if (isNaN(parseInt(ev.target.innerText))) {
        if (operator === "") {
            operator = ev.target.innerText;
            OPERATOR_D.innerText = operator;
        } else {
            buttonClick({ target: { innerText: "=" } });
            operator = ev.target.innerText;
            OPERATOR_D.innerText = operator;
        }
    }
}

for (let button of document.querySelectorAll(".button-group button")) {
    button.addEventListener("click", buttonClick);
}




