def get_info():
    print("=== APEX ENTERTAINMENT PASS GENERATOR ===\n")

    attendee = input("ATTENDEE: ")
    org = input("ORG: ")
    contact = input("CONTACT: ")
    access = input("ACCESS: ")
    issuer = input("ISSUER: ")

    print("\n\n")

    print("+--------------------------------------------------------------------------------+")
    print("|                         APEX ENTERTAINMENT PASS                                |")
    print("|--------------------------------------------------------------------------------|")
    print(f"| ATTENDEE : {attendee:<66}|")
    print(f"| ORG      : {org:<66}|")
    print(f"| CONTACT  : {contact:<66}|")
    print(f"| ACCESS   : {access:<66}|")
    print(f"| ISSUER   : {issuer:<66}|")
    print("+--------------------------------------------------------------------------------+")


get_info()
