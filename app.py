from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for simplicity
expenses = []

@app.route('/')
def index():
    total = sum(float(item['amount']) for item in expenses)
    return render_template('index.html', total=total)

@app.route('/log', methods=['GET', 'POST'])
def log_expense():
    if request.method == 'POST':
        item = request.form['item']
        amount = request.form['amount']
        expenses.append({'item': item, 'amount': amount})
        return redirect(url_for('history'))
    return render_template('log_expense.html')

@app.route('/history')
def history():
    return render_template('history.html', expenses=expenses)

if __name__ == '__main__':
    app.run(debug=True)