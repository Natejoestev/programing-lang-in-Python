#shell

from syntax import SYNTAX
from error  import ERROR
from exception import EXEPTION, EXEPTION_MGER

from context import Context
from executor import Executor

## GLOBALS

global_CTX = Context(None)
expt_mger = EXEPTION_MGER(shellQuiter=quit)
execute = Executor(global_CTX, expt_mger)

## MAIN

def shell():
    while True:
        line = input("> ")
        if line.upper() == "EXIT":
            expt = EXEPTION("exit", "exit exeption was called", expt_mger)
            expt.Raise()
        
        line_ret = execute.run_line(line)

        if isinstance(line_ret, SYNTAX.types[0]): # got value
            print("VALUE:", line_ret.vlu.value, "OBJ:", line_ret.vlu)

        if isinstance(line_ret, ERROR): # got error
            print("ERROR:", line_ret)


        expt_mger.load_expts()

if __name__ == "__main__":
    shell()