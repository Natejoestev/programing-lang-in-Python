# executor

from typing_extensions import Concatenate
from syntax import SYNTAX
from Type_values import decideOBJtype
from error  import ERROR


class Executor:
    def __init__(self, global_CTX, expt_mger):
        self.global_CTX = global_CTX
        self.expt_mger = expt_mger

        self.current_CTX = self.global_CTX
    
    def run_line(self, line):
        if line.startswith(SYNTAX.line_starters[0]) or line == SYNTAX.line_starters[1]:
            return None
        
        elif line.startswith(SYNTAX.line_starters[2]): # VAR
            keywords = line.split(" ")
            if keywords[2] == SYNTAX.keywords[1][0]: # set
                item = " ".join([*keywords, "_"][3:-1])
                value_obj = decideOBJtype.getType(item)#f"{keywords[-2]} {keywords[-1]}")
                if isinstance(value_obj, ERROR):
                    return value_obj
                else:
                    value = value_obj.value
                    print(f"Var: {keywords[1]} = {value_obj}:{value}") # DEBUGOUT the newvarubal
                    self.current_CTX.setValue(keywords[1], SYNTAX.types[0](value_obj))

            return None
        else: #for now just return the VALUE obj for a value of the STR they input using a CONTEXT
            return self.current_CTX.getValue(line) # Going to change into other part with Shell only execution

    def run_lines(self, code):
        lines = code.split("\n")
        for line in lines:
            self.run_line(line)