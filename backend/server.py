from flask import Flask, render_template, request
from machineLearningModels.fakeNewsPredector import fake_news_det
from machineLearningModels.sentimentAnalysis import sentimentAnalysis

from flask_cors import CORS

from flask_pymongo import PyMongo
from flask_mongoengine import MongoEngine
import graphene
from graphene_mongo import MongoengineObjectType
from graphene.relay import Node
from flask_graphql import GraphQLView
from mongoengine import connect
from flask_graphql_auth import (
    AuthInfoField,
    GraphQLAuth,
    get_jwt_identity,
    create_access_token,
    create_refresh_token,
    query_header_jwt_required,
    mutation_jwt_refresh_token_required,
    mutation_jwt_required
)

from schema import schema

app = Flask(__name__)
CORS(app)
connect("fake_news", host="mongodb://localhost/fake_news", alias="default")


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        a = request.get_json()
        pred = fake_news_det(str(a['message']))
        return str(pred)
    else:
        return "Ops!! il y un erreur [predict() method]"

@app.route('/sentiment', methods=['POST'])
def predict2():
    if request.method == 'POST':
        a = request.get_json()
        pred = sentimentAnalysis(str(a['sntmnt']))
        return str(pred)

    else:
        return "Ops!! il y un erreur [predict() method]"

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(  
        'graphql',
        schema=schema,
        graphiql=True
    )
)

if __name__ == '__main__':
    app.run(debug=True)