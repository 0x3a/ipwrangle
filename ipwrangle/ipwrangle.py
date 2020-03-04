#!/usr/bin/env python3

import sys
import argparse

import ipaddress
from netaddr import IPNetwork

def parse_args(prog):
    parser = argparse.ArgumentParser(prog=prog)
    parser.add_argument('value', nargs='?', type=str, default=None, help="Value to convert (can also be supplied on stdin)")

    return parser.parse_args()

def expand_main():
    args = parse_args('ipexpand')

    worklist = sys.stdin
    if args.value:
        worklist = args.value.split(',')

    for line in worklist:
        line = line.rstrip()
        [print(ip) for ip in IPNetwork(line)]

def reduce_main():
    args = parse_args('ipreduce')

    worklist = [line.rstrip() for line in sys.stdin.readlines()]
    if args.value:
        worklist = [line.rstrip() for line in args.value.split(',')]

    [print(cidr) for cidr in list(ipaddress.collapse_addresses([ipaddress.ip_network(ip) for ip in sorted(worklist)]))]
