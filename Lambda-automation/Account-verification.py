import json
import boto3
import random
import string
import psycopg2


ses = boto3.client('ses')


DB_HOST = 'banka-db-service'
DB_PORT = '5432'
DB_NAME = 'PostgreSQL'
DB_USER = 'banka_user'
DB_PASSWORD = 'banka_password'

def generate_verification_code(length=6):
    """Generate a random verification code."""
    return ''.join(random.choices(string.digits, k=length))

def lambda_handler(event, context):
    body = json.loads(event['body'])
    user_email = body['email']

    
    verification_code = generate_verification_code()

    try:
        # Connect to PostgreSQL database
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = conn.cursor()

        # Insert or update the verification code
        cursor.execute("""
            INSERT INTO users (email, verification_code)
            VALUES (%s, %s)
            ON CONFLICT (email)
            DO UPDATE SET verification_code = %s
        """, (user_email, verification_code, verification_code))

        
        conn.commit()

        
        email_subject = 'Account Verification Code'
        email_body = f"Your verification code is: {verification_code}"

        ses.send_email(
            Source='noreply@banka.com',  
            Destination={'ToAddresses': [user_email]},
            Message={'Subject': {'Data': email_subject}, 'Body': {'Text': {'Data': email_body}}}
        )

        
        cursor.close()
        conn.close()

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Verification email sent successfully'})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Failed to send verification email', 'error': str(e)})
        }
