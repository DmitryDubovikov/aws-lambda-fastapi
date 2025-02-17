import json
from transformers import pipeline


def get_pipeline():
    print("Initializing pipeline...")
    return pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")


def lambda_handler(event, context):
    try:
        text = event['body']['text']
    except (KeyError, TypeError):
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'No text provided for sentiment analysis'})
        }

    if not text:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Empty text provided'})
        }

    nlp_pipeline = get_pipeline()
    result = nlp_pipeline(text)

    sentiment = result[0]['label']
    score = result[0]['score']

    sentiment_label = 'Positive' if sentiment == 'POSITIVE' else 'Negative'

    response = {
        'statusCode': 200,
        'body': json.dumps({
            'sentiment': sentiment_label,
            'score': score,
            'analyzed_text': text[:50]
        })
    }

    return response