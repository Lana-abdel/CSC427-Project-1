# reading in the alphabet from txt file
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

print(states)
print()
print(symbols)
print()
print(startState)
print()
print(acceptedStates)
print()
print(transitionTable)
print()

#TODO: probably best to make some sort of class that connects all of this information, then modify the code below so that it can take string values for the various files

def convert_char_to_collumn(symbol,symbols):
  for i in range(0,len(symbols)):
    if symbol == symbols[i]:
      return i
      
def d_recognize(tape,transitionTable,symbols,accepted_states):
  index = 0 
  current_state = startState 
  while True:
    # print(current_state)
    # print(transitionTable[0])
    # print(tape[index])
    # print(symbols)
    # print()
    if index >= len(tape): 
      if current_state in accepted_states:
        return 'accepted'
      else:
        return 'rejected'
    #elif transitionTable[current_state][convert_char_to_collumn(tape[index],symbols)] == "NULL":
      #return 'rejected'
    #else: 
      #current_state = transitionTable[current_state][convert_char_to_collumn(tape[index],symbols)]
      #index += 1 
    else:
      for item in transitionTable:
        if current_state == "NULL":
          return "rejected"
        elif item[0] == current_state and item[1] == tape[index]:
          current_state = item[2]
          index += 1
          break

# tapes = ['baaa!', 'baba', 'baaa', 'baaaaaaa!', 'ba!', 'ababa', "b!", "ba", "baa", "abaaa!", "baa!"] # this line user input 
# for tape in tapes:
#   print(tape +':\t' + d_recognize(tape,transitionTable,symbols,acceptedStates))

while True:
  print("Only input letters in the given alphabet: ", symbols)
  tape = input("Enter a word - Ctrl+C to Exit\n")
  print(d_recognize(tape,transitionTable,symbols,acceptedStates))
  print()
  
