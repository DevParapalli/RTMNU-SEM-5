function vowelPosition(string) {
    for (let char of string) {
        if (['a', 'e', 'i', 'o', 'u'].includes(char.toLowerCase())) {
            return `Leftmost Vowel is at ${string.indexOf(char)} index`;
        }
    }
    return 'No Vowel Found';
}

function reverseNumber(num) {
    let numStr = num.toString();
    let numStrRev = numStr.split('').reverse().join('');
    return parseInt(numStrRev);
}

function load(_ev) {
    const func1 = document.getElementById('func1');
    const func2 = document.getElementById('func2');
    const input = document.getElementById('str');
    func1.addEventListener('click', () => {
        alert(vowelPosition(input.value ?? ''));
    });
    func2.addEventListener('click', () => {
        alert(reverseNumber(parseInt(input.value, 10) ?? 0));
    });
}

window.addEventListener('load', load);