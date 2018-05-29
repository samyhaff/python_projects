import sys
import traceback
 
def printv (var):
    for Id, Stack in sys._current_frames().items():
        for filename, lineno, name, line in traceback.extract_stack(Stack):
            if 'printv(' in line:
                print(line.replace('printv(', '').replace(')', ''), '=', var)
                
