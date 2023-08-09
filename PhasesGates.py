#!/usr/bin/env python
# coding: utf-8

# In[160]:


from qiskit import *
from qiskit.tools.visualization import plot_bloch_multivector, plot_histogram, array_to_latex
from math import pi
get_ipython().run_line_magic('matplotlib', 'inline')


# In[204]:


circuit = QuantumCircuit(3)
circuit.h([0,1,2])
circuit.t(1)
circuit.tdg(2)
circuit.draw(output='mpl')


# In[205]:


simulator = Aer.get_backend('statevector_simulator')
result = execute(circuit, backend = simulator).result()
plot_bloch_multivector(result.get_statevector())


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




