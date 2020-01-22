# python connection creator (pcc)
import socket
import argparse
from datetime import datetime

__version__ = "1.0"

def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(description="Python Connection Creator (pcc) v" + __version__)
    print "*** "
    print "*** " + parser.description
    print "*** "
    parser._action_groups.pop()
    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')
    required.add_argument("-dst", "--destination", required=True, action="store", help="DNS name or IP address for destination")
    required.add_argument("-dport", "--destination-port", required=True, type=int, action="store", help="Port number for destination")
    optional.add_argument("-t", "--timeout", type=float, action="store", help="Username to access the API")
    args = parser.parse_args()

    if args.destination:
        dest_addr = args.destination
    if args.destination_port:
        dest_port = args.destination_port
    if args.timeout:
        timeout = args.timeout
    else:
        timeout = 10.0

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.settimeout(timeout)
        print_status("Attempting a TCP connection with a {} second timeout to {} on port {}...".format(timeout, dest_addr, dest_port),"status")
        s.connect((dest_addr, dest_port))
        print_status("Connection completed successfully.", "normal")
    except socket.error as error:
        print_status("Error: {}".format(error), "error")

def print_status(message, type):
    if type.lower() == "error":
        indent = "!!!"
    elif type.lower() == "status":
        indent = "---"
    else:
        indent = "..."
    print "{} [{:%H:%M:%S}] {}".format(indent, datetime.now(), message)

if __name__ == '__main__':
    main()