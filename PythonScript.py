## Start from Bash with the following command line
## genie shell --testbed-file mock_test.yaml

from pprint import pprint
uut = testbed.devices.xe
uut.connect()

interface = uut.learn('interface')
pprint(interface.info)
pprint(interface.info['GigabitEthernet2'])
pprint(interface.info['GigabitEthernet2']['phys_address'])



###############################

interface_before = uut.learn('interface')

from genie.conf import Genie
testbed = Genie.init('mock_disaster.yaml')

uut = testbed.devices.xe
uut.connect()

interface_after = uut.learn('interface')

diff = interface_after.diff(interface_before)
print(diff)

############################

interface_after = uut.learn('interface', attributes=['info[(.*)][oper_status]'])

testbed = Genie.init('mock_test.yaml')
uut = testbed.devices.xe
uut.connect()


interface_before = uut.learn('interface', attributes=['info[(.*)][oper_status]'])

diff = interface_after.diff(interface_before)

print(diff)


###########################

#Tabular Parsing

import os
os.chdir('parser_gen')

testbed = Genie.init('mocked_first.yaml')
uut = testbed.devices.iosxe1
uut.connect()

from genie import parsergen

output = uut.device.execute('show nve vni')

header = ['Interface', 'VNI', 'Multicast-group', 'VNI state', 'Mode', 'BD', 'cfg', 'vrf']

result = parsergen.oper_fill_tabular(device_output=output, device_os='iosxe', header_fields=header, index=[0])

pprint(result.entries)
