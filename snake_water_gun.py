import random

def print_header():
    print("="*45)
    print("           🐍 SNAKE WATER GUN 🔫💧")
    print("="*45)
    print("Rules:")
    print("- Snake drinks Water (Snake wins)")
    print("- Water rusts Gun  (Water wins)")
    print("- Gun kills Snake  (Gun wins)")
    print("="*45)

def get_user_choice():
    valid_inputs = {'s': 'snake', 'w': 'water', 'g': 'gun'}
    while True:
        choice = input("\nEnter your choice ([S]nake, [W]ater, [G]un): ").strip().lower()
        
        # Allow user to type the full word or just the first letter
        if choice in valid_inputs:
            return valid_inputs[choice]
        elif choice in valid_inputs.values():
            return choice
        else:
            print("Invalid choice. Please try again.")

def play_game():
    print_header()

    # Match the slider logic from the HTML (choosing number of rounds)
    try:
        total_rounds = int(input("\nHow many rounds do you want to play? (e.g., 3, 5, 11): "))
    except ValueError:
        print("Invalid input. Defaulting to 5 rounds.")
        total_rounds = 5

    user_score = 0
    comp_score = 0
    choices = ['snake', 'water', 'gun']
    icons = {'snake': '🐍', 'water': '💧', 'gun': '🔫'}

    # Game logic dicts directly mirroring your JS `OUTCOMES` and `RULES`
    outcomes = {
        ('snake', 'water'): 'win',  ('water', 'gun'): 'win',  ('gun', 'snake'): 'win',
        ('water', 'snake'): 'lose', ('gun', 'water'): 'lose', ('snake', 'gun'): 'lose'
    }

    rules_text = {
        ('snake', 'water'): 'Snake drinks water',
        ('water', 'gun'): 'Water rusts gun',
        ('gun', 'snake'): 'Gun kills snake',
    }

    # Main game loop
    for round_num in range(1, total_rounds + 1):
        print(f"\n--- Round {round_num} of {total_rounds} ---")
        
        user_choice = get_user_choice()
        comp_choice = random.choice(choices)

        print(f"\nYou chose:      {icons[user_choice]} {user_choice.capitalize()}")
        print(f"Computer chose: {icons[comp_choice]} {comp_choice.capitalize()}")

        # Determine winner
        if user_choice == comp_choice:
            print("Result: Same choice — it's a draw!")
        else:
            result = outcomes[(user_choice, comp_choice)]
            
            if result == 'win':
                rule = rules_text.get((user_choice, comp_choice), "")
                print(f"Result: {rule}. You win this round! ✅")
                user_score += 1
            else:
                rule = rules_text.get((comp_choice, user_choice), "")
                print(f"Result: {rule}. Computer wins this round. ❌")
                comp_score += 1

        print(f"Scoreboard -> You: {user_score} | Computer: {comp_score}")

    # Final Match Banner
    print("\n" + "="*45)
    print("               FINAL RESULTS")
    print("="*45)
    print(f"Total Rounds Played: {total_rounds}")
    print(f"Your Score: {user_score}")
    print(f"Computer Score: {comp_score}\n")

    if user_score > comp_score:
        print("🏆 You won the match! 🎉")
    elif comp_score > user_score:
        print("💀 Computer won the match.")
    else:
        print("🤝 It's a tie match!")

if __name__ == "__main__":
    play_game()
