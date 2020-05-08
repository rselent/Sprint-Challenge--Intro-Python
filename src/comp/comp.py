# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("\nStarts with D:")
a = [human.name for human in humans if human.name[0] == "D"]
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("\nEnds with e:")
b = [human.name for human in humans if human.name[-1] == "e"]
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("\nStarts between C and G, inclusive:")
c = [human.name for human in humans if "C" <= human.name[0] <= "G"]
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("\nAges plus 10:")
d = [human.age + 10 for human in humans]
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("\nName hyphen age:")
e = [str( human.name) + "-" + str( human.age) for human in humans]
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("\nNames and ages between 27 and 32:")
f = [(human.name, human.age) for human in humans if 27 <= human.age <= 32]
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("\nAll names uppercase:")
g = [Human( human.name.upper(), human.age + 5) for human in humans]
print(g)
print( id( humans), id( a), id( b), id( g))     # verifying if new list or copy

# Write a list comprehension that contains the square root of all the ages.
print("\nSquare root of ages:")
import math
h = [ f"{math.sqrt( human.age):.2f}" for human in humans]
print(h)
