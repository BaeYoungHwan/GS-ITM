from flask import Flask, render_template, send_file

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('main.html')

@app.route('/Seoul')
def map_gu():
    return render_template('Map_gu.html')

@app.route('/Plant')
def Plant():
    return render_template('index.html')

@app.route('/sector')
def grid():
    return render_template('inner.html')

@app.route('/rec')
def recommend():
    return render_template('rec.html')

@app.route('/repo')
def report():
    return render_template('report.html')

@app.route('/benefit')
def benefit():
    return render_template('benefit.html')

if __name__ == '__main__':
    app.run()