#!/usr/bin/env python
# coding: utf-8

# In[270]:


from qiskit import *
from qiskit.tools.visualization import plot_bloch_multivector, plot_histogram, array_to_latex
from math import pi
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


circuit = QuantumCircuit(2)
#prepare the bell state and distribute qubites
circuit.h(0)
circuit.cx(0, 1)

circuit.barrier()

# Olivia encodes her message and transmites her qubits to barron
match message := '11': #The message
    case '00':
        circuit.id(0)
    case '01':
        circuit.z(0)SSS
    case '10':
        circuit.x(0)
    case '11':
        circuit.z(0)
        circuit.x(0)
        
circuit.barrier()

#Barron decodes Olivia 's  message
circuit.cx(0,1)
circuit.h(0)

#Barron measures the qubits to read Olivia's message
circuit.measure_all()
circuit.draw(output='mpl')


# In[ ]:


simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend=simulator).result()
plot_histogram(result.get_counts())

