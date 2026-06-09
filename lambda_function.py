from game import battle

def lambda_handler(event, context):

    result = battle()

    return {
        "statusCode": 200,
        "body": result
    }