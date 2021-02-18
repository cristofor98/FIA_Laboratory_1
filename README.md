# Expert system
> This is a expert system that helps to detect tourists that are in Luna city,

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [How to run](#setup)
* [Code Examples](#features)
* [Example of usage](#status)
* [Contact](#contact)

## General info
Expert system is a program that will allow by asking some question to determine what type of tourist is in the user's head. First you need to collect a database of facts about each type of tourist so this will be our knowledge_database and this help out system base on this facts and rules to determine what type of tourist is that persone. 

## Technologies
* Python 3.8.2

## How to run
$ python lab1.py

## Code Examples
Rule example: 

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

facts example:

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

## Example of usage

![Example screenshot](./img/screenshot.png)


## Contact
Created by @cristofor98
