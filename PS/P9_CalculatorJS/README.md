# P9_CalculatorJS

Concepts used in this practical:

1. `isNaN()`:
   `isNaN()` stands for "is Not-a-Number." It's a JavaScript function that determines whether the value provided is not a valid number. It returns `true` if the value is not a number, and `false` if it is a number. Keep in mind that `isNaN()` can be a bit tricky because it coerces non-numeric values to numbers before performing the check. This means that values like strings that can be converted to numbers (e.g., `"123"`) might return unexpected results.

   Example:
   ```javascript
   isNaN("hello"); // true
   isNaN(123);     // false
   isNaN("123");   // false
   ```

2. `innerText`:
   `innerText` is a property of a DOM element in the browser. It's used to get or set the visible text content of an element, excluding any hidden or styled elements. It retrieves the text content as a string, and you can use it to change the text displayed within an HTML element.

   Example:
   ```html
   <div id="myDiv">Hello, <span>world</span>!</div>
   ```
   ```javascript
   const myDiv = document.getElementById("myDiv");
   const textContent = myDiv.innerText; // Gets the visible text: "Hello, world!"
   myDiv.innerText = "New content";     // Sets the text: "New content"
   ```

3. `parseInt()` and `parseFloat()`:
   These are JavaScript functions used to parse strings into numbers. `parseInt()` parses a string and returns an integer, while `parseFloat()` parses a string and returns a floating-point number. They both extract as much numeric content as they can from the beginning of the string.

   Example:
   ```javascript
   const intNumber = parseInt("42");      // 42 (as an integer)
   const floatNumber = parseFloat("3.14"); // 3.14 (as a floating-point number)
   ```

4. `querySelectorAll()`:
   `querySelectorAll()` is a method provided by the Document Object Model (DOM) in web browsers. It's used to select multiple elements from the DOM that match a specified CSS selector. It returns a NodeList containing all matching elements.

   Example:
   ```html
   <ul>
     <li>Item 1</li>
     <li>Item 2</li>
     <li>Item 3</li>
   </ul>
   ```
   ```javascript
   const listItems = document.querySelectorAll("li");
   console.log(listItems.length); // Outputs: 3
   ```