'''
Validate the contents of our INPUT_FILE.
Contents should be a list of IP addresses, one per line.
pound-prefaced comments are ignored.

Valid IPs result in an exit 0
Any issue in the file, exit 1
'''
import sys
import re
import ipaddress

INPUT_FILE = 'allow_service_ips.txt'


def main():
    ''' main function '''
    ipv4examples = list()
    with open(INPUT_FILE, 'r') as filehandle:
        wholefile = filehandle.readlines()
        for line in wholefile:
            if re.match(r'^\s*#', line):
                # commented line
                continue
            ipv4examples.append(line.strip())

    # Validate the examples list is bigger than 2
    if len(ipv4examples) < 2:
        print('Error: list too short')
        sys.exit(1)

    for ipv4example in ipv4examples:
        # Validate it's really an IP address
        try:
            ipaddr = ipaddress.ip_network(ipv4example)
        except ValueError:
            print(f'Error: "{ipv4example}" failed to parse')
            sys.exit(1)

        # Validate it's a public IP address
        if not ipaddr.is_global:
            print(f'Error: "{ipv4example}" is not a public IP')
            sys.exit(1)

        # Validate it's just one address
        if ipaddr.num_addresses != 1:
            print(f'Error: "{ipv4example}" is not a single IP')
            sys.exit(1)

    # Final fall-through, all checks passed.
    sys.exit(0)


if __name__ == '__main__':
    main()
