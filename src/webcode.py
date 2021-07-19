from flask import *
import pymysql
con=pymysql.connect(host="localhost",port=3306,user="root",password="",db="medbot")
cmd=con.cursor()

obj=Flask(__name__)

@obj.route('/')
def main():
    return render_template('login.html')

@obj.route('/login',methods=['post','get'])
def login():
    uname=request.form['textfield']
    pwd=request.form['textfield2']
    cmd.execute("select * from login where user_name='"+uname+"' and password='"+pwd+"'")
    s=cmd.fetchone()
    if s is None:
        return '''<script>alert("Invalid username or password");window.location='/'</script>'''
    elif  s[3]=='admin':
        return '''<script>alert("login successfull");window.location='/home'</script>'''

    else :
        return '''<script>alert("Invalid");window.location='/'</script>'''

@obj.route('/logout')
def logout():
    return '''<script>alert("Successfully logged out");window.location='/'</script>'''
@obj.route('/home')
def home():
    return render_template('home.html')
@obj.route('/disease')
def disease():
    con = pymysql.connect(host="localhost", port=3306, user="root", password="", db="medbot")
    cmd = con.cursor()
    cmd.execute("select * from diseases")
    s=cmd.fetchall()
    return render_template('Diseasemain.html',val=s)

@obj.route('/diseaserest',methods=['post','get'])
def diseaseres():
    return render_template('Disease.html')

@obj.route('/adddisease',methods=['post','get'])
def adddisease() :
    disease = request.form['textfield2']
    treatment = request.form['textfield3']
    preventive = request.form['textfield']
    cmd.execute("insert into diseases values(Null,'"+disease+"','"+treatment+"','"+preventive+"')")
    con.commit()
    return '''<script>alert("Insertion successfull");window.location='/disease'</script>'''


@obj.route('/HomeRemedies')
def Homerem():
    cmd.execute("select * from remedies")
    s = cmd.fetchall()
    return render_template('home remedies.html',val=s)

@obj.route('/addremedy',methods=['post','get'])
def addrem() :
    disease = request.form['textfield']
    remedy = request.form['textfield2']
    instruction = request.form['textfield3']
    cmd.execute("insert into remedies values(Null,'"+disease+"','"+remedy+"','"+instruction+"')")
    con.commit()
    return '''<script>alert("Insertion successfull");window.location='/HomeRemedies'</script>'''



@obj.route('/Symptom')
def symptom():
    con = pymysql.connect(host="localhost", port=3306, user="root", password="", db="medbot")
    cmd = con.cursor()
    cmd.execute("select * from diseases")
    s=cmd.fetchall()
    cmd.execute("SELECT `diseases`.`Disease`,`symptoms`.* FROM `diseases` JOIN `symptoms` ON `diseases`.`Disease_id`=`symptoms`.`Disease`")
    x = cmd.fetchall()
    return render_template('Symptom.html',val=s,value=x)

@obj.route('/addsymptom',methods=['post','get'])
def addsymptom():
    disease = request.form['select']
    symptom = request.form['textfield']
    cmd.execute("insert into symptoms values(Null,'"+symptom+"','"+disease+"')")
    con.commit()
    return '''<script>alert("Insertion successful");window.location='/Symptom'</script>'''


@obj.route('/Vaccine')
def Vaccine():
    cmd.execute("select * from vaccines")
    s=cmd.fetchall()
    return render_template('vaccine.html',val=s)
@obj.route('/viewsymptom')
def viewsymptom():
    id = request.args.get('id')
    cmd.execute("select * from symptoms where disease='"+id+"'")
    sym=cmd.fetchall()
    return (render_template('viewsymptom.html',var=sym))
@obj.route('/addvaccine',methods=['post','get'])
def addvaccine() :
    vaccinename = request.form['textfield']
    use = request.form['textfield2']
    dosage = request.form['textfield3']
    cmd.execute("insert into vaccines values(Null,'"+vaccinename+"','"+use+"','"+dosage+"')")
    con.commit()
    return '''<script>alert("Insertion successfull");window.location='/Vaccine'</script>'''

@obj.route('/Councilque')
def Councilque():
    cmd.execute("select * from query")
    s = cmd.fetchall()
    return render_template('counque.html',val=s)

@obj.route('/addcounque',methods=['post','get'])
def addconque() :
    query = request.form['textfield1']
    cmd.execute("insert into query values(Null,'"+query+"')")
    con.commit()
    return '''<script>alert("Insertion successfull");window.location='/Councilque'</script>'''


@obj.route('/Councilres')
def Councilres():
    cmd.execute("select * from council")
    s=cmd.fetchall()
    return render_template('counresult.html',val=s)
@obj.route('/addcouncil',methods=['post','get'])
def addcouncil():
    score = request.form['textfield']
    result = request.form['textfield2']
    cmd.execute("insert into council values('"+score+"','"+result+"',Null,Null)")
    con.commit()
    return '''<script>alert("Insertion successful");window.location ='/Councilres'</script>'''

@obj.route('/Diet')
def Diet():
    cmd.execute("select * from diet")
    s=cmd.fetchall()
    return render_template('dietresult.html',val=s)

@obj.route('/adddiet',methods=['post','get'])
def adddiet():
    BMIscore = request.form['textfield']
    BMIage =  request.form['textfield4']
    drinks = request.form['textfield2']
    food = request.form['textfield3']
    exercise = request.form['textfield5']
    cmd.execute("insert into diet values ('"+BMIscore+"','"+drinks+"','"+food+"','"+exercise+"','"+BMIage+"',Null)")
    con.commit()
    return '''<script>alert("Insertion successful");window.location = '/Diet'</script>'''

@obj.route('/deletedisease')
def deletedisease():
    id = request.args.get('id')
    cmd.execute("delete from diseases where Disease_id='"+id+"'")
    con.commit()
    return '''<script>alert("Deletion Successful");window.location='/disease'</script>'''
@obj.route('/deleterem')
def deleterem():
    id = request.args.get('id')
    cmd.execute("delete from remedies where Rem_id='" + id + "'")
    con.commit()
    return '''<script>alert("Deletion Successful");window.location='/HomeRemedies'</script>'''

@obj.route('/deletesymptom')
def deletesymptom():
    id = request.args.get('id')
    cmd.execute("delete from symptoms where S_id='"+id+"'")
    con.commit()
    return '''<script>alert("Deletion Successful");window.location='/Symptom'</script>'''

@obj.route('/deletevaccine')
def deletevaccine():
    id = request.args.get('id')
    cmd.execute("delete from vaccines where V_id='"+id+"'")
    con.commit()
    return '''<script>alert("Deletion Successful");window.location='/Vaccine'</script>'''

@obj.route('/deletecouncilque')
def deleteconcilque():
    id = request.args.get('id')
    cmd.execute("delete from query where query_id='"+id+"'")
    con.commit()
    return '''<script>alert("Deletion Successful");window.location='/Councilque'</script>'''

@obj.route('/deletecouncilres')
def deleteconcilres():
    id = request.args.get('id')
    cmd.execute("delete from council where score_id='"+id+"'")
    con.commit()
    return '''<script>alert("Deletion Successful");window.location='/Councilres'</script>'''

@obj.route('/deletediet')
def deletediet():
    id = request.args.get('id')
    cmd.execute("delete from diet where diet_id='"+id+"'")
    con.commit()
    return '''<script>alert("Deletion Successful");window.location='/Diet'</script>'''
































obj.run(debug=True)