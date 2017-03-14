# What's a web page?

This short chapter summarizes what you need to known about the Web and web pages.

## TL;DR

* The [World Wide Web](https://en.wikipedia.org/wiki/World_Wide_Web) (or **Web**) is an information space built on top of the [Internet](https://en.wikipedia.org/wiki/Internet). Web resources are accessible via their [URL](https://en.wikipedia.org/wiki/Uniform_Resource_Locator), and can contain [hyperlinks](https://en.wikipedia.org/wiki/Hyperlink) to other resources.

* A **web page** is a document suitable for the Web. Creating web pages usually involves three technologies: [HTML](https://en.wikipedia.org/wiki/HTML) to structure the content, [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) to define its presentation and JavaScript to add interactivity.

* An HTML document is made of text and structural elements called **tags** that describe the page content: paragraphs, headings, hyperlinks, images, etc.

* CSS uses **selectors** to declare which HTML elements a style applies to. Elements can be selected by tag name (`h1`), by class (`.done`) or by identifier (`#rude`).

* An HTML document can include a CSS stylesheet with a `<link>` tag and a JavaScript file with a `<script>` tag.

```html
<!doctype html>
<html>

<head>
    <!-- Info about the page: title, character set, etc -->

    <!-- Link to a CSS stylesheet -->
    <link href="path/to/file.css" rel="stylesheet" type="text/css">
</head>

<body>
    <!-- Page content -->

    <!-- Link to a JavaScript file -->
    <script src="path/to/file.js"></script>
</body>

</html>
```

* A **browser** is the software you use to visit webpages and use web applications. The modern ones include a set of **developer tools** to ease the task of developing for the web.

## Internet and the Web

As you probably know, the [World Wide Web](https://en.wikipedia.org/wiki/World_Wide_Web) (or **Web** for short) is an ever-expanding information space built on top of the [Internet](https://en.wikipedia.org/wiki/Internet). Web resources are accessible via their address, called their [URL](https://en.wikipedia.org/wiki/Uniform_Resource_Locator), and can contain [hyperlinks](https://en.wikipedia.org/wiki/Hyperlink) to other resources. Together, all these interlinked resources form a huge mesh analogous to a spider web.

Documents suitable for the Web are called **web pages**. They are grouped together on **websites** and visited through a special kind of software called a [browser](https://en.wikipedia.org/wiki/Web_browser).

## The languages of the Web

There are three main technologies for creating web pages: HTML, CSS and JavaScript.

### HTML

HTML, short for [HyperText Markup Language](https://en.wikipedia.org/wiki/HTML), is the document format of web pages. An HTML document is made of text and structural elements called **tags**. Tags are used to describe the page content: paragraphs, headings, hyperlinks, images, etc.

Here is an example of a simple web page, usually stored as an `.html` file.

```html
<!doctype html>
<html>

<head>
    <meta charset="utf-8">
    <title>My web page</title>
</head>

<body>
    <h1>My web page</h1>
    <p>Hello! My name's Baptiste.</p>
    <p>I live in the great city of <a href="https://en.wikipedia.org/wiki/Bordeaux">Bordeaux</a>.</p>
</body>

</html>
```

![Display result](images/chapter13-01.png)

Here are a few references for learning more about HTML:

* [Khan Academy - Intro to HTML](https://www.khanacademy.org/computing/computer-programming/html-css#intro-to-html)
* [Mozilla Developer Network - HTML reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference)

### CSS

CSS, or [Cascading Style Sheets](https://en.wikipedia.org/wiki/Cascading_Style_Sheets), is a language used to alter the presentation of web pages.

CSS uses **selectors** to declare which HTML elements a style applies to. Many selecting strategies are possible, most notably:

* All elements of a given tag name.
* Elements matching a given **class** (selector syntax: `.myClass`).
* The element matching a given and unique **identifier** (selector syntax: `#MyId`).

Here is an example of a simple CSS style sheet, usually stored as a `.css` file.

```css
/* All h1 elements are pink */
h1 {
   color: pink;
}

/* All elements with the class "done" are strike through */
.done {
  text-decoration: line-through;
}

/* The element having id "rude" is shown uppercase with a particular font */
#rude {
  font-family: monospace;
  text-transform: uppercase;
}
```

A style sheet is associated with an HTML document using a `link` tag in the `head` part of the page.

```html
<!-- Link to a CSS stylesheet -->
<link href="path/to/file.css" rel="stylesheet" type="text/css">
```

To learn more about CSS, visit the following links:

* [Khan Academy - Intro to CSS](https://www.khanacademy.org/computing/computer-programming/html-css#intro-to-css)
* [Mozilla Developer Network - CSS reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference)

### JavaScript

JavaScript can interact with an HTML document to provide dynamic interactivity: responses to user actions on the page, dynamic styling, animations, etc. It is the only programming language understood by all web browsers.

A JavaScript file, usually stored in a `.js` file, is loaded by a web page with a `<script>` tag.

```html
<!-- Link to a JavaScript file -->
<script src="path/to/file.js"></script>
```

## Developing web pages

To create interactive web pages, you need to write HTML, CSS and JavaScript code. If you're just starting out, the easiest way to do so is by using an online JavaScript playground like [CodePen](http://codepen.io). However, you will likely want to develop in a more professional fashion at some point. You may also need to work offline, which is not supported by CodePen.

### Using a code editor

To do so, you'll need a **code editor**, a software that will assist you during coding. Here are some of them:

* [Visual Studio Code](https://code.visualstudio.com/) (my personal favorite).
* [Brackets](http://brackets.io/).
* [Atom](https://atom.io/).
* [Sublime Text](https://www.sublimetext.com/).

### Browser and developer tools

A **browser** is the software you use to visit webpages and use web applications. Modern browser include **developer tools** to help with web development. Each browser differs in exactly which tools they provide, but they're more similarities than differences among them.

These tools usually include a **JavaScript console** (to show JS output and type commands), a **page inspector** (to browse the page structure) and many more!

![The Firefox JavaScript console](images/chapter12-01.png)

Check out the following links to discover more about browser developer tools:

* [Khan Academy - Inspecting HTML and CSS](https://www.khanacademy.org/computing/computer-programming/html-css/web-development-tools/a/using-the-browser-developer-tools).
* [OpenClassrooms - Optimize your website with DevTools](https://openclassrooms.com/courses/optimize-your-website-with-devtools).
* [Chrome DevTools Overview](https://developer.chrome.com/devtools).
* [Firefox Developer Tools](https://developer.mozilla.org/son/docs/Tools).

> Even if you're using CodePen to follow along this book, you can still use the developer tools in addition to the CodePen console. For performance reasons, the CodePen console does not always show the same amount of information as the "real" browser console.

## Coding time!

You can skip this exercise if you ahve prior experience with HTML and CSS.

### Your first web page

Using CodePen or working offline, follow the beginning of the [Getting started with the Web](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web) tutorial from Mozilla Develper Network to create a simple web page using HTML and CSS. The required steps are:

1. [What will your website look like?](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/What_will_your_website_look_like)
1. [Dealing with files](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/Dealing_with_files)
1. [HTML basics](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics)
1. [CSS basics](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics)

![Expected result](images/chapter12-02.png)
