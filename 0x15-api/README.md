# 0x15. API - Python Scripting and Back-end Development

## Project Overview

This project focuses on interacting with an API to gather and manipulate employee data. The goal is to create Python scripts that fetch data from a REST API, process it, and export it in both CSV and JSON formats. This project is designed to help you understand the limitations of Bash scripting and the advantages of using Python for such tasks.

## Background Context

Traditional system administrators often rely on Bash for scripting, but modern system administrators (SREs) use more advanced programming languages like Python. APIs are a common way to expose applications and datasets, allowing external systems to interact with them. In this project, you will work with an API to access employee data, organize it, and export it to different data structures.

## Learning Objectives

By the end of this project, you should be able to explain the following concepts without relying on external resources:

- **General:**
  - Limitations of Bash scripting
  - What an API is
  - What a REST API is
  - What microservices are
  - CSV and JSON formats
  - Pythonic naming conventions for packages, modules, classes, variables, functions, and constants
  - The significance of CapWords or CamelCase in Python

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- Libraries imported in your Python files must be organized in alphabetical order
- A `README.md` file at the root of the project folder is mandatory
- Your code should use `pycodestyle` (version 2.8.*)
- All files must be executable
- The length of your files will be tested using `wc`
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- You must use `get` to access dictionary values by key
- Your code should not be executed when imported (use `if __name__ == "__main__":`)

## Tasks

### 0. Gather Data from an API

**Mandatory**

Write a Python script that, using a REST API, fetches information about a given employee's TODO list progress.

**Requirements:**
- Use `urllib` or `requests` module
- Accept an integer as a parameter (employee ID)
- Display the employee's TODO list progress in a specific format

**Example:**
```bash
$ python3 0-gather_data_from_an_API.py 2
Employee Ervin Howell is done with tasks(8/20):
    distinctio vitae autem nihil ut molestias quo
    voluptas quo tenetur perspiciatis explicabo natus
    aliquam aut quasi
    veritatis pariatur delectus
    nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis
    repellendus veritatis molestias dicta incidunt
    excepturi deleniti adipisci voluptatem et neque optio illum ad
    totam atque quo nesciunt

Author: Dzeble Kwame
