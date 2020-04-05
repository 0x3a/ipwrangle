# ipwrangle
Simple python-based command-line utilities to work with CIDRs individual IPs.

#### Usage
`ipwrangle` is installed as four command-line utility accessible as `innet`, `netlen`, `ipreduce` and `ipexpand` from the command-line.

You can use it them to convert a CIDR notation into the list of IP addresses contained in the block, reduce a list of IP addresses into its smallest CIDR blocks possible, calculate a CIDR block size or check if an IP is in a CIDR block.

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

Reduction:
```text
-$ ipexpand 192.0.2.0/24 | head -n10 | ipreduce
192.0.2.0/29
192.0.2.8/31
```

Network size:
```text
-$ netlen netlen 2001:db4::/56
4722366482869645213696
```

IP in CDIR block, this utility writes on stderr (for human reading) but also has a return code of 0 (true) -1 (false) to use in automation:
```text
 innet 192.168.0.1 192.168.0.0/24
true
-$ echo $?
0
-$ innet 192.169.0.1 192.168.0.0/24
false
-$ echo $?
255
```

All tools besides `innet` accept data as commandline arguments (multiple entries split with a comma) or through stdin as multiline.


#### Bugs
Feel free to report issues, I build these tools simply because I couldn't find ones that did exactly this.