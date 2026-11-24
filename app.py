from flask import Flask, render_template, request, redirect

app = Flask(__name__)

expenses = []

@app.route('/')
def home():

    total = sum(item['amount'] for item in expenses)

    return render_template(
        'index.html',
        expenses=expenses,
        total=total
    )


@app.route('/add', methods=['POST'])
def add_expense():

    title = request.form['title']
    category = request.form['category']
    amount = float(request.form['amount'])

    expense = {
        'title': title,
        'category': category,
        'amount': amount
    }

    expenses.append(expense)

    return redirect('/')


@app.route('/delete/<int:index>')
def delete_expense(index):

    if 0 <= index < len(expenses):
        expenses.pop(index)

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)