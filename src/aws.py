import boto3
from botocore.exceptions import ClientError
import json


def get_ms_api_key():
    """
    Retrieve the api key for the ML microservices from SecretsManager.
    """
    secret_name = "perception/ms-api-key"
    region_name = "us-west-1"

    # Create a Secrets Manager client
    session = boto3.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        return None

    secret = json.loads(response["SecretString"])["MICROSERVICES_API_KEY"]
    return secret
