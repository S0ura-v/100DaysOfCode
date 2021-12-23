from flask import Flask, render_template, redirect, request
from wtforms import fields
from flask_wtf import Form
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
from smtplib import SMTP 
import os

# initialize the flask app and database
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///contact_info.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# defining the database 
class Info(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.String(500), nullable=False)


# main route
@app.route("/")
def main(): 
    return render_template("index.html")

@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        # test  
        print("Here Boy\n\n\n")

        # defining the variables 
        from_email = os.getenv('EMAIL')
        print(from_email)
        to_email = os.getenv('PERSONAL_EMAIL')
        print(to_email)
        password = os.getenv('PASSWORD')
        print(password+"\n\n\n")
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        print("Here Boy1\n\n\n")
        # checking some parameters here
        mail_message = f"Subject: New E-Mail from personal website\n\nSender's Email: {email}\nName of Sender: {name}\n{message}"
        
        if (len(name) < 101 and len(name) > 0) and (len(email) < 100 and len(email) > 0) and (len(message) < 500 and len(message) > 0):
            # sending mail 
            smtp = SMTP(host="smtp.gmail.com", port=42069)
            smtp.starttls()
            smtp.login(from_email, password)
            smtp.sendmail(from_addr=from_email, to_addr=to_email, msg=mail_message)
            smtp.close()

            # adding to SQL database 
            new_contact = Info(name=name, email=email, message=message)
            db.session.add(new_contact)
            db.session.commit()

            # redirecting 
            return render_template("success.html", name=name)
        
        return render_template("error.html", name=name)
    else:
        return render_template("contact.html")
# running the script
if __name__ == "__main__":
    app.run(debug=True)