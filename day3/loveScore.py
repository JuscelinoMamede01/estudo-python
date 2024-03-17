# This is a difficult challenge! 💪
# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs.

# Then check for the number of times the letters in the word LOVE occurs.

# Then combine these numbers to make a 2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:

# "Your score is *x*, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:

# "Your score is *y*, you are alright together."
# Otherwise, the message will just be their score. e.g.:

# "Your score is *z*."
# e.g.

# name1 = "Angela Yu"
# name2 = "Jack Bauer"
# T occurs 0 times

# R occurs 1 time

# U occurs 2 times

# E occurs 2 times

# Total = 5

# L occurs 1 time

# O occurs 0 times

# V occurs 0 times

# E occurs 2 times

# Total = 3

# Love Score = 53

# Print: "Your score is 53."

# These functions will help you:
# lower() count()

# Example Input 1
# Kanye West
# Kim Kardashian
# Example Output 1
# The Love Calculator is calculating your score...
# Your score is 42, you are alright together.
# Example Input 2
# Brad Pitt
# Jennifer Aniston
# Example Output 2
# The Love Calculator is calculating your score...
# Your score is 73.
# Hint
# You can check your values against mine using this table:

# Name 1	        Name 2	            Score
# Brad Pitt	        Jennifer Aniston	73
# Prince William	Kate Middleton	    67
# Ashton Kutcher	Mila Kunis	        63
# Angela Yu	Jack    Bauer	            53
# David Beckham	    Victoria Beckham	45
# Mario	Princess    Peach	            43
# Kanye West	    Kim Kardashian	    42


print("\033[92m*******************************")
print("THE LOVE SCORE")
print("*******************************\033[0m")

name1 = input("Digite o primeiro nome:\n ").upper()
name2 = input("Digite o segundo nome:\n ").upper()

combined_names = name1 + name2
print(combined_names)

t = combined_names.count("T")
r = combined_names.count("R")
u = combined_names.count("U")
e = combined_names.count("E")
print('t', t)
print('r', r)
print('u', u)
print('e', e)

first_digit = t + r + u + e
print('true nome', first_digit)

l = combined_names.count("L")
o = combined_names.count("O")
v = combined_names.count("V")
e2 = combined_names.count("E")


print('l', l)
print('o', o)
print('v', v)
print('e', e)

second_digit = l + o + v + e2
print('true nome', second_digit)

love_score = int(str(first_digit) + str(second_digit))
print(love_score)

if love_score <= 10 or love_score >= 90:
    print(
        "\033[92m*****************************************************************")
    print(f"Your score is {love_score}, you go together like coke and mentos.")
    print(
        "*****************************************************************\033[0m")
elif love_score >= 40 and love_score <= 50:
    print(
        "\033[92m*****************************************************************")
    print(f"Your score is {love_score}, you are alright together.")
    print(
        "*****************************************************************\033[0m")
else:
    print(f"Your score is {love_score}.")
