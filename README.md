# CMU 18755 - Networks in the Real World (Project)

This is the repository for the course project for CMU 18755 - Networks in the Real World (Fall 2021).

## Project Info
- Project Name: Network Destroy Repair Game

- Group member 1 info: Tony Huang, runqih@andrew.cmu.edu

- Group member 2 info: Vikas Kashyap, vhuvinah@andrew.cmu.edu


## Project Description
- This repository includes the Python implementation for Network Destroy-Repair Game and the reports for each milestone. In this project, we are interested in investigating the robustness property of real-world network, by designing different attack/defense algorithms and simluating the response of the networks.

- Data: [Stanford SNAP dataset](https://snap.stanford.edu/data/#citnets), Gnutella peer to peer network from August 31 2002

- Known dependencies: Python, numpy, networkX, igraph


## Experiment Parameters
- `--seed`: defines the random seed setting for experiments

- `--network_name`: defines the network that will be used for experiment (Gnutella peer-to-peer network from August 31 2002)

- `--attack_algorithm`: defines the type of algorithms used for attack

- `--defense_algorithm`: defines the type of algorithms used for defense

- `--criterion`: defines the type of criterion used to evalute network robustness (Molloy-Reed criterion)

- `--niter`: defines number of time steps an experiment is expected to perform

- `--p`: defines the percentage of initial edges that will be attacked and repaired at each time step


## Code and File Structure

- `./runner.py`: contains code for running the experiments

- `./algorithm/attack.py`: code for the three attack algorithms

- `./algorithm/defense.py`: code for the three defense algorithms

- `./utils/criterion.py`: code for the robustness evalution critieron

- `./utils/misc.py`: code for useful functions and parameters

- `./utils/plot.py`: code for plotting results

- `./experiment`: folder containing the experiment results and analysis

- `./data`: folder containing the network data

- `./data`: folder containing report/demo/presentation for each of the three milestones


## Usage

To run the experiment, set the desired paramters in misc.py and run the following command in the terminal:

```python main.py```