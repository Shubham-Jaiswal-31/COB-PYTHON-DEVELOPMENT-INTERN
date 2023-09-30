# A program to Validate an IPv4 Address
# Written by Shubham Anand Jaiswal

# function to check if each part is between 0-255
def within_range(num): 
    if num >= 0 and num <= 255:
        return True
    return False

# function to check if each part has a leading zero.
def has_leading_zero(n):
    if len(n) > 1:
        if n[0] == "0":
            return True
    return False

# function to check if it's a valid IPv4 address
def isValid(s):
    # split the address by period in parts list
    parts = s.split(".")
    #if number of parts are not 4, address is invalid
    if len(parts) != 4:
        return False
    
    # loop thorugh each part and check further conditions
    for part in parts:
        # address is invalid if leading zeroes exist
        if has_leading_zero(part):
            return False
        # address is invalid if part does not have any character
        if len(part) == 0:
            return False
        
        # to handle the error if int(part) is not an integer
        try: 
            part = int(part)
            # address is invalid if not within 0 and 255
            if not within_range(part):
                return False
        except:
            # address is invalid if each part is not an integer
            return False
    # return true if all conditions are satisfied
    return True

# main code
if __name__=="__main__":
    
    # Receive the address to check from user
    address = input("Enter IPv4 Address: ")
    
    # Check if valid address and display a message
    if isValid(address):
        print(f"{address} is a valid IPv4 address")
    else:
        print(f"{address} is Invalid")
