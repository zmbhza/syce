import pymysql,time
#数据库索引
def mysql(a):
    if a == '测试':
        b = pymysql.connect(
        host="47.111.103.72",  # 数据库地址
        port=26535,  # 端口号
        db='qs_3.0_product',  # 数据库名
        user="root",  # 用户名
        passwd="WYmjdijDldsiqnporelease",  # 密码
        charset="utf8",  # 指定字符编码
    )
        return b
#sql语句索引
def sql(a):
    if a =='新增商品查询':
        b = "SELECT name FROM tb_product_cash_sale WHERE NAME like %s  LIMIT 1"
        return b


