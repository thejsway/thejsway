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
const a = 3.14; // The value of a can't be modified
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

On appelle **portée** (*scope*) d'une variable la portion du code source dans laquelle cette variable est visible et donc utilisable. Les variables déclarées avec `let` et `const` ont une portée de type bloc : elles ne sont visibles qu'au sein du bloc de code dans lequel elles sont déclarées (ainsi que dans tous les sous-blocs éventuels). En JavaScript et dans de nombreux autres langages, un **bloc de code** est délimité par une paire d'accolades ouvrante et fermante. Un programme JavaScript correspond par défaut à un unique bloc de code.

```js
let var1 = 0;
{
    var1 = 1; // OK : var1 est déclarée dans le bloc parent
    const var2 = 0;
}
console.log(var1); // OK : var1 est déclarée dans le bloc courant
console.log(var2); // Erreur : var2 n'est pas visible ici
```

## La notion d'expression

Une **expression** est un morceau de code qui produit une valeur. On crée une expression en combinant des variables, des valeurs et des opérateurs. Toute expression produit une valeur et correspond à un certain type. Le calcul de la valeur d'une expression s'appelle **l'évaluation**. Lors de l'évaluation d'une expression, les variables sont remplacées par leur valeur.

```js
// 3 est une expression dont la valeur est le nombre 3
const c = 3;
// c est une expression dont la valeur est celle de c (ici 3)
let d = c;
// (d + 1) est une expression. Sa valeur est celle de d augmentée de 1 (ici 4)
d = d + 1; // d contient la valeur 4
console.log(d); // Affiche 4
```

Une expression peut comporter des parenthèses qui modifient la priorité des opérations lors de l'évaluation. En l'absence de parenthèses, la priorité des opérateurs est la même qu'en mathématiques.

```js
let e = 3 + 2 * 4; // e contient la valeur 11
e = (3 + 2) * 4; // e contient la valeur 20
```

Le langage JavaScript permet d'inclure des expressions dans une chaîne de caractères lorsque cette chaîne est délimitée par une paire d'accents graves seuls ou *backticks* (\`). Une telle chaîne est appelée un *template literal* ou littéral de gabarit. A l'intérieur, les expressions sont indiquées par la syntaxe `${expression}`.

On utilise souvent cette possibilité pour créer des chaînes intégrant des valeurs de variables.

```js
const pays = "France";
console.log(`J'habite en ${pays}`); // Affiche "J'habite en France"
const x = 3;
const y = 7;
console.log(`${x} + ${y} = ${x + y}`); // Affiche "3 + 7 = 10"
```

## Conversions de types

L'évaluation d'une expression peut entraîner des conversions de type. Ces conversions sont dites **implicites** : elles sont faites automatiquement, sans intervention du programmeur. Par exemple, l'utilisation de l'opérateur `+` entre une valeur de type chaîne et une valeur de type nombre provoque la concaténation des deux valeurs dans un résultat de type chaîne.

```js
const f = 100;
// Affiche "La variable f contient la valeur 100"
console.log("La variable f contient la valeur " + f);
```

Le langage JavaScript est extrêmement tolérant au niveau des conversions de type. Cependant, il se peut qu'aucune conversion ne soit possible. En cas d'échec de la conversion d'un nombre, la valeur du résultat est `NaN` (*Not a Number*).

```js
const g = "cinq" * 2;
console.log(g); // Affiche NaN
```

Il arrive parfois que l'on souhaite forcer la conversion d'une valeur dans un autre type. On parle alors de conversion **explicite**. Pour cela, JavaScript dispose des instructions `Number()` et `String()` qui convertissent respectivement en un nombre et une chaîne la valeur placée entre parenthèses.

```js
const h = "5";
console.log(h + 1); // Concaténation : affiche la chaîne "51"
const i = Number("5");
console.log(i + 1); // Addition numérique : affiche le nombre 6
```

## Interactions avec l'utilisateur

### Saisie et affichage à l'écran

Maintenant que nous savons utiliser des variables, nous pouvons écrire des programmes qui échangent des informations avec l'utilisateur.

```js
const prenom = prompt("Entrez votre prénom :");
alert(`Bonjour, ${prenom}`);
```

A l'exécution, une première boîte de dialogue apparaît pour demander la saisie du prénom.

![Résultat de l'exécution](images/chapter02-04.png)

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
