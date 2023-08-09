#!/usr/bin/env python
# coding: utf-8

# In[160]:


from qiskit import *
from qiskit.tools.visualization import plot_bloch_multivector, plot_histogram, array_to_latex
from math import pi
get_ipython().run_line_magic('matplotlib', 'inline')


# In[217]:


circuit = QuantumCircuit(3)
circuit.x(0)
circuit.h(1)
circuit.ry(pi/3, 2)
circuit.measure_all()
circuit.draw(output='mpl')


# In[218]:


simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend = simulator, shots= 1000000).result()
plot_histogram(result.get_counts())


# In[ ]:




