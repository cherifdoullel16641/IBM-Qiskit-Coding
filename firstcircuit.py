#!/usr/bin/env python
# coding: utf-8

# In[17]:


from qiskit import *
from qiskit.tools.visualization import plot_histogram, array_to_latex, plot_bloch_multivector
get_ipython().run_line_magic('matplotlib', 'inline')


# In[37]:


qr = QuantumRegister(1)
cr = ClassicalRegister(1)
circuit = QuantumCircuit(qr, cr)
circuit.measure(qr, cr)


# In[41]:


simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend = simulator, shots=1024).result()
plot_histogram(result.get_counts())


# In[44]:


simulator2 = Aer.get_backend('statevector_simulator')
result2 = execute(circuit, backend=simulator2).result()
statevector = result2.get_statevector()
array_to_latex(statevector)


# In[43]:


plot_bloch_multivector(statevector)


# In[ ]:




