# Python Decorators

This repo implements different properties and use cases of decorators as functions.

### Odd Function Runner  
**function** - *odd_it(fn)*  
Above function is a decorator that allows to run any function using it, only at odd seconds, else it prints out "We're even"!  

#### The Decorator in detail:
> It has an outer function *odd_it()* and an inner function *inner(\*args, \*\*kwargs)*.  
> Func *odd_it(fn)* receives the implementing function (which uses this decorator) as input parameter. It wraps around inner the function definition of input function *fn()*, so that the property like function name, parameters etc. are retained inside inner(). It returns an object of inner function.  
> Func *inner(\*args, \*\*kwargs)* takes parameters of fn() as inputs and checks if the current second is even or odd. If odd, then returns evaluated result. If even, prints "We're even" and returns None.  

### Logger Function
**function** - *logger(fn)*  
Above function is a decorator that generates logs about the function sent in as parameter.

#### The Decorator in detail:
> It has an outer function *logger()* and an inner function *inner(\*args, \*\*kwargs)*.  
> Func *logger(fn)* receives the implementing function (which uses this decorator) as input parameter. It wraps around inner the function definition of input function *fn()*, so that the property like function name, parameters etc. are retained inside inner(). It returns an object of inner function.  
> Func *inner(\*args, \*\*kwargs)* takes parameters of fn() as inputs and prints logs which include - function_name,  execution_time,  function_description, function annotation.  


### Decorator Factory Function
**function** - *decorator_factory(access:str)*  
Above function is a decorator that takes in access mode as parameter and sets access to different free variables accordingly.

#### The Decorator in detail:
> It has a factory function - the outermost function, *decorator_factory(access:str)*, which takes in a string input parameter.  
> Function *outer(fn)* and an inner function *inner(\*args, \*\*kwargs)*.  
> Func *outer(fn)* receives the implementing function (which uses this decorator) as input parameter. It wraps around inner the function definition of input function *fn()*, so that the property like function name, parameters etc. are retained inside inner(). It returns an object of inner function.  
> Func *inner(\*args, \*\*kwargs)* takes parameters of fn() as inputs and returns a list of variables based on access modifier set.


### Authenticate Function
**function** - *authenticate(set_password)*  
Above function is a decorator that validates a password sent in as parameter.

#### The Decorator in detail:
> It has an outermost function *authenticate(set_password)*, an outer function *outer(fn)* and an inner function *inner(\*args, \*\*kwargs)*.   
> Func *authenticate(set_password)*
> Func *outer(fn)* receives the implementing function (which uses this decorator) as input parameter. It wraps around inner the function definition of input function *fn()*, so that the property like function name, parameters etc. are retained inside inner(). It returns an object of inner function.  
> Func *inner(\*args, \*\*kwargs)* takes parameters of fn() as inputs and prints logs which include - function_name,  execution_time,  function_description, function annotation.   

### Timed Function
**function** - *timed(reps)*  
Above function is a decorator that executes a function the number of times set as variable reps, prints avg time taken and returns implementing funtion output.

#### The Decorator in detail:
> It has an outermost function *timed(reps)*, an *outer(fn)* and an inner function *inner(\*args, \*\*kwargs)*.    
> Func *timed(reps)* recieves reps containing number of repetitions used as a free variable.  
> Func *outer(fn)* receives the implementing function (which uses this decorator) as input parameter. It wraps around inner the function definition of input function *fn()*, so that the property like function name, parameters etc. are retained inside inner(). It returns an object of inner function.   
> Func *inner(\*args, \*\*kwargs)* takes parameters of fn() as inputs and prints average time taken by a function to execute for a given number of repetitions and returns the output of fn() once executed.

