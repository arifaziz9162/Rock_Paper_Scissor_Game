import random 
import logging

# Stream Logger Setup
logger = logging.getLogger("RockPaperScissor")
logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
stream_handler.setFormatter(formatter)

if not logger.hasHandlers():
    logger.addHandler(stream_handler)

item_list = ["Rock", "Paper", "Scissor"]

def get_winner(user, comp):
    if user == comp:
        return "Tie"
    elif (user == "Rock" and comp == "Scissor") or \
         (user == "Paper" and comp == "Rock") or \
         (user == "Scissor" and comp == "Paper"):
        return "User"
    else:
        return "Computer"

def play_round():
    try:
        user_choice = input("Enter your move (Rock, Paper, Scissor): ").capitalize()
        if user_choice not in item_list:
            raise ValueError("Invalid choice. Choose only Rock, Paper and Scissor.")
        comp_choice = random.choice(item_list)

        print(f"User choice = {user_choice}, Computer_choice = {comp_choice}")
        logger.info(f"User : {user_choice} and Computer : {comp_choice}")

        if user_choice == comp_choice:
            print("Both choose same: = Match Tie")
            logger.info("Result: Tie.")
            return "Tie"

        elif user_choice == "Rock":
            if comp_choice == "Paper":
                print("Paper covers rock = Computer Win.")
                logger.info("Result: Computer Wins.")
                return "Computer"
            else:
                print("Rock smashes scissor = You Win.")
                logger.info("Result: User Wins.")
                return "User"

        elif user_choice == "Paper":
            if comp_choice == "Scissor":
                print("Scissor cuts paper = Computer Win.")
                logger.info("Result: Computer Wins.")
                return "Computer"
            else:
                print("Paper covers rock = You Win.")
                logger.info("Result: User Wins.")
                return "User"

        elif user_choice == "Scissor":
            if comp_choice == "Paper":
                print("Scissor cuts paper = You Win.")
                logger.info("Result: User Wins.")
                return "User"
            else:
                print("Rock smashes scissor = Computer Win.")
                logger.info("Result: Computer Wins.")
                return "Computer"

    except ValueError as ve:
        logger.error(f"Error occurred during user input : {ve}")
        return None

    except Exception as e:
        logger.error(f"Something went wrong please try again : {e}")
        return None

def play_game():
    user_score = 0
    comp_score = 0
    rounds = 5

    for round_num in range(1, rounds + 1):
        print(f"\n--- Round {round_num} ---")
        result = None
        while result is None: 
            result = play_round()
        if result == "User":
            user_score += 1
        elif result == "Computer":
            comp_score += 1
        print(f"Score => You: {user_score} | Computer: {comp_score}")

    print("\n=== Final Result ===")
    if user_score > comp_score:
        print("🎉 Congratulations! You won the game!")
    elif user_score < comp_score:
        print("😞 Computer won the game. Better luck next time!")
    else:
        print("🤝 It's a tie overall!")

    logger.info(f"Final Score => You: {user_score}, Computer: {comp_score}")

def main():
    while True:
        play_game()
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thank you for playing!")
            break


if __name__ == "__main__":
    main()