'''
@Author: 华豪
@Date: 2019-09-06 17:55:49
@E-Mail: hh@huahaohh.cn
@LastEditors: 华豪
@LastEditTime: 2019-09-17 14:00:07
'''
import pymysql
import sys


conn = pymysql.connect("127.0.0.1", 'hh', '92868520', 'supermarket')

# 获取一个游标对象(Cursor类)，用于执行SQL语句
cur = conn.cursor()

def add_goods():
    print("请输入商品信息")
    gsno = int(input("商品编号："))
    cur.execute("select * from goods where sno = %s"%gsno)
    # 通过游标获取执行结果
    rows = cur.fetchall()
    if rows:
        print("编号已存在！")
    else:
        gname = input("商品名称：")
        gprice = input("商品价格：")
        gcount = int(input("商品数量："))
        try:
            # 执行任意支持的SQL语句
            cur.execute("insert into goods values (%s,'%s','%s',%s)"%(gsno,gname,gprice,gcount))
            # print(cur.rowcount)
            # 提交事务
            conn.commit()
            print("添加商品信息成功！")
        except Exception as e:
            print("添加商品信息失败！",e)
        
def update_goods():
    while True:
        print("\n*******操作指令********")
        print("1. 按商品编号修改")
        print("2. 按商品名称修改")
        print("0. 退出修改")
        print("***********************")

        op = input("\n>：")   

        if op == '0':
            break
        elif op == '1':
            sno = find_sno()
            if sno:
                update_one_good(sno)
        elif op == '2':
            sno = find_name()
            if sno:
                update_one_good(sno)
        else:
            print("输入错误，请重新输入！")

def del_goods():
    while True:
        print("\n*******操作指令********")
        print("1. 按编号删除")
        print("2. 按名字删除")
        print("0. 退出删除")
        print("***********************")

        op = input("\n>：")

        if op == '0':
            break
        elif op == '1':
            sno = find_sno()
            if sno:
                del_all_goods(sno)
        elif op == '2':
            sno = find_name()
            if sno:
                del_all_goods(sno)
        else:
            print("输入错误，请重新输入！")

def find_goods():
    while True:
        print("\n*******操作指令********")
        print("1. 按编号查找")
        print("2. 按名字查找")
        print("3. 查看数量小于10的商品")
        print("0. 退出查找")
        print("***********************")

        op = input("\n>：")

        if op == '0':
            break
        elif op == '1':
            find_sno()
        elif op == '2':
            find_name()
        elif op == '3':
            find_count()
        else:
            print("输入错误，请重新输入！")

def find_sno():
    sno = int(input("请输入商品编号："))
    cur.execute("select * from goods where sno = %s"%sno)
    # 通过游标获取执行结果
    rows = cur.fetchall()
    if rows:
        tplt = "{:<10}\t{:<10}\t{:<10}\t{:<10}"
        print(tplt.format("编号","名称","价格","数量"))
        print(tplt.format(rows[0][0],rows[0][1],rows[0][2],rows[0][3]))
        return sno
    else:
        print("没有该商品信息！")

def find_name():
    gname = input("请输入商品名称：")
    cur.execute("select * from goods where name = '%s'"%gname)
    # 通过游标获取执行结果
    rows = cur.fetchall()
    # rows = rows[0][0]
    if rows:
        tplt = "{:<10}\t{:<10}\t{:<10}\t{:<10}"
        print(tplt.format("编号","名称","价格","数量"))
        print(tplt.format(rows[0][0],rows[0][1],rows[0][2],rows[0][3]))
        return rows[0][0]
    else:
        print("没有该商品信息！")

def find_count():
    cur.execute("select * from goods where count < 10")
    rows = cur.fetchall()
    tplt = "{:<10}\t{:<10}\t{:<10}\t{:<10}"
    print(tplt.format("编号","名称","价格","数量"))
    for row in rows:
        print(tplt.format(row[0],row[1],row[2],row[3]))
    # print(rows)

def update_one_good(sno):
    print("请输入修改后的商品信息")
    gsno = int(input("商品编号："))
    gname = input("商品名称：")
    gprice = input("商品价格：")
    gcount = int(input("商品数量："))
    try:
        op = input("是否修改(y/n)? ")
        if op == 'y' or op == 'Y': 
        # 执行任意支持的SQL语句
            cur.execute("update goods set sno=%s,name='%s',price='%s',count=%s where sno=%s"%(gsno,gname,gprice,gcount,sno))
            # print(cur.rowcount)
            # 提交事务
            conn.commit()
            print("修改商品信息成功！")
    except Exception as e:
        print("修改商品信息失败！",e)

def del_all_goods(sno):
    op = input("是否删除(y/n)? ")
    if op == 'y' or op == 'Y': 
        cur.execute("delete from goods where sno=%s"%sno)
        # 提交事务
        conn.commit()
        print("删除成功！")
    else:
        print("删除失败！") 

def main():
    while True:
        print("\n*******操作指令********")
        print("1. 添加商品信息")
        print("2. 修改商品信息")
        print("3. 查看商品信息")
        print("4. 删除商品信息")
        print("0. 退出系统")
        print("***********************")

        op = input("\n>：")

        if op == '0':
            print("感谢您的使用，下次再见！")
            # 关闭游标
            cur.close()
            # 关闭数据库连接
            conn.close()
            sys.exit(2)
        elif op == '1':
            add_goods()
        elif op == '2':
            update_goods()
        elif op == '3':
            find_goods()
        elif op == '4':
            del_goods()
        else:
            print("输入错误，请重新输入！")

if __name__ == "__main__":
    main()