import base64
from PIL import Image
from elasticsearch import Elasticsearch


image_file = input("Enter the path to the image file: ")

try:
    with open(image_file, "rb") as image:
        image_data = image.read()

        base64_encoded = base64.b64encode(image_data).decode("utf-8")

        es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme': 'http'}])
        doc_id = input("Enter an ID for the document: ") 
        thread_text = input("Enter the thread text: ")

        document = {
            'thread_id': 4, 
            'op_id': 554,  
            'thread_text': thread_text,  
            'image_data': base64_encoded
        }

        index_name = 'thread' 

        es.index(index=index_name, id=doc_id, body=document)

        print(f"Image encoded and stored in Elasticsearch index '{index_name}'")

except FileNotFoundError:
    print("File not found. Please enter a valid file path.")
except Exception as e:
    print(f"An error occurred: {str(e)}")