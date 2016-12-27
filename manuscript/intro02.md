# Introduction à la programmation

## TL;DR

* Un **ordinateur** n'est qu'une machine qui se contente d'exécuter automatiquement, très vite et sans erreur, les opérations qu'on lui demande d'effectuer.
* Un **programme** est une liste d'ordres indiquant à un ordinateur ce qu'il doit faire. Il se présente sous la forme d'un ensemble de commandes textuelles appelées des **instructions**.
* Le rôle du **programmeur** est de créer ces programmes. Pour cela, il peut utiliser différents langages de programmation.
* Avant d'écrire un programme, il faut réfléchir et décomposer le problème à résoudre en opérations élémentaires afin d'aboutir à un **algorithme**.

## Un programme, c'est quoi ?

![L'Evolution (?)](images/intro02-01.jpg)

Depuis son invention dans les années 1950, l'informatique a révolutionné bien des domaines de notre vie quotidienne. Le calcul d'un itinéraire depuis un site Internet ou un GPS, la réservation à distance d'un billet de train ou d'avion ou encore la possibilité de voir et de parler avec des amis à l'autre bout du monde : tous ces actes courants sont possibles grâce aux **ordinateurs**.

I> Le terme "ordinateur" est à prendre dans son sens le plus général, celui d'une "machine électronique capable d'exécuter des opérations arithmétiques et logiques" ([Wikipedia](https://fr.wikipedia.org/wiki/Ordinateur)). Il peut désigner aussi bien un ordinateur de bureau ou portable (PC, Mac), un serveur de calcul ou encore un terminal mobile de type tablette ou smartphone. 

Cependant un ordinateur, même très performant, n'est qu'une **machine** capable d'exécuter automatiquement une série d'opérations simples qu'on lui a demandées. Il ne dispose par lui-même d'aucune capacité d'apprentissage, de jugement, d'improvisation, bref d'aucune "intelligence". Il se contente de faire ce qu'on lui dit de faire. L'intérêt des ordinateurs est de savoir manipuler très rapidement et sans erreur d'énormes quantités d'informations. 

Une intervention humaine est nécessaire pour qu'un ordinateur puisse accomplir des tâches utiles. C'est le rôle du **programmeur** (appelé également développeur). Il va fournir les ordres que la machine doit exécuter en écrivant des **programmes**.

Un programme informatique (également appelé application ou logiciel) est "**une liste d'ordres indiquant à un ordinateur ce qu'il doit faire**" ([Wikipedia](https://fr.wikipedia.org/wiki/Programme_informatique)). Il se présente concrètement sous la forme d'un ou (le plus souvent) plusieurs fichiers contenant des commandes textuelles : ce sont les ordres données à la machine, qu'on appelle également des **instructions**. L'ensemble des fichiers contenant les instructions du programme constitue son code source. Programmer, c'est donc écrire le code source d'un programme, d'où l'emploi du terme synonyme de **coder**.

Cependant, on ne peut pas écrire tout et n'importe quoi dans le code source d'un programme. Imaginons que vous souhaitiez dialoguer avec une personne anglophone. Vous ne vous ferez pas comprendre si vous utilisez des mots qui ne sont pas anglais, ou bien si vous les placez n'importe où dans vos phrases. C'est la même chose lorsqu'on écrit des programmes : pour être compris par un ordinateur, un programme doit respecter les règles du langage de programmation utilisé.

Un **langage de programmation** définit une manière de donner des ordres à un ordinateur. Un peu comme une langue vivante, tout langage a son vocabulaire (un ensemble de mots-clés, chacun jouant un rôle spécifique) et sa grammaire (un ensemble de règles définissant la manière d'écrire des programmes dans ce langage).

## Comment créer des programmes ?

### Au plus près de la machine : l'assembleur

Le seul langage de programmation directement compréhensible par un ordinateur est le langage machine, également appelé [assembleur](https://fr.wikipedia.org/wiki/Assembleur). Il s'agit d'instructions élémentaires liées à un type de processeur (le "cerveau" de l'ordinateur) et qui permettent de manipuler directement la mémoire de la machine.

Voici un exemple de programme écrit en assembleur, tiré de [Wikipedia](https://fr.wikipedia.org/wiki/Assembleur#Afficher_Bonjour). Son rôle est d'afficher le message "Bonjour" à l'utilisateur.

{lang="assembly"}
    str:
     .ascii "Bonjour\n"
     .global _start
 
    _start:
    movl $4, %eax
    movl $1, %ebx
    movl $str, %ecx
    movl $8, %edx
    int $0x80
    movl $1, %eax
    movl $0, %ebx
    int $0x80

Plutôt intimidant, non ? Rassurez-vous, il est heureusement possible de coder de manière bien plus simple et conviviale en utilisant d'autres langages que l'assembleur. 

### La grande famille des langages de programmation

Il existe un grand nombre de langages de programmation, adaptés à des usages variés. Chaque langage de programmation dispose de sa propre syntaxe et d'instructions spécifiques. On peut faire une analogie avec les langues étrangères : avant de pouvoir parler telle ou telle langue, il faut l'étudier afin de connaître ses spécificités.

Cela dit, on peut dégager des similitudes entre les langages de programmation les plus courants. Par exemple, voici le programme précédent écrit en utilisant le langage Python.

{lang="python"}
    print("Bonjour")

On peut écrire le même programme en utilisant le langage PHP.

{lang="php"}
    <?php
    echo("Bonjour\n");
    ?>

Même exemple avec le langage C#.

{lang="csharp"}
    class Program {
        static void Main(string[] args) {
            Console.WriteLine("Bonjour");
        }
    }

Et voici le même programme, écrit cette fois en langage Java.

{lang="java"}
    public class Program {
        public static void main(String[] args) {
            System.out.println("Bonjour");
        }
    }

Tous ces programmes affichent le message "Bonjour", mais chacun d'eux le fait à sa manière.

### L'exécution d'un programme

On nomme **exécution** le fait de demander à un ordinateur de réaliser les ordres contenus dans un programme. Quel que soit le langage avec lequel il est écrit, un programme doit être traduit en assembleur pour pouvoir être exécuté. Ce processus de traduction dépend du langage choisi.

Avec certains langages, les lignes du code source sont traduites en assembleur puis exécutées ligne après ligne par un programme spécifique appelé interpréteur. On dit alors que le langage est **interprété**. Python et PHP sont des exemples de langages interprétés.

Une autre possibilité consiste à créer à partir de l'ensemble du code source un fichier directement exécutable (sous Windows, il portera l'extension `.exe`) en utilisant un programme intermédiaire appelé compilateur. On parle alors de langage **compilé**. Les langages C sont C++ sont des exemples de langages compilés.

Enfin, une troisième option consiste à utiliser un pseudo-compilateur pour générer à partir du code source un ensemble de fichiers pouvant être exécutés sur n'importe quelle plate-forme supportant
l'environnement. C'est le cas du langage Java et des langages de la plate-forme Microsoft .NET (VB.NET, C#, etc).

## Apprendre à programmer

### Introduction aux algorithmes

Sauf dans des cas très simples, on ne crée pas un programme en se lançant directement dans l'écriture du code source. Il est d'abord nécessaire d'analyser le problème pour trouver la suite d'opérations à réaliser pour le résoudre. 

Prenons un exemple concret tiré de la vie courante (l'idée originale est d'Alain Tarlowski) : je souhaite me préparer un plat de pâtes. Quelles sont les étapes qui vont me permettre d'atteindre mon objectif ?

On peut imaginer la solution ci-dessous.

{lang="text"}
    Début
        Sortir une casserole
        Mettre de l'eau dans la casserole
        Ajouter du sel
        Mettre la casserole sur le feu
        Tant que l'eau ne bout pas
        Attendre
        Sortir les pâtes du placard
        Verser les pâtes dans la casserole
        Tant que les pâtes ne sont pas cuites
            Attendre
        Verser les pâtes dans une passoire
        Egoutter les pâtes
        Verser les pâtes dans un plat
        Goûter
        Tant que les pâtes sont trop fades
            Ajouter du sel
            Goûter
        Si on préfère le beurre à l'huile
            Ajouter du beurre
        Sinon
            Ajouter de l'huile
    Fin

![C'est prêt !](images/pates.jpg)

On constate qu'on arrive à l'objectif visé en combinant un ensemble d'actions dans un ordre précis.
On peut distinguer différents types d'actions :

* des actions simples ("Sortir une casserole") ;
* des actions conditionnelles ("Si on préfère le beurre à l'huile...") ;
* des actions qui se répètent ("Tant que les pâtes sont trop fades...").

Nous avons employé une notation simple, compréhensible et indépendante de tout langage de programmation. En fait, nous venons d'écrire ce qu'on appelle un **algorithme**.

On peut définir un algorithme comme **une suite ordonnée d'opérations permettant de résoudre un problème donné**. Un algorithme décompose un problème complexe en une suite d'opérations simples.

### Le rôle du programmeur

Ecrire des programmes qui réalisent de manière fiable les tâches attendues est la première mission du programmeur. Un débutant arrivera vite à créer des programmes simples. La difficulté apparaît lorsque que le programme évolue et se complexifie. Il faut de l'expérience et beaucoup de pratique avant d'arriver à maîtriser cette complexité.

C'est aussi ce qui fait de la programmation un art subtil et stimulant. Une fois les bases acquises, vos seules limites seront celles de votre imagination !

> "Le programmeur est un créateur d'univers dont il est seul responsable. Des univers d'une complexité virtuellement infinie peuvent être créés sous la forme de programmes informatiques." (Joseph Weizenbaum)
