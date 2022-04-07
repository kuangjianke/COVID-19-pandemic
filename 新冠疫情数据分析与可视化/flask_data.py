from flask_dome import Flask, render_template
from 比赛b题.flask_total import *
flask = FLASK_DATA()
app = Flask(__name__)


@app.route('/')  # 玫瑰图
def flasks_1():
    return render_template('柱状图.html', lists=flask.pandas_ht()[0], counts=flask.pandas_ht()[1])
if __name__ == '__main__':
    app.run(debug=True)
