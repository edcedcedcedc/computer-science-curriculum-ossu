Understanding the Goal
We need to build a **VSCode Debugging Extension prototype** 
using **CPython** and **DAP (Debug Adapter Protocol)**. 
The prototype should demonstrate our understanding 
of debugging and communication between the debugger and an IDE.  

Goal
- Implement a **simple debugger** in CPython.  
- Use **`sys.settrace`** to control code execution.  
- Communicate debugging info via **HTTP/WebSocket**.  
- Integrate with VSCode through **DAP**.  
- Make this a strong part of our **GSoC technical proposal**.  

Strategy
1. Learn Debug Adapter Protocol (DAP) 
   - Study DAP messages and lifecycle.  
   - Identify key methods (breakpoints, stepping, variables).  

2. Build a CPython Debugger
   - Use `sys.settrace` to track function calls, line execution.  
   - Capture variable states.  
   - Implement step-in, step-over, breakpoints.  

3. Set Up Communication (HTTP/WebSocket)
   - Send debugging data via WebSocket or HTTP API.  
   - Allow external clients (VSCode) to control execution.  

4. Write a Debug Adapter for VSCode 
   - Implement a DAP-compatible server in Python.  
   - Translate DAP requests into Python debugging commands.  

5. Test & Evaluate  
   - Test with simple Python scripts.  
   - Connect it to VSCode via launch.json.  

### Implementation Steps  
1. **Basic Debugger with `sys.settrace`**  
2. **WebSocket Server for Communication**  
3. **DAP Adapter Implementation**  
4. **VSCode Integration**  
5. **Testing & Debugging**  

### Evaluation  
- Does it handle breakpoints, stepping, variable inspection?  
- Does VSCode recognize it as a valid debugging backend?  
- Is communication stable over WebSocket/HTTP?  


Updates
05/03/2025:
Project init

06/03/2025:
Phase 1 and 2(debugger), have to test it more and re-read the documentation for DAP

08/03/2025:
I got denied! Thats bad news, no GSOC 2025 with pocketpy, I am dropping this project!