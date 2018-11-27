

import back_game as game
from back_game import *
win_combination=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
def win(input1,a):
	for i in range(0,len(win_combination)):
		if input1 in win_combination[i]:
			flag=0
			count=0
			for j in range(0,len(win_combination[i])):
				key=win_combination[i][j]
				key=key-1
				if(sheet[key]!='X'):
					break
				else:
					flag=1
					count=count+1
					if(count==3):
						return flag
					

	
def win1(input1,a):
	for i in range(0,len(win_combination)):
		if input1 in win_combination[i]:
			flag=0
			count=0
			for j in range(0,len(win_combination[i])):
				key=win_combination[i][j]
				key=key-1
				if(sheet[key]!='*'):
					break
				else:
					flag=1
					count=count+1
					if(count==3):
						return flag


					
	
				
 
def checkAll(a):
	for i in range(0,len(a)):
		for j in range(0,len(a[i])):
			if(a[i][j]!='X') and (a[i][j]!='*'):
				return -1
				
	return 1
				

def start_game(a):
	while(1):

		print("\t\t Player 1")
		input1=int(input("Enter moves player 1:"))
		s=game.checkXO(input1,a)
		if(s==1):
			game.player1(a,input1)
		elif(s==2):
			print("\t\t Player 1")
			input1=int(input("Enter moves player 1:"))
			s=game.checkXO(input1,a)
			if(s==1):
				game.player1(a,input1)
		
		p=checkAll(a)
		if(p==1):
			print("\t\t****Game is tie****")
			return 0
		flag=win(input1,a)
		if(flag==1):
			print("\t\t Congratulation,Player 1,u r winner!!!")
			return 0
		print("\t\t Player 2")
		input1=int(input("Enter moves Player 2:"))
		s=game.checkXO(input1,a)
		if(s==1):
			game.player2(a,input1)
		elif(s==2):
			print("\t\t Player 2")
			input1=int(input("Enter moves player 2:"))
			s=game.checkXO(input1,a)
			if(s==1):
				game.player2(a,input1)

		flag=win1(input1,a)
		if(flag==1):
			print("\t\t Congratuation,Player 2,ur winner!!!")
			return 0

def print_sheet(a):
	for i in range(0,len(a)):
		for j in range(0,len(a[i])):
			print(a[i][j],end=' ')
		print()
		
c=[[1,2,3],[4,5,6],[7,8,9]]	
print("\t\t ****Game is Start****")
print_sheet(c)
start_game(c)
