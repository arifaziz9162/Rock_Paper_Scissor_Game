import random 
import logging

# File handler and stream handler setup
logger = logging.getLogger("Rock_Paper_Scissor_Logger")
logger.setLevel(logging.DEBUG)

if logger.hasHandlers():
    logger.handlers.clear()

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)  
stream_handler.setFormatter(formatter)

file_handler = logging.FileHandler("rock_paper_scissor.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)



class RockPaperScissorsGame:
    CHOICES = ["Rock", "Paper", "Scissor"]

    def __init__(self, rounds=5):
        self.rounds = rounds
        self.user_score = 0
        self.comp_score = 0


    def get_computer_choice(self):
        return random.choice(self.CHOICES)


    def get_user_choice(self):
        choice = input("Enter your move (Rock, Paper, Scissor): ").title()
        if choice not in self.CHOICES:
            raise ValueError("Invalid choice. Choose Rock, Paper, or Scissor.")
        return choice


    def decide_winner(self, user, comp):
        if user == comp:
            return "Tie"
        elif (user == "Rock" and comp == "Scissor") or \
            (user == "Paper" and comp == "Rock") or \
            (user == "Scissor" and comp == "Paper"):
            return "User"
        else:
            return "Computer"


    def play_round(self):
        try:
            user = self.get_user_choice()
            comp = self.get_computer_choice()
            logger.info(f"User: {user}, Computer: {comp}")
            print(f"User: {user}, Computer: {comp}")

            winner = self.decide_winner(user, comp)
            if winner == "User":
                print("You win this round!")
                logger.info("Round result: User wins")
                self.user_score += 1
            elif winner == "Computer":
                print("Computer wins this round!")
                logger.info("Round result: Computer wins")
                self.comp_score += 1
            else:
                print("This round is a tie!")
                logger.info("Round result: Tie")
            
            return True
           
        except ValueError as ve:
            logger.error(f"Error occurred during user input : {ve}")
            print(str(ve))
 
        except Exception as e:
            logger.error(f"Something went wrong please try again : {e}")
            print(str(e))
       

    def play_game(self):
        for round_num in range(1, self.rounds + 1):
            print(f"\n--- Round {round_num} ---")
            while not self.play_round():
                continue
            print(f"Score => You: {self.user_score} | Computer: {self.comp_score}")

        self.show_final_result()


    def show_final_result(self):
        print("\n=== Final Result ===")
        if self.user_score > self.comp_score:
            print("🎉 Congratulations! You won the game!")
        elif self.user_score < self.comp_score:
            print("😞 Computer won the game. Better luck next time!")
        else:
            print("🤝 It's a tie overall!")

        logger.info(f"Final Score => You: {self.user_score}, Computer: {self.comp_score}")


def main():
        while True:
            game = RockPaperScissorsGame(rounds=5)
            game.play_game()
            again = input("\nDo you want to play again? (yes/no): ").strip().lower()
            if again != "yes":
                print("Thank you for playing!")
                logger.info("Game session ended.")
            break


if __name__ == "__main__":
    main()
