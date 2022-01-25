from pip._vendor import requests
from behave import *
from data.userPayload import *
from utilities.resources import *
from utilities.configurations import *



@given('the User details which needs to be added')
def step_impl(context):
   
    context.url = get_config()['API']['endpoint'] + UserApiResources.add_user
    context.headers = {"Content-Type": "application/json"}
    context.payload = add_user_payload()


@when('we execute the Create User PostAPI method')
def step_impl(context):
    context.response = requests.post(context.url, json=context.payload , headers=context.headers)


@then('user is successfully added')
def step_impl(context):
    response_json = context.response.json()
    assert context.payload == response_json # Validate input payload is same as response body
    assert context.response.status_code == 200 # Validate Success Status Code




@given('the User details input array which needs to be added')
def step_impl(context):
   
    context.url = get_config()['API']['endpoint'] + UserApiResources.add_user_with_list
    context.headers = {"Content-Type": "application/json"}
    context.payload = add_user_list_payload()


@when('we execute the Create list of Users PostAPI method')
def step_impl(context):
    context.response = requests.post(context.url, json=context.payload , headers=context.headers)


@then('users are successfully added')
def step_impl(context):
    print(context.response.json())
    response_json = context.response.json()
    assert context.payload == response_json # Validate input payload is same as response body
   


@given('the username and password for login')
def step_impl(context):
    context.url = get_config()['API']['endpoint'] + UserApiResources.user_login
    auth = {}
    auth["username"] = add_user_payload()['username']
    auth["password"] = add_user_payload()['password']
    context.params = auth


@when('user log-in to the system')
def step_impl(context):
    context.response = requests.get(context.url,params=context.params)

@then('users is successfully logged-in')
def step_impl(context):
    assert "Logged in" in context.response.text # Validate Logged In Message in Response 


@when('user logged out of the system')
def step_impl(context):
    context.url = get_config()['API']['endpoint'] + UserApiResources.user_logout
    context.response = requests.get(context.url)

@then('users is successfully logged-out')
def step_impl(context):
    print(context.response.text)
    assert "User logged out" in context.response.text # Validate Log Out Message in Response
    





@given('the username for details to be fetched')
def step_impl(context):
    context.url = get_config()['API']['endpoint'] + UserApiResources.add_user + "/" + add_user_payload()['username']


@when('user details are fetched')
def step_impl(context):
    context.response = requests.get(context.url)

@then('users details matches')
def step_impl(context):
    assert context.response.json() == add_user_payload() # Validate Response body is same as Input Payload
    

@given('the username for details to be updated')
def step_impl(context):
    context.url = get_config()['API']['endpoint'] + UserApiResources.add_user + "/" + add_user_payload()['username']
    context.payload = updated_user_payload()
    context.headers = {"Content-Type": "application/json"}
@when('details are updated and sent')
def step_impl(context):
     context.response = requests.put(context.url,json=context.payload,headers= context.headers)
    
@then('details are updated successfully')
def step_impl(context):
    assert context.response.json() == updated_user_payload() # Validate Response body is same as Input Payload
    
    

@given('the username needed to be removed')
def step_impl(context):
    context.url = get_config()['API']['endpoint'] + UserApiResources.add_user + "/" + add_user_payload()['username']

@when('remove operation is performed')
def step_impl(context):
   context.response = requests.delete(context.url)
    

@then('details are removed successfully')
def step_impl(context):
    assert context.response.status_code == 200 # Validate Success Status Code
