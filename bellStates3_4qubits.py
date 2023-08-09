#!/usr/bin/env python
# coding: utf-8

# In[270]:


from qiskit import *
from qiskit.tools.visualization import plot_bloch_multivector, plot_histogram, array_to_latex
from math import pi
get_ipython().run_line_magic('matplotlib', 'inline')


# In[298]:


#Bell States with four qubits
circuit = QuantumCircuit(4)
circuit.h(0)
circuit.cnot(0,1) 
circuit.cnot(1,2)
circuit.cnot(2,3)
circuit.draw(output='mpl')


# In[299]:


simulator = Aer.get_backend('statevector_simulator')
result = execute(circuit, backend = simulator).result()
statevector = result.get_statevector()
array_to_latex(statevector, prefix="\\text{statevector = }\n")


# In[300]:


circuit.measure_all()
simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend=simulator).result()
plot_histogram(result.get_counts())


# In[ ]:





# In[ ]:




