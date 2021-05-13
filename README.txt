 -----------------------------------------------------------------------
   ___  _   _   _    _   _ _____ _   _ __  __    ____    _  _____ _____ 
  / _ \| | | | / \  | \ | |_   _| | | |  \/  |  / ___|  / \|_   _| ____|
 | | | | | | |/ _ \ |  \| | | | | | | | |\/| | | |  _  / _ \ | | |  _|  
 | |_| | |_| / ___ \| |\  | | | | |_| | |  | | | |_| |/ ___ \| | | |___ 
  \__\_\\___/_/   \_\_| \_| |_|  \___/|_|  |_|  \____/_/   \_\_| |_____|
 -----------------------------------------------------------------------

Quantum Gate is a game designed around resource management & solving quantum circuits. Your aim is to manipulate these circuits into various states, and manipulate probability in your favor.

Quantum Gate utilizes the Qiskit programming language in order to display these circuits. Qiskit, and various functions created for the game allow various inputs for the player.

In order to run this program, open and run 'Game_Test.py' in your IDE of choice (NOTE: if you run the program in a Jupyter Notebook, it may stop working if Qiskit updates).

---------
OPERATORS
---------
The most basic input is adding operators to a circuit. Speaking broadly, there are three types of operators the circuit can accept.

1. Operators which act on one qubit and take only a positional argument. An example of this is the Hadamard operator. To place a Hadamard operator on a circuit, input h, then the qubit you want the gate to act on.

-----------
h             
0
     ┌───┐
q_0: ┤ H ├
     └───┘
q_1: ─────

c: 2/═════
-----------

Other operators in this category include x, y, z, & reset.


2. Operators which act on both qubits, or on one qubit while placed on another. An example of this is the Controlled Not operator. To place a Controlled Not operator on qbit 0 acting on qubit 1, input cx, then 0, 1.

-----------
cx
0, 1

q_0: ──■──
     ┌─┴─┐
q_1: ┤ X ├
     └───┘
c: 2/═════
-----------

The only other operator in this category is swap.


3. Operators which act on one qubit, but act as rotational operators. An example of this is the general unitary matrix U. To place a U matrix on a circuit, type u, then input the parameters followed by the qubit you wish the operator to act on.

-------------------------
u
1*pi/2, 1*pi/2, 1*pi/2, 0

     ┌────────────────┐
q_0: ┤ U(π/2,π/2,π/2) ├
     └────────────────┘
q_1: ──────────────────

c: 2/══════════════════
-------------------------

Other operators in this category include rx, ry, and rz, though these only take 1 positional argument.

----------------
rx
1*pi/2, 0

     ┌─────────┐
q_0: ┤ RX(π/2) ├
     └─────────┘
q_1: ───────────

c: 2/═══════════
----------------

HINT: These rotation operators are the best way to manipulate the probabilities in your superposition.

You begin the game with a limited number of operators. When you use an operator, the game will print how many of that operator you have left. What happens if you run out will be discussed below.

-----
CHECK
-----
The next operation available to you is the Check function. Once you are satisfied with the circuit you have constructed, type 'check' into the command line, then '0', and the function will check the state of your circuit against the expected one.

-----------------------------------------------
check
0
The state you entered was [1, 0.0, 0.0, 1] ...
...and the correct state is [1, 0.0, 0.0, 1]
Congrats, you have solved the circuit!


Measuring circuit...


The result is: 00
-----------------------------------------------

If your circuit is incorrect, you will be returned to it and prompted to try again. If it is correct, what happens next depends on the circuit's output. If the circuit returns the state |00>, all the gates you used on that circuit will be returned to you. If not, you will have to make due with what you have left. Therefore, it is in your best interest to manipulate the probabilities of the states, so you are more likely to get your operators back. If you run out of operators, you must face the dreaded...

----
GRUE
----
The 'Quantum Grue' is the creature chasing you as you attempt to escape. It will attack you if you completely run out of operators. It is represented by a harder quantum circuit. Unlike the regular circuits, which ask you to manipulate the qubits into a certain arrangement, when fending off the Grue your only concern is returning the |00> state, by any means necessary. No matter what the Grue circuit returns, you get some operators back and return to the original circuit. But if it returns a state other than |00>, you lose some health. If your health reaches zero, it's Game Over.

If you run out of a crucial gate, but aren't completely depleted, you can input 'grue', then '0', to wait for the Grue to catch you and regain some operators the hard way.

-----------------------------------------
grue
0
The Grue has caught you! Defend yourself!
     ┌───┐
q_0: ┤ H ├
     ├───┤
q_1: ┤ X ├
     └───┘
c: 2/═════
-----------------------------------------

Each time the Grue faces you, it will present you with a new, harder circuit, so stay on your toes and manage your operators wisely...

NOTE: While the Grue function will iterate each time it is called, currently it will not end your game if your health reaches zero. So if this happens, just use the honor system and pretend that you've been killed.

----
UNDO
----
The final input you can use is the undo function. This will remove a previously applied gate from the circuit, and return you one use of that gate.

----------
h
0
     ┌───┐
q_0: ┤ H ├
     └───┘
q_1: ─────

c: 2/═════

undo
1

q_0:

q_1:

c: 2/
----------

--------------------------
CREATING YOUR OWN CIRCUITS
--------------------------
With the code already in place, creating your own circuits is easy. On line 45 of 'Easy.py' you will find the place in the Easy_First() function where the Check function is called. One of its arguments is the following.

[0.707+0j, 0+0j, 0+0j, 0.707+0j]

This represents the Bell State, 1/(√2)*(|00> + |11>). Let's say you wanted a player to create a circuit in the state α|00> + β|10>. Qiskit represents this state as the following.

[0.707+0j, 0+0j, 0.707+0j, 0+0j] (The 0.707 represents 1/(√2), but the values of α & β really aren't important).

Simply replace the Bell state with the above and the Check function will do the rest, matching the new state against whatever you input. You can also update the print statement at the beginning of the function to represent your new state. If you're unsure how to represent a certain state in this format, you can create the state on the IBM Quantum Experience website, and the "statevector" tab will tell you its representation. This is also a good way to determine a solution to your circuit.

If you want your circuit to start with operators on it, you can edit the circuit before it is called in the function. If you read the above section on operators, the syntax for this should be fairly clear. For instance, if you're still working on circuit1, the circuit used in Easy_First(), it is defined on line 9 of 'Easy.py'. If you want this circuit to start with a H operator on qubit 1, and a CX operator on qubit zero, acting on qubit one, insert the following lines.

-----------------------------------------------------------------
circuit1 = QuantumCircuit(2, 2) #defining a blank quantum circuit
circuit1.h(1)
circuit.cx(0, 1)
-----------------------------------------------------------------

Now when you run Easy_First(), circuit1 will start as the following.

---------------
q_0: ───────■──
     ┌───┐┌─┴─┐
q_1: ┤ H ├┤ X ├
     └───┘└───┘
c: 2/══════════
---------------



Currently, the program only supports two-qubit systems, but it is possible to generalize it.