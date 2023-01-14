##Import required modules
import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import uploads.search 

##Initialise flask app
app = Flask(__name__)


@app.route('/')
def input():
    return render_template('index.html')

uploads_dir = os.path.join('uploads')
os.makedirs(uploads_dir, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['doc_file']
        if uploaded_file.filename == '':
            return render_template('index.html')
        else:
            uploaded_file.save(os.path.join("./uploads/sample.docx"))
            return redirect(url_for('home'))
    return render_template('index.html')

    
@app.route('/backend')
def backend():
    return uploads.search.poll()

@app.route('/home')
def home():
    return render_template('./resumebuilder/main/home.html')

@app.route('/awards')
def awards():
    return render_template('./resumebuilder/awards/awards.html')

@app.route('/education')
def education():
    return render_template('./resumebuilder/education/education.html')

@app.route('/experience')
def experience():
    return render_template('./resumebuilder/experience/experience.html')


@app.route('/convert')
def convert():
    return app.function

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8080', debug=True, use_reloader=True)
    