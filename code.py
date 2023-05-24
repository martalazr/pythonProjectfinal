import random

#French Menu

from French import french_vocabulary

def f_menu():

    '''
       Allows the user to translate words from a specific category from English to French by specifying the number of rounds the learner wishes to play

               Parameters:
                       category: indicates the topic category the user wants to be tested on.
                       rounds: an integer value that indicates the number of rounds the user wants to play (number of words to translate).
                       word: word from the French list within the chosen category to be translated
                       translation: allows the user to insert their translation into the program.

               Returns:
                      A score board that tells the user how many correct translations they have.
                      In each round, the user will be able to know if they translated the word correctly and, if not, see the correct translation.
       '''

    print(f"Bienvenu au French Language Center!")
    category = input(f"Which vocabulary category do you want to learn today? (colors, animals, professions, family, house, sports, school, food, clothes, body): ")
    category = category.lower()
    if category not in french_vocabulary:
        print(f"Sorry this category is not offered by our program. Please try again.")
        return

    rounds = int(input(f"How many rounds do you want to play? (max. 10): "))
    if int(rounds) not in range(0, 11):
        print(f"Sorry, the rounds must be inserted as a integer smaller or equal than 10. Please try again.")
        return

    score = 0

    words = list(french_vocabulary[category].keys())
    random.shuffle(words)

    for i in range(rounds):
        word = words[i]
        translation = input(f"Translate {word}: ")

        if translation.lower() == french_vocabulary[category][word].lower():
            print(f"Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct translation is {french_vocabulary[category][word]}.")

    print(f"Total score: {score}/{rounds}")

    choice = input(f"Press 'M' to go back to the French menu or 'L' to go back to the Language Academy main menu: ")
    if choice.lower() == "m":
        f_menu()
    elif choice.lower() == "l":
        l_menu()
    else:
        print(f"Invalid choice. Exiting...")

#German Menu

from German import german_vocabulary

def g_menu():
    '''
          Allows the user to translate words from a specific category from English to German by specifying the number of rounds the learner wishes to play

                  Parameters:
                          category: indicates the topic category the user wants to be tested on.
                          rounds: an integer value that indicates the number of rounds the user wants to play (number of words to translate).
                          word: word from the German list within the chosen category to be translated
                          translation: allows the user to insert their translation into the program.

                  Returns:
                         A score board that tells the user how many correct translations they have.
                         In each round, the user will be able to know if they translated the word correctly and, if not, see the correct translation.
          '''

    print(f"Wilkommen im German Language Center!")
    category = input(f"Which vocabulary category do you want to learn today? (colors, animals, professions, family, house, sports, school, food, clothes, body): ")
    category = category.lower()
    if category not in german_vocabulary:
        print(f"Sorry this category is not offered by our program. Please try again.")
        return

    rounds = int(input(f"How many rounds do you want to play? (max. 10): "))
    if int(rounds) not in range(0, 10):
        print(f"Sorry, the rounds must be inserted as a integer smaller or equal than 10. Please try again.")
        return

    score = 0

    words = list(german_vocabulary[category].keys())
    random.shuffle(words)

    for i in range(rounds):
        word = words[i]
        translation = input(f"Translate {word}: ")

        if translation.lower() == german_vocabulary[category][word].lower():
            print(f"Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct translation is {german_vocabulary[category][word]}.")

    print(f"Total score: {score}/{rounds}")

    choice = input(f"Press 'M' to go back to the German menu or 'L' to go back to the Language Academy main menu: ")
    if choice.lower() == "m":
        g_menu()
    elif choice.lower() == "l":
        l_menu()
    else:
        print(f"Invalid choice. Exiting...")

#Portuguese Menu

from Portuguese import portuguese_vocabulary

def p_menu():

    '''
             Allows the user to translate words from a specific category from English to Portuguese by specifying the number of rounds the learner wishes to play

                     Parameters:
                             category: indicates the topic category the user wants to be tested on.
                             rounds: an integer value that indicates the number of rounds the user wants to play (number of words to translate).
                             word: word from the Portuguese list within the chosen category to be translated
                             translation: allows the user to insert their translation into the program.

                     Returns:
                            A score board that tells the user how many correct translations they have.
                            In each round, the user will be able to know if they translated the word correctly and, if not, see the correct translation.
             '''

    print(f"Bem-vindo ao Portuguese Language Center!")
    category = input(f"Which vocabulary category do you want to learn today? (colors, animals, professions, family, house, sports, school, food, clothes, body): ")
    category = category.lower()
    if category not in portuguese_vocabulary:
        print(f"Sorry this category is not offered by our program. Please try again.")
        return

    rounds = int(input(f"How many rounds do you want to play? (max. 10): "))
    if int(rounds) not in range(0, 10):
        print(f"Sorry, the rounds must be inserted as a integer smaller or equal than 10. Please try again.")
        return

    score = 0

    words = list(portuguese_vocabulary[category].keys())
    random.shuffle(words)

    for i in range(rounds):
        word = words[i]
        translation = input(f"Translate {word}: ")

        if translation.lower() == portuguese_vocabulary[category][word].lower():
            print(f"Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct translation is {portuguese_vocabulary[category][word]}.")

    print(f"Total score: {score}/{rounds}")

    choice = input(f"Press 'M' to go back to the Portuguese menu or 'L' to go back to the Language Academy main menu: ")
    if choice.lower() == "m":
        p_menu()
    elif choice.lower() == "l":
        l_menu()
    else:
        print(f"Invalid choice. Exiting...")

# Main Menu
def l_menu():

    '''
                 Language Center main menu, in which the user can select the language they want to be tested on

                         Parameters:
                             choice: User's input of the first letter of the language they want to get tested on (f, g, p)

                         Returns:
                                Calls the function of the selected language menu to start the translation quiz
                 '''

    print(f"Welcome to the Language Learning Center! What language do you want to learn today?")
    print(f"For French press: F")
    print(f"For German press: G")
    print(f"For Portuguese press: P")

    choice = input(f"I want to learn: ")
    choice = choice.lower()

    if choice == "f":
        f_menu()
    elif choice == "g":
        g_menu()
    elif choice == "p":
        p_menu()
    else:
        print(f"Sorry, {choice} is not offered by the Language Center. Exiting...")

l_menu()
