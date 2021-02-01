import json
import datetime
import requests

def handler(event,context):
    # TO DO implement 
    print('request: {}'.format(json.dumps(event)))
    data = {
        'output': 'Hello from ' + event['Country'],
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(data)
    }