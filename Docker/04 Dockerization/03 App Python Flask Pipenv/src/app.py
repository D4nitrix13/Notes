# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielBenjaminPerezMoralesDev13
# Gitlab: https://gitlab.com/DanielBenjaminPerezMoralesDev13
# Correo electrónico: danielperezdev@proton.me

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

