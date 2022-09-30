import random

class Game():
    def game_start(self):
        points = 300
        game = "y"
        print("Your starting score is 300. If you answer right then it will go up by 100, if you answer wrong then it'll go down by 75.")
        while(game == "y"):
            card = Card()
            win_condition = card.find_card()
            curr_card = card.current_card
            next_card = card.next_card
            print(f"\nThe card is: {curr_card}")
            use_inp = User_Input()
            answer = use_inp.get_input()
            if(answer == "h"):
                answer = 0
            elif(answer == "l"):
                answer = 1
            else:
                answer = 5
            output = Output()
            print(f"The next card is {next_card}")
            points = output.get_output(answer, win_condition, points)
            print(f"Your score is: {points}")
            if (points < 0):
                print("You're out of points, the game is over. You lost.")
                break
            game = use_inp.get_game_input()
            if (game == "n"):
                print("Thanks for playing my game.")
                break
            

class Card:
    def __init__(self):
        self.current_card = 0
        self.next_card = 0
    
    def find_card(self):
        self.current_card = random.randint(1,13)
        self.next_card = random.randint(1,13)
        if self.current_card > self.next_card:
            c_is_higher = 1
        elif self.current_card < self.next_card:
            c_is_higher = 0
        else:
            c_is_higher = 2
        
        return c_is_higher

class User_Input:
    def get_input(self):
        answer = input("Higher or lower? [h/l] ")
        return answer

    def get_game_input(self):
        game = input("do you want to play again? [y/n] " )
        return game

class Output:
    def get_output(self, ans, what_ans_must_be, points):
        if (what_ans_must_be == 2):
            print("That's unfair, they're the same value. I'll just give you the win.")
            points += 100
        elif (ans == what_ans_must_be):
            print("Nice Job.")
            points += 100
        elif (ans != what_ans_must_be):
            print("Try harder")
            points -= 75
        else:
            print("This doesn't apply. So it's wrong. -75 points for you.")
            points -= 75

        return points

start = Game()
start.game_start()