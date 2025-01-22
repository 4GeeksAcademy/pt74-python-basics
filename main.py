import random

"""
/**
 * Variables
 * A way to give data a name
 */
"""
# Variables
# Bare-word variable assignment

some_var = "Some value"

some_str = "This is a string"
some_other_str = 'This is also a string'

some_str_literal = """
This is a string literal!

It can have line breaks!
"""

# fstrings are like string formatting literals in JS:
some_fstring = f"This is an f string!  {0.1 + 0.2}"
# print(some_fstring)

some_int = 1
some_float = 0.1

# PascalCase = "camelCase with the first letter capitalized as well."

# print("We run our programs with the python interpreter.")

"""
/**
 * Booleans!
 * Are a binary value, always true or false.
 */
"""
some_true = True
some_false = False
some_null = None

# We will still be writing most of our
# booleans as expressions:
# print((0.2 + 0.2) == 0.3)

"""
/**
 * Arrays
 * A way to store iterable data
 */
"""
some_list = [
    "Lists work much the same way in Python.",
    "They are still collections of iterable data.",
    "They still are indexed from 0!",
    "And finally, they are still made with [] and ,",
]
# print(some_list)

some_sorted_list = sorted(
    some_list
)
# print(some_sorted_list)

some_filtered_list = list(filter(
    # (x) => x.length <= 39
    lambda x: len(x) <= 39,
    some_list
))
# print(some_filtered_list)

# We'll come back to how weird tuples are later...
some_tuple = (1,)
# some_tuple[0] = 2
print(some_tuple)

"""
/**
 * Objects
 * A way to store related data.
 */
"""
some_dict = {
    "title": "Something Wicked This Way Comes",
    "author": "Ray Bradbury",
    "num_pages": 293,
    "year_published": 1997,
    "isbn13": "978-0-380-72940-1",
    "isbn10": "0-380-72940-7",
    "is_awesome": True,
    "good_chapters": [
        '''Chapter 31 - "Nothing much else happened, all the rest of that night."''',
    ],
}

# You can iterate over k/v pairs in a dictionary:

# for k, v in some_dict.items():
#     print(f"{k}: {v}")

some_dict["title"] = "Something Wicked This Way Comes 2"

# print(some_dict)
# some_dict["title"]
# print(some_dict.get("some random key", "default value"))

library = [
    {
        "title": "Something Wicked This Way Comes",
        "author": "Ray Bradbury",
        "num_pages": 293,
        "year_published": 1997,
        "isbn13": "978-0-380-72940-1",
        "isbn10": "0-380-72940-7",
        "is_awesome": True,
    },
    {
        "title": "One Hundred Years of Solitude",
        "author": "Gabriel Garcia Marquez",
        "num_pages": 383,
        "year_published": 1970,
        "isbn13": None,
        "isbn10": "0-380-01503-X",
        "is_awesome": True,
    },
    {
        "title": "Snow Crash",
        "author": "Neal Stephenson",
        "num_pages": 470,
        "year_published": 1992,
        "isbn13": "978-061336162",
        "isbn10": None,
        "is_awesome": True,
    },
    {
        "title": "The Ultimate Hitchiker's Guide To The Galaxy",
        "author": "Douglas Adams",
        "num_pages": 815,
        "year_published": 2002,
        "isbn13": "978-0-645-45374-7",
        "isbn10": None,
        "is_awesome": True,
    },
]

# for book in library:
#     print(book["title"])

# for idx, book in enumerate(library):
#     print(idx, book["title"])

# for thing in enumerate(library):
#     print(thing)

# is_done = False

# while not is_done:
#     rand = random.randint(1, 10)
#     print(f"The random number is {rand}")
#     if rand > 5:
#         is_done = True

"""
/**
 * Operators!
 */
// = --> assignation or assigning values
let equality = "10" == 10; // This will be truthy.
let strictEquals = "10" === 10; // This will be falsy.
let inequality = "10" != 10; // This will be falsy.
let strictNotEquals = "10" !== 10; // This will be truthy.
let negate = !10; // This will be falsy.
let lessThan = 5 < 10; // This will be truthy.
let lte = 5 <= 10; // This will be truthy.
let greaterThan = 10 > 5; // This will be truthy.
let gte = 10 >= 5; // This will be truthy.
// Plus can add numbers or concatenate strings.
let plus = 10 + 10; // This will equal 20.
plus = "This first string " + "has been concatenated with this other string.";
// console.log(plus);
let min = 10 - 10; // This will equal 0.
let mul = 10 * 10; // This will equal 100.
let div = 10 / 10; // 1
let pow = 10 ** 10; // 10000000000
let modulo = 10 % 3; // 1
"""

# Identity operations:
# x = {
#     "a": 0,
#     "b": 1
# }

# y = {
#     "a": 0,
#     "b": 1
# }

# if x is y:
#     print("Well, yeah.")
# else:
#     print("Wait, what?")

"""
/**
 * Functions
 * Let you define or name behavior that you want to use.
 */
"""
def some_func():
    print("Hello world!")

# some_func()

def some_returning_func():
    return "Hello world!"

# print(some_returning_func())

"""
/**
 * Generator functions let us iterate over a function.
 */
const fibGen = function*(n = 15) {
  let prev = 0n;
  let curr = 1n;
  for (let i = 0; i < n; i++) {
    let temp = curr;
    curr = prev + curr;
    prev = temp;
    yield prev;
  }
};
"""
def fib_gen(n=15):
    prev = 0
    curr = 1
    for _ in range(n):
        temp = curr
        curr = prev + temp
        prev = temp
        yield prev


# for fib in fib_gen(100):
#     print(fib)

"""
// Arrow or anonymous functions support implicit returns.
"""
some_anon_func = lambda x: f"You input {x} into this function"

# print(some_anon_func('"What?"'))
