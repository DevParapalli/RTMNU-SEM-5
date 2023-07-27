# P3_RegistrationForm

- HTML forms are essential components used to collect user input and send it to a web server for processing. They provide a way for users to interact with a website by entering data, making selections, and submitting the information to perform various actions, like submitting a contact form, logging in, or making a purchase.

A basic HTML form is represented using the `<form>` element, and it contains various form elements, also known as form controls, that define the input fields, buttons, and other interactive elements within the form. Let's explore some commonly used form elements and their attributes:

1. `<form>` element:
    - The `<form>` element is used to define the start and end of the form.
    - Attributes:
    - `action`: Specifies the URL of the server-side script or endpoint where form data will be sent for processing. For example, `<form action="/submit_form.php">`.
    - `method`: Specifies the HTTP method to be used when submitting the form data. Common values are "GET" and "POST". For example, `<form method="post">`.
    - `target`: Specifies where the response from the form submission will be displayed. Common values include "\_self", "\_blank", "\_parent", and "\_top".
    - `enctype`: Specifies how the form data should be encoded before being sent to the server. Common values include "application/x-www-form-urlencoded" (default), "multipart/form-data" (used when uploading files), and "text/plain".

2. `<input>` element:
    - The `<input>` element is used to create various types of form input fields.
    - Attributes:
    - `type`: Specifies the type of input field. Common values include:
    - `"text"`: Single-line text input.
    - `"password"`: Password input, where characters are masked for security.
    - `"checkbox"`: A checkbox to select one or multiple options.
    - `"radio"`: Radio buttons, allowing users to choose one option from a group.
    - `"submit"`: A button to submit the form.
    - `"reset"`: A button to reset the form to its initial values.
    - `name`: Provides a name for the input element, used to identify the input when the form is submitted.
    - `value`: Specifies the default value of the input field.
    - `placeholder`: Displays a hint or example text inside the input field.
    - `required`: If present, makes the field required and prevents the form submission until it is filled.
    - `disabled`: If present, disables the input field, preventing user interaction.

3. `<textarea>` element:
    - The `<textarea>` element is used for multi-line text input.
    - Attributes:
    - `name`: Provides a name for the textarea, used to identify the input when the form is submitted.
    - `rows`: Specifies the visible number of rows in the textarea.
    - `cols`: Specifies the visible number of columns (characters per row) in the textarea.
    - `placeholder`: Displays a hint or example text inside the textarea.

4. `<select>` element:
    - The `<select>` element creates a dropdown list (also known as a select box) for users to choose an option from.
    - Attributes:
    - `name`: Provides a name for the select element, used to identify the selection when the form is submitted.
    - `multiple`: If present, allows users to select multiple options simultaneously.
    - `<option>` element (used inside `<select>`):
    - Represents an option within the dropdown list.
    - Attributes:
    - `value`: Specifies the value sent to the server when the option is selected.
    - `selected`: If present, specifies that the option is initially selected.

5. `<button>` element:
    - The `<button>` element creates a clickable button within the form.
    - Attributes:
    - `type`: Specifies the type of button. Common values include:
    - `"submit"`: Submits the form when clicked.
    - `"reset"`: Resets the form when clicked.
    - `"button"`: A generic button that can have custom JavaScript actions associated with it.
    - `name`: Provides a name for the button, used to identify the button when the form is submitted.
    - `value`: Specifies the value sent to the server when the button is clicked.

