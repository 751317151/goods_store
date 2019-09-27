'''
@Author: 华豪
@Date: 2019-09-16 09:30:24
@E-Mail: hh@huahaohh.cn
@LastEditors: 华豪
@LastEditTime: 2019-09-27 11:57:01
'''

import os
import pymysql
import supermarket
from flask import Flask, request, render_template, redirect, Response, session

hh = Flask(__name__)

hh.secret_key = os.urandom(16)
sno = 0

# 打开数据库连接
conn = pymysql.connect("127.0.0.1","hh","92868520","supermarket" )

# 使用 cursor() 方法创建一个游标对象 cursor
cur = conn.cursor()

@hh.route("/")
def home():
    return render_template("index.html")
    
@hh.route("/add", methods=["GET", "POST"])
def gadd():
    if request.method ==  "GET":
        return Response(render_template("index.html"))
    elif request.method == "POST":
        gsno = request.form.get("sno")
        gname = request.form.get("name")
        gprice = request.form.get("price")
        gcount = request.form.get("count")

        cur.execute("insert into goods values (%s,'%s','%s',%s)"%(gsno,gname,gprice,gcount))
        conn.commit()

        rsp = Response(render_template("index.html",po=1,sel=1))
        return rsp

@hh.route("/update", methods=["GET", "POST"])
def gupdate():
    global sno
    if request.method ==  "GET":
        return Response(render_template("index.html"))
    elif request.method == "POST":
        sno = request.form.get("upd_sno")

        cur.execute("select * from goods where sno = %s"%sno)
        # 通过游标获取执行结果
        rows = cur.fetchall()

        if rows:
            rsp = Response(render_template("index.html",uprows=rows,sel=2))
        else:
            rsp = Response(render_template("index.html",uprows=0,sel=2))

        return rsp

@hh.route("/update2", methods=["GET", "POST"])
def gupdate2():
    global sno
    if request.method ==  "GET":
        return Response(render_template("index.html"))
    elif request.method == "POST":
        name = request.form.get("upd_name")

        cur.execute("select * from goods where name = '%s'"%name)
        # 通过游标获取执行结果
        rows = cur.fetchall()

        if rows:
            sno = rows[0][0]
            rsp = Response(render_template("index.html",uprows=rows,sel=2))
        else:
            rsp = Response(render_template("index.html",uprows=0,sel=2))

        return rsp

@hh.route("/update3", methods=["GET", "POST"])
def gupdate3():
    global sno
    if request.method ==  "GET":
        return Response(render_template("index.html"))
    elif request.method == "POST":
        # sno = request.form.get("sno")
        gsno = request.form.get("upsno")
        gname = request.form.get("upname")
        gprice = request.form.get("upprice")
        gcount = request.form.get("upcount")

        cur.execute("update goods set sno=%s,name='%s',price='%s',count=%s where sno=%s"%(gsno,gname,gprice,gcount,sno))
        conn.commit()

        rsp = Response(render_template("index.html",op=1,sel=2))
        return rsp

@hh.route("/find", methods=["GET", "POST"])
def gfind():
    if request.method ==  "GET":
        return Response(render_template("index.html"))
    elif request.method == "POST":
        sno = request.form.get("find_sno")

        cur.execute("select * from goods where sno = %s"%sno)

        rows = cur.fetchall()

        if rows:
            rsp = Response(render_template("index.html",rows=rows,sel=3))
        else:
            rsp = Response(render_template("index.html",rows=0,sel=3))

        return rsp

@hh.route("/find2", methods=["GET", "POST"])
def gfind2():
    if request.method ==  "GET":
        return Response(render_template("index.html"))
    elif request.method == "POST":
        name = request.form.get("find_name")

        cur.execute("select * from goods where name = '%s'"%name)
    
        rows = cur.fetchall()

        if rows:
            rsp = Response(render_template("index.html",rows=rows,sel=3))
        else:
            rsp = Response(render_template("index.html",rows=0,sel=3))

        return rsp

@hh.route("/find3", methods=["GET", "POST"])
def gfind3():
    if request.method ==  "GET":
        return Response(render_template("index.html"))
    elif request.method == "POST":

        cur.execute("select * from goods")
    
        rows = cur.fetchall()

        if rows:
            rsp = Response(render_template("index.html",rows=rows,sel=3))
        else:
            rsp = Response(render_template("index.html",rows=0,sel=3))

        return rsp

@hh.route("/del1", methods=["GET", "POST"])
def del1():
    global sno
    if request.method ==  "GET":
        return Response(render_template("index.html"))
    elif request.method == "POST":
        sno = request.form.get("del_sno")

        cur.execute("select * from goods where sno = %s"%sno)
        # 通过游标获取执行结果
        rows = cur.fetchall()

        if rows:
            rsp = Response(render_template("index.html",derows=rows,sel=4))
        else:
            rsp = Response(render_template("index.html",derows=0,sel=4))

        return rsp

@hh.route("/del2", methods=["GET", "POST"])
def del2():
    global sno
    if request.method ==  "GET":
        return Response(render_template("index.html"))
    elif request.method == "POST":
        name = request.form.get("del_name")
        print(2,name)
        cur.execute("select * from goods where name = '%s'"%name)
        # 通过游标获取执行结果
        rows = cur.fetchall()

        if rows:
            sno = rows[0][0]
            rsp = Response(render_template("index.html",derows=rows,sel=4))
        else:
            rsp = Response(render_template("index.html",derows=0,sel=4))

        return rsp

@hh.route("/del3", methods=["GET", "POST"])
def del3():
    global sno
    if request.method ==  "GET":
        return Response(render_template("index.html"))
    elif request.method == "POST":
        cur.execute("delete from goods where sno=%s"%sno)
        conn.commit()

        rsp = Response(render_template("index.html",dp=1,sel=4))
        return rsp


if __name__ == '__main__':
    hh.run()
