import unittest
from pseudocode_problem_set_example import *
# Add imports here

import random
import builtins
import unittest
from io import StringIO, TextIOWrapper
from unittest.mock import patch
NUM_TASKS = 3

# Add initialization code here


class CIEPseudocodeLinter(unittest.TestCase):
    def test_interfaces_check(self):
      # Enter code here

      if self.interfaces_check:
        raise Exception(self.interfaces_check)

      assert self.interfaces_check == ""

    def test_comments_check(self):
      # Enter code here
      if self.comments_check:

        raise Exception(self.comments_check)

      assert self.comments_check == ""

    def test_illegal_techniques(self):
      # Enter code here
   
      
      if self.illegal_techniques_check:

        raise Exception(self.illegal_techniques_check)



      assert self.illegal_techniques_check == ""


    def test_variable_declarations(self):
      # Enter code here
      
      
      if self.declarations_check:

        raise Exception(self.declarations_check)

      assert self.declarations_check == ""


    def redirect_print(self, *args, end="\n", sep=" "):
      self.print_log += sep.join(str(a) for a in args) + end

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
              s = "\n" + f"Illegal pseudocode-style Python technique encountered: {illegal} in {tn} solution."
              self.illegal_techniques_check += s

      for line in task.code:
        if "[" in line and "]" in line:
          var = line.split("[")[0].split()[-1].strip()
          for p in task.params: # TODO + task.locals:

              if p.name == var:
                  if "ARRAY" not in p.type:

                      self.illegal_techniques_check += "\n" + f"Illegal pseudocode-style Python technique encountered: {var}[x] in {tn} solution."

    
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
          if var not in task.declarations and not any(p.startswith(var) for p in task.params):
            self.declarations_check += f"Variable {var} has not been declared.\n"

    def check_interfaces(self):



      for tn, task in self.code_by_task.items():
        
        header = task.code[0]
        return_annotation = ""
        if "->" in header:
          return_annotation = header.split("-> ")[-1].strip()[:-1]
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
                "+ '":"&"
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
              self.comments_check += f"Missing selection statement comment in {tn}: {line[:15]}...\n"    
            if "ENDIF" not in all_code:
              self.comments_check += f"Missing selection statement close comment in {tn}: {line[:15]}...\n"
          elif line.startswith("def"):  
            if "ENDFUNCTION" not in all_code and "ENDPROCEDURE" not in all_code:
              self.comments_check += f"Missing subroutine close comment in {tn}: {line[:15]}...\n"
          elif line.startswith("for"):
            if "TO" not in comments:
              self.comments_check += f"Missing count-controlled loop statement comment in {tn}: {line[:15]}...\n"    
            if "NEXT " not in all_code:
              self.comments_check += f"Missing count-controlled loop close comment in {tn}: {line[:15]}...\n"
          elif line.startswith("while"):
            if "ENDWHILE" not in all_code:
              self.comments_check += f"Missing conditional loop close comment in {tn}: {line[:15]}...\n"
          elif line.startswith("class"):
            if "TYPE" not in comments:
              self.comments_check += f"Missing record structure statement comment in {tn}: {line[:15]}...\n"    
            if "ENDTYPE" not in all_code:
              self.comments_check += f"Missing record structure close comment in {tn}: {line[:15]}...\n"
          tokens = line.split()

          for op, rep in inline.items():
            
            if op in tokens and rep not in comments:
              if op == "=" and "= [" in line:  continue
              self.comments_check += f"Missing {op} operator comment in {tn}: {line[:15]}...\n"

          if len(self.comments_check.splitlines()) > 5:
            self.comments_check += " [truncated]"
            return False


    def check_prereqs(self):

      if self.comments_check == self.interfaces_check == self.declarations_check == self.illegal_techniques_check:
        return True

      raise Exception("Functionality can only be checked if you are writing pseudocode-style Python.")

    def setUp(self):
      # Add setup code here
      self.ALLOWED_TYPES = "INTEGER,STRING,REAL,BOOLEAN,CHAR,ARRAY".split(",")
      self.print_log = ''
      illegals = ["."+m+"(" for m in dir(str) + dir(list)] + [f+"(" for f in dir(builtins) + dir(random) + dir(TextIOWrapper)]
      illegals.remove("range(")
      illegals += "+=,-=,/=,*=,%=,//=,**,break,continue,finally,True,False".split(",")

      self.illegal_map = {"start":illegals + ['f"', "f''"], "token":"int,bool,str,float,list".split(",")}

      self.illegal_techniques_check = ""
      self.declarations_check = ""
      self.comments_check = ""
      self.interfaces_check = ""

      with open("pseudocode_problem_set_example.py", encoding="utf-8") as f:
        code = f.read()

      self.task_names = ["LastLines",
                   "NewLastLines",
                   "Parse",
                   "IsPalindrome",
                   "HomeMadeMid",
                   "GetField1And3",
                   "FindSevens"]

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
        try:
          code_start = code.index("def " + task_name)
        except:
          continue

        for i, line in enumerate(code[code_start:].splitlines()):
          if i == 0:
            params = line.strip().replace(define_sub, "")
            params = [Variable(p) for p in params[:params.index(")")].split(",")]
            new_task.params = params
          elif line.startswith("def"):  break

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
