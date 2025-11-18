# Python Objects: Understanding Mutability, Immutability, and How Everything Works Under the Hood

## Introduction

Every Python developer eventually encounters the same confusion: why do some variable modifications affect other variables while others don't? The answer centers on Python's fundamental design principle: *everything in Python is an object*. Let's examine how Python treats different object types, the mutable versus immutable distinction, and the practical implications for the code.

## Understanding id() and type()

Python provides two essential built-in functions to understand objects: id() and type().

*The type() function* returns the class/type of an object, showing what kind of object you're working with:

python
>>> a = 42
>>> type(a)
<class 'int'>

>>> b = [1, 2, 3]
>>> type(b)
<class 'list'>


*The id() function* returns the object's identity - a unique integer representing its memory address in CPython. This identity remains constant throughout the object's lifetime:

python
>>> a = 42
>>> id(a)
140234866278064

>>> b = [1, 2, 3]
>>> id(b)
140234866278128


The id() is crucial for understanding whether two variables reference the same object in memory or different objects with the same value.

## Mutable Objects

*Mutable objects* are objects whose state or content can be modified after creation without changing their identity. Python's built-in mutable types include:

- Lists (list)
- Dictionaries (dict)
- Sets (set)
- User-defined classes (by default)

Here's what makes an object mutable:

python
>>> my_list = [1, 2, 3]
>>> id(my_list)
140234866278064

>>> my_list.append(4)
>>> my_list
[1, 2, 3, 4]

>>> id(my_list)
140234866278064  # Same ID - object modified in place


The list's identity remains the same even after modification. This has important implications:

python
>>> l1 = [1, 2, 3]
>>> l2 = l1  # l2 is an alias for l1
>>> l1.append(4)
>>> l2
[1, 2, 3, 4]  # l2 also changed!


Both variables reference the *same object* in memory, so modifying through one variable affects the other.

## Immutable Objects

*Immutable objects* cannot be changed after creation. Any operation that appears to modify an immutable object actually creates a new object. Python's built-in immutable types include:

- Integers (int)
- Floats (float)
- Strings (str)
- Tuples (tuple)
- Booleans (bool)
- Frozen sets (frozenset)

Here's how immutability works:

python
>>> a = 89
>>> id(a)
140234866275120

>>> a = 90
>>> id(a)
140234866275152  # Different ID - new object created


With strings:

python
>>> s1 = "Best School"
>>> id(s1)
140234866278200

>>> s1 = s1 + "!"
>>> s1
"Best School!"
>>> id(s1)
140234866278264  # New object created


You cannot modify an immutable object in place - you can only create a new object and reassign the variable.

## Why It Matters: How Python Treats Mutable vs Immutable Objects

Understanding mutability is critical because Python treats these objects differently in several contexts.

### Memory Efficiency

Python uses *integer interning* for small integers (typically -5 to 256):

python
>>> a = 89
>>> b = 89
>>> a is b
True  # Same object!

>>> a = 1000
>>> b = 1000
>>> a is b
False  # Different objects


This optimization saves memory by reusing immutable objects.

### String Interning

Python also interns short strings:

python
>>> s1 = "Best"
>>> s2 = "Best"
>>> s1 is s2
True  # Same object


But longer strings or strings with spaces may not be interned:

python
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> s1 is s2
False  # Usually different objects (implementation-specific)


### Lists Are Never Interned

Lists, being mutable, are never interned - even identical lists are separate objects:

python
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3]
>>> l1 == l2
True  # Same value
>>> l1 is l2
False  # Different objects


### Assignment vs Mutation

With mutable objects, there's a crucial difference between *assignment* (=) and *mutation* (.append(), +=):

python
# Mutation - modifies in place
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> l1.append(4)
>>> l2
[1, 2, 3, 4]  # l2 affected

# Assignment - creates new object
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> l1 = l1 + [4]  # Creates NEW list
>>> l2
[1, 2, 3]  # l2 unaffected
>>> l1
[1, 2, 3, 4]


The operator += behaves differently depending on the object type:

python
# With lists (mutable) - modifies in place
>>> l1 = [1, 2, 3]
>>> original_id = id(l1)
>>> l1 += [4]
>>> id(l1) == original_id
True  # Same object!

# With concatenation - creates new object
>>> l1 = [1, 2, 3]
>>> original_id = id(l1)
>>> l1 = l1 + [4]
>>> id(l1) == original_id
False  # New object!


## How Arguments Are Passed to Functions

Python uses a mechanism often called *"pass by object reference"* or *"pass by assignment"*. The behavior depends on whether the object is mutable or immutable.

### Immutable Objects in Functions

When you pass an immutable object to a function, the function cannot modify the original object:

python
def increment(n):
    n += 1

a = 1
increment(a)
print(a)  # Output: 1 (unchanged)


Why? Because n += 1 creates a *new integer object* and rebinds the local variable n to it. The original object that a references remains unchanged.

### Mutable Objects in Functions

When you pass a mutable object, the function receives a reference to the *same object*:

python
def increment(my_list):
    my_list.append(4)

l = [1, 2, 3]
increment(l)
print(l)  # Output: [1, 2, 3, 4] (modified!)


The function modifies the original list because both the function parameter and the original variable reference the same object in memory.

### Assignment vs Mutation in Functions

However, *assignment* inside a function doesn't affect the original object:

python
def assign_value(n, v):
    n = v  # This is assignment, not mutation

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)  # Output: [1, 2, 3] (unchanged)


The assignment n = v only rebinds the local variable n to point to the object that v references. It doesn't modify the object that l1 references.

### Key Takeaway

Python passes the *reference to the object*, not the object itself or a copy of it. Whether the original object appears to be modified depends on:

1. Whether the object is mutable or immutable
2. Whether you perform *mutation* (e.g., list.append()) or *assignment* (e.g., n = something) inside the function

## Conclusion

Understanding Python's object model is fundamental to writing correct Python code.

- Everything in Python is an object with an identity (id()), type (type()), and value
- Mutable objects can be modified in place; immutable objects cannot
- Python passes objects by reference, but immutability prevents modification
- The distinction between assignment (=) and mutation (.append(), +=) is crucial for mutable objects

Once one internalizes these concepts, many of Python's seemingly quirky behaviors become predictable and logical. This knowledge will help anyone avoid subtle bugs and write more efficient, cleaner code.

---