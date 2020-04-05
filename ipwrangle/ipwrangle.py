#!/usr/bin/env python3

import sys
import argparse

import ipaddress
from netaddr import IPNetwork
from signal import signal, SIGPIPE, SIG_DFL

# http://newbebweb.blogspot.com/2012/02/python-head-ioerror-errno-32-broken.html
signal(SIGPIPE,SIG_DFL)


# Taken from: https://mail.python.org/pipermail/tutor/2003-November/026645.html
class Unbuffered(object):
   def __init__(self, stream):
       self.stream = stream
   def write(self, data):
       self.stream.write(data)
       self.stream.flush()
   def writelines(self, datas):
       self.stream.writelines(datas)
       self.stream.flush()
   def __getattr__(self, attr):
       return getattr(self.stream, attr)


# Remove buffering, processing large datasets eats memory otherwise
sys.stdout = Unbuffered(sys.stdout)


def parse_args(prog):
    parser = argparse.ArgumentParser(prog=prog)
    parser.add_argument('value', nargs='?', type=str, default=None, help="Value to process")
    parser.add_argument('value_two', nargs='?', type=str, default=None, help="Second value to process")

    return parser.parse_args()


def innet_main():
    args = parse_args('innet')

    if args.value in IPNetwork(args.value_two):
        sys.stderr.write('true\n')
        return 0
    else:
        sys.stderr.write('false\n')
        return -1


def netlen_main():
    args = parse_args('netlen')

    worklist = sys.stdin
    if args.value:
        worklist = args.value.split(',')

    for line in worklist:
        line = line.rstrip()
        print(IPNetwork(line).size)

def expand_main():
    args = parse_args('ipexpand')

    worklist = sys.stdin
    if args.value:
        worklist = args.value.split(',')

    for line in worklist:
        line = line.rstrip()
        [print(ip) for ip in IPNetwork(line)]


def reduce_main():
    try:
        args = parse_args('ipreduce')

        worklist = []
        if args.value:
            worklist = [line.rstrip() for line in args.value.split(',')]
        else:
            worklist = [line.rstrip() for line in sys.stdin.readlines()]

        [print(cidr) for cidr in list(ipaddress.collapse_addresses([ipaddress.ip_network(ip) for ip in sorted(worklist)]))]
    except KeyboardInterrupt:
        sys.stdout.write('\n')
