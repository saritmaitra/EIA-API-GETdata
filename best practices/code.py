"""It is wrong to use assert statements to control our application logic or program execution. 
It can lead to retrieval of wrong results, introduce security risks, or even worse, program failure."""

#example
def get_clients(user):
    """List of clients"""
    assert is_superuser(user), "User is not a member of superuser group"
    return db.Lookup("Clients")
    
"""Running above Python program in optimized mode, the assertstatement is ignored. 
Any user, including those who are not members of the superuser group, can successfully get the list of clients.
This means whatever protection was wired into the code is removed, leaving the application vulnerable to attacks."""

#Best practice
def get_clients(user):
    """List of clients"""
    if not is_superuser(user):
        raise PermissionError ("User is not a member of superuser group")
    return db.Lookup("Clients")
    
 """The assert mechanism should only be used for communication with other developers. For instance, when performing unit or integration tests"""
 
#Insecure Deserialization
import python
from CallNode call

where call = Value::named("yaml.load")getACall()
select call.getNode(), "yaml.load function is unsafe when loading data from untrusted sources; use yaml.safe_load instead"


from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.backends import default_backend

private_key = dsa.generate_private_key(
    key_size=512,
    backend=default_backend()
)
