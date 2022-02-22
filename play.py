


x = str(input())

if x not in ["paper", "scissors" , "rock"]:
	print("""Enter one of these words please:
		rock
		paper
		scissors""")
	exit()

import random


enemy_list= ["👽" , "🐉" , "🦀" , "🐸" , "🐭"]

enemy = random.choice(enemy_list)

print("			You VS {m}\n".format(m=enemy))

list = ["rock", "paper", "scissors"]

y = random.choice(list)

print("You : {a} \n{b} : {c}\n".format(a=x, b=enemy, c = y))


if x==y :
	print("	😬	It's a draw")
elif (x=="paper" and y =="rock") or (x=="rock" and y == "scissors" ) or (x=="scissors" and y=="paper" ):
	print("	🥳		You won")
elif (x=="paper" and y == "scissors") or (x=="rock" and y == "paper") or (x=="scissors" and y=="rock"):
	print("	😅		You lost")
	






