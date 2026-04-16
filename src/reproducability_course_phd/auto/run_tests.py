import subprocess


def run_tests():
    subprocess.run(["pytest"], check=False)
