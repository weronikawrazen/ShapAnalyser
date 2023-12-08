from flask import Flask, render_template, url_for, request, session
from create_reg import Feature, generate_data
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
                session["r_seed_DGP"] = r_seed_DGP

            if ('x1_dist' and 'x1_min_avg' and 'x1_min_avg' and 'x1_max_var' and 'x1_coeff') in request.form:
                X1 = Feature('x1',request.form["x1_dist"],request.form["x1_min_avg"],request.form["x1_max_var"],request.form["x1_coeff"])
                session["X1"] = X1

            if ('x2_dist' and 'x2_min_avg' and 'x2_min_avg' and 'x2_max_var' and 'x2_coeff') in request.form:
                X2 = Feature('x2',request.form["x2_dist"],request.form["x2_min_avg"],request.form["x2_max_var"],request.form["x2_coeff"])
                session["X2"] = X2
            
            if ('x3_dist' and 'x3_min_avg' and 'x3_min_avg' and 'x3_max_var' and 'x3_coeff') in request.form:
                X3 = Feature('x3',request.form["x3_dist"],request.form["x3_min_avg"],request.form["x3_max_var"],request.form["x3_coeff"])
                session["X3"] = X3                
            
            if ('x4_dist' and 'x4_min_avg' and 'x4_min_avg' and 'x4_max_var' and 'x4_coeff') in request.form:
                X4 = Feature('x4',request.form["x4_dist"],request.form["x4_min_avg"],request.form["x4_max_var"],request.form["x4_coeff"])
                session["X4"] = X4
            
            if ('x5_dist' and 'x5_min_avg' and 'x5_min_avg' and 'x5_max_var' and 'x5_coeff') in request.form:
                X5 = Feature('x5',request.form["x5_dist"],request.form["x5_min_avg"],request.form["x5_max_var"],request.form["x5_coeff"])
                session["X5"] = X5 

            if ('x6_dist' and 'x6_min_avg' and 'x6_min_avg' and 'x6_max_var' and 'x6_coeff') in request.form:
                X6 = Feature('x6',request.form["x6_dist"],request.form["x6_min_avg"],request.form["x6_max_var"],request.form["x6_coeff"])
                session["X6"] = X6                

            return render_template("genreg.html")    
    
    @app.route('/regression', methods = ["GET", "POST"])
    def create_regression():
        X1 = session.get("X1")
        X2 = session.get("X2")
        X3 = session.get("X3")
        X4 = session.get("X4")
        X5 = session.get("X5")
        X6 = session.get("X6")
        r_seed_DGP = session.get("r_seed_DGP")

        X1.values, X2.values, X3.values, X4.values, X5.values, X6.values = generate_data(X1,X2,X3,X4,X5,X6, r_seed_DGP)


        return "ok"


    return app

app = create_app()

if __name__ == '__main__':
    app.run()


#deactivate
