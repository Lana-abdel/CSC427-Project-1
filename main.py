# reading in the alphabet from txt file
states = []  
with open('states2.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        states.append(line)

# reading in the alphabet from txt file
symbols = []  
with open('alphabet2.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        symbols.append(line)

# reads input from startState.txt
startState = []
with open('startState2.txt', 'r') as f:
    for line in f.readlines():
        startState = line

# reading input from finalStates.txt
acceptedStates = []
with open('finalStates2.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        acceptedStates.append(line)

# reading in the transition table from txt file
transitionTable = []
with open('transitionTable2.txt', 'r') as f:
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

# tapes = ['baaa!', 'baba', 'baaa', 'baaaaaaa!', 'ba!', 'ababa', "b!", "ba", "baa", "abaaa!", "baa!"] # this line user input 
# for tape in tapes:
#   print(tape +':\t' + d_recognize(tape,transitionTable,symbols,acceptedStates))

while True:
  print("Only input letters in the given alphabet: ", symbols)
  tape = input("Enter a word - Ctrl+C to Exit\n") 

  print("D1: exact string match: ", d_recognize(tape,transitionTable,symbols,acceptedStates))
  print("D2: different start: ", check_front(tape,transitionTable,symbols,acceptedStates))
  print("D3: different start and end: ", check_front_back(tape,transitionTable,symbols,acceptedStates))
  print()
