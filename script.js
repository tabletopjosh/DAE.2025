// Centralize JavaScript Management
// All JavaScript code is in this file

// Create interactive web pages
// Connect this JavaScript file to an HTML webpage

// Utilize descriptive variable names
let userName = "Joshua";
let userAge = 25;

// Integrate distinct data types
let isStudent = true;
let numberOfCourses = 4;

// Implement Mathematical Operation s
let sum = numberOfCourses + 1;

// Create decision making with decision structures
if (userAge >= 18) {
    console.log(userName + " is an adult.");
} else {
    console.log(userName + " is a minor.");
}

// Utilize Logical Operators for Complex Condition Evaluation
if (isStudent && numberOfCourses > 0) {
    console.log(userName + " is a student enrolled in courses.");
} else {
    console.log(userName + " is not currently a student.");
}

// Showcase JavaScript Output Techniques
document.getElementById("output").innerHTML = "Hello, " + userName + "! Your sum is: " + sum;
console.log("Hello, " + userName + "! Your sum is: " + sum);