import facebook
import os

access_token = os.environ['FACEBOOK_ACCESS_TOKEN']
graph = facebook.GraphAPI(access_token=access_token, version='2.2')
friends = graph.get_connections(id='me', connection_name='friends')
print friends
