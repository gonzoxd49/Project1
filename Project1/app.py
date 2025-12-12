Python 3.13.7 (v3.13.7:bcee1c32211, Aug 14 2025, 19:10:51) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> from flask import Flask, render_template, request, redirect, url_for
... 
... app = Flask(__name__)
... 
... # In-memory storage for timesheet entries
... timesheet_entries = []
... 
... @app.route('/')
... def index():
...     return render_template('index.html', entries=timesheet_entries)
... 
... @app.route('/add', methods=['GET', 'POST'])
... def add_entry():
...     if request.method == 'POST':
...         date = request.form['date']
...         task = request.form['task']
...         hours = request.form['hours']
...         timesheet_entries.append({'date': date, 'task': task, 'hours': hours})
...         return redirect(url_for('index'))
...     return render_template('add.html')
... 
... if __name__ == '__main__':
