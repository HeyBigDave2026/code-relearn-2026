# lesson01_types.py
# Phase 2 - lesson 1: Variables & Types
# Dave, May 2026

# --- Basic types ---
name = "Dave"  # string
years_away = 31  # integer
completion_pct = 0.0  # float
is_rusty = True  # boolean

# type() tells you what you;re dealing with
print(type(name)) # <class 'str'>
print(type(years_away)) # <class 'int'>

# --- Dynamic typing in action ---
x = 42
print(type(x)) # int
x = "Now I'm a string!"
print(type(x)) # str -Python is dynamically typed, so the type of x can change at runtime
# ***BE CAREFUL DAVE*** - this can lead to bugs if you're not careful! :-)

# --- f-strings: your new sprintf ---
# f-strings are a way to embed expressions inside string literals, using curly braces {}
print(f"Name: {name}, Years away: {years_away}, Completion: {completion_pct}%, Rusty: {is_rusty}")

# --- None: Python's null ----
result = None  # None is a special value that represents the absence of a value
print(result is None) # True - use 'is' to check for None, not '=='

# --- Type conversion ---
age_str = "55"
age_int = int(age_str)  # Convert string to integer
print(age_int + 1) # 56 - explicit cast, just like C

# --- Quick sanity check ---
a, b, c = 1, 2, 3 # tuple unpacking - assign multiple variables in one line
print (a, b, c)



