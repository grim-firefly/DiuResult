import os.path


class Validate:
	def __init__(self):
		pass
	# checking if all elements of the list is digit or not
	def AllDigit(self,ls):
		for i in ls:
			if not i.isdigit():
				return False
		return True
	# validating if it's a possible ID
	def ValidateId(self, id:str):
		ls=id.strip('\n').split('-')
		if(len(ls)!=3 or not self.AllDigit(ls)):
			return False
		return True
	# Validating File is exists or not
	def ValidateFile(self,FileName:str):
		if os.path.isfile(FileName):
			return  True
		return  False
	# validating semester
	def ValidateSem(self,sem:str):
		if sem.isdigit() and len(sem)==3 and sem[2]>='1' and sem[2]<='3':
			return  True
		return  False
	# checking weather two id have same initial and same department
	def SameDepartMentWithInitial(self,First:str,Second:str):
		f=First.split('-')
		s=Second.split('-')
		if(f[0]==s[0] and f[1]==s[1]):
			return  True
		return  False