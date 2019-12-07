import math
import time
import logging
import librosa
import madmom
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


def track_beat(file):
    """track the beats in a given file"""
    y, sr = librosa.load(file)
    tempo, beats = librosa.beat.beat_track(y, sr=sr)
    beat_times = librosa.frames_to_time(beats, sr=sr)
    return tempo, beat_times, y, sr  # tempo, beats

def track_accurate_beat(file):
    """track accurate beats with CMM"""
    logging.info("analyzing audio %s", file)
    start = time.time()
    y, sr = librosa.load(file)
    beat_times = madmom.features.beats.DBNBeatTrackingProcessor(fps=100)(
        madmom.features.beats.RNNBeatProcessor()(file)
    )
    end = time.time()
    logging.info("analyzing took: %s", end - start)
    return beat_times, y, sr