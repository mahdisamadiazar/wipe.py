import subprocess
import multiprocessing

command = "lsblk -o NAME -n -d | awk '/^sd/ {print $1}'"
output = subprocess.check_output(command, shell=True, text=True).splitlines()

dontwipe = "/dev/" + input("Select the disk you don't want to be wiped: ")

disks = []
for disk in output:
    if disk != dontwipe:
        disks.append("/dev/" + disk)


def wipe_disk(disk):
    print(f"Wiping {disk}...")
    command = f"sudo dd if=/dev/zero of={disk} bs=4M status=progress"
    subprocess.run(command, shell=True, check=True)    
    command2 = f"sudo badblocks -sv {disk}"	
    subprocess.run(command2, shell=True, check=True)

    result = f"Wiping {disk} finished."
    with open("wipe_result.txt", "a") as file:
        file.write(result + "\n")
    print(result)


# Create a process pool and map the wipe_disk function to each disk
with multiprocessing.Pool() as pool:
    pool.map(wipe_disk, disks)
