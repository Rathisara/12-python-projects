import random

def play():
    user_score = 0
    computer_score = 0
    
    for round_num in range(1, 4):
        print(f"\n--- Round {round_num} ---")
        user = input("What's your choice? 'r' for rock , 'p' for paper , 's' for scissors\n")
        computer = random.choice(['r','p','s'])
        
        if user == computer:
            print('Tie!')
        elif is_win(user, computer):
            print('You won this round!')
            user_score += 1
        else:
            print('Computer won this round!')
            computer_score += 1
        
        print(f"Score - You: {user_score}, Computer: {computer_score}")
    
    print("\n--- Final Results ---")
    if user_score > computer_score:
        print(f"You won the game! Final score: {user_score} - {computer_score}")
    elif computer_score > user_score:
        print(f"Computer won the game! Final score: {computer_score} - {user_score}")
    else:
        print(f"It's a tie! Final score: {user_score} - {computer_score}")
    
def is_win(player, opponent):
    #return true if player wins
    #r>s, s>p, p>r
    if (player=='r' and opponent=='s') or (player=='s' and opponent=='p') or (player=='p' and opponent=='r'):
        return True
    
play()