def get_info():
    print("=== APEX ENTERTAINMENT PASS GENERATOR ===\n")
    attendee = input("ATTENDEE: ")
    org = input("ORG: ")
    contact = input("CONTACT: ")
    access = input("ACCESS: ")
    
    issuer = "BCH Software Terminal System"
    
    print("\n\n")
    print("+--------------------------------------------------------------------------------+")
    print("|                         APEX ENTERTAINMENT PASS                                |")
    print("|--------------------------------------------------------------------------------|")
    print(f"| ATTENDEE : " + attendee.ljust(68) +"|")
    print(f"| ORG      : " + org.ljust(68) +"|")
    print(f"| CONTACT  : " + contact.ljust(68) +"|")
    print(f"| ACCESS   : " + access.ljust(68) +"|")
    print(f"| ISSUER   : " + issuer.ljust(68) +"|")
    print("+--------------------------------------------------------------------------------+")

get_info()