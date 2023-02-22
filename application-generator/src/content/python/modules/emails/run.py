from flask import Flask, request, render_template, jsonify
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv
from threading import Thread
from flask_moment import Moment
   
load_dotenv()
app = Flask(__name__)
moment = Moment(app)

# # configuration of mail
app.config['MAIL_SERVER']=os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = os.getenv('MAIL_PORT')
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')

# use the app password created 
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS')
app.config['MAIL_USE_SSL'] = False

# instantiating the mail service only after the 'app.config' to avoid error   
mail = Mail(app)

   
@app.route("/api/email/send", methods=['GET', 'POST'])
def Send_email():
    # try and except method
    #to avoid the app crashing if the message does not go through due to network or something
    try:
        # if it is a post request
        if request.method == 'POST':
            #getting the json inputs and referencing them
            if request.json['template'] == "userContactUs": #working
                data = {
				"MSender": request.json['MSender'],
				"Memail": request.json['Memail'],
				"Phone": request.json['Phone'],
				"Msubject": request.json['Msubject'],
				"Message": request.json['Message']
			    }
            elif request.json['template'] == "reset": #working
                data = {
				"url": request.json['url'],
				"first_name": request.json['first_name']
			    }
            elif request.json['template'] == "productApproved": #working
                data = {
				"first_name": request.json['first_name'],
				"product_name": request.json['product_name'],
				"product_slug": request.json['product_slug']
			    }
            elif request.json['template'] == "subAccountCreated": # working
                data = {
				"first_name": request.json['first_name'],
				"user_name": request.json['user_name'],
				"password": request.json['password']
			    }
            elif request.json['template'] == "unListProduct": #working
                data = {
				"first_name": request.json['first_name'],
				"product_name": request.json['product_name']
			    }
            elif request.json['template'] == "vendorApproved": #working
                data = {
				"first_name": request.json['first_name'],
				"business_name": request.json['business_name'],
				"business_slug": request.json['business_slug']
			    }
            elif request.json['template'] == "vendorCreated": #working
                data = {
				"first_name": request.json['first_name'],
				"business_name": request.json['business_name']
			    }
            elif request.json['template'] == "unListVendor": #working
                data = {
				"first_name": request.json['first_name'],
				"business_name": request.json['business_name']
			    }
            elif request.json['template'] == "orderComplete": 
                data = {
				"first_name": request.json['first_name'],
				"order_id": request.json['order_id']
			    }
            elif request.json['template'] == "orderNotComplete": 
                data = {
				"first_name": request.json['first_name']
			    }
            elif request.json['template'] == "lowProduct": #working
                data = {
				"first_name": request.json['first_name'],
				"business_name": request.json['business_name'],
				"remaining_quantity": request.json['remaining_quantity'],
				"product_name": request.json['product_name']
			    }
            else: #working
                data = {
				"first_name": request.json['first_name']
			    }

            sender = "donotreply@bestdealnaija.com"
            subject = request.json['subject']
            recipient = request.json['email']
            template = request.json['template']
            # inputing the message in the correct order
            msg = Message(subject,sender=sender,recipients =[recipient] )
           
            #msg.body = message
            msg.body = render_template(template + '.txt', **data)
            msg.html = render_template(template + '.html', os=os, **data)
            mail.send(msg)

            response = jsonify({
				'message': 'Email sent'
			})
            return response
            #return "message Sent"
        #return render_template('reset.html', os=os, **data)
    except Exception as e:
        return f'<p>{e} </p>'
thread = Thread(target=Send_email)
        # run the thread
thread.start()
    
   
if __name__ == '__main__':
    # for app to run and debug to True
   app.run(port=5005, debug = True)