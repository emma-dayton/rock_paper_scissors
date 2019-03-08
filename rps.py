from flask import Flask, render_template
app = Flask(__name__)

rps_dict = {
            'rock': {'paper': 'lose', 'scissors': 'win', 'rock': 'tie'},
            'paper': {'paper': 'tie', 'scissors': 'lose', 'rock': 'win'},
            'scissors': {'paper': 'win', 'scissors': 'tie', 'rock': 'lose'}
}

@app.route('/')
def home():
    return render_template('index.html')








if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)
