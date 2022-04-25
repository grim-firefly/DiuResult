from Modules.Result import Result
from Modules.UserCommand import UserCommand
import sys
Command=UserCommand(sys.argv[1:])
MyResult=Result() #if you want to change together file name pass a string file name through result like  Result('illus1on')

MyResult.OutPutTheCommand(Command.IdList,Command.SemList,Command.together)



