#!/usr/bin/env python
# coding: utf-8

# In[17]:


from qiskit import *
from qiskit.tools.visualization import plot_histogram, array_to_latex, plot_bloch_multivector
get_ipython().run_line_magic('matplotlib', 'inline')


# In[61]:


#qr = QuantumRegister(2)
#cr = ClassicalRegister(2)
circuit = QuantumCircuit(2)
circuit.h(0)
circuit.measure_all()


# In[56]:


simulator = Aer.get_backend('statevector_simulator')
result = execute(circuit, backend = simulator).result()
statevector = result.get_statevector()
array_to_latex(statevector)


# In[54]:


plot_bloch_multivector(statevector)


# In[63]:


simulator2 = Aer.get_backend('qasm_simulator')
result2 = execute(circuit, backend = simulator2).result()
counts = result.get_counts()


# In[60]:


plot_histogram(counts)


# In[ ]:




