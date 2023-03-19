from cie_builtins import *

#######################################################

# Cambridge International linked list ADT

# NOTE: you don't need to learn the code for this until Year 13

# You just need to understand HOW it can be programmed

# (variables used, associated operations etc.)

#######################################################

"""CONSTANT Size = 5
CONSTANT Null = -1""" 
# exam board wants -1 to be the null pointer, this does not make sense in Python.
SIZE = 10000
NULL = None

# declare globals
"""DECLARE StartPointer, HeapPointerPointer : INTEGER  
DECLARE LinkedList : ARRAY[0:SIZE-1] OF Node"""

class Node:                        # TYPE Node
    def __init__(self):            
        self.Item = ""                # DECLARE Item : STRING
        self.Pointer = None           # DECLARE Pointer : INTEGER
                                   # ENDTYPE

##################################################################

def OutputList():
    """DECLARE OutString : STRING
    DECLARE Current: INTEGER"""
    OutString = ""
    Current = StartPointer
    while Current != NULL:
        OutString = OutString + LinkedList[Current].Item + ","   # &
        Current = LinkedList[Current].Pointer
    # ENDWHILE
    OUTPUT(OutString)
# ENDPROCEDURE
    
##################################################################

def DeleteFromList(RemoveItem: STRING):    
    global StartPointer, HeapPointer

    """DECLARE PrevPointer, ThisPointer, NextPointer : INTEGER"""

    if StartPointer == NULL:
        OUTPUT('Empty')
    else:
        # search for item to delete
        ThisPointer = StartPointer
        PrevPointer = NULL

        while ThisPointer != NULL and LinkedList[ThisPointer].Item != RemoveItem:   # <>       
            PrevPointer = ThisPointer                                        # ←
            ThisPointer = LinkedList[ThisPointer].Pointer                            # ←
        # ENDWHILE

        if ThisPointer == NULL:                              # if item to remove not found
            OUTPUT('NewItem not found')
        else:
            NextPointer = LinkedList[ThisPointer].Pointer    # store next 
            LinkedList[ThisPointer].Item = ""                       # remove the item
            LinkedList[ThisPointer].Pointer = HeapPointer    # link deleted back to heap
            HeapPointer = ThisPointer                        # update heap pointer

            if PrevPointer != NULL:
                LinkedList[PrevPointer].Pointer = NextPointer# fix broken link
            else:
                StartPointer = NextPointer                   # new start pointer needed
            # ENDIF
        # ENDIF
    # ENDIF
# ENDPROCEDURE
                
def AppendToList(NewItem: STRING):

    global StartPointer, HeapPointer

    """DECLARE PrevPointer, ThisPointer, NextPointer : INTEGER"""
    if HeapPointer == NULL:
        OUTPUT('Full')
    else:

        NewPointer = HeapPointer
        HeapPointer = LinkedList[NewPointer].Pointer           # update heap pointer
        LinkedList[NewPointer].Item = NewItem
        
        NextPointer = NULL
        PrevPointer = ''
        
        if StartPointer == NULL:
            StartPointer = NewPointer
            
        else:

            ThisPointer = StartPointer
            PrevPointer = NULL

            while ThisPointer != NULL:
                PrevPointer = ThisPointer                
                ThisPointer = LinkedList[ThisPointer].Pointer
            # ENDWHILE            

            if PrevPointer == NULL:
                StartPointer = NewPointer                       # new start pointer required
            else:
                LinkedList[PrevPointer].Pointer = NewPointer    # connect prev
            # ENDIF
        LinkedList[NewPointer].Pointer = NULL
# ENDPROCEDURE
        
               
##################################################################

def InsertIntoList(NewItem: STRING, AfterThisItem: STRING):

    global StartPointer, HeapPointer

    """DECLARE PrevPointer, ThisPointer, NextPointer : INTEGER"""
    if HeapPointer == NULL:
        OUTPUT('Full')
    else:

        ThisPointer = HeapPointer
        HeapPointer = LinkedList[ThisPointer].Pointer           # update heap pointer
        LinkedList[ThisPointer].Item = NewItem
        
        NextPointer = NULL
        PrevPointer = ''
        
        if StartPointer == NULL:
            StartPointer = ThisPointer
            
        else:

            NextPointer = StartPointer
            PrevPointer = NULL

            while NextPointer != NULL and LinkedList[NextPointer].Item != AfterThisItem:
                PrevPointer = NextPointer                
                NextPointer = LinkedList[NextPointer].Pointer
            # ENDWHILE            

            if NextPointer == NULL:                              # search failed
                OUTPUT("Not found")
                return
            elif PrevPointer == NULL:
                StartPointer = ThisPointer                       # new start pointer required
            else:
                LinkedList[PrevPointer].Pointer = ThisPointer    # connect prev
            # ENDIF
        LinkedList[ThisPointer].Pointer = NextPointer            # new node links to next (Current)
# ENDPROCEDURE
        
##################################################################

def ResetList():
    global LinkedList, StartPointer, HeapPointer
    
    LinkedList = [Node() for _ in range(SIZE)]
    for i in range(SIZE-1):                        # FOR i ← 0 TO SIZE - 2
        LinkedList[i].Pointer = i + 1              # ←
    # ENDFOR
    StartPointer = NULL
    HeapPointer = 0
# ENDPROCEDURE

ResetList()