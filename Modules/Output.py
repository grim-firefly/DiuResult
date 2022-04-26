import os.path
import sys


class Output:
    def __init__(self,outputFolderName='Output'):
        self.CreateOutputFolder(outputFolderName)
        self.__header='''
        <!doctype html>
<html lang="en">

<head>
  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <!-- Bootstrap CSS -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
  
  <title>Academic Result | illus1on</title>
  
  <style>

  * {
	margin: 0;
	padding: 0;
	box-sizing: border-box;
}

.navbar {
	height: 60px;
	background: radial-gradient(#1fe4f5, #3fbafe);
}

.navbar-text {
	color: #FFF;
	text-align: center;
	font-weight: bolder;
	font-size: 20px;
	width: 100%;
}


.card {
	height: 110px;
	width: 550px;
	background: radial-gradient(#1fe4f5, #3fbafe);
	color: #FFF;
	text-align: center;
	font-weight: bolder;

}

.card-title {
	font-size: 20px;
	font-weight: bolder;
}

.card-text {
	font-size: 18px;
	font-weight: bold;
}

.semester {
	height: 30px;
	text-align: center;
	color: #FFF;
	font-weight: bold;
	font-size: 17px;
}

.cgpa {
	color: #FFF;
	height: 40px;
	line-height: 40px;
	font-weight: bold;
}
</style>


  
</head>

<body>
  <div class="row">
    <div class="navbar">
      <p class="navbar-text">DIU Academic Result </p>
    </div>
  </div>


  <div class="container">



        '''


        self.__footer='''

  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</body>
</html>

        '''
    # create output folder
    def CreateOutputFolder(self,FolderName):
        if os.path.isdir(FolderName):
            self.__outputFolder=FolderName+os.path.sep
        else:
            try:
                os.mkdir(FolderName)
                self.__outputFolder=FolderName+os.path.sep
                print('Output directory Created')
            except:
                print('Failed to create Output Directory')
                adsjfdfdsfsfsfsa = input("press close or anykey to exit")

                sys.exit(1)

    # ui for user name and some small details
    def userInfoCard(self,InfoList,FileName):
        UserCard='''
        <div class="row">
      <div class="cards mt-2 col d-flex justify-content-center">
        <div class="card">
          <h2 class="card-title mt-2">{0}</h2>
          <h4 class="card-text">{1}</h4>
          <h4 class="card-text">{2}</h4>
        </div>
      </div>
    </div>
        '''.format(InfoList[0],InfoList[1],InfoList[2])

        file = self.__outputFolder + FileName + '.html'
        try:
            with open(file,'a') as f:
                f.write(UserCard)
        except:
            print("Error File Writing")
            adsjfdfdsfsfsfsa = input("press close or anykey to exit")
            sys.exit(1)


    # adding semester UI to the file
    def SemesterUi(self,SemName,FileName):
        semester = '''
                    <div class="row">
              <div class="semester bg-info mt-2">
                <p class="semester-text">{0}</p>
              </div>
            </div>
            <div class="row">
      <table class="table table-striped">
        <thead>
          <tr class="table-info">
            <th scope="col" colspan="2">Course Code</th>
            <th scope="col" colspan="5">course Title</th>
            <th scope="col">Credit</th>
            <th scope="col">Grade</th>
            <th scope="col">Grade Point</th>
          </tr>
        </thead>
        <tbody> 
        
                '''.format(SemName)
        file = self.__outputFolder + FileName + '.html'
        try:
            with open(file, 'a') as f:
                f.write(semester)
        except:
            print("Error File Writing")
            adsjfdfdsfsfsfsa = input("press close or anykey to exit")
            sys.exit(1)

    # print if id is not valid
    def inValidInfoCard(self,id,FileName):
        UserCard='''
               <div class="row">
             <div class="cards mt-2 col d-flex justify-content-center">
               <div class="card">
                 <h2 class="card-title mt-2">{0}</h2>
                 <h4 class="card-text">{1}</h4>
                 <h4 class="card-text">{2}</h4>
               </div>
             </div>
           </div>
               '''.format("Invalid","invalid id"+ str(id), "Invalid")
        file = self.__outputFolder + FileName + '.html'
        try:
            with open(file, 'a') as f:
                f.write(UserCard)
        except:
            print("Error File Writing")
            adsjfdfdsfsfsfsa = input("press close or anykey to exit")
            sys.exit(1)
# creating file with header
    def CreateFile(self,FileName):
        file=self.__outputFolder+FileName+'.html'
        if not os.path.isfile(file):
            try:
                with open(file, 'w') as f:
                    f.write(self.__header)
            except:
                print("failed to create file")
                adsjfdfdsfsfsfsa = input("press close or anykey to exit")
                sys.exit(1)
        else:
            flag=input(" This File is Already Exist! Do You want to Replace it (Y/N) ?\n= ")
            if flag=='Y' or flag=='y':
                try:
                    with open(file, 'w') as f:
                        f.write(self.__header)
                except:
                    print("failed to create file")
                    adsjfdfdsfsfsfsa = input("press close or anykey to exit")
                    sys.exit(1)
            else:
                print("File Location is : ", os.getcwd() + os.path.sep + self.__outputFolder)
                adsjfdfdsfsfsfsa = input("press close or anykey to exit")
                sys.exit(1)



# adding footer to the table
    def CloseFile(self, FileName):
        file = self.__outputFolder + FileName + '.html'
        if not os.path.isfile(file):
            try:
                with open(file, 'a') as f:
                    f.write(self.__footer)
            except:
                print("failed to add Footer file")
                adsjfdfdsfsfsfsa = input("press close or anykey to exit")
                sys.exit(1)

    # output Result Row UI
    def TableRowUi(self,RowsValue,FileName):
        row='''
         <tr>
            <th scope="row" colspan="2">{0}</th>
            <td colspan="5">{1}</td>
            <td>{2}</td>
            <td>{3}</td>
            <td>{4}</td>
          </tr>
        
        '''.format(RowsValue[0],RowsValue[1],RowsValue[2],RowsValue[3],RowsValue[4])
        file = self.__outputFolder + FileName + '.html'
        try:
            with open(file, 'a') as f:
                f.write(row)
        except:
            print("Error Row Writing")
            adsjfdfdsfsfsfsa = input("press close or anykey to exit")
            sys.exit(1)
    # writing sgpa in the table
    def TableSgpaUi(self,Credit,Sgpa,FileName):
        sgpa='''
          <tr class="table-warning" >
            <th scope="row" colspan="7" style="text-align: center;">Semester Result</th>
            <th colspan="2">{0}</th>
            <th>{1}</th>
          </tr>
        
        </tbody>
      </table>
    </div>
        '''.format(Credit,Sgpa)
        file = self.__outputFolder + FileName + '.html'
        try:
            with open(file, 'a') as f:
                f.write(sgpa)
        except:
            print("Error Sgpa row Writing")
            adsjfdfdsfsfsfsa = input("press close or anykey to exit")
            sys.exit(1)


    # adding CGPA at the bottom
    def CgpaUi(self,credit,cgpa,FileName):
        try:
            cgpaValue = round(cgpa / credit,2)
        except:
            cgpaValue='Teaching Evaluation Pending'



        cgpa='''
          <div class="row">
      <div class="bg-danger cgpa">
        <div class="row">
          <div class="col-4" style="text-align: center;">In those Semester</div>
          <div class="col-3"style="text-align: center;">Credit Completed {0}</div>
          <div class="col-5" style="text-align: center;">CGPA {1}</div>
        </div>
      </div>
    </div>
        
        '''.format(credit,cgpaValue)
        file = self.__outputFolder + FileName + '.html'
        try:
            with open(file, 'a') as f:
                f.write(cgpa)
        except:
            print("Error in CGPA Writing")
            adsjfdfdsfsfsfsa = input("press close or anykey to exit")
            sys.exit(1)
