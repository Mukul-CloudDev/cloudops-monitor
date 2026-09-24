import psutil
import json
from datetime import datetime

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage("/").percent

status = "HEALTHY"

if cpu > 80 or memory > 80 or disk > 80:
    status = "WARNING"

report = {
    "timestamp": datetime.now().astimezone().isoformat(),
    "cpu_usage_percent": cpu, 
    "memory_usage_percent": memory,
    "disk_usage_percent": disk,
    "status": status
}

print("===== AI CloudOps Health Check =====")
print(f"CPU Usage: {cpu}%")
print(f"Memory Usage: {memory}%")
print(f"Disk Usage: {disk}%")
print(f"Status: {status}")

with open("health_report.json", "w") as file:
    json.dump(report, file, indent=4)

print("Report saved: health_report.json")
