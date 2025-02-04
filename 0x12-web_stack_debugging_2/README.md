# 0x12. Web Stack Debugging #2

## Project Overview
This project focuses on debugging and securing web server configurations. It involves running software as a non-root user, ensuring Nginx runs as the `nginx` user, and debugging web server issues. The goal is to improve security by limiting the privileges of the user running the web server.

## Project Details
- **Weight**: 1
- **Start Date**: Feb 2, 2025, 6:00 PM
- **End Date**: Feb 4, 2025, 6:00 PM
- **Checker Release**: Feb 4, 2025, 1:12 AM
- **Auto Review**: Launched at the deadline

## Concepts Covered
- Web Stack Debugging

## Requirements
### General
- All files will be interpreted on Ubuntu 20.04 LTS
- All files should end with a new line
- A `README.md` file at the root of the project folder is mandatory
- All Bash script files must be executable
- Bash scripts must pass Shellcheck without any errors
- Bash scripts must run without errors
- The first line of all Bash scripts should be `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining what the script does

## Tasks

### 0. Run software as another user
**Mandatory**
- Write a Bash script that accepts one argument.
- The script should run the `whoami` command under the user passed as an argument.
- Example:
  ```bash
  root@ubuntu:~# whoami
  root
  root@ubuntu:~# ./0-iamsomeoneelse www-data
  www-data
  root@ubuntu:~# whoami
  root

Author: Dzeble Kwame 
