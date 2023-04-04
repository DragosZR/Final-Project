from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Cluj-Napoca, Romania',
        'salary': 'EUR 1700',
    },
    {
        'id': 2,
        'title': 'Front-End Engineer',
        'location': 'Cluj-Napoca, Romania',
        'salary': 'EUR 1300'
    },
    {
        'id': 3,
        'title': 'Data Scientist',
        'location': 'Cluj-Napoca, Romania',
    },
    {
        'id': 4,
        'title': 'Full-Stack Developer',
        'location': 'Cluj-Napoca, Romania',
        'salary': 'EUR 2000'
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
