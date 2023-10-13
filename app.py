from flask import Flask, render_template, request, redirect, flash
import psycopg2
import requests
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import html
import config

################################################# VARS
host = config.host
db_user = config.db_user
db_pass = config.db_pass
db_name = config.db_name


app = Flask(__name__)
connection = psycopg2.connect(host=host, user=db_user, password=db_pass, database=db_name)
connection.autocommit = True
app.config['SECRET_KEY'] = 'fdsakhggfakhgfds'
# cursor = connection.cursor()

def send_email(send_to, page):
	HOST = config.exhanage_server
	TO = send_to
	FROM = "cybersecurity@yamalspg.ru"
	msg = MIMEMultipart('alternative')
	msg['Subject'] = 'Welcome Email'
	msg['From'] = FROM
	msg['To'] = TO
	msg.attach(MIMEText(page, 'html'))
	server = smtplib.SMTP(HOST)
	server.sendmail(FROM, [TO,'dmitriy.bezzubikov@yamalspg.ru'], msg.as_string())
	server.quit()

def KeepassToDB(values):
    with connection.cursor() as cur:
        cur.execute("""DROP TABLE IF EXISTS keepass""")
        cur.execute("""CREATE TABLE IF NOT EXISTS keepass(
            username text PRIMARY KEY,
            password text
        )""")
        cur.executemany("""INSERT INTO keepass(username,password) VALUES(LOWER(%s),%s)""", values)


def FetchFromDB(id):
	with connection.cursor() as cursor:
		cursor.execute(f'''SELECT * from keepass WHERE username='{id}' ''')
		result = cursor.fetchone()
		return result

def FetchFromISE(id):
	url = f"https://{config.ise_server}:9060/ers/config/internaluser/?filter=name.EQ." + id

	payload = {}
	headers = {
		'Accept': 'application/json',
		'Content-Type': 'application/json',
		'Authorization': 'Basic Z29kb2ZhcGk6V2F1bXo5NHNjSA==',
		'Cookie': 'APPSESSIONID=39CA9453A74728BE5CB3DA6610829DC1; JSESSIONIDSSO=87978D01CEC651AEEA9AC3F05CAA6B42'
	}
	response = requests.request("GET", url, headers=headers, data=payload, verify=False)
	jsonData = response.text
	dictData = json.loads(jsonData)
	clear_data = dictData["SearchResult"]["resources"]
	try:
		ise_user_password = str(clear_data[0].get("description"))
		return ise_user_password
	except:
		ise_user_password = None
		return ise_user_password



@app.route('/', methods =["GET", "POST"])
def gfg():
	if request.method == "POST" and request.form.get("lname").lower() != '':
		samaccountname = request.form.get("lname").lower()
		master_pass = FetchFromDB(samaccountname)
		ise_user_password = FetchFromISE(samaccountname)
		to_email = samaccountname + "@yamalspg.ru"
		if master_pass is None and ise_user_password is None:
			return redirect("/errorfull")
		elif master_pass is None and ise_user_password is not None:
			page = html.html_func(samaccountname, ise_user_password, 'None')
			send_email(to_email, page)
			return redirect("/errormaster")
		elif master_pass is not None and ise_user_password is None:
			page = html.html_func(samaccountname, 'None', master_pass[1])
			send_email(to_email, page)
			return redirect("/errorise")
		else:
			page = html.html_func(samaccountname, ise_user_password, master_pass[1])
			send_email(to_email, page)
			flash(f'{samaccountname}')
			return render_template("success.html")
	return render_template('index.html')

@app.route('/errorfull', methods=['GET', 'POST'])
def errorfull():
	if request.method == 'POST':
		if request.form.get('action1') == 'Да':
			return redirect(config.service_desk)
		elif request.form.get('action2') == 'Нет':
			return redirect('/')
	return render_template('/errorfull.html')

@app.route('/errormaster', methods=['GET', 'POST'])
def errormaster():
	if request.method == 'POST':
		if request.form.get('action1') == 'Да':
			return redirect(config.service_desk)
		elif request.form.get('action2') == 'Нет':
			return redirect('/')
	return render_template('/errormaster.html')

@app.route('/errorise', methods=['GET', 'POST'])
def errorise():
	if request.method == 'POST':
		if request.form.get('action1') == 'Да':
			return redirect(config.service_desk)
		elif request.form.get('action2') == 'Нет':
			return redirect('/')
	return render_template('/errorise.html')

@app.route('/QA', methods =["GET"])
def qa():
	return render_template('QA.html')


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port='5000')

