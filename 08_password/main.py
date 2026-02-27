import bcrypt

password = "test"
hashed = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt()) # rounds

print(hashed)


print(hashed.decode('utf-8')) # save db

print(bcrypt.checkpw(password.encode('utf-8'), hashed ))