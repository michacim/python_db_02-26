import bcrypt

def hash_password(plain_password:str)->str: 
    ''' 
        Erzeugt bcrypt hash 
        return hashed password für  DB
        -> prüfe Parameter und werfe Exception (raise ValueError)
    '''
    pass

def verify_password(plain_password:str, stored_hash:str)->bool:
    '''
    Prüft Plaintext gegen gespeicherten bcrypt-Hash 
     Return  True, wenn Valid
     -> prüfe Parameter und werfe Exception (raise ValueError)
    '''
    pass