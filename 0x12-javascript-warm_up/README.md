**_Learning Objectives_**
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

**_General_**
Why JavaScript programming is amazing
How to run a JavaScript script
How to create variables and constants
What are differences between var, const and let
What are all the data types available in JavaScript
How to use the if, if ... else statements
How to use comments
How to affect values to variables
How to use while and for loops
How to use break and continue statements
What is a function and how do you use functions
What does a function that does not use any return statement return
Scope of variables
What are the arithmetic operators and how to use them
How to manipulate dictionary
How to import a file

**_Process Object_**

In computing, a process in a running instance of a software program. A software program is simply an executable file of computer programming codes i.e. in lower level programming language like C, it can be a compiled and executable binary file or in higher level programming languages, it can be a source code that is intepreted at execution i.e. a software can be a packaged source code ready to be intepreted by an intepreter. Each process is isolated in the sense that when you run two identical software programs on two different locations in the same computer, they will both run as separate process each having its own process ID. Processes are isolated in the sense that each process is allocated its own resource i.e memory, CPU time or I/O devices

In JavaScript, the keyword 'process' represents the process object, which is a global object specific to the Node.js runtime environment. The process object is available globally and provides information and control over the current Node.js process. While it is not a direct instance of the 'EventEmitter' class, it does emit events and shares some similarities with the event emitter pattern. The process object can be accessed by any running JavaScript code within the Node.js environment. This process object will provide information and control on the current process, i.e the current program. The process object has information such command line arguments run together with the script and methods like 'process.exit()' which terminates the current process. process.argv[0] is the path to the node.js intepreter
