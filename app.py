from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 2,
        'title': 'Software Engineer',
        'company': 'Google',
        'location': 'San Francisco',
        'date': '2017-01-01',
        'description': 'I am a software engineer at Google. I love to code.'
    },
    {
        'id': 3,
        'title': 'Developer',
        'company': 'Microsoft',
        'location': 'Lviv',
        'date': '2024-01-01',
        'description': 'I am a software engineer at Microsoft. I love coding.'
    },
    {
        'id': 4,
        'title': 'Software Engineer',
        'company': 'Amazon',
        'location': 'Lviv',
        'date': '2024-01-01',
        'description': 'I am a good boy.'
    }
]

@app.route('/')
def hello_world():
    return render_template('home.html', JOBS=JOBS)



if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)