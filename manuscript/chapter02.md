# Play with variables

You know how to use JavaScript to display values. However, for a program to be truly useful, it must be able to store data, like information entered by a user. Let's check that out.

## TL;DR

* Une **variable** est une zone de stockage d'information. Chaque variable possède un **nom**, une **valeur** et un **type**. En JavaScript, le type d'une variable est déduit implicitement de sa valeur, et non pas défini explicitement. Il s'agit d'un langage à typage **dynamique**.
* On déclare une variable JavaScript avec le mot-clé `let` suivi du nom de la variable. Si la valeur initiale d'une variable n'est pas destinée à changer, on utilise de préférence le mot-clé `const` pour déclarer une variable **constante**.
* L'opérateur d'affectation `=` permet de donner une valeur à une variable. Dans le cas d'une variable de type nombre, on peut utiliser les opérateurs `+=` et `++` pour incrémenter (augmenter de 1) sa valeur.
* La **portée** (*scope*) d'une variable représente la portion du code source dans laquelle cette variable est utilisable. Les variables définies avec `let` et `const` ont une portée de type bloc : elles ne sont utilisables qu'à l'intérieur du **bloc de code** dans lequel elles sont définies. Un bloc de code est délimité par une paire d'accolades ouvrante et fermante.
* Une **expression** est un morceau de code combinant des variables, des valeurs et des opérateurs. L'évaluation d'une expression produit une valeur et correspond à un certain type.
* On peut inclure des expressions dans une chaîne de caractères délimitée par une paire d'accents graves seuls (\`) et appelée *template literal*.
* Des **conversions de types** peuvent avoir lieu implicitement lors de l'évaluation d'une expression, ou bien explicitement avec les instructions `Number()` et `String()` qui convertissement respectivement une expression en un nombre et en une chaîne.
* Les instructions `prompt()` et `alert()` permettent respectivement de faire saisir et d'afficher une information sous la forme d'une boîte de dialogue.
* Il est essentiel de bien nommer ses variables et d'adopter une convention de nommage, comme par exemple *camelCase*.

## Variables

### Role of a variable

A computer program stores data using variables. A **variable** is an information storage area. We can imagine it as a box in which you can put and store things!

### Variable properties

A variable has three main properties:

* Its **name**, which identifies it. A variable name may contain upper and lower case letters, numbers (not in the first position) and characters like the dollar (`$`) or underscore (`_`).
* Its **value**, which is the data stored in the variable.
* Its **type**, which determines the role and actions available to the variable.

I> You don't have to define a variable type explicitly in JavaScript. Its type is deduced from the value stored in the variable and may change while the program runs. That's why we say that JavaScript is a **dynamically typed** language. Other languages, like C or Java, require variable types to always be defined. This is called **static typing**.

### Declaring a variable

Before you can store information in a variable, you have to create it! This is called declaring a variable. **Declaring** a variable means the computer reserves memory in which to store the variable. The program can then read or write data in this memory area by manipulating the variable.

Here's a code example that declares a variable and shows its contents:

```js
let a;
console.log(a);
```

In JavaScript, you declare a variable with the `let`  keyword followed by the variable name. In this example, the variable created is called `a`.

I> In previous versions of the language, variables were declared using the `var` keyword.

Here's the execution result for this program.

![Execution result](images/chapter02-01.png)

Note that the result is `undefined`. This is a special JavaScript type indicating no value. I declared the variable, calling it `a`, but didn't give it a value!

### Assign values to variables

While a program is running, the value stored in a variable can change. To give new value to a variable, use the `=` operator called the **assignment operator**.

Check out the example below:

```js
let a;
a = 3.14;
console.log(a);
```

![Execution result](images/chapter02-02.png)

We modified the variable by assigning it a value. `a = 3.14` reads as "a receives the value 3.14".

E> Be careful not to confuse the assignment operator `=` with mathematical equality! You'll soon see how to express equality in JavaScript.

You can also combine declaring a variable and assigning it a value in one line. Just know that, within this line, you're doing two different things at once:

```js
let a = 3.14;
console.log(a);
```

### Declaring a constant variable

If the initial value of a variable won't ever change during the rest of program execution, this variable is called a **constant**. This constantness can be enforced by using the keyword `const` instead of `let` to declare it. Thus, the program is more expressive and further attempts to modify the variable can be detected as errors.

```js
const a = 3.14; // The value of a cannot be modified
a = 6.28;       // Impossible!
```

![Attempt to modify a constant variable](images/chapter02-03.png)

### Increment a number variable

You can also increase or decrease a value of a number with `+=`  and `++`. The latter is called an **increment operator**, as it allows incrementation (increase by 1) of a variable's value.

In the following example, lines 2 and 3 each increase the value of variable b  by 1.

```js
let b = 0;      // b contains 0
b += 1;         // b contains 11
b++;            // b conttains 2
console.log(b); // Shows 2
```

### Variable scope

The **scope** of a variable is the part of the program where the variable is visible and usable. Variables declared with `let` or `const` are **block-scoped**: their visibility is limited to the block where they are declared (and every sub-block, if any). In JavaScript and many other programming languages, a **code block** is a portion of a program delimited by a pair of opening and closing braces. By default, a JavaScript program forms one block of code.

```js
let nb1 = 0;
{
    nb1 = 1; // OK : nb1 is declared in the parent block
    const nb2 = 0;
}
console.log(nb1); // OK : nb1 is declared in the current block
console.log(nb2); // Error! nb2 is not visible here
```

## Expressions

An **expression** is a piece of code that produces a value. An expression is created by combining variables, values and operators. Every expression has a value and thus a type. Calculating an expression's value is called **evaluation**. During evaluation, variables are replaced by their values.

```js
// 3 is an expression whose value is 3
const c = 3;
// c is an expression whose value is the value of c (3 here)
let d = c;
// (d + 1) is an expression whose value is d's + 1 (4 here)
d = d + 1; // d now contains the value 4
console.log(d); // Show 4
```

Operator priority inside an expression is the same as in math. However, an expression can integrate **parenthesis** that modify these priorities.

```js
let e = 3 + 2 * 4; // e contains 11 (3 + 8)
e = (3 + 2) * 4;   // e contains 20 (5 * 4)
```

It is possible to include expressions in a string by using **backticks** (\`) to delimitate the string. Such a string is called a **template literal**. Inside a template literal, expressions are identified by the `${expression}` syntax.

This is often used to create strings containing the values of some variables.

```js
const country = "France";
console.log(`I live in ${country}`); // Show "I live in France"
const x = 3;
const y = 7;
console.log(`${x} + ${y} = ${x + y}`); // Show "3 + 7 = 10"
```

## Type conversions

An expression's evaluation can result in type conversions. These are called **implicit** conversions, as they happen automatically without the programmer's intervention. For example, using the `+` operator between a string and a number causes the concatenation of the two values into a string result.

```js
const f = 100;
// Show "Variable f contains the value 100"
console.log("Variable f contains the value " + f);
```

JavaScript is extremely tolerant in terms of type conversion. However, sometimes conversion isn't possible. If a number fails to convert, you'll get the result `NaN`  (*Not a Number*).

```js
const g = "five" * 2;
console.log(g); // Show NaN
```

Sometimes you'll wish to convert the value of another type. This is called **explicit** conversion. JavaScript has the `Number()`  and `String()` instructions that convert the value between the parenthesis to a number or a string.

```js
const h = "5";
console.log(h + 1); // Concatenation: show the string "51"
const i = Number("5");
console.log(i + 1); // Numerical addition: show the number 6
```

## User interactions

### Entering and displaying information

Once you start using variables, you can write programs that exchange information with the user.

```js
const name = prompt("Enter your first name:");
alert(`Hello, ${name}`);
```

During execution, an alert box pops up, asking for your name.

![Execution resultn](images/chapter02-04.png)

Cette boîte est le résultat de l'exécution de l'instruction JavaScript `prompt("Entrez votre prénom :")`.

Après saisie du prénom, une seconde boîte affiche un "bonjour" personnalisé.

![Résultat de l'exécution](images/chapter02-05.png)

La valeur saisie dans la première boîte de dialogue a été stockée dans une variable de type chaîne nommée `prenom`. Ensuite, l'instruction JavaScript `alert()` a déclenché l'affichage de la seconde boîte, contenant le message d'accueil.

### Affichege dans la console

Nous avons vu dans le précédent chapitre que l'instruction JavaScript `console.log()` permettait d'afficher une information.

I> On désigne par "console" une zone d'informations textuelles. L'instruction `console.log()` ne fait pas à proprement parler partie de la spécification du langage JavaScript. Cependant, la très grande majorité des environnements JavaScript, et notamment les navigateurs web, disposent d'une console dans laquelle il est possible d'afficher des informations.

On peut donc utiliser soit `console.log()`, soit `alert()` pour afficher des informations à l'utilisateur. Contrairement à `alert()`, `console.log()` ne bloque pas l'exécution du programme, ce qui en fait parfois un meilleur choix.

Il est possible d'utiliser `console.log()` pour afficher plusieurs valeurs simultanément, en les séparant par des virgules.

```js
const temp1 = 36.9;
const temp2 = 37.6;
const temp3 = 37.1;
console.log(temp1, temp2, temp3); // Affiche "36.9 37.6 37.1"
```

### Saisie d'un nombre

Quel que soit le texte saisi, l'instruction `prompt()` renvoie toujours une valeur de type chaîne. Il faudra penser à convertir cette valeur avec l'instruction `Number()` si vous souhaitez ensuite la comparer à d'autres nombres ou l'utiliser dans des expressions mathématiques.

```js
const saisie = prompt("Entrez un nombre : "); // saisie est de type chaîne
const nb = Number(saisie); // nb est de type nombre
```

Il est possible de combiner les deux opérations (saisie et conversion) en une seule ligne de code, pour un résultat identique :

```js
const nb = Number(prompt("Entrez un nombre : ")); // nb est de type nombre
```

Ici, le résultat de la saisie utilisateur est directement converti en une valeur de type nombre par l'instruction `Number()` et affecté à la variable `nb`.

## Importance du nommage des variables

Pour clore ce chapitre, j'aimerais insister sur un aspect parfois négligé par les développeurs débutants : le nommage des variables. Le nom choisi pour une variable n'a pour la machine aucune importance, et le programme fonctionnera de manière identique. Rien n'empêche de nommer toutes ses variables `a`, `b`, `c`...,  voire de choisir des noms absurdes comme `steackhache` ou `jesuisuncodeurfou`.

Et pourtant, la manière dont sont nommées les variables affecte grandement la facilité de compréhension d'un programme. Observez ces deux versions du même exemple.

```js
const nb1 = 5.5;
const nb2 = 3.14;
const nb3 = 2 * nb2 * nb1;
console.log(nb3);
```

```js
const rayon = 5.5;
const pi = 3.14;
const perimetre = 2 * pi * rayon;
console.log(perimetre);
```

Leur fonctionnement est strictement identique, et pourtant la compréhension du second est beaucoup plus rapide grâce aux noms choisis pour ses variables.

Comment faire pour bien nommer les variables de ses programmes ?

### Choisir des noms significatifs

La règle la plus importante est de donner à toute variable un nom qui reflète son rôle. C'est bien le cas dans le second exemple ci-dessus : les variables `rayon`, `pi` et `perimetre` stockent respectivement le rayon d'un cercle, la valeur du nombre PI et le périmètre calculé.‌

### Bannir les caractères accentués

Les caractères accentués comme `é` ou `à` sont mal supportés dans certains environnements et sont inconnus du monde anglophone. Mieux vaut les éviter : on nommera une variable `perimetre` plutôt que `périmètre`.

### Ne pas utiliser les noms réservés du langage

Les mots-clés du langage JavaScript sont des noms réservés. Ils ne doivent pas être utilisés comme noms de variables. Vous trouverez sur [cette page](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Mots_r%C3%A9serv%C3%A9s) la liste des noms réservés de JavaScript.

### Adopter une convention de nommage

Il faut parfois plusieurs mots pour décrire le rôle de certaines variables. Dans ce cas, on a intérêt à adopter une **convention de nommage**, c'est-à-dire une manière uniforme d'écrire les noms de toutes les variables. Il en existe plusieurs. Dans ce cours, nous allons adopter la plus fréquemment utilisée : la norme [camelCase](https://fr.wikipedia.org/wiki/CamelCase) (appelée parfois *lowerCamelCase*). Elle repose sur deux grands principes :

* Tout nom de variable commence par une **lettre minuscule**.
* Si le nom d'une variable se compose de plusieurs mots, la première lettre de chaque mot (sauf le premier) s'écrit en **majuscule**.

Par exemple, les noms `montantTravauxMaison` et `codeClientSuivant` respectent la norme *camelCase*.

W> Comme de nombreux langages, JavaScript fait la distinction entre majuscules et minuscules. On dit qu'il est **sensible à la casse** (*case sensitive*). Par exemple, `mavariable` et `maVariable` seront considérées comme deux variables différentes. Attention aux étourderies !
