### Using ROBOT Framework to further automate

[ROBOT](https://robotframework.org/) framework is a generic Python/Java test automation framework that focuses on acceptance test automation through English like keyword-driven test approach.

ROBOT framework support is an optional subpackage to GENIE.

It is added to GENIE by using the following command

```bash
pip install --upgrade genie.libs.robot
```



### Network validation with ROBOT

We shall perform the same exercise as demonstrated with GENIE CLI but will be using a ROBOT script to automate the process.

Our Workshop Robot script will:

- Learn the good state of the network
- Rerun periodically or when a disaster occurs to figure out what happened

With an editor, open the script below and examine its content:

- `robot_initial_snapshot/robot_initial_snapshot.robot`

The Robot language is keyword based, which makes reading this script quite easy. Without much effort, you should see that this script does the following:

- Load Genie Library
- Connect to the two devices
- Learn BGP, interface, platform, OSF and the device configuration and save it to file

Let's run the script:

```bash
# this environment variable is needed as we are using our Mocked Device.
# When Genie cli is used with real devices, these can be omitted.
export unicon_replay=~/pyATS_GENIE_NetDevOpsLive/record_initial

# run robot script
cd robot_initial_snapshot
robot --outputdir run robot_initial_snapshot.robot
```

RobotFramework generates its own log files. You can open the `run/log.html` with a web browser to view it.

Our good snapshot was saved as file `robot_initial_snapshot/good_snapshot`; we are now ready for a disaster to happen!

**Disaster!**

In the previous step we've taken a snapshot of our network when it was performing as expected. We will now take a new snapshot and compare it with the previous good snapshot.

With an editor open the script below, and examine its content:

```
robot_compare_snapshot/compare_snapshot.robot
```

This is the 2nd RobotFramework based script which, upon running, will:

- Load Genie Library
- Connect to the two devices
- Learn BGP, interface, platform, OSPF and the device configuration, and save it to files
- And compare the new snapshot with the original one!

Let's start the script.

```bash
# this environment variable is needed as we are using our Mocked Device.
# When Genie cli is used with real devices, these can be omitted.
export unicon_replay=~/pyATS_GENIE_NetDevOpsLive/record_disaster

# run robot script
cd ../robot_compare_snapshot
robot --outputdir run compare_snapshot.robot
```

And again, open the `run/log.html` with a web browser to view the log.

Now we shall move onto using GENIE in a Python interactive shell - [Python demonstration](pythondemo)