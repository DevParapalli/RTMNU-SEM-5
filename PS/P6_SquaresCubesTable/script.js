function load(_ev) {
    if ("content" in document.createElement('template')) {
        // template tag is supported
        let template = document.querySelector('#_table-row');
        let table = document.querySelector('#tbl-sq-cu');
        for (let i = 1; i <= 10; i++) {
            let clone = template.content.cloneNode(true);
            let td = clone.querySelectorAll('td');
            td[0].textContent = i;
            td[1].textContent = i ** 2;
            td[2].textContent = i ** 3;
            table.appendChild(clone);
        }
    }
}

window.onload = load;