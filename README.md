Secure Network Asset Inventory & System Information Scanner

1. Project Overview

The Secure Network Asset Inventory & System Information Scanner is a Python-based command-line security utility developed as part of the Cyber Security & Ethical Hacking Internship — Task 1.

The purpose of the project is to automatically collect basic system and network information from a Linux system and generate a structured inventory report.

Manual collection of system information can be time-consuming and difficult to maintain. This tool provides a lightweight way to gather important host information from the command line.

2. Objectives

The project aims to:

* Identify the system hostname.
* Retrieve the local IP address.
* Retrieve the MAC address.
* Identify the operating system and version.
* List active network interfaces.
* Display CPU and memory information.
* Display disk usage information.
* Identify system architecture.
* Display the installed Python version.
* Generate a timestamped system inventory report.
* Save the collected information to a text file.
* Provide a menu-driven command-line interface.

3. Technologies Used

* Programming Language: Python
* Operating System: Kali Linux
* Virtualization: UTM
* Version Control: Git
* Repository: GitHub
* Libraries/Modules:
    * socket
    * platform
    * uuid
    * subprocess
    * psutil
    * shutil
    * datetime

4. Project Architecture

Kali Linux
    │
    ▼
Python Inventory Scanner
    │
    ├── Hostname
    ├── IP Address
    ├── MAC Address
    ├── Operating System
    ├── Network Interfaces
    ├── CPU & Memory
    ├── Disk Usage
    ├── Architecture
    └── Python Version
            │
            ▼
     Structured Report
            │
            ▼
 inventory_report.txt

5. Main Features

System Information

The application collects:

* Hostname
* Local IP address
* MAC address
* Operating system
* Operating system version
* System architecture
* Python version

Network Information

The application identifies active network interfaces and displays their network configuration.

Hardware Information

The application collects:

* CPU core count
* Total memory
* Total disk space
* Used disk space
* Free disk space

Report Generation

Every scan includes a timestamp and is saved as:

inventory_report.txt

Menu-Driven Interface

The application provides three options:

1. Scan System
2. View Saved Report
3. Exit

6. Project Structure

secure-network-inventory/
│
├── inventory.py
├── inventory_report.txt
├── README.md
├── .gitignore
└── venv/

The venv/ directory is a local Python virtual environment and is excluded from Git using .gitignore.

7. Requirements

* Kali Linux or another Linux-based operating system
* Python 3
* Python virtual environment support
* psutil
* Git

8. Installation

Clone the repository:

git clone https://github.com/rutulparate0305/secure-network-inventory.git

Enter the project directory:

cd secure-network-inventory

Create a Python virtual environment:

python3 -m venv venv

Activate the virtual environment:

source venv/bin/activate

Install the required Python package:

pip install psutil

9. Running the Application

Run:

python3 inventory.py

The menu will appear:

================================
 Secure Network Asset Inventory
================================
1. Scan System
2. View Saved Report
3. Exit

Select 1 to perform a system scan.

Select 2 to view the previously saved report.

Select 3 to exit the application.

10. Example Output

SECURE NETWORK ASSET INVENTORY
==============================
Scan Time: <timestamp>
Hostname: <hostname>
IP Address: <IP address>
MAC Address: <MAC address>
Operating System: Linux
Operating System Version: <version>
Network Interfaces:
<interface information>
CPU Cores: <number>
Memory: <memory>
Disk Total: <size>
Disk Used: <size>
Disk Free: <size>
Python Version: <version>
Architecture: <architecture>

11. Security Relevance

System and network asset information is an important part of cybersecurity because security teams need visibility into the systems they manage.

An inventory utility can help establish basic information about a host before further security assessment activities are performed.

This project demonstrates the foundation for automated asset discovery and system information collection.

12. Learning Outcomes

Through this project, the following concepts were practiced:

* Linux command-line administration
* Networking fundamentals
* Python system information collection
* Network interface inspection
* File handling in Python
* Virtual environments
* Git version control
* GitHub repository management
* Technical documentation
* Basic cybersecurity automation

13. Future Enhancements

Possible future improvements include:

* JSON report generation
* CSV report generation
* Installed software detection
* Application event logging
* Multiple-system/network-wide inventory
* Additional network information
* Automated report management

14. Disclaimer

This project is intended for educational and authorized cybersecurity purposes.

It should only be used on systems and networks for which the user has permission to perform security-related activities.

15. Author

Rutul Parate

