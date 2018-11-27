#from tic_tac_toe import sheet
sheet=[1,2,3,4,5,6,7,8,9]
def checkXO(input1,a):
	if (input1==1 or input1==2 or input1==3):
		if(input1==1):
			if(a[0][0]=='X' or a[0][0]=='*'):
				print("\t\tAlready done this move,SORRY")
				return 2
			else:
				return 1
		if(input1==2):
			if(a[0][1]=='X' or a[0][1]=='*'):
				print("\t\tAlready done this move,SORRY")
				return 2
			else:
				return 1
		if(input1==3):
			if(a[0][2]=='X' or a[0][2]=='*'):
				print("\t\tAlready done this move,SORRY")
				return 2
			else:
				return 1
	elif (input1==4 or input1==5 or input1==6):
		if(input1==4):
			if(a[1][0]=='X' or a[1][0]=='*'):
				print("\t\tAlready done this move,SORRY")
				return 2
			else:
				return 1
		if(input1==5):
			if(a[1][1]=='X' or a[1][1]=='*'):
				print("\t\tAlready done this move,SORRY")
				return 2
			else:
				return 1
		if(input1==6):
			if(a[1][2]=='X' or a[1][2]=='*'):
				print("\t\tAlready done this move,SORRY")
				return 2
			else:
				return 1

	elif (input1==7 or input1==8 or input1==9):
		if(input1==7):
			if(a[2][0]=='X' or a[2][0]=='*'):
				print("\t\tAlready done this move,SORRY")
				return 2
			else:
				return 1
		if(input1==8):
			if(a[2][1]=='X' or a[2][1]=='*'):
				print("\t\tAlready done this move,SORRY")
				return 2
			else:
				return 1
		if(input1==9):
			if(a[2][2]=='X' or a[2][2]=='*'):
				print("\t\tAlready done this move,SORRY")
				return 2
			else:
				return 1
	else:
		print("INVALID INPUT")


def player1(a,input1):

	if(input1==1 or input1==2 or input1==3):
		if(input1==1):
			a[0][0]='X'
			sheet[0]='X'
			print_sheet(a)
		elif(input1==2):
			a[0][1]='X'
			sheet[1]='X'
			print_sheet(a)
		elif(input1==3):
			a[0][2]='X'
			sheet[2]='X'
			print_sheet(a)
	elif(input1==4 or input1==5 or input1==6):
		if(input1==4):
			a[1][0]='X'
			sheet[3]='X'
			print_sheet(a)
		elif(input1==5):
			sheet[4]='X'
			a[1][1]='X'
			print_sheet(a)
		elif(input1==6):
			a[1][2]='X'
			sheet[5]='X'
			print_sheet(a)
	elif(input1==7 or input1==8 or input1==9):
		if(input1==7):
			a[2][0]='X'
			sheet[6]='X'
			print_sheet(a)
		elif(input1==8):
			a[2][1]='X'
			sheet[7]='X'
			print_sheet(a)
		elif(input1==9):
			a[2][2]='X'
			sheet[8]='X'
			print_sheet(a)


def player2(a,input1):

	if(input1==1 or input1==2 or input1==3):
		if(input1==1):
			a[0][0]='*'
			sheet[0]='*'
			print_sheet(a)
		elif(input1==2):
			a[0][1]='*'
			sheet[1]='*'
			print_sheet(a)
		elif(input1==3):
			a[0][2]='*'
			sheet[2]='*'
			print_sheet(a)
	elif(input1==4 or input1==5 or input1==6):
		if(input1==4):
			a[1][0]='*'
			sheet[3]='*'
			print_sheet(a)
		elif(input1==5):
			a[1][1]='*'
			sheet[4]='*'
			print_sheet(a)
		elif(input1==6):
			a[1][2]='*'
			sheet[5]='*'
			print_sheet(a)
	elif(input1==7 or input1==8 or input1==9):
		if(input1==7):
			a[2][0]='*'
			sheet[6]='*'
			print_sheet(a)
		elif(input1==8):
			a[2][1]='*'
			sheet[7]='*'
			print_sheet(a)
		elif(input1==9):
			a[2][2]='*'
			sheet[8]='*'
			print_sheet(a)


def print_sheet(a):
	for i in range(0,len(a)):
		for j in range(0,len(a[i])):
			print(a[i][j],end=' ')
		print()
		
