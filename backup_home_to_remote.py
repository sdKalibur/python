#!/usr/bin/env python3
import subprocess
import os
from multiprocessing import Pool

user = "kalibur"
# dest = "/tmp/" + user  + "/"
dest = "/kal-net/backup/kal-inspiron/home/" + user  + "/"
#backup_host = 'localhost'
backup_host = 'kal-bunker'
user_home = "/home/" + user + '/'


def backup_job(item):
    """ Spins backups threads """
    print("Backing up : {} ".format(item))
    subprocess.run(["echo","rsync","-arihvv", user_home + item," " , backup_host+':'+dest])

def check_free_space():
    """checks if there is enought space on remote system"""
    subprocess.run(["ssh",backup_host, "du -h", dest ]])
    # get output

def used_space():
    pass


if __name__ == "__main__":
    """setup direction varaialbes and call multithreading Pools."""

    bk_files = [ files for base_dir, child_dir, files in os.walk(user_home)]
    bk_dirs = [ dirs for base_dir, dirs, files in os.walk(user_home)]
    targets =  bk_files[0] + bk_dirs[0]
    # Create a pool of specific number of CPUs
    p = Pool(len(targets))
    print(p)
    # Start each task within the pool

    free_space = check_free_space()
    used_space = Check_required_space()
    
    if 

    try:
        p.map( backup_job, targets)
    except Exception as e:
        print(e)

