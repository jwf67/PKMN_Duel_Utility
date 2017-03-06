from decimal import *

#Global constants
DISK_SIZE = 96

#Generic Pokemon in Pokemon Duel
class Figure(object):
	#Define instance of a Figure
	def __init__(self, moves, status):
		self.moves = moves 
		self.status = status

#Moves in Pokemon Duel
class Move(object):
	#Define move characteristics
	#Type can be white, purple, yellow, or blue (red is white with power -1)
	def __init__(self, name, power, type, stars, size):
		self.name = name
		self.power = power
		self.type = type
		self.stars = stars #stars is 0 for all non-purple moves
		self.size = size

	def printStats(self):
		print self.name
		print self.power 
		print self.type
		print self.stars
		print self.size
	
#Does the move attack
def isAttacking(move):
	if move.type == "white" or move.type == "yellow":
		return True
	else:
		return False

#Does the move defend
def isDefending(move):
	if move.type == "purple":
		return True
	else:
		return False

#Are both moves attacking
def twoAttackingMoves(moveA, moveB):
	doesAAttack = isAttacking(moveA)
	doesBAttack = isAttacking(moveB)

	return doesAAttack and doesBAttack

#Are both moves defending
def twoDefendingMoves(moveA, moveB):
	doesADefend = isDefending(moveA)
	doesBDefend = isDefending(moveB)

	return doesADefend and doesBDefend

#Are the moves one white and one purple
def isOneAtkOneDef(moveA, moveB):
	if (moveA.type == "purple" and moveB.type == "white") or (moveB.type == "purple" and moveA.type == "white"):
		return True
	else:
		return False

#Takes 2 Moves and determines which move will win
def compareMoves(moveA, moveB):
	#print "Starts"
	if twoAttackingMoves(moveA, moveB):
		return compareAttacking(moveA, moveB)
	elif isOneAtkOneDef(moveA, moveB):
		return comparePurpleWhite(moveA, moveB)
	elif twoDefendingMoves(moveA, moveB):
		return comparePurpleMoves(moveA, moveB)
	else: #For now, just say there's a draw
		return 0


#Compare 2 attacking moves
def compareAttacking(moveA, moveB):
	if moveA.power > moveB.power:
		return 1
	elif moveA.power < moveB.power:
		return -1
	else:
		return 0

#Compare Purple and White Moves
#Currently Purple wins automatically v. white
def comparePurpleWhite(moveA, moveB):
	if moveA.type == "purple":
		return 1
	else:
		return -1

#Compare Yellow and Purple Moves
#Currently Yellow wins autmatically v. purple
def compareYellowPurple(moveA, moveB):
	if moveA.type == "yellow":
		return 1
	else:
		return -1

#Compare 2 Purple Moves
#Works off of star count
def comparePurpleMoves(moveA, moveB):
	if moveA.stars > moveB.stars:
		return 1
	elif moveA.stars < moveB.stars:
		return -1
	else:
		return 0

#Compare anything with a blue
def compareBlue(moveA, moveB):
	#For most purposes, blue just makes the battle neutral
	return 0

#Calculates the chance of both pokemon winning and drawing
def compareFigures(f1, f2):
	chanceOfF1Win = 0
	chanceOfF2Win = 0
	chanceOfDraw = 0
	for move1 in f1.moves:
		for move2 in f2.moves:
			if compareMoves(move1, move2) == 1:
				print "%s beats %s." % (move1.name, move2.name)
				chanceOfF1Win += percentOccurance(move1, move2)
			elif compareMoves(move1, move2) == -1:
				print "%s beats %s." % (move2.name, move1.name)
				chanceOfF2Win += percentOccurance(move1, move2)
			else:
				chanceOfDraw += percentOccurance(move1, move2)
				print "draw"
	print "Complete"
	print "%f" % (chanceOfF1Win)
	print "%f" % (chanceOfF2Win)
	print "%f" % (chanceOfDraw)

# Calculate the percent chance a move combination occurs when the two pokemon battle
def percentOccurance(moveA, moveB):
	print moveA.size
	print moveB.size
	print Decimal(moveA.size)/Decimal(DISK_SIZE)*Decimal(moveB.size)/Decimal(DISK_SIZE)*100
	return Decimal(moveA.size)/Decimal(DISK_SIZE)*Decimal(moveB.size)/Decimal(DISK_SIZE)*100

#Called to start the program, prompts the user to give information about the two combating pokemon
def receivePokemon():
	F = []
	movesA = []
	movesB = []
	move_count = 1
	
	#Look at 2 pokemon and receive all of their characteristics
	for figureNum in range(1, 3):
		move_count = input("How many moves does the pokemon #%d have?: " % (figureNum))
		for moveNum in range(1, move_count+1):
			move_name = raw_input("Enter move number %d's name for figure %d: " % (moveNum, figureNum))
			move_power = input("Enter the move's power: " )
			move_type = raw_input("Enter the move's type: ")
			move_stars = input("Enter the move's stars: ")
			move_size = input("Enter the move's size: ")
			
			if figureNum == 1:
				movesA.append(Move(move_name, move_power, move_type, move_stars, move_size))
			else:
				movesB.append(Move(move_name, move_power, move_type, move_stars, move_size))
		
		if checkIfSizeAccounted(movesA):
			if figureNum == 1:
				F.append(Figure(movesA, "healthy"))
			else:
				F.append(Figure(movesB, "healthy"))
			
	compareFigures(F[0], F[1])

#Check to make sure the person entered a total valid amount of moves
def checkIfSizeAccounted(moves):
	total_size = 0
	for move in moves:
		total_size += move.size
	
	if total_size != DISK_SIZE:
		print "Invalid Size! Check all size values!"
		return False
	else:
		return True
	
#Add More Tests
def test():	
	#Testing
	pm = []
	tackle = Move("tackle", 40, "white", 0, 32)
	thunder = Move("thunder", 100, "yellow", 0, 48)
	tailwhip = Move("tailwhip", 0, "purple", 2, 16)

	pm.append(tackle)
	pm.append(thunder)
	pm.append(tailwhip)

	Pikachu = Figure(pm, "healthy")

	cm = []
	scratch = Move("scratch", 20, "white", 0, 12)
	flamethrower = Move("flamethrower", 120, "white", 0, 64)
	miss = Move("miss", -1, "white", 0, 20)

	cm.append(scratch)
	cm.append(flamethrower)
	cm.append(miss)

	Charmander = Figure(cm, "healthy")

	compareFigures(Pikachu, Charmander)
	
hugeTest()
receivePokemon()
