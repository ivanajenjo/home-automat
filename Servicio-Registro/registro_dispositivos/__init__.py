import markdown
import os
#Import Framework
from flask import Flask

#Crear una instancia de Flask
app = Flask(__name__)

@app.route("/")
def index():
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:
        content = markdown_file.read()

        return markdown.markdown(content)
    