# Mail Merge

# Load names from the text file
with open("Input/Names/invited_names.txt") as names:
    names_list = names.read()
    names_list = names_list.split("\n")

# Invite template letter
with open("Input/Letters/starting_letter.txt") as letter:
    letter_template = letter.read()

# Loop through every name
for name in names_list:
    # Add name in letter template
    new_letter = letter_template.replace("[name]", name)
    # Write mail to text file
    with open(f"Output/ReadyToSend/letter_to_{name.lower()}.txt", "w") as f:
        f.write(new_letter)
