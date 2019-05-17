### Using GENIE with Python

We shall now explore the initial steps to leverage Genie within a Python script.  The examples given previously provide a very powerful method of validating the state of the network with little or no programming experience.  By leveraging Python we can provide additional logic to **supercharge** your network validation.

If you continuing from the previous labs, then please remove the environmental variables from you shell

```bash
unset unicon_replay
unset unicon_speed
```

We can initiate an interactive Python shell direct from Genie CLI. 

```bash
genie shell --testbed-file mock_test.yaml
```

This command will start a Python shell and load the Genie libraries and initiate the testbed

Now create a device object that will be named **uut**, and use the connect method to establish a connection to the device.  In this instance our device object is the IOS XE device in the topology.

```python
uut = testbed.devices.iosxe1 
uut.connect()
```

