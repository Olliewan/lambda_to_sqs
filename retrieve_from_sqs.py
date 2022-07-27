import json
from json import JSONDecodeError
import boto3
import os
import datetime

def lambda_handler(event, context):
    start = datetime.datetime.now()
    sqs = boto3.client('sqs')
    queue_url = os.environ['QUEUE_URL']
    retrieve_rounds = int(os.environ['RETRIEVE_ROUNDS'])
    for i in range(retrieve_rounds):
        print(get_time(start), f'Start retrieving message from queue for round {i}')
        response = retrieve_message(queue_url, sqs)
        try:
            message_count = len(response['Messages'])
            print(get_time(start), f'{message_count} messages from current round')
            for message in response['Messages']:
                receipt_handle = message['ReceiptHandle']
                try:
                    msg = json.loads(message['Body'])
                    # transfer json file to a dic file in Python and do ETL operations 
                    print(msg)
                    print(get_time(start), f'Delete message from queue \nReceiptHandle: {receipt_handle}')
                    delete_message(queue_url, sqs, receipt_handle)
                except JSONDecodeError:
                    print(get_time(start), 'Message body cannot be decoded\n' + message['Body'])
                    print(get_time(start), f'Delete message from queue \nReceiptHandle: {receipt_handle}')
                    delete_message(queue_url, sqs, receipt_handle)
                    pass
        except KeyError:
            print(get_time(start), 'No more message in the queue')
    

def get_time(start):
    return datetime.datetime.now() - start

def retrieve_message(url, client):
    response = client.receive_message(
        QueueUrl = url,
        AttributeNames = ['SentTimeStamp'],
        MaxNumberOfMessages = 10,
        MessageAttributeNames = ['All'],
        VisibilityTimeout = 30,
        WaitTimeSeconds = 5
    )
    return response
    
def delete_message(url, client, handle):
    client.delete_message(
        QueueUrl = url,
        ReceiptHandle = handle
    )