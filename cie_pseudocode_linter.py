import unittest
from main import *
import random
import builtins
import unittest
from io import StringIO, TextIOWrapper
from unittest.mock import patch
NUM_TASKS = 3

# Add initialization code here
import unittest
from main import *
# Add imports here

import random
import builtins
import unittest
from io import StringIO, TextIOWrapper
from unittest.mock import patch
NUM_TASKS = 9
GLOBALS = ["Membership", "Screen", "LogArray"]
TASKS = ["SortAscending",
"FlowchartAlgorithm",
"AnAlgorithm",
"Student",
"GetIDs",
"LogEvents",
"MakeNewFile",
"SetRow",
"SearchInRow",
"GetCentreCol"]




class CIEPseudocodeLinter(unittest.TestCase):
    def test_interfaces_check(self):
      # Enter code here

      if self.interfaces_check:
        raise Exception(self.interfaces_check)

      assert self.interfaces_check == ""

    def test_comments_check(self):
      # Enter code here
      if self.comments_check:

        raise Exception("\n".join(self.comments_check))

      assert len(self.comments_check) == 0

    def test_illegal_techniques(self):
      # Enter code here
   
      if self.illegal_techniques_check:

        raise Exception("\n".join(self.illegal_techniques_check))

      assert len(self.illegal_techniques_check) == 0


    def test_variable_declarations(self):
      # Enter code here
      
      
      if self.declarations_check:

        raise Exception(self.declarations_check)

      assert self.declarations_check == ""

#### Initialization ####

    def redirect_print(self, *args, end="\n", sep=" "):
      self.print_log += sep.join(str(a) for a in args) + end


    def mock_input(self):
      return self.mock_inputs.pop(0)

    def check_for_illegals(self):

      illegal_at_start = 'f"'

      
      for tn, task in self.code_by_task.items():
      
        for pos_check, illegals in self.illegal_map.items():

          for illegal in illegals:
          
            
            all_code = "".join(task.code)
            illegal_found = False
            if pos_check in ["start","token"]:
      
              if any(token.startswith(illegal) for token in all_code.split()):
                illegal_found = True
            
            elif illegal in all_code:
              illegal_found = True
      
            if illegal_found:
              s = f"Illegal pseudocode-style Python technique encountered: {illegal} in {tn} solution."
              self.illegal_techniques_check.add(s)

      for line in task.code:
        remove_string = ""
        quote = []

        for char in line:
          for quote_check in ["'", '"']:
            if char == quote_check:
              if quote and quote[-1] == char:
                quote.pop(-1)
              else:
                quote.append(quote_check)
              continue
          if quote:
            continue

          remove_string += char
          
        tokens = remove_string.split()
        
        if "in" in tokens:
          in_pos = tokens.index("in")
          if tokens[in_pos+1].startswith("range") == False:
            exp = f"{tokens[in_pos-1]} {tokens[in_pos]} {tokens[in_pos+1]}"
            self.illegal_techniques_check.add(f"Illegal pseudocode-style Python technique encountered: {exp} in {tn} solution.")

        if "[" in line and "]" in line:
          var = line.split("[")[0].split()[-1].strip()
          for p in task.params: # TODO + task.locals:

              if p.name == var:
                  if p.type and "ARRAY" not in p.type:

                      self.illegal_techniques_check.add(f"Illegal pseudocode-style Python technique encountered: {var}[x] in {tn} solution.")


    def check_declarations(self):

      
      
      for task in self.code_by_task.values():

        for line in task.code:
          if "#" in line:
            line = line[:line.index("#")]
          if " = " in line:
            var = line.split(" = ")[0]
            if "[" in var:
              var = var.split("[")[0]

          elif line.startswith("for "):
            var = line[5:].split()[0]

          else:
            continue
          var = var.strip()
          if var in GLOBALS:
            continue
          if "." not in var and var not in task.declarations and not any(p.startswith(var) for p in task.params):
            msg = f"Variable {var} has not been declared.\n"
            if msg not in self.declarations_check:
              self.declarations_check += msg

    def check_interfaces(self):



      for tn, task in self.code_by_task.items():
        
        header = task.code[0]
        return_annotation = ""
        if "->" in header:
          header = header.split("#")[0]
          return_annotation = header.split(" -> ")[-1].strip()[:-1]
          if return_annotation not in self.ALLOWED_TYPES:
              self.interfaces_check += f"Invalid type declaration for return value {return_annotation} in {tn}.\n"

        if "return" in "".join(task.code) and not return_annotation:
          self.interfaces_check += f"Missing return type annotation for {tn}.\n"   
        
        for param in task.params:
          if param.type == "":
            self.interfaces_check += f"No type declaration for param {param} in {tn}.\n"
          else:
            if param.type.strip() not in self.ALLOWED_TYPES:

              self.interfaces_check += f"Invalid type declaration for param {param} ({param.type}) in {tn}.\n"
        
          
          

    def check_comments(self):

      inline = {"=":"←",
                "==":"=",
               "!=":"<>",
               "%":"MOD",
               "//":"DIV",
                '+ "':"&",
                "+ '":"&",
                "][":","
               }



      for tn, task in self.code_by_task.items():

        all_code = "\n".join(task.code)

        for line in task.code:

          line = line.strip()
          comments = ""
          if "#" in line:
            comments = line.split("#")[-1]

          line = line.replace(comments, "")

          if line.startswith("if"):
            if "THEN" not in comments:
              self.comments_check.add(f"Missing selection statement comment in {tn}: {line[:15]}...")    
            if "ENDIF" not in all_code:
              self.comments_check.add(f"Missing selection statement close comment in {tn}: {line[:15]}...")
          elif line.startswith("def") and "__init__" not in line:  
            if "ENDFUNCTION" not in all_code and "ENDPROCEDURE" not in all_code:
              self.comments_check.add(f"Missing subroutine close comment in {tn}: {line[:15]}...")
          elif line.startswith("self."):
            if "DECLARE" not in comments:
              self.comments_check.add(f"Missing record property declaration in {tn}: {line[:15]}...")
          elif line.startswith("class"):
            if "TYPE" not in all_code:
              self.comments_check.add(f"Missing record definition comment in {tn}: {line[:15]}...")
            if "ENDTYPE" not in all_code:
              self.comments_check.add(f"Missing record definition close comment in {tn}: {line[:15]}...")
          elif line.startswith("for"):
            if "TO" not in comments:
              self.comments_check.add(f"Missing count-controlled loop statement comment in {tn}: {line[:15]}...")    
            if "NEXT " not in all_code:
              self.comments_check.add(f"Missing count-controlled loop close comment in {tn}: {line[:15]}...")
          elif line.startswith("while"):
            if "ENDWHILE" not in all_code:
              self.comments_check.add(f"Missing conditional loop close comment in {tn}: {line[:15]}...")

          tokens = line.split()

          for op, rep in inline.items():
            
            if op in tokens and rep not in comments:
              if op == "=" and ("= [" in line or line.startswith("self.") or "INPUT()" in line):  continue
                
              self.comments_check.add(f"Missing {op} operator comment in {tn}: {line[:15]}...")

          



          


    def check_prereqs(self):

      if not USE_LINTER or (not self.comments_check and self.interfaces_check == self.declarations_check and not self.illegal_techniques_check):
        return True

      raise Exception("Functionality can only be checked if you are writing pseudocode-style Python.")

#### SETUP ####

    def setUp(self):
      


      # Add setup code here
      self.ALLOWED_TYPES = "INTEGER,STRING,REAL,BOOLEAN,CHAR,ARRAY,Planet".split(",")
      self.print_log = ''
      illegals = ["."+m+"(" for m in dir(str) + dir(list)] + [f+"(" for f in dir(builtins) + dir(random) + dir(TextIOWrapper)]
      illegals.remove("range(")
      illegals.remove("__init__(")
      illegals += "+=,-=,/=,*=,%=,//=,**,break,continue,finally,True,False".split(",")

      self.illegal_map = {"start":illegals + ['f"', "f''"], "token":"int,bool,str,float,list".split(",")}

      self.illegal_techniques_check = set()
      self.declarations_check = ""
      self.comments_check = set()
      self.interfaces_check = ""

      with open("main.py", encoding="utf-8") as f:
        code = f.read()

      self.task_names = TASKS
      class Task:
        def __init__(self):
          self.task_name = ""
          self.code = []
          self.params = []
          self.declarations = []


      class Variable:
        def __init__(self, p):
          self.name = p.split(":")[0].replace(" ", "")
          self.type = ""
          try:
            self.type = p.split(":")[1].replace(" ", "")
          except IndexError:    pass
        def startswith(self, t):
          return self.name.startswith(t)
        def __contains__(self, t):
          return t in self.name
        def __repr__(self): return self.name


      self.code_by_task = {}

      for task_name in self.task_names:
        new_task = Task()

        
        
        define_sub = "def " + task_name + "("
        define_class = "class " + task_name
        is_class = False
        try:
          code_start = code.index("def " + task_name)
        except:
          try:
            code_start = code.index("class " + task_name)
            is_class = True
          except:
            continue

        for i, line in enumerate(code[code_start:].splitlines()):
          if i == 0:
            if not is_class:
              params = line.strip().replace(define_sub, "")
              for p in params[:params.index(")")].split(","):
                if p.strip():            
                  new_task.params.append(Variable(p))
          elif (line.startswith("def") and "__init__" not in line) or line.startswith("class") or "__main__" in line:  break

          new_task.code.append(line)


        decs = eval(task_name+".__doc__") or ""

        decs = decs.replace("DECLARE ", "")
        for line in decs.splitlines():
          line = line.split(":")[0].strip()
          
          new_task.declarations += [i.strip() for i in line.split(",")]

        

        self.code_by_task[task_name] = new_task



        self.check_interfaces()
        self.check_declarations()
        self.check_for_illegals()
        self.check_comments()


if __name__ == "__main__":

     unittest.main()
