word = "Emma"
letter_print = "_"*len(word)
guess = input("guess: ")
for _ in range(word.count(guess)):
 ind = word.find(guess)
 letter_print.replace(_, guess)