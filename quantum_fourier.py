import numpy as np
from numpy import pi

#!pip install qiskit
import qiskit as q

%matplotlib inline

#cubit register
circuit = q.QuantumCircuit(5,5)  
circuit.h(0)
circuit.u1(pi/2, 0)
circuit.cx(0, 1) 
circuit.u1(pi/2, 1)
circuit.cx(0, 1) 
circuit.u1(pi/2, 2)
circuit.h(1)
circuit.cx(0, 2) 
circuit.u1(pi/2, 2)
circuit.cx(0,2)
circuit.u1(pi/4, 1)
circuit.u1(pi/8, 2)
circuit.cx(1,2)
circuit.u1(-pi/4,2)
circuit.cx(1,2)
circuit.u1(pi/4,2)
circuit.h(2)
circuit.measure(list(range(0,4)), list(range(0,4))) 
circuit.draw(output="mpl")  

from qiskit.tools.monitor import job_monitor
from qiskit import IBMQ
IBMQ.save_account("token")
backend = provider.get_backend("ibmq_london")
job = q.execute(circuit, backend=backend, shots=500)
job_monitor(job)

from qiskit.visualization import plot_histogram
from matplotlib import style
  
style.use("dark_background")
# Dark theme is very cool.

result = job.result()
counts = result.get_counts(circuit)

v = plot_histogram([counts], legend=['Device'])
# Save v as png etc etc etc.
