import sys
from Modules.Validate import Validate
import  requests
import  json

class UserCommand:
	IdList = []
	SemList = []
	together = False
	def __init__(self, AllCmd=['-h']):
		self.__AllCmd = AllCmd
		self.__Validator=Validate()
		if not self.__AllCmd:
			self.CheckUse()
		self.CommandCreator()

	# # id list getter
	# def GetIdList(self):
	# 	return  self.IdList
	# # sem list getter
	# def GetSemList(self):
	# 	return  self.SemList
	# def GetTogetherValue(self):
	# 	return  self.together

	# if there is nothing in command
	def CheckUse(self):
		print('Usage: python main.py -h')
		adsjfdfdsfsfsfsa = input("press close or anykey to exit")
		sys.exit(1)
# add all id from st to en
	def AddRange(self,st:str,en:str):
		if(self.__Validator.ValidateId(st) and self.__Validator.ValidateId(en) and self.__Validator.SameDepartMentWithInitial(st,en)):
			s=st.split('-')
			e=en.split('-')
			initial=s[0]+'-'+s[1]+'-'
			for i in range(int(s[2]),int(e[2]) + 1):
				self.IdList.append(initial+str(i))
		else:
			print('Bad Range')


# Add Id From File
	def AddFromFile(self,filename:str):
		with open(filename, "r") as f:
				for line in f:
					if line.startswith('-range'):
						ls=line.split()
						if(len(ls)==3):
							self.AddRange(ls[1], ls[2])
						else:
							print("Bad Range")
					elif self.__Validator.ValidateId(line):
						self.IdList.append(line.strip('\n'))
					else:
						print(line , "is not matched with Default Documentation")
	def Documentation(self):
		print("-h : view the usuage section ")
		print('-id : pass students id like -id 191-35-407 191-35-408 191-35-408.... ')
		print('      You can pass multiple id like this')
		print('-range :  you can give a range of id as input.use like : -range 191-35-407 191-35-412 [here out script will take all id  from 407 to 412 including 407 and 412')
		print('          you can give multiple range input')
		print('          -range 191-35-395 191-35-401 191-35-405 191-35-418 [ here script will take id from 395 to 401 and from 405 to 418]')
		print("-sem: initilize which semester result you want.. if you don't have any specific semester. The default is all semesters ")
		print('     use like : -sem 191 192 193 [ here 19 is year last 2 digit and 1 means spring 2 means summer and 3 means fall')
		print('     example : spring 2020 -> 201 , summer 2020 -> 202 , fall 2020 ->203')
		print('-f : this flag is use to give id input from file.use like -f ids.txt ')
		print('      You can store id in file in 2 ways Like :')
		print('    191-35-407')
		print('    191-35-441')
		print('    191-35-405')
		print('    -range 191-35-407 191-35-441  [remember you can give multiple range here. if you want multple range use another line with -range')
		print('    -range 191-35-395 191-35-401')
		print("-together: this is a indipendent flag. Its use to determine if you want all result in a single file or different")
		print('				if you use this , all result will be shown in a single file')
		print('N.B: Individual result will be use their id.html as file name and Together result will use output.html as the file name')
		print('You can change together file name by passing file name as string in the Result("filename") in main.py .')
		adsjfdfdsfsfsfsa = input("press close or anykey to exit")
		sys.exit(1)




	# Readline commandline arguments and create command according that
	def CommandCreator(self):
		ls = self.__AllCmd
		i = 0
		while (i < len(ls)):
			if ls[i] == '-id':
				while (i + 1 < len(ls) and self.__Validator.ValidateId(id=ls[i + 1])):
					self.IdList.append(ls[i + 1])
					i += 1
			elif ls[i]=='-f':
				while(i+1<len(ls) and self.__Validator.ValidateFile(ls[i+1])):
					self.AddFromFile(ls[i+1])
					i+=1
			elif ls[i]=='-range':
				while(i+1<len(ls) and i+2<len(ls) and self.__Validator.ValidateId(ls[i+1]) and self.__Validator.ValidateId(ls[i+2])):
					self.AddRange(ls[i+1],ls[i+2])
					i+=2
			elif ls[i]=='-sem':
				while(i+1<len(ls) and self.__Validator.ValidateSem(ls[i+1])):
					self.SemList.append(ls[i+1])
					i+=1
			elif ls[i]=='-together':
				self.together=True
			elif ls[i]=='-h':
				self.Documentation()

			i += 1
		if not self.IdList:
			self.CheckUse()



		
		    

		
