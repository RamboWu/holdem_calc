from flask import Flask
import holdem_calc
import holdem_argparser
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test')
def test_func():
    print 'test success'
    return 'test success!'

@app.route('/calc')
def calc_holdem():
    print 'calc call success'
    exact = False
    num = 100000
    hole_cards_args = ['Kc', 'Kh', 'Ac', 'Ah']
    board_args = ['5c', '6c', '7c']
    hole_cards, board = holdem_argparser.parse_cards(hole_cards_args, board_args)
    holdem_calc.run(hole_cards, num, exact, board, None, True)
    return 'start World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
