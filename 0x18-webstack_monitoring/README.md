# 0x18. Webstack Monitoring

## Project Overview
This project focuses on **Webstack Monitoring**, a crucial aspect of **DevOps** and **SysAdmin** practices. Monitoring allows us to measure and improve the performance of our software systems. The project is divided into tasks that involve setting up monitoring tools, configuring metrics, and creating dashboards to visualize server and application performance.

- **Weight**: 1
- **Start Date**: Feb 25, 2025, 6:00 PM
- **End Date**: Feb 26, 2025, 6:00 PM
- **Checker Release**: Feb 26, 2025, 12:00 AM
- **Auto Review**: Launched at the deadline

---

## Concepts Covered
For this project, you will explore the following concepts:
- **Monitoring**
- **Server**

---

## Background Context
The saying, *“You cannot fix or improve what you cannot measure”*, highlights the importance of monitoring in the tech industry. In this project, you will implement tools to measure and analyze the performance of your servers. Web stack monitoring can be broken down into two categories:
1. **Application Monitoring**: Collecting data about your running software to ensure it behaves as expected.
2. **Server Monitoring**: Collecting data about your virtual or physical servers to ensure they are not overloaded (e.g., CPU, memory, disk, or network overload).

---

## Resources
### Read or Watch:
- [What is Server Monitoring?](https://www.datadoghq.com/blog/server-monitoring/)
- [What is Application Monitoring?](https://www.datadoghq.com/blog/application-monitoring/)
- [System Monitoring by Google](https://cloud.google.com/monitoring)
- [Nginx Logging and Monitoring](https://www.nginx.com/blog/logging-and-monitoring-nginx/)

---

## Learning Objectives
By the end of this project, you should be able to explain the following without using Google:
- Why monitoring is needed.
- The two main areas of monitoring.
- What access logs and error logs are for a web server (e.g., Nginx).

---

## Requirements
### General
- Allowed editors: `vi`, `vim`, `emacs`.
- Files will be interpreted on **Ubuntu 16.04 LTS**.
- All files must end with a new line.
- A `README.md` file at the root of the project folder is mandatory.
- All Bash script files must be executable.
- Bash scripts must pass **Shellcheck (version 0.3.7)** without errors.
- The first line of all Bash scripts should be `#!/usr/bin/env bash`.
- The second line of all Bash scripts should be a comment explaining what the script does.

---

## Servers
| Name          | Username | IP            | State    |
|---------------|----------|---------------|----------|
| 655284-web-01 | ubuntu   | 54.172.165.35 | running  |
| 655284-web-02 | ubuntu   | 34.232.69.16  | running  |
| 655284-lb-01  | ubuntu   | 54.89.179.11  | running  |

---

## Tasks

### 0. Sign Up for Datadog and Install Datadog Agent
**Mandatory**
1. Sign up for a free Datadog account at [Datadog](https://app.datadoghq.com).
   - Use the **US1 region**.
2. Install the Datadog agent on `web-01`.
3. Create an application key.
4. Copy-paste your **Datadog API key** and **application key** into your Intranet user profile.
5. Ensure your server `web-01` is visible in Datadog under the hostname `XX-web-01`.
   - Validate this using the [Datadog API](https://docs.datadoghq.com/api/).

**Repo:**
- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x18-webstack_monitoring`

---

### 1. Monitor Some Metrics
**Mandatory**
Set up monitors in the Datadog dashboard to track system metrics such as:
- Number of read requests issued to the device per second.
- Number of write requests issued to the device per second.

Refer to [System Check](https://docs.datadoghq.com/integrations/system/) for more details on system metrics.

**Repo:**
- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x18-webstack_monitoring`

---

### 2. Create a Dashboard
**Mandatory**
1. Create a new dashboard in Datadog.
2. Add at least 4 widgets to monitor various metrics.
3. Create a file named `2-setup_datadog` with the `dashboard_id` on the first line.
   - Use the [Datadog API](https://docs.datadoghq.com/api/) to retrieve the dashboard ID if needed.

**Repo:**
- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x18-webstack_monitoring`
- File: `2-setup_datadog`

---

## Copyright and Plagiarism
- You are required to come up with solutions for the tasks yourself to meet the learning objectives.
- Copying and pasting someone else’s work is strictly forbidden and will result in removal from the program.
- You are not allowed to publish any content of this project.

Author:Dzeble Baku Kwame 
