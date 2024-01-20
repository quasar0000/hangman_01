while True:
    word = input("Type in your secret word to start the game:\n").lower()

    if " " in word:
        print("No spaces allowed.")
    elif any(char.isdigit() for char in word):
        print("No numbers allowed.")
    elif not word.isalpha():
        print("Only letters allowed")
    else:
        break

word = word.lower()
visible_word = word.replace(word, '_' * len(word))
print("Your word has this many letters:", visible_word)

num_hits = 0
letters_guessed = []

while num_hits <= 5 and not word == visible_word:
    userLetter = input("Guess a letter").lower()

    if userLetter in letters_guessed:
        print("You already guessed that letter! Try again.")
    # letters_guessed.append(userLetter)
    elif len(userLetter) > 1:
        print("Please only type in one letter")
    elif not userLetter.isalpha():
        print("Please guess a LETTER")
    else:
        letters_guessed.append(userLetter)
        print("You guessed ", userLetter.lower())

        if userLetter in word:
            print("There is/are", word.count(userLetter), userLetter)
            # slicing (replace doesn't take three inputs, only two.)
            letter_places = [i for i, letter in enumerate(word) if letter == userLetter]

            for letter_place in letter_places:
                visible_word = visible_word[:letter_place] + userLetter + visible_word[letter_place + 1:]
                print("Updated word:",visible_word)

        else:
            print("You got hit")
            num_hits += 1
            print("You have", 6-num_hits, "hits left")
            if num_hits == 6:
                print("Hangman. Game Over")

    if word == visible_word:
        print("You win!!!")
        exit()