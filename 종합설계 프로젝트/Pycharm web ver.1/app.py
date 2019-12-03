from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    temp = request.args.get('id')
    List = ['알타리무', '상추', '배추', '신선초', '두릅', '콩나물', '아스파라거스', '부추', '무화과', '파', '곰치', '완두콩', '토마토', '수박', '고구마']
    if temp in List:
        return render_template('Test.html', data = temp)
    else:
        return render_template('error.html')


@app.route('/Angelica')
@app.route('/신선초')
def 신선초():
    return render_template('Angelica.html')
@app.route('/Altarimiu')
@app.route('/알타리무')
def 알타리무():
    return render_template('Altarimiu.html')
@app.route('/Arakua elata')
@app.route('/두릅')
def 두릅():
    return render_template('Arakua elata.html')
@app.route('/Asparagus')
@app.route('/아스파라거스')
def 아스파라거스():
    return render_template('Asparagus.html')
@app.route('/Bean sprouts')
@app.route('/콩나물')
def 콩나물():
    return render_template('sidebar-right.html')
@app.route('/Cabbage')
@app.route('/배추')
def 배추():
    return render_template('basic-grid.html')
@app.route('/Chives')
@app.route('/부추')
def 부추():
    return render_template('Chives.html')
@app.route('/Corn')
@app.route('/옥수수')
def 옥수수():
    return render_template('corn.html')
@app.route('/Fig')
@app.route('/무화과')
def 무화과():
    return render_template('fig.html')
@app.route('/Green onion')
@app.route('/파')
def 파():
    return render_template('Green onion.html')
@app.route('/Lettuce')
@app.route('/상추')
def 상추():
    return render_template('Lettuce.html')
@app.route('/Gomchwi')
@app.route('/곰치')
def 곰치():
    return render_template('Gomchwi.html')
@app.route('/Pakchoi')
@app.route('/배추')
def 청경채():
    return render_template('Pakchoi.html')
@app.route('/Pea')
@app.route('/완두콩')
def 완두콩():
    return render_template('Pea.html')
@app.route('/Sweetpotato')
@app.route('/고구마')
def 고구마():
    return render_template('Sweetpotato.html')
@app.route('/Tomato')
@app.route('/토마토')
def 토마토():
    return render_template('width.html')
@app.route('/Watermelon')
@app.route('/수박')
def 수박():
    return render_template('sidebar-left.html')
if __name__ == '__main__':
    app.run()
