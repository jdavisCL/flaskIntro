from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
    name = 'Jake'
    projectList = ["Rock Paper Scissors", "Tic Tac Toe", "Platformer", "Space Shooter", "Web Page", "Bitmaps"]
    return render_template('index.html', title='Welcome', username=name, projects=projectList)

@app.route('/hello')
def hello():
    return "Hello World"

@app.route('/name')
def displayName():
    return "Jake"

@app.route('/product/<name>')
def get_product(name):
    return "The product is " + str(name)

@app.route('/dashboard/<name>')
def dashboard(name):
    return "Welcome to the site " + str(name)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for('dashboard',name=user))
    else:
        return render_template('login.html')
    
@app.route('/journal')
def journal():
    return render_template('journal.html')

@app.route('/journalentry', methods= ['POST', 'GET'])
def showEntry():
    if request.method == "POST":
        entry = request.form
        return render_template('journalEntry.html', entry=entry)

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/uploader', methods= ['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        file.save(file.filename)
        return "File uploaded Successfully"

if __name__ == '__main__':
    app.run(debug=True)