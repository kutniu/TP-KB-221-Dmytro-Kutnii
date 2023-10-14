import random

def play_game():
    choices = ["камінь", "ножиці", "папір"]
    
    user_choice = input("Виберіть (камінь, ножиці, папір): ").lower()
    computer_choice = random.choice(choices)
    
    print(f"Ви вибрали: {user_choice}")
    print(f"Комп'ютер вибрав: {computer_choice}")
    
    if user_choice == computer_choice:
        print("Нічия!")
    elif (user_choice == "камінь" and computer_choice == "ножиці") or \
         (user_choice == "ножиці" and computer_choice == "папір") or \
         (user_choice == "папір" and computer_choice == "камінь"):
        print("Ви перемогли!")
    else:
        print("Комп'ютер переміг!")

if __name__ == "__main__":
    while True:
        play_game()
        play_again = input("Хочете грати ще раз? (так/ні): ")
        if play_again.lower() != "так":
            break
