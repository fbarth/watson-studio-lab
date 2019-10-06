import json
from ibm_watson import NaturalLanguageClassifierV1

natural_language_classifier = NaturalLanguageClassifierV1(
    username='6d7b6e37-f9a1-48f8-9573-88993dd9c98b',
    password='wP4E1FYUwztK'
)

classes = natural_language_classifier.classify(
    '948e81x625-nlc-35', 
    'história muito legal sobre a cerveja').get_result()
print(classes['top_class'])

import pandas as pd
test = pd.read_csv('data/test_cerveja.csv', header=None)