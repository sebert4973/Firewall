import csv
from collections import defaultdict

# Store information about a rule and provide functionality to see if a packet matches this rule
class Rule:
    def __init__(self, direction, protocol, port, ip):
        self.direction = direction
        self.protocol = protocol

        ports = port.split("-")
        self.lowerPort = int(ports[0])
        if len(ports) == 1:
            self.upperPort = int(ports[0])
        else:
            self.upperPort = int(ports[1])

        ips = ip.split("-")
        self.lowerIp = ips[0]
        if len(ips) == 1:
            self.upperIp = ips[0]
        else:
            self.upperIp = ips[1]

    def accepts_packet(self, packet):
        return (packet.direction == self.direction) and \
        (packet.protocol == self.protocol) and \
        (self.lowerPort <= packet.port <= self.upperPort) and \
        (self.lowerIp.split(".") <= packet.ip.split(".") <= self.upperIp.split(".")) # We can't compare the strings directly, so make them arrays

# Store information about a single data packet
class Packet:
    def __init__(self, direction, protocol, port, ip):
        self.direction = direction
        self.protocol = protocol
        self.port = port
        self.ip = ip

# Manages the operation of the firewall with a list of rules
class Firewall:
    def __init__(self, file_name):

        # store rules as a map of (direction, protocol) to the list of rules
        # that match that direction and protocol.
        # This can reduce lookup speed by a factor of 4, assuming that these two
        # values are evenly distibuted.
        self.rules = defaultdict(lambda: [])

        with open(file_name) as csv_file:
            reader = csv.reader(csv_file)
            for line in reader:
                direction = line[0]
                protocol = line[1]
                portRange = line[2]
                ipRange = line[3]
                rule = Rule(direction, protocol, portRange, ipRange)
                # add to the list for the given direction and protocol
                self.rules[(direction, protocol)].append(rule)

    def accept_packet(self, direction, protocol, port, ip):
        packet = Packet(direction, protocol, port, ip)

        # only check rules that match the direction and protocol to save time
        for rule in self.rules[(direction, protocol)]:
            if rule.accepts_packet(packet):
                return True
        return False

fw = Firewall("file.csv")
print fw.accept_packet("inbound", "udp", 53, "192.168.2.1")
