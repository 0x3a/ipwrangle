# ipwrangle
A simple python-based command-line utility to expand CIDRs or wrangle a list of IPs back to its smallest CIDR blocks possible.

#### Usage
`ipwrangle` is installed as two command-line utility accessible as `ipreduce` and `ipexpand` from the command-line.

You can use it them to convert a CIDR notation into the list of IP addresses contained in the block or reduce a list of IP addresses into its smallest CIDR blocks possible.

An example of expansion:

```
-$ ipexpand 192.0.2.0/24 | head -n10
192.0.2.0
192.0.2.1
192.0.2.2
192.0.2.3
192.0.2.4
192.0.2.5
192.0.2.6
192.0.2.7
192.0.2.8
192.0.2.9
```

Or reduction:
```text
-$ ipexpand 192.0.2.0/24 | head -n10 | ipreduce
192.0.2.0/29
192.0.2.8/31

```

Both tools accept commandline arguments (multiple entries split with a comma) or over stdin as multiline.


#### Bugs
Feel free to report issues, I build this tool simply because I couldn't find one that did exactly this.