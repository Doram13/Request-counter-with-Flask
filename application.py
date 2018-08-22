from flask import Flask, render_template, redirect

app = Flask(__name__)

counts = 0
prp = {GET: 0, POST: 0, DELETE: 0, PUT: 0}


@app.route('/')
def route_index():
    return render_template('index.html', counter = counts)

@app.route('/request_counter')
def request_counter():
     global counts
     counts += 1
     return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)