import json
import boto3
 ### When you have transction send sms is it successful ##
def lambda_handler(event, context):
    sns = boto3.client('sns')
    body = json.loads(event['body'])
    user_phone_number = body['phoneNumber']
    transaction_amount = body['amount']
    transaction_type = body['type']

    message = f"Transaction Alert: {transaction_type} of ${transaction_amount} was made to your account."

    try:
        response = sns.publish(
            Message=message,
            PhoneNumber=user_phone_number
        )
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Transaction notification sent successfully!'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Failed to send transaction notification', 'error': str(e)})
        }
