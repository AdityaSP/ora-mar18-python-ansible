#1. ask the user to enter an ip address
ip = input("Enter an ip address: ")

if ip.count('.') != 3:
    print("Wrongly formatted ip address. Exiting...")
    exit(-1)

parts = ip.split('.')
#304, 127, 45 , 234
for part in parts:
    if not (int(part) >=0 and int(part) <=255):
        print("Not in range:", part, ". Exiting...")
        exit(-1)

part_4 = int(parts[-1]) + 1
parts[-1] = str(part_4)
print("Next in series: ", '.'.join(parts))