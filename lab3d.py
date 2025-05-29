#!/usr/bin/env python3
# Author ID: pshah116

import subprocess

def free_space():

    output = subprocess.run(
        "df -h | grep '/$' | awk '{print $4}'",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return output.stdout.decode('utf-8').strip()


if __name__ == '__main__':
    print(free_space())
