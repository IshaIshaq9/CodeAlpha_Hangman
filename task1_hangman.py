# ===== TASK 1: HANGMAN GAME =====

import random  # random module: list me se random word chunne ke liye

# 5 predefined words ki list
words = ["python", "program", "computer", "internet", "keyboard"]

word = random.choice(words)      # list me se ek random word select karo
guessed = []                     # jo letters player guess kar chuka hai unki list
wrong = 0                        # galat guesses ka counter
max_wrong = 6                    # maximum allowed galat guesses

print("=== HANGMAN GAME ===")
print("Word guess karo, 6 galat guesses allowed hain.\n")

while wrong < max_wrong:         # jab tak 6 galat guesses nahi hote, game chalta rahe
    # Word ka display banao: sahi letter dikhao, baaki ke liye "_"
    display = ""
    for letter in word:          # word ke har letter par loop
        if letter in guessed:    # agar letter pehle guess ho chuka hai
            display += letter + " "
        else:
            display += "_ "

    print("Word:", display)
    print("Galat guesses bache:", max_wrong - wrong)

    # Check: kya saare letters guess ho gaye? (koi "_" nahi bacha)
    if "_" not in display:
        print("\n🎉 Mubarak ho! Aap jeet gaye! Word tha:", word)
        break                    # loop se bahar

    guess = input("Ek letter likho: ").lower()   # input lo aur lowercase me convert karo

    # Input validation: sirf ek alphabet hona chahiye
    if len(guess) != 1 or not guess.isalpha():
        print("Please sirf ek letter likho!\n")
        continue                 # agle round par jao

    if guess in guessed:         # agar pehle hi guess kar chuke hain
        print("Ye letter pehle guess ho chuka hai!\n")
        continue

    guessed.append(guess)        # letter ko guessed list me daalo

    if guess in word:            # agar letter word me hai
        print("✅ Sahi guess!\n")
    else:                        # agar letter word me nahi hai
        wrong += 1               # galat counter +1
        print("❌ Galat guess!\n")
else:
    # while-else: ye tab chalta hai jab loop bina break ke khatam ho (yaani player haar gaya)
    print("\n💀 Game Over! Sahi word tha:", word)
