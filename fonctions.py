#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import spacy
from spacy.tokens import Span


def ouvrir_json(chemin):
    f = open(chemin , encoding="utf−8")
    toto = json.load(f)
    f.close()
    return toto

def ecrire_fichier(chemin , contenu):
    w = open(chemin , "w", encoding="utf−8")
    w.write(contenu)
    w.close()

def initialize_nlp(language):
    nlp = spacy.blank(language)
    nlp.add_pipe('parser')
    ruler = nlp.add_pipe('entity_ruler')
    nlp.initialize()
    return ruler, nlp

def get_names_list(chaine):
    if '-' in chaine:
        l = chaine.replace("-", " ")
        c = l.split(' ')
    elif ',' in chaine:
        l = chaine.replace(',', '')
        c = l.split(' ')
    elif '\xa0' in chaine:
        l = chaine.replace('\xa0', ' ')
        c = l.split(' ')
    else:
        c = chaine.split(' ')
    return c

def get_pattern(entity_names, type_ent, id_ent):
    pattern_final = {}
    pattern_final['label'] = type_ent  
    pattern_entity = []
    for x in entity_names:      
        if x != entity_names[-1] and len(entity_names)>1:
            nom = x.lower()
            a = {'LOWER': nom}
            op = {"IS_PUNCT":True, "OP":"?"}
            pattern_entity.append(a)
            pattern_entity.append(op)
        else:
            nom = x.lower()
            a = {'LOWER': nom}
            pattern_entity.append(a)
    
    pattern_final['pattern'] = pattern_entity
    
    id_pattern = '%s_%s'%(entity_names[-1].upper(), id_ent)
    pattern_final['id'] = id_pattern
    return pattern_final

def get_entities(text, nlp):
    doc = nlp(text)
    result = []
    for ent in doc.ents:
        span = Span(doc, ent.start, ent.end)
    print('Les entités suivantes ont été trouvées :\n')
    for ent in doc.ents:
        span = Span(doc, ent.start, ent.end)
        print(ent.text, '\n')
        print("Entite de type : ", ent.label_)
        print("Elle se trouve entre les tokens : ", span.start_char, " et ", span.end_char)
        print('Cette entité correspond au pattern : ', ent.ent_id_, '\n')
        result.append({'value': ent.text, 'type': ent.label_, 'start': span.start_char, 'end': span.end_char, 'pattern': ent.ent_id_})
    return result

