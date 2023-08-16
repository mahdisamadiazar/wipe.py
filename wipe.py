import subprocess

disks = ['/dev/sda', '/dev/sdb']  # List of disks to wipe

for disk in disks:
    print(f"Wiping {disk}...")
    command = f"sudo dd if=/dev/zero of={disk} bs=4M status=progress"
    subprocess.run(command, shell=True, check=True)    
    command2 = f"sudo badblocks -sv {disk}"	
    subprocess.run(command2, shell=True, check=True)

    result = f"Wiping {disk} finished."
    with open("wipe_result.txt", "a") as file:
        file.write(result + "\n")
    print(result)

