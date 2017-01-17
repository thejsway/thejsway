# 3, 2, 1... Code!

Let's get started! This chapter will introduce you to the fundamentals of programming including values, types, and program structure.

## TL;DR

* The JavaScript instruction `console.log()` displays a message.
* A **value** is a piece of information. The **type** of a value defines its role and the operations applicable to it.
* The JavaScript language uses the **number** type to represent a numerical value (with or without decimals) and the **string** type to represent text.
* A string value is surrounded by a pair of single quotes (`'...'`) or a pair of quotation marks (`"..."`).
* Arithmetic operations between numbers are provided by the `+`, `-`, `*` and `/` operators. Applied to two strings, the `+` operators joins them together. This operation is called **concatenation**.
* A computer program is made of several **lines of code** read sequentially during execution.
* **Comments** (`// ...` or `/* ... */`) are non-executed parts of code. They form a useful program documentation.

## Your first program

Here's our very first JavaScript program.

```javascript
console.log("Hello from JavaScript!");
```

This program displays the text `"Hello from JavaScript!"` in the **console**. To achieve that, its uses a JavaScript order named `console.log()`, which role is to display a piece of information. The displayed text is placed between parenthesis and followed by a semicolon, which mark the end of the line.

Displaying a text on the screen (the famous [Hello World](https://en.wikipedia.org/wiki/Hello_world) all programmers know) is often the first thing you'll do when you learn a new programming language. It's the classic example. You've already taken that first step!

## Values and types

A **value** is a piece of information used in a computer program. Values exist in different forms called types. The **type** of a value determines its role and operations available to it.

Every computer language has its own types and values. Let's look at two of the types available in JavaScript.

### Number

A **number** is a numerical value (thanks Captain Obvious). Let's go beyond that though! Like mathematics, you can use integer values (or whole numbers) such as 0, 1, 2, 3, etc, or real numbers with decimals for greater accuracy.

Numbers are mainly used for counting. The main operations you'll see are summarized in the following table. All of them produce a number result.

|Operator|Role|
|---------|----|
|`+`|Addition|
|`-`|Soustraction|
|`*`|Multiplication|
|`/`|Division|

### String

A **string** in JavaScript is text surrounded by quotation marks, such as `"This is a string"`. 

I> You can also define strings with a pair of single quotes: `'This is another string'`. The best practice for single or double quotes is a whole political thing. Use whichever you like, but don't mix the two in the same program!

W> Always remember to close a string with the same type of quotation marks you started it with.

To include special characters in a string, use the `\` character (*backslash*) before the character. For example, type `\n` to add a new line within a string: `"This is\na multiline string"`.

You can not add or remove string values like you'd do with numbers. However, the `+` operator has a special meaning when applied to two string values. It will join the two chains together, and this operation is called a **concatenation**. For example, `"Hel" + "lo"` produces the result `"Hello"`.

## Program structure

We already defined a computer program as a list of commands telling a computer what to do. These orders are written as text files and make up what's called the "source code" of the program. The lines of text in a source code file are called **lines of code**.

I> The source code may include empty lines: these will be ignored when the program executes.

### Statements

Each instruction inside a program is called a **statement**. A statement in JavaScript usually ends with a **semicolon** (albeit it's not strictly mandatory). Your program will be made up of a series of these statements.

I> You usually write only one statement per line.

### Execution flow

When a program is executed, the statements in it are "read" one after another. It's the combination of these individual results that produces the final result of the program.

Here's an example of a JavaScript program including several statements.

```js
console.log("Hello from JavaScript!");
console.log("Let's do some math");
console.log(4 + 7);
console.log(12 / 0);
console.log("Goodbye!");
```

![Execution result](images/chapter01-01.png)

I> On remarque au passage qu'une division par zéro (ici `12/0`) produit, comme attendu, un résultat infini (`Infinity`).

### Commentaires

Par défaut, chaque ligne de texte dans les fichiers source d'un programme est considérée comme une instruction à exécuter. Il est possible d'exclure certaines lignes de l'exécution en les préfixant par une double barre oblique `//`. Ce faisant, on transforme ces lignes en **commentaires**.

```js
console.log("Bonjour en JavaScript !");
//console.log("Faisons quelques calculs.");
console.log(4 + 7);
//console.log(12 / 0);
console.log("Au revoir !");
```

Lors de l'exécution, les lignes commentées ne produisent plus de résultat.

![Résultat de l'exécution](images/chapter01-03.png)

Les commentaires servent à donner des informations sur le programme et sont destinées au programmeur, non à la machine.

I> Il existe une autre manière de créer des commentaires en entourant une ou plusieurs lignes par les caractères `/*` et `*/`.
I>
I>     /* Un commentaire
I>     sur plusieurs
I>     lignes */
I>
I>     // Un commentaire sur une seule ligne

Les commentaires fournissent une aide précieuse pour comprendre le code source d'un programme. Il est important de décrire les parties importantes ou compliquées d'un programme grâce à des commentaires. Prenez cette bonne habitude dès maintenant !
