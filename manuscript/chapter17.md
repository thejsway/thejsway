# Manipulate forms

JavaScript lets you manage forms defined within your web page, in order to improve interactivity.

## TL;DR

Forms let users input data through a web page.
Inputted data can be sent to a web server.
Before data gets sent off, you can use JavaScript to interact with the form data.
Text zones (`input type="text">` or `<textarea>` each have a value property to access the inputted value.
Once a text field is selected, we can say that this field has "focus." focus and blur events are triggered when the field is selected or deselected, respectively.
Chexboxes, radio buttons, and dropdown menus generate change events once a user modifies their choice.
The DOM element that corresponds the form has an elements property that lets you access its input fields. 
Submitting a form triggers a submit event on a form. You can prevent the sending of data associated with this event handler by using the preventDefault method on the associated Event object.
Any modification of a text field triggers an input event, which can be used to validate its data in real time.

## JavaScript and forms

### Form recap

Forms enhance web pages and allow users to input information through text fields, check boxes, dropdown menus, and more. Forms are defined with a `<form>` HTML tag, and within this tag, you have your different `<input>` tags, `<select>` tags, or `<textarea>` tags.

If you'd like a recap on forms in general, check out this chapter from our course on HTML and CSS: https://openclassrooms.com/courses/build-your-website-with-html5-and-css3/forms
Data entered into a form by users is normally sent via a network to a web server that processes and sends a response to the browser. This response is normally a new web page! To do this, web servers use backend programming languages like PHP or Ruby.

### Handling forms with JavaScript

Thanks to JavaScript, you can manage forms (and their data) directly within the browser before sending them to an external server. You can notify users of incorrect input data, make suggestions on what they type, and more. Who said forms were boring?!

## Form fields

Example form

We're going to start with a simple form that allows users to sign up for a service. Put the following content in your chapter 6 HTML document, called course.html , or into a pen on CodePen.

<!doctype html>
<html>
    <head>
    <meta charset="utf-8">
        <title>Playing with forms</title>
    </head>
    
    <body>
        <form>
    <h1>Signup form</h1>
        <p>
            <label for="username">Username</label> :
            <input type="text" name="username" id="username" required>
            <span id="usernameHelp"></span>
        </p>
        <p>
            <label for="password">Password</label> :
            <input type="password" name="password" id="password" required>
            <span id="passwordHelp"></span>
        </p>
        <p>
            <label for="emailAddress">Email address</label> :
            <input type="email" name="emailAddress" id="emailAddress" required placeholder="user@gmail.com">
            <span id="emailHelp"></span>
        </p>
        <p>
            <input type="checkbox" name="confirmation" id="confirmation">
            <label for="confirmation">Send me a confirmation email</label>
        </p>
        <p>
            <input type="radio" name="subscription" id="newsroom" value="newspromo">
            <label for="newsroom">Subscribe me to newsletters and promotions</label>
            <br>
            <input type="radio" name="subscription" id="news" value="news">
            <label for="news">Subscribe me only to the newsletter</label>
            <br>
            <input type="radio" name="subscription" id="no" value="no" checked>
            <label for="no">No subscriptions please</label>
            <br>
        </p>
        <p>
            <label for="nationality">Nationality :</label>
            <select name="nationality" id="nationality">
                <option value="US" selected>American</option>
                <option value="FR">French</option>
                <option value="ES">Spanish</option>
                <option value="XX">Other</option>
            </select>
        </p>
        
        <input type="submit" value="Submit">
        <input type="reset" value="Cancel">
    </form>
    
    <script src="../js/course.js"></script>
        </body>

</html>
This example contains multiple input zones: text, checkboxes, radio buttons, a dropdown menu, as well as send and cancel buttons. We'll learn how to deal with each of these elements with JavaScript. 

You might have noticed that the <form> tag doesn't have the usual action and method attributes. These attributes allow you to define a particular resource and request type, but since our form only handles a client-side situation here, they're not necessary.

Type code examples as we go along into your course.js file or add them to your pen on CodePen.

### Text zones

#### Access input values

A text field allows a user to input text on single or multiple lines. You have two options for defining text fields: a single-line text field is defined in HTML as <input type="text"> , and a multi-line text input field will be defined via <textarea> instead. Choose the best one for the content the user will be inputting!

Here's the extract from the above code that lets users input a username:

<label for="username">Username</label> :
<input type="text" name="username" id="username" required>
<span id="usernameHelp"></span>
In JavaScript, you can access the value of a text field by using the value  property of the corresponding DOM element. In adding a new value to this property, you'll modify the value shown in the text field.

The following example adds the value "MyCoolUsername" to the the text field:

var usernameElement = document.getElementById("username");
usernameElement.value = "MyCoolUsername";

#### Focus areas

When a text zone is selected, it becomes the "focus" area of the form. You may have noticed field borders turning blue or other effects when you're accessing a particular input area. This helps you know where you are in the form. A user clicking on a text field (or tabbing down into it) kicks off a focus  event. Additionally, a focus event triggers a blur  event on the field that previously had the focus.

You can use these events to show the user tips related to the current text field, as in the following example:

// Show a tip associated with a selected text area
usernameElement.addEventListener("focus", function () {
document.getElementById("usernameHelp").textContent = "Enter a unique username!";
});
// Hide the advice when the user moves onto a different field
usernameElement.addEventListener("blur", function (e) {
document.getElementById("usernameHelp").textContent = "";
});
Test it! Click the username field to get a helpful hint. http://codepen.io/eclairereese/pen/aZmVay?editors=1011  ✏️
By selecting the username input field, you'll see a helpful message in the <span> tag, which was included in the HTML specifically to house the message (thus why it's initially empty).

From the JavaScript code, you can modify the target event by calling focus  (to add focus) and blur  (to remove it) on a DOM element. 

// Add focus on username input
usernameElement.focus();
Multi-line text fields (<textarea> ) work similarly to <input> tags.
We'll learn how to validate text that a user inputs (to make sure it fits certain criteria) later in this chapter!

### Choice elements

You often see form elements that allow users to make a choice among multiple possibilities. A change  event will be kicked off once a user changes their choice.

#### Checkboxes

You can add checkboxes to your HTML form by using the tag <input type="checkbox"> .

Here's the code from the example form that offers a user the choice to receive a confirmation email (or not).

<input type="checkbox" name="confirmation" id="confirmation">
<label for="confirmation">Send me a confirmation email</label>
If the value of this box changes, an Event object associated with the change has a boolean property that checks what the new state of the field is (checked or not checked).

The below code will show a message in the console if the box is checked or not.

// Show if the email confirmation checkbox is checked
document.getElementById("confirmation").addEventListener("change", function (e) {
console.log("Email confirmation request: " + e.target.checked);
});
Test it! Click the confirmation check box and look at the console. http://codepen.io/eclairereese/pen/aZmVay?editors=1011 ✏️
Radio buttons

Radio buttons allow users to make a choice (out of multiple possibilities). Create radio buttons with <input type="radio"> tags, which have the same name attribute and different value attributes.

Here's the extract from the example form that lets a user select between three radio buttons, each representing a subscription option.

<input type="radio" name="subscription" id="newsroom" value="newspromo">
<label for="newsroom">Subscribe me to newsletters and promotions</label>
<br>
<input type="radio" name="subscription" id="news" value="news">
<label for="news">Subscribe me only to the newsletter</label>
<br>
<input type="radio" name="subscription" id="no" value="no" checked>
<label for="no">No subscriptions please</label>
<br>
The following code adds a message to the console if the radio button selection changes.

// Show the subscription type selected via radio button
var subscriptionElements = document.getElementsByName("subscription");
for (var i = 0; i < subscriptionElements.length; i++) {
    subscriptionElements[i].addEventListener("change", function (e) {
    console.log("Selected subscription: " + e.target.value);
    });
}
Test it! Change the subscription type and look at the console. http://codepen.io/eclairereese/pen/aZmVay?editors=1011  ✏️
Once the value of a radio button input changes, the e.target.value of the change event contains the ﻿value  attribute of the newly selected <input>tag. 

#### Dropdown lists

Make a dropdown list by using the <select> tag (for the menu overall) in which you can add <option> tags for possible choices!

Here's the code extract from above that lets users choose a nationality:

<label for="nationality">Nationality :</label>
<select name="nationality" id="nationality">
    <option value="US" selected>American</option>
    <option value="FR">French</option>
    <option value="ES">Spanish</option>
    <option value="XX">Other</option>
</select>
The following code uses the change events triggered on the dropdown list to show the new choice made.

// Show the selected nationality
document.getElementById("nationality").addEventListener("change", function (e) {
console.log("Nationality code: " + e.target.value);
});
Test it! Change the nationality selected and look at the console. http://codepen.io/eclairereese/pen/aZmVay?editors=1011 ✏️
Like you saw with radio buttons, the e.target.value property of the change event contains the value attribute of the <option> tag associated with the new choice -- not the text shown in the dropdown list!

## Forms as DOM elements

### Access form fields

A <form> tag corresponds to a DOM element. This element has an elements property that pulls together all the form input fields. You can use this property to access a field via its name attribute or by its index (where it appears in the form).

The below example shows some information on the input fields of our example form.

var form = document.querySelector("form");
console.log("Number of fields:" + form.elements.length); // Will be 10
console.log(form.elements[0].name); // Will be "username"
console.log(form.elements.password.type); // Will be "password"

### Submitting a form

A form will be submitted when a user clicks on the submit button, which will have an <input type="submit" tag. An <input type="reset"> tag shows a button that resets the form data.

Here are the two buttons from the sample form: 

<input type="submit" value="Submit">
<input type="reset" value="Cancel">
As a general rule, submitting a form happens by sending the form data to a specified resource within the action attribute of the <form> tag. Prior to this, a submit event is triggered on the DOM element corresponding to the form. By adding a handler for this type of event, you can access form data before it gets sent. 

However, if you don't want a form to submit (or you want to disable any other default behavior), you can use the method ﻿preventDefault()﻿. 

## Form validation

Checking data inputted by users before it gets sent to a server is a major use of JavaScript with web forms. You can also immediately alert a user to problems with their input, which improves the user's experience, since they won't have to deal with constant retrying if they submit the wrong type of data.

Validation can happen in several ways:

as input is being entered;
after input is entered;
when the user submits the form.
This last technique only involves adding validation in the submit event handler for the form. We'll look at each technique one at a time, using the example form from the last chapter!

Instant validation

Validation while a user is inputting information is based on ﻿input  events, which are triggered on an input zone each time its value changes.

The following code example adds an input event handler on the password field. This handler checks the length (number of characters) of the password being typed and shows a message to the user with specific content and color.

// Validate password length
document.getElementById("password").addEventListener("input", function (e) {
    var password = e.target.value; // Value of the password field
    var passwordLength = "weak";
    var messageColor = "red"; // Weak password => red
    if (password.length >= 8) {
        passwordLength = "strong";
        messageColor = "green"; // Long password => green
    } else if (password.length >= 4) {
        passwordLength = "moderate";
        messageColor = "orange"; // Moderate password => orange
    }
    var passwordHelpElement = document.getElementById("passwordHelp");
    passwordHelpElement.textContent = "Strength: " + passwordLength; // helper text
    passwordHelpElement.style.color = messageColor; // helper text color
});
Test it! Try different passwords and see which ones give you a green "strong" message. http://codepen.io/eclairereese/pen/vKXWwQ?editors=1010 ✏️
Post-input validation

A text zone's input is considered finished once ﻿focus  is lost on the zone, which kicks off a ﻿blur  event that you can use to trigger validation.

Let's imagine that you want to validate the presence of an @ in the email address entered by a user. You'll need the JavaScript method indexOf to do this, which will let you find a value in a string of characters and send a value of -1 if the value isn't found.

Here's the JavaScript code which shows this validation. 

// Checking an email address once it's entered
document.getElementById("emailAddress").addEventListener("blur", function (e) {
    var emailAddressValidity = "";
    if (e.target.value.indexOf("@") === -1) {
        // the email address doesn't contain @
        emailAddressValidity = "invalid address";
    }
    document.getElementById("emailHelp").textContent = emailAddressValidity;
});

## Coding time!