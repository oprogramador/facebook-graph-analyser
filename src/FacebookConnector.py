import facebook
import os

def getFriends(id):
    access_token = os.environ['FACEBOOK_ACCESS_TOKEN']
    graph = facebook.GraphAPI(access_token=access_token, version='2.2')
    friends = graph.get_connections(id=id, connection_name='friends')

    return map(lambda item: item['id'], friends['data'])
