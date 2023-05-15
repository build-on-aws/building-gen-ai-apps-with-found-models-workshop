import json
import boto3

def parse_response(query_response):
    """Parse response and return generated image and the prompt"""

    response_dict = json.loads(query_response)
    return response_dict["generated_image"], response_dict["prompt"]


def lambda_handler(event, context):
    client = boto3.client("sagemaker-runtime")

    data_string = event["body"]
    text = json.loads(data_string)["text"]

    encoded_text = text.encode("utf-8")

    CONTENT_TYPE = "application/x-text"
    endpoint_name = "YOUR_MODEL_ENDPOINT"  # Replace with your model endpoint

    response = client.invoke_endpoint(
        EndpointName=endpoint_name, ContentType=CONTENT_TYPE, Body=encoded_text
    )

    print(response)

    response_payload = json.loads(response["Body"].read().decode("utf-8"))
    print(text)

    resp = json.dumps(response_payload)

    return {"statusCode": 200, "body": resp}
