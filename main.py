from elasticsearch import Elasticsearch

es = Elasticsearch(["http://localhost:9200"], http_auth=('username', 'password'))

indices = es.cat.indices(format="json")
for index in indices:
    index_name = index['index']
    es.indices.delete(index=index_name)
