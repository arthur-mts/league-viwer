const { verify } = require('jsonwebtoken');

exports.authorizationHandler = async function (event) {
    const token = event.authorizationToken;
    const methodArn = event.methodArn;
    try {
        const id = verify(token, process.env.JWTSECRET);
        console.log(id);
        return generateAuthResponse('user', 'Allow', methodArn, id);

    }
    catch(e){
        console.log(e);
        return generateAuthResponse('user', 'Deny', methodArn);
    }
}

function generateAuthResponse(principalId, effect, methodArn, id) {
    const policyDocument = generatePolicyDocument(effect, methodArn);
    const response = {
        principalId,
        policyDocument
    }
    if(id) {
        response.context = {userId: id};
    }
    return response;
}

function generatePolicyDocument(effect, methodArn) {
    if (!effect || !methodArn) return null

    const policyDocument = {
        Version: '2012-10-17',
        Statement: [{
            Action: 'execute-api:Invoke',
            Effect: effect,
            Resource: methodArn
        }]
    };
    console.log(policyDocument);
    return policyDocument;
} 