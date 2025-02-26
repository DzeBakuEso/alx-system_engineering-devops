## 0x17. Web Stack Debugging #3

### DevOps | SysAdmin | Scripting | Debugging

**Weight:** 1  
**Project Start:** Feb 24, 2025, 6:00 PM  
**Project End:** Feb 26, 2025, 6:00 PM  
**Checker Release:** Feb 26, 2025, 1:12 AM  
**Auto Review:** Launched at the deadline

---

### Concepts

For this project, we expect you to look at the following concepts:

- **Web Server**
- **Web Stack Debugging**

---

### Background Context

When debugging, sometimes logs are not enough. Either because the software is breaking in a way that was not expected and the error is not being logged, or because logs are not providing enough information. In this case, you will need to go down the stack. The good news is that this is something students can do :)

WordPress is a very popular tool that allows you to run blogs, portfolios, e-commerce, and company websites. It actually powers 26% of the web, so there is a fair chance that you will end up working with it at some point in your career.

WordPress is usually run on LAMP (Linux, Apache, MySQL, and PHP), which is a very widely used set of tools.

The web stack you are debugging today is a WordPress website running on a LAMP stack.

---

### Requirements

#### General

- All your files will be interpreted on Ubuntu 14.04 LTS.
- All your files should end with a new line.
- A `README.md` file at the root of the folder of the project is mandatory.
- Your Puppet manifests must pass `puppet-lint` version 2.1.1 without any errors.
- Your Puppet manifests must run without error.
- Your Puppet manifests' first line must be a comment explaining what the Puppet manifest is about.
- Your Puppet manifests files must end with the extension `.pp`.
- Files will be checked with Puppet v3.4.

---

### More Info

#### Install `puppet-lint`

```bash
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1

Author:Dzeble Baku Kwame
