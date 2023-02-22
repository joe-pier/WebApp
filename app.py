from flask import Flask, render_template

app = Flask(__name__) # instance of class Flask

@app.route("/") # any website has a route. a part of the url after the url
# this is going to match the empty route
def hello_world():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = True)