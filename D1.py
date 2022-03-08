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

while True:
  print("Only input letters in the given alphabet: ", symbols)
  tape = input("Enter a word - Ctrl+C to Exit\n")
  print("D1: exact string match: ", d_recognize(tape,transitionTable,acceptedStates))
