from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    user_info = {
        'name': 'Alex Jensen',
        'role': 'Data Engineer',
        'projects': ['Data Platform', 'ETL Pipelines', 'Cloud Solutions'],
        'email': 'alex.jensen@example.com'
    }
    return render_template('index.html', user=user_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)