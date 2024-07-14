# ssh-keygen
This is a pure python implementation of `ed25519` key generation, with the support for seeded key generation so that you can create a pair of ssh keys from any string you like.

## Security & Disclaimer
The author of this project is **NOT** a cryptography expert and provide **ZERO** guarantee on the security of this tool.

**USE IT AT YOUR OWN RISK.**

To the best of the author's knowledge, this tool has the following characteristics:
* It may suffer from timing attacks, so the key generation process must not be timed by a potential attacker.
* After generation, the key pair is cryptographically safe to use:
  * The private key cannot be recovered from the public key.
  * The seed cannot be recovered from the public key or private key or both.

## Install
```bash
pip install ssh-keygen
```

## Usage
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

## Acknowledgements
This project refers to the following sources:
* `ed25519` python implementation: https://github.com/pyca/ed25519/blob/main/ed25519.py
* OpenSSH private key format: https://coolaj86.com/articles/the-openssh-private-key-format/
* `balloon` password hashing: https://github.com/nachonavarro/balloon-hashing/blob/master/balloon.py