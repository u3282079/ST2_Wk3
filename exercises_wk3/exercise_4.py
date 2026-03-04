def get_owners():
    owner_dictionary = {}
    with open("owners.txt", "r") as thefile:
        for line in thefile:
            owner, comp_type, comp_value = line.rstrip().split()
            comp_value = int(comp_value)

            if owner not in owner_dictionary:
                owner_dictionary[owner] = {}

            owner_dictionary[owner][comp_type] = comp_value

    return owner_dictionary

print(get_owners())
#
# def get_info(customers):
#     print("Nested Structure:", type(customers),
#           type(customers[0]), type(customers[0][0]))
#     # partial contents of customers
#     print(customers[0], customers[1], sep="\n", end="\n\n")
#
# def get_dictionary(customers):
#     # Convert to dictionary using a dictionary comprehension
#     return {"{}{}".format(cust[0], cust[1]): cust for cust in customers}
#
# def print_customernames(customer_names):
#     print("Customer names:")
#     for i, name in enumerate(customer_names):
#         print("{0:20}".format(name), end="|")
#         if i % 4==3:
#             print()
#     print("\n")
#
# def user_interaction(customers):
#     tags = ["FirstName", "LastName", "Street", "City", "State", "ZipCode"]
#     fmt = "{:16}{:16}{:20}{:16}{:6}{:5}"
#     while True:
#         name=input("Enter a name (or 'quit' to quit):")
#         if name =="quit":
#             break
#         data = customers.get(name)
#         if data:
#             print(fmt.format(*tags))
#             print(fmt.format(*data))

# next step is to create the application that "calls all the preceding functions", it's called "customers.py"