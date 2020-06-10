import basilica

import os
from dotenv import load_dotenv

load_dotenv()
BASILICA_API_KEY = os.getenv('BASILICA_API_KEY')

connection = basilica.Connection(BASILICA_API_KEY)
print(type(connection))

if __name__ == '__main__':

    embeddings = connection.embed_sentences(["Hello world!", "How are you?"])
    print(list(embeddings)) # [[0.8556405305862427, ...], ...]
