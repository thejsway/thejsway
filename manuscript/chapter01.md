# 3, 2, 1... Code!

## TL;DR

* The JavaScript instruction `console.log()` displays an message.
* A **value** is a piece of information. The **type** of a value defines its role and the operations applicable to it.

* Le langage JavaScript dispose du type **nombre** (*number*) pour représenter une valeur numérique entière ou réelle, et du type **chaîne de caractères** (*string*) pour représenter un texte.
* Une valeur de type texte est délimitée par une paire de guillemets simples (`'...'`) ou doubles (`"..."`).
* Les opérateurs `+`, `-`, `*` et `/` permettent de réaliser des opérations arithmétiques entre deux nombres. Appliqué à deux chaînes, l'opérateur `+` les fusionne en une seule. Cette opération est appelée **concaténation**. 
* Un programme informatique se compose de plusieurs **lignes de code** qui s'exécutent successivement.
* Les **commentaires** (`// ...` ou `/* ... */`) sont des portions de code non exécutées. Ils permettent de documenter le fonctionnement d'un programme.

## Un premier programme

C'est le moment de faire vos premiers pas avec JavaScript ! Voici votre tout premier programme.

    console.log('Bonjour en JavaScript !');

Ce programme affiche dans la console le texte "Bonjour en JavaScript !". Pour cela, il utilise l'ordre JavaScript `console.log()`, dont le rôle est d'afficher une information. Le texte à afficher est placé entre parenthèses et suivi d'un point-virgule. 

Afficher un texte à l'écran (le fameux [Hello World](https://fr.wikipedia.org/wiki/Hello_world)) est souvent la première chose que l'on apprend à faire lorsqu'on découvre un nouveau langage. Vous venez de franchir cette première étape !

## Valeurs et types

Une **valeur** est un morceau d'information utilisé dans un programme informatique. Les valeurs existent sous différentes formes, appelées des types. Le **type** d'une valeur détermine son rôle et les opérations qui lui sont applicables. 

Chaque langage informatique dispose d'une panoplie de types qui lui est propre. Nous allons étudier deux des principaux types disponibles en JavaScript.

### Le type nombre

Une valeur de type **nombre** (*number*) représente une valeur numérique, autrement dit une quantité. Comme en mathématiques, on distingue les valeurs entières (ou entiers) 0, 1, 2, 3... et les valeurs réelles (ou réels) auxquelles on ajoute des chiffres après la virgule pour plus de précision.

W> La virgule s'exprime en informatique sous la forme d'un point : `3.14` et non `3,14` !

Les nombres servent essentiellement à compter. Nous pouvons appliquer à des valeurs de type nombre les mêmes opérations qu'en mathématiques. Ces opérations produisent un résultat lui aussi de type nombre. Les principales opérations applicables sont rassemblées dans le tableau suivant.

|Opérateur|Rôle|
|`+`|Addition|
|`-`|Soustraction|
|`*`|Multiplication|
|`/`|Division|

### Le type chaîne

Une valeur de type **chaîne de caractères** (en abrégé chaîne, ou *string*) représente un texte. Ces valeurs sont délimitées par une paire de guillemets simples : `'Ceci est une chaîne'`.

I> Il est également possible de délimiter une chaîne de caractères avec une paire de guillemets doubles : `"Ceci est aussi une chaîne"`. Par convention, nous emploierons les guillemets simples dans ce cours. L'important est d'être cohérent : utilisez l'une ou l'autre notation, mais ne mélangez pas les deux.

E> Il ne faut surtout pas oublier de "fermer" une chaîne : simples ou doubles, les guillemets vont toujours par deux !

Pour inclure dans une chaîne certains caractères spéciaux, on utilise le caractère `\` (prononcé "antislash" ou "backslash" en anglais) qui donne un sens particulier au caractère suivant. Par exemple, `\n` permet d'ajouter un retour à la ligne dans une chaîne : `'Ceci est une chaîne\nSur plusieurs lignes'`.

On ne peut pas additionner ou supprimer des valeurs de type chaîne comme on peut le faire avec des nombres. En revanche, l'opérateur `+` peut être appliqué à deux valeurs de type chaîne. Son résultat est la jointure de ces deux chaînes, appelée **concaténation**. Par exemple, `'Bon'+'jour'` produit le résultat `"Bonjour"`.

## Structure d'un programme

Nous avons précédemment défini un programme informatique comme étant une liste d'ordres indiquant à un ordinateur ce qu'il doit faire. Ces ordres sont écrits sous forme de texte dans un ou plusieurs fichiers et forment ce qu'on appelle le code source du programme. Les lignes de texte dans un fichier de code source s'appellent des **lignes de code**. 

I> Le code source peut comporter des lignes vides : celles-ci seront ignorées lors de l'exécution du programme.

### Instructions

Chaque ordre inclus dans un programme est appelée une **instruction**. Une instruction est délimitée par un point virgule. Un programme est constitué d'une suite d'instructions. 

I> Le plus souvent, on n'écrit qu'une seule instruction par ligne, mais ce n'est pas une obligation.

### Déroulement de l'exécution

Lorsqu'un programme est exécuté, les instructions qui le composent sont "lues" les unes après les autres. Chaque instruction produit un résultat, et c'est la combinaison de ces résultats individuels qui produit le résultat final du programme.

Voici un exemple de programme JavaScript composé de plusieurs instructions.

    console.log('Bonjour en JavaScript !');
    console.log('Faisons quelques ' + 'calculs.');
    console.log(4 + 7);
    console.log(12 / 0);
    console.log('Au revoir !');

Le résultat de son exécution est le suivant.

![Résultat de l'exécution](images/chapter01-01.png)

I> On remarque au passage qu'une division par zéro (ici `12/0`) produit, comme attendu, un résultat infini (`Infinity`).

### Commentaires

Par défaut, chaque ligne de texte dans les fichiers source d'un programme est considérée comme une instruction à exécuter. Il est possible d'exclure certaines lignes de l'exécution en les préfixant par une double barre oblique `//`. Ce faisant, on transforme ces lignes en **commentaires**.

    console.log('Bonjour en JavaScript !');
    //console.log('Faisons quelques ' + 'calculs.');
    console.log(4 + 7);
    //console.log(12 / 0);
    console.log('Au revoir !');

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

## A vous de jouer !

Passons maintenant à quelques exercices pratiques pour vérifier que vous avez tout compris ! 

### Présentation

Ecrivez un programme qui affiche votre nom et votre âge. Voici le résultat de l'exécution de ma version de ce programme.

![Résultat de l'exécution](images/chapter01-02.png)

### Mini-calculatrice

Ecrivez un programme qui calcule et affiche le résultat de l'addition, de la soustraction, de la multiplication et de la division de 6 par 3.

### Valeurs affichées

Observez le programme ci-dessous puis tentez de prévoir les valeurs affichées lors de son exécution.

    console.log(4 + 5);
    console.log('4 + 5');
    console.log('4' + '5');

Vérifiez vos prévisions en exécutant ce programme.
