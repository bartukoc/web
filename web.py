from flask import Flask,  render_template
import random

app = Flask(__name__)



@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/rastgele_mizah")
def mizah():
    liste = ["sucuklu yumurta","koka kola vs babaci","babaci player"]

@app.route("/rastgele_gercek")
def rasgele():
    liste = ["alkim=muz","atilla=muz","atilla ve alkim hiyar yemekte","atilla ve alkim hiyarlarini dusurdu"]

    x = random.choice(liste)

    return render_template("rastgele.html", x=x )

    


app.run(debug=True)
