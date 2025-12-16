contacts = {
    "Ammar": "01098712355",
    "Hamza": "01086765421",
    "Youssef": "01298548736"
}

print("Contacts:")
for name in contacts:
    print(name)

search_name = input("Enter a name to search: ")

if search_name in contacts:
    print("Phone number of", search_name, ":", contacts[search_name])
else:
    print("Contact not found.")
