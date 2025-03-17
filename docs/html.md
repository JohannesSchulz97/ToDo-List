## HTML Basics

### Elements and Structure

- HTML consists of a hierarchical forest structure of elements inside other elements. Elements that can hold content (**container elements**) can be created with the following syntax:

    ```html
    <elementkeyword> 
        content inside the element 
    </elementkeyword>
    ```

- Elements can also be **self-closing**:

    ```html
    <img src="image.jpg" alt="Example">
    ```

- An HTML element can have so-called **attributes** to specify additional properties of the given element, like the `src` and `alt` attributes in the example above.

### JavaScript Integration

- JavaScript can be used inside HTML within the `<script>...</script>` element:

    ```html
    <script>
      console.log("Hello, World!");
    </script>
    ```

### High-Level Structure

1. On the top level, each HTML document needs to first define the document type inside the self-closing `<!DOCTYPE ...>` element. The exclamation mark here signals special content. (It is also used to create comments: `<!-- comment here -->`).
2. Then the **HTML root element** is defined, inside which all further elements will be contained. Inside the root element, we can find two elements, `head` and  `body`.
The `head` element contains information for the browser, while the `body` element is intended to store user content:

    ```html
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8">
        <title>My Document</title>
      </head>
      <body>
        <h1>Hello, World!</h1>
      </body>
    </html>
    ```

### Some Important Elements

- `<p>...</p>` creates a paragraph of text
- `<div>...</div>` creates a *container* to group together other elements

To create a list of elements use the following syntax:
```html
  <ul>
    <li> item1 </li>
    <li> item2 </li>
  </ul>
  ``` 
  Here, the `<ul>` keyword creates an unordered list (bullet points). To make it ordered, meaning numbered, use `<ol> ... </ol>`.
  `<li>` here stands for list item and does not need to be changed.
To create *hyperlinks*, the `<a>` element is used: 
```html
  <a href="https://www.example.com">Click here</a>
```

