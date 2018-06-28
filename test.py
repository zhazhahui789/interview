import datetime
import subprocess
import os


def upload():
    date = datetime.datetime.today().isoformat()[0:10]
    init = subprocess.run(["git", "init"])
    gcren = subprocess.run(["git", "config", "--global", "credential.helper", "store"])
    gadd = subprocess.run(["git", "add","." ])
    gcom = subprocess.run(["git", "commit", "-m" + date])
    # grm = subprocess.run(["git","remote","rm","origin"])
    # gremote = subprocess.run(["git", "remote", "add", "origin", "https://github.com/zhazhahui789/123.git"])
    # gpull = subprocess.run(["git","pull","origin","master","--allow-unrelated-histories"])
    gpush = subprocess.run(["git", "push", "-u", "origin", "master"])


def main():
    upload()


if __name__ == '__main__':
    main()