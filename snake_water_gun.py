
"""
Snake–Water–Gun Game (Python)
Rules:
- snake drinks water  -> snake wins
- water rusts gun     -> water wins
- gun kills snake     -> gun wins
"""

import random

CHOICES = {
    "s": "snake",
    "w": "water",
    "g": "gun"
}


OUTCOMES = {
    ("snake", "water"): "win",
    ("water", "gun"): "win",
    ("gun", "snake"): "win",
    ("water", "snake"): "lose",
    ("gun", "water"): "lose",
    ("snake", "gun"): "lose",
}

def normalize(choice: str) -> str:
    c = choice.strip().lower()
    if c in CHOICES:
        return CHOICES[c]
    if c in CHOICES.values():
        return c
    raise ValueError("Invalid choice. Use 's'/'snake', 'w'/'water', or 'g'/'gun'.")

def decide_winner(player: str, computer: str) -> str:
    if player == computer:
        return "draw"
    return OUTCOMES.get((player, computer), "lose") 

def prompt_round(round_no: int) -> tuple[str, str, str]:
    while True:
        try:
            raw = input(f"[Round {round_no}] Choose (s)nake, (w)ater, (g)un: ")
            player = normalize(raw)
            break
        except ValueError as e:
            print(e)
    computer = random.choice(list(CHOICES.values()))
    result = decide_winner(player, computer)
    return player, computer, result

def play_best_of(total_rounds: int) -> None:
    player_score = 0
    computer_score = 0

    for r in range(1, total_rounds + 1):
        player, computer, result = prompt_round(r)
        if result == "win":
            player_score += 1
            msg = "You win this round!"
        elif result == "lose":
            computer_score += 1
            msg = "Computer wins this round."
        else:
            msg = "It's a draw."
        print(f" You: {player} | Computer: {computer} -> {msg}")
        print(f" Score: You {player_score} - {computer_score} Computer\n")

    print("Final Result".center(30, "-"))
    if player_score > computer_score:
        print(f"You won the match! 🎉 ({player_score}-{computer_score})")
    elif computer_score > player_score:
        print(f"Computer won the match. ({computer_score}-{player_score})")
    else:
        print(f"It's a tie! ({player_score}-{computer_score})")

def main():
    print("=== Snake–Water–Gun ===")
    print("Enter 's'/'snake', 'w'/'water', or 'g'/'gun'.")
    while True:
        try:
            rounds = int(input("How many rounds? (odd number recommended): ").strip())
            if rounds <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    if rounds % 2 == 0:
        print(f"Even number detected. Playing {rounds + 1} rounds to avoid ties.")
        rounds += 1
    play_best_of(rounds)
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
