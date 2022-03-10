# CSC427-Project-1 
## Authors: Lana Abdelmohsen, Michael Giordano, Joseph Carmichael, Rebecca Goldberg 
## Description 
An implementation of the D-recognize algorithm 
### What you will find  
- main.py: Our main source code for the d_recognize algorithm (prints out D1, D2, D3) 
    - code description: 
        - The code takes as input a finite state machine and a string. 
        - It then calls three functions:
            - d_recognize (...): which takes the transitionTable, the symbols, the accepted_states, the startState, and the tape inputted by the user as parameters. It will output "accepted" if the machine accepts the string and "rejected" otherwise. This covers the D1 deliverable 
            - check_front (...): takes in the same parameters as d_recognize. It will detect matches in a string where the match is not necessarily correct at the beginning of the string. 
            - check_front_back: takes in the same parameters as d_recognize. It will detect matches even if there are more characters in the string after the matching part.
- Two sub-folders 

    1. sheep: Where the sheep language machine txt files are located and include the following files: 
    2. great: This is where you will find the txt files for our own machine. It accepts the words "great!" or "Greater!" or "Greatest" (D4)
        - For our new machine, our regex language would be: (great!|greater!|greatest!) 
 
    - inside each folder, you will find: 
        - states.txt - each line containing a string identifying a state in the machine (in the format: q0,q1,...,) 
        - alphabet.txt - each line containing a character in the alphabet
        - startState.txt - a one-line file containing the start-state
        - finalStates.txt - each line containing the name of a state that is a final (accepting) state
        - transitionTable.txt - each line containing “stateID1” , “symbol” , “stateID2” 
           meaning that when in "stateID1" and reading "symbol"
           from the input string, the machine transitions to "stateID2". If
           there is no transition, then the string "NULL" is used to indicate that.
- D5.pdf: a pdf file that responds to the following questions: 
    - What was easy about this assignment?
    - What was challenging about this assignment or parts that you couldn't get working correctly?
    - What did you like about this assignment?
    - What did you dislike about this assignment?
    - How did your team function? Include details regarding what each team
      member contributed, how the team communicated with each other, and
      how team software development & design was accomplished. 
    - What did you learn from this assignment? 
### Instructions for command line 

1. on OnDemand, go to your file Home Directory and upload "main.py". Then in the HPC terminal enter: 
>
> module add python 
> 
> python main.py path
>

(the path, is where the machine files are located for example ./sheep) 
