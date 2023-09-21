import random

class Riddle:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

riddles = [
    Riddle("I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?", "an echo"),
    Riddle("I am taken from a mine, and shut up in a wooden case, from which I am never released, and yet I am used by almost every person. What am I?", "pencil lead"),
    Riddle("What has keys but can't open locks?", "a piano"),
    Riddle("The more you take, the more you leave behind. What am I?", "footsteps"),
    Riddle("I'm tall when I'm young and short when I'm old. What am I?", "a candle"),
    Riddle("I'm not alive, but I can grow. I don't have lungs, but I need air. What am I?", "a fire"),
]

def play_riddle_game():
    print("Welcome to ProjectMystic - Riddle Challenge!")
    print("Can you solve these mysterious riddles?")

    score = 0

    random.shuffle(riddles)

    for riddle in riddles:
        print("\nRiddle:")
        print(riddle.question)
        guess = input("Your answer: ").strip().lower()

        if guess == riddle.answer:
            print("Correct!")
            score += 1
        else:
            print(f"Sorry, the correct answer is: {riddle.answer}")

    print(f"\nYou answered {score} out of {len(riddles)} riddles correctly!")

if __name__ == "__main__":
    play_riddle_game()
