import random

class Game():
    def game_start(self): #this is the game function. It runs everything.
        points = 300
        game = "y"
        print("Your starting score is 300. If you answer right then it will go up by 100, if you answer wrong then it'll go down by 75.") #this is all just establishing a few things before we get into the game loop.
        while(game == "y"): #as long as you say yes to playing agin you will go through the loop.
            card = Card()
            win_condition = card.find_card()
            curr_card = card.current_card
            next_card = card.next_card
            print(f"\nThe card is: {curr_card}") #just grabbing the find_card function and initializing the win_condition
            use_inp = User_Input()
            answer = use_inp.get_input() #init the user_input and getting an answer
            if(answer == "h"):
                answer = 0
            elif(answer == "l"):
                answer = 1 #the code above me just converts it to a format similar to a bool but with a third value in case you didn't put in a number.
            else:
                answer = 5 #if you put in a value that isnt h or l, then you get this.
            output = Output()
            print(f"The next card is {next_card}") #shows the next card
            points = output.get_output(answer, win_condition, points) #gets whether you won or not
            print(f"Your score is: {points}") #shows your score
            if (points < 0): #if you have no more points then the game is over
                print("You're out of points, the game is over. You lost.")
                break
            game = use_inp.get_game_input() #grabbing the input of if you want to play again
            if (game == "n"): #if you don't then the game ends
                print("Thanks for playing my game.")
                break
            

class Card:
    def __init__(self): #I needed to init it as 0 so it would reset every loop.
        self.current_card = 0
        self.next_card = 0
    
    def find_card(self):
        self.current_card = random.randint(1,13) #just grabbing a random value.
        self.next_card = random.randint(1,13)
        if self.current_card > self.next_card: #converting it into the same values as win condition for easier to read code later.
            c_is_higher = 1
        elif self.current_card < self.next_card:
            c_is_higher = 0
        else:
            c_is_higher = 2
        
        return c_is_higher #returning the win_condition

class User_Input:
    def get_input(self): #asking if the card is higher or lower and returning the answer
        answer = input("Higher or lower? [h/l] ")
        return answer

    def get_game_input(self): #asking if they want to play again and returning the answer
        game = input("do you want to play again? [y/n] " )
        return game

class Output:
    def get_output(self, ans, what_ans_must_be, points):
        if (what_ans_must_be == 2): #if the curr_card and next_card is the same then it's unfair.
            print("That's unfair, they're the same value. I'll just give you the win.")
            points += 100
        elif (ans == what_ans_must_be): #they got it right
            print("Nice Job.")
            points += 100
        elif (ans == 5): #they didn't put in the correct type of answer
            print("This doesn't apply. So it's wrong. -75 points for you.")
            points -= 75
        else: #they got it wrong
            print("Try harder")
            points -= 75

        return points #return their ending points

start = Game()
start.game_start() #game starts