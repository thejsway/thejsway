# Add conditions

Up until now, all the code in our programs has been executed chronologically. Let's enrich our code by adding conditional execution!

## TL;DR

* L'instruction `if` permet d'exprimer une **condition**. Les instructions associées au `if` n'est exécuté que si la condition est vérifiée (vraie). Une **condition** est une expression dont l'évaluation produit une valeur **booléenne** (`true` ou `false`).

* Les instructions associées à une instruction `if` sont regroupées dans un **bloc de code** délimité par une paire d'accolades ouvrante et fermante. Pour plus de lisibilité, le contenu d'un bloc de code être **indenté** (décalé vers la droite) par rapport à l'instruction `if` à laquelle il est associé.

* Les opérateurs `===`, `!==`, `<`, `<=`, `>` et `>=` peuvent être utilisés pour comparer des nombres au sein d'une condition. Ils renvoient tous un résultat booléen.

* Associée à un `if`, l'instruction `else` permet d'exprimer une **alternative**. Selon la valeur de la condition, le bloc de code associé au `if` ou celui associé au `else` sera exécuté, mais jamais les deux. On peut imbriquer sans limite des instructions `if/else` à l'intérieur d'autres instructions `if/else`.

* Les opérateurs logiques `&&` (ET), `||` (OU) et `!` (NON) permettent de créer des conditions composées.

* L'instruction `switch` permet d'exécuter un bloc de code parmi plusieurs selon la valeur d'une expression.

## What's a condition?

Suppose we want to write a program that makes enter a number to the user, who then displays a message if the number is positive. Here the corresponding algorithm.

```text
Enter a number
Si the number is positive
    Display a message
```

The message should display only if the number is positive: this means it's "subject" to a **condition**.

### The `if` statement

Here's how you translate the program to JavaScript.

```js
const number = Number(prompt("Enter a number:"));
if (number > 0) {
    console.log(`${number} is positive`);
}
```

The `console.log(...)` command is executed only *if* the number is positive. Test this program to see for yourself!

Conditional syntax looks like this:

```js
if (condition) {
    // Statements executed when the condition is true
}
```

The pair of opening and closing braces defines the block of code associated with an `if` statement. This statement represents a **test**. It results in the following: "If the condition is true, then executes the instructions contained in the code block".

The condition is always placed in parentheses after the `if`. The statements within the associated code block are shifted to the right. This practice is called **indentation** and helps make your code more readable. As your programs grow in size and complexity, it will become more and more important. The indentation value is often 2 or 4 spaces.

I> When the code block has only one statement, braces may be omitted. As a beginner, you should nonetheless always use braces when writing your first conditions.

### Conditions

A **condition** is an expression that evaluates as a value either true or false: it's called a **boolean** value. When the value of a condition is true, we say that this condition is satisfied.

We have already studied numbers and strings, two types of data in JavaScript. Booleans are another type. This type has only two possible values: `true` and `false`.

Any expression producing a boolean value (either `true` or `false`) can be used as a condition in an `if` statement. If the value of this expression is `true`, the code block associated with it is executed.

```js
if (true) {
    // The condition for this if is always true
    // This block's instructions will always be executed
}
if (false) {
    // The condition for this if is always false
    // This block's instructions will never be executed
}
```

Boolean expressions can be created using the comparison operators shown in the following table.

|Operator|Meaning|
|---------|----|
|`===`|Equal|
|`!==`|Not equal to|
|`<`|Less than|
|`<=`|Less than or equal to|
|`>`|Greater than|
|`>=`|Greater than or equal to|

In some other programming languages, equality and inequality operators are `==` and `!=`. They also exist in JavaScript, but it's safer to use `===` and `!==` ([more details](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness)).

E> It's easy to confuse comparison operators like `===` (or `==`) with the assignment operator `=`. They're very, very different. Be warned!

Now let's modify the example code to replace `>` with `>=` and change the message, then test it with the number 0.

```js
const number = Number(prompt("Enter a number:"));
if (number >= 0) {
    console.log(`${number} is positive or zero`);
}
```

If the user input is 0, the message appears in the console, which means that the condition`(number >= 0)` was satisfied.

## Alternative conditions

You'll often want to have your code execute one way when something's true and another way when something's false.

### The `else` statement

Enrichissons notre programme d'exemple pour qu'il affiche un message adapté au nombre saisi par l'utilisateur.

```js
const nombre = Number(prompt("Entrez un nombre :"));
if (nombre > 0) {
    console.log(`${nombre} est positif`);
}
else {
    console.log(`${nombre} est négatif ou nul`);
}
```

Selon le nombre saisi, un message adapté est toujours affiché dans la console. Notre programme agit différemment selon que la condition `(nombre > 0)` soit vraie ou fausse : c'est ce que l'on appelle une **alternative**.

Une alternative s'exprime en JavaScript grâce à l'instruction `else` associée à un `if`. Voici sa syntaxe.

```js
if (condition) {
    // instructions exécutées quand la condition est vraie
}
else {
    // instructions exécutées quand la condition est fausse
}
```

On peut traduire une instruction `if/else` comme ceci : "Si la condition est vraie, alors exécute les instructions du bloc de code associé au `if`, sinon exécute celles du bloc de code associé au `else`".

L'instruction `if/else` permet de créer un **branchement logique** à l'intérieur d'un programme. Pendant l'exécution, les instructions exécutées seront différentes selon la valeur de la condition. Un seul des deux blocs de code sera pris en compte.

### Imbriquer des conditions

Notre programme d'exemple peut encore être enrichi pour afficher un message spécifique si le nombre saisi est nul. Pour cela, le code doit être modifié de la manière suivante.

```js
const nombre = Number(prompt("Entrez un nombre :"));
if (nombre > 0) {
    console.log(`${nombre} est positif`);
} else { // nombre <= 0
    if (nombre < 0) {
        console.log(`${nombre} est négatif`);
    } else { // nombre === 0
        console.log(`${nombre} est nul`);
    }
}
```

Ce programme affiche bien un message adapté au nombre saisi, y compris lorsque ce nombre est 0.

C'est maintenant qu'il faut faire appel à votre sens logique pour le comprendre. Si le premier bloc `else` est exécuté, c'est que le nombre saisi est soit négatif, soit nul, puisque la condition`(nombre > 0)` du premier `if` n'a dans ce cas pas été vérifiée. A l'intérieur de ce bloc `else`, on vérifie si le nombre est strictement négatif avec la condition `(nombre < 0)`. Si cette condition est fausse, alors le nombre est forcément égal à 0.

I> Les commentaires présents sur les lignes de chaque instruction else donnent des précisions sur la condition lorsque ce blocelse est exécuté. Ils sont optionnels mais aident à comprendre le code. Je vous conseille de vous entraîner à écrire ce genre de commentaires lorsque vous imbriquez des conditions.

Il est possible de représenter graphiquement l'exécution du programme précédent au moyen d'un **diagramme de flux** qui montre les différents cheminements possibles selon la valeur du nombre saisi.

![Diagramme de flux du programme d'exemple](images/chapter03-01.png)

Cet exemple nous montre que l'indentation permet de bien visualiser les différents blocs crées par les instructions `if/else`. Il n'y a pas de limite (si ce n'est la lisibilité du programme) au niveau de profondeur des imbrications.

On rencontre fréquemment le cas particulier où la seule instruction d'un bloc `else` est un `if` (le `else` éventuellement associé à ce `if` ne compte pas comme une seconde instruction). Dans ce cas, il est possible d'écrire ce `if`  sur la même ligne que le premier `else`, sans accolades ni indentation. Ainsi, notre programme d'exemple peut être réécrit de la manière suivante.

```js
const nombre = Number(prompt("Entrez un nombre :"));
if (nombre > 0) {
    console.log(`${nombre} est positif`);
} else if (nombre < 0) {
    console.log(`${nombre} est négatif`);
} else {
    console.log(`${nombre} est nul`);
}
```

## Créer des conditions composées

### L'opérateur logique ET

Supposons qu'on souhaite vérifier qu'un nombre est compris entre 0 et 100. Cela signifie que le nombre doit être à la fois supérieur à 0 et inférieur à 100. La condition "nombre compris entre 0 et 100" peut s'exprimer sous la forme de deux sous-conditions "nombre supérieur ou égal à 0" et "nombre inférieur ou égal à 100". Il faut que l'une ET l'autre de ces sous-conditions soient vérifiées.

I> L'expression `0 <= nombre <= 100` est mathématiquement exacte mais ne peut pas s'écrire de cette manière en JavaScript (ni dans la plupart des autres langages de programmation).

La traduction en JavaScript de cette condition donne le résultat suivant.

```js
if ((nombre >= 0) && (nombre <= 100)) {
    console.log(`${nombre} est compris entre 0 et 100`);
}
```

I> Les parenthèses entre les sous-conditions ne sont pas obligatoires. Cependant, je vous conseille de les ajouter systématiquement dans un premier temps pour mieux visualiser la structure des conditions et éviter d'éventuelles mauvaises surprises liées aux priorités des opérateurs.

L'opérateur `&&` (ET logique) s'applique à deux valeurs de type booléen. Son résultat est la valeur `true` uniquement si les deux valeurs auxquelles il s'applique valent `true`.

```js
console.log(true && true);   // Affiche true
console.log(true && false);  // Affiche false
console.log(false && true);  // Affiche false
console.log(false && false); // Affiche false
```

Le résultat ci-dessus constitue ce qu'on appelle la **table de vérité** de l'opérateur `&&`.

### L'opérateur logique OU

Imaginons maintenant qu'on souhaite vérifier qu'un nombre est en dehors de l'intervalle [0, 100]. Pour satisfaire à cette condition, ce nombre doit être inférieur à 0 OU supérieur à 100.

Traduit en JavaScript, cet exemple donne le résultat suivant.

```js
if ((nombre < 0) || (nombre > 100)) {
    console.log(`${nombre} est en dehors de l'intervalle [0, 100]`);
}
```

L'opérateur `||` (OU logique) s'applique à deux valeurs de type booléen. Son résultat est la valeur true si au moins une des deux valeurs auxquelles il s'applique vaut `true`. Voici la table de vérité de l'opérateur `||`.

```js
console.log(true || true);   // Affiche true
console.log(true || false);  // Affiche true
console.log(false || true);  // Affiche true
console.log(false || false); // Affiche false
```

### L'opérateur logique NON

Il existe un troisième opérateur logique qui permet d'inverser la valeur d'une condition : l'opérateur NON. Il s'écrit en JavaScript sous la forme d'un point d'exclamation `!`.

```js
if (!(nombre > 100)) {
    console.log(`${nombre} est inférieur ou égal à 100`);
}
```

Voici la table de vérité de cet opérateur.

```js
console.log(!true);  // Affiche false
console.log(!false); // Affiche true
```

## Exprimer un choix

Essayons d'écrire un programme qui conseille l'utilisateur sur la tenue à porter en fonction de la météo actuelle. Une première solution consiste à utiliser des instructions `if/else`.

```js
const meteo = prompt("Quel temps fait-il dehors ?");
if (meteo === "soleil") {
    console.log("Sortez en t-shirt");
} else if (meteo === "vent") {
    console.log("Sortez en pull");
} else if (meteo === "pluie") {
    console.log("Sortez en blouson");
} else if (meteo === "neige") {
    console.log("Restez au chaud à la maison");
} else {
    console.log("Je n'ai pas compris !");
}
```

Lorsqu'un programme consiste à déclencher un bloc d'opérations parmi plusieurs selon la valeur d'une expression, on peut l'écrire en utilisant l'instruction JavaScript `switch`.

```js
const meteo = prompt("Quel temps fait-il dehors ?");
switch (meteo) {
case "soleil":
    console.log("Sortez en t-shirt");
    break;
case "vent":
    console.log("Sortez en pull");
    break;
case "pluie":
    console.log("Sortez en blouson");
    break;
case "neige":
    console.log("Restez au chaud à la maison");
    break;
default:
    console.log("Je n'ai pas compris !");
}
```

Le comportement de ce programme est strictement identique à celui de la version précédente.

L'instruction `switch` déclenche l'exécution d'un bloc d'instructions parmi plusieurs possibles. Seul le bloc correspondant à la valeur de l'expression testée sera pris en compte. Sa syntaxe est la suivante.

```js
switch (expression) {
case valeur1:
    // instructions exécutées quand expression vaut valeur1
    break;
case valeur2:
    // instructions exécutées quand expression vaut valeur2
    break;
...
default:
    // instructions exécutées quand aucune des valeurs ne correspond
}
```

Il n'y a pas de limite au nombre de cas possibles. Le mot-clé `default`, à placer en fin de `switch`, est optionnel. Il sert souvent à gérer les cas d'erreurs, comme dans l'exemple ci-dessus.

E> Les instructions `break;` dans les blocs `case` sont indispensables pour sortir du `switch` et éviter de passer d'un bloc à un autre.
E>
E>     const x = "abc";
E>     switch (x) {
E>     case "abc":
E>         console.log("x vaut abc");
E>         // pas de break : on passe au bloc suivant !
E>     case "def":
E>         console.log("x vaut def");
E>         break;
E>     }

L'exécution de cet exemple affiche deux messages : `"x vaut abc"` (résultat attendu) mais aussi `"x vaut def"`.
