import pandas as pd 

#pandas is a library which is used to extract data from a csv or any file. It creates a dataFrame out of the extracted data

class data:
	def __init__(self):
		self.df = pd.read_csv('questions.csv') #read_csv() [predifined fun] reads the file and passes a Dataframe into a given variable.
		# print(self.df.head(len(self.df))) #'Self' is an instance to the given class.display purpose
		# print(self.df['QUESTIONS'][103:104].values)

	def getData(self):
		return self.df

# ob1 = data()
