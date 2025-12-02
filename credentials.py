import os
from qiskit_ibm_runtime import QiskitRuntimeService

# Load in data
file_path = os.path.dirname(os.path.abspath(__file__)) + '/config.txt'
data_dict = {}

with open(file_path, 'r') as f:
    for line in f:
        # Split each line into key and value
        key, value = line.strip().split(',')
        data_dict[key] = str(value)

QiskitRuntimeService.save_account(
token= data_dict['APIKey'],
instance= data_dict['instance'],
overwrite=True
)