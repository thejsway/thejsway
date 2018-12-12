# Work with strings

A lot of code you write will involve modifying chains of text characters - or [strings]( https://en.wikipedia.org/wiki/String_(computer_science) ). Let's look at how!

## TL;DR

* Although string values are primitive JavaScript types, some **properties** and **methods** may be applied to them just as if they were objects.

* The `length` property returns the number of characters of the string.

* JavaScript strings are **[immutable]( https://en.wikipedia.org/wiki/Immutable_object )**: once created, a string value never changes. String methods never affect the initial value and always return a new string.

* The `toLowerCase()` and `toUpperCase()` methods respectively return new converted strings to lower and upper case.

* String values may be compared using the `===` operator, which is case sensitive.

* A string may be seen as an **array of characters** identified by their **index**. The index of the first character is 0 (not 1).

* You may iterate over a string using either a `for` or the newer `for-of` loop.

* The `Array.from()` method can be used to turn a string into an array that can be traversed letter by letter with the `forEach()` method.

* Searching for values inside a string is possible with the `indexOf()`, `startsWith()` and `endsWith()` methods.

* The `split()` method breaks a string into subparts delimited by a separator.

## String recap

Let's recapitulate what we already know about strings:

* A string value represents text.

* In JavaScript, a string is defined by placing text within single quotes (`'I am a string'`) or double quotes (`"I am a string"`).

* You may use special characters within a string by prefacing them with  `\` ("backslash") followed by another character. For example, use `\n`  to add a line break.

* The `+` operator concatenates (combines or adds) two or more strings.

Beyond these basic uses, strings have even more versatility.

## Obtaining string length

To obtain the **length** of a string (the number of characters it contains), add `.length` to it. The length will be returned as an integer.

```js
console.log("ABC".length); // 3
const str = "I am a string";
const len = str.length;
console.log(len); // 13
```

Although string values are primitive JavaScript types, some properties and methods can be applied to them just as if they were objects by using the **dot notation**. `length` is one of those properties.

## Converting string case

You may convert a string's text to **lowercase** by calling the `toLowerCase()` method. Alternatively, you may do the same with  `toUpperCase()` to convert a string to uppercase.

```js
const originalWord = "Bora-Bora";

const lowercaseWord = originalWord.toLowerCase();
console.log(lowercaseWord); // "bora-bora"

const uppercaseWord = originalWord.toUpperCase();
console.log(uppercaseWord); // "BORA-BORA"
```

`toLowerCase()` and `toUpperCase()` are two string methods. Like every string method, both have no affect on the initial value and return a new string.

T> It's important to understand that once created, a string value never changes: strings are **immutable** in JavaScript.

## Comparing two strings

You may compare two strings with the `===` operator. The operation returns a boolean value: `true` if the strings are equal, `false` if not.

```js
const word = "koala";
console.log(word === "koala");    // true
console.log(word === "kangaroo"); // false
```

W> String comparison is case sensitive. Do indeed pay attention to your lower and uppercase letters!

```js
console.log("Qwerty" === "qwerty");               // false
console.log("Qwerty".toLowerCase() === "qwerty"); // true
```

## Strings as sets of characters

### Identifying a particular character

You may think of a string as an array of characters. Each character is identified by a number called an index, just as it does for an array. The same golden rules apply:

* The index of the first character in a string is 0, not 1.
* The highest index number is the string's length minus 1.

### Accessing a particular character

You know how to identify a character by its index. To access it, you use the **brackets notation** `[]` with the character index placed between the brackets.

W> Trying to access a string character beyond the string length produces an `undefined` result.

```js
const sport = "basketball";
console.log(sport[0]);  // first "b"
console.log(sport[6]);  // second "b"
console.log(sport[10]); // undefined: last character is at index 9
```

### Iterating over a string

Now what if you want to access all string characters one-by-one? You could access each letter individually, as seen above:

```js
const name = "Sarah"; // 5 characters
console.log(name[0]); // "S"
console.log(name[1]); // "a"
console.log(name[2]); // "r"
console.log(name[3]); // "a"
console.log(name[4]); // "h"
```

This is impractical if your string contains more than a few characters. You need a better solution to *repeat* access to characters. Does the word "repeat" bring to mind a former concept? Loops, of course!

You may write a **loop** to access each character of a string. Generally speaking, a `for` loop is a better choice than a `while` loop, since we know the loop needs to run once for each character in the string.

```js
for (let i = 0; i < myString.length; i++) {
    // Use myString[i] to access each character one by one
}
```

The loop counter `i` ranges from 0 (the index of the string's first character) to string length - 1 (index of the last character). When the counter value equals the string length, the expression becomes false and the loop ends.

So, the previous example may also be written with a `for` loop for an identical result.

```js
const name = "Sarah";
for (let i = 0; i < name.length; i++) {
  console.log(name[i]);
}
```

As for arrays covered earlier, a recent JavaScript evolution has introduced yet another option to iterate over a string: the `for-of` loop. The previous example may also be written:

```js
const name = "Sarah";
for (const letter of name) {
  console.log(letter);
}
```

If the index is not needed inside the loop, this syntax is arguably simpler than a standard `for` loop.

## Turning a string into an array

The JavaScript method `Array.from()` can be used to turn a string into an array. This array can further be traversed with the `forEach()` method. Just like the previous ones, this example shows the string letters one-by-one.

```js
const name = "Sarah";
const nameArray = Array.from(name);
nameArray.forEach(letter => {
  console.log(letter);
});
```

## Searching inside a string

Looking for particular values inside a string is a common task.

The `indexOf()` method takes as a parameter the searched-for value. If that value is found inside the string, it returns the index of the first occurrence of the value. Otherwise, it returns -1.

```js
const song = "Honky Tonk Women";
console.log(song.indexOf("onk")); // 1
console.log(song.indexOf("Onk")); // -1 because of case mismatch
```

When searching for a value at the beginning or end of a string, you may also use the `startsWith()` and `endsWith()` methods. Both return either `true` or `false`, depending on whether the value is found or not. Beware: these methods are case-sensitive.

```js
const song = "Honky Tonk Women";

console.log(song.startsWith("Honk")); // true
console.log(song.startsWith("honk")); // false
console.log(song.startsWith("Tonk")); // false

console.log(song.endsWith("men")); // true
console.log(song.endsWith("Men")); // false
console.log(song.endsWith("Tonk")); // false
```

## Breaking a string into parts

Sometimes a string is made of several parts separated by a particular value. In that case, it's easy to obtain the individual parts by using the `split()` method. This method takes as a parameter the separator and returns an array containing the parts.

```js
const monthList = "Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec";
const months = monthList.split(",");
console.log(months[0]);  // "Jan"
console.log(months[11]); // "Dec"
```

## Coding time!

### Word info

Write a program that asks you for a word then shows its length, lowercase, and uppercase values.

### Vowel count

Improve the previous program so that it also shows the number of vowels inside the word.

### Backwards word

Improve the previous program so that it shows the word written backwards.

### Palindrome

Improve the previous program to check if the word is a palindrome. A palindrome is a word or sentence that's spelled the same way both forward and backward, ignoring punctuation, case, and spacing.

> `"radar"` should be detected as a palindrome, `"Radar"` too.
