import shutil
import psutil
def check_disk(disk):
    du = shutil.disk_usage(disk)
    free = du.free*100/du.total
    return free > 20
def check_cpu():
    usage = psutil.cpu_percent(1)
    return usage < 75

if not check_disk("/") and not check_cpu():
    print("ERRR!!")
else:
    print("OK")
