# Quantum-Algorithms

My name is Max Behrens and I am a 4th-year MSci Physics student at Imperial College London. This repository contains a collection of quantum computing algorithms implemented using Qiskit, intended for learning and exploring basic quantum circuits on simulators and real IBM Quantum devices.

---

## H_CNOT.ipynb

This notebook demonstrates a 2-qubit quantum circuit that creates a Bell state. It covers:

- Preparing the initial state |00>
- Applying a Hadamard gate on qubit 0
- Applying a CNOT gate with qubit 0 as control and qubit 1 as target
- Simulating the circuit using fake backends and real IBM Quantum hardware
- Measuring expectation values of Pauli observables using the Estimator primitive

The notebook illustrates entanglement, circuit behaviour, and comparison between simulator and hardware results including statistical and mitigation errors.

---

### Requirements

- Python 3.8+  
- Qiskit (qiskit, qiskit-ibm-runtime)  
- Matplotlib  
- Pandas  
