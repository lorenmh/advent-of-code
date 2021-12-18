#!/usr/local/bin/python3

import os
import requests
import stat
import sys

solution_contents = '''#!/usr/local/bin/python3

import os

dir = os.path.dirname(os.path.realpath(__file__))

with open(f'{dir}/input', 'r') as f:
    input = f.read().splitlines()

for line in input:
    pass
'''

default_year = 2021

def write_solution(solution_path):
    if not os.path.exists(solution_path):
        with open(solution_path, 'w') as f:
            f.write(solution_contents)
        stat_info = os.stat(solution_path)
        os.chmod(solution_path, stat_info.st_mode | stat.S_IEXEC)

def main():
    session = os.getenv('SESSION')
    if session is None:
        print('session is required')
        os.exit(1)
    if len(sys.argv) < 1:
        print('day is required')
        os.exit(1)
    elif len(sys.argv) == 2:
        year = default_year
        day = sys.argv[1]
    elif len(sys.argv) == 3:
        year = sys.argv[1]
        day = sys.argv[2]
    else:
        print('too many args')
        os.exit(1)
    workdir = os.path.dirname(os.path.realpath(__file__))
    path = f'{workdir}/{year}/{day}'
    os.makedirs(path, mode=0o777, exist_ok=True)
    url_path = f'https://adventofcode.com/{year}/day/{day}/input'
    resp = requests.get(url_path, headers={'cookie': f'session={session}'})
    input_path = f'{path}/input'
    solution_path_1 = f'{path}/solution-1.py'
    solution_path_2 = f'{path}/solution-2.py'
    with open(input_path, 'w') as f:
        f.write(resp.text)
    write_solution(solution_path_1)
    write_solution(solution_path_2)

if __name__ == '__main__':
    main()
