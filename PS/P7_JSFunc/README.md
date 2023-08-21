# P7_JSFunc

1. **Event Handling:**
Event handling in JavaScript refers to the process of responding to events that occur in the web browser, such as user interactions like clicks, keypresses, mouse movements, and more. These events can be captured and handled by attaching event listeners to specific HTML elements. When an event occurs, the associated event listener's callback function is executed, allowing you to respond to the event by performing certain actions or executing specific code.

2. **Event Listeners:**
Event listeners are functions in JavaScript that "listen" for specific events on HTML elements and execute a designated callback function when the event occurs. They are used to create interactivity in web applications. Event listeners can be added to elements using methods like `addEventListener`. Here's a basic example of attaching an event listener for a button click:

   ```javascript
   const button = document.getElementById('myButton');

   button.addEventListener('click', function() {
       console.log('Button clicked!');
   });
   ```

3. **Nullish Coalescing (??):**
Nullish coalescing is a JavaScript operator (`??`) used to provide a default value when dealing with values that might be `null` or `undefined`. It's a way to handle cases where you want to use a fallback value only if the original value is `null` or `undefined`, not when it's a falsy value like `false`, `0`, or an empty string.

   ```javascript
   const someValue = null;
   const fallbackValue = 'Fallback';

   const result = someValue ?? fallbackValue;
   console.log(result); // Output: 'Fallback'
   ```

4. **Alerts:**
In JavaScript, the `alert()` function is used to display a dialog box with a message and an "OK" button. It's commonly used for simple notifications or alerts to users. Here's an example:

   ```javascript
   alert('This is an alert message.');
   ```

   However, `alert()` has limitations, such as blocking the execution of further code until the user interacts with the alert box. As a result, it's often considered a less user-friendly way of displaying information compared to using other methods like manipulating the DOM or using modal dialogs.
