# Lab1.4


from ipaddress import IPv4Network
import random

numberofnets = 20  # число требуемых сетей


class IPv4RandomNetwork(IPv4Network):
    def __init__(self, n, p):
        IPv4Network.__init__(self, (n, p), strict=False)

    def regular(self):
        return not (self.is_multicast |
                    self.is_loopback |
                    self.is_private |
                    self.is_reserved |
                    self.is_unspecified)


# randnettest = 0xc0a80000
# randmasktest = 24

netarray = []
netarraystr = []

for i in range(0, numberofnets):
    randnet = random.randint(0x0B000000, 0xDF000000)
    randmask = random.randint(8, 24)
    net = IPv4RandomNetwork(randnet, randmask)
    netarray.append(net)
    # netarraystr.append(str(net))
    # nettest = IPv4RandomNetwork(randnettest, randmasktest)
    # print("%20s\t" % str(net), net.regular())
    # print(nettest, nettest.regular())


# print(netarraystr)


def keyfunc(addr):
    ip = int(addr.network_address)
    mask = int(addr.netmask)
    return mask * 2 ** 32 + ip


netarraysorted = sorted(netarray, key=keyfunc)

print("%20s\t%20s" % ("Base", "Sorted"))
for i in range(0, numberofnets):
    print("%20s\t%20s" % (str(netarray[i]), str(netarraysorted[i])))

