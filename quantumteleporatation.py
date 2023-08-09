#!/usr/bin/env python
# coding: utf-8

# In[502]:


from qiskit import *
from qiskit.tools.visualization import plot_bloch_multivector, plot_histogram
from math import pi
get_ipython().run_line_magic('matplotlib', 'inline')


# In[503]:


#Initialize 3-qubit circuit with named registers 
q0 = QuantumRegister(1, name="q0") #Olivia's source qubit to teleport 
q1 = QuantumRegister(1, name="q1") #Middle qubit send to olivia(half of bell state pair)
q2 = QuantumRegister(1, name="q2") #Barron's destination qubit (half of bell state pair)

crz = ClassicalRegister(1, name="crz") #Olivia's measurement of her source qubit
crx = ClassicalRegister(1, name="crx") #Olivia's measurment of middle qubit(half of bell state)

circuit = QuantumCircuit(q0, q1, q2, crz, crx)

#initialize olivia's qubit (quantum state to teleport)
circuit.x(0)
circuit.barrier()

#Create Bell state pair
circuit.h(q1)
circuit.cx(q1, q2)
circuit.barrier()

#Olivia performs Bell state measurement
circuit.cx(q0, q1)
circuit.h(q0)
circuit.barrier()
circuit.measure(q0, crz)
circuit.measure(q1, crx)
circuit.barrier()

#Barron transforms his based on measurement results
circuit.x(q2).c_if(crx, 1) # apply X gate if cr_x is 1
circuit.z(q2).c_if(crz, 1) #apply Z gate if cr_z is 1

circuit.draw(output='mpl')


# In[504]:


simulator = Aer.get_backend('statevector_simulator')
statevector = execute(circuit, backend=simulator).result().get_statevector()
plot_bloch_multivector(statevector)


# In[508]:


# add final measurement of barron's qubit
cr_result = ClassicalRegister(1, name="result")
circuit.barrier()
circuit.add_register(cr_result)
circuit.measure(2,2)
circuit.draw(output='mpl')


# In[509]:


simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend=simulator).result()
plot_histogram(result.get_counts())


# In[512]:


#quantum teleportation circuit using deferred measaurement 
circuit_def = QuantumCircuit(3,1)

#initialize Olivia's qubit (quantum state to teleport)
circuit_def.x(0)
circuit_def.barrier()


# In[ ]:





# In[ ]:




