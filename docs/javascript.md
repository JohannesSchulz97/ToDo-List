## JavaScript

In general, JavaScript is a coding language that is used to create dynamic web content.
Meaning that it is what allows users to interact with websites. 
When loading a webpage, the browser creates a so called **Document Object Model (DOM)**, a tree-like representation of the websites content. 
JavaScript is able to access this **DOM**, to change and modify its structure.

### Global Objects
1. the `console` variable can be used to access the console, mostly to print information or organize output in general. The simplest use case is the standard `log()` function: `console.log("Hello, world!");`

### Selecting Elements

To retrieve a single element from the DOM, we can make use of the `id` attribute: 
```js
document.getElementById("myButton");
```
More flexible however, is the `querySelector()` method: 
```js
const button = document.querySelector("#buttonID");
const button = document.querySelector(".buttonClass");
```
It allows us to retrieve the first element that matches a given **CSS selector**, meaning that we can select by class, id, tag, other attributes or nested elements (**#id**, **.class**, ...).

If we want to retrieve all elements that match a certain CSS signature we can instead use the `document.querySelectorAll()` function.


### Further Points
1. Constants and Variables can be defined in the following way: 
```js
let name = "Buddy";  // Can be reassigned
const age = 3;       // Cannot be reassigned
```
2. Compared to Java, JavaScript runs directly in the browser (not in the **JVM**) where it has access to the **DOM**. It has dynamic types and is a **procedural language**, in contrast to Java which is object oriented (an **OOP language**). So it is no longer necessary for code to be within classes, although that is also supported. Code in **procedural languages** is executed from top to bottom, whereas **OOP languages** need a designated entry point (*main()* function)
3. It is possible to dynamically add or remove classes for an element: 
```js
document.querySelector("button").classList.add("active");
```


