def validate(ip):
    is_valid = True
    
    if ip.count('.') !=3:
        print("Wrongly formatted ip address. Exiting...")
        return False

    parts = ip.split('.')
    for part in parts:
        if not ( 0 <= int(part) <= 255):
            print("Not in range:", part, ". Exiting...")
            return False
            
    return is_valid    

        
#1. ask the user to enter an ip address
ip = input("Enter an ip address: ")

if not validate(ip):
    exit(-1)
    

parts = ip.split('.')
part_4 = int(parts[-1]) + 1
parts[-1] = str(part_4)
print("Next in series: ", '.'.join(parts))