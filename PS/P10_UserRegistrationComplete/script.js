import formkitautoAnimate from 'https://cdn.jsdelivr.net/npm/@formkit/auto-animate@0.8.0/+esm'


const USERNAME = "DevParapalli"
const PASSWORD = "shhh!iamasecret"

// map to input fields
let currentUserName = ""; 
let currentPassword = "";

let TEMPLATES = new Map();

// TODO: Create onLoginPageSubmit, onSignUpPageSubmit, onForgotPageSubmit, render and load functions.
const duration = 250;

const SUN = `<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="currentColor" d="M12 17q-2.075 0-3.538-1.463T7 12q0-2.075 1.463-3.538T12 7q2.075 0 3.538 1.463T17 12q0 2.075-1.463 3.538T12 17ZM2 13q-.425 0-.713-.288T1 12q0-.425.288-.713T2 11h2q.425 0 .713.288T5 12q0 .425-.288.713T4 13H2Zm18 0q-.425 0-.713-.288T19 12q0-.425.288-.713T20 11h2q.425 0 .713.288T23 12q0 .425-.288.713T22 13h-2Zm-8-8q-.425 0-.713-.288T11 4V2q0-.425.288-.713T12 1q.425 0 .713.288T13 2v2q0 .425-.288.713T12 5Zm0 18q-.425 0-.713-.288T11 22v-2q0-.425.288-.713T12 19q.425 0 .713.288T13 20v2q0 .425-.288.713T12 23ZM5.65 7.05L4.575 6q-.3-.275-.288-.7t.288-.725q.3-.3.725-.3t.7.3L7.05 5.65q.275.3.275.7t-.275.7q-.275.3-.687.288T5.65 7.05ZM18 19.425l-1.05-1.075q-.275-.3-.275-.713t.275-.687q.275-.3.688-.287t.712.287L19.425 18q.3.275.288.7t-.288.725q-.3.3-.725.3t-.7-.3ZM16.95 7.05q-.3-.275-.288-.687t.288-.713L18 4.575q.275-.3.7-.288t.725.288q.3.3.3.725t-.3.7L18.35 7.05q-.3.275-.7.275t-.7-.275ZM4.575 19.425q-.3-.3-.3-.725t.3-.7l1.075-1.05q.3-.275.712-.275t.688.275q.3.275.288.688t-.288.712L6 19.425q-.275.3-.7.288t-.725-.288Z"/></svg>`
const MOON = `<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="currentColor" d="M12 21q-3.75 0-6.375-2.625T3 12q0-3.75 2.625-6.375T12 3q.35 0 .688.025t.662.075q-1.025.725-1.638 1.888T11.1 7.5q0 2.25 1.575 3.825T16.5 12.9q1.375 0 2.525-.613T20.9 10.65q.05.325.075.662T21 12q0 3.75-2.625 6.375T12 21Z"/></svg>`

function changeTheme() {
    const btn = document.getElementsByTagName('button')[0]
    let html = document.getElementsByTagName('html')[0];
    if (html.getAttribute('data-theme') == 'dark') {
        html.setAttribute('data-theme', 'light');
        setTimeout(() => { btn.innerHTML = MOON }, duration)
    }
    else {
        html.setAttribute('data-theme', 'dark');
        setTimeout(() => { btn.innerHTML = SUN }, duration)
    }
}

/**
 * This function is called whenever an input event is triggered.
 * @param {InputEvent} event 
 */
function inputHandler(event) {}

/**
 * DOMContentLoaded stuff
 */
function load() {
    const btn = document.getElementsByTagName('button')[0]
    btn.innerHTML = MOON;
    btn.addEventListener('click', changeTheme);
    
    formkitautoAnimate(document.querySelector('main'), { duration: 250, easing: 'ease-in-out' });
    
    document.querySelectorAll('template').forEach((template) => {
        TEMPLATES.set(template.id, template.content.cloneNode(true));
    })

    // console.log(TEMPLATES);
    render('login-page');
}

/**
 * Sets up content, event listeners, change page title, href handlers etc.
 * 
 * @param {string} id contains id of the template to render
 */
function render(id) {
    const main = document.querySelector('main');
    main.innerHTML = "";
    main.appendChild(TEMPLATES.get(id));
    main.setAttribute('data-page', id);

    document.querySelector('.sub-title').innerHTML = id;
}


document.addEventListener('DOMContentLoaded', load);