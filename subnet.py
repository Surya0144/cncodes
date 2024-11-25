# Function to split a string into parts based on a delimiter
def split(string, delimiter):
    return string.split(delimiter)

# Function to get the class of an IP address
def get_class(ip):
    first_byte = int(split(ip, '.')[0])
    if first_byte < 128:
        return 'A'
    elif first_byte < 192:
        return 'B'
    elif first_byte < 224:
        return 'C'
    elif first_byte < 240:
        return 'D'
    else:
        return 'E'

# Function to get the network mask based on the class and subnet bits
def get_network_mask(ip_class, subnet_bits):
    if ip_class == 'A':
        return f"255.{256 - (1 << (16 - subnet_bits))}.0.0"
    elif ip_class == 'B':
        return f"255.255.{256 - (1 << (8 - subnet_bits))}.0"
    elif ip_class == 'C':
        return f"255.255.255.{256 - (1 << (8 - subnet_bits))}"
    else:
        return "Invalid"

# Function to generate the subnet IP address
def generate_subnet(ip, subnet_mask):
    ip_parts = list(map(int, split(ip, '.')))
    subnet_mask_parts = list(map(int, split(subnet_mask, '.')))
    subnet_ip = '.'.join(str(ip_parts[i] & subnet_mask_parts[i]) for i in range(4))
    return subnet_ip

def main():
    ip = input("Enter IP address: ")
    subnet_bits = int(input("Enter subnet bits: "))
    ip_class = get_class(ip)
    print(f"Class of IP address: {ip_class}")
    
    if ip_class not in 'ABC':
        print("Subnetting is not applicable for this IP class.")
        return

    subnet_mask = get_network_mask(ip_class, subnet_bits)
    print(f"Network mask: {subnet_mask}")
    subnet_ip = generate_subnet(ip, subnet_mask)
    print(f"Subnet IP address: {subnet_ip}")

if __name__ == "__main__":
    main()
