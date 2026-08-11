from flask import Flask, render_template, request, session
import os
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
app.secret_key="any string"
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from contacts')
    the_username = "anonyme"
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
@app.route("/add_one_user", methods=["GET","POST"])
def add_one_user():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescountry= query_db("select * from country")

        one_user = query_db("insert into user (username,email,password,phone,country_id) values (:username,:email,:password,:phone,:country_id)",hey)
        user = query_db('select * from user')

        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        session["current_user_id"]=last_user["id"]
        for x in ['username','email','password','phone','country_id']:
            session[x]=hey[x]


        return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry)


    touslescountry= query_db("select * from country")

    user = query_db('select * from user')
    one_user = query_db("select * from user limit 1", one=True)
    return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry)


@app.route("/user_sign_out", methods=["GET","POST"])
def user_sign_out():
    if request.method == 'POST':
        session["current_user_id"]=""
        for x in ['username','email','password','phone','country_id']:
            session[x]=""
        return redirect("/")


@app.route("/user_log_in", methods=["GET","POST"])
def user_login():
    if request.method == 'POST':
        hey=request.form
        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        try:
            session["current_user_id"]=last_user["id"]
            for x in ['username','email','password','phone','country_id']:
                session[x]=hey[x]
        except:
            return render_template("userlogin.html")
    return render_template("userlogin.html")
@app.route("/add_one_country", methods=["GET","POST"])
def add_one_country():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into country (name) values (:name)",hey)
        user = query_db('select * from country')

        return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")


    user = query_db('select * from country')
    one_user = query_db("select * from country limit 1", one=True)
    return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")

@app.route("/add_one_programming_session", methods=["GET","POST"])
def add_one_programming_session():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)

        uploaded_file = request.files['pic']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join('static/photos', uploaded_file.filename))

        hey["pic"]=uploaded_file.filename


        touslesuser= query_db("select * from user")

        one_user = query_db("insert into programming_session (title,description,user_id,timestamp,pic) values (:title,:description,:user_id,:timestamp,:pic)",hey)
        user = query_db('select * from programming_session')

        return render_template("programming_sessionform.html", programming_sessions=user, one_user=one_user, the_title="add new programming_session", touslesuser=touslesuser)


    touslesuser= query_db("select * from user")

    user = query_db('select * from programming_session')
    one_user = query_db("select * from programming_session limit 1", one=True)
    return render_template("programming_sessionform.html", programming_sessions=user, one_user=one_user, the_title="add new programming_session", touslesuser=touslesuser)

@app.route("/add_one_sewing_session", methods=["GET","POST"])
def add_one_sewing_session():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)

        uploaded_file = request.files['pic']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join('static/photos', uploaded_file.filename))

        hey["pic"]=uploaded_file.filename


        touslesuser= query_db("select * from user")

        one_user = query_db("insert into sewing_session (title,description,user_id,pic,timestamp) values (:title,:description,:user_id,:pic,:timestamp)",hey)
        user = query_db('select * from sewing_session')

        return render_template("sewing_sessionform.html", sewing_sessions=user, one_user=one_user, the_title="add new sewing_session", touslesuser=touslesuser)


    touslesuser= query_db("select * from user")

    user = query_db('select * from sewing_session')
    one_user = query_db("select * from sewing_session limit 1", one=True)
    return render_template("sewing_sessionform.html", sewing_sessions=user, one_user=one_user, the_title="add new sewing_session", touslesuser=touslesuser)

@app.route("/add_one_sport_session", methods=["GET","POST"])
def add_one_sport_session():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)

        uploaded_file = request.files['pic']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join('static/photos', uploaded_file.filename))

        hey["pic"]=uploaded_file.filename


        touslesuser= query_db("select * from user")

        one_user = query_db("insert into sport_session (title,description,user_id,pic,timestamp) values (:title,:description,:user_id,:pic,:timestamp)",hey)
        user = query_db('select * from sport_session')

        return render_template("sport_sessionform.html", sport_sessions=user, one_user=one_user, the_title="add new sport_session", touslesuser=touslesuser)


    touslesuser= query_db("select * from user")

    user = query_db('select * from sport_session')
    one_user = query_db("select * from sport_session limit 1", one=True)
    return render_template("sport_sessionform.html", sport_sessions=user, one_user=one_user, the_title="add new sport_session", touslesuser=touslesuser)

@app.route("/add_one_application_development", methods=["GET","POST"])
def add_one_application_development():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)

        uploaded_file = request.files['pic']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join('static/photos', uploaded_file.filename))

        hey["pic"]=uploaded_file.filename


        touslesuser= query_db("select * from user")

        one_user = query_db("insert into application_development (title,description,user_id,timestamp,pic,dev_or_prod_mode) values (:title,:description,:user_id,:timestamp,:pic,:dev_or_prod_mode)",hey)
        user = query_db('select * from application_development')

        return render_template("application_developmentform.html", application_developments=user, one_user=one_user, the_title="add new application_development", touslesuser=touslesuser)


    touslesuser= query_db("select * from user")

    user = query_db('select * from application_development')
    one_user = query_db("select * from application_development limit 1", one=True)
    return render_template("application_developmentform.html", application_developments=user, one_user=one_user, the_title="add new application_development", touslesuser=touslesuser)

