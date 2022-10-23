if __name__ == '__main__':
    pkgs = []
    pkgs_sorted = []
    with open("pypi-install/requirements.txt") as req_file:
        pkgs = req_file.readlines()
        pkgs_sorted = sorted(list(set(pkgs)))
        print(len(pkgs))
        print(len(pkgs_sorted))
    with open("pypi-install/requirements1.txt", 'w') as req_file1:
        req_file1.writelines(pkgs_sorted)
