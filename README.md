# Quantum Algorithms

A collection of quantum computing algorithms and implementations using Qiskit. This repository contains tutorial implementations of fundamental quantum algorithms, as well as more advanced projects exploring quantum machine learning techniques.

## Table of Contents

- [QUMAP - Quantum UMAP](#qumap---quantum-umap)
- [Quantum Autoencoder](#quantum-autoencoder)
- [Tutorial Algorithms](#tutorial-algorithms)
- [Requirements](#requirements)

---

## QUMAP - Quantum UMAP

A quantum implementation of the UMAP (Uniform Manifold Approximation and Projection) dimensionality reduction algorithm. This project uses variational quantum circuits trained with the classical UMAP loss function to map high-dimensional quantum states to 2D embeddings.

### Files

| File | Description |
|------|-------------|
| `QUMAP.py` | Core QUMAP class implementing the quantum UMAP algorithm. Contains methods for state encoding, parametrized ansatz circuits, cost computation, and 2D embedding generation. |
| `TrainQUMAP.py` | Training script that optimizes the variational circuit parameters to minimize the UMAP cost function. Saves optimized parameters to JSON with timestamps for multiple training runs. |
| `PlotQUMAP.py` | Visualization script that loads saved parameters and plots the 2D embeddings with distinct colours for each data category. |
| `IrisStateGeneration.ipynb` | Jupyter notebook for preprocessing the Iris dataset and preparing quantum states for QUMAP. |
| `iris_dataset.csv` | Preprocessed Iris dataset with features normalised to [-1, 1] and plant type labels. |
| `iris_params.json` | Saved optimized parameters from training runs. |

### Usage

```python
from QUMAP import QUMAP

# Create QUMAP instance
qumap = QUMAP(num_qubits=4, num_layers=2, k=10)

# Load data and compute cost
data = pd.read_csv('iris_dataset.csv').values
params = qumap.random_params()
cost = qumap.compute_cost(data, params)

# Get 2D embedding
coords_2d, labels = qumap.get_embedding(data, optimized_params)

# Visualize circuit structure
qumap.draw_circuit()
```

---

## Quantum Autoencoder

Implementation of quantum autoencoders for quantum data compression, including Schumacher compression and comparisons with classical PCA.

### Files

| File | Description |
|------|-------------|
| `QuantumAutoencoder.ipynb` | Main implementation of the quantum autoencoder using variational circuits to compress quantum states into a lower-dimensional latent space. |
| `SchumacherEig.ipynb` | Implementation of Schumacher compression using eigenvalue decomposition of density matrices. |
| `PCACompression.ipynb` | Classical PCA compression for comparison with quantum methods. |
| `StateGeneration.ipynb` | Notebook for generating quantum states (BeH₂ molecular states) used as training data for the autoencoder. |
| `beh2_states_dataset.json` | Dataset of BeH₂ molecular ground states at various bond lengths for autoencoder training. |
| `density_matrix_eigvals.csv` | Eigenvalues of density matrices used in Schumacher compression analysis. |

---

## Tutorial Algorithms

Implementations of fundamental quantum algorithms for educational purposes.

### Files

| File | Description |
|------|-------------|
| `BellStatePrep.ipynb` | Preparation and measurement of Bell states - maximally entangled two-qubit states. Demonstrates basic quantum entanglement. |
| `Grovers.ipynb` | Grover's search algorithm for unstructured database search, demonstrating quadratic speedup over classical search. |
| `QuantumFT.ipynb` | Quantum Fourier Transform (QFT) implementation - a key subroutine in many quantum algorithms including Shor's algorithm. |
| `RandNumGen.ipynb` | Quantum random number generator using quantum superposition to generate truly random numbers. |

---

## Requirements

- Python 3.10+
- Qiskit
- NumPy
- SciPy
- Pandas
- Matplotlib

Install dependencies:

```bash
pip install qiskit numpy scipy pandas matplotlib
```

---

## Author

Max Behrens - Imperial College London

---

### Requirements

- Python 3.8+  
- Qiskit (qiskit, qiskit-ibm-runtime)  
- Matplotlib  
- Pandas  
