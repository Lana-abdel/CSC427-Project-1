import sys
import os

# takes command line input to get directory to desired folder
os.chdir(str(sys.argv[1]))

# reading in the states from txt file
states = []  
with open('states.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        states.append(line)

# reading in the alphabet from txt file
symbols = []  
with open('alphabet.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        symbols.append(line)

# reads input from startState.txt
startState = []
with open('startState.txt', 'r') as f:
    for line in f.readlines():
        startState = line

# reading input from finalStates.txt
acceptedStates = []
with open('finalStates.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        acceptedStates.append(line)

# reading in the transition table from txt file
transitionTable = []
with open('transitionTable.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        line = line.split(',')
        temp = []
        for datavalue in line:
            if datavalue != "NULL":
                datavalue = datavalue
            else:
                datavalue = "NULL"
            datavalue = datavalue[1:-1]
            temp.append(datavalue)
        transitionTable.append(temp) 

'''This function checks input string given by the user. It checks to see if each tape letter is in the alphabet. If it is we create a 
a subtape variable that excludes the first part of the input string that was not in the alphabet and then we call d_Recognize'''
def check_front(tape,transitionTable,symbols,acceptedStates):
  index = 0
  while index < len(tape):
    if tape[index] in symbols:
      sub_tape = tape[index:] 
      return_message = d_recognize(sub_tape,transitionTable,symbols,acceptedStates)

      if return_message == "accepted":
        return "accepted"
    index += 1
  return "rejected" 

'''This function checks input string given by the user. It checks to see if each tape letter is in the alphabet. If it is we create a 
a subtape variable that excludes the first part and the last past of the input string that was not in the alphabet and then we call d_Recognize'''
def check_front_back(tape,transitionTable,symbols,acceptedStates):
  start_index = 0
  end_index = len(tape) - 1
  while start_index < len(tape):
    end_index = len(tape)
    while end_index > start_index:
      sub_tape = tape[start_index:end_index]

      return_message = d_recognize(sub_tape,transitionTable,symbols,acceptedStates)

      if return_message == "accepted":
        return "accepted"

      end_index -= 1
    start_index += 1
  return "rejected"

''' This is the d_recognize function. It returns accept if the entire string it is pointing at is in the language defined by the FSA,
and reject if the string is not in the language.'''   
def d_recognize(tape,transitionTable,symbols,accepted_states):
  index = 0 
  current_state = startState 
  while True:
    if index >= len(tape): 
      if current_state in accepted_states:
        return 'accepted'
      else:
        return 'rejected'

    elif tape[index] not in symbols:
      return "rejected"
    
    else:
      for item in transitionTable:
        if current_state == "NULL":
          return "rejected"
        elif item[0] == current_state and item[1] == tape[index]:
          current_state = item[2]
          index += 1
          break

 ''' Take user input, and print out results for deliverables (D1,D2,D3) 
while True:
  tape = input("Enter a word - Ctrl+C to Exit\n") 

  print("D1: exact string match: ", d_recognize(tape,transitionTable,symbols,acceptedStates))
  print("D2: different start: ", check_front(tape,transitionTable,symbols,acceptedStates))
  print("D3: different start and end: ", check_front_back(tape,transitionTable,symbols,acceptedStates))
  print()
  
