# https://papers.gceguide.com/A%20Levels/Computer%20Science%20(for%20first%20examination%20in%202021)%20(9618)/2022/9618_s22_in_22.pdf

# https://pastpapers.co/cie/A-Level/Computer%20Science%20%28for%20first%20examination%20in%202021%29%20%289618%29/Syllabus%20%26%20Specimen/9618_y21_sg.pdf

################################################

from inspect import stack as call_stack
from random import randint
from datetime import date


file_map = {}

FALSE = False
TRUE = True
INTEGER = int
STRING = str
REAL = float
BOOLEAN = bool
CHAR = str
ARRAY = list


line_q = []

################################################

class PseudocodeNameError(NameError):
    def __init__(self):        
        self.message = f"This function does not exist"
        super().__init__(self.message)

################################################

class PseudocodeTypeError(TypeError):
    def __init__(self, func, expected_type, value_given):        
        self.message = f"{func}() received {value_given} - this is not a valid {expected_type} value"
        super().__init__(self.message)

################################################

class PseudocodeValueError(ValueError):
    def __init__(self, func, value_given, extra):        
        self.message = f"{func}() received {value_given} - " + extra
        super().__init__(self.message)

################################################

class PseudocodeFileError(FileNotFoundError):
    def __init__(self, func, fn, msg=None):        
        if msg is None:
            self.message = f'file "{fn}" is not open in memory.'
        else:
            self.message = msg
        super().__init__(self.message)

################################################

def no_func(a):    
    raise PseudocodeNameError()

################################################

def file_check(func, fn):
    try:
        file = file_map[fn]
    except KeyError:
        raise PseudocodeFileError(func, fn)

#################################################

def string_check(func, string):
    if type(string) != str:
        raise PseudocodeTypeError(func, "STRING", string)

################################################

def int_check(func, integer, minimum=None):
    if type(integer) != int:
        raise PseudocodeTypeError(func, "INTEGER", integer)
    if minimum and integer < 0:
        raise PseudocodeTypeError(func, f"INTEGER (minimum is {minimum}", integer)

################################################

def real_check(func, real):
    if type(real) != float or type(real) != int:
        raise PseudocodeTypeError(func, "REAL", real)

################################################

def char_check(func, char):
    if type(char) == str:
        if len(char) in [0, 1]:
            return

    raise PseudocodeTypeError(func, "CHARACTER", char) 

################################################

def date_check(func, this_date):
    if type(this_date) != str:
        raise PseudocodeTypeError(func, "DATE", this_date)
    try:
        dd, mm, yyyy = this_date.split("/")
    except:
        raise PseudocodeTypeError(func, "DATE", this_date)

    if not all(i.isdigit() for i in [dd, mm, yyyy]):
        raise PseudocodeTypeError(func, "DATE", this_date)

    iso = "-".join([yyyy, mm, dd])
    try:
        date.fromisoformat(iso)
    except ValueError:
        raise PseudocodeTypeError(func, "DATE", this_date)
        
################################################            

def number_check(func, number):
    number = str(number)
	
    if number[0] == "-":
        number = number[1:]

    if number.count(".") == 1:
        number = number.replace(".", "")

    if not all(d.isdigit() for d in number):
        raise PseudocodeValueError(func, number, f'not a numeric string')

#################################################

def MID(string, index, num_chars):
    """Implementation of CAIE's pseudocode MID function"""
    FUNC = call_stack()[0][3]
    string_check(FUNC, string)
    int_check(FUNC, index)
    int_check(FUNC, num_chars)
    
    if len(string) < 1:
        raise PseudocodeValueError(FUNC, string, "cannot slice an empty string.")    
    elif index < 1 or index > len(string):
        raise PseudocodeValueError(FUNC, index, f'not a valid index for the string "{string}"')
    elif num_chars + index > len(string) + 1:
        raise PseudocodeValueError(FUNC, num_chars, f'not enough characters in string "{string}"')
    return string[index-1:index+num_chars-1]

################################################

def LENGTH(string):
    """Implementation of CAIE's pseudocode LENGTH function"""
    FUNC = call_stack()[0][3]
    string_check(FUNC, string)        
    return len(string)

################################################
    
def LEFT(string, num_chars):
    """Implementation of CAIE's pseudocode LEFT function"""
    
    FUNC = call_stack()[0][3]
    string_check(FUNC, string)
    int_check(FUNC, num_chars)
    
    if num_chars > len(string):
        raise PseudocodeValueError(FUNC, num_chars, f'not enough characters in string "{string}"')
        
    return string[:num_chars]

################################################

def RIGHT(string, num_chars):
    """Implementation of CAIE's pseudocode RIGHT function"""
        
    FUNC = call_stack()[0][3]
    
    string_check(FUNC, string)
    int_check(FUNC, num_chars)
    
    if num_chars > len(string):
        raise PseudocodeValueError(FUNC, num_chars, f'not enough characters in string "{string}"')
    
    return string[0-num_chars:]

################################################

def INT(real):
    """Implementation of CAIE's pseudocode INT function"""
    
    FUNC = call_stack()[0][3]
    number_check(FUNC, real)
    
    return int(real)

################################################

def NUM_TO_STR(num):
    """Implementation of CAIE's pseudocode NUM_TO_STR function"""
    
    FUNC = call_stack()[0][3]
    number_check(FUNC, str(num))
    
    return str(num)

################################################

def STR_TO_NUM(string):
    """Implementation of CAIE's pseudocode STR_TO_NUM function"""
    string = str(string)
    
    FUNC = call_stack()[0][3]
    string_check(FUNC, string)
    number_check(FUNC, string)

    if "." in string:
        return float(string)
    else:
        return int(string)

################################################

def LCASE(char):
    """Implementation of CAIE's pseudocode LCASE function"""
    
    FUNC = call_stack()[0][3]    
    char_check(FUNC, char)
        
    return char.lower()

################################################    

def UCASE(char):
    """Implementation of CAIE's pseudocode UCASE function"""
    
    FUNC = call_stack()[0][3]    
    char_check(FUNC, char)
        
    return char.upper()

################################################

def TO_LOWER(string):
    """Implementation of CAIE's pseudocode TO_LOWER function"""
    
    FUNC = call_stack()[0][3]    
    string_check(FUNC, string)
        
    return string.lower()

################################################

def TO_UPPER(string):
    """Implementation of CAIE's pseudocode TO_UPPER function"""
    
    FUNC = call_stack()[0][3]    
    string_check(FUNC, string)
        
    return string.upper()

################################################

def IS_NUM(string):
    """Implementation of CAIE's pseudocode IS_NUM function"""
    
    FUNC = call_stack()[0][3]    
    string_check(FUNC, string)
    try:
        number_check(FUNC, string)
        return True
    except PseudocodeValueError:
        return False
        
################################################

def ASC(char):
    """Implementation of CAIE's pseudocode ASC function"""
    
    FUNC = call_stack()[0][3]    
    char_check(FUNC, char)
    return ord(char)

################################################        

def CHR(x):
    """Implementation of CAIE's pseudocode CHR function"""
    
    FUNC = call_stack()[0][3]    
    int_check(FUNC, x, minimum=1)
    return chr(x)

################################################

def RAND(x):
    """Implementation of CAIE's pseudocode RAND function"""
    
    FUNC = call_stack()[0][3]    
    int_check(FUNC, x, minimum=1)
    
    return round(randint(0, x*100)/100, 2)

################################################

def DAY(date):
    """Implementation of CAIE's pseudocode DAY function"""
    
    FUNC = call_stack()[0][3]    
    date_check(FUNC, date)
    
    return int(date.split("/")[0])

################################################

def MONTH(date):
    """Implementation of CAIE's pseudocode MONTH function"""
    
    FUNC = call_stack()[0][3]    
    date_check(FUNC, date)    
    
    return int(date.split("/")[1])

################################################

def YEAR(date):
    """Implementation of CAIE's pseudocode YEAR function"""
    
    FUNC = call_stack()[0][3]    
    date_check(FUNC, date)    
    
    return int(date.split("/")[2])

################################################

def DAYINDEX(this_date):
    """Implementation of CAIE's pseudocode DAYINDEX function"""
    FUNC = call_stack()[0][3]    
    days = "Sun,Mon,Tue,Wed,Thu,Fri,Sat,Sun".split(",")
    date_check(FUNC, this_date)
    dd, mm, yy = this_date.split("/")
    day = date(*map(int, [yy, mm, dd])).strftime("%a")
    
    return days.index(day)

################################################

def TODAY():
    """Implementation of CAIE's pseudocode TODAY function"""    
    return date.today().strftime("%d/%m/%Y")    

################################################
    
def SETDATE(dd, mm, yyyy):
    """Implementation of CAIE's pseudocode TODAY function"""
    FUNC = call_stack()[0][3]    
    int_check(FUNC, dd, minimum=1)
    int_check(FUNC, mm, minimum=1)
    int_check(FUNC, yyyy, minimum=1)
    try:
        return f"{str(dd).zfill(2)}/{str(mm).zfill(2)}/{yyyy}"
    except ValueError:
        raise PseudocodeValueError(func, [dd, mm, yyyy], "dd/mm/yy out of range")

################################################

def INPUT():
    """Implementation of CAIE's pseudocode INPUT statement"""
    return input()
	
################################################

def OUTPUT(*text):
    """Implementation of CAIE's pseudocode OUTPUT statement"""
    print(" ".join(str(t) for t in text))

################################################

def OPENFILE(file_name, mode):
    """Implementation of CAIE's pseudocode OPENFILE statement"""
    FUNC = call_stack()[0][3]
    try:
        file_check(file_name)
        raise PseudocodeFileError(FUNC, file_name, "can't open file - already open in memory.")
    except:
        pass
        
    try:
        mode = {"FOR READ":"r","FOR WRITE":"w","FOR APPEND":"a", "FOR RANDOM":"rb"}[mode]
    except KeyError:
        raise PseudocodeFileError(FUNC, file_name, "FOR (mode) must be READ/WRITE/APPEND/RANDOM")
    
    file_map[file_name] = open(file_name, mode)
    
################################################

def WRITEFILE(file_name, data):
    """Implementation of CAIE's pseudocode WRITEFILE statement"""
    FUNC = call_stack()[0][3]   
    file_check(FUNC, file_name)
    string_check(FUNC, data)

    file = file_map[file_name]

    file.write(data + "\n")    
    
################################################


def READFILE(file_name):
    """Implementation of CAIE's pseudocode READFILE statement"""

    FUNC = call_stack()[0][3]   
    file_check(FUNC, file_name)

    if len(line_q):
        return line_q.pop(0) 

    file = file_map[file_name]   

    return file.readline().strip()   
    
################################################


def CLOSEFILE(file_name):
    """Implementation of CAIE's pseudocode READFILE statement"""
    FUNC = call_stack()[0][3]

    file_check(FUNC, file_name)

    file_map[file_name].close()

    file_map.pop(file_name)
    
################################################

def EOF(file_name):
    """Implementation of CAIE's pseudocode EOF function"""
    FUNC = call_stack()[0][3]

    file_check(FUNC, file_name)

    this_line = file_map[file_name].readline().strip()
    if this_line:
        line_q.append(this_line)
    else:
        return True

    
################################################

    
def NOT(exp):
    """Implementation of CAIE's pseudocode NOT operator, which is normally used like a function"""
    return not exp

################################################

def tests():

    string = "hello"
    char = 'X'
    today_date = "20/11/2022"

    try:
        assert MID(string, 1, 1) == 'h'
    except Exception as e:
        print(e)
    try:
        assert MID(string, 5, 1) == 'o'
    except Exception as e:
        print(e)
    try:
        assert MID(string, 1, 5) == string
    except Exception as e:
        print(e)
    try:
        MID(string, 1, 6)
    except Exception as e:
        print(e)
    try:
        MID(453, 1, 6)
    except Exception as e:
        print(e)

    try:
        assert LENGTH(string) == 5
    except Exception as e:
        print(e)
    try:
        LENGTH(123)
    except Exception as e:
        print(e)
    try:
        LENGTH(False)
    except Exception as e:
        print(e)
    try:
        assert LENGTH("") == 0
    except Exception as e:
        print(e)

    try:
        assert LEFT(string, 1) == 'h'
    except Exception as e:
        print(e)
    try:
        assert LEFT(string, 3) == 'hel'
    except Exception as e:
        print(e)
    try:
        LEFT(string, 10)
    except Exception as e:
        print(e)
    try:
        LEFT(123, 3)
    except Exception as e:
        print(e)
    try:
        LEFT(string, 0)
    except Exception as e:
        print(e)

    try:
        assert RIGHT(string, 1) == 'o'
    except Exception as e:
        print(e)
    try:
        assert RIGHT(string, 4) == "ello"
    except Exception as e:
        print(e)
    try:
        RIGHT(string, 10)
    except Exception as e:
        print(e)
    try:
        RIGHT(4312, 5)
    except Exception as e:
        print(e)
    try:
        RIGHT(string, 2.2)
    except Exception as e:
        print(e)

    try:
        assert INT(3.433) == 3
    except Exception as e:
        print(e)
    try:
        assert INT(-9.9999) == 9
    except Exception as e:
        print(e)
    try:
        INT(342)
    except Exception as e:
        print(e)
    try:
        INT("3242.34")
    except Exception as e:
        print(e)
    try:
        INT(3 > 4)
    except Exception as e:
        print(e)

    try:
        assert NUM_TO_STR(343) == "343"
    except Exception as e:
        print(e)
    try:
        assert NUM_TO_STR(-343) == "-343"
    except Exception as e:
        print(e)
    try:
        assert NUM_TO_STR(3.555) == "3.555"
    except Exception as e:
        print(e)
    try:
        NUM_TO_STR("23423")
    except Exception as e:
        print(e)
    try:
        NUM_TO_STR(False)
    except Exception as e:
        print(e)

    try:
        assert STR_TO_NUM("555") == 555
    except Exception as e:
        print(e)
    try:
        assert STR_TO_NUM("5.5") == 5.5
    except Exception as e:
        print(e)
    try:
        assert STR_TO_NUM("-34") == -34
    except Exception as e:
        print(e)
    try:
        STR_TO_NUM("234324x")
    except Exception as e:
        print(e)
    try:
        STR_TO_NUM("-234324-")
    except Exception as e:
        print(e)

    try:
        assert LCASE("X") == "x"
    except Exception as e:
        print(e)
    try:
        assert LCASE("x") == "x"
    except Exception as e:
        print(e)
    try:
        LCASE('')
    except Exception as e:
        print(e)
    try:
        LCASE("abc")
    except Exception as e:
        print(e)
    try:
        LCASE(123)
    except Exception as e:
        print(e)

    try:
        assert UCASE('h') == 'H'
    except Exception as e:
        print(e)
    try:
        assert UCASE('1') == '1'
    except Exception as e:
        print(e)
    try:
        UCASE(123)
    except Exception as e:
        print(e)
    try:
        UCASE(4)
    except Exception as e:
        print(e)
    try:
        UCASE(False)
    except Exception as e:
        print(e)

    try:
        assert TO_LOWER(string) == string
    except Exception as e:
        print(e)
    try:
        assert TO_LOWER("a213B") == "a213b"
    except Exception as e:
        print(e)
    try:
        assert TO_LOWER("HELLO%") == string + '%'
    except Exception as e:
        print(e)
    try:
        TO_LOWER(1231)
    except Exception as e:
        print(e)
    try:
        TO_LOWER(False)
    except Exception as e:
        print(e)

    try:
        assert TO_UPPER(string) == "HELLO"
    except Exception as e:
        print(e)
    try:
        assert TO_UPPER("123") == "123"
    except Exception as e:
        print(e)
    try:
        assert TO_UPPER("DINOSAUr") == "DINOSAUR"
    except Exception as e:
        print(e)
    try:
        TO_UPPER(4234.4)
    except Exception as e:
        print(e)
    try:
        TO_UPPER([342,343])
    except Exception as e:
        print(e)

    try:
        assert IS_NUM("-5") == True
    except Exception as e:
        print(e)
    try:
        assert IS_NUM("53.25") == True
    except Exception as e:
        print(e)
    try:
        assert IS_NUM("-3242-") == False
    except Exception as e:
        print(e)
    try:
        assert IS_NUM("453.5335.") == False
    except Exception as e:
        print(e)
    try:
        IS_NUM(234.234)
    except Exception as e:
        print(e)

    try:
        assert ASC("X") == ord("X")
    except Exception as e:
        print(e)
    try:
        assert ASC("☺") == ord("☺")
    except Exception as e:
        print(e)
    try:
        ASC(123)
    except Exception as e:
        print(e)
    try:
        ASC("Awe")
    except Exception as e:
        print(e)
    try:
        ASC(False)
    except Exception as e:
        print(e)

    try:
        assert CHR(123) == chr(123)
    except Exception as e:
        print(e)
    try:
        assert CHR(156151) == chr(156151)
    except Exception as e:
        print(e)
    try:
        CHR(-342)
    except Exception as e:
        print(e)
    try:
        CHR("d")
    except Exception as e:
        print(e)
    try:
        CHR(False)
    except Exception as e:
        print(e)

    try:
        assert 0 <= RAND(5) <= 5
    except Exception as e:
        print(e)
    try:
        assert type(RAND(10)) == float
    except Exception as e:
        print(e)
    try:
        assert 0 <= RAND(100) <= 100
    except Exception as e:
        print(e)
    try:
        RAND(0)
    except Exception as e:
        print(e)
    try:
        RAND("dogs")
    except Exception as e:
        print(e)

    try:
        assert DAY(today_date) == 20
    except Exception as e:
        print(e)
    try:
        assert DAY("05/06/1999") == 5
    except Exception as e:
        print(e)
    try:
        DAY("2023/23/23")
    except Exception as e:
        print(e)
    try:
        DAY("12/12/99")
    except Exception as e:
        print(e)
    try:
        DAY(234)
    except Exception as e:
        print(e)

    try:
        assert MONTH(today_date) == 11
    except Exception as e:
        print(e)
    try:
        assert MONTH("05/06/1999") == 6
    except Exception as e:
        print(e)
    try:
        MONTH("2023/23/23")
    except Exception as e:
        print(e)
    try:
        MONTH("12/12/99")
    except Exception as e:
        print(e)
    try:
        MONTH(234)
    except Exception as e:
        print(e)

    try:
        assert YEAR(today_date) == 2022
    except Exception as e:
        print(e)
    try:
        assert YEAR("05/06/1999") == 1999
    except Exception as e:
        print(e)
    try:
        YEAR("2023/23/23")
    except Exception as e:
        print(e)
    try:
        YEAR("12/12/99")
    except Exception as e:
        print(e)
    try:
        YEAR(234)
    except Exception as e:
        print(e)

    try:
        assert DAYINDEX(today_date) == 0
    except Exception as e:
        print(e)
    try:
        DAYINDEX("2023/23/23")
    except Exception as e:
        print(e)
    try:
        DAYINDEX("2022-11-22")
    except Exception as e:
        print(e)
    try:
        DAYINDEX(234234)
    except Exception as e:
        print(e)
    try:
        assert DAYINDEX("21/11/2022") == 1
    except Exception as e:
        print(e)

    try:
        assert TODAY() == date.today().strftime("%d/%m/%y")
    except Exception as e:
        print(e)

    try:
        assert SETDATE(20, 11, 2022) == today_date
    except Exception as e:
        print(e)
    try:
        assert SETDATE(1, 1, 1999) == "01/01/1999"
    except Exception as e:
        print(e)
    try:
        SETDATE(99, 99, 1999)
        print("Able to SETDATE with illogical mm / dd values")
        assert False
    except Exception as e:
        print(e)
    try:
        SETDATE(29, 2, 2022)
        print("Able to SETDATE with illegal 29th feb")
        assert False
    except Exception as e:
        print(e)
    try:
        SETDATE(6, 13, 2000)
        print("Able to SETDATE with mm and dd switched")
        assert False
    except Exception as e:
        print(e)

    try:
        READFILE("notopen")
        print("Able to read from file not open")
        assert False
    except Exception as e:
        print(e)

    OPENFILE("write.txt", "FOR WRITE")

    assert "write.txt" in file_map

    WRITEFILE("write.txt", "some text")

    try:
        READFILE("write.txt")
        print("reading from file open in write mode?")
    except Exception as e:
        print(e)

    CLOSEFILE("write.txt")

    OPENFILE("write.txt", "FOR READ")

    assert READFILE("write.txt") == "some text"

    try:
        CLOSEFILE("notopen")
        print("Able to close file not open")
        assert False
    except Exception as e:
        print(e)

    CLOSEFILE("write.txt")

    OPENFILE("write.txt", "FOR WRITE")
    WRITEFILE("write.txt", "new")
    CLOSEFILE("write.txt")
    OPENFILE("write.txt", "FOR READ")

    assert READFILE("write.txt") == "new"

    CLOSEFILE("write.txt")

    OPENFILE("write.txt", "FOR APPEND")
    WRITEFILE("write.txt", "second")
    CLOSEFILE("write.txt")
    OPENFILE("write.txt", "FOR READ")
    x = READFILE("write.txt")
    y = READFILE("write.txt")
    assert x + y == "newsecond"


if __name__ == "__main__":
    tests()
