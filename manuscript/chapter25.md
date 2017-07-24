# Create a web server

## TL;DR

TODO

## Using a framework

We saw in the previous chapter that Node.js was a platform for building JavaScript applications outside the browser. as such, Node is well suited for creating **web servers** in JavaScript.

> As a reminder, a web server is a machine built specially to publish resources on the Web.

### About frameworks

It's entirely possible to build a web server from scratch with Node, but we'll take a different approach and use a framework for it.

In computer programming, a **framework** provides a standard way to design and structure an application. It typically takes care of many low-level details so that the developer can concentrate on high-level, business-related tasks.

### Choosing a framework

Among the many possible frameworks for creating a web server in JavaScript, we'll use one of the most well-known: **Express**. To paraphrase its [web site](http://expressjs.com/), Express is "a minimal and flexible Node.js web application framework that provides a robust set of features for web and mobile applications".

In other words, Express provides a foundation on which you can easily and quickly build a web server.

### Installing Express

The Express framework is available as an npm package and its installation is straightforward. First, you'll need an existing Node application with a  `package.json` file it. Run the following command in a terminal open in your application folder to install Express as a dependency.

```console
npm install express
```

As an alternative, you can directly add Express as a dependency in your `package.json` file and run the `npm install` command.

```json
"dependencies": {
  "express": "^4.15.3"
},
```

## Responding to requests

The main job of a web server is to respond to HTTP requests. Here's the JavaScript code for a minimal Express-based web server that returns `"Hello from Express!"` for a request to the root URL.

```js
// Load the Express package as a module
const express = require("express");

// Access the exported service
const app = express();

// Return a string for requests to the root URL ("/")
app.get("/", (request, response) => {
  response.send("Hello from Express!");
});

// Start listening to incoming requests
// If process.env.PORT is not defined, port number 3000 is used
const listener = app.listen(process.env.PORT || 3000, () => {
  console.log(`Your app is listening on port ${listener.address().port}`);
});
```

You can launch your server with commands `node index.js` or `npm start`, then type its root URL (<http://localhost:3000> if your server runs on your local machine) in a browser. You should see the string `"Hello from Express!"` appear.

![Execution result](images/chapter25-01.png)

Let's dissect this example.

### Accessing Express services

Once Express is installed, you can load its package in your main application file and access the exported services provided by the framework. The beginning of the server code does just that.

```js
// Load the Express package as a module
const express = require("express");

// Access the main Express object
const app = express();
```

### Defining routes

In web development terminology, a **route** is an entry point into an application. It is relative to the application URL. The `"/"` route matches the root of the application.

```js
// Return a string for requests to the root URL ("/")
app.get("/", (request, response) => {
  response.send("Hello from Express!");
});
```

When an HTTP request is made to the route URL, the associated callback function is executed. This function takes as parameters objects representing the HTTP request and response. Here, the function body sends a text response with the content `"Hello from Express!"`.

### Listening to requests

To detect incoming request, a web server must listen on a specific port. A **port** is a communication endpoint on a machine.

The main Express object has a `listen()` method that taks as parameter the listening port and a callback function called for each request. The last part of the server code calls this method to start listening.

```js
// Start listening to incoming requests
// If process.env.PORT is not defined, 3000 is used
const listener = app.listen(process.env.PORT || 3000, () => {
  console.log(`Your app is listening on port ${listener.address().port}`);
});
```

## Publishing data

Our web server is pretty limited for now, handling only one route and always returning the same string. Let's create our own little API by publishing some data in JSON format.

To match what was done on the client side in a previous chapter, we'll publish some blog articles. The API route is `"/api/articles"`, and the associated callback return a list of JavaScript objects.

Here's the code to be added to the server *before* the last part (the one that starts the listening).

```js
// Define a list of articles
const articles = [
  { id: 1, title: "First article", content: "Hello World!" },
  {
    id: 2,
    title: "Lorem ipsum",
    content:
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut hendrerit mauris ac porttitor accumsan. Nunc vitae pulvinar odio, auctor interdum dolor. Aenean sodales dui quis metus iaculis, hendrerit vulputate lorem vestibulum."
  },
  {
    id: 3,
    title: "Lorem ipsum in French",
    content:
      "J’en dis autant de ceux qui, par mollesse d’esprit, c’est-à-dire par la crainte de la peine et de la douleur, manquent aux devoirs de la vie. Et il est très facile de rendre raison de ce que j’avance."
  }
];

// Return the articles list in JSON format
app.get("/api/articles", (request, response) => {
  response.json(articles);
});
```

When accessing the `"/api/articles"` route (<http://localhost:3000/api/articles> if your server runs locally) with a browser or a specialized tool like Postman or RESTClient, you should see the article list in JSON format.

![Execution result](images/chapter25-02.png)

## Accepting data

Our web server offers a *read-only* service: it publishes some data but doesn't accept any... Until now!

As you saw in a previous chapter, information submitted to a web server can be either form data or JSON data.

### Enabling Cross-Origin Resource Sharing

TODO

### Handling form data

Form data comes encapsulated into the HTTP `POST` request sent by the client to the server. The first server task is to extract this information from the request. The simplest way to do this is to use a specialized npm package, such as [multer](https://www.npmjs.com/package/multer).

```json
"dependencies": {
  ...
  "multer": "^1.3.0"
},
```

Once **multer** is installed, add the following code towards the beginning of your server main file.

```js
// Load the multer package as a module
const multer = require("multer");

// Access the exported service
const upload = multer();
```

The following route accepts form data sent to the `"/animals"` route.

```js
// Handle form data submission to the "/animals" route
app.post("/animals", upload.array(), (request, response) => {
  const name = request.body.name;
  const vote = request.body.strongest;
  response.send(`Hello ${name}, you voted: ${vote}`);
});
```

The values of the `name` and `vote` variables are extracted from the request body, and a string is constructed and sent back to the client.

### Handling JSON data

TODO: cars

## Coding time!

### T-shirt color

### New article

### Visited countries
