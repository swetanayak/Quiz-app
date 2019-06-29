from data import data
# Imports the class data from the file data.py
import random

class Quiz:
	def __init__(self):
		#def defines a function
		self.ob = data() #Creates an object of the class data from the file data.py
		self.df = self.ob.getData() 


	def random(self):
		self.nums = list(range(len(self.df)))
		# self.num = np.arange(len(self.df)) + 1
		# np.random.shuffle(self.num)
		# for j in range(len(self.num)):
		# 	self.nums.append(self.num)
		random.shuffle(self.nums)

	def quizzie(self):
		self.score = 0
		self.name = input("Enter your name: ")
		print(self.name + ", Are you ready for a round of 10 questions?")
		t1 = input("Y/N? : ")
		if (t1 == 'y' or t1 == 'Y'):
			for (a,i) in zip(range(10), self.nums):
			#	for i in range(self.nums):
					print(self.df['QUESTIONS'][i:i+1].values)
					print("(1)" + self.df['OPTION 1'][i:i+1].values) 
					print("(2)" + self.df['OPTION 2'][i:i+1].values)
					print("(3)" + self.df['OPTION 3'][i:i+1].values)
					print("(4)" + self.df['OPTION 4'][i:i+1].values)
					t2 = float(input("Enter your option (0-4): "))

					if (t2 == self.df['ANSWER'][i:i+1].values):
					    self.score = self.score + 1
					    print("Congrats " + self.name + "! Your Answer is Correct. Score = " + str(self.score))
					else:
					    print("That was an incorrect answer. Score = " + str(self.score))

					t3 = input("Next question? (y/n): ")
					if(t3 == 'y' or t3 == 'Y'):
					    continue
					else:
					    break
			print("You've made it through! Your score is " + str(self.score))



ob2 = Quiz()
ob2.random()
ob2.quizzie()

	
	
