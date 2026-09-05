email = input("Write ur amail: ").strip()

if not email.endswith("@gmail.com"):
    print("Invalid email address")
else:
    name, domain = email.split("@")

    if len(name) <= 2:
        print("Write more symbols")
    elif len(name) <= 5:
        hidden_name = name[0] + "*" * (len(name) - 2) + name[-1]
        print(hidden_name + "@" + domain)
    else:
        hidden_name = name[:2] + "*" * (len(name) - 4) + name[-2:]
        print(hidden_name + "@" + domain)
