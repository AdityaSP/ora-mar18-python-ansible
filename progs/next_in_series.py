#1. ask the user to enter an ip address
ip = input("Enter an ip address: ")

if ip.count('.') != 3:
    print("Wrongly formatted ip address.")
    exit(-1)
    
#2. next in series IP address
parts = ip.split('.')
part_4 = int(parts[-1]) + 1
parts[-1] = str(part_4)
print("Next in series: ", '.'.join(parts))