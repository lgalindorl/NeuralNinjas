from flask import Flask,  request, render_template, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/files'


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 


#upload files and serve base file
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if 'file' not in request.files:
            print("file not in request.files")
            return render_template('submit.html')
            
        file = request.files['file']

        if file.filename == "":
            print("file has no name")
            return render_template('submit.html')
        
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(pp.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('results', name=filename))

    return render_template('submit.html')

#serve results
