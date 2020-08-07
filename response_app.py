import time
import sys

machinename = "vm-image-hackathon-1"

print("-----------------------")
for i in range(20):
    time.sleep(0.3)
    sys.stdout.write("\r"+machinename+"> .  ")
    sys.stdout.flush()
    time.sleep(0.3)
    sys.stdout.write("\r"+machinename+"> .. ")
    sys.stdout.flush()
    time.sleep(0.3)
    sys.stdout.write("\r"+machinename+"> ...")
    sys.stdout.flush()
print("\r"+machinename+"> New image submitted by user 22319")
print(machinename+"> Analysis running ...")
time.sleep(2)
print(machinename+"> 3 damages detected in Omiyacho, Wakaba-ku, Chiba 264-0016, Japan - returning to user for confirmation")
for i in range(50):
    time.sleep(0.3)
    sys.stdout.write("\r"+machinename+"> .  ")
    sys.stdout.flush()
    time.sleep(0.3)
    sys.stdout.write("\r"+machinename+"> .. ")
    sys.stdout.flush()
    time.sleep(0.3)
    sys.stdout.write("\r"+machinename+"> ...")
    sys.stdout.flush()