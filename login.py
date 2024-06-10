import hashlib
#PBKDF2 is a modern hashing algorithm that is being used nowadays since it has a considerable computational cost which reduces the vulnerabilities of brute force attacks.
from hashlib import pbkdf2_hmac as pbkdf2
import mysql.connector as msql
import os
from connection_detail import sql_details
"""
https://www.youtube.com/watch?v=--tnZMuoK3E
Because the Python hashlib library cannot
hash unicode encoded strings, such as those in utf-8,
we need to first convert the string to bytes.
We can do this using the .encode() and .hexdigest() methods.

#http://www.codinghorror.com/blog/archives/000953.html
"""


"""
With regular cryptographic hash functions (e.g. MD5, SHA256),
an attacker can guess billions of passwords per second.
With PBKDF2, bcrypt, or scrypt, the attacker can only make a
few thousand guesses per second (or less, depending on
the configuration).
"""
def create_hash(password, salt):
    #https://levelup.gitconnected.com/python-salting-your-password-hashes-3eb8ccb707f9
    #Python String encode() converts a string value into a collection of bytes, using an encoding scheme specified by the user.
    # the 10000 is called iteration, what it does is hashing the password 100000 times.
    #  Example "password" => "234567890"
    #           "234567890" => "HUVHV77V"
    #           "HUVHV77dV" => "JBHDBHDB"
    #           ... 10000 times
    plaintext = password.encode()
    digest = pbkdf2('sha256', plaintext, salt, 100000)
    hex_hash = digest.hex()
    return hex_hash

def create_connection():
    conn = msql.connect(**sql_details)
    return conn

def store_user(username, password):
    salt=os.urandom(32)
    hashed_password = create_hash(password,salt)

    conn = create_connection()
    if conn.is_connected():
        cursor = conn.cursor()
        query = f'''INSERT INTO user(username, password, salt)
                    VALUES (%s, %s, %s);'''

        val = (username, hashed_password, salt.decode('latin1'))
        cursor.execute(query,val)
        conn.commit()
        conn.close()

def check_password(username, userPassword):
    conn = create_connection()
    sql = f'select * from user where username = "{username}"'
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()[0]

    hash_password_InDB = result[2]
    salt = result[3].encode('latin1')

    hex_hash = create_hash(userPassword,salt)
    return hex_hash == hash_password_InDB