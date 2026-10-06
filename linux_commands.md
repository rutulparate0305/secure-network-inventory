Linux Command Documentation

Cyber Security & Ethical Hacking Internship — Task 1

This document records the Linux commands practiced during the Cyber Security & Ethical Hacking Internship Task 1. The commands cover filesystem navigation, file management, user management, permissions, system information, and basic administration.

⸻

1. Navigation Commands

pwd

Displays the current working directory.

pwd

ls

Lists files and directories in the current directory.

ls

ls -la

Displays detailed information, including hidden files.

ls -la

cd

Changes the current directory.

cd /tmp

Return to the user’s home directory:

cd ~

⸻

2. Directory and File Management

mkdir

Creates a new directory.

mkdir task1_test

touch

Creates an empty file.

touch test.txt

echo

Writes text to a file.

echo "Cyber Security Task 1" > test.txt

cat

Displays the contents of a file.

cat test.txt

cp

Copies a file.

cp test.txt copy.txt

mv

Moves or renames a file.

mv copy.txt renamed.txt

rm

Removes a file.

rm renamed.txt

rmdir

Removes an empty directory.

rmdir task1_test

A directory must be empty before rmdir can remove it.

⸻

3. User Information

whoami

Displays the currently logged-in username.

whoami

id

Displays the user ID, group ID, and group membership information.

id

id taskuser

Displays identity information for a specific user.

id taskuser

groups

Displays the groups associated with a user.

groups taskuser

⸻

4. User and Group Administration

useradd

Creates a new Linux user.

sudo useradd -m taskuser

The -m option creates a home directory for the user.

passwd

Sets or changes a user’s password.

sudo passwd taskuser

groupadd

Creates a new group.

sudo groupadd securityteam

usermod

Adds an existing user to a supplementary group.

sudo usermod -aG securityteam taskuser

getent group

Displays information about a group.

getent group securityteam

⸻

5. Creating Project Directories

The Task 1 practice environment included a dedicated directory structure.

mkdir ~/linux_task
cd ~/linux_task
mkdir reports logs
touch reports/system.txt
touch logs/activity.log

The resulting structure is:

linux_task/
├── reports/
│   └── system.txt
├── logs/
│   └── activity.log
└── permissions.txt

⸻

6. File Permissions

ls -l

Displays file permissions and ownership information.

ls -l permissions.txt

chmod

Changes file permissions.

For owner-only read/write access:

chmod 600 permissions.txt

For owner read/write and everyone else read access:

chmod 644 permissions.txt

The permission values are based on three categories:

* Owner
* Group
* Others

The numeric permission values represent:

4 = Read
2 = Write
1 = Execute

Therefore:

600 = Owner: read + write
      Group: no permissions
      Others: no permissions
644 = Owner: read + write
      Group: read
      Others: read

⸻

7. System Information Commands

date

Displays the current system date and time.

date

uname -a

Displays detailed information about the Linux kernel and system.

uname -a

df -h

Displays filesystem disk-space usage in human-readable format.

df -h

free -h

Displays memory usage in human-readable format.

free -h

⸻

8. Networking Commands

ip addr

Displays network interfaces and IP address information.

ip addr

ip route

Displays the system’s routing table.

ip route

ping

Tests network connectivity.

ping -c 4 8.8.8.8

The -c 4 option sends four packets.

DNS/network connectivity can also be tested using:

ping -c 4 google.com

ss -tuln

Displays listening TCP and UDP network sockets.

ss -tuln

Options:

* -t — TCP
* -u — UDP
* -l — Listening sockets
* -n — Display numerical addresses and ports

⸻

9. Package Management

The Kali Linux system was updated using:

sudo apt update

This refreshes the available package information.

Packages can then be upgraded using:

sudo apt upgrade -y

The -y option automatically confirms the upgrade prompts.

⸻

10. Git Commands Used in the Project

git init

Initializes a Git repository in the project directory.

git init

git status

Displays the current Git repository status.

git status

git add

Stages files for the next commit.

git add inventory.py inventory_report.txt .gitignore

git commit

Creates a version-controlled snapshot of the staged files.

git commit -m "Initial Secure Network Asset Inventory project"

git log --oneline

Displays the project’s commit history in a compact format.

git log --oneline

git push

Uploads local commits to the remote GitHub repository.

git push

⸻

11. Security Relevance

Linux command-line administration is an important foundation for cybersecurity work.

The commands practiced in this task provide basic capabilities for:

* Navigating Linux systems
* Managing files and directories
* Managing users and groups
* Understanding file permissions
* Inspecting system resources
* Checking network configuration
* Testing network connectivity
* Inspecting listening network services
* Managing software packages
* Maintaining project version history

These skills support later cybersecurity activities such as system administration, reconnaissance, security assessment, and vulnerability analysis.

⸻

12. Summary

The Linux exercises completed during Task 1 provided practical experience with:

* Linux filesystem navigation
* File and directory management
* User and group management
* File permissions
* System information
* Network configuration
* Connectivity testing
* Package management
* Git and GitHub version control

These commands were practiced in the Kali Linux cybersecurity lab environment used for the Task 1 project.
