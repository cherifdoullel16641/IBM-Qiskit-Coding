#!/usr/bin/env python
# coding: utf-8

# In[160]:


from qiskit import *
from qiskit.tools.visualization import plot_state_qsphere
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[161]:


circuit = QuantumCircuit(4)
circuit.x([0,1,3])
circuit.draw(output='mpl')


# In[162]:


simulator = Aer.get_backend('statevector_simulator')
statevector = execute(circuit, backend = simulator).result().get_statevector()
plot_state_qsphere(statevector)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




