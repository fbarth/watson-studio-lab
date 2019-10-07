import json
from ibm_watson import NaturalLanguageClassifierV1

natural_language_classifier = NaturalLanguageClassifierV1(
    iam_apikey='{iam-apikey}',
    url='https://gateway.watsonplatform.net/natural-language-classifier/api')

classes = natural_language_classifier.classify(
    '94904ex626-nlc-66', 
    'história muito legal sobre a cerveja').get_result()
print(classes['top_class'])

