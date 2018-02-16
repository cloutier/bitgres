import sys
if sys.version_info.major < 3:
    sys.stderr.write('Sorry, Python 3.x required by this example.\n')
    sys.exit(1)

import hashlib
import bitcoin.rpc
import sys

from bitcoin import params
from bitcoin.core import *
from bitcoin.core.script import *

import psycopg2

bitcoin.SelectParams("testnet")
proxy = bitcoin.rpc.Proxy()

try:
    connect_str = "dbname='bitgres' user='vincent' host='localhost' " + \
                  "password=''"
    # use our connection values to establish a connection
    conn = psycopg2.connect(connect_str)
    conn.autocommit = True
    # create a psycopg2 cursor that can execute queries
    cursor = conn.cursor()
    # create a new table with a single column called "name"
except Exception as e:
    print("Uh oh, can't connect. Invalid dbname, user or password?")
    print(e)

while True:
    cursor.execute("""SELECT * from blocks;""")
    rows = cursor.fetchall()
    print(rows)
    blockcount = proxy.getblockcount()    
    print(blockcount)
    blockhash = proxy.getblockhash(1)
    block= proxy.getblock(blockhash)
    print(block.hashMerkleRoot);
    cursor.execute("""INSERT INTO blocks (hash, merkleroot, version, timestamp, bits, nounce) 
        VALUES (%s, %s, %s, %s, %s, %s);""", (blockhash, block.hashMerkleRoot, block.nVersion, block.nTime, block.nBits, block.nNonce))
