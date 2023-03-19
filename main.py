# please leave these here:

from given_modules_and_data import  Screen, LogArray
from cie_builtins import *
USE_LINTER = FALSE

################################################


def SortAscending(Numbers: ARRAY, Size : INTEGER) -> ARRAY:
    """DECLARE Index, Temp : INTEGER
DECLARE SwapMade : BOOLEAN"""

    Index = 0 # ←
    SwapMade = TRUE # ←
    
    while SwapMade:
        SwapMade = FALSE
        for Index in range(0, Size-1):
            if Numbers[Index] > Numbers[Index+1]:
                Temp = Numbers[Index] # ←
                Numbers[Index] = Numbers[Index + 1] # ←
                Numbers[Index + 1] = Temp # ←
                SwapMade = TRUE # ←
        
    return Numbers

def ReBoot() -> BOOLEAN: # FUNCTION ReBoot RETURNS BOOLEAN
    return TRUE
# ENDFUNCTION

def Alert(n: INTEGER): # PROCEDURE
    OUTPUT (n)
# ENDPROCEDURE

def Check() -> BOOLEAN: # FUNCTION Check RETURNS BOOLEAN
    return FALSE
# ENDFUNCTION

def FlowChartAlgorithm(): # PROCEDURE

    """DECLARE Count: INTEGER
    DECLARE Flag: BOOLEAN"""
    Flag = FALSE # ←
    Count = 1 # ←

    while Flag == FALSE and Count <= 5: # WHILE .. AND =
        ReBoot() # CALL ReBoot
        Count = Count + 1 # ←
        Flag = Check() # ←
    # ENDWHILE
    
    if Flag == FALSE: # IF = THEN
        Alert(27) # CALL ReBoot
    # ENDIF
# ENDPROCEDURE

def AnAlgorithm(): # PROCEDURE

    """DECLARE IntVal, PosCount, NegCount, PosSum, NegSum, Index : INTEGER"""
    PosCount = 0 # ←
    NegCount = 0 # ←
    PosSum = 0 # ←
    NegSum = 0 # ←

    IntVal = 999 # ←

    while IntVal != 0: # WHILE <>
        IntVal = STR_TO_NUM(INPUT()) # INPUT IntVal
        
        if IntVal > 0: # IF THEN
            PosSum = PosSum + IntVal # ←
            PosCount = PosCount + 1 # ←
        elif IntVal < 0: # ELSE IF THEN
            NegSum = NegSum + IntVal # ←
            NegCount = NegCount + 1 # ←
        # ENDIF
    OUTPUT ("Positive values counted: " + NUM_TO_STR(PosCount))
    OUTPUT ("Positive total: " + NUM_TO_STR(PosSum))
    
    OUTPUT ("Negative values counted: " + NUM_TO_STR(NegCount))
    OUTPUT ("Negative total: " + NUM_TO_STR(NegSum))
# ENDPROCEDURE

class Student: # TYPE Student
    def __init__(self):
        self.StudentID = "" #  DECLARE StudentID : STRING
        self.Email = "" # DECLARE Email : STRING
        self.Club_1 = 0 # DECLARE Club_1 : STRING
        self.Club_2 = 0 # DECLARE Club_2 : STRING
        self.Club_3 = 0 # DECLARE Club_3 : STRING
# ENDTYPE

"""DECLARE Membership : ARRAY[1:50] OF STUDENT"""
Membership = [Student() for _ in range(50)]
Membership[0].StudentID = 'AX1023' # ←
Membership[0].Club_1 = 65 # ←
Membership[0].Club_2 = 99 # ←
Membership[1].StudentID = 'FA3123' # ←
Membership[1].Club_2 = 99 # ←
Membership[2].StudentID = 'FE3342' # ←
Membership[2].Club_1 = 65 # ←
Membership[2].Club_2 = 99 # ←
Membership[3].StudentID = 'GF3424' # ←
Membership[3].Club_3 = 99 # ←
Membership[4].StudentID = 'LK2111' # ←
Membership[4].Club_1 = 65 # ←

Membership[5].StudentID = 'CB9900' # ←
Membership[5].Club_1 = 99 # ←

Membership[6].StudentID = 'FS9990' # ←
Membership[6].Club_1 = 65 # ←

Membership[7].StudentID = 'FS2344' # ←

Membership[7].Club_3 = 99 # ←
Membership[8].StudentID = 'HS2311' # ←
Membership[8].Club_1 = 99 # ←

Membership[9].StudentID = 'AF1124' # ←
Membership[9].Club_1 = 65 # ←
Membership[9].Club_2 = 99 # ←

Membership[10].StudentID = 'FA9293' # ←
Membership[10].Club_1 = 99 # ←

Membership[11].StudentID = 'FA1234' # ←
Membership[11].Club_1 = 65 # ←
Membership[11].Club_2 = 99 # ←
Membership[11].Club_3 = 99  # ←




def GetIDs(): # PROCEDURE
    """DECLARE ClubNo, Index, Count : INTEGER"""
    OUTPUT ("Give club number: ")
    ClubNo = STR_TO_NUM(INPUT())  # ←
    Count = 0  # ←
    for Index in range(0, 50): # FOR Index ← 0 TO 49
        if Membership[Index].Club_1 == ClubNo or Membership[Index].Club_2 == ClubNo or Membership[Index].Club_3 == ClubNo:
            OUTPUT (Membership[Index].StudentID)
            Count = Count + 1  # ←
        # ENDIF
    # NEXT Index

    OUTPUT ("Number of students in club number " + NUM_TO_STR(ClubNo) + ": " + NUM_TO_STR(Count))
# ENDPROCEDURE

def LogEvents(StudentID: STRING) -> INTEGER: # FUNCTION LogEvents(StudentID: STRING) RETURNS INTEGER
    """DECLARE Index, Count : INTEGER"""
    OPENFILE("LogFile.txt", "FOR APPEND")
    Count = 0  # ←

    for Index in range(0, 50): # FOR Index ← 0 TO 49
        if LogArray[Index] != "":   # IF <> THEN
            if LEFT(LogArray[Index], 6) == StudentID: # IF = THEN
                WRITEFILE("LogFile.txt", LogArray[Index])            
                Count = Count + 1  # ←
                LogArray[Index] = ""  # ←
            # ENDIF
        # ENDIF
    # NEXT In
    CLOSEFILE("LogFile.txt")
    return Count
# ENDFUNCTION

def MakeNewFile(FileName: STRING, NewFileName: STRING, SearchStatus: STRING): # PROCEDURE
    """DECLARE Originals, Copies : INTEGER
    DECLARE Name, Email, Status : STRING"""
    Originals = 0  # ←
    Copies = 0  # ←
    OPENFILE(NewFileName, "FOR WRITE")

    OPENFILE(FileName, "FOR READ")

    while NOT(EOF(FileName)): # WHILE
        Name = READFILE(FileName)
        Email = READFILE(FileName)
        Status = READFILE(FileName)
        Originals = Originals + 1 # ←

        if Status == SearchStatus: # IF = THEN
            WRITEFILE(NewFileName, Name)
            WRITEFILE(NewFileName, Email)
            WRITEFILE(NewFileName, Status)
            Copies = Copies + 1 # ←
        # ENDIF
    OUTPUT ("File " + FileName + " contained " + NUM_TO_STR(Originals) + " employee details")
    OUTPUT (Copies, "employee sets of details were written to file", NewFileName)
    CLOSEFILE(FileName)
    CLOSEFILE(NewFileName)
# ENDPROCEDURE

def SetRow(Row: INTEGER, Column: INTEGER, Pixels: INTEGER) -> ARRAY: # FUNCTION SetRow RETURNS ARRAY
    """DECLARE x : INTEGER"""
    global Screen
    for x in range(Column, Column+Pixels): # FOR x ← Column TO Column + Pixels
        Screen[Row-1][x-1] = 1 # ←
    # NEXT x
    return Screen
# ENDFUNCTION

def SearchInRow(Row : INTEGER, Column: INTEGER) -> INTEGER: # FUNCTION.. RETURNS INTEGER
    """DECLARE x, Start, End, Step : INTEGER"""
    if Column == 1: # IF = THEN
        Start = 0 # ←
        End = 128 # ←
        Step = 1 # ←
    else: # ELSE
        End = -1 # ←
        Start = 127 # ←
        Step = -1  # ←
    # ENDIF
    
    for x in range(Start, End, Step): # FOR x ← 1 TO End
        if Screen[Row-1][x] == 1:     # IF  = [Row, x] = THEN
            return x+1
        # ENDIF
    # NEXT x
    return -1
# ENDFUNCTION

def GetCentreCol(Row: INTEGER, ) -> INTEGER: # FUNCTION GetCentreCol(Row: INTEGER) RETURNS INTEGER
    """DECLARE First, Last : INTEGER"""
    First = SearchInRow(Row, 1) # ←
    Last = SearchInRow(Row, 128)  # ←
    if First == Last == -1: # IF = THEN
        return -1
    elif First == Last: # ELSE IF ...  = THEN
        return First
    else:
        return First + (Last-First) // 2
    # ENDIF
# ENDFUNCTION

if __name__ == "__main__":   
    SetRow(50, 50, 30)
    print(GetCentreCol(50), 65)
