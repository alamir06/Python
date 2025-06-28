# datat type is a type of data 
# 1. Primitive data type
# 2. 
# primitive is a type of data that is come from the programming language
# 1. int: an integer is a whole number, positive or negative, without decimals, of unlimited length.
# e.g. 1, -2, 3, 0 and large numbers like 1000000, -9999999999999999999999999 , large integer also display by underscore for easier readability like 1_000_000, -999_999_999_999_999_999_999_999_9
# 2. float: a float is a number, positive or negative, containing one or more decimals.
# e.g. 1.0, -2.5, 3.14, 0.0 and large float like 1_000_000.0, -999_999_999_999_999_999.9999999
# 3. string: a string is a sequence of characters, used to store text.
# e.g. "Hello, World!", 'Python is fun', "12345", '1.0', 'True', 'None', '3.14'
# 4. bool: a boolean is a type of data that can only have two values: True or False.
# e.g. True, False

# 5. NoneType: a NoneType is a type of data that represents the absence of a value or a null value.
# 6. complex: a complex number is a number that can be expressed in the form a + bi, where a and b are real numbers and i is the imaginary unit.
# 7. bytes: a bytes object is an immutable sequence of bytes, used to represent binary data.
# 8. bytearray: a bytearray is a mutable sequence of bytes, used to represent binary data that can be modified.
# 9. memoryview: a memoryview is a view of a memory buffer, allowing access to the underlying binary data without copying it.
# 10. range: a range is an immutable sequence of numbers, commonly used in for loops to iterate over a sequence of numbers.
# 11. frozenset: a frozenset is an immutable version of a set, which is an unordered collection of unique elements.
# 12. set: a set is an unordered collection of unique elements, used to store multiple items in a single variable.
# 13. list: a list is an ordered collection of items, which can be of different types, and is mutable (can be changed).
# 14. tuple: a tuple is an ordered collection of items, similar to a list, but it is immutable (cannot be changed).
# 15. dict: a dictionary is an unordered collection of key-value pairs, where each key is unique and maps to a value.
# 16. object: an object is an instance of a class, which can contain data and methods to manipulate that data.
# 17. type: a type is a classification that defines the nature of a data item, determining what operations can be performed on it.
# 18. function: a function is a block of reusable code that performs a specific task, defined by the `def` keyword in Python.
# 19. module: a module is a file containing Python code, which can define functions, classes, and variables, and can be imported into other Python programs to use its functionality.
# 20. class: a class is a blueprint for creating objects, defining their properties and behaviors, encapsulating data and functions that operate on that data.
# 21. method: a method is a function that is defined within a class and is used to operate on instances of that class, allowing for object-oriented programming.
# 22. generator: a generator is a special type of iterator that allows you to iterate over a sequence of values without storing them all in memory at once, using the `yield` keyword to produce values one at a time.
# 23. coroutine: a coroutine is a special type of function that can pause and resume its execution, allowing for asynchronous programming, typically defined using the `async def` syntax in Python.
# 24. async function: an async function is a function defined with the `async def` syntax, which allows it to be paused and resumed, enabling asynchronous programming and the use of `await` to call other async functions.
# 25. async generator: an async generator is a special type of generator that can be used to produce values asynchronously, defined with the `async def` syntax and using `yield` to produce values, allowing for asynchronous iteration.
# 26. async coroutine: an async coroutine is a coroutine defined with the `async def` syntax, which can be paused and resumed, allowing for asynchronous programming and the use of `await` to call other async coroutines, enabling concurrent execution of tasks.
# 27. context manager: a context manager is an object that defines the runtime context to be established when executing a `with` statement, allowing for resource management and cleanup, typically defined using the `__enter__` and `__exit__` methods.
# 28. decorator: a decorator is a special type of function that can modify or enhance the behavior of another function or method, typically defined using the `@decorator_name` syntax before the function definition, allowing for code reuse and separation of concerns.
# 29. lambda function: a lambda function is a small anonymous function defined using the `lambda` keyword, which can take any number of arguments but can only have one expression, often used for short, throwaway functions.
# 30. slice: a slice is an object that represents a set of indices specified by a start, stop, and step, used to access a portion of a sequence like a list or string, defined using the `slice(start, stop, step)` syntax.
# 31. buffer: a buffer is a memory area that can be used to store binary data, allowing for efficient manipulation of large amounts of data without copying it, typically accessed through the `memoryview` object in Python.
# 32. weakref: a weak reference is a reference to an object that does not prevent it from being garbage collected, allowing for memory-efficient management of objects that may be deleted, typically created using the `weakref` module in Python.
# 33. namedtuple: a namedtuple is a subclass of tuple that allows you to define a tuple with named fields, providing a way to access elements by name instead of index, defined using the `collections.namedtuple` function.
# 34. deque: a deque (double-ended queue) is a data structure that allows for fast appends and pops from both ends, providing an efficient way to implement queues and stacks, defined in the `collections` module.
# 35. Counter: a Counter is a subclass of dict that counts the occurrences of elements in an iterable, providing a way to count and tally items efficiently, defined in the `collections` module.
# 36. defaultdict: a defaultdict is a subclass of dict that provides a default value for missing keys, allowing you to avoid key errors and simplify code when working with dictionaries, defined in the `collections` module.

# len() function is used to get the length of an object, such as a string, list, tuple, or dictionary.

# data types and function is like  machine and input for that machine
# function is a machine that takes input and gives output and data type is the input for that machine so,if you give wrong input to the machine it will not work properly or give error similarly if you give wrong data type to the function it will not work properly or give error.
# e.g. if you give a string to a function that expects an integer, it will give an error.
# len(2344) # TypeError: object of type 'int' has no len()
# correct way to use len() function is to give a string, list, tuple, or dictionary as input.

# type conversion is the process of converting one data type to another data type.
# e.g. converting a string to an integer, or a float to an integer, or a list to a tuple, etc.
# type casting is the process of converting one data type to another data type explicitly.
# e.g. int("123") # converts string to integer
print(int("123"))
# e.g. float("123.45") # converts string to float
print(float("123.45"))
# e.g. str(123) # converts integer to string
print(str(123))
# e.g. list((1, 2, 3)) # converts tuple to list
print(list((1, 2, 3)))
# e.g. tuple([1, 2, 3]) # converts list to tuple
print(tuple([1, 2, 3]))
# e.g. dict([(1, 'one'), (2, 'two')]) # converts list of tuples to dictionary
print(dict([(1, 'one'), (2, 'two')]))

# problem: write a function that adds the digits of the two digits of a number and returns the sum.
# description: you should take an integer as input and return the sum of the digits of the number.
number = int(input("Enter a two-digit number: "))
digit1=str(number)[0]
digit2=str(number)[1]
sum_of_digits = int(digit1) + int(digit2)
print(f"The sum of the digits of {number} is {sum_of_digits}")
