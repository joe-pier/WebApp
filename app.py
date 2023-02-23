from flask import Flask, render_template, jsonify

app = Flask(__name__) # instance of class Flask

jobs =  [
        {
        "id":3,
        "title": "Data Analyst",
        "company": "Google",
        "jobdescription": "Python developer",
        "location": "Milan",
        "start": "01-01-2021",
        "end" : "01-06-2021"
        }
        ,
        {
        "id":1,
        "title": "Data & Analytics Consultant",
        "company": "PwC",
        "jobdescription": "mulesoft developer",
        "location": "Milan",
        "start": "06-06-2022",
        "end" : "01-12-2022"
        }
        ,
        {
        "id":2,
        "title": "Data Scientist",
        "company": "BendingSpoons",
        "jobdescription": "Python developer",
        "location": "Milan",
        "start": "01-01-2023"
        }
        ]

@app.route("/") # any website has a route. a part of the url after the url
# this is going to match the empty route
def home():
    return render_template('home.html', jobs= jobs, name = "Piergiorgio")

@app.route("/jobs")
def list_jobs():
    return jsonify(jobs)

@app.route("/ml")
def game():
    return jsonify(jobs)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = True)