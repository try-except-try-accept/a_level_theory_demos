from cie_builtins import *

#######################################################

# Cambridge International queue ADT

# NOTE: you don't need to learn the code for this until Year 13

# You just need to understand HOW it can be programmed

# (variables used, associated operations etc.)

#######################################################

SIZE = 5
NULL = None

#######################################################

def Enqueue(NewItem: STRING):
    global FrontPointer, BackPointer, QueueLength

    if QueueLength == SIZE:
        OUTPUT ("Can't enqueue", NewItem + ". Queue is full!")
    else:
        QueueLength = QueueLength + 1
        Queue[BackPointer] = NewItem
        BackPointer = BackPointer + 1
        
        if BackPointer == SIZE:
            BackPointer = 0
        # ENDIF
    # ENDIF
# ENDPROCEDURE
            
#######################################################

def Dequeue() -> STRING:
    global FrontPointer, BackPointer, QueueLength

    if QueueLength == 0:
        OUTPUT ("Can't dequeue. Queue is empty!")
        return ""
    else:
        QueueLength = QueueLength - 1
        Dequeued = Queue[FrontPointer]
        Queue[FrontPointer] = ""
        FrontPointer = FrontPointer + 1
        
        if FrontPointer == SIZE:
            FrontPointer = 0
        # ENDIF
        return Dequeued
    # ENDIF
   
# ENDFUNCTION
    
#######################################################

def OutputQueue():
    """DECLARE PrintQueue : STRING"""
    PrintQueue = ""
    for i in range(SIZE):  # FOR i ← SIZE TO 0 STEP -1
        PrintQueue = PrintQueue + Queue[i] + "  |  "
    # NEXT i
    OUTPUT (PrintQueue)
# ENDPROCEDURE
    
#######################################################

Queue = [" " for _ in range(SIZE)]
FrontPointer = 0
BackPointer = 0
QueueLength = 0
