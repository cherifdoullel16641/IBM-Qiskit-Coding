#!/usr/bin/env python
# coding: utf-8

# In[160]:


from qiskit import *
from qiskit.tools.visualization import plot_bloch_multivector, plot_histogram, array_to_latex
from math import pi
get_ipython().run_line_magic('matplotlib', 'inline')


# In[237]:


circuit = QuantumCircuit(3)
circuit.x(0)
circuit.cx(1,2)
circuit.cnot(0,1)
circuit.draw(output='mpl')


# In[238]:


simulator = Aer.get_backend('statevector_simulator')
result = execute(circuit, backend = simulator).result()
plot_bloch_multivector(result.get_statevector())


# In[ ]:




