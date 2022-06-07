#<import>
from random import randint
import sys
import os
from time import sleep
#</import>

#<variables>
score1 = 0
score2 = 0
round_no = 0
endgame_anim = ["             @\n             @\n             @\n\n        The Endgame\n\n             @\n             @\n             @", "                       @\n                     @\n                   @\n\n        The Endgame\n\n       @\n     @\n   @", "\n\n\n\n@  @  @ The Endgame @  @  @", "   @\n     @\n       @\n\n        The Endgame\n\n                   @\n                      @\n                         @"]
dicey_anim = ["\\\\\\\\//////DICEY\\\\\\\\\\\\////  ", "\\\\////////DICEY\\\\\\\\\\\\\\\\//  ", "//////////DICEY\\\\\\\\\\\\\\\\\\\\  ", "////////||DICEY||\\\\\\\\\\\\\\\\    ", "//////||||DICEY||||\\\\\\\\\\\\      ", "////||||||DICEY||||||\\\\\\\\        ", "//||||||||DICEY||||||||\\\\          ", "||||||||||DICEY||||||||||            ", "||||||||\\\\DICEY//||||||||          ", "||||||\\\\\\\\DICEY////||||||        ", "||||\\\\\\\\\\\\DICEY//////||||      ", "||\\\\\\\\\\\\\\\\DICEY////////||    ", "\\\\\\\\\\\\\\\\\\\\DICEY//////////  ", "\\\\\\\\\\\\\\\\//DICEY\\////////    ", "\\\\\\\\\\\\////DICEY\\\\//////      "]
round_nums = ["\n╭━━━╮╱╱╱╱╱╱╱╱╱╱╭╮╱╭╮\n┃╭━╮┃╱╱╱╱╱╱╱╱╱╱┃┃╭╯┃\n┃╰━╯┣━━┳╮╭┳━╮╭━╯┃╰╮┃\n┃╭╮╭┫╭╮┃┃┃┃╭╮┫╭╮┃╱┃┃\n┃┃┃╰┫╰╯┃╰╯┃┃┃┃╰╯┃╭╯╰╮\n╰╯╰━┻━━┻━━┻╯╰┻━━╯╰━━╯\n\n", "\n╭━━━╮╱╱╱╱╱╱╱╱╱╱╭╮╭━━━╮\n┃╭━╮┃╱╱╱╱╱╱╱╱╱╱┃┃┃╭━╮┃\n┃╰━╯┣━━┳╮╭┳━╮╭━╯┃╰╯╭╯┃\n┃╭╮╭┫╭╮┃┃┃┃╭╮┫╭╮┃╭━╯╭╯\n┃┃┃╰┫╰╯┃╰╯┃┃┃┃╰╯┃┃┃╰━╮\n╰╯╰━┻━━┻━━┻╯╰┻━━╯╰━━━╯\n\n", "\n╭━━━╮╱╱╱╱╱╱╱╱╱╱╭╮╭━━━╮\n┃╭━╮┃╱╱╱╱╱╱╱╱╱╱┃┃┃╭━╮┃\n┃╰━╯┣━━┳╮╭┳━╮╭━╯┃╰╯╭╯┃\n┃╭╮╭┫╭╮┃┃┃┃╭╮┫╭╮┃╭╮╰╮┃\n┃┃┃╰┫╰╯┃╰╯┃┃┃┃╰╯┃┃╰━╯┃\n╰╯╰━┻━━┻━━┻╯╰┻━━╯╰━━━╯\n\n", "\n╭━━━╮╱╱╱╱╱╱╱╱╱╱╭╮╭╮╱╭╮\n┃╭━╮┃╱╱╱╱╱╱╱╱╱╱┃┃┃┃╱┃┃\n┃╰━╯┣━━┳╮╭┳━╮╭━╯┃┃╰━╯┃\n┃╭╮╭┫╭╮┃┃┃┃╭╮┫╭╮┃╰━━╮┃\n┃┃┃╰┫╰╯┃╰╯┃┃┃┃╰╯┃╱╱╱┃┃\n╰╯╰━┻━━┻━━┻╯╰┻━━╯╱╱╱╰╯\n\n", "\n╭━━━╮╱╱╱╱╱╱╱╱╱╱╭╮╭━━━╮\n┃╭━╮┃╱╱╱╱╱╱╱╱╱╱┃┃┃╭━━╯\n┃╰━╯┣━━┳╮╭┳━╮╭━╯┃┃╰━━╮\n┃╭╮╭┫╭╮┃┃┃┃╭╮┫╭╮┃╰━━╮┃\n┃┃┃╰┫╰╯┃╰╯┃┃┃┃╰╯┃╭━━╯┃\n╰╯╰━┻━━┻━━┻╯╰┻━━╯╰━━━╯\n\n"]
GG = "\n░██████╗░░██████╗░\n██╔════╝░██╔════╝░\n██║░░██╗░██║░░██╗░\n██║░░╚██╗██║░░╚██╗\n╚██████╔╝╚██████╔╝\n░╚═════╝░░╚═════╝░\n"
#</variables>

#<fuctions>
def fancy(text): #Makes the last charachter of a string flash
    for i in range(5):
        print(text[:-1] + " ", end="\r")
        sleep(0.2)
        print(text, end="\r")
        sleep(0.2)
def clear(): #Clears the whole console, and first determines the OS to be able to do so
    if os.name in ('nt', 'dos'):
        os.system("cls")
    else:
        os.system("clear")
def login(p, taken): #This validates the user by keeping them locked in a while loop until they give correct info
    check = False
    user = input("Player " + p + " username: ")
    pas = input("Player " + p + " password: ")
    for name in data:
        if name[0] == user and name[0] != taken and name[1] == pas:
            check = True
    while check == False:
        print("username and/or password not found")
        user = input("Player " + p + " username: ")
        pas = input("Player " + p + " password: ")
        for name in data:
            if name[0] == user and name[0] != taken and name[1] == pas:
                check = True
        if user == taken: #The "taken" variable is the username of the last login, which is empty the first time this function is called, but the second time (when logging in player 2) it ensures the two players are different users
            print("Player 2 must choose a different account from " + str(user1))
    return user
def fanc(text): #This animates a text as if it's being typed
    for char in text:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
def roll1(): #Animation for rolling one die
    while True:
        print(str(randint(1, 6)), end="\r")
        sleep(0.07)
        if randint(1, 50) == 1:
            break
    num = randint(1, 6)
    return(num)
def roll2(): #rolls 2 dice
    while True:
        print(str(randint(1, 6)) + " " + str(randint(1, 6)), end="\r")
        sleep(0.07)
        if randint(1, 35) == 1:
            break
    nums = [randint(1, 6), randint(1, 6)]
    print(nums[0], nums[1])
    sleep(0.5)
    print("You rolled " + str(nums[0]) + " + " + str(nums[1]) + " = " + str(nums[0]+nums[1]))
    return nums
def double(a, b, score): #checks if you rolled a double, and acts accordingly
    if a == b:
        input("You also rolled a double\nPress ENTER to Roll Again")
        num = roll1()
        print(num)
        sleep(0.5)
        print("You rolled " + str(num) + "\n" + str(score) + " + " + str(num) + " = " + str(score+num) + " new points")
        return num
    else:
        return 0
def even_odd(new): #checks if your throw is even or odd, and returns change value
    if new%2 == 0:
        print("Even\n+10 points\n" + str(new) + " + 10 = " + str(new+10) + " new points")
        return 10
    else:
        print("Odd\n-5 points\n" + str(new) + " - 5 = " + str(new-5) + " new points")
        return -5
def go(user, score): #This calls all the necessary functions and makes the updates for a player in a round
    input(str(user) + ", press ENTER to Roll") #This input is how the program waits for the user to press ENTER.
    dice = roll2()
    score = dice[0] + dice[1]
    score += even_odd(score)
    score += double(dice[0], dice[1], score)
    print("\n")
    return score
def endgame(): #This is the potentially eternal ordeal in which players who tie will keep throwing one die until one of them wins
    clear()
    fancy("Welcome to:")
    clear()
    for i in range(18):
        for m in endgame_anim: #special animation to give this event a proper intro
            print(m)
            sleep(0.05)
            clear()
    while True: #                                                      \
        input("\n" + str(user1) + ", press ENTER to Roll...O_O") #     |
        rolled1 = roll1() #                                            |
        print(str(rolled1) + "\n") #                                   |
        input(str(user2) + ", press ENTER to Roll...O_O") #            |
        rolled2 = roll1() #                                            |
        print(str(rolled2) + "\n") #                                   |-- This is the actual loop until someone rolls higher
        if rolled1 > rolled2: #                                        |
            winner = [str(user1), str(score1)] #                       |
            break #                                                    |
        elif rolled1 < rolled2: #                                      |
            winner = [str(user2), str(score1)] #                       |
            break #                                                    |
    return winner #                                                    /
#</functions>

#<Intro>
fancy("You are playing:")
dicey = "DICEY"
for i in range(6): #                                                    \
    print("           " + dicey[:i] + "       ", end="\r") #            |
    sleep(0.2) #                                                        |-- This is a silly animation
    print("                                             ", end="\r") #  |
    sleep(0.2) #                                                        /
for i in range(6): #             \
    for m in dicey_anim: #       |-- A horrendous animation
        print(m, end="\r") #     |
        sleep(0.04) #            /
print("Aight, I'm done...                                          \n")
sleep(1)
print("Let's begin\n")
sleep(1)
clear()
print("    DICEY\nby Uygar Arabul\n\n")
sleep(2)
#</Intro>

#<login>
file = open("Code/Players.txt", "r") #  \
data = file.read() #               |-- Fetches user data from external file
file.close() #                     /
data = data.split("\n")
for line in range(len(data)): #Prepares list used in login function
    data[line] = data[line].split(",")
user1 = login("1", 0)
print("\n")
user2 = login("2", user1)
print("\n")
sleep(0.5)
#</login>

#<game>
fanc(str(user1)+ "'s score: 0\n" + str(user2) + "'s score: 0\n")
sleep(0.5)
for round_no in range(5): #This loop evaluates and records all changes at the end of a round (after calling one, 5 times)
    fanc(round_nums[round_no])
    changes = [go(user1, score1), go(user2, score2)]
    def update(score, i):
        if -changes[i] > score:
            return 0
        else:
            return changes[i]
    old1 = score1
    old2 = score2
    score1 += update(score1, 0)
    score2 += update(score2, 1)
    print(str(user1) + "'s score: " + str(old1) + " + " + str(changes[0]) + " = " + str(score1) + "\n" + str(user2) + "'s score: " + str(old2) + " + " + str(changes[1]) + " = " + str(score2) + "\n")
    round_no += 1
#</game>

#<aftermath>
print("\n\n")
sleep(1)
fancy("尺🝗丂ㄩ㇄〸丂:") #animates the heading
sleep(0.5)
fanc("\n" + str(user1) + "'s score: " + str(score1) + "\n" + str(user2) + "'s score: " + str(score2))
sleep(0.5)                  #  ^^  prints results with the typing effect ^^
if score1 > score2:
    winner = [user1, str(score1)]
    print("\n\n" + str(user1) + " Wins. What a try hard...")
elif score1 < score2:         #  ^^ Literal favouritism ^^
    winner = [user2, str(score2)]#      \/      \/
    print("\n\n" + str(user2) + " Wins! Congratulations!")
else: #If neither score is greater, hence they tie...
    sleep(1)
    print("\n\nYou two... How?")
    sleep(1.5)
    print("Your fortunes are one and the same...")
    sleep(2)
    print("This can only mean one thing...")
    sleep(2)
    winner = endgame() #begins the endgame and stores the returned winner and their score in a list
    print("\n" + winner[0] + " wins!")
#</aftermath>

#<report>
file = open("Code/Winners.txt", "r") #Fetches the winners' data from the external file
data = file.read()
file.close()
data = data.split("\n")
for i in range(len(data)):
    data[i] = data[i].split(",")
wins = []
for person in data: #          \
    for item in person: #         |-- This creates a list with all of the winners' data
        wins.append(item) #  /
for i in range(int(len(wins)/2)):
    if wins[i*2] == winner[0]:
        if wins[i*2+1] < winner[1]:
            if wins[i*2+1] < winner[1]:
                wins.pop(i*2)
                wins.pop(i*2)
                wins.append(winner[0])
                wins.append(winner[1])
                break
    elif i == (int(len(wins)/2)-1):
        wins.append(winner[0])
        wins.append(winner[1])
        break
changed = True
while changed == True:
    changed = False                                                     #This breaks the condition set above, and must be corrected for the while loop to go again. This is how I know when a whole pass has happened without any changes.
    for i in range(int((len(wins)/2)-1)):                                    #This sorts the winners' list using bubble sort
        if int(wins[2*(i+1)-1]) < int(wins[2*(i+1)+1]):               #If score of the current score is less than the next (two items ahead as this list includes names and scores)
            changed = True                                             #Adjustments are about to be made so the while loop's condition is set to go
            current = [wins[2*(i+1)-2], wins[2*(i+1)-1]]                      #Stores the current username and score ina list
            wins[2*(i+1)-2] = wins[2*(i+1)]                       #Replaces the current username with the next
            wins[2*(i+1)-1] = wins[2*(i+1)+1]                       #Replaces the current score with the next
            wins[2*(i+1)] = current[0]                           #Appends the current username to the next slot
            wins[2*(i+1)+1] = current[1]                         #Appends the current score to the next slot
print("\nTop five leaderboard:")
for i in range(5):
    print(wins[i*2] + ", " + wins[i*2+1])
file = open("Code/Winners.txt", "w")
file.write(wins[0] + "," + wins[1])
for i in range(int(len(wins)/2)-1):
    file.write("\n" + wins[(i+1)*2] + "," + wins[(i+1)*2+1])
file.close()
#</report>

fanc(GG) #Final animation