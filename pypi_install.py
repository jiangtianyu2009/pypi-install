import sys
from pip import main as pip_main


def install(package):
    pip_main(['download', '-d', 'tmp_pkgs', package])


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            install(line)
