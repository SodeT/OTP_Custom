#Functions:
#           key256(pass, salt), key512(pass, salt)
#           encrypt(msg, key), decrypt(msg, key)


import random, hashlib as hl, string

def key256(password, salt): # hashes salt and password

    hash = hl.new('sha256')
    hash.update(str.encode(password + salt))
    
    key = hash.hexdigest()

    return key

def key512(password, salt):

    hash = hl.new('sha512')
    hash.update(str.encode(password + salt))
    
    key = hash.hexdigest()

    return key


def salt(): # generates salt for password
    salt = ''
    for i in range(10):
        salt += random.choice(string.printable)

    return salt


def encrypt(message, key):
    max_value = 10000 # max value chr accepts
    chunk_len = len(key)
    chunks = []
    # -------------- pad message ------------- #
    while len(message) % chunk_len != 0:
        message += ' '

    # -------------- loading chunks ------------------- #
    while len(message) != 0:
        chunks.append(message[:chunk_len]) # adding the chunk to the list
        message = message[chunk_len:] # removing the chunk so it only reads once
    chunks_num = len(chunks)
    # ---------------- encoding all chunks --------- #
    
    encoded_chunks = []
    for i in range(chunks_num):
        chunk = []
        for x in range(chunk_len):
            chunk.append(ord(chunks[i][x]))
        encoded_chunks.append(chunk)

    # ----------- encoding the key ---------------- #
    encoded_key = []
    for i in range(chunk_len):
        encoded_key.append(ord(key[i])) # making the chipher look more random
    
    # ---------- generating a longer key --------- #
    key_chunks = [encoded_key] # the key for each chunk, every key is unique
    for i in range(chunks_num):
        key_chunk = []
        for x in range(chunk_len):
            new_key_value = key_chunks[-1][x] + key_chunks[-1][x] # adding the key to itself so that every chunk get encryptet with a unique key
            if new_key_value > max_value:
                new_key_value -= max_value
            key_chunk.append(new_key_value)
        key_chunks.append(key_chunk)
            
   # ----------- encrypting ------------- #
    encrypted_chunks = []
    for i in range(chunks_num):
        
        chipher_chunk = []
        chunk = encoded_chunks[i]
        chunk_key = key_chunks[i]
        for x in range(chunk_len):
            cipher_value = chunk[x] + chunk_key[x]
            if cipher_value >= max_value:
                cipher_value = cipher_value - max_value
                
            chipher_chunk.append(cipher_value)
        encrypted_chunks.append(chipher_chunk)

    # ------------ making it to chipher text ---------- #
    chipher_text = ''
    for i in range(chunks_num):

        encrypted_chunk = encrypted_chunks[i]
        
        for x in range(chunk_len):
            
            chipher_text += chr(encrypted_chunk[x])

    return chipher_text


            
def decrypt(chipher_text, key):
    max_value = 10000 # max value chr accepts
    chunk_len = len(key)
    chunks = []
    # -------------- pad message ------------- #
    while len(chipher_text) % chunk_len != 0:
        chipher_text += ' '

    # -------------- loading chunks ------------------- #
    while len(chipher_text) != 0:
        chunks.append(chipher_text[:chunk_len]) # adding the chunk to the list
        chipher_text = chipher_text[chunk_len:] # removing the chunk so it only reads once
    chunks_num = len(chunks)
    # ---------------- encoding all chunks --------- #
    
    encoded_chunks = []
    for i in range(chunks_num):
        chunk = []
        for x in range(chunk_len):
            chunk.append(ord(chunks[i][x]))
        encoded_chunks.append(chunk)

    # ----------- encoding the key ---------------- #
    encoded_key = []
    for i in range(chunk_len):
        encoded_key.append(ord(key[i])) # making the chipher look more random

    # ---------- generating a longer key --------- #
    key_chunks = [encoded_key] # the key for each chunk, every key is unique
    for i in range(chunks_num):
        key_chunk = []
        for x in range(chunk_len):
            new_key_value = key_chunks[-1][x] + key_chunks[-1][x] # adding the key to itself so that every chunk get encryptet with a unique key
            if new_key_value > max_value:
                new_key_value -= max_value
            key_chunk.append(new_key_value)
        key_chunks.append(key_chunk)
    
   # ----------- decrypting ------------- #
    decrypted_chunks = []
    for i in range(chunks_num):
        
        plain_chunk = []
        chunk = encoded_chunks[i]
        chunk_key = key_chunks[i]
        for x in range(chunk_len):
            plain_value = chunk[x] - chunk_key[x]
            if plain_value < 0:
                plain_value = plain_value + max_value
            plain_chunk.append(plain_value)
        decrypted_chunks.append(plain_chunk)

    # ------------ making it to plain text ---------- #
    plain_text = ''
    for i in range(chunks_num):

        decrypted_chunk = decrypted_chunks[i]
        
        for x in range(chunk_len):
            
            plain_text += chr(decrypted_chunk[x])

    return plain_text



