import  requests
import json
import sys
from Modules.Output import Output
class Result:
    __StudentResultUrl = "http://software.diu.edu.bd:8189/result"
    __StudentInfoUrl = 'http://software.diu.edu.bd:8189/result/studentInfo'
    def __init__(self,TogetherFileName='output'):
        self.AllSemesterList=self.SemesterList()
        self.__Output=Output()
        self.__TogetherFileName=TogetherFileName
    # semester SGPA requests
    def Sgpa(self,id:str,sem:str):
        payloads={
            'grecaptcha':'',
            'semesterId':sem,
            'studentId':id
        }
        response=requests.get(self.__StudentResultUrl,params=payloads)
        response=json.loads(response.content)
        if not response:
            return  [None]
        ls=[]
        for i in response:
            ls.append([i['customCourseId'],i['courseTitle'],i['totalCredit'],i['gradeLetter'],i['pointEquivalent'],i['cgpa']])
        return  ls
    # students info requests
    def StudentInfo(self,id):
        payloads = {
            'studentId': id
        }
        response=requests.get(self.__StudentInfoUrl,params=payloads)
        response=json.loads(response.content)
        return  [response['studentName'],response['studentId'],response['programName']]
    # finding all semester
    def SemesterList(self):
        response = requests.get('http://software.diu.edu.bd:8189/result/semesterList')
        dct=json.loads(response.text)
        ls={}
        for i in dct:
            # ls.append([i['semesterId'], i['semesterName']+' '+str(i['semesterYear'])])
            ls[i['semesterId']]= i['semesterName']+' '+str(i['semesterYear'])
        return  ls

# if semester is not set we will take all valid semester for this id
    def ValidSemesterList(self,id:str):
        ls=[]
        id=id.split('-')[0]
        for i in self.AllSemesterList:
            if i>=id:
                ls.append(i)
        ls.sort()
        return  ls
    # return semester name by semester id
    def SemesterName(self,semId):
        return self.AllSemesterList[semId]
# creating files according to the command
    def OutPutTheCommand(self,IdList:list , semlist:list , together:bool):
        flag= bool(semlist)
        if together:
            self.__Output.CreateFile(self.__TogetherFileName)
        fname=self.__TogetherFileName
        for i in IdList:
            # if not together then file name will be id
            if not together:
                fname=i
                self.__Output.CreateFile(fname)
            # if there is no semester initialized we will take all valid semester
            if not flag:
                semlist=self.ValidSemesterList(i)

            studentinfo=self.StudentInfo(i)
            if studentinfo[0]==None:
                self.__Output.inValidInfoCard(i,fname)
                semlist=[]
            else:
                self.__Output.userInfoCard(studentinfo,fname)

            credit,cg=0.0,0.0
            for sem in semlist:
                CurrentSemResult=self.Sgpa(i,sem)
                if CurrentSemResult[0]==None:
                    continue
                self.__Output.SemesterUi(self.SemesterName(sem),fname)

                # # print(sem)
                ThisSem=0
                for res in CurrentSemResult:
                    self.__Output.TableRowUi(res,fname)
                    if res[5]:
                        ThisSem += float(res[2])
                        cg += float(res[4]) * float(res[2])

                self.__Output.TableSgpaUi(ThisSem,CurrentSemResult[0][5],fname)
                credit+=ThisSem

            self.__Output.CgpaUi(credit,cg,fname)

            if not together:
                self.__Output.CloseFile(fname)
            print("SuccessFully Added",i,"Results")

        if together:
            self.__Output.CloseFile(self.__TogetherFileName)









	