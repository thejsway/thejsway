# Style guide {#style-guide}

Here are the coding rules and principles used throughout the book.

> This chapter is by nature subjective and opinionated. Feel free to make your own choices.

## Naming

Naming things right goes a long way into making code cleaner and easier to understand. Some general naming rules are presented below.

### Choose meaningful names

The most important rule is to give each element (variable, function, class, etc) a specific name that reflects its role. A variable holding the value of a circle radius should be named `radius` rather than `num` or `myVal`.

Brevity should be limited to short-lived elements, like loop counters.

### Don't use reserved words

Each JavaScript keyword is a reserved name. They should not be used as variable names. Here's the [list of reserved words in JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#Keywords).

### Follow a naming convention

It can take several words to describe precisely the role of certain elements. This book adopts the popular [camelCase](https://en.wikipedia.org/wiki/Camel_case) naming convention, based on two main principles:

* All names begin with a **lowercase** letter.
* If a name consists of several words, the first letter of each word (except the first word) is **uppercase**.

In addition, this book uses the following naming rules:

* Functions and method names include an **action verb**: `computeTotal()`, `findFirstParent()`, `attackTarget()`, etc.
* To be consistent with other programming languages, class names start with an **uppercase** letter: `User` instead of `user`.
* Since they may contain multiple elements, arrays are named **plurally** or suffixed with `List`: `movies` or `movieList`, but not `movie`.
* To distinguish them from other variables, DOM elements are suffixed with `Element` (or `Elements` for array-like variables): `divElement` rather than simply `div`.

W> Like many other languages, JavaScript is **case sensitive**. For example, `myVariable` and `myvariable` are two different variable names. Be careful!

## Code formatting

This is a subject of many debates in the JavaScript community: using spaces or tabulations for indenting, omitting semicolons, simple vs double quotes for strings, and so on.

A simple and efficient solution is to rely on a tool to automate the low-level task of formatting code, so that you can concentrate on more high-level work. This book uses [Prettier](https://github.com/prettier/prettier) with default configuration (double quotes and semicolons).

## Code quality

Since JavaScript is a dynamically typed language, a number of errors don't show up until execution: misnaming a function, loading a nonexistent module, etc. In addition, many other mistakes like declaring a variable without ever using it won't affect execution outcome, but make your code harder to read and lower its overall quality.

Fortunately, specialized tools called **linters** can check your code against rules during edition and warn about potential defects. By allowing to fix many bugs before they happen, linters greatly enhance developer productivity.

This book uses [ESLint](http://eslint.org) for linting code. ESLint is a very flexible tool and you can tailor it to your specific needs. Different set of ESLint rules have emerged, notably one based on the popular [AirBnb Style Guide](https://github.com/airbnb/javascript).

> This opinionated style guide is well worth a read.

This book's ESLint configuration extends the AirBnb and Prettier rules (Prettier getting the precedence), with a few minor deviations.

Here is the content of the book's `.eslintrc` configuration file.

```json
{
  "extends": ["airbnb", "prettier"],
  "env": {
    "browser": true
  },
  "plugins": ["prettier"],
  "rules": {
    "no-console": "off",
    "no-alert": "off",
    "no-plusplus": "off",
    "default-case": "off",
    "no-param-reassign": [
      "error",
      {
        "props": false
      }
    ],
    "arrow-body-style": [
      "error",
      "as-needed",
      { "requireReturnForObjectLiteral": true }
    ]
  }
}
```

The deviations from predefined rules are explained below.

* `"no-console"` and `"no-alert"`: to enable `console.XXX()` and `alert()` calls.
* `"no-plusplus"`: to enable unary operators like `++`, commonly used and generally harmless.
* `"default-case"`: to enable `switch` statements without a `default` case, which are common.
* `"no-param-reassign"`: to enable updating properties of an object passed as a parameter.
* `"arrow-body-style"`: to use the more explicit `return` syntax for arrow functions that return an object literal.
