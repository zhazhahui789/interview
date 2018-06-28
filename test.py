import datetime
import subprocess
import os


def upload(path):
    date = datetime.datetime.today().isoformat()[0:10]
    init = subprocess.run(["git", "init",path])
    gcren = subprocess.run(["git", "config", "--global", "credential.helper", "store"])
    path1 = path+"\\"
    gadd = subprocess.run(["git", "add","." ])
    gcom = subprocess.run(["git", "commit", "-m" + date])
    gremote = subprocess.run(["git", "remote", "add", "origin", "https://github.com/zhazhahui789/111.git"])
    gpush = subprocess.run(["git", "push", "-u", "origin", "master"])


def main():
    Path = input("请输入需要push的路径：")
    upload(Path)


if __name__ == '__main__':
    main()