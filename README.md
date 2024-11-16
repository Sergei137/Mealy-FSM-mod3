# Mealy Machine Notes 1

2024-11-15  
Sergei M  



DFA - Deterministic Finite Automata  
NFA - Non-deterministic Finite Automata  

Finite Automata / Finite State Machine / Transducer  

Mealy Machine and Moore Machines are used to show the model and behavior of circuits and diagrams of a computer. Used in basic control and decision making systems.  
Subsets of Turing machines.  
Not Turing complete.  
Limited memory (finite).  



### Moore machine
The Moore machine is named after Edward F. Moore, who presented the concept in a 1956 paper: Gedanken-experiments on Sequential Machines.  

Current output values are determined only by its current state.  
Simple, outputs are tied to states.  



### Mealy machine
The Mealy machine is named after George H. Mealy, who presented the concept in a 1955 paper: A Method for Synthesizing Sequential Circuits.  

Outpute can change immediately in respnse to input.  

Output values are determined by both current state AND current inputs.  
Only up to 1 transition is possible (Transition >= 1).  

A mealy machine has 6 tuples: (Q, q0, ∑, O, δ, λ)
- **Q** is a finite set of states 
- **q0** is the initial state, which is an element of **Q**
- **∑** is the input alphabet (finite set).
- **O** is the output alphabet (finite set).
- **δ : Q * ∑ ==> Q** is a transition function which maps the pairs of a state and an input symbol to the corresponding next state.
- **λ : Q * ∑ ==> O** is an output function that maps the pairs of a state and an input symbol to the corresponding output symbol.

Sometimes the functions are combined into a single function: δ : Q * ∑ ==> Q * λ  



### Binary Brush Up
1 bit == 1 bit  
1 byte == 8 bits  

1 byte can represent 2^8 or 256 different values (0 to 255)  

bit 0 = 2^0 = 1  
bit 1 = 2^1 = 2  
bit 2 = 2^2 = 4  
bit 3 = 2^3 = 8  
bit 4 = 2^4 = 16  
bit 5 = 2^5 = 32  
bit 6 = 2^6 = 64  
bit 7 = 2^7 = 128  

(for binary finger counting method)  
bit 8 = 2^8 = 256  
bit 9 = 2^9 = 512  



### Mealy Machine Binary Modulo 3
Binary division by 3  
Inputs: 0 or 1  
Is output divisible by 3? (remainder is 0)  

Transition rules: transitions (go to) will depend on input and current state.  

State 0:
- If input == 0, remainder does not change (stay in state 0)
- If input == 1, remainder becomes 1 (go to state 1)

State 1: 
- If input == 0, remainder becomes 2 (go to state 2)
- If input == 1, remainder becomes 0 (go to state 0)

State 2: 
- If input == 0, remainder becomes 1 (go to state 1)
- If input == 1, remainder becomes 2 (go to state 2)

Output == 1 when input is divisible by 3 (when state is 0), otherwise output == 0  

Mealy Machine Table:  
| Current State | Input | Next State | Output |
| --- | --- | --- | --- |
| 0 | 0 | 0 | 1 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 2 | 0 |
| 1 | 1 | 0 | 0 |
| 2 | 0 | 1 | 0 |
| 2 | 1 | 2 | 0 |



