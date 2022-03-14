print("""****************************************************************************************************
Chess is without a doubt one of the most fascinating and popular games in history.
Do you know how many moves are possible in chess, or which is the longest chess game?

If you fancy testing your knowledge while learning cool facts about chess, then take the chess quiz!
****************************************************************************************************\n""")

playing = input("Do you want to play? Yes|No\n")

if playing.lower() != "yes":
    quit()

print("\nOkay! Let's play :)\n")
score = 0

answer = input("""How many squares does a chessboard have?
A) 65
B) 32
C) 64
D) 99\n""")
if answer.upper() == "C":
    print('Correct!')
    score += 1
else:
    print('Incorrect! There are eight horizontals (called "files) and eight verticals (called "ranks"), totalling 64 squares.')

answer = input("""\nWhat is it called when a player can't defend an attack against their king?
A) Check
B) Chess
C) Checkchess
D) Checkmate\n""")
if answer.upper() == "D":
    print('Correct!')
    score += 1
else:
    print('Incorrect! Checkmating your opponent is the most important and crucial goal in the game of chess.')

answer = input("""\nWhere did chess originate?
A) India
B) Russia
C) Italy
D) France\n""")
if answer.upper() == "A":
    print('Correct!')
    score += 1
else:
    print('Incorrect! Historical evidence suggests that chess originated in India.')

answer = input("""\nWhat determines which player starts first in a chess game?
A) Coin flip
B) Whoever comes first to the board
C) The player with the black pieces always goes first
D) The player with the white pieces always goes first\n""")
if answer.upper() == "D":
    print('Correct!')
    score += 1.5
else:
    print("Incorrect! The player with the white pieces always goes first")

answer = input("""\nWho were the opponents in the famous Evergreen Game?
A) Adolf Anderssen vs. Jean Dufresne
B) Paul Morphy vs. Howard Staunton
C) Wilhelm Steinitz vs. Emanuel Lasker
D) Jose Raul Capablanca vs. Alexander Alekhine\n""")
if answer.upper() == "D":
    print('Correct!')
    score += 3
else:
    print('Incorrect! The evergreen game is a famous chess game played by Jean Dufresne and Adolf Anderssen in 1852. Anderssen won it by sacrificing multiple pieces and delivering a beautiful checkmate.')

answer = input("""\nWhich is greatest in number?
A) All atoms in the universe
B) Possible games of chess
C) Stars in the Milky Way
D) People on the planet\n""")
if answer.upper() == "B":
    print('Correct!')
    score += 3
else:
    print("Incorrect! The virtually infinite number of possible chess games is one of the reasons why chess is so interesting and it's still popular today.")

answer = input("""\nIf you put one grain of wheat on the first square of the chessboard, then two on the second, four on the third, eight on the fourth, and so on, how many grains of wheat do you need to put on the last 64th square?
A) 999 999
B) 1 000 000 001
C) 64 000 000 000
D) 9 223 372 036 864 775 808 (approx. 9.22x10^18)\n""")
if answer.upper() == "D":
    print('Correct!')
    score += 3
else:
    print("Incorrect! D is the correct answer, and This is how vast and deep the game of chess is! There are so many combinations of possible moves, which make the game so interesting and unpredictable.")

print("You got " + str(score) + " questions correct!")
print("You got " + str("{:.2f}".format((score / 7) * 100)) + "% of answers correct.")
#https://www.chess.com/terms/chess-quiz