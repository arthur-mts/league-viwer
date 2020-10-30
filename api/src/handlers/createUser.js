const dynamodb = require('aws-sdk/clients/dynamodb');
const fetch = require('node-fetch');
const docClient = new dynamodb.DocumentClient();
const { hash } = require('bcrypt');
const { sign, verify } = require('jsonwebtoken');

const tableName = process.env.SAMPLE_TABLE;

const noParamsErrorResponse = { statusCode: 400, body: {message: 'name, email and password required'}};

const summonerNotFountResponse = { statusCode: 404, body: {message: 'sumoner not found'}};

const summonerAleredySaved = { statusCode: 400, body: {message: 'sumoner ja esta cadastrado'}};
exports.createUserHandler = async (event) => {
    if (event.httpMethod !== 'POST') {
        throw new Error(`postMethod only accepts POST method, you tried: ${event.httpMethod} method.`);
    }

    if(!event.body) return noParamsErrorResponse;

    const body = JSON.parse(event.body)
    

    const {nickname, email, password } = body;

    if(! nickname && email && password) return noParamsErrorResponse;

    const userInfo = await getPlayerData(nickname);

    if(!userInfo) return JSON.stringify(summonerNotFountResponse);

    const {id, name, puuid, summonerLevel, accountId} = userInfo;

    var params = {
        TableName : tableName,
        Key: {
            id
        }
    };

    const { Item } = await docClient.get(params).promise();
    
    if(Item) return JSON.stringify(summonerAleredySaved);

    const hashedPassword = await hash(password, 8);

    params = {
        TableName : tableName,
        Item: { email, id, name, puuid, accountId, summonerLevel, password: hashedPassword }
    };

    await docClient.put(params).promise();

    const token = sign(id, process.env.JWTSECRET);

    console.log(verify(token, process.env.JWTSECRET))
    const responseBody = {token};

    const response = {
        statusCode: 200,
        body: JSON.stringify(responseBody),
        headers: JSON.stringify({'Content-Type': 'application/json'})
    };

    return response;
}


async function getPlayerData(nickname){
    const url = `${process.env.RIOTAPIBASEURL}/summoner/v4/summoners/by-name/${nickname}?api_key=${process.env.RIOTAPIKEY}`
    const response = await (await fetch(url)).json();
    console.log(url, response);
    if(response.status  && response.status.status_code >= 400)  return null ;
    return response;
}
