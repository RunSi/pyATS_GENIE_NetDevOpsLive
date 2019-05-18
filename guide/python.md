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
uut = testbed.devices.xe
uut.connect()
```

Now create an interface object using the learn method of uut.

```python
interface = uut.learn('interface')
```

This will now issue a number of show commands, parse the output and save it as structured data in the **info** attribute of **interface**

To display the output

```python
interface.info
```

And to pretty print the output

```python
from pprint import pprint
```

As this data is structured as a python dictionary we can use dictionary keys to obtain relevant data

```python
pprint(interface.info['GigabitEthernet2']) 

pprint(interface.info['GigabitEthernet2']['phys_address'])  
```



### Comparing network state

Similar to the previous exercises the objective is to compare network state before and after a change.  

First create an initial interface state, this the object will be called interface_before

```python
interface_before = uut.learn('interface')
```

**NOTE**

Now a network topology is loaded where the state of the network has changed.  This step is necessary as we are using **mock** devices.  In a live environment, this step would not be needed

```python
from genie.conf import Genie
testbed = Genie.init('mock_disaster.yaml’) 

uut = testbed.devices.xe
uut.connect()   
```

Now learn the new state of the interface, the object will be called interface_after

```python
interface_after = uut.learn(‘interface’)
```

Both the interface_after object and the interface_before object have a **diff** method.  We can use the diff method to determine the differences between the two snapshots

```python
diff = interface_after.diff(interface_before) 
print(diff)
```

The output of _print(diff)_ displays all the differences between the interfaces, this includes all interface counters.  This results in a lot of _noise_

To overcome this we can select the keys to parse by passing in an attribute argument.

```python
interface_after = uut.learn('interface', attributes=['info[(.*)][oper_status]'])

testbed = Genie.init('mock_test.yaml')
uut = testbed.devices.xe
uut.connect()

interface_before = uut.learn('interface', attributes=['info[(.*)][oper_status]'])
diff = interface_after.diff(interface_before) 
print(diff)
```



### Simple Parsing with GENIE

As has been described previously, the learn method will issue a number of show commands relevant to the model being learnt.  The result is returned as structured data.

If data needs to be obtained for a single show command, then the parse method of the device object can be used.

```python
version = uut.parse('show version')
type(version)
version
version['version']['uptime']
```



## Conclusion

To iterate a few points about pyATS and Genie:

- pyATS and Genie is developed and used as the de-facto testing library and solution in Cisco
- Genie is **THE** Python library to use and automate your network!
- It is **free** to use and all the libraries are [open source](https://github.com/CiscoTestAutomation)
- The Cisco internal and customer external version of pyATS/Genie is exactly the same
- New libraries and innovation are being released as we speak!
- Genie libraries can be used in many ways:
  - With the [Genie CLI](https://pubhub.devnetcloud.com/media/pyats-packages/docs/genie/cli.html)
  - RobotFramework [Genie library](https://pubhub.devnetcloud.com/media/pyats-packages/docs/genie/robot/index.html)
  - As a pure [Python library](https://pubhub.devnetcloud.com/media/pyats-packages/docs/genie/)

