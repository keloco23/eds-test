import os
import requests
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb',
                          endpoint_url='http://localhost:8000'
                          )

def get_usd(event, context):

    table_name = os.environ['USD_TABLE']
    table = dynamodb.Table(table_name)

    url = 'https://mindicador.cl/api/dolar'
    response = requests.get(url, timeout=120)
    data = response.json()
    usd_value = data['serie'][0]['valor']

    today_date = datetime.now().strftime('%Y-%m-%d--%H.%M.%S')
    table.put_item(
        Item={
            'date': today_date,
            'value': float(usd_value)
        }
    )

    return {
        'statusCode': 200,
        'body': f'Valor ingresado a DB. Valor: {usd_value}'
    }