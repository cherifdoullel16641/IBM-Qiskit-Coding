#!/usr/bin/env python
# coding: utf-8

# In[270]:


from qiskit import *
from qiskit.tools.visualization import plot_bloch_multivector, plot_histogram, array_to_latex
from math import pi
get_ipython().run_line_magic('matplotlib', 'inline')


# In[450]:


# Bell states
circuit = QuantumCircuit(2)
circuit.h(0)
circuit.cx(0, 1)
circuit.measure_all()
circuit.draw(output='mpl')


# In[452]:


simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend=simulator).result()
plot_histogram(result.get_counts())


# In[471]:


from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit.tools.monitor import job_monitor
IBMQ.save_account('83d2199ecd44381580a58d1ffc760f7ef6a34d5f3a23c84b558b0eefd117c08f0a5647753c3f08e551fd575d6d9329707097566a59142793f80d047899f1a5b6')
provider = IBMQ.load_account()


# In[479]:


qcomp = provider.get_backend('ibmq_belem')
job = execute(circuit, backend = qcomp)
job_monitor(job)


# In[483]:


qcomp_result = job.result()
plot_histogram(qcomp_result.get_counts())


# In[ ]:





# In[ ]:




