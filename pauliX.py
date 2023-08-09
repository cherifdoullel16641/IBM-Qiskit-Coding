#!/usr/bin/env python
# coding: utf-8

# In[85]:


from qiskit import *
from qiskit.tools.visualization import plot_histogram, array_to_latex, plot_bloch_multivector
from math import pi
get_ipython().run_line_magic('matplotlib', 'inline')


# In[89]:


circuit = QuantumCircuit(1)
circuit.ry(pi/4, 0)
circuit.x(0)
print(circuit)
circuit.draw(output='mpl')


# In[90]:


simulator = Aer.get_backend('statevector_simulator')
result = execute(circuit, backend = simulator).result()
statevector = result.get_statevector()
array_to_latex(statevector, prefix="\\text{statevector = }\n")


# In[91]:


plot_bloch_multivector(statevector)


# In[ ]:




