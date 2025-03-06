# 0x1A. Application Server

## Project Overview
This project focuses on setting up an application server to serve dynamic content for the Airbnb clone project. The application server will be integrated with Nginx, which is already serving static content. The project involves configuring Gunicorn as the application server and ensuring seamless communication between Nginx and Gunicorn.

### Project Details
- **Weight**: 1
- **Start Date**: Mar 2, 2025, 6:00 PM
- **End Date**: Mar 6, 2025, 6:00 PM
- **Checker Release**: Mar 5, 2025, 8:24 AM
- **Auto Review**: Will be launched at the deadline

### Concepts Covered
- Web Server
- Server
- Web Stack Debugging

## Background Context
Your web infrastructure is already serving web pages via Nginx, which was set up in the first web stack project. While a web server can serve dynamic content, this task is typically handled by an application server. In this project, you will add an application server to your infrastructure, connect it to Nginx, and configure it to serve your Airbnb clone project.

## Resources
- [Application server vs web server](https://example.com)
- [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04](https://example.com)
- [Running Gunicorn](https://example.com)
- [Flask strict_slashes](https://example.com)
- [Upstart documentation](https://example.com)

## Requirements
### General
- A `README.md` file at the root of the project folder is mandatory.
- All Python-related tasks must be done using `python3`.
- All configuration files must include comments.
- All Bash scripts must be executable and pass Shellcheck without errors.
- The first line of all Bash scripts should be `#!/usr/bin/env bash`.
- The second line of all Bash scripts should be a comment explaining the script's purpose.

### Bash Scripts
- All files will be interpreted on Ubuntu 16.04 LTS.
- All files should end with a new line.
- All Bash script files must be executable.
- Bash scripts must pass Shellcheck (version 0.3.7-5~ubuntu16.04.1 via apt-get) without any errors.

### Servers
| Name          | Username | IP             | State    |
|---------------|----------|----------------|----------|
| 655284-web-01 | ubuntu   | 34.201.117.65  | running  |
| 655284-web-02 | ubuntu   | 44.204.24.63   | running  |
| 655284-lb-01  | ubuntu   | 44.211.126.136 | running  |

## Tasks

### 0. Set up development with Python
**Mandatory**

Set up your development environment on `web-01` to serve the Airbnb clone v2 - Web framework.

**Requirements:**
- Ensure task #3 of your SSH project is completed for `web-01`.
- Install the `net-tools` package: `sudo apt install -y net-tools`.
- Git clone your `AirBnB_clone_v2` on `web-01`.
- Configure `web_flask/0-hello_route.py` to serve content from the route `/airbnb-onepage/` on port 5000.
- The Flask application object must be named `app`.

**Example:**
```bash
# Window 1:
ubuntu@229-web-01:~/AirBnB_clone_v2$ python3 -m web_flask.0-hello_route
 * Serving Flask app "0-hello_route" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
35.231.193.217 - - [02/May/2019 22:19:42] "GET /airbnb-onepage/ HTTP/1.1" 200 -

# Window 2:
ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1:5000/airbnb-onepage/
Hello HBNB!ubuntu@229-web-01:~/AirBnB_clone_v2$

Author: Dzeble Baku Kwame
