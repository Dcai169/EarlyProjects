global usrIn
global rhFactor
global act
bloodDict={"a+":"a+", "b+":"b+", "ab+":"ab+", "o+":"o+", "a-":"a-", "b-":"b-", "ab-":"ab-", "o-":"o-"}
donStr=str("You can donate to people with type ")
recStr=str("You con receive from people with type ")
def donation(usrIn): 
	if len(usrIn)==2:
		bloodType=usrIn[0]
		rhFactor=usrIn[1]
	elif len(usrIn)==3:
		bloodType=usrIn[0:2]
		rhFactor=usrIn[2:3]
	if bloodType == 'o':
		print(donStr + rhFactor)	
	elif bloodType == 'ab':
		print(donStr + bloodType.upper() + rhFactor + " blood")
	elif bloodType == 'a':
		print(donStr + bloodType.upper() + rhFactor + " blood, and type AB" + rhFactor + " blood")
	elif bloodType == 'b':
		print(donStr + bloodType.upper() + rhFactor + " blood, and type AB" + rhFactor + " blood")
	else:
		print("Input Invaild; Try again")
def receiving(usrIn):
	if len(usrIn)==2:
		bloodType=usrIn[0]
		rhFactor=usrIn[1]
	elif len(usrIn)==3:
		bloodType=usrIn[0:2]
		rhFactor=usrIn[2:3]
	if bloodType == 'o':
		print(recStr + rhFactor)	
	elif bloodType == 'ab':
		print(recStr + rhFactor + " blood")
	elif bloodType == 'b':
		print(recStr + bloodType.upper() + rhFactor + " blood, and type O" + rhFactor)
	elif bloodType == 'a':
		print(recStr + bloodType.upper() + rhFactor + " blood, and type O" + rhFactor)
	else:
		print("Input Invaild; Try again")

act=str(input("Are you Donating or Receiving?: ").lower())
if act == 'donating':
	donation(input("What is your Blood Type?: ").lower())
elif act == 'receiving':
	receiving(input("What is your Blood Type?: ").lower())
else:
    print("Input Invaild; Try again")