import os
import requests
from fpdf import FPDF
import boto3
import logging
from datetime import datetime

#logs
logging.basicConfig(level=logging.INFO)

def get_uf(event, context):
    logging.info("Inicio de la función Lambda.")
    
    # API url
    uf_url = 'https://mindicador.cl/api/uf'
    try:
        response = requests.get(uf_url, timeout=120) 
        logging.info("Solicitud a mindicador exitosa.")
    except requests.exceptions.Timeout:
        logging.error("Timeout al conectar con mindicador.cl")
        return {
            'statusCode': 500,
            'body': 'Error: Timeout al conectar con la API de mindicador'
        }

    uf = response.json()
    uf_value = uf['serie'][0]['valor']
    
    #PDF
    logging.info(f"Valor de la UF recibido: {uf_value}")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"El valor de la UF es: {uf_value}", ln=True, align='C')
    
    timestamp = datetime.now().strftime("%Y-%m-%d-%H.%M.%S")
    pdf_filename = f"./s3-storage/uf_{timestamp}.pdf" 
    pdf.output(pdf_filename)
    logging.info(f"Archivo PDF generado en {pdf_filename}")
    
    # SESSION S3 WITH BOTO3
    session = boto3.Session(
        aws_access_key_id='S3RVER',
        aws_secret_access_key='S3RVER'
    )

    # S3 LOCAL
    s3 = session.client(
        's3',
        endpoint_url=os.getenv('S3_ENDPOINT_URL', 'http://localhost:8001')
    )
    
    # BUCKET
    bucket_name = os.getenv('S3_BUCKET', 'local-bucket')
    
    try:
        logging.info("Intentando subir archivo a S3 local.")
        s3.upload_file(pdf_filename, bucket_name, f'uf_{timestamp}.pdf')
        logging.info("Archivo subido con éxito a S3 local.")
    except Exception as e:
        logging.error(f"Error al subir el archivo a S3: {e}")
        return {
            'statusCode': 500,
            'body': 'Error al subir el archivo a S3 local'
        }

    return {
        'statusCode': 200,
        'body': f'PDF generado y valor de la UF: {uf_value}'
    }
