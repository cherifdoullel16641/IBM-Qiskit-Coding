#!/usr/bin/env python
# coding: utf-8

# In[160]:


from qiskit import *
from qiskit.tools.visualization import plot_bloch_multivector, plot_histogram, array_to_latex
from math import pi
get_ipython().run_line_magic('matplotlib', 'inline')


# In[260]:


circuit = QuantumCircuit(3)
circuit.x(0)
circuit.h(1)
circuit.rx(-pi/4, 2)
#circuit.swap(1,2)
circuit.cswap(0,1,2)
circuit.draw(output='mpl')


# In[261]:


simulator = Aer.get_backend('statevector_simulator')
result = execute(circuit, backend = simulator).result()
plot_bloch_multivector(result.get_statevector())


# In[ ]:





# In[ ]:




