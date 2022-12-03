CMU 18755 - Networks in the Real World (Project)
====

Project Info:
- Project Name: Network Destroy Repair Game
- Group member 1 info: Tony Huang (runqih@andrew.cmu.edu)
- Group member 2 info: Vikas Kashyap (vhuvinah@andrew.cmu.edu)

Project Description:
- This repository includes the Python implementation for Network Destroy-Repair Game and the reports for each milestone.
- In this project, we are interested in investigating the robustness property of real-world network, by designing different attack/defense algorithms and simluating the response of the networks.
- Data: Stanford SNAP dataset (https://snap.stanford.edu/data/#citnets)

Paramters:
- Network: P2P network (Gnutella peer-to-peer network, August 31 2002)
- Attack algorithm: attack algorithm can be random, degree, or betweeness
- Defense algorithm: defense algorithm can be random, degree, or betweeness
- Number of iterations (niter): number of time steps an experiment is expected to perform, default: 100
- Percentage of attacks/defense (p): the percentage of initial edges that will be attacked and repaired at each time step
- Seed: seed for the random experiment

## Usage

```python main.py```
