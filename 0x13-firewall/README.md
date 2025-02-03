## Firewall Project

This project focuses on configuring and managing firewalls using **UFW (Uncomplicated Firewall)**. The goal is to secure your servers by blocking all incoming traffic except for specific ports (SSH, HTTP, and HTTPS).

---

### Project Information
- **Weight:** 1
- **Start Date:** Feb 2, 2025 6:00 PM
- **End Date:** Feb 3, 2025 6:00 PM
- **Checker Release:** Feb 3, 2025 12:00 AM
- **Auto Review:** Will be launched at the deadline

---

### Background Context
Firewalls are essential for securing servers by controlling incoming and outgoing network traffic. In this project, you will configure a firewall to block all incoming traffic except for specific ports (SSH, HTTP, and HTTPS) on your server.

---

### Concepts
This project covers the following concept:
- **Web Stack Debugging**

---

### Resources
#### Read or Watch:
- [What is a Firewall?](https://en.wikipedia.org/wiki/Firewall_(computing))

---

### More Information
#### Testing with Telnet
You can use `telnet` to check if ports are open. For example:
```bash
$ telnet web-02.holberton.online 22
Trying 54.89.38.100...
Connected to web-02.holberton.online.
Escape character is '^]'.
SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.8

Protocol mismatch.
Connection closed by foreign host.

Author: Dzeble Kwame
