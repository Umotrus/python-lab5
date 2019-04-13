import pymysql


def db_insert_task(text):

    # prepare the query text
    sql = """INSERT INTO task(todo) VALUES (%s)"""

    # connect to the db
    conn = pymysql.connect(user="root", password="root", host="localhost", database="todolist")
    cursor = conn.cursor()
    result = -1
    try:
        # execute the query passing the needed parameters
        cursor.execute(sql, (text, ) )
        # commit all pending queries
        conn.commit()
        result = 1
    except Exception as e:
        print(str(e))
        # if something goes wrong: rollback
        conn.rollback()

    # close the connection
    conn.close()

    return result


def get_sorted_tasks_list():

    sql = "SELECT * FROM task order by todo ASC"  # here we order data using "order by"
    conn = pymysql.connect(user="root", password="root", host="localhost", database="todolist")

    cursor = conn.cursor()
    cursor.execute(sql)

    results = cursor.fetchall()

    conn.close()

    return results


def db_contains(task):

    # prepare the query text
    sql = "select todo from task where todo = %s"

    # connect to the db
    conn = pymysql.connect(user="root", password="root", host="localhost", database="todolist")
    cursor = conn.cursor()
    cursor.execute(sql, (task,))

    results = cursor.fetchall()
    conn.close()

    if len(results) == 0:
        return False
    else:
        return True


def db_remove_task(task_id):

    # prepare the query text
    sql = "delete from task where id_task = %s"

    # connect to the db
    conn = pymysql.connect(user="root", password="root", host="localhost", database="todolist")
    cursor = conn.cursor()
    result = -1
    try:
        # execute the query passing the needed parameters
        cursor.execute(sql, (task_id,))
        # commit all pending executed queries in the connection
        conn.commit()
        result = 1
    except Exception as e:
        print(str(e))
        # if something goes wrong: rollback
        conn.rollback()

    # close the connection
    conn.close()

    return result


def db_remove_multiple_tasks(text):

    # prepare the query text
    sql = "delete from task where todo LIKE %s"

    # add percent sign (%) wildcard to select all the strings that contain specified text
    # <<the multiple character percent sign (%) wildcard can be used to represent
    # any number of characters in a value match>>
    text = "%" + text + "%"

    # connect to the db
    conn = pymysql.connect(user="root", password="root", host="localhost", database="todolist")
    cursor = conn.cursor()

    result = -1
    try:
        # execute the query passing the needed parameters
        cursor.execute(sql, (text, ))
        # commit all pending executed queries in the connection
        conn.commit()
        result = 1
    except Exception as e:
        print(str(e))
        # if something goes wrong: rollback
        conn.rollback()

    # close the connection
    conn.close()

    return result
