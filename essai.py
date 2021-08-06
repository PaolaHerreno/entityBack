#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from fonctions import *
from flask import Flask, jsonify
from flask import request
from flask import render_template
from flask_cors import CORS


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
CORS(app)
def get_all(chemin):
    humains = ouvrir_json(chemin)
    patterns = []
    for h in humains:
        label = h['label']
        id_ent = h['id_ent']
        liste_noms = get_names_list(label)
        pattern_final = get_pattern(liste_noms, "PERSON", id_ent)
        patterns.append(pattern_final)
    return patterns



@app.route('/')
def home():
    return render_template('homeEN.html')

@app.route('/', methods=['POST'])
def text_box():
    liste = get_all('humains_toMongo.json')
    ruler, nlp = initialize_nlp('en')
    ruler.add_patterns(liste)
    payload = request.get_json()
    result = get_entities(payload['text'], nlp)
#     text = 'Isaac Newton and Albert Einstein did great advances in the scientific word !'
    return jsonify(result)

if __name__ == '__main__':
    app.run(host="0.0.0.0")

