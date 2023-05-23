import random

#French Menu

from French import french_vocabulary

def f_menu():
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
        translation = input("Translate '{}': ".format(word))

        if translation.lower() == french_vocabulary[category][word].lower():
            print(f"Correct!")
            score += 1
        else:
            print("Incorrect. The correct translation is '{}'.".format(french_vocabulary[category][word]))

    print("Total score: {}/{}".format(score, rounds))

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
    print(f"Wilkommen im German Language Center!")
    category = input(f"Which vocabulary category do you want to learn today? (colors, animals, professions, family, house, sports, school, food, clothes, body): ")
    category = category.lower()
    if category not in german_vocabulary:
        print(f"Sorry this category is not offered by our program. Please try again.")
        return

    rounds = int(input(f"How many rounds do you want to play? (max. 10): "))
    if int(rounds) not in range(0, 11):
        print(f"Sorry, the rounds must be inserted as a integer smaller or equal than 10. Please try again.")
        return

    score = 0

    words = list(german_vocabulary[category].keys())
    random.shuffle(words)

    for i in range(rounds):
        word = words[i]
        translation = input("Translate '{}': ".format(word))

        if translation.lower() == german_vocabulary[category][word].lower():
            print(f"Correct!")
            score += 1
        else:
            print("Incorrect. The correct translation is '{}'.".format(german_vocabulary[category][word]))

    print("Total score: {}/{}".format(score, rounds))

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
    print(f"Bem-vindo ao Portuguese Language Center!")
    category = input(f"Which vocabulary category do you want to learn today? (colors, animals, professions, family, house, sports, school, food, clothes, body): ")
    category = category.lower()
    if category not in portuguese_vocabulary:
        print(f"Sorry this category is not offered by our program. Please try again.")
        return

    rounds = int(input(f"How many rounds do you want to play? (max. 10): "))
    if int(rounds) not in range(0, 11):
        print(f"Sorry, the rounds must be inserted as a integer smaller or equal than 10. Please try again.")
        return

    score = 0

    words = list(portuguese_vocabulary[category].keys())
    random.shuffle(words)

    for i in range(rounds):
        word = words[i]
        translation = input("Translate '{}': ".format(word))

        if translation.lower() == portuguese_vocabulary[category][word].lower():
            print(f"Correct!")
            score += 1
        else:
            print("Incorrect. The correct translation is '{}'.".format(portuguese_vocabulary[category][word]))

    print("Total score: {}/{}".format(score, rounds))

    choice = input(f"Press 'M' to go back to the Portuguese menu or 'L' to go back to the Language Academy main menu: ")
    if choice.lower() == "m":
        p_menu()
    elif choice.lower() == "l":
        l_menu()
    else:
        print(f"Invalid choice. Exiting...")

# Main Menu
def l_menu():
    print(f"Welcome to the Language Learning Center! What language do you want to learn today?")
    print(f"For French press: F")
    print(f"For German press: G")
    print(f"For Portuguese press: P")

    choice = input("I want to learn: ")
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