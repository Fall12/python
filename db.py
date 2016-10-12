import MySQLdb


# Get db.
def get_db():
    db = MySQLdb.connect(host="xxxx", port=33, user="*****", passwd="*****",
                         db="****")
    cursor = db.cursor()
    return cursor

#get data from db.
def get_data(id):
    sql = 'select * from table where id=%s' %id
    cursor = get_db()
    # Get the data.
    try:
        mysqlData = cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            username = row[0]
            nickname = row[1]
    except BaseException as e:
        print('Error: ' + e )
