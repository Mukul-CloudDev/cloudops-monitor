# CloudOps Health Monitoring

A simple CloudOps health monitoring project built on AWS EC2 using Python, Docker, and Git.

## Project Overview

This project monitors the basic health of an EC2 Linux server.

It checks:

- CPU usage
- Memory usage
- Disk usage
- Overall system health status

The monitoring script generates a JSON health report.

## Technologies Used

- AWS EC2
- Ubuntu Linux
- Python 3
- psutil
- Docker
- Git
- GitHub

## Project Structure

```text
cloudops-monitor/
├── Dockerfile
└── scripts/
    ├── health_check.py
    └── health_report.json
