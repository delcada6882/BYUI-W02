The first class that will be needed is the game class will hold everything within it, from there we can start seeing what needs to be done. There should be a separate card class that will handle finding two random numbers between 1-13. They'd be saved into values called self.currentCard and self.nextCard. The next class will be user_input. It will take what the user says and then return it back using a function. From there I think having an outputs class would be helpful with calculating the resulting change or points and if the game is over or not. Then the "Play again? [y/n]" line will be in the main game class attached to a while loop.

Game():
    while(game is still being played):
        card = Card()
        print(the card is current card)
        use_inp = User_Input()
        answer = use_inp.get_input();
        output = Output()
        points = output.get_output(answer)
        game = use_inp.get_game_input()
        if (game is no):
            game isn't being played anymore, break the while loop
        elif (points equals 0):
            game isn't being played anymore, break the while loop
            print(You lost.)
            
    print(Thanks for playing my game.)


Card:
    current card = random
    next card = random

User_Input:
    get_input():
        answer = input(high or lower)
        return answer

    get_game_input():
        game = input(do you want to play again?)
        return game

Output:
    get_output(ans):
        if (ans is correct):
            points += 100
        elif (ans isn't correct):
            points -= 75
        else:
            print(this doesn't apply)
            points -= 75
    
    return points