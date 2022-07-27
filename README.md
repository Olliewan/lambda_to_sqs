# Send data to SQS from lambda and comsume the messages by lambda

Architecture for the process
![image](https://user-images.githubusercontent.com/97939971/181184224-80908891-462f-446d-9bb5-c4aa64a5ef3e.png)

# Settings for lambda sent_to_sqs
1. Change lambda timeout to 10 seconds
2. Give lambda role the permission to send message to SQS
3. Set QUEUE_URL in Environment variables

# Settings for lambda retrieve_from_sqs
1. Change lambda timeout to 60 seconds
2. Give lambda role the permission to retrieve and delete message to SQS
3. Set QUEUE_URL, RETRIEVE_ROUNDS in Environment variables

![image](https://user-images.githubusercontent.com/97939971/181188852-c8357724-8a94-4cb4-8345-23dae05df0d1.png)

# Create a standarf SQS 
