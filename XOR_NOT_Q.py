#!/usr/bin/env python
# coding: utf-8

# In[160]:


from qiskit import *
from qiskit.tools.visualization import plot_bloch_multivector, plot_histogram, array_to_latex
from math import pi
get_ipython().run_line_magic('matplotlib', 'inline')


# In[264]:


circuit = QuantumCircuit(4,2)
circuit.x(0) #initialize the input A
circuit.x(1) #initialize the input B
circuit.barrier() # It's a barrier between the gates 

circuit.cx(0,2)
circuit.cx(1,2)
circuit.ccx(0,1,2)

circuit.barrier()
circuit.measure(2,0) #Measure SUM
circuit.measure(3,1) #Measure CARRY-OUT

circuit.draw(output='mpl')


# In[265]:


simulator = Aer.get_backend('statevector_simulator')
result = execute(circuit, backend = simulator).result()
plot_bloch_multivector(result.get_statevector())


# In[ ]:





# In[ ]:




