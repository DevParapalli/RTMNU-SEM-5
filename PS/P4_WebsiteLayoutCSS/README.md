# P4_WebsiteLayoutCSS

- CSS, which stands for Cascading Style Sheets, is a fundamental web technology used to control the presentation and layout of HTML documents. It allows web developers to define how the content of a web page should be displayed, including aspects like colors, fonts, spacing, positioning, and more.

CSS works by selecting HTML elements and applying styles to them. It follows a cascading model, meaning that styles can be inherited from parent elements and overridden by more specific rules or styles defined later in the code. This helps maintain a consistent look and feel across a website while also allowing for customization on specific elements.

Basics of CSS:

1. **Selectors** : CSS selectors are patterns used to target specific HTML elements. They specify which elements the following styles should apply to. There are various types of selectors, including element selectors, class selectors, ID selectors, attribute selectors, and more.
    - Element selector: Targets HTML elements by their tag name (e.g., `p`, `h1`, `div`).
    - Class selector: Targets elements with a specific class attribute (e.g., `.my-class`).
    - ID selector: Targets a single element with a specific ID attribute (e.g., `#my-id`).
2. **Properties** : CSS properties define the visual appearance of selected elements. Each property has a name and a value. For example, to set the color of a text to red, you would use the `color` property and set its value to `red`.
3. **Declaration Block** : A set of CSS properties and their values enclosed within curly braces `{}` is known as a declaration block. It follows the selector in the CSS rule. For example:

    ```css
    h1 {
    color: blue;
    font-size: 24px;
    }
    ```

4. **Comments** : CSS allows developers to add comments to their code for documentation or explanatory purposes. Comments are ignored by the browser and start with `/*` and end with `*/`.

    ```css
    /* This is a CSS comment */
    ```

5. **Selectors and Properties Combination** : CSS rules consist of selectors and properties combined together to target HTML elements and define their styles.

    ```css
    /* Selects all paragraphs and sets their color to red */
    p {
    color: red;
    }
    ```

6. **External CSS** : CSS can be written in a separate file with a .css extension and linked to an HTML document using the `<link>` element. This approach allows you to apply the same styles to multiple pages and keeps the HTML and CSS code separated.
7. **Internal CSS** : Alternatively, CSS can be written within the `<style>` element in the head section of an HTML document. This method is useful when you need to apply specific styles to a single page.
8. **Inline CSS** : CSS styles can also be applied directly to individual HTML elements using the `style` attribute. Inline CSS should generally be avoided as it reduces code maintainability and reusability.

```html
<p style="color: green;">This text is green.</p>
```
