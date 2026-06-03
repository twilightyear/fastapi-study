from pwdlib import PasswordHash

password_hasher = PasswordHash.recommended() #Create Hashing Object

def hash_password(plain_password: str) -> str: #Turn raw password in to hashed password
    return password_hasher.hash(plain_password)

def verify_password(plain_password: str, hashed_password: str) -> bool: #Verify hashed password if it is right or wrong
    return password_hasher.verify(plain_password, hashed_password)
