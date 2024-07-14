"""ssh-keygen

# Usage
Generate a private/public key pair:

```bash
# Interactive mode (launch a key generation wizard)
python -m ssh_keygen

# Command line mode
#   -s <seed_string>  Option 1: use seed string
#   -f <file>         Option 2: use seed file
#   --random          Option 3: use random 128-bit string
#   -o <path>         Path to save the private key file
#   -n <N=1024>       The number of hash iterations for seed string
#                     Larger N is safer but takes more time.
#   -C <comment>      Comment for the generate key
python -m ssh_keygen -s "this is a seed string" -o "/path/to/save/private_key"
python -m ssh_keygen -f "/path/to/seed_file"    -o "/path/to/save/private_key"
```
"""

__version__ = '1.0.2'
