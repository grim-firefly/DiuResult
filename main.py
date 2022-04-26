from Modules.Result import Result
from Modules.UserCommand import UserCommand
import sys

cmdInp=input('Enter Your Command(-h) for Help : ').strip().split()

Command=UserCommand(cmdInp)
MyResult=Result() #if you want to change together file name pass a string file name through result like  Result('illus1on')

MyResult.OutPutTheCommand(Command.IdList,Command.SemList,Command.together)
k=input("press close to exit")


