#!/usr/bin/env python3
import os
import subprocess
import time
from git import Repo

REPO_URL = "https://github.com/deinusername/brainrot"
LOCAL_PATH = "/home/pi/brainrot"

def clone_or_pull():
    if not os.path.exists(LOCAL_PATH):
        print("[+] Cloning repo ...")
        Repo.clone_from(REPO_URL, LOCAL_PATH)
    else:
        print("[+] Pulling latest changes ...")
        repo = Repo(LOCAL_PATH)
        origin = repo.remotes.origin
        origin.pull()

if __name__ == "__main__":
    while True:
        clone_or_pull()
        subprocess.run(["python3", f"{LOCAL_PATH}/main.py"])
        time.sleep(1800)
