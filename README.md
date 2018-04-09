# Madfuscator
Fully undetectable payload injection in Python

# Usage
Replace the payload and run the script with **python mad.py**.

# Is PyInstaller supported?
Yes. Run pyinstaller with --onefile and --windowed options and you are done.

# How it works
Mad will change variable names and will obfuscate the final source code. In addition it will generate a 3-characters long key to be used in a XOR-Brute force method until the original payload's MD5 Hash is found.

Be responsible.
