# Write functions

In this chapter, you'll learn how to break down a program into subparts called functions.

## TL;DR

* Une **fonction** est un regroupement d'instructions qui réalise une tâche donnée. En JavaScript, une fonction est créée à l'aide du mot-clé `function`.
* Ecrire un programme sous forme d'un ensemble de fonctions plutôt qu'en un seul bloc permet de gagner en **lisibilité** et en **modularité**.
* Les variables déclarées dans le corps d'une fonction sont appelées des **variables locales**. Leur portée se limite au corps de la fonction.
* Une fonction peut renvoyer une valeur grâce au mot-clé `return`, ou ne rien renvoyer (on parle alors de **procédure**). Elle peut également accepter ou non des **paramètres**, qui sont les données dont elle a besoin pour fonctionner.
* En JavaScript, la valeur d'une variable peut être une fonction. On peut donc créer une **fonction anonyme** et l'affecter à une variable. Pour cela, il est possible de définir la fonction de manière classique ou d'utiliser la syntaxe dite **fonction fléchée** (*fat arrow*).
* Il est important de créer des fonctions ayant un **rôle** bien défini et de limiter leur complexité. Le **nom** de la fonction, souvent basé sur un verbe à l'infinitif exprimant une **action**, doit réfléter son rôle. JavaScript offre de nombreuses fonctions prédéfinies qui peuvent simplifier la tâche du programmeur.

## Introduction: the role of functions

To understand why functions are important, check out our example from a previous chapter: the burrito algorithm :)

```text
Begin
    Get out the rice cooker
    Fill it with rice
    Fill it with water
    Cook the rice
    Chop the vegetables
    Stir-fry the vegetables
    Taste-test the vegetables
        If the veggies are good
            Remove them from the stove
        If the veggies aren't good
            Add more pepper and spices
        If the veggies aren't cooked enough
            Keep stir-frying the veggies
    Heat the tortilla
    Add rice to tortilla
    Add vegetables to tortilla
    Roll tortilla
End
```

Here's the same general idea written in a different way.

```text
Début
    Cook rice
    Stir-fry vegetables
    Add fillings
    Roll together
Fin
```

The first version details all the individual actions that make up the cooking process. The second breaks down the recipe into **broader steps** and introduces concepts that could be re-used for other dishes as well like *cook*, *stir-fry*, *add* and *roll*.

Our programs so far have mimicked the first example, but it's time to start modularizing our code into sub-steps so we can re-use bits and pieces as needed. In JavaScript, these sub-steps are called **functions**!

## Discovering functions

A **function** is a group of instructions that performs a particular task.

Here's a basic example of a function.

```js
function sayHello() {
    console.log("Hello!");
}

console.log("Start of program");
sayHello();
console.log("End of program");
```

![Execution result](images/chapter05-01.png)

Let's study what just happened.

### Declaring a function

Check out the first lines of the example above.

```js
function sayHello() {
    console.log("Hello!");
}
```

This creates a function called `sayHello()`. It consists of only one statement that will make a message appear in the console: `"Hello!"`.

This is an example of a function **declaration**.

```js
// Declaring a function called myFunction
function myFunction() {
    // Function code
}
```

The declaration of a function is performed using the JavaScript keyword `function`, followed by the function name and a pair of parentheses. Statements that make up the function constitute the **body** of the function. These statements are enclosed in curly braces and indented.

### Calling a function

Functions must be called in order to actually run. Here's the second part of our example program.

```js
console.log("Start of program");
sayHello();
console.log("End of program");
```

The first and third statements explicitly display messages in the console. The second line makes a **call** to the function `sayHello()`.

You can call a function by writing the name of the function followed by a pair of parentheses.

```js
// ...
myFunction(); // Call myFunction
// ...
```

Calling a function triggers the execution of actions listed therein (the code in its body). After it's done, execution resumes at the place where the call was made.

![Function call mechanism](images/chapter05-02.png)

### Usefulness of functions

A complex problem is generally more manageable when broken down in simpler subproblems. Computer programs are no exception to this rule. Writen as a combinaison of several short and task-focused functions, a program will be easier to understand and to update than a monolitic one. As an added bonus, some functions could be reused in other programs!

Creating functions can be a solution to the problem of [code duplication](https://en.wikipedia.org/wiki/Duplicate_code): instead of being duplicated at several places, a piece of code is centralized in a function and called from anywhere when needed.

## Possibilités des fonctions

### Valeur de retour

Voici une variante de notre programme d'exemple.

```js
function sayHello() {
    return "Hello!";
}

console.log("Début du programme");
const resultat = sayHello();
console.log(resultat);
console.log("Fin du programme");
```

Elle produit exactement le même résultat que précédemment.

Dans cet exemple, le corps de la fonction `sayHello()` a été modifié : l'instruction `console.log(...)` a été remplacée par la ligne `return "Hello!"`.

L'utilisation du mot-clé `return` dans une fonction permet de lui donner une **valeur de retour**. Son appel produit un résultat qui correspond à la valeur placée juste après le `return` dans la fonction. Ce résultat peut être récupéré par le programme appelant. Ici, la fonction `sayHello()` renvoie la valeur chaîne `"Hello!"`. Cette valeur est stockée par le programme dans la variable `resultat`, qui est ensuite affichée.

Une fonction incluant une instruction `return` renvoie une valeur de retour lorsqu'elle est appelée : l'expression située immédiatement après lereturn.

```js
// Déclaration d'une fonction nommée maFonction
function maFonction() {
    let valeurRetour;
    // Calcul de la valeur de retour
    // valeurRetour = ...
    return valeurRetour;
}

// Récupération de la valeur de retour de maFonction
const valeur = maFonction();
// ...
```

Cette valeur de retour peut être de n'importe quel type (nombre, chaîne, etc). En revanche, une fonction ne peut renvoyer qu'une seule valeur.

W> Rien n'oblige à récupérer la valeur de retour d'une fonction, mais dans ce cas, cette valeur est "oubliée" par le programme qui appelle la fonction !

Si on essaie de récupérer la valeur de retour d'une fonction qui n'inclut pas d'instruction `return`, on obtient la valeur JavaScript `undefined`.

```js
function maFonction() {
    // ...
    // Pas d'instruction return
}

const resultat = maFonction();
console.log(resultat); // Affiche undefined
```

I> Une fonction qui ne renvoie pas de valeur est parfois appelée une **procédure**.

W> L'exécution de l'instruction `return` renvoie immédiatement vers le programme appelant. Il ne faut jamais ajouter d'instructions après un `return` dans une fonction : elles ne seraient jamais exécutées.

On peut simplifier un peu notre exemple en affichant directement le résultat de l'appel à la fonction `sayHello()` sans utiliser de variable. Ici, la valeur de retour de `sayHello()` est directement affichée dans la console.

```js
function sayHello() {
    return "Hello!";
}

console.log(sayHello()); // Affiche "Hello!"
```

### Variables locales

Il est possible de déclarer des variables à l'intérieur d'une fonction, comme dans l'exemple ci-dessous.

```js
function sayHello() {
    const message = "Hello!";
    return message;
}

console.log(sayHello()); // Affiche "Hello!"
```

La fonction `sayHello()` déclare une variable nommée `message`, puis renvoie sa valeur.

Les variables déclarées dans le corps d'une fonction sont appelées des **variables locales**. En effet, leur portée se limite au corps de la fonction. Ainsi, l'exécution du programme suivant provoquera une erreur.

```js
function sayHello() {
    const message = "Hello!";
    return message;
}

console.log(sayHello()); // Affiche "Hello!"
console.log(message); // Erreur : la variable message n'existe pas ici
```

A chaque appel d'une fonction qui déclare des variables locales, ces variables sont recréées. On peut donc appeler plusieurs fois la même fonction, et chaque appel sera parfaitement indépendant des autres.

Ne pas pouvoir utiliser de variables locales en dehors des fonctions où elles sont déclarées peut sembler une limitation. C'est au contraire un double avantage :

* Une fonction peut être conçue comme une entité autonome et réutilisable.

* Un programme peut déclarer ses propres variables et utiliser autant de fonctions que nécessaire, sans se préoccuper des variables locales qui y sont déclarées.

### Passage de paramètres

Un **paramètre** est une information dont une fonction a besoin pour jouer son rôle. Les paramètres d'une fonction sont définis entre parenthèses juste après le nom de la fonction. On peut ensuite utiliser leur valeur dans le corps de la fonction.

La valeur d'un paramètre est fournie au moment de l'appel de la fonction : on dit que cette valeur est **passée en paramètre**. On appelle **argument** la valeur donnée à un paramètre lors d'un appel.

Modifions notre exemple pour construire un message de bienvenue personnalisé.

```js
function sayHello(prenom) {
    const message = `Bonjour, ${prenom} !`;
    return message;
}

console.log(sayHello("Baptiste")); // Affiche "Bonjour, Baptiste !"
console.log(sayHello("Sophie"));   // Affiche "Bonjour, Sophie !"
```

La déclaration de la fonction ‌`sayHello()` a été modifiée : elle contient à présent un paramètre nommé `prenom`.

Dans cet exemple, le premier appel à la fonction `sayHello()` est fait avec l'argument `"Baptiste"` et le second avec l'argument `"Sophie"`. Dans le premier cas, le paramètre `prenom` reçoit la valeur `"Baptiste"` et dans le second, la valeur `"Sophie"`.

Les paramètres d'une fonction sont parfois appelés des paramètres formels et les arguments des paramètres effectifs. Pour des raisons de simplicité, je préfère employer les termes de paramètre et d'argument.

Voici la syntaxe générale de la déclaration d'une fonction acceptant des paramètres. Leur nombre n'est pas limité, mais il est rarement nécessaire de dépasser 3 ou 4 paramètres.

```js
// Déclaration de la fonction maFonction
function maFonction(param1, param2, ...) {
    // Instructions pouvant utiliser param1, param2, ...
}

// Appel de la fonction maFonction
// param1 reçoit la valeur de arg1, param2 la valeur de arg2, ...
maFonction(arg1, arg2, ...);
```

Lors d'un appel à une fonction acceptant des paramètres, le nombre et l'ordre des paramètres doivent être respectés. Observez l'exemple suivant et le résultat de son exécution.

```js
function presentation(prenom, age) {
    console.log(`Tu t'appelles ${prenom} et tu as ${age} ans`);
}

presentation("Garance", 9); // Affiche "Tu t'appelles Garance et tu as 9 ans"
presentation(5, "Prosper"); // Affiche "Tu t'appelles 5 et tu as Prosper ans"
```

Lors du second appel, les valeurs données aux paramètres sont inversées : `prenom` reçoit la valeur `3` et `age` reçoit la valeur `"Prosper"`.

## Fonctions anonymes

Il existe d'autres manières de créer des fonctions en JavaScript. En voici un exemple.

```js
const Hello= function(prenom) {
    const message = `Bonjour, ${prenom} !`;
    return message;
}

console.log(bonjour("Thomas")); // Affiche "Bonjour, Thomas !"
```

La fonction créée ci-dessus est **anonyme** et directement affectée à la variable `bonjour`. La valeur de cette variable est donc une fonction.

La syntaxe pour créer une fonction anonyme et l'affecter à une variable est la suivante.

```js
// Affectation d'une fonction anonyme à la variable maVariable
const maVariable = function(param1, param2, ...) {
    // Instructions pouvant utiliser param1, param2, ...
}

// Appel de la fonction anonyme
// param1 reçoit la valeur de arg1, param2 la valeur de arg2, ...
maVariable(arg1, arg2, ...);
```

Les dernières évolutions du langage JavaScript ont introduit une syntaxe plus concise pour créer des fonctions anonymes. L'exemple suivant est strictement équivalent au précédent.

```js
const Hello= (prenom) => {
    const message = `Bonjour, ${prenom} !`;
    return message;
}

console.log(bonjour("Thomas")); // Affiche "Bonjour, Thomas !"
```

Cette syntaxe est appelée **fonction fléchée** (*fat arrow*).

```js
// Affectation d'une fonction anonyme à la variable maVariable
const maVariable = (param1, param2, ...)  => {
    // Instructions pouvant utiliser param1, param2, ...
}

// Appel de la fonction anonyme
// param1 reçoit la valeur de arg1, param2 la valeur de arg2, ...
maVariable(arg1, arg2, ...);
```

Dans certains cas particuliers, on peut simplifier la syntaxe des fonctions fléchées :

* Lorsque le corps de la fonction se limite à une seule ligne, on peut écrire son résultat sans créer de blocs de code avec des accolades. Dans ce cas, l'instruction `return` est implicite.
* Lorsque la fonction n'a qu'un seul argument, on peut omettre les parenthèses autour de celui-ci.

```js
// Dificile de faire plus concis !
const Hello= prenom => `Bonjour, ${prenom} !`;

console.log(bonjour("Thomas")); // Affiche "Bonjour, Thomas !"
}
```

Nous reviendrons plus loin sur les utilisations possibles des fonctions anonymes et les nombreuses possibilités offertes par les fonctions en JavaScript.

## Comment (bien) programmer avec les fonctions

### Créer des fonctions à bon escient

Une fonction peut utiliser les mêmes éléments qu'un programme classique : variables, conditions, boucles, etc. Une fonction peut même faire appel à une autre fonction, ce qui ouvre des possibilités infinies pour construire nos programmes.

Il convient toutefois de rester raisonnable et de ne pas multiplier artificiellement le nombre de fonctions d'un programme, sous peine de compliquer sérieusement sa compréhension. Il vaut mieux essayer de créer des fonctions ayant chacune un rôle bien défini et minimiser les interdépendances entre fonctions.

### Utiliser les fonctions prédéfinies de JavaScript

Sans les nommer ainsi, nous avons déjà utilisé plusieurs fonctions prédéfinies de JavaScript comme `prompt()` ou `alert()`. Le langage vous propose un nombre important de fonctions qui répondent à des besoins variés. En programmation comme ailleurs, il est rarement utile de réinventer la roue et il est important de privilégier l'utilisation de ces fonctions existantes plutôt qu'une réécriture manuelle.

I> La seule exception à cette règle est d'ordre pédagogique : apprendre à "faire comme" est souvent formateur.

Voici un exemple utilisant deux des nombreuses fonctions mathématiques offertes par JavaScript.

```js
console.log(Math.min(4.5, 5)); // Affiche 4.5
console.log(Math.min(19, 9));  // Affiche 9
console.log(Math.min(1, 1));   // Affiche 1
console.log(Math.random());    // Affiche un nombre aléatoire entre 0 et 1
```

La fonction `Math.min()` renvoie le minimum des nombres passés en paramètres. La fonction `Math.random()` génère un nombre aléatoire entre 0 et 1.

Nous découvrirons d'autres fonctions prédéfinies dans la suite de ce livre.

### Limiter la complexité des fonctions

Le corps d'une fonction doit garder un niveau de complexité faible et ne pas être trop long. Il n'y a pas de maximum universel, mais au-delà d'une vingtaine de lignes de code, la question de la décomposition d'une fonction en sous-fonctions doit se poser.

### Bien nommer fonctions et paramètres

Comme pour les variables, le nommage des fonctions et des paramètres joue un rôle important dans la lisibilité du programme. Les recommandations sont les mêmes : choisir des noms qui expriment précisément le rôle et respecter la norme [camelCase](https://fr.wikipedia.org/wiki/CamelCase).

Le plus souvent, on choisira un nom basé sur un verbe à l'infinitif exprimant une **action** (*calculer*, *afficher*, *trouver*, etc).

T> S'il est difficile de trouver un nom pertinent pour une fonction, c'est sans doute que son rôle n'est pas bien défini et que son existence doit être remise en cause.
