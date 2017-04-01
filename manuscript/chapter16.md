# React to events

To make a web page interactive, you have to respond to user actions. Let's discover ho to do so.

## TL;DR

* You can make a web page interactive by writing JavaScript code tied to **events** within the browser.

* Numerous types of events can be handled. Each event type is associated with an `Event` object that contains information about the event itself and its properties.

* `keypress`, `keydown` and `keyup` events let you react to keyboard-related events.

* `click`, `mousedown` and `mouseup` events let you react to mouse-related events.

* Page loading and closing are associated with the events `load` and `beforeunload` respectively.

* An event propagates within the DOM tree from its node of origin until the document root. This propagation can be interrupted with the `stopPropagation()` method.

## Introduction to events

Up until now, your JavaScript programs were executed right from the start. The execution order of statements was determined in advance and the only user interactions were data input through `prompt()` calls.

To add more interactivity, the page should react to the user's actions: clicking on a button, filling a form, etc. In that case, the execution order of statements is not determined in advance anymore, but depends on the user behavior. His actions trigger **events** that can be handled by writing JavaScript code.

This way of writing programs is called **event-driven programming**. It is often used by user interfaces, and more generaly anytime a program needs to interact with an user.

## A first example

Here's some starter HTML code.

```html
<button id="myButton">Click me!</button>
```

 And here's the associated JavaScript code.

```js
function showMessage() {
  alert("Hello!");
}
// Access the button
const buttonElement = document.getElementById("myButton");
// Listen to the "click" event
buttonElement.addEventListener("click", showMessage);
```

In both cases, clicking on the button shows an `"Hello!` message.

![Execution result](images/chapter16-01.png)

### Adding an event listener

Called on a DOM element, the `addEventListener()` method adds a **handler** for a particular event. This method takes as parameter the **event type** and the associated **function**. This function gets called whenever an event of the corresponding type appears for the DOM element.

The above JavaScript code could be rewritten more concisely using an anonymous function, for an identical result.

```js
// Show a message when the user clicks on the button
document.getElementById("myButton").addEventListener("click", () => {
  alert("Hello!");
});
```

Common event handling
Key presses

The most common solution for reacting to key presses on a keyboard involves handling keypress events that happen on a web page (the DOM body  element, which corresponds to the global variable called document  in JavaScript). 

To manage the press and release of any key, you'll use the keydown and keyup  events. This example uses the same function to manage two events. This time, the key's code is accessible in the keyCode property of the Event object.

// Show information on a keyboard event
function keyboardInfo(e) {
    console.log("Keyboard event:" + e.type + ", key: " + e.keyCode);
}

// Integrate this function into key press and release:
document.addEventListener("keydown", keyboardInfo);
document.addEventListener("keyup", keyboardInfo);
Test it! Type a key, any key. http://codepen.io/eclairereese/pen/QEKOrW?editors=1111 ✏️
Mouse clicks

Mouse clicks on any DOM element produce a click  type element.

Tactile interfaces like smartphones and tablets also have click events associated with buttons, which are kicked off by actually pressing a finger on the button. 
The Event object associated with a click event has a button property which lets you know the button the mouse used (left or right), as well as clientX and clientY properties that return the horizontal and vertical coordinates of the place where the click happened. These coordinates are defined relative to the page zone currently shown by the browser. 

The below code shows information on all click events that happen on a web page. These events are managed by a function called mouseInfo . 

// Return the name of the mouse button
function getMouseButton(code) {
    var button = "unknown";
    switch (code) {
    case 0: // 0 is the code for the left mouse button
        button = "left";
        break;
    case 1: // 1 is the code for the middle mouse button
        button = "middle";
        break;
    case 2: // 2 is the code for the right button
        button = "right";
        break;
    }
    return button;
}

// Show information about a mouse event
function mouseInfo(e) {
    console.log("Mouse event: " + e.type + ", button " +
        getMouseButton(e.button) + ", X : " + e.clientX + ", Y : " + e.clientY);
}

// Add mouse click event listener
document.addEventListener("click", mouseInfo);
Test it! http://codepen.io/eclairereese/pen/PzGOeV?editors=1011 ✏️
You can use mousedown and mouseup events similarly to how you saw keydown and keyup events used with keyboard events! The code below associates the same handler to two events.

// Handle mouse button press and release
document.addEventListener("mousedown", mouseInfo);
document.addEventListener("mouseup", mouseInfo);
Page loading

Depending on how complex it is, a web page can take time to be loaded 100% by the browser. You can add an event listener to know when this happens; it's an event listener on the window  object. This avoids messy situations where JavaScript interacts with pages that aren't fully loaded.

The following code displays a message in the console once the page is fully loaded.

// Web page loading event
window.addEventListener("load", function () {
    console.log("The page has been loaded!");
});
Go farther with events
Event propagation

The DOM represents a web page as a hierarchy of nodes. Events triggered on a child node are going to then trigger on the parent node, then the parent node of the parent node, up until the root of the DOM (the document variable). This is called event propagation.

To see propagation in action, add this HTML code in the <body> tag of your HTML code.

<p id="para">A paragraph with a <button id="propa">button</button> inside
</p>
Now add the complementary JavaScript code below to course.js. It adds click event handlers on the button, its parent (the paragraph), and the parent of that too (the root of the DOM). 

// Click handler on the document
document.addEventListener("click", function () {
    console.log("Document handler");
});
// Click handler on the paragraph
document.getElementById("para").addEventListener("click", function () {
    console.log("Paragraph handler");
});
// Click handler on the button
document.getElementById("propa").addEventListener("click", function (e) {
    console.log("Button handler");
});
Test it! Click the button and look at the console. http://codepen.io/eclairereese/pen/rLMYrj?editors=1111 ✏️
The result in the browser console demonstrates the propagation of click events from the button up to the document level. You clicked the button, which means you also clicked the paragraph, which means you also clicked the document. But maybe you only want an event to kick off once the button is clicked and not count its larger ecosystem!

Event propagation can be interrupted at any moment by calling the stopPropagation method on the Event object from a function that manages an event. This is useful to avoid the same event being handled multiple times.

Adding a line in the button's click handler prevents the click event from propagating everywhere in the DOM tree.

// Click handler on the button
document.getElementById("propa").addEventListener("click", function (e) {
    console.log("Button handler");
    e.stopPropagation(); // Stop the event propagation
});
