# What is Cuckoo Sandbox?

Cuckoo is an open source automated malware analysis system. It’s used to automatically run and analyze files and collect comprehensive analysis results that outline what the malware does while running inside an isolated operating system. It can retrieve the following type of results:

  1. Traces of calls performed by all processes spawned by the malware.
  2. Files being created, deleted and downloaded by the malware during its execution.
  3. Memory dumps of the malware processes.
  4. Network traffic trace in PCAP format.
  5. Screenshots taken during the execution of the malware.
  6. Full memory dumps of the machines.

# What is Cuckins?

Cuckins is a tool that designed to install cuckoo sandbox required packages and tools automatically. This script required Python 3+ and Pip3 to work correctly, so before running this script please install Python3 and Pip3. Also, I should mention here, This script just tested successfully on Ubuntu 16 x64. Furthermore, you have to install virtualbox on your system, because I assume you want to work with this virtualization software with by Cuckoo Sandbox. 

## Requirements:
  1. Ubuntu 16 x86-x64
  2. Python 3+
  3. Pip3
  4. git

# How to run the program?
In order to run this program correctly, you must have root privilege upon linux machine. So, you have to run this program with following command:

> sudo python3 main.py
