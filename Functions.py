import numpy as np
import collections
from Grue import Grue_Attack, Convert
from qiskit import(
  QuantumCircuit,
  assemble,
  execute,
  Aer)

simulator = Aer.get_backend('qasm_simulator') #use Aer's simulated quantum computer to run circuits
svsim = Aer.get_backend('statevector_simulator') # tell Qiskit how to simulate our circuit

def op_match(op, operator_count, operator_list):
    count = operator_count[operator_list.index(op)]

    count_index = int(operator_list.index(op))

    if sum(operator_count) == 0:
        operator_count = Grue_Attack(operator_count, operator_list)
        update = operator_count
        return update
    elif count == 0:
        print('You are out of ' + str(op) + ' gates!')
        return False
    else:
        count_new = count - 1
        operator_count.pop(count_index)
        operator_count.insert(count_index, count_new)
        print('You have ' + str(count_new) + ' ' + str(op) + ' gates remaining')
        return True


def Check(circuit, state_correct, operator_count, operator_list, stored_inputs): #this function checks if the user-created state matches the expected one.
    qobj = assemble(circuit)
    state_actual = svsim.run(qobj).result().get_statevector()
    
    numpy_state_correct = np.asarray(state_correct)
    numpy_state_actual = np.asarray(state_actual)

    state_actual_real = numpy_state_actual.real #removing complex componant so they are easier to compare.
    state_correct_real = numpy_state_correct.real

    normalized_state_actual = [] #'normalizing' the states so they match even if the probabilities are different.
    for state in state_actual_real:
        if state == 0: 
            pass
        else:
            state = 1
        normalized_state_actual.append(state)

    normalized_state_correct = []
    for state in state_correct_real:
        if state == 0: 
            pass
        else:
            state = 1
        normalized_state_correct.append(state)

    print("The state you entered was", normalized_state_actual, "...")
    print("...and the correct state is", normalized_state_correct)
    i = 1
    while i < 4: #checking if each position of the correct state matches the corrusponding position for the input state
        similar_list = []
        similar = normalized_state_correct[i] - normalized_state_actual[i]
        similar_list.append(similar)
        if similar == 0:
            i = i + 1
        else:
            print("This circuit is not correct")
            print(circuit)
            break

    if sum(similar_list) == 0:
        print("Congrats, you have solved the circuit!")

        circuit.measure([0,1], [0,1])

        print("")
        print("")
        print("Measuring circuit...")
        print("")
        print("")

        job = execute(circuit, simulator, shots = 1001) #execute the circuit on the qasm simulator
        result = job.result() #grab results from the job
        counts = result.get_counts(circuit)
        answer = counts.most_frequent()
        print("The result is:", answer)
        if answer == '00':
            print('You got your gates back!')
            operators_and_amounts = collections.Counter(stored_inputs)
            values = np.array(list(operators_and_amounts.items()))
            operators = [sublist[0] for sublist in values]
            amounts = [sublist[-1] for sublist in values]

            j = -1

            for operator in operators:
                j = j + 1
                new_index = operator_list.index(operator)
                new_value = operator_count[new_index] + int(amounts[j])
                operator_count.pop(new_index)
                operator_count.insert(new_index, new_value)

        else:
            print("")
            print('Better luck next time!')

        return True
    
    else:
        return False


def Undo(n, circuit, stored_inputs, operator_count, operator_list):
    circuit.data.pop(n-1)
    gate = stored_inputs[n-1]
    old_count = operator_count[operator_list.index(gate)]
    new_count = old_count + 1
    count_index = int(operator_list.index(gate))
    operator_count.pop(count_index)
    operator_count.insert(count_index, new_count)
    print('You have ' + str(new_count) + ' ' + str(gate) + ' gates remaining')