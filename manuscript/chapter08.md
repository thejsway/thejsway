# Work with strings

A lot of code you'll write involves modifying strings, or chains of characters. Let's look at how!

## TL;DR

* Although string values are primitive JavaScript types, some **properties** and **methods** can be applied to them just like they were objects.

* The `length` property returns the number of characters of the string.

* JavaScript string are **immutable**: once created, a string value will never change. All string methods don't affect the initial value and return a new string.

* The `toLowerCase()` and `toUpperCase()` methods respectively convert the string into lower and upper case.

* String values can be compared using the `===` operator, which is case sensitive.

* A string can be seen as a **set of characters** identified by their **index**. First character index is 0 (not 1).

* You can iterate over a string using either a `for` or the newer `for-of` loop.

* Searching for values inside a string is possible with the `indexOf()`, `startsWith()` and `endsWith()` methods.

* The `split()` method breaks a string into subparts delimited by a separator.

## String recap

Let's recap what we already know about strings:

* A string value represents text.

* In JavaScript, a string is defined by placing text within single quotes (`'I am a string'`) or double quotes (`"I am a string"`).

* You can use special characters within a string by prefacing them with  `\` ("backslash") followed by another character. For example, use `\n`  to add a linebreak.

* The `+` operator concatenates (combines) two strings together.

Strings are much more versatile beyond these basic uses.

## Obtaining string length

To find the **length** of a string (the number of characters in it), add `.length` to it. The length will be returned as an integer.

```js
console.log("ABC".length); // 3
const m = "I am a string";
const l = m.length;
console.log(l); // 13
```

Although string values are primitive JavaScript types, some properties and methods can be applied to them just like they were objects by using the **dot notation**. `length` is one of such properties.

## Converting string case

You can convert a string's text to **lowercase** by calling the `toLowerCase()` method on it. Alternatively, you can do the same thing with  `toUpperCase()` to convert it to uppercase.

```js
const originalWord = "Bora-Bora";

const lowercaseWord = originalWord.toLowerCase();
console.log(lowercaseWord); // "bora-bora"

const uppercaseWord = originalWord.toUpperCase();
console.log(uppercaseWord); // "BORA-BORA"
```

`toLowerCase()` and `toUpperCase()` are two string methods. Like every string method, both don't affect the initial value and will return a new string.

It's very important to understand that once created, a string value will never change: strings are **immutable** in JavaScript.

## Comparing two strings

You can compare two strings with the `===` operator. This returns a boolean value: `true` if the strings are equal, `false` if not.

```js
const word = "koala";
console.log(word === "koala");    // true
console.log(word === "kangaroo"); // false
```

Beware: string comparison is case sensitive! You'll have to pay attention to your lower and uppercase letters.

```js
console.log("Qwerty" === "qwerty");               // false
console.log("Qwerty".toLowerCase() === "qwerty"); // true
```

## Strings at sets of characters

### Identifying a particular character

You can think of a string as a set of characters. Each character is identified by a number called an index, just like for an array. The same golden rules apply:

* The index of the first character in a string is 0, not 1.
* The highest index number is the string's length minus 1.

### Accessing a particular character

You know how to identify a character by its index. To access it, you use the **brackets notation** `[]` with the character index placed between the brackets.

W> Trying to access a string character past the string length produces an `undefined` result.

```js
const sport = "basketball";
console.log(sport[0]);  // first "b"
console.log(sport[6]);  // second "b"
console.log(sport[10]); // undefined: last character is at index 9
```

### Iterating over a string

Now what if you want to access all string characters one-by-one? You could individually access each letter, as seen above:

```js
const name = "Sarah"; // 5 characters
console.log(name[0]); // "S"
console.log(name[1]); // "a"
console.log(name[2]); // "r"
console.log(name[3]); // "a"
console.log(name[4]); // "h"
```

This is impractical if your string contains more than a few characters. We have to find a better solution to *repeat* access to characters. Does the word "repeat" bring to mind a former concept? Loops, of course!

You can write a **loop** to access each character of a string. Generally speaking, a `for` loop is a better choice than a `while` loop for that task, since we know here that the loop will need to run for each character in the string.

```js
for (let i = 0; i < myString.length; i++) {
    // Use myString[i] to access each character one by one
}
```

The loop counter `i` ranges from 0 (the index of the string's first character) to string length - 1 (index of the last character). When the counter value equals the string length, the expression  becomes false, and the loop ends.

So, the previous example can also be written with a `for` for an identical result.

```js
const name = "Sarah";
for (let i = 0; i < name.length; i++) {
    console.log(name[i]);
}
```

Recent language evolutions have introduced yet another option to iterate over a string: the `for-of` loop. The previous example can also be written that way.

```js
const name = "Sarah";
for (const letter of name) {
    console.log(letter);
}
```

If the character index is not needed inside the loop, this syntax is arguably the simplest one.

## Searching inside a string

Looking for particular values inside a string is a very common task.

The `indexOf()` takes as a parameter the searched value. If that value is found inside the string, it returns the index of the first occurrence of the value. Otherwise, it returns -1.

```js
const song = "Honky Tonk Women";
console.log(song.indexOf("onk")); // 1
console.log(song.indexOf("Onk")); // -1 because of case sensitivity
```

When only searching for a value at the beginning or end of a string, you can alos use the `startsWith()` and `endsWith()` methods. Both return either `true` or `false`, depending if the value is found or not.

```js
const song = "Honky Tonk Women";

console.log(song.startsWith("Honk")); // true
console.log(song.startsWith("Tonk")); // false because of case sensitivity

console.log(song.endsWith("men")); // true
console.log(song.endsWith("Men")); // false because of case sensitivity
```

## Breaking a string into subparts

Sometimes a string is made of several subparts separated by a particular value. In that case, it's easy to obtain these subparts by using the `split()` method. It takes as a parameter the separator and returns an array containing the parts.

```js
const monthList = "Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec";
const months = monthList.split(",");
console.log(months[0]);  // "Jan"
console.log(months[11]); // "Dec"
```

## Coding time!

### Word info

Write a program that asks the user for a word then shows its length, lowercase and uppercase values.

### Vowel count

Improve the previous program so that it also shows the number of vowels inside the word.

### Backwards word

Improve the previous program so that it shows the word written backwards.

### Palindrome

Improve the previous program to check if the word is a palindrome. A palindrome is a word or sentence that's spelled the same way both forward and backward, ignoring punctuation, case, and spacing. Punctuation and spacing may not be taken into account here.

> `"radar"` should be detected as a palindrome, `"Radar"` too.
