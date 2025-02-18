# Sentiment Analysis API

A simple sentiment analysis system using FastAPI and a custom AWS Lambda function.

## Setup

```shell
docker compose build

docker compose up -d
```

## API Endpoints

1. **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)  
   Explore and test the API interactively.


2. **Analyze Sentiment**: [http://localhost:8000/analyze/](http://localhost:8000/analyze/)  
   Send a POST request with text to analyze its sentiment.

### Example Requests

#### Negative Text
```
This product is a complete disaster! Poor quality, terrible service, and a waste of money. Never buying again. Horrible experience!
```

#### Positive Text
```
This is absolutely amazing! Incredible quality, fantastic service, and worth every penny. Highly recommend it! Truly a wonderful experience!"
```