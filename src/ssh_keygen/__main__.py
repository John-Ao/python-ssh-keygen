import argparse
import getpass
import os
import secrets
import socket

from .keygen import gen_pk, gen_sk, write_files

DEFAULT_N_ITER = 1024

parser = argparse.ArgumentParser()
parser.add_argument('-s', metavar='seed', type=str, help='the seed string')
parser.add_argument('-f', metavar='file', type=str, help='the seed file')
parser.add_argument('--random', action='store_true', help='use random seed')
parser.add_argument('-o', metavar='path', type=str, help='path to save the private key file')
parser.add_argument('-y', action='store_true', help='overwrite files if exist')
parser.add_argument('-C', metavar='comment', type=str, help='comment')
parser.add_argument('-n', type=int, help='the number of hash iterations for seed string', default=DEFAULT_N_ITER)
args = parser.parse_args()

print('Generating public/private ed25519 key pair.')

if args.s is not None and args.f is not None:
    print('Error: please use either `-s` or `-f`.')
    exit()
if args.s is not None:
    seed = args.s.encode('utf8')
elif args.f is not None:
    with open(args.f, 'rb') as f:
        seed = f.read()
elif args.random:
    seed = secrets.token_bytes(64)
else:
    seed = input('Enter the seed string: ').encode('utf8')

if args.o is None:
    default_path = os.path.expanduser('~/.ssh/id_ed25519')
    output_path = input(f'Enter file in which to save the key ({default_path}): ')
    if output_path == '':
        output_path = default_path
else:
    output_path = args.o
if (
    os.path.exists(output_path) or
    os.path.exists(output_path+'.pub')
):
    if not args.y:
        print(f'File already exists. {output_path}.')
        if input('Overwrite (y/n)? ') != 'y':
            exit()

comment = args.C
if comment is None:
    comment = getpass.getuser()+'@'+socket.gethostname()

sk = gen_sk(seed, args.n)
pk = gen_pk(sk)
write_files(sk, pk, comment, output_path)
print(f'Your identification has been saved in {output_path}.')
print(f'Your public key has been saved in {output_path}.pub.')
