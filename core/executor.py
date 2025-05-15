# core/executor.py
import subprocess

def execute(command: str):
    subprocess.run(command, shell=True)