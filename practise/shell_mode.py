import struct

print(struct.calcsize("P"*8))

#2nd_solution

import platform
import struct

architecture=platform.architecture()[0]
print(architecture)

print(struct.calcsize("p")*8)