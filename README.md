# CMU 18755 - Networks in the Real World (Project)

Project Info:
- Project Name: Network Destroy Repair Game
- Group member 1 info: Tony Huang (runqih@andrew.cmu.edu)
- Group member 2 info: Vikas Kashyap (vhuvinah@andrew.cmu.edu)

Project Description:
- This repository includes the Python implementation for Network Destroy-Repair Game and the reports for each milestone.
- In this project, we are interested in investigating the robustness property of real-world network, by designing different attack/defense algorithms and simluating the response of the networks.
- Data: Stanford SNAP dataset (https://snap.stanford.edu/data/#citnets), Gnutella peer to peer network from August 31 2002, which is contained in the 'data' folder
- Reports: The 'report' folder contains the report/demo/presentation for each of the three milestones
- Experiment outcomes: the results of the experiments are contained in the "experiment" folder
- Utils: the 'utils' folder contains miscellenous helper function, such as plotting and paramters

Paramters of the Experiment:
- Network: P2P network (Gnutella peer-to-peer network, August 31 2002)
- Attack algorithm: attack algorithm can be random, degree, or betweeness
- Defense algorithm: defense algorithm can be random, degree, or betweeness
- Number of iterations (niter): number of time steps an experiment is expected to perform, default: 100
- Percentage of attacks/defense (p): the percentage of initial edges that will be attacked and repaired at each time step
- Seed: seed for the random experiment

## Usage

To run the experiment, set the desired paramters in misc.py and run the following command in the terminal:

```python main.py```