### NetDevOps Live - pyATS / GENIE Guide

### s02t08

### Lab Setup

Clone this repository and move to directory 

```bash
git clone 
cd ~/Genie_NetDevOpsLive
```

Create a Python virtual environment and install necessary libraries

```bash
# create python virtual environment
python3 -m venv venv

# activate virtual environment
source venv/bin/activate

# update pip/setuptools
pip install --upgrade pip setuptools

# install pyATS and GENIE libraries
pip install -r requirements.txt
```



**GENIE Mock Devices**

As part of this lab we shall be leveraging GENIE _mock devices_.  Mock devices are recordings of real devices, in this instance an XE, an NXOS and an XR device.  The GENIE CLI commands / ROBOT examples / Python examples can all be used on real devices with changes to the **testbed** files.



###Network Topology



-----------------

### GENIE CLI

Initially we shall be leveraging a suite of Command Line tools that are part of Genie.  Genie command line tools allows a user to learn and parse information from network devices within the topology.  

To view the commands available within Genie CLI enter the following

```bash
genie -help

# output from the above command

Usage:
  genie <command> [options]

Commands:
    diff                Command to diff two snapshots saved to file or directory
    learn               Command to learn device features and save to file
    parse               Command to parse show commands
    run                 Run Genie triggers & verifications in pyATS runtime environment
    shell               enter Python shell and load a Genie testbed file and/or Pickled file

General Options:
  -h, --help            Show help

Run 'genie <command> --help' for more information on a command.

argument -h/--help: ignored explicit argument 'elp'
```



To begin with we are going to make a snapshot of the current state of the network topology and save that state in a directory called **learnt**

```bash
# These two environment variables are needed as we are using our Mocked Devices.
# When Genie cli is used with real devices these can environmental variables can be omitted.

export unicon_replay=~/Genie_NetDevOpsLive/record_initial
export unicon_speed=10

# run Genie CLI
genie learn ospf interface bgp --testbed-file testbed.yaml --output learnt
```



Please review the output of this command in the learnt directory.

Internally Genie uses its [Models](https://pubhub.devnetcloud.com/media/pyats-packages/docs/genie/genie_libs/#/models) to decide which commands to issue and what to store.  Genie feature models are agnostic across OS, platforms and management protocols (eg, CLI/NETCONF).

With an editor of your choice open the files

```
learnt/ospf_nxos_nx-osv-1_ops.txt
```

```
learnt/ospf_nxos_nx-osv-1_console.txt
```

The `_ops` file contains the datastructure learnt/parsed from the show commands for the feature OSPF on the nxos device.

The `_console` file contains all the cli and device output which were sent to the device to learn OSPF on the nxos device.

Each feature's relevant information is parsed into structured data. 



