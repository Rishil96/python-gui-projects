# NATO Alphabet
import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary comprehension to get words for each letter
nato_dict = {row.letter: row.code for _, row in data.iterrows()}

# Get input from user and return its NATO words in list
user_input = input("Enter your word: ")
nato_result = [nato_dict.get(letter.upper(), "") for letter in user_input]

# Print Result
print(f"NATO Words Result: {nato_result}")
