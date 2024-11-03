Задание 1

Найдите ошибку в коде:


from flask import Flask


app = Flask(__name__)


@app.route('')

def home():

   return 'Hello, World!'



if __name__ == '__main__':

   app.run()

Ошибка:
Путь в декораторе @app.route('') не может быть пустым, например ('/') 
