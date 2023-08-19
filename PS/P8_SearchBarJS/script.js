// This file assumes PRODUCTS is defined before.

function search(query) {
    return PRODUCTS.filter((product) => product.Product.toLowerCase().includes(query.toLowerCase()));
}

function modifyTableProducts(products) {
    const tableBody = document.querySelector('#product-table>tbody');
    tableBody.innerHTML = '';
    for (let product of products) {
        const row = document.createElement('tr');
        const name = document.createElement('td');
        const price = document.createElement('td');
        name.innerText = product.Product;
        price.innerText = product.Price;
        row.appendChild(name);
        row.appendChild(price);
        tableBody.appendChild(row);
    }
}


document.addEventListener('DOMContentLoaded', () => { 
    modifyTableProducts(PRODUCTS) 
});

document.getElementById('search').addEventListener('click', (event) => {
    const query = document.getElementById('search-input').value;
    if (query === '') {
        document.querySelector('.body').setAttribute('data-search-active', 'false');
        modifyTableProducts(PRODUCTS);
        return;
    }
    document.querySelector('.body').setAttribute('data-search-active', 'true');
    document.querySelector('#search-value').innerText = query;
    modifyTableProducts(search(query));
});