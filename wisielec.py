import sys
number_of_tries = 5
word="laptop"
user_word = []
used_letters = []

def find_indexes(word, letter):
    indexes=[]
    for index,letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)
    return indexes

def state_of_game():
    print()
    print(user_word)
    print(f"Uzyte litery: {used_letters}")
    print(f"Pozostalo prob: {number_of_tries}")
    print()





for _ in word:
    user_word.append("_")



while True:
    letter = input("Podaj litere: ")
    used_letters.append(letter)
    found_indexes = find_indexes(word,letter)

    if len(found_indexes) == 0 :
        print("Nie ma takiej litery")
        number_of_tries -=1

        if number_of_tries ==0:
            print("Koniec gry")
            sys.exit(0)
    else:
        for index in found_indexes:
            user_word[index] = letter

        if word == "".join(user_word):
            print("Brawo to jest to slowo")
            print("".join(user_word))
            sys.exit()
    state_of_game()



