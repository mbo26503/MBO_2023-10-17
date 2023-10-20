# 20/10/2023 15:38
# Flask - serwer www
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
#    return "Hello Wrorld!"
    return render_template(('home.html'))  # wyswietlenie strony home.html


@app.route("/salvador:")
def salvador():
    return "hello Salvador"


if __name__ == '__main__':
    app.run(debug=True, port=8080)

