from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin:0 auto;
                width: 540px;
                font: 16px san-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/encrypt" method="post">
        <label for="rotateby">Rotate By:<input type="text" name="rot" value="0">
        <textarea name="text">{0}</textarea>
        <input type="submit" value="Submit Query">
    </body>
</html>
"""
@app.route("/encrypt", methods=["POST"])
def encrypt():
    text = request.form['text']
    rot = int(request.form['rot'])
    encrypted_text = rotate_string(text, rot)
    return form.format(encrypted_text)


@app.route("/")
def index():
    content = form
    return form.format("")


app.run()