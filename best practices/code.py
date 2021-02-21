#It is wrong to use assert statements to control our application logic or program execution. 
#It can lead to retrieval of wrong results, introduce security risks, or even worse, program failure.

#example 1
def get_clients(user):
    #List of clients
    assert is_superuser(user), "User is not a member of superuser group"
    return db.Lookup("Clients")
    
#Running above Python program in optimized mode, the assertstatement is ignored. 
#Any user, including those who are not members of the superuser group, can successfully get the list of clients.
#This means whatever protection was wired into the code is removed, leaving the application vulnerable to attacks.

#Best practice
def get_clients(user):
    #List of clients
    if not is_superuser(user):
        raise PermissionError ("User is not a member of superuser group")
    return db.Lookup("Clients")
    
# The assert mechanism should only be used for communication with other developers. For instance, when performing unit or integration tests

#EXAMPLE 2
def is_high_end_device(device):
    if device.price > 1000 and device.manufacturer=='apple':
        return True
    else:
        return False
    
#Best practice
def is_high_end_device(device):
    return device.price > 1000 and device.manufacturer=='apple'


#EXAMPLE 3
def extract_phone_information(invoice, insurance):
    phone = invoice.item

    p = phone.price
    m = phone.manufacturer
    high_end_flag = False
    if price > 1000 and manufacturer=='apple:
        high_end_flag = True

    insr_active = False
    if insurance.active==1:
        insr_active = True

    phone_info = {
        'manufacturer': m,
        'price': p,
        'is_high_end': high_end_falg,
        'has_active_insurance': insr_active
    }
    return phone_info

# Best practice
# Creating variables such as p,m,high_end_flag etc are totally unnecessary.
def extract_phone_information(invoice, insurance):
    phone = invoice.item
    return {
        'manufacturer': phone.manufacturer,
        'price': phone.price,
        'is_high_end': phone.price>1000 and phone.manufacture=='apple',
        'has_active_insurance': insurance.active==1
    }

#EXAMPLE 4
def is_hed(device):
    return device.price > 1000 and device.manufacturer=='apple'

#Best practice
# avoid using abbreviation
def is_high_end_device(device):
    return device.price > 1000 and device.manufacturer=='apple'

#EXAMPLE 5
# Descriptive function and variable names over code comments
def fraud(trans, cust):
    '''
    This function tells you if transaction is fraud. Input
    parameter trans represents the transaction. cust is for customer.
    '''
    flag = False

    # if device is high end AND customer has not provided any ssn AND
    # customer's state of residence is not equal to store's state then
    # mark that as potential fraud and run further checks
    if is_hed(trans.device) and cust.ssn == None and cust.st != trans.store.st:
        flag=True

    if flag:
        # run further checks
        # return True or False based on these checks
        
#Best practice
def is_fraudulent_transaction(transaction, customer):

    potential_fraud = False
    if is_high_end_device(transaction.device) \
        and customer.ssn is None \
        and customer.state != transaction.store.state:
        potential_fraud = True

    if potential_fraud:
        # run further checks
        # return True or False based on these checks
        
#EXAMPLE 6
#Difficult to understand
def process_numbers(input):
    '''
    Create a list that has square of all even numbers in input list
    Now in this list, if number is less then 20 return a list where
    every element is a dictionary containing square and cube of a number
    '''
    return [{'square': n*n, 'cube': n*n*n} for n in [i*i for i in input if i%2==0] if n<20]

#Best practice
def process_numbers(input):
    even_squares = [i*i for i in input if i%2==0]
    processed_list = []
    for n in even_squares:
        if n<20:
            processed_list.append({
                'square': n*n,
                'cube': n*n*n
            })
    return processed_list

#EXAMPLE 7
# Nest code
for i in range(100):
    if condition_1:
        if condition_2:
            if condition_3 and condition_4:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    
#Best pracice
for i in range(100):
    if not condition_1 or not condition_2:
        return False
    return condition_3 and condition_4

# EXAMPLE 8
# team work on coding style/naming config
for i in range(100):
    if not condition_1 or not condition_2:
        return False
    return condition_3 and condition_4

#Best practice 1
def is_fraudulent_transaction(transaction, customer):
    potential_fraud = False
    is_fraud = False

    if is_high_end_device(transaction.device) \
        and customer.ssn is None \
        and customer.state != transaction.store.state:
        potential_fraud = True

    if potential_fraud:
        if further_checks(transaction, customer):
            is_fraud = True
    return is_fraud

#Best practice 2
def isFraudulentTransaction(transaction, customer):
    potentialFraud = False
    isFraud = False

    if isHighEndDevice(transaction.device) \
        and customer.ssn is None \
        and customer.state != transaction.store.state:
        potentialFraud = True

    if potentialFraud:
        if furtherChecks(transaction, customer):
            isFraud = True
    return isFraud

#EXAMPLE 9
def foo():
    if device.price>1000 \
       and device.manufacturer=='apple' \
       and device.version > 5:
        # do something

def bar():
    # some logic
    # some other logic
    if device.price>1000 \
       and device.manufacturer=='apple' \
       and device.version > 5:
        # do something
        
#Best practice
def is_high_end_device(device):
    return device.price>1000 \
       and device.manufacturer=='apple' \
       and device.version > 5

def foo():
    if is_high_end_device(device):
        # do something

def bar():
    # some logic
    # some other logic
    if is_high_end_device(device):
        # do something
        
#EXAMPLE 10
# extract unique countries
customers = [
    {
        'name': 'John',
        'country': 'USA'
    },
    {
        'name': 'Mohan',
        'country': 'India'
    },
    {
        'name': 'Nancy',
        'country': 'USA'
    },    
    {
        'name': 'Abdul',
        'country': 'India'
    }
]
countries = [] # Use a list
for customer in customers:
    countries.append(customer['country'])

unique_countries = remove_duplicates(countries)
# unique_countries now has ['USA','India']

#Best practice
# extract unique countries
customers = [
    {
        'name': 'John',
        'country': 'USA'
    },
    {
        'name': 'Mohan',
        'country': 'India'
    },
    {
        'name': 'Nancy',
        'country': 'USA'
    },    
    {
        'name': 'Abdul',
        'country': 'India'
    }
]
unique_countries = set() # Use a set 
for customer in customers:
    unique_countries.append(customer['country'])

# unique_countries now has {'India', 'USA'}




from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.backends import default_backend

# Below query would report an alert for this Python code
private_key = dsa.generate_private_key(
    key_size=512,
    backend=default_backend()
)

