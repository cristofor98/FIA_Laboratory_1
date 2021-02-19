import random
import knowledge_database
from anytree import Node, RenderTree
import sys


def ask_first_question(fact_dictionary):
   check_remain_questions()
   subject = random.choice(list(fact_dictionary.values()))
   key = get_key(subject,knowledge_database.fact_dictionary)
   if check_if_have_sens_question(key):
    answer = question(subject)
   else:
    answer = "no"
   if answer.lower() == "yes":
    value = True 
    current_facts.append(key)
    delete_question(key)
    expresion,result = find_rule(key)
    rule_value = verify_expresion(expresion,value,key)
    if rule_value == True:
      current_knoledge[result] = knowledge_database.knowledge_dictionary.get(result)
    verify_knowledge(result)
   elif answer.lower() == "no":
    value = False
    delete_question_with_pair(key)
    ask_first_question(remain_questions)
   else:
    print("not writing respons in correct format")


def backward_chaining():
  print("Choose type of tourist")
  for i in knowledge_database.turists_dictinary:
    print(i, knowledge_database.turists_dictinary[i])
  print("Type just the letter of type of tourist")
  answer = input()
  if answer.upper() in knowledge_database.turists_dictinary:
    expresion = find_component(answer.upper())
    if "+" in expresion:
      left_knowledge,right_knowledge = expresion.split("+")
      facts = []
      left_fact, right_fact = decompose_rule(left_knowledge)
      if left_fact not in facts:
        facts.append(left_fact)
      if right_fact not in facts:  
        facts.append(right_fact)
      left_fact, right_fact = decompose_rule(right_knowledge)
      if left_fact not in facts:
        facts.append(left_fact)
      if right_fact not in facts:  
        facts.append(right_fact)
      for i in range(len(facts)):
       fact_info = knowledge_database.fact_dictionary.get(facts[i])
       print(fact_info)
  else: 
    print("not writing respons in correct format")  

def decompose_rule(key):
    expresion = find_component(key)
    if "+" in expresion:
      left_part,right_part = expresion.split("+")
      return left_part,right_part
    if "|" in expresion:
      left_part,right_part = expresion.split("|")
      return left_part,right_part


def verify_knowledge(key):
    left_part,right_part = find_rule(key)
    if "+" in left_part:
      left_knowledge,right_knowledge = left_part.split("+")
      if left_knowledge != key :
         expresion = find_component(left_knowledge)
         if "+" in expresion:
           left_fact,right_fact = expresion.split("+")
           answer_left_fact = verify_known_facts(left_fact)
           answer_right_fact = verify_known_facts(right_fact)
           if answer_right_fact == answer_left_fact == True:
             result = knowledge_database.turists_dictinary.get(right_part)
             print(result)
           else: 
             print("did not found such turist type")
         if "|" in expresion:
           left_fact,right_fact = expresion.split("|")
           answer_left_fact = ask_question(left_fact)
           if answer_left_fact == True:
            result = knowledge_database.turists_dictinary.get(right_part)
            print(result)
           answer_right_fact = ask_question(right_fact)
           if answer_right_fact == True:
            result = knowledge_database.turists_dictinary.get(right_part)
            print(result)
      elif right_knowledge != key:    
            fint_answer(right_knowledge,right_part)

def fint_answer(left_knowledge,right_part):
         expresion = find_component(left_knowledge)
         if "+" in expresion:
           left_fact,right_fact = expresion.split("+")
           answer_left_fact = verify_known_facts(left_fact)
           answer_right_fact = verify_known_facts(right_fact)
           if answer_right_fact == answer_left_fact == True:
             result = knowledge_database.turists_dictinary.get(right_part)
             print(result)
           else: 
             print("did not found such turist type")
         if "|" in expresion:
           left_fact,right_fact = expresion.split("|")
           answer_left_fact = ask_question(left_fact)
           if answer_left_fact == True:
            result = knowledge_database.turists_dictinary.get(right_part)
            print(result)
           answer_right_fact = ask_question(right_fact)
           if answer_right_fact == True:
            result = knowledge_database.turists_dictinary.get(right_part)
            print(result)

def ask_questions():
  subject = random.choice(list(remain_questions.values()))
  answer = question(subject)

def find_component(key):
  check = set(key)
  for rule in knowledge_database.rules:
    if check & set(rule):
      left_part,right_part = rule.split('=')
      if check_rule(right_part,key):
        return   
      return left_part


def delete_question(key):
  check_remain_questions()
  if key in remain_questions:
    remain_questions.pop(key)


def find_fact_by_rule(key):
   expresion,result = find_rule(key)
   if "|" in expresion:
    left_fact,right_fact = expresion.split("|")
    if left_fact != key:
      return False,left_fact,result
    elif right_fact != key:
      return False,right_fact,result
   if "+" in expresion:
    left_fact,right_fact = expresion.split("+")
    if left_fact != key:
      return True,left_fact,result
    elif right_fact != key:
      return True,right_fact,result

def delete_question_with_pair(key):
  if key in remain_questions:
   check_remain_questions()
   statement,second_key,result = find_fact_by_rule(key)
   delete_question(key)
   if statement:
    if check_if_not_have_another_rule(key):
     delete_question(second_key)
     second_knowledge = find_knowledge(result)
     expresion = find_component(second_knowledge)
     if "+" in expresion:
      left_fact,right_fact = expresion.split("+")
     elif "|" in expresion:
      left_fact,right_fact = expresion.split("|")
     if left_fact not in [key,second_key]:
      delete_question_with_pair(left_fact)
     elif right_fact not in [key,second_key]:
      delete_question_with_pair(right_fact) 

def check_if_have_sens_question(key):
  statement,second_key,result = find_fact_by_rule(key)
  second_knowledge = find_knowledge(result)
  expresion = find_component(second_knowledge)
  if "+" in expresion:
     left_fact,right_fact = expresion.split("+")
     if left_fact and right_fact in remain_questions:
      return True
  elif "|" in expresion:
     left_fact,right_fact = expresion.split("|")
     if left_fact or right_fact in remain_questions:
      return True
  else:
    return False

def check_if_not_have_another_rule(key):
  statement,second_key,result = find_fact_by_rule(key)
  second_knowledge = find_knowledge(result)
  third_knowledge = find_knowledge(second_knowledge)
  if third_knowledge not in [second_knowledge,result]:
    return False
  else:
    return True

def find_knowledge(knowledge):
  left_part,right_part = find_rule(knowledge)
  if "+" in left_part:
    left_knowledge,right_knowledge = left_part.split("+")
    if left_knowledge != knowledge:
      return left_knowledge
    elif right_knowledge != knowledge:
      return right_knowledge

def check_remain_questions():
  if len(remain_questions) == 0:
     print("you respond to all question but we cann't find any turist with this description")
     sys.exit()

def find_rule(key):
  check = set(key)
  for rule in knowledge_database.rules:
    if check & set(rule):
      left_part,right_part = rule.split('=')
      if check_rule(right_part,key):
         return left_part,right_part
      
def check_rule(right_part,key):
  if right_part == key:
   return False
  else:
   return True

def question(subject):
   question = "This person " + subject + " ?"
   print(question)
   answer = input()
   return answer  

def verify_known_facts(fact):
   if fact in current_facts:
    return True
   else:
    answer_fact = ask_question(fact)
    return answer_fact

def ask_question(key):
    subject = remain_questions.get(key)
    print(subject)
    answer = question(subject) 
    if answer.lower() == "yes":
      node_value = True
      current_facts.append(key)
      delete_question(key) 
      return node_value
    elif answer.lower() == "no":
      node_value = False
      delete_question(key)
      return node_value 
    else:
      print("not writing respons in correct format")


def verify_expresion(expresion,value,key):
    if "|" in expresion:
      left_fact,right_fact = expresion.split("|")
      return value
    if "+" in expresion:
      left_fact,right_fact = expresion.split("+")
      if left_fact != key:
        value = ask_question(left_fact)
        return value
      else:
        value = ask_question(right_fact)
        return value

def get_key(val,my_dict):
    for key, value in my_dict.items():
         if val == value:
             return key
    return "key doesn't exist"
 
current_knoledge = {}
current_facts = []
remain_questions = knowledge_database.fact_dictionary.copy()
print("Do you whan forward chaining or backward chaining ? (Type forwards for foward chaining or backwards for backward chaining)")
response = input()
if response.lower() == "backward":
  backward_chaining()
elif response.lower() == "forward":  
  ask_first_question(knowledge_database.fact_dictionary)
else:
  print("not writing respons in correct format")
