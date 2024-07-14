import base64
import textwrap

from .balloon import balloon
from .ed25519 import publickey_unsafe as gen_pk  # keep this

SALT = 'python-ssh-keygen by John Ao'
MEMORY = 2048


def gen_sk(seed, n_iter):
    return balloon(seed, SALT, MEMORY, n_iter)


def write_files(sk, pk, comment, output_path):
    # ref: https://coolaj86.com/articles/the-openssh-private-key-format/
    c = comment.encode('utf8')
    sf_1 = (
        b'openssh-key-v1\x00'
        b'\x00\x00\x00\x04none'
        b'\x00\x00\x00\x04none'
        b'\x00\x00\x00\x00'
        b'\x00\x00\x00\x01'
        b'\x00\x00\x003'
        b'\x00\x00\x00\x0bssh-ed25519'
        b'\x00\x00\x00 '
        + pk
    )
    sf_2 = (
        b'a\xbbsHa\xbbsH'
        b'\x00\x00\x00\x0bssh-ed25519'
        b'\x00\x00\x00 '
        + pk
        + b'\x00\x00\x00@'
        + sk
        + pk
        + len(c).to_bytes(4, 'big')
        + c
    )
    sf_2 = (sf_2+bytes(range(1, 8)))[:(len(sf_2)+7)//8*8]
    sf = base64.b64encode(sf_1+len(sf_2).to_bytes(4, 'big')+sf_2).decode('utf8')

    pf = b'\x00\x00\x00\x0bssh-ed25519\x00\x00\x00 '+pk
    pf = base64.b64encode(pf).decode('utf8')

    with open(output_path, 'w', encoding='utf8') as f:
        f.write('-----BEGIN OPENSSH PRIVATE KEY-----\n')
        f.write('\n'.join(textwrap.wrap(sf, 70)))
        f.write('\n-----END OPENSSH PRIVATE KEY-----\n')

    with open(output_path+'.pub', 'w', encoding='utf8') as f:
        f.write(f'ssh-ed25519 {pf} {comment}\n')
