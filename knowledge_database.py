turists_dictinary = {
  "L": "is a loonie",
  "S": "is a saturnian",
  "P": "is a human",
  "M": "is marsian",
  "N": "is neptunian",
  "V": "is venusian"
}

knowledge_dictionary = {
  "A": "has big body",
  "B": "has big head",
  "C": "has long legs",
  "D": "has normal body",
  "F": "has big eyes",
  "H": "has small nose",
  "W": "has ultrasonic ability",
  "J": "has antenna",
}

fact_dictionary = {
  "I": "has purple skin",
  "O": "has orange hair",
  "K": "has long ears",
  "X": "has four ears",
  "Q": "has big shoes",
  "R": "has jeans",
  "T": "has white skin",
  "Y": "has two legs",
  "U": "has big fingers",
  "1": "has red eyes",
  "4": "has blue skin",
  "5": "has blue eyes",
  "6": "has a long neck",
  "7": "has four hands"
}

rules = [
  "I|O=A",
  "K+X=B",
  "A+B=L",
  "Q+R=C",
  "B+C=S",
  "T+Y=D",
  "D+C=P",
  "U|1=F",
  "2|3=E",
  "6+7=J",
  "4|5=W",
  "5+7=H",
  "F+D=M",
  "H+W=N",
  "J+H=V"
]