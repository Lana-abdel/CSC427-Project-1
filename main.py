# reading in the transition table from txt file
transitionTable = []
with open('transitionTable.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        line = line.split(',')
        temp = []
        for datavalue in line:
            if datavalue != "NULL":
                datavalue = int(datavalue)
            else:
                datavalue = "NULL"
            temp.append(datavalue)
        transitionTable.append(temp)

# reading in the alphabet from txt file
symbols = []  
with open('alphabet.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        symbols.append(line)

# reading input from finalStates.txt
acceptedStates = []
with open('finalStates.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        acceptedStates.append(int(line))

# make this read input from startState.txt
startState = []
with open('startState.txt', 'r') as f:
    for line in f.readlines():
        startState = int(line)

def convert_char_to_collumn(symbol,symbols):
  for i in range(0,len(symbols)):
    if symbol == symbols[i]:
      return i
      
def d_recognize(tape,transitionTable,symbols,accepted_states):
  index = 0 
  current_state = startState 
  while True:
    if index >= len(tape):
      if current_state in accepted_states:
        return 'accepted'
      else:
        return 'rejected'
    elif transitionTable[current_state][convert_char_to_collumn(tape[index],symbols)] == "NULL":
      return 'rejected'
    else: 
      current_state = transitionTable[current_state][convert_char_to_collumn(tape[index],symbols)]
      index += 1 

tapes = ['baaa!', 'baba', 'baaa', 'baaaaaaa!', 'ba!', 'ababa', "b!", "ba", "baa"] # this line user input 
for tape in tapes:
  print(tape +':\t' + d_recognize(tape,transitionTable,symbols,acceptedStates))
