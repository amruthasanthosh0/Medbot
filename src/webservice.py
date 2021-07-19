import base64
import os
from datetime import datetime
import google_trans_new as google_translator
from flask import *
import pymysql
from src.chatbot import *
from gtts import gTTS
con=pymysql.connect(host="localhost",port=3306,user="root",password="",db="medbot")
cmd=con.cursor()
obj=Flask(__name__)
@obj.route('/login',methods=['post'])
def login():
    username=request.form['username']
    password=request.form['pswd']
    cmd.execute("select * from login where user_name='"+username+"' and password='"+password+"' and type='user'")
    var=cmd.fetchone()
    if var is None:
        return jsonify({'task':"Invalid"})
    else:
        return jsonify({'task': str(var[0])})

@obj.route('/reg',methods=['post'])
def reg():
    username = request.form['username']
    password = request.form['pswd']
    lname=request.form['lname']
    fname = request.form['fname']
    email=request.form['email']
    phn=request.form['phn']
    weight=request.form['weight']
    height=request.form['height']
    bloodgrp=request.form['bloodgrp']
    location=request.form['location']
    age=request.form['age']
    gender=request.form['gender']
    cmd.execute("insert into login values (NULL,'"+username+"','"+password+"','user')")
    lid=con.insert_id()
    cmd.execute("insert into user_details values(NULL,'"+height+"','"+weight+"','"+age+"','"+bloodgrp+"','"+location+"','"+gender+"','"+fname+"','"+lname+"','"+str(lid)+"','"+phn+"','"+email+"')")
    con.commit()
    return jsonify({'task':'Success'})

@obj.route('/viewvaccineinfo',methods=['post'])
def viewvaccineinfo():
    cmd.execute("select * from vaccines")
    var=[x[0] for x in cmd.description]
    result=cmd.fetchall()
    json_data=[]
    for results in result :
        row=[]
        for i in results:
            row.append(str(i))
        json_data.append(dict(zip(var,row)))
    con.commit()
    return jsonify(json_data)
@obj.route('/symp',methods=['post'])
def symp():
    cmd.execute("SELECT DISTINCT `Symptom`,S_id FROM `symptoms` ")
    var = [x[0] for x in cmd.description]
    result = cmd.fetchall()
    json_data = []
    for results in result:
        row = []
        for i in results:
            row.append(str(i))
        json_data.append(dict(zip(var, row)))
    con.commit()
    return jsonify(json_data)
@obj.route('/srch_disease',methods=['post'])
def srch_disease():
    cmd.execute("SELECT * FROM `diseases`")
    var = [x[0] for x in cmd.description]
    result = cmd.fetchall()
    print(result)
    json_data = []
    for results in result:
        row = []
        for i in results:
            row.append(str(i))
        json_data.append(dict(zip(var, row)))
    con.commit()
    return jsonify(json_data)
@obj.route('/dinfo',methods=['post'])
def dinfo():
    did=request.form['dis']
    print(did)
    cmd.execute("SELECT * FROM `diseases` WHERE `Disease_id`='"+str(did)+"'")
    var = [x[0] for x in cmd.description]
    result = cmd.fetchall()
    print(result)
    json_data = []
    for results in result:
        row = []
        for i in results:
            row.append(str(i))
        json_data.append(dict(zip(var, row)))
    con.commit()
    return jsonify(json_data)
@obj.route('/homeremedies',methods=['post'])
def homerem():
    cmd.execute("SELECT * FROM `remedies`")
    var = [x[0] for x in cmd.description]
    result = cmd.fetchall()
    print(result)
    json_data = []
    for results in result:
        row = []
        for i in results:
            row.append(str(i))
        json_data.append(dict(zip(var, row)))
    con.commit()
    return jsonify(json_data)
@obj.route('/hinfo',methods=['post'])
def hinfo():
    rid=request.form['dis']
    print(rid)
    cmd.execute("SELECT * FROM `remedies` WHERE `Rem_id`='"+str(rid)+"'")
    var = [x[0] for x in cmd.description]
    result = cmd.fetchall()
    print(result)
    json_data = []
    for results in result:
        row = []
        for i in results:
            row.append(str(i))
        json_data.append(dict(zip(var, row)))
    con.commit()
    return jsonify(json_data)
@obj.route('/viewprofile',methods=['post'])
def viewprofile():
    lid=request.form['lid']
    cmd.execute("select * from user_details where loginid='"+str(lid)+"'")
    var = [x[0] for x in cmd.description]
    result = cmd.fetchall()
    json_data = []
    for results in result:
        row = []
        for i in results:
            row.append(str(i))
        json_data.append(dict(zip(var, row)))
    con.commit()
    return jsonify(json_data)
@obj.route('/diet',methods=['post'])
def diet():
    age=request.form['age']
    weight=int(request.form['wt'])
    height =float( request.form['ht'])
    bmi=weight/(height*height)
    if int(bmi) <= 15:
        age1=15
        cmd.execute("SELECT * FROM `diet` WHERE `BMI_age`='" + str(age1) + "'")
        var = [x[0] for x in cmd.description]
        result = cmd.fetchall()
        json_data = []
        for results in result:
            row = []
            for i in results:
                row.append(str(i))
            json_data.append(dict(zip(var, row)))
        con.commit()
        return jsonify(json_data)
    elif(int(age)<=22 and int(age)>15):
        age1=22
        cmd.execute("SELECT * FROM `diet` WHERE `BMI_score`='" + str(age1) + "'")
        var = [x[0] for x in cmd.description]
        result = cmd.fetchall()
        json_data = []
        for results in result:
            row = []
            for i in results:
                row.append(str(i))
            json_data.append(dict(zip(var, row)))
        con.commit()
        return jsonify(json_data)
    elif int(age)<=28 and int(age)>22:
        age1=28
        cmd.execute("SELECT * FROM `diet` WHERE `BMI_score`='" + str(age1) + "'")
        var = [x[0] for x in cmd.description]
        result = cmd.fetchall()
        json_data = []
        for results in result:
            row = []
            for i in results:
                row.append(str(i))
            json_data.append(dict(zip(var, row)))
        con.commit()
        return jsonify(json_data)
    else :
        age1=35
        cmd.execute("SELECT * FROM `diet` WHERE `BMI_score`='" + str(age1) + "'")
        var = [x[0] for x in cmd.description]
        result = cmd.fetchall()
        json_data = []
        for results in result:
            row = []
            for i in results:
                row.append(str(i))
            json_data.append(dict(zip(var, row)))
        con.commit()
        return jsonify(json_data)

@obj.route("/response",methods=['post'])
def response() :
    con = pymysql.connect(host="localhost", port=3306, user="root", password="", db="medbot")
    cmd = con.cursor()
    st_id=request.form['lid']
    cmd.execute("SELECT msg,u_id,reply FROM `chatbot` WHERE `u_id`="+str(st_id))
    s=cmd.fetchall()
    row_headers = ['frmid','toid','msg']
    json_data = []
    for result in s:
        print(result)
        row=[]
        row.append(st_id)
        row.append(0)
        b64b = result[0].encode("utf-8")
        resultd = base64.b64decode(b64b)
        resultstring = resultd.decode('utf-8')
        row.append(resultstring)
        json_data.append(dict(zip(row_headers, row)))
        row = []
        row.append(0)
        row.append(st_id)
        b64b = result[2].encode("utf-8")
        resultd = base64.b64decode(b64b)
        resultstring = resultd.decode('utf-8')
        row.append(resultstring)
        json_data.append(dict(zip(row_headers, row)))
    print(json_data)
    return jsonify(json_data)
def voice(text):
    con = pymysql.connect(host="localhost", port=3306, user="root", password="", db="medbot")
    cmd = con.cursor()
    language = 'ml'
    myobj = gTTS(text=text, lang=language, slow=False)
    fn=datetime.now().strftime("%Y%m%d%H%M%S")+".mp3"
    myobj.save("static/voice/"+fn)
    return fn

@obj.route('/insertchatbot',methods=['GET','POST'])
def insertchatbot():
    con = pymysql.connect(host="localhost", port=3306, user="root", password="", db="medbot")
    cmd = con.cursor()
    from google_trans_new import google_translator
    qus=request.form['msg']
    lid=request.form['lid']
    print("============",qus,type(qus))
    print(lid)
    flag=0
    try:
        rr=qus.encode("ascii")
        print("okkkkkkkkkk",rr)
    except:
        flag=1
        print("errorrrrr")
    qus1=qus
    if flag==1:
        translator = google_translator()
        qus1 = translator.translate(qus, lang_src='ml', lang_tgt='en').lower()
    print("qus1",qus1)
    res = cb(qus1)
    if flag==1:
        translator = google_translator()
        res = translator.translate(res, lang_src='en', lang_tgt='ml')
    print("res",res)
    fn=voice(res)
    samplestringb=qus.encode("utf-8")
    b64b=base64.b64encode(samplestringb)
    b64s=b64b.decode('utf-8')
    print(b64s)
    ress = res.encode("utf-8")
    b64bres = base64.b64encode(ress)
    b64sres = b64bres.decode('utf-8')
    print(b64sres)
    cmd.execute("INSERT INTO `chatbot` VALUES(NULL,'" + b64s + "','" + str(lid) + "','" + b64sres + "')")
    con.commit()
    print(fn,"======================================fn")
    return jsonify({'task':res,"fn":fn})

@obj.route("/chatbot",methods=['post'])
def chatbot() :
    con = pymysql.connect(host="localhost", port=3306, user="root", password="", db="medbot")
    cmd = con.cursor()
    lid=request.form['lid']
    cmd.execute("SELECT MAX(qid) FROM `answer` where uid='" + str(lid) + "'")
    p = cmd.fetchone()
    if p[0] is not None:
        cmd.execute("SELECT MAX(qid)+1 FROM `answer` where uid='" + str(lid) + "'")
        p1 = cmd.fetchone()
        print(p1, "===")
        if p1[0] is not None:
            cmd.execute(
                " SELECT `question`.`question`,`question`.`qid`,`answer`.`answer` FROM `question` LEFT JOIN `answer` ON `question`.`qid`=`answer`.`qid` where `question`.`qid` BETWEEN 1 and '" + str(
                    p1[0]) + "' ")
            s = cmd.fetchall()
            row_headers = ['frmid', 'toid', 'msg']
            json_data = []
            for result in s:
                row = []
                row.append(lid)
                row.append(0)
                row.append(result[0])
                json_data.append(dict(zip(row_headers, row)))
                row = []
                row.append(0)
                row.append(lid)
                row.append(result[2])
                json_data.append(dict(zip(row_headers, row)))
            print(json_data)
            return jsonify(json_data)
        else:
            return ''
    else:
        cmd.execute("select min(qid) from answer where answer='null' ")
        a=cmd.fetchone()
        if a[0] is None:
            cmd.execute(
                " SELECT `question`.`question`,min(`question`.`qid`),`answer`.`answer` FROM `question` LEFT JOIN `answer` ON `question`.`qid`=`answer`.`qid` ")
            s = cmd.fetchall()
            row_headers = ['frmid', 'toid', 'msg']
            json_data = []
            for result in s:
                row = []
                row.append(lid)
                row.append(0)
                row.append(result[0])
                json_data.append(dict(zip(row_headers, row)))
                row = []
                row.append(0)
                row.append(lid)
                row.append(result[2])
                json_data.append(dict(zip(row_headers, row)))
            print(json_data)
            return jsonify(json_data)
        else:
            print("**************************")
            cmd.execute(
                " SELECT `question`.`question`,`question`.`qid`,`answer`.`answer` FROM `question` LEFT JOIN `answer` ON `question`.`qid`=`answer`.`qid` ")
            s = cmd.fetchall()
            row_headers = ['frmid', 'toid', 'msg']
            json_data = []
            for result in s:
                row = []
                row.append(lid)
                row.append(0)
                row.append(result[0])
                json_data.append(dict(zip(row_headers, row)))
                row = []
                row.append(0)
                row.append(lid)
                row.append(result[2])
                json_data.append(dict(zip(row_headers, row)))
            print(json_data)
            return jsonify(json_data)
@obj.route('/disease',methods=['post'])
def disease():
    uid = request.form['lid']
    cmd.execute("SELECT SUM(`score`) FROM `answer` WHERE `qid` IN(7,10) OR qid IN(12,13) AND uid='"+str(uid)+"'")
    p=cmd.fetchone()
    cmd.execute("SELECT SUM(`score`) FROM `answer` WHERE `qid` IN(4) AND uid='" + str(uid) + "'")
    p1 = cmd.fetchone()
    cmd.execute("SELECT SUM(`score`) FROM `answer` WHERE `qid` IN(3,6) AND uid='" + str(uid) + "'")
    p2 = cmd.fetchone()
    if(int(p[0])>1):
        disease="fever"
        cmd.execute("SELECT * FROM `diseases` WHERE `Disease`='" +disease+ "'")
        var = [x[0] for x in cmd.description]
        result = cmd.fetchall()
        json_data = []
        for results in result:
            row = []
            for i in results:
                row.append(str(i))
            json_data.append(dict(zip(var, row)))
        con.commit()
        cmd.execute("delete from answer where uid='" + str(uid) + "'")
        con.commit()
        return jsonify(json_data)
    elif(int(p1[0])==1):
        disease="Ringworm"
        cmd.execute("SELECT * FROM `diseases` WHERE `Disease`='" +disease+ "'")
        var = [x[0] for x in cmd.description]
        result = cmd.fetchall()
        json_data = []
        for results in result:
            row = []
            for i in results:
                row.append(str(i))
            json_data.append(dict(zip(var, row)))
        con.commit()
        cmd.execute("delete from answer where uid='" + str(uid) + "'")
        con.commit()
        return jsonify(json_data)
    elif(int(p2[0])>=1):
        disease="flue"
        cmd.execute("SELECT * FROM `diseases` WHERE `Disease`='" +disease+ "'")
        var = [x[0] for x in cmd.description]
        result = cmd.fetchall()
        json_data = []
        for results in result:
            row = []
            for i in results:
                row.append(str(i))
            json_data.append(dict(zip(var, row)))
        con.commit()
        cmd.execute("delete from answer where uid='" + str(uid) + "'")
        con.commit()
        return jsonify(json_data)
    else:
        disease="chickenpox"
        cmd.execute("SELECT * FROM `diseases` WHERE `Disease`='" +disease+ "'")
        var = [x[0] for x in cmd.description]
        result = cmd.fetchall()
        json_data = []
        for results in result:
            row = []
            for i in results:
                row.append(str(i))
            json_data.append(dict(zip(var, row)))
        con.commit()
        cmd.execute("delete from answer where uid='" + str(uid) + "'")
        con.commit()
        return jsonify(json_data)

@obj.route('/insertchat',methods=['post'])
def insertchat():
    uid = request.form['lid']
    answer=request.form['msg']
    cmd.execute("SELECT MAX(qid)+1 FROM `answer` where uid='" + str(uid) + "'")
    p = cmd.fetchone()
    if p[0] is not None:
        if answer=="yes":
            cmd.execute("insert into `answer` VALUES(null,'"+str(p[0])+"','"+str(uid)+"','"+answer+"','1')")
            con.commit()
            return jsonify({'task': "ok"})
        else:
            cmd.execute("insert into `answer` VALUES(null,'" + str(p[0]) + "','" + str(uid) + "','" + answer + "','0')")
            con.commit()
            return jsonify({'task': "ok"})
    else:
        if answer == "yes":
            cmd.execute("insert into `answer` VALUES(null,1,'" + str(uid) + "','" + answer + "','1')")
            con.commit()
            return jsonify({'task': "ok"})
        else:
            cmd.execute("insert into `answer` VALUES(null,1,'" + str(uid) + "','" + answer + "','0')")
            con.commit()
            return jsonify({'task': "ok"})

@obj.route("/respcouncil",methods=['post'])
def respcouncil() :
    con = pymysql.connect(host="localhost", port=3306, user="root", password="", db="medbot")
    cmd = con.cursor()
    lid=request.form['lid']
    cmd.execute("SELECT MAX(qid) FROM `councilres` where uid='" + str(lid) + "'")
    p = cmd.fetchone()
    if p[0] is not None:
        cmd.execute("SELECT MAX(qid)+1 FROM `councilres` where uid='" + str(lid) + "'")
        p1 = cmd.fetchone()
        print(p1, "===")
        if p1[0] is not None:
            cmd.execute(
                " SELECT `query`.`query`,`query`.`query_id`,`councilres`.`res` FROM `query` LEFT JOIN `councilres` ON `query`.`query_id`=`councilres`.`qid` where `query`.`query_id` BETWEEN 1 and '" + str(
                    p1[0]) + "' ")
            s = cmd.fetchall()
            row_headers = ['frmid', 'toid', 'msg']
            json_data = []
            for result in s:
                row = []
                row.append(lid)
                row.append(0)
                row.append(result[0])
                json_data.append(dict(zip(row_headers, row)))
                row = []
                row.append(0)
                row.append(lid)
                row.append(result[2])
                json_data.append(dict(zip(row_headers, row)))
            print(json_data)
            return jsonify(json_data)
        else:
            return ''
    else:
        cmd.execute("select min(qid) from councilres where res='null' ")
        a=cmd.fetchone()
        if a[0] is None:
            cmd.execute(
                " SELECT `query`.`query`,min(`query`.`query_id`),`councilres`.`res` FROM `query` LEFT JOIN `councilres` ON `query`.`query_id`=`councilres`.`qid` ")
            s = cmd.fetchall()
            row_headers = ['frmid', 'toid', 'msg']
            json_data = []
            for result in s:
                row = []
                row.append(lid)
                row.append(0)
                row.append(result[0])
                # row.append(result[3])
                json_data.append(dict(zip(row_headers, row)))
                row = []
                row.append(0)
                row.append(lid)
                row.append(result[2])
                # row.append(result[3])
                json_data.append(dict(zip(row_headers, row)))
            print(json_data)
            return jsonify(json_data)
        else:
            print("**************************")
            cmd.execute(
                " SELECT `query`.`query`,`query`.`query_id`,`councilres`.`res` FROM `query` LEFT JOIN `councilres` ON `query`.`query_id`=`councilres`.`qid` ")
            s = cmd.fetchall()
            row_headers = ['frmid', 'toid', 'msg']
            json_data = []
            for result in s:
                row = []
                row.append(lid)
                row.append(0)
                row.append(result[0])
                # row.append(result[3])
                json_data.append(dict(zip(row_headers, row)))
                row = []
                row.append(0)
                row.append(lid)
                row.append(result[2])
                # row.append(result[3])
                json_data.append(dict(zip(row_headers, row)))
            print(json_data)
            return jsonify(json_data)

@obj.route('/insertcouncil',methods=['post'])
def insertcouncil():
    uid = request.form['lid']
    answer=request.form['msg']
    cmd.execute("SELECT MAX(qid)+1 FROM `councilres` where uid='" + str(uid) + "'")
    p = cmd.fetchone()
    if p[0] is not None:
        cmd.execute("insert into `councilres` VALUES(null,'"+str(p[0])+"','"+answer+"','"+str(uid)+"','0')")
        con.commit()
        qid=str(p[0])
        sent(uid,answer,qid)
        return jsonify({'task': "ok"})
    else:
        cmd.execute("insert into `councilres` VALUES(null,1,'"+answer+"','" + str(uid) + "','0')")
        con.commit()
        qid=1
        sent(uid,answer,qid)
        return jsonify({'task': "ok"})
@obj.route('/council',methods=['post'])
def council():
    uid = request.form['lid']
    cmd.execute("SELECT SUM(`score`) FROM `councilres` WHERE uid='"+str(uid)+"'")
    s=cmd.fetchone()
    if int(s[0]<=1):
        cmd.execute("SELECT * FROM `council` WHERE `Score`=1")
        var = [x[0] for x in cmd.description]
        result = cmd.fetchall()
        json_data = []
        for results in result:
            row = []
            for i in results:
                row.append(str(i))
            json_data.append(dict(zip(var, row)))
        con.commit()
        cmd.execute("delete from councilres where uid='" + str(uid) + "'")
        con.commit()
        return jsonify(json_data)
    elif int(s[0])<=20 and int(s[0])>2 :
        cmd.execute("SELECT * FROM `council` WHERE `Score`=20")
        var = [x[0] for x in cmd.description]
        result = cmd.fetchall()
        json_data = []
        for results in result:
            row = []
            for i in results:
                row.append(str(i))
            json_data.append(dict(zip(var, row)))
        con.commit()
        cmd.execute("delete from councilres where uid='" + str(uid) + "'")
        con.commit()
        return jsonify(json_data)
    elif int(s[0]) <= 30 and int(s[0]) > 20:
        cmd.execute("SELECT * FROM `council` WHERE `Score`=30")
        var = [x[0] for x in cmd.description]
        result = cmd.fetchall()
        json_data = []
        for results in result:
            row = []
            for i in results:
                row.append(str(i))
            json_data.append(dict(zip(var, row)))
        con.commit()
        cmd.execute("delete from councilres where uid='" + str(uid) + "'")
        con.commit()
        return jsonify(json_data)
    elif int(s[0]) <= 40 and int(s[0]) > 30:
        cmd.execute("SELECT * FROM `council` WHERE `Score`=40")
        var = [x[0] for x in cmd.description]
        result = cmd.fetchall()
        json_data = []
        for results in result:
            row = []
            for i in results:
                row.append(str(i))
            json_data.append(dict(zip(var, row)))
        con.commit()
        cmd.execute("delete from councilres where uid='" + str(uid) + "'")
        con.commit()
        return jsonify(json_data)
    else:
        cmd.execute("SELECT * FROM `council` WHERE `Score`=50")
        var = [x[0] for x in cmd.description]
        result = cmd.fetchall()
        json_data = []
        for results in result:
            row = []
            for i in results:
                row.append(str(i))
            json_data.append(dict(zip(var, row)))
        con.commit()
        cmd.execute("delete from councilres where uid='" + str(uid) + "'")
        con.commit()
        return jsonify(json_data)

def sent(uid,answer,qid):
    import nltk
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    pstv=0
    ngtv=0
    ntl=0
    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(answer)
    a = float(ss['pos'])
    b = float(ss['neg'])
    c = float(ss['neu'])
    score = 2.5
    if (ss['neu'] > ss['pos'] and ss['neu'] > ss['neg']):
        pass
    if (ss['neg'] > ss['pos']):
        negva = 5 - (5 * ss['neg'])
        if negva > 2.5:
            negva = negva - 2.5
        score = negva
    else:
        negva = 5 * ss['pos']
        if negva < 2.5:
            negva = negva + 2.5
        score = negva
    cmd.execute("update councilres set score='"+str(score)+"' where uid='"+str(uid)+"' and qid='"+qid+"' ")
    con.commit()
    return "ol"

obj.run(host='0.0.0.0',port=5000)





