# please leave this here:

from cie_builtins import * 

###########################################

def HomeMadeMid(s: STRING, start: INTEGER, num : INTEGER) -> STRING:
    start = start - 1 # ←
    
    return MID(s, start, num)   
# ENDFUNCTION

def Parse(s: STRING) -> STRING:
    """DECLARE nums : ARRAY[1:10] OF INTEGER
    DECLARE ThisChar: CHAR
    DECLARE ThisNum : STRING
    DECLARE Count, Total : INTEGER
    DECLARE Average:  REAL"""
    ThisNum = "" # ←

    Total = 0 # ←
    Count = 0 # ←
    for Index in range(1, LENGTH(s)+1): # FOR Index ← 1 TO LENGTH(s)
        ThisChar = MID(s, Index, 1) # ←
        
        if ThisChar != ',': # <> THEN
            ThisNum = ThisNum + ThisChar # ←
        # ENDIF

        if ThisChar == "," or Index == LENGTH(s): # =, =, THEN
            Total = Total + STR_TO_NUM(ThisNum) # ← 
            ThisNum = "" # ←
            Count = Count + 1 # ←
        # ENDIF
    # NEXT Index
    Average = Total / Count # ←
    OUTPUT ("ffff")
    return "The average is " + NUM_TO_STR(Average) + " and the total is " + NUM_TO_STR(Total) + '.'
# ENDFUNCTION
def IsPalindrome(s : STRING) -> BOOLEAN:
    """DECLARE i, j : INTEGER"""
    i = 1  # ← 
    j = LENGTH(s) # ← 
    s = TO_LOWER(s) # ← 

    while i < j: 


        if MID(s, i, 1) != MID(s, j, 1): # <> THEN
            return FALSE
        # ENDIF

        i = i + 1 # ←
        j = j - 1 # ←
    # ENDWHILE

    return TRUE
# ENDFUNCTION
def FindSevens(x : INTEGER, y : INTEGER):
    """DECLARE count, x : INTEGER"""
    count = 0 # ←

    for p in range(x, y+1): # FOR p ← x TO y
        if NUM_TO_STR(p)[-1] == '7': # THEN, =
            OUTPUT(p)
            count = count + 1 # ←
        # ENDIF
    # NEXT p

    OUTPUT(count)
# ENDPROCEDURE

def GetField1And3(fn : STRING, s : STRING) -> STRING:
    """DECLARE line, buffer : STRING"""

    OPENFILE(fn, "FOR READ")

    buffer = "" # ←
    for i in range(LENGTH(s)): # FOR i ← 0 TO LENGTH(s)
        buffer = buffer + " " # ←
    # NEXT i
    while NOT(EOF(fn)):
        line = READFILE(fn) # ←

        if MID(line, LENGTH(s)+1, LENGTH(s)) == s: # = THEN
            return MID(line, 1, LENGTH(s)) + buffer + MID(line, (LENGTH(s)*2)+1, LENGTH(s))
        # ENDIF
    # ENDWHILE
    CLOSEFILE(fn)
# ENDFUNCTION
def NewLastLines(fn : STRING, x: INTEGER) -> ARRAY:
    """DECLARE Lines : ARRAY[0:x] OF STRING
    DECLARE Counter : INTEGER
    DECLARE line : STRING"""
    Lines = [None for _ in range(x)]
    Counter = 0 # ←

    OPENFILE(fn, "FOR READ")
 
    while NOT(EOF(fn)):
        line = READFILE(fn) # ←
        for i in range(1, x): # FOR i ← 1 TO x
            Lines[i-1] = Lines[i] # ←
        # NEXT i

        Lines[x-1] = line # ←
        
    # ENDWHILE

    CLOSEFILE(fn)

    return Lines
# ENDFUNCTION

def LastLines(fn : STRING) -> ARRAY:
    """DECLARE Lines : ARRAY[0:2] OF STRING
    DECLARE Counter : INTEGER
    DECLARE line : STRING"""
    Lines = [None for _ in range(3)]
    Counter = 0 # ←

    OPENFILE(fn, "FOR READ")
 
    while NOT(EOF(fn)):
        line = READFILE(fn) # ←
        for i in range(1, 3): # FOR i ← 1 TO x
            Lines[i-1] = Lines[i] # ←
        # NEXT i

        Lines[2] = line # ←
        
    # ENDWHILE

    CLOSEFILE(fn)

    return Lines
# ENDFUNCTION
