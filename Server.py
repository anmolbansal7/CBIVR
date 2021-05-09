import numpy as np
from PIL import Image
from DeepFeatures import DeepFeatures
from datetime import datetime
from flask import Flask, request, render_template
from pathlib import Path

app = Flask(__name__)

df = DeepFeatures()
features = []
img_paths = []
for feature_path in Path("./static/feature").glob("*.npy"):
    features.append(np.load(feature_path))
    img_paths.append(Path("./static/image") / (feature_path.stem + ".jpg"))
features = np.array(features)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['query_img']
        img = Image.open(file.stream)
        uploaded_img_path = "static/uploaded/" + datetime.now().isoformat().replace(":", ".") + "_" + file.filename
        img.save(uploaded_img_path)
        query = df.extract(img)
        dists = np.linalg.norm(features-query, axis=1)
        ids = np.argsort(dists)[:5]
        scores = [(dists[id], img_paths[id]) for id in ids]

        return render_template('index.html', query_path=uploaded_img_path, scores=scores)
    else:
        return render_template('index.html')
    
"""@app.route('/login', methods=['POST'])
def upload():
    if request.method == 'POST':
       file = request.files['query_img']
        img = Image.open(file.stream)
        uploaded_img_path = "static/uploaded/" + datetime.now().isoformat().replace(":", ".") + "_" + file.filename
        img.save(uploaded_img_path)
"""

if __name__=="__main__":
    app.run(host = "127.0.0.1", port = 8000)