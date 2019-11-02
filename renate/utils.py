import math
import time
import logging
import itertools

import paramiko


def download_file_from_pepper(config, remote_path, local_path):
    """Download a file via SFTP from the pepper to a local file system."""
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(
            config.Ip,
            username=config.Username,
            password=config.Password
    )
    sftp = ssh.open_sftp()
    sftp.get(remote_path, local_path)
    sftp.remove(remote_path)
    sftp.close()
    ssh.close()


def upload_file_to_pepper(config, local_path, remote_path):
    """Upload a file to the pepper."""
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(
            config.Ip,
            username=config.Username,
            password=config.Password
    )
    sftp = ssh.open_sftp()
    sftp.put(local_path, remote_path)
    sftp.close()
    ssh.close()

