from flask import Flask, render_template, url_for, request
from create_reg import Feature
# pip3 freeze > requirements.txt 
#.\venv\Scripts\activate 

#aiaia

#Tworzenie instancji klasy
#__name__ - nazwa modułu, z którego ta klasa będzie tworzona
def create_app():
    app = Flask(__name__)
    @app.route('/', methods = ["GET", "POST"]) #Określenie jaki kod tego programu ma się uruchomić, kiedy użytkownik wejdzie na strone
    def start_website():
        if request.method == "GET":
            return render_template("base.html")
        else:
            r_seed_DGP = "1"
            if 'r_seed_DGP' in request.form:
                r_seed_DGP = request.form["r_seed_DGP"]

            if ('x1_dist' and 'x1_min_avg' and 'x1_min_avg' and 'x1_max_var') in request.form:
                X1 = Feature('x1',request.form["x1_dist"],request.form["x1_min_avg"],request.form["x1_max_var"])

            return render_template("regression_settings.html", x1_dist = X1.distribution, x1_min_avg = X1.min_avg)    
    #@app.route('/exchange', methods = ["GET", "POST"])

    return app

app = create_app()

if __name__ == '__main__':
    app.run()


#deactivate
