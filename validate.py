import ipaddress

ipv4examples = []
file = open("allow_service_ips.txt", "r")
for x in file:
    ipv4examples.append(x.rstrip())

# Validate the examples list is bigger than 2
if len(ipv4examples) < 2:
    print("Error: list too short")
    exit(1)

for ipv4example in ipv4examples:
    # Validate it's really an IP address
    try:
        ip = ipaddress.ip_network(ipv4example)
    except:
        print("Error: failed to parse {0}".format(ipv4example))
        exit(1)

    # Validate it's a public IP address
    ip = ipaddress.ip_network(ipv4example)
    if ip.is_global is False:
        print("Error: not a public IP {0}".format(ipv4example))
        exit(1)

    # Validate it's just one address
    if ip.num_addresses != 1:
        print("Error: not a single IP {0}".format(ipv4example))
        exit(1)
