from pip._vendor import requests
from behave import *
from data.storeOrderPayload import *
from utilities.resources import *
from utilities.configurations import *


@when('we execute the get inventory API method')
def step_impl(context):
    context.url = get_config()['API']['endpoint'] + StoreApiResources.get_inventory
    context.response = requests.get(context.url)


@then('inventory details are returned')
def step_impl(context):
    response_json = context.response.json()
    print(response_json)
    
@then('status code of response should be 200')
def step_impl(context):
    assert context.response.status_code == 200 # Validate Success Status Code


@given('the details of Pet to be Ordered')
def step_impl(context):
    context.url = get_config()['API']['endpoint'] + StoreApiResources.post_order
    context.headers = {"Content-Type": "application/json"}
    context.payload = pet_order_payload()


@when('we execute the Order API method')
def step_impl(context):
    context.response = requests.post(context.url, json=context.payload , headers=context.headers)


@then('order details are returned')
def step_impl(context):
    response_json = context.response.json()
    assert context.payload["id"] == response_json["id"]
    assert context.payload["petId"] == response_json["petId"]
    

@given('the ID of order that needs to be fetched')
def step_impl(context):
    context.url = get_config()['API']['endpoint'] + StoreApiResources.post_order + "/" + str(pet_order_payload()['id'])
    context.payload = pet_order_payload()

@when('we execute get Order by ID Method')
def step_impl(context):
    context.response = requests.get(context.url)


@then('order details are successfully retrieved')
def step_impl(context):
    response_json = context.response.json()
    assert context.payload["id"] == response_json["id"]
    assert context.payload["petId"] == response_json["petId"]
    


@given('the ID of order that needs to be deleted')
def step_impl(context):
    context.url = get_config()['API']['endpoint'] + StoreApiResources.post_order + "/" + str(pet_order_payload()['id'])
    

@when('we execute Delete Order by ID Method')
def step_impl(context):
   context.response = requests.delete(context.url)
    

@then('order details are successfully deleted')
def step_impl(context):
    assert context.response.status_code == 200 # Validate Success Status Code
