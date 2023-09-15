import base64
import random
from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
from elasticsearch import Elasticsearch

app = Flask(__name__)

# Replace with your Elasticsearch server URL
es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme': 'http'}])

# Initialize global variables to keep track of thread IDs
thread_id_counter = 1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    try:
        global thread_id_counter

        # Generate a random 3-digit op_id
        op_id = random.randint(100, 999)
        thread_text = request.form.get("thread_text")

        image = request.files['image']
        if image:
            image_data = image.read()
            base64_encoded = base64.b64encode(image_data).decode("utf-8")

            # Use the current thread_id (incremented) as the document ID
            doc_id = str(thread_id_counter)
            thread_id_counter += 1

            document = {
                'thread_id': doc_id,
                'op_id': op_id,
                'thread_text': thread_text,
                'image_data': base64_encoded
            }

            index_name = 'thread'

            es.index(index=index_name, id=doc_id, body=document)

            return redirect(url_for('success'))
        else:
            return "No image uploaded."
    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.route('/success')
def success():
    return "Image encoded and stored in Elasticsearch."

if __name__ == '__main__':
    app.run(debug=True, port=6000)
