from cie_builtins import *

#######################################################

# Cambridge International stack ADT

# NOTE: you don't need to learn the code for this until Year 13

# You just need to understand HOW it can be programmed

# (variables used, associated operations etc.)

#######################################################

SIZE = 5
NULL = -1

#######################################################

def Push(NewItem: STRING):
    global TopPointer

    if TopPointer == SIZE - 1:
        OUTPUT ("Can't add", NewItem, "to the stack. Stack is full!")
    else:
        TopPointer = TopPointer + 1
        Stack[TopPointer] = NewItem
        
    # ENDIF
# ENDPROCEDURE
        
#######################################################

def Pop() -> STRING:
    global TopPointer

    if TopPointer == NULL:
        OUTPUT ("Can't pop from the stack. Stack is empty!")
    else:
        Popped = Stack[TopPointer]
        Stack[TopPointer] = ""
        TopPointer = TopPointer - 1
    # ENDIF
    
    return Popped
# ENDFUNCTION
    
#######################################################

def OutputStack():
    """DECLARE Bar : STRING"""
    Bar = "----------"
    for i in range(SIZE-1, -1, -1):  # FOR i ← SIZE TO 0 STEP -1
        OUTPUT(Bar)
        OUTPUT(Stack[i])
        OUTPUT(Bar)
    # NEXT i
# ENDPROCEDURE
        
#######################################################

Stack = ["" for _ in range(SIZE)]
TopPointer = -1
