from pymongo import MongoClient
from elasticsearch import Elasticsearch
from progress.spinner import Spinner
from bson.json_util import dumps
import json


class MongoElastic:
    def __init__(self, args):

        # mongo db connection
        self.mongo_host = args.get('mongo_host', 'localhost')
        self.mongo_port = args.get('mongo_port', None)
        self.mongo_max_pool_size = args.get('mongo_max_pool_size', 50)
        self.mongo_db_name = args.get('mongo_db_name', None)
        self.mongo_document_name = args.get('mongo_document_name', None)

        # elasticsearch connection
        self.es = args.get('es_connection', None)
        self.es_index_name = args.get('es_index_name', 'test_index')
        self.es_doc_type = args.get('es_doc_type', 'test_doc_type')

    def start(self, m_filter=None):
        m_filter = dict() if not m_filter else m_filter
        client = MongoClient(self.mongo_host, self.mongo_port, maxPoolSize=self.mongo_max_pool_size)
        db = client[self.mongo_db_name]
        document_name = db[self.mongo_document_name]

        mongo_where = m_filter.get('mongo_condition', {})
        # get all data from mongoDB db
        m_data = document_name.find(mongo_where)
        if not self.es:
            es = Elasticsearch(
                ['localhost'],
                use_ssl=False,
            )
        i = 1
        spinner = Spinner('')
        for line in m_data:
            docket_content = line
            # remove _id from mongo object
            del docket_content['_id']
            try:
                self.es.index(index=self.es_index_name, doc_type=self.es_doc_type,id=i, body=docket_content)
            except Exception as error:
                print("Error for ", error)
            i += 1
            spinner.next()
        l = MongoElastic.display_search(self.es_index_name, self.es)
        print(l)
        # res = self.es.search(index="idx",doc_type="idx",body={})
        # hit_list = res['hits']['hits']
        # print(hit_list)
        client.close()
        return True

    @staticmethod
    def display_search(index_,es):  
        # Run a search for all existing words
        res = es.search(index=index_, doc_type=index_, body={})
        print(res)
        # Pull the word object from each hit in the search results
        hit_list = (res['hits']['hits'])

        # List word objects, appending the contents from the search hit's _source field.
        words_list = []
        for hit in hit_list:
            words_list.append(hit['_source'])

        # JSON-ify the list of words.
        return json.dumps(words_list)

es_connection_object = Elasticsearch(['localhost'],use_ssl=False)

config = {
    'mongo_host': 'localhost',
    'mongo_port': 27017,
    'mongo_db_name': 'NLP_project',
    'mongo_document_name': 'Article',
    'es_connection': es_connection_object,
    'es_index_name':'idx',
    'es_doc_type':'idx'
}

k= MongoElastic(config)
# m_filter = {'mongo_condition':{"field1" : "name1"}}
k.start()