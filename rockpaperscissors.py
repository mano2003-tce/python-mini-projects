import random
#main input for proceding the game
gamers = input("do you want play player vs comp(pc) or comp vs comp (cc):  ")
# if it is for player vs computer
if gamers == "pc":
    status = int(input('enter the number of games you want to play: '))
    n = 1
    myp = 0
    cp = 0
    tp = 0
    while n <= status:   #for making true inputs
        game = ["r", "p", "s"]
        user = True
        while user not in game: #to avoid false inputs
            user = input('enter your choice: ')
            computer = random.choice(game)
            print("the computer: ", computer)
            if user == computer:
                print('its a tie!')
                print("----------------")
                tp += 1
            elif user == "r" and computer == "s" or user == "s" and computer == "p" or user == "p" and computer == "r" :
                print('you win!')
                print("----------------")
                myp += 1
            else:
                print('you lose')
                print("----------------")
            cp += 1
            n += 1
    print("RESULTS")
    print('your point: ', myp)
    print("comp point: ", cp)
    print("tie: ", tp)
    print("----------------")
elif gamers == "cc": #to play computer vs computer
    status = int(input('enter the number of games you want to play: '))
    i = 1
    comp1_point = 0
    comp2_point = 0
    comp_tie = 0
    for i in range(status):
        game = ["r", "p", "s"]
        computer1 = random.choice(game)
        computer2 = random.choice(game)
        print("computer1: ", computer1)
        print("computer2: ", computer2)
        if computer1 == computer2:
            print('its a tie!')
            print("----------------")
            comp_tie += 1
        elif computer1 == "r" and computer2 == "s" or computer1 == "s" and computer2 == "p" or computer1 == "p" and computer2 == "r":
            print('computer 1 wins!')
            print("----------------")
            comp1_point += 1
        else:
            print('computer 2 wins!')
            print("----------------")
            comp2_point += 1
        print("RESULTS")
        print('computer 1 point: ', comp1_point)
        print("computer 2 point: ", comp2_point)
        print("computer tie: ", comp_tie)
        print("---------------")
else:
    print("MANO hates these kind of inputs")
