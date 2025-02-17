import os
import subprocess

def start_pgadmin():
    print("Starting pgAdmin...")
    subprocess.run(["/usr/local/bin/python3", "/usr/local/lib/python3.*/site-packages/pgadmin4/pgAdmin4.py"])

if __name__ == "__main__":
    start_pgadmin()