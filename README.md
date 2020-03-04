# ipwrangle
A simple python-based command-line utility to expand CIDRs or wrangle a list of IPs back to its smallest CIDR blocks possible.

#### Usage
`ipwrangle` is installed as two command-line utility accessible as `ipreduce` and `ipexpand` from the command-line.

You can use it them to convert a CIDR notation into the list of IP addresses contained in the block or reduce a list of IP addresses into its smallest CIDR blocks possible.

An example of expansion:

```
-$ ipexpand 127.0.0.0/24
127.0.0.1
127.0.0.2
127.0.0.3
127.0.0.4
...
```

Or reduction:
```text
-$ ipreduce 127.0.0.1,127.0.0.2

```

Both tools accept commandline arguments (multiple entries split with a comma) or over stdin as multiline.


#### Bugs
Feel free to report issues, I build this tool simply because I couldn't find one that did exactly this.