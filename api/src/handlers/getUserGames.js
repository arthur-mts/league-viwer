const dynamodb = require('aws-sdk/clients/dynamodb');
const fetch = require('node-fetch');
const docClient = new dynamodb.DocumentClient();
const { hash } = require('bcrypt');
const userTableName = process.env.USER_TABLE;
const gameTableName = process.env.GAME_TABLE;
const baseUrl = process.env.RIOTAPIBASEURL;
const apiKey = process.env.RIOTAPIKEY;

async function getLastGames(userId, limit = 5){
    const url = `${baseUrl}/match/v4/matchlists/by-account/${userId}?endIndex=${limit}&api_key=${apiKey}`;
    const response = await (await fetch(url)).json();
    console.log(url, response)
    if(response.status  && response.status.status_code >= 400)  return null ;
    return response.matches;
}

exports.getUserGamesHandler = async (event) => {
    if (event.httpMethod !== 'GET') {
        throw new Error(`Only accepts GET method, you tried: ${event.httpMethod} method.`);
    }

    const userId = event.pathParameters.id;


    const lastGames = await getLastGames(userId);
    
    const response = {
        statusCode: 200,
        body: JSON.stringify(lastGames),
        headers: JSON.stringify({'Content-Type': 'application/json'})
    };

    return response;
}