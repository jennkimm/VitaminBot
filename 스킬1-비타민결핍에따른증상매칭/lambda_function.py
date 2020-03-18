import pandas as pd
import json
import ctypes

def lambda_handler(event, context):
    request_body = json.loads(event['body'])
    params = request_body['action']['params']
    ans = params['symptom']

    df = pd.read_csv('https://dsc-winter-nlp.s3.ap-northeast-2.amazonaws.com/vitamin22.csv', encoding='CP949')
    del df['Unnamed: 2']
    del df['Unnamed: 3']
    df = df.drop(96, 0)
    df = df.drop(97, 0)

    test=ans

    vit=[]
    for i in range(96):
        if (df.symtoms[i]==test):
            vit.append(df.vitamin[i])

    vitamin = ' ,'.join(vit)

    result = {
        "version": "2.0",
        "data":{
            "menu": ans,
            "vitamin": vitamin
        }
    }

    return {
        'statusCode':200,
        'body': json.dumps(result),
        'headers': {
            'Access-Control-Allow-Origin': '*',
        }
    }



