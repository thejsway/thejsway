# Send data to a web server

You know now how to retrieve some data from web servers or APIs. This chapter will teach you how to send data to them.

## TL;DR

## Sensding data: the basics

Sending data to a server is usually done with via an HTTP `POST` method. In that case, the request body contains the data to be sent.

The data format depends on what the server expects. It can either be:

* Key/value pairs like when a form is directly submitted.
* JSON for more structured data.

## Sending form data

If the web server expects direct form data, you can use the JavaScript `FormData` object to encapsulate the information to be sent.

Here's an example form for choosing the strongest animal of all.

```html
<h2>Which one is the strongest?</h2>
<form>
    <p>
        <input type="radio" name="strongest" id="elephant" value="ELE" checked>
        <label for="elephant">The elephant</label>
        <br>
        <input type="radio" name="strongest" id="rhinoceros" value="RHI">
        <label for="rhinoceros">The rhinoceros</label>
        <br>
        <input type="radio" name="strongest" id="hippopotamus" value="HIP">
        <label for="hippopotamus">The hippopotamus</label>
        <br>
    </p>
    <p>
        <label for="name">Your name</label>:
        <input type="text" name="name" id="name" required>
    </p>
    <input type="submit" value="Vote">
</form>
<p id="result"></p>
```

![Form display](images/chapter23-01.png)

And here is the associated JavaScript code which handles the form submission.

```js
// Handle form submission
document.querySelector("form").addEventListener("submit", e => {
  // Cancel default behavior of sending a synchronous POST request
  e.preventDefault();
  // Create a FormData object, passing the form as a parameter
  const formData = new FormData(e.target);
  // Send form data to the server with an aynchronous POST request
  fetch("https://thejsway.glitch.me/animals", {
    method: "POST",
    body: formData
  })
    .then(response => response.text())
    .then(result => {
      document.getElementById("result").textContent = result;
    })
    .catch(err => {
      console.error(err.message);
    });
});
```

The event listener starts by disabling the default form submission behavior, which is to send a synchronous HTTP `POST` request to a server. Instead, a `FormData` object is created with the forum itself (`e.target`) as a parameter. All form fields are created as key/value pairs in this object.

Once the form fields are encapsulated in the `FormData` object, the `fetch()` method seen previously is used to send an asynchronous request to the `https://thejsway.glitch.me/animals` URL. The second parameter of the `fetch()` call sets the HTTP method as `POST` and adds the form data into the body of the request.

Lastly, the page's `result` element is updated when the server responds to the asynchronous request.

![Submission result](images/chapter23-02.png)

The `FormData` object can also be used to send custom key/value pairs to a server. Here is a very basic example form containing only a button.

```html
<button id="buyButton">Buy a new t-shirt</button>
<p id="result"></p>
```

When the user clicks on the button, custom data is added to a `FormData` object and sent to the server through an asynchronous `POST` request.

```js
// Create a new, empty FormData object
const formData = new FormData();
// Fill the object with key/value pairs
formData.append("size", "L");
formData.append("color", "blue");
// Send data to the server
fetch("https://thejsway.glitch.me/tshirt", {
  method: "POST",
  body: formData
})
  then(response => response.text())
    .then(result => {
      document.getElementById("result").textContent = result;
    })
    .catch(err => {
      console.error(err.message);
    });
```

![Submission result](images/chapter23-03.png)

## Sending JSON data

## Coding time!