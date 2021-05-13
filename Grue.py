from qiskit import(
  QuantumCircuit,
  assemble,
  execute,
  Aer)
import numpy as np

simulator = Aer.get_backend('qasm_simulator') #use Aer's simulated quantum computer to run circuits
svsim = Aer.get_backend('statevector_simulator') # tell Qiskit how to simulate our circuit

def Convert(string): #a function to convert a string to a list
    int_list = []
    li = list(string.split(", "))
    for bit in li:
        try:
            if 'pi' in bit: #since input() makes the input a string, the pi must be removed, then added back in
                unstrung_bit = bit
                numerator = float(unstrung_bit.split('*')[0])
                denominator = float(unstrung_bit.split('/')[1]) 
                unstrung_bit = numerator * np.pi/denominator
                int_list.append(unstrung_bit)
            else:
                unstrung_bit = int(bit)
                int_list.append(unstrung_bit)
        except ValueError:
            print("That is not a valid position...")
            return 'incorrect'

        
    return int_list

grue_operator_count = [5, 2, 3, 3, 3, 3, 3, 3, 2, 1, 2]

def grue_check(circuit):
    circuit.measure([0,1], [0,1])
    job = execute(circuit, simulator, shots = 1001) #execute the circuit on the qasm simulator
    result = job.result() #grab results from the job
    counts = result.get_counts(circuit)
    print(counts)
    answer = counts.most_frequent()
    print("The result is:", answer)
    if answer == '00':
        return True
    else:
        return False

def grue_match(op, operator_list):
    count = grue_operator_count[operator_list.index(op)]

    count_index = int(operator_list.index(op))

    if count == 0:
        print('You are out of ' + str(op) + ' gates!')
        return False
    else:
        count_new = count - 1
        grue_operator_count.pop(count_index)
        grue_operator_count.insert(count_index, count_new)
        print('You have ' + str(count_new) + ' ' + str(op) + ' gates remaining')
        return True

grue_circuit1 = QuantumCircuit(2, 2)
grue_circuit1.h(0)
grue_circuit1.x(1)


grue_circuit2 = QuantumCircuit(2, 2)
grue_circuit2.x(0)
grue_circuit2.y(1)

i = 0

def Grue_Attack(operator_count, operator_list):
    new_operator_count = [5, 2, 3, 3, 3, 3, 3, 3, 2, 1, 2]
    health = 3
    global i
    i += 1
    if i == 1:
        print("The Grue has caught you! Defend yourself!")
        print(grue_circuit1)
        while True:
            operator = input()
            qbit = input()
            qbit = Convert(qbit) #Convert the qbit value to a list...
            if qbit == 'incorrect':
                continue

            if operator in operator_list:
                if grue_match(operator, operator_list) == True:
                    getattr(grue_circuit1, operator)(*qbit) #...and use each value in the list as an argument for the operator
                    print(grue_circuit1)
                else:
                    pass
            elif operator == 'check':
                print("Measuring circuit...")
                print("")
                if grue_check(grue_circuit1) == True:
                    print("You have fended off the Grue, this time...")
                else:
                    print("You manage to push the Grue back, but not before it slashes your arm. You can't take much more of that...")
                    health = health - 1
                    print("Your health is now", health)
                print('You now have ', new_operator_count, 'operators remaining')
                operator_count = new_operator_count
                return operator_count
                break

    if i == 2:
        print("The Grue has caught you! Defend yourself!")
        print(grue_circuit2)
        while True:
            operator = input()
            qbit = input()
            qbit = Convert(qbit) #Convert the qbit value to a list...
            if qbit == 'incorrect':
                continue

            if operator in operator_list:
                if grue_match(operator, operator_list) == True:
                    getattr(grue_circuit2, operator)(*qbit) #...and use each value in the list as an argument for the operator
                    print(grue_circuit2)
                else:
                    pass
            elif operator == 'check':
                new_operator_count = [5, 2, 3, 3, 3, 3, 3, 3, 2, 4, 2]
                print("Measuring circuit...")
                print("")
                if grue_check(grue_circuit2) == True:
                    print("You have fended off the Grue, this time...")
                else:
                    print("You manage to push the Grue back, but not before it slashes your arm. You can't take much more of that...")
                    health = health - 1
                    print("Your health is now", health)
                operator_count = new_operator_count
                print('You now have ', operator_count, 'operators remaining')