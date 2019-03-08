from flask import Flask, render_template, request
from random import choice
app = Flask(__name__)

rps_dict = {
            'rock': {'paper': 'loses', 'scissors': 'wins', 'rock': 'ties'},
            'paper': {'paper': 'ties', 'scissors': 'loses', 'rock': 'wins'},
            'scissors': {'paper': 'wins', 'scissors': 'ties', 'rock': 'loses'}
}

computer = ['rock', 'paper', 'scissors']




@app.route('/')
def home():
    return render_template('index.html')


@app.route('/result', methods=['POST', 'GET'])
def play():
    winner = ''
    player = ''
    comp = choice(computer)
    if request.form['my_options'] == 'rock':
        player = 'rock'
    elif request.form['my_options'] == 'paper':
        player = 'paper'
    elif request.form['my_options'] == 'scissors':
        player = 'scissors'
    else:
        return render_template('index.html')
    comp_str = f'Computer chooses: {comp}.'
    play_str = f'Player chooses: {player}.'
    resolution = f'Player {rps_dict[player][comp]}.'

    return render_template('index.html', comp_str=comp_str, play_str=play_str, resolution=resolution)



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)
