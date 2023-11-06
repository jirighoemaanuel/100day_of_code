# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# names = []
# with open('./Input/Names/invited_names.txt') as invited_names:
#     for name in invited_names:
#         names.append(name.rstrip())

# with open('./Input/Letters/starting_letter.txt', 'r') as starting_letter:
#     letter = starting_letter.read()
#     for name in names:
#         letter = letter.replace["[name]", name]
#         with open(f'./Output/ReadyToSend/{name}.txt', 'w') as readytosend:
#             readytosend.write(letter)

names = []
with open('./Input/Names/invited_names.txt') as invited_names:
    for name in invited_names:
        names.append(name.rstrip())

with open('./Input/Letters/starting_letter.txt', 'r') as starting_letter:
    letter = starting_letter.read()
    for name in names:
        personalized_letter = letter.replace("[name]", name)
        with open(f'./Output/ReadyToSend/{name}.txt', 'w') as readytosend:
            readytosend.write(personalized_letter)

    # Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
    # Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
