from syntax import SYNTAX
from error  import ERROR

def getType(section):
    str_end = SYNTAX.keywords[2]
    int_end = (*SYNTAX.number, "")[0:-1]
    if section.startswith(str_end) and section.endswith(str_end):
        obj = SYNTAX.types[1][2](section.replace(str_end[0], "").replace(str_end[1], ""))
        return obj
    elif section.startswith(int_end) and section.endswith(int_end):
        flt_len = len([chr for chr in section if chr == "."])
        if flt_len > 1:
            return ERROR("integer error", f"\"{section}\"", "no more then 1 \".\" in an iteger")
        elif flt_len > 0:
            obj = SYNTAX.types[1][1][1](section)
        else:
            obj = SYNTAX.types[1][1][0](section)
        return obj
    elif section == SYNTAX.keywords[3]:
        obj = SYNTAX.types[1][0]()
        return obj
    else:
        return None