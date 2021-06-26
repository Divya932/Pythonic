### This folder contains example implementations of Closures to understand scope of variables and how closures behave

## What is a Closure?  
A Closure is a **function object** that remembers values in **enclosing scopes** even if they are not present in memory.
It implements the concept of **nested functions** and heavily uses **scope of variables** to provide its functionality.
Scope of variables can be defined as:
1. Global: Exists outside all functions and is accessible anywhere inside a module.
2. Local: Exists inside a block or function. Accessible only inside the function
3. Nonlocal: Found in Nested functions. Inside outer function, but outside inner function. Can be modified by inner function once declared with keyword **nonlocal** inside inner function.

Refer other sources for terms like **lexical scope** and **dynamic scope**.

**When do nested functions act like a closure?**
When the outer function does not call the inner function, but returns the inner function, that is when it acts like a closure. This provides a dynamic nature to our function and can be used as per the needs. Also keeps the inner function secure from being tampered by any user.

> Refer the code files above to understand functionalities of closures.  

1. [docstring_closure.ipynb](https://github.com/Divya932/Pythonic/blob/main/Closures_%26_Scope/docstring_closure.ipynb) contains code for a closure that takes a function and then checks whether the function passed has a docstring with more than 50 characters.  
Concept Tags: free variables, docstrings

2. [fibonacci_closure.ipynb](https://github.com/Divya932/Pythonic/blob/main/Closures_%26_Scope/fibonacci_closure.ipynb) gives you the next Fibonacci number

3. [counter_closure.ipynb](https://github.com/Divya932/Pythonic/blob/main/Closures_%26_Scope/counter_closure.ipynb) counts how many times a function was called and updates the counts in one/multiple dictionaries.
