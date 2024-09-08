from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects/<index>')
def projects(index):
    header = ['Сапер', 'Приключения колобка', 'Сайт с гороскопами']
    number = int(index)
    left_number = number - 1
    right_number = number + 1
    if number == 0:
        left_number = 2
    if number == 2:
        right_number = 0

    with open(f'static/text/{number}.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    return render_template('projects.html', number=number, left_number=left_number, right_number=right_number, text=text, header=header[number])

if __name__ == '__main__':
    app.run(debug=True)