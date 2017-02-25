# Understand object-oriented programming

A few chapters ago, you learned how to create your first objects in JavaScript. Now it's time to better understand how to work with them.

## TL;DR

TODO

## Context: a multiplayer RPG

As a reminder, here's the code for our minimalist RPG taken from a previous chapter. it creates an object literal named `aurora` with threee properties (`name`, `health` and `strength`) and a `describe()` method.

```js
const aurora = {
  name: "Aurora",
  health: 150,
  strength: 25,
  xp: 0,

  // Return the character description
  describe() {
    return `${this.name} has ${this.health} health points, ${this.strength} as strength and ${this.xp} XP points`;
  }
};

// Aurora is harmed by an arrow
aurora.health = aurora.health - 20;

// Aurora equips a strength necklace
aurora.strength = aurora.strength + 10;

// Aurora learn a new skill
aurora.xp = aurora.xp + 15;

console.log(aurora.describe());
```

To make the game more interesting, we'd like to have more characters in it. So here comes Glacius, Aurora's fellow.

```js
const glacius = {
  name: "Glacius",
  health: 139,
  strength: 30,
  xp: 0,

  // Return the character description
  describe() {
    return `${this.name} has ${this.health} health points, ${this.strength} as strength and ${this.xp} XP points`;
  }
};
```

Our two characters are strikingly similar. They share the same properties, with the only difference being some property values.

You should already be aware that code duplication is evil. We must find a way to share what's common to our characters.

## Objects and prototypes in JavaScript

To share properties between objects in JavaScript, we use **prototypes**.

In addition to its special properties, any JavaScript object has an internal property called `prototype`. This is a link (known as a **reference**) to another object. When trying to access a property that does not exist in an object, JavaScript tries to find this property in the prototype of this object.

Here's an example.

```js
const anObject = {
    myProp: 2
};

// Create anotherObject using anObject as a prototype
const anotherObject = Object.create(anObject);

console.log(anotherObject.myProp); // 2
```

In this example, the JavaScript statement `Object.create()` is used to create the object `anotherObject` with object `anObject` as its prototype.

```js
const obj = Object.create(objPrototype);
```

When the statement `anotherObject.myProp` is run, the `myProp` property of `anObject` is used since `myProp` doesn't exist in `anotherObject`.

If the prototype of an object does not have a desired property, then research continues in its own prototype until we get to the end of the **prototype chain**. If the end of this chain is reached without having found the property, access to it returns the value `undefined`.

```js
const anObject = {
    myProp: 2
};

// Create anotherObject using anObject as a prototype
const anotherObject = Object.create(anObject);

// Create yetAnotherObject using anotherObject as a prototype
const yetAnotherObject = Object.create(anotherObject);

// myProp is found in yetAnotherObject's prototype chain (in anObject)
console.log(yetAnotherObject.myProp); // 2

// myOtherProp can't be found in yetAnotherObject's prototype chain
console.log(yetAnotherObject.myOtherProp); // undefined
```

This type of relationship between JavaScript objects is called **delegation**: an object delegates part of its operation to its prototype.

## A prototype for our characters

### Character creation

Now back to our RPG. Check out its updated code and the execution result.

```js
// Character prototype
const Character = {
  // Return the character description
  describe() {
    return `${this.name} has ${this.health} health points, ${this.strength} as strength and ${this.xp} XP points`;
  }
};

const aurora = Object.create(Character);
aurora.name = "Aurora";
aurora.health = 150;
aurora.strength = 25;
aurora.xp = 0;

const glacius = Object.create(Character);
glacius.name = "Glacius";
glacius.health = 150;
glacius.strength = 30;
glacius.xp = 0;

console.log(aurora.describe());
console.log(glacius.describe());
```

![Execution result](images/chapter09-01.png)

In this example, we start by creating a `Character` object sharing the common properties between all characters. Aurora and Glacious are created with `Character` as their prototype and **delegate** their common behavior to it.

I> Naming prototype objects with a first letter in uppercase is a popular convention.

### Character setup

In the previous example, the character setup process became quite tedious and error-prone: first an object is created through `Object.create()`, and then each property is manually added to it.

There is a better way. Check it out.

```js
// Character prototype
const Character = {
  // Initialize the character
  init(name, health, strength) {
    this.name = name;
    this.health = health;
    this.strength = strength;
    this.xp = 0; // XP is always zero for new characters
  },
  // Return the character description
  describe() {
    return `${this.name} has ${this.health} health points, ${this.strength} as strength and ${this.xp} XP points`;
  }
};

// Factory function to create and setup a new character
function createCharacter(name, health, strength) {
  const character = Object.create(Character);
  character.init(name, health, strength);
  return character;
}

const aurora = createCharacter("Aurora", 150, 25);
const glacius = createCharacter("Glacius", 130, 30);

console.log(aurora.describe());
console.log(glacius.describe());
```

The new `init()` method of the `Character` object takes the initial values of a character's attributes and defines them as object properties. The `xp` property is always set to 0, since a newly created character has no experience.

We also added the `createCharacter()` function in order to make character creation and setup process a one-liner. This is a example of a **factory function**: a function whose role is to create, initialize and return something (here, an object).

## Let the fighting begin

Even with these improvements, our RPG is still pretty boring. What does it lack? Monsters and fights, of course!

Here's how a fight will be handled: an attacked character will lose a health points value equal to its attacker's strength. If its health value fall below zero, the character is considered dead and cannot attack anymore. Its slayer receives a fixed number of 10 experience points.

First, let's add the possibility for our characters to fight one another. Since it's a shared ability, we define it as a `Character` method named 'attack()`.

```js
// Character prototype
const Character = {
  // Initialize the character
  init(name, health, strength) {
    this.name = name;
    this.health = health;
    this.strength = strength;this.xp = 0; // XP is always zero for new characters
  },
  // Attack a target
  attack(target) {
    if (this.health > 0) {
      const damage = this.strength;
      console.log(`${this.name} attacks ${target.name} and causes ${damage} damage points`);
      target.health -= damage;
      if (target.health > 0) {
        console.log(`${target.name} has ${target.health} health points left`);
      } else {
        target.health = 0;
        const bonusXP = 10;
        console.log(`${this.name} eliminated ${target.name} and wins ${bonusXP} experience points`);
        this.xp += bonusXP;
      }
    } else {
      console.log(`${this.name} can't attack (they've been eliminated)`);
    }
  },
  // Return the character description
  describe() {
    return `${this.name} has ${this.health} health points, ${this.strength} as strength and ${this.xp} XP points`;
  }
};
```

Now we can introduce a monster in the game and make it fight our players. Here's the final code of our RPG.

```js
// Character prototype
const Character = {
  // Initialize the character
  init(name, health, strength) {
    this.name = name;
    this.health = health;
    this.strength = strength;this.xp = 0; // XP is always zero for new characters
  },
  // Attack a target
  attack(target) {
    if (this.health > 0) {
      const damage = this.strength;
      console.log(`${this.name} attacks ${target.name} and causes ${damage} damage points`);
      target.health -= damage;
      if (target.health > 0) {
        console.log(`${target.name} has ${target.health} health points left`);
      } else {
        target.health = 0;
        const bonusXP = 10;
        console.log(`${this.name} eliminated ${target.name} and wins ${bonusXP} experience points`);
        this.xp += bonusXP;
      }
    } else {
      console.log(`${this.name} can't attack (they've been eliminated)`);
    }
  },
  // Return the character description
  describe() {
    return `${this.name} has ${this.health} health points, ${this.strength} as strength and ${this.xp} XP points`;
  }
};

// Factory function to create and setup a new character
function createCharacter(name, health, strength) {
  const character = Object.create(Character);
  character.init(name, health, strength);
  return character;
}

const aurora = createCharacter("Aurora", 150, 25);
const glacius = createCharacter("Glacius", 130, 30);

console.log("Welcome to the adventure! Here are our heroes:");
console.log(aurora.describe());
console.log(glacius.describe());

const monster = createCharacter("Spike", 40, 20);
console.log("A wild monster has appeared: it's named " + monster.name);

monster.attack(aurora);
monster.attack(glacius);
aurora.attack(monster);
glacius.attack(monster);

console.log(aurora.describe());
console.log(glacius.describe());
```

![Execution result](images/chapter09-02.png)

This example shows how objects can be combined to create programs in JavaScript.

## JavaScript classes... Or lack thereof

If you come from another programming background, chances are you already heard about things like classes and inheritance. Most object-oriented languages (C++, Java, C#, ...) use **classes** as blueprints for creating objects. **Inheritance** is the fact for a class to inherit properties and behavior from another one, creating a **"is a"** kind of relationship between the two classes.

## Coding time!
