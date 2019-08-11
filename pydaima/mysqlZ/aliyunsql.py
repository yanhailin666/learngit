import pymysql
def my_db(sq1):
    conn = pymysql.Connect(
        host='47.XXX',##mysql服务器地址
        port=3306,##mysql服务器端口号
        user='XXX',##用户名
        passwd='XXXX',##密码  J5p";~OVazNl%y)?
        db='yhj666',##数据库名
        charset='utf8',##连接编码
    )

    # cursor = con.cursor()  # 获取游标
    # sql = 'select * from my_user where username="%s";' % username
    cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cur.execute(sq1)
    uer = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return uer



    #data1 = cursor.fetchall()
    # print(data1[0][1])
    # uer=data1[0][1]

# sq1='select * from my_user where username="a12121"'
# print(my_db(sq1))


def my_db1(insert_sql):
    con = pymysql.Connect(
        host='',##mysql服务器地址
        port=3306,##mysql服务器端口号
        user='',##用户名
        passwd='',##密码  J5p";~OVazNl%y)?
        db='yhj666',##数据库名
        charset='utf8',##连接编码
    )

    cursor = con.cursor()  # 获取游标
    # sql = 'select * from my_user where username="%s";' % username

    cursor.execute(insert_sql)
    data1 = cursor.fetchall()