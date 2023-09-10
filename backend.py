from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/portfolio')
def portfolio():
    return app.send_static_file('portfolio.html')

# @app.route('/portfolio')
# def portfolio():
#     return app.render_template('portfolio.html')

if __name__ == '__main__':
    app.run(debug=True)
