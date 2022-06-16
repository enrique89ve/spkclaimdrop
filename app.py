from ast import Not
import datetime
import calendar
from flask import Flask, render_template, jsonify, request, redirect
import werkzeug
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from form import consulta
import json
import requests 
import re
import json
import time 
from valid import username_is_valid, username_ready
from werkzeug.wrappers.request import Request
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.middleware.proxy_fix import ProxyFix

import configparser, os

node = 'https://spkinstant.hivehoneycomb.com/'



app = Flask(__name__)




def accountapi(ac):

    
    urlapi = node+"@"+ac
    reponse = requests.get(urlapi)
    data = reponse.json()


    return data




@app.route('/', methods=["GET", "POST"])
def claim():


    


    try:

        if request.method == 'POST':

            time.sleep(30)
            
            return redirect("/")
            

            

        

        else:
            


            

        
        

            

            return render_template( "base.html")

           

    
        

        
    except (UnboundLocalError):

       return redirect("/")



@app.route('/stats', methods=["GET", "POST"])
def stats():

    try:
        form = consulta(request.form)


            
        
        if request.method == 'POST' and form.validate():

            

            userconsulta = request.form['username']

        


            if userconsulta is None:
                pass
            
            else:
                ac = userconsulta.isnumeric()

                
            
            if ac is False:

            
                ac = userconsulta


                if not username_is_valid(ac):

                    return render_template("statsext.html", error = "invalid user" ) 

                    

                    

                else:


                    if username_ready(ac):


                        return render_template("statsext.html", error = "invalid user" ) 

                        
                        

            
                    else: 
                        data = accountapi(ac)


                        balance = data['balance']

                        tokens = balance/1000

                        drop = data['drop']

                        snap = drop['availible']

                        meslast = drop['last_claim']

                        monthinteger = int(meslast)
                        month = calendar.month_name[monthinteger]
                        
                        





                        cantidad = snap['amount']/1000

                        if cantidad == 0:

                            reclamados = "There are no pending tokens to claim"

                            datos  = (" @%s your balance %s LARYNX / %s" % (ac, tokens, reclamados,  ))

                        else: 
                            reclamados = cantidad
                    

                            datos  = (" @%s your balance: %s LARYNX  / Last claimed %s" % (ac, tokens, month,  ))

                        datos = datos

            return render_template("statsext.html", datos = datos)

        return render_template("stats.html")
    except (UnboundLocalError):

        return redirect("/")
    
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly

    time.sleep(5)
    
    return redirect("/")
        


@app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    return 'bad request!', 400



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3500)