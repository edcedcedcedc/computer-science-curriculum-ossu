""" 
Implements the Python debugger using sys.settrace; requested by @blueloveTH 

Copyright (c) 05.03.2025  Andro Ranogajec @edcedcedcedc

Permission is hereby granted, free of charge, to any person obtaining a copy of this software 
and associated documentation files (the "Software"), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions: The above copyright notice and this permission notice shall be 
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN 
ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION 
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

 """

import sys

STATE = {"step_in": False, "step_over": False, "breakpoints": [74,69] }

def tracefunc(frame, event, arg):
    if event == "call":

        if STATE["step_in"]:
            STATE["step_over"] = False
            return tracefunc
        elif STATE["step_over"]:
            STATE["step_in"] = False
            return None
        
        print(f"Call: {frame.f_code.co_name}, with Args: {frame.f_locals}, Line: {frame.f_lineno}")

    elif event == "line":
    
        if frame.f_lineno in STATE["breakpoints"]:
            print(f"Breakpoint hit at line {frame.f_lineno}")
            
            while True:
                user_input = input("(c) Continue, (i) Step into, (o) Step over: ")
                if user_input == "c":
                    STATE["step_in"] = False
                    STATE["step_over"] = False
                    break
                elif user_input == "i":
                    STATE["step_in"] = True  
                    STATE["step_over"] = False 
                    break
                elif user_input == "o":
                    STATE["step_in"] = False
                    STATE["step_over"] = True
                    break
                else:
                    print(f"Wrong token {user_input}, please try again!")
            
        
        print(f"Line: {frame.f_code.co_name}, with Args: {frame.f_locals} Line: {frame.f_lineno}")
    elif event == "return":
        print(f"Return: {frame.f_code.co_name}, Return value: {arg} Line: {frame.f_lineno}, ")
    elif event == "exception":
        print(f"Exception: {frame.f_code.co_name}, Line: {frame.f_lineno}: {arg}")
    return tracefunc
   
def funcA():
    x = 10
    return x

def funcB():
    y = 15
    return funcA() + y

def main():
    sys.settrace(tracefunc)
    funcB()
    sys.settrace(None) 

if __name__ == "__main__":
    main()


