from pip._vendor import requests
from utilities.resources import *
from utilities.configurations import *

def after_scenario(context, scenario):
    if "remove_users" in scenario.tags:
        for item in context.response.json():
            print(item)
            url = get_config()['API']['endpoint'] + UserApiResources.add_user + "/" + item['username']
            response_delete_user = requests.delete(url)
            assert response_delete_user.status_code == 200

