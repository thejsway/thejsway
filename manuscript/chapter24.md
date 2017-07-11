# The Node.js platform

In this chapter, you'll discover how to create JavaScript applications outside the browser thanks to a technology called Node.js.

## TL;DR

## Introducing Node.js

### A bit of history

To understand what Node.js (or Node for short) is, we have to travel back in time to the 2000's. As JavaScript was becoming increasingly important for improving the user experience on the web, web browser designers spent a considerable amount of resources on executing JS code as fast as possible. In particular, the Chrome JavaScript engine, codenamed V8, became open source in 2008 and was a huge step forward in general performance and optimization.

![Chrome V8 logo](images/chapter24-01.png)

The core idea behind Node.js was simple yet visionary: since the V8 engine is so good at executing code, why not leverage its power to create efficient JavaScript applications *outside the browser*? And thus Node.js was born in 2009, originally written by Ryan Dahl. Its project quickly became very popular and Node is now one of the top technologies for building apps and creating APIs with JavaScript.

![The offical Node logo](images/chapter24-02.png)

Node also made it easier for developers to publish, share and reuse code. Today, hundreds of thousands of ready-to-use JavaScript libraries, called **packages**, are available and easy to integrate in any Node-based project (more on that later). This rich ecosystem is one of Node's greatest strengths.

### A first example

> The rest of this chapter assumes a working Node environnement. Refer to the [appendix](#env-setup) for setting one up.

The simplest possible Node program is as follows.

```js
console.log("Hello from Node!");
```

As you see, the `console.log()` command is also available in Node. Just like in a web browser, it outputs the value passed as parameter to the console. Assuming this code is saved into a file named `hello.js`, here's how to execute it through Node in a terminal.

```console
node hello.js
```

An in-depth study of the Node platform is out of this book's scope. Let's focus on two of its defining features: **modules** and **packages**.

## Node.js modules

The general idea behind modules is pretty straighforward and similar to the one behind functions. Instead of writing all the code in one place, thus creating a monolithic application, it's often better to split the functionalities into smaller, looslety coupled parts. Each part should focus on a specific task, making it far easier to understand and reuse. The general application's behavior results from the interactions between its parts.

These smaller parts are sometimes referred to as components. In Node, they are called **modules** and can come under different forms.

### Creating a module

The simplest form of module is a single file of JavaScript code, containing special commands to **export** specific pieces of it. The rest of the code is **private** to the module and won't be visible outside of it.

For example, a `greetings.js` file could contain the following code.

```js
// Create three functions
const sayHello = name => `Hello, ${name}`;
const flatter = () => `Look how gorgeous you are today!`;
const sayGoodbye = name => `Goodbye, ${name}`;

// Export two of them
module.exports.sayHello = sayHello;
module.exports.flatter = flatter;
```

In Node, functions are *exported* (made accessible outside) by specifying additional properties on the special `module.exports` object. Here, two functions are exported under the names `sayHello` and `flatter`. The third one is not exported.

This module could have been written in a slightly more concise way by directly defining the functions as properties of the `module.exports` object.

```js
// Create and export two functions
module.exports.sayHello = name => `Hello, ${name}`;
module.exports.flatter = () => `Look how gorgeous you are today!`;

// Create a non-exported function
const sayGoodbye = name => `Goodbye, ${name}`;
```

### Loading a module

Assuming both files are located in the same directory, another JavaScript file could load the previously created module by using the `require()` function provided by Node.js.

```js
// Load the module "greetings.js"
const greetings = require("./greetings.js");

// Use exported functions
console.log(greetings.sayHello("Baptiste")); // "Hello, Baptiste"
console.log(greetings.flatter()); // "Look how gorgeous you are today!"
console.log(greetings.sayGoodbye("Baptiste")); // Error: sayGoodbye doesn't exist
```

The parameter passed to `require()` identifies the module to load. Here, the `"./"` substring at the beginning indicates a **relative path**: the module should be searched for in the same directory as the file that loads it.

The result of the call to `require()` is an object, named `greetings` here. This object references the value of the `module.exports` object defined inside the module. Thus, the `greetings` object has two functions `sayHello` and `flatter` as properties. Trying to access its non-existent `sayGoodbye` property triggers an error during execution.

> Giving the object resulting from a call to `require()` the same name as the loaded module's name, through not mandatory, is a common practice.

### Exposing an object

Numerous modules in the Node.js ecosystem expose only a single object aggregating all of the module's functionality. To do so, they reassign the `module.exports` object instead of adding properties to it.

For example, check out how the following module `calculator.js` is defined.

```js
// Declare a factory function that returns an object
function createCalc() {
  return {
    add(x, y) {
      return x + y;
    },
    substract(x, y) {
      return x - y;
    },
    multiply(x, y) {
      return x * y;
    },
    divide(x, y) {
      return x / y;
    }
  };
}

// Export the factory function
module.exports = createCalc;
```

In this module, the only exported element is a function that returns an object. Using it is as follows.

```js
// Load the module "calculator.js"
const calculator = require("./calculator.js");

// Create an object by calling the exported function of this module
const calc = calculator();

// Use the object's methods
console.log(`2 + 3 = ${calc.add(2, 3)}`); // "2 + 3 = 5"
```

The result of the call to `require()` is a function stored in the `calculator` variable, referencing the `createCalc()` function. Calling this function returns an object with several methods, which can be subsequently used.

### Exposing a class

When you want a module to only export a specific class, you can also reassign the `module.exports` object.

Here is a module `user.js` that defines and exports a `User` class.

```js
// Export a class User
module.exports = class User {
  constructor(firstName, lastName) {
    this.firstName = firstName;
    this.lastName = lastName;
    // Create user login by combining first letter of first name + last name
    this.login = (firstName[0] + lastName).toLowerCase();
  }
  describe() {
    return `${this.firstName} ${this.lastName} (login: ${this.login})`;
  }
};
```

Here's how to use this class in another file located in the same folder.

```js
// Load the module "user.js"
const User = require("./user.js");

// Instantiate the exported class
const johnDoe = new User("John", "Doe");
console.log(johnDoe.describe());
```

## Node.js packages

### The Node.js package ecosystem

### Using an external package

## Coding time!

### Saying goodbye

### Accounting

### Playing with dates