import json

def handler(event, context):
    print('request : {}'.format(json.dumps(event)))

    return{
        'statusCode' : 200,
        'headers' : {
            'Context-Type' : 'rext/plain'
        },
        'body':'hello! CDk! You have hit {}\n'.format(event['path'])

    }