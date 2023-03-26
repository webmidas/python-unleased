import argparse

parser = argparse.ArgumentParser(description='Process some user information.')

parser.add_argument('username', type=str, help='the user\'s username')
parser.add_argument('last_name', type=str, help='the user\'s last name')

args = parser.parse_args()

print(f"User: {args.username}, Last Name: {args.last_name}")
