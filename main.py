# Thayer Yang  
# 18 NOV 2024
# Default Values for Parameters Practice

# 8-3 (T-Shirt)

# def make_shirt(size, message):
#     print(f'Shirt Order: a {size} shirt with the message: "{message}"')

# make_shirt("large", "I LOVE VIDEO GAMES")
# make_shirt(message="I love numbers!", size="XXL")


# 8-4 (Large Shirts)

def make_shirt(size = "large", message= "I love Python"):
    print(f'Shirt Order: a {size} shirt with the message: "{message}" ')

make_shirt()
make_shirt(size="medium")
make_shirt(size="small",message="MINCERAFT")

# 8-5 (Cities)

def describe_city(country = "Canada", city= "Ottawa"):
    print(f'{city.title()} is in {country.title()}')

describe_city(city="Toronto")
describe_city(city="Detroit")
describe_city(city="Paris")
