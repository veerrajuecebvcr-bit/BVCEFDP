from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num_subjects = int(request.form['num_subjects'])
        return render_template('marks.html', num_subjects=num_subjects)
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num_subjects = int(request.form['num_subjects'])
    marks = [float(request.form[f'mark_{i}']) for i in range(num_subjects)]
    total = sum(marks)
    percentage = total / num_subjects
    if percentage >= 90:
        grade = 'A'
    elif percentage >= 80:
        grade = 'B'
    elif percentage >= 70:
        grade = 'C'
    elif percentage >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return render_template('result.html', percentage=percentage, grade=grade)

if __name__ == '__main__':
    app.run(debug=True)
