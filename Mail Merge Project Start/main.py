
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
