import json
import boto3

def lambda_handler(event, context):
    client = boto3.client("sagemaker-runtime")

    data_string = event["body"]
    text = json.loads(data_string)["text"]

    query = "write a summary"

    prompt = f"{text}\n{query}"

    MAX_LENGTH = 150  # 256
    NUM_RETURN_SEQUENCES = 1
    TOP_K = 0
    TOP_P = 0.7
    DO_SAMPLE = True
    CONTENT_TYPE = "application/json"

    payload = {
        "text_inputs": prompt,
        "max_length": MAX_LENGTH,
        "num_return_sequences": NUM_RETURN_SEQUENCES,
        "top_k": TOP_K,
        "top_p": TOP_P,
        "do_sample": DO_SAMPLE,
    }

    payload = json.dumps(payload).encode("utf-8")

    endpoint_name = "YOUR_MODEL_ENDPOINT"  # Replace with your model endpoint

    response = client.invoke_endpoint(
        EndpointName=endpoint_name, ContentType=CONTENT_TYPE, Body=payload
    )
    model_predictions = json.loads(response["Body"].read())
    generated_text = model_predictions[0]["generated_text"]
    print(f"Response: {generated_text}")

    resp = json.dumps({"text": generated_text})

    return {"statusCode": 200, "body": resp}
