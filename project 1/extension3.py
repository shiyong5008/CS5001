age_of_oldboy = 37
guess = int(input("age you guess:"))
if guess > age_of_oldboy :
    print("am I that old, try again! 猜的太⼤了，往小⾥试试...")
elif guess < age_of_oldboy :
    print("thanks, but I am not that young, try again! 猜的太⼩了，往⼤里试试...")
else:
    print("congratulations, you are right! 恭喜你，猜对了...")