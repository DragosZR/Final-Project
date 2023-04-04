from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Cluj-Napoca, Romania',
        'salary': '7420 RON',
    },
    {
        'id': 2,
        'title': 'Front-End Engineer',
        'location': 'Cluj-Napoca, Romania',
        'salary': '10100 RON'
    },
    {
        'id': 3,
        'title': 'Data Scientist',
        'location': 'Cluj-Napoca, Romania',
        'salary': '4400 RON'
    },
    {
        'id': 4,
        'title': 'Full-Stack Engineer',
        'location': 'Cluj-Napoca, Romania',
        'salary': '7100 RON'
    }
]


@app.route("/")
def hello_python():
    return render_template('home.html', jobs=JOBS, company_name='TechLand')


@app.route("/jobs/")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(debug=True)
