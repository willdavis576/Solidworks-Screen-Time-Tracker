import win32gui
import time

run = False
track = False
timeDiff = 0

with open('sessionTime.txt') as f:
    timeDiff = eval(f.readlines()[0])
    f.close()

sessionStart = input("start session? (y/n) ")

if sessionStart == "y" or sessionStart == "Y":
    run = True
    
if sessionStart == "n" or sessionStart == "N":
    run = False

while run:
    try:
        nameID = win32gui.GetForegroundWindow()
        progName = win32gui.GetWindowText(nameID)
        
        if "SOLIDWORKS" in progName and track == False:
            clock = time.time() - timeDiff
            track = True
        
        if "SOLIDWORKS" in progName and track == True:
            timeDiff = time.time() - clock
            
        if "SOLIDWORKS" not in progName:
            track = False
            
        print(timeDiff)
    
    except KeyboardInterrupt:
        print("stopping")
        f = open('sessionTime.txt','w')
        f.write(str(timeDiff))
        f.close()
        break
    
        
    
