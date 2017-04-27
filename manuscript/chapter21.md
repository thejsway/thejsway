# Query a web server

## TL;DR

## Writing asynchronous code: callbacks Vs promises

Understanding asynchronous code can be tricky, since statements won't be executed in a linear and sequential fashion like with synchronous operations.

Traditionally, JavaScript uses **callbacks** to performs actions asynchonously. A callback is a function executed in the future when a particular condition is met. A DOM event handler like the following one is an example of a callback.

```js
// Add a event handler (a callback) to the "click" event
document.getElementById("myButton").addEventListener("click", e => {
  // Callback code, called when the "click" event arises on the DOM element
  // ...
}};
```

However, callback-based code has a dangerous tendency to end up like this: a pyramid-shaped imbroglio of nested callback functions.

```js
// The pyramid of doom
getData(a => {
    filterData(a, b => {
        processData(b, c => {
            displayData(c, d => {
                // ...
            });
        });
    });
});
```

Code written this way is often confusing and difficult to debug. As such, it is referred as **callback hell**.

A more elegant solution for writing asynchronous code has emerged under the form of promises. A **promise** is a wrapper for an operation whose result might be available in the future.

In JavaScript, a promise is an object with `then()` and `catch()` methods. `then()` is called when the promise is **fulfilled**: the associated operation has finished successfully. It takes the operation result as a parameter. On the contrary, `catch()` is called when the promise is **rejected**: this associated operation has failed.

What's great about promises is that they can be chained together.

The previous code example could be rewritten Using promises instead of callbacks.

```js
getData()
  .then(a => filterData(a))
  .then(b => processData(b))
  .then(c => displayData(c))
  // ...
```

## Querying a web server

Let's start with a very basic example: displaying the content of a text file located on a web server. This file is located at URL `https://s3-us-west-2.amazonaws.com/s.cdpn.io/814404/languages.txt` and has the following content.

```text
C++;Java;C#;PHP
```

Check out how to retrieve that file in JavaScript.

```js
// Retrieve file from the server
fetch("https://s3-us-west-2.amazonaws.com/s.cdpn.io/814404/languages.txt")
  .then(response => {
    // Return file textual content
    return response.text();
  })
  .then(text => {
    // Display file content in the console
    console.log(text);
  });
```

This code uses the JavaScript `fetch()` function to get the file from its URL. This function launches an **asynchronous** HTTP request to a web server and returns a promise. When the HTTP response sent by the server is available, it transforms it into text and shows this text in the console.

## Dealing with errors

```js
//  .catch(err => console.error(err));
```

## Handling JSON data

```js
fetch("https://s3-us-west-2.amazonaws.com/s.cdpn.io/814404/movies.json")
  .then(response => response.json())
  .then(movies => {
    for (const movie of movies) {
      console.log(movie.titre);
    }
  }).catch(err => {
    console.error(err);
  });
```

## Coding time!
