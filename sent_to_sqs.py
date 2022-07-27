import json
import boto3
import os

def lambda_handler(event, context):
    sqs = boto3.client('sqs')
    queue_url = os.environ['QUEUE_URL']
    response = send_message(queue_url, sqs, event)
    print(response)

def send_message(url, client, message):
    response = client.send_message(
        QueueUrl = url,
        MessageBody = json.dumps(message)
    )
    return response
