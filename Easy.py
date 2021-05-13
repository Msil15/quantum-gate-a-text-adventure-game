from time import sleep
from qiskit import(
  QuantumCircuit,
  assemble,
  execute,
  Aer)
from Functions import Convert, op_match, Check, Undo, Grue_Attack

circuit1 = QuantumCircuit(2, 2) #defining a blank quantum circuit

circuit2 = QuantumCircuit(2, 2)

circuit3 = QuantumCircuit(2, 2)

simulator = Aer.get_backend('qasm_simulator') #use Aer's simulated quantum computer to run circuits
svsim = Aer.get_backend('statevector_simulator') # tell Qiskit how to simulate our circuit

operator_list = ['h', 'cx', 'x', 'y', 'z', 'rx', 'ry', 'rz', 'u', 'reset', 'swap'] #list of quantum operators
operator_count = [5, 2, 3, 3, 3, 3, 3, 3, 2, 17, 2]
stored_inputs = []

new_operator_count = [5, 2, 3, 3, 3, 3, 3, 3, 2, 1, 2]

def Easy_First():
    print("Circuit 1: Manipulate this circuit so it is in the Bell state (α|00> + β|11>)")
    print("")
    print(circuit1)
    global operator_count
    while True:
        #the function asks for an operator, and which qbit it operates on
        operator = input()
        qbit = input()
        qbit = Convert(qbit) #Convert the qbit value to a list...
        if qbit == 'incorrect': #check with the convert function if a correct value (0 or 1) has been entered
            continue

        if operator in operator_list:
            op_match_output = op_match(operator, operator_count, operator_list)
            if op_match_output == True:
                getattr(circuit1, operator)(*qbit) #...and use each value in the list as an argument for the operator
                qobj = assemble(circuit1)
                state_actual = svsim.run(qobj).result().get_statevector()
                state_real = state_actual.real
                print(circuit1)
                print('The circuit is in the state', state_real)
                stored_inputs.append(operator)
            elif op_match_output == new_operator_count:
                print(new_operator_count)
                operator_count = new_operator_count
        elif operator == 'check':
            #calling the check function w/ the Bell State (|00> and |11>) as input
            if Check(circuit1, [0.707+0j, 0+0j, 0+0j, 0.707+0j], operator_count, operator_list, stored_inputs):
                print("You have", operator_count, "gates remaining")
                print("")
                print("")
                Easy_Second()
            else:
                pass
        elif operator == 'undo':
            Undo(qbit[0], circuit1, stored_inputs, operator_count, operator_list)
            print(circuit1)
        elif operator == 'grue':
            Grue_Attack(operator_count, operator_list)
        else:
            print("That is not a valid gate")
            continue

def Easy_Second():
    new_stored_inputs = []
    stored_inputs = new_stored_inputs
    print("Circuit 2: Manipulate this circuit so it is in the state α|00> + β|10>")
    print("")
    print(circuit2)
    while True:
        #the function asks for an operator, and which qbit it operates on
        operator = input()
        qbit = input()
        qbit = Convert(qbit) #Convert the qbit value to a list...
        if qbit == 'incorrect':
            continue

        if operator in operator_list:
            if op_match(operator, operator_count, operator_list) == True:
                getattr(circuit2, operator)(*qbit) #...and use each value in the list as an argument for the operator
                qobj = assemble(circuit2)
                state_actual = svsim.run(qobj).result().get_statevector()
                state_real = state_actual.real
                print(circuit2)
                stored_inputs.append(operator)
            else:
                pass
        elif operator == 'check':
            if Check(circuit2, [0.707+0j, 0+0j, 0.707+0j, 0+0j], operator_count, operator_list, stored_inputs):
                print("You have", operator_count, "gates remaining")
                print("")
                print("")
                Easy_Third()
            else:
                pass
        elif operator == 'undo':
            Undo(qbit[0], circuit2, stored_inputs, operator_count, operator_list)
            print(circuit2)
        elif operator == 'grue':
            Grue_Attack(operator_count, operator_list)
        else:
            print("That is not a valid gate")
            continue

def Easy_Third():
    new_stored_inputs = []
    stored_inputs = new_stored_inputs
    print("Circuit 3: Manipulate this circuit so it *only* returns the |00> state.")
    print("")
    print(circuit3)
    while True:
        #the function asks for an operator, and which qbit it operates on
        operator = input()
        qbit = input()
        qbit = Convert(qbit) #Convert the qbit value to a list...
        if qbit == 'incorrect':
            continue

        if operator in operator_list:
            if op_match(operator, operator_count, operator_list) == True:
                getattr(circuit3, operator)(*qbit) #...and use each value in the list as an argument for the operator
                qobj = assemble(circuit3)
                state_actual = svsim.run(qobj).result().get_statevector()
                state_real = state_actual.real
                print(circuit3)
                stored_inputs.append(operator)
            else:
                pass
        elif operator == 'check':
            if Check(circuit3, [0.707+0j, 0+0j, 0+0j, 0+0j], operator_count, operator_list, stored_inputs):
                Victory_file = open("Victory.txt")
                
                lines = Victory_file.readlines()

                for line in lines:
                    print(line, end="")
                    sleep(0.3)
            else:
                pass
        elif operator == 'undo':
            Undo(qbit[0], circuit3, stored_inputs, operator_count, operator_list)
            print(circuit3)
        elif operator == 'grue':
            Grue_Attack(operator_count, operator_list)
            print(circuit3)
        else:
            print("That is not a valid gate")
            continue
