import psycopg2

try:
    connect_str = "dbname='bitgres' user='vincent' host='localhost' " + \
                  "password=''"
    # use our connection values to establish a connection
    conn = psycopg2.connect(connect_str)
    conn.autocommit = True
    # create a psycopg2 cursor that can execute queries
    cursor = conn.cursor()
    # create a new table with a single column called "name"
    cursor.execute("""CREATE TABLE blocks (
                        hash char(32) primary key,
                        merkleroot char(32),
                        version integer,
                        timestamp integer,
                        bits integer,
                        nounce integer,
                        prev_block char(32),
                        content char(40),
                        witness char(40));
""")
    cursor.execute("""CREATE TABLE transactions (
                        content char(40),
                        witness char(40),
                        merkleroot char(40),
                        version integer,
                        hash char(40));
""")
    # run a SELECT statement - no data in there, but we can try it
    cursor.execute("""SELECT * from blocks""")
    rows = cursor.fetchall()
    print(rows)
except Exception as e:
    print("Uh oh, can't connect. Invalid dbname, user or password?")
    print(e)
