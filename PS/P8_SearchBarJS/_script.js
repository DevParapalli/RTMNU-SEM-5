// This file assumes PRODUCTS is defined before.

/**
 *  Returns the matching parameter, how much of the first string matches the second string
 * @param {string} string1 
 * @param {string} string2 
 * @returns {number} closeness
 */
function findCloseness(string1, string2) {
    let param = 0;
    for (let char of string1.toLowerCase()) {
        if (string2.toLowerCase().includes(char)) {
            param++;
        }
    }
    for (let char of string2.toLowerCase()) {
        if (string1.toLowerCase().includes(char)) {
            param++;
        }
    }
    return param / ((string1.length + string2.length));
}

function search(query) {
    return PRODUCTS.filter((product) => findCloseness(query, product.Product) > 0.5);
}



console.log(search("b"))