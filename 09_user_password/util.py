import bcrypt

def hash_password(plain_password:str)->str: 
    ''' 
        Erzeugt bcrypt hash 
        return hashed password für  DB
        -> prüfe Parameter und werfe Exception (raise ValueError)
    '''
    if plain_password is None:
        raise ValueError("Password darf nicht None sein")
    if not isinstance(plain_password, str) or plain_password == "":
        raise ValueError("Password muss ein nicht-leerer String sein")

    salt = bcrypt.gensalt() 
    hashed = bcrypt.hashpw(plain_password.encode("utf-8"), salt)
    return hashed.decode("utf-8")
    

def verify_password(plain_password:str, stored_hash:str)->bool:
    '''
    Prüft Plaintext gegen gespeicherten bcrypt-Hash 
     Return  True, wenn Valid
     -> prüfe Parameter und werfe Exception (raise ValueError)
    '''
    if not plain_password or not stored_hash:
        return False

    try:
        return bcrypt.checkpw(plain_password.encode("utf-8"),stored_hash.encode("utf-8"))
    except Exception:
        # z.B. wenn stored_hash kein gültiger bcrypt-String ist
        return False
    