# Discover functional programming

Object-oriented programming, albeit quite popular, is not the only way to create programs. This chapter will introduce you to another important paradigm: functional programming.

## TL;DR

TODO

## JavaScript: a multi-paradigm language

TODO

## Context: a movie list

In this chapter, we'll start with an example program and improve it little by little, without adding any new functionality. This important programmer task is called **refactoring**.

Our initial program is about recent Batman movies. The data comes under the form of an array of objects. Each object describes a movie.

```js
const movieList = [{
  title: "Batman",
  year: 1989,
  director: "Tim Burton",
  imdbRating: 7.6
}, {
  title: "Batman Returns",
  year: 1992,
  director: "Tim Burton",
  imdbRating: 7.0
}, {
  title: "Batman Forever",
  year: 1995,
  director: "Joel Schumacher",
  imdbRating: 5.4
}, {
  title: "Batman & Robin",
  year: 1997,
  director: "Joel Schumacher",
  imdbRating: 3.7
}, {
  title: "Batman Begins",
  year: 2005,
  director: "Christopher Nolan",
  imdbRating: 8.3
}, {
  title: "The Dark Knight",
  year: 2008,
  director: "Christopher Nolan",
  imdbRating: 9.0
}, {
  title: "The Dark Knight Rises",
  year: 2012,
  director: "Christopher Nolan",
  imdbRating: 8.5
}];
```

And here is the rest of the program, that uses the data to show some results about the movies. Check it out, it should be pretty self-explanatory.

```js
// Get movie titles
const titles = [];
for (movie of movieList) {
  titles.push(movie.title);
}
console.log(titles);

// Count movies by Christopher Nolan
const nolanMovieList = [];
for (movie of movieList) {
  if (movie.director === "Christopher Nolan") {
    nolanMovieList.push(movie);
  }
}
console.log(nolanMovieList.length);

// Get titles of movies with an IMDB rating greater or equal to 7.5
const bestTitles = [];
for (movie of movieList) {
  if (movie.imdbRating >= 7.5) {
    bestTitles.push(movie.title);
  }
}
console.log(bestTitles);

// Compute average movie rating of Christopher Nolan's movies
let ratingSum = 0;
let averageRating = 0;
for (movie of nolanMovieList) {
  ratingSum += movie.imdbRating;
}
averageRating = ratingSum / movieList.length;
console.log(averageRating);
```

![Execution result](images/chapter10-01.png)

## Pure functions

The previous program is an example of what is called **imperative programming**. In this paradigm, the programmer gives orders to the computer through a series of statements that modify the program state. Imperative programming focuses on describing *how* a program operates.

The concept of state is an important one. The **state** of a program is the value of its **global variables** (variables visible everythere in the code) at a given time. In our example, the values of `movieList`, `titles`, `nolanMovieCount`, `bestTitles`, `ratingSum` and `averageRating` form the state of the program. Any assignment to one of these variables is a state change, often called a **mutation**.

In imperative programming, the state can be modified anywhere in the source code. This is convenient, but can also lead to nasty bugs and maintenance headaches. As the program grows in size and complexity, it's becoming easier for the programmer to mutate a part of the state by mistake, and harder to monitor state modifications.

A first solution is to split the source code into subroutines called procedures or **functions**. This approach is called **procedural programming** and has the benefit of transforming some variables into **local variables**, which are only visible in the subroutine code.

Let's try to introduce some functions in our code.

```js
// Get movie titles
function titles() {
  const titles = [];
  for (movie of movieList) {
    titles.push(movie.title);
  }
  return titles;
}

// Count movies by Christopher Nolan
function nolanMovies() {
  for (movie of movieList) {
    if (movie.director === "Christopher Nolan") {
      nolanMovieList.push(movie);
    }
  }
}

// Get titles of movies with an IMDB rating greater or equal to 7.5
function bestTitles() {
  const bestTitles = [];
  for (movie of movieList) {
    if (movie.imdbRating >= 7.5) {
      bestTitles.push(movie.title);
    }
  }
  return bestTitles;
}

// Compute average rating of Christopher Nolan's movies
function averageNolanRating() {
  let ratingSum = 0;
  let averageRating = 0;
  for (movie of nolanMovieList) {
    ratingSum += movie.imdbRating;
  }
  return ratingSum / nolanMovieList.length;
}

let nolanMovieList = [];

console.log(titles());
nolanMovies();
console.log(nolanMovieList.length);
console.log(bestTitles());
console.log(averageNolanRating());
```

## Array operations

## Higher-order functions

## Coding time!

TODO