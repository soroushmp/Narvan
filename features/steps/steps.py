import requests
from behave import given, when, then

# Base URL for the API
BASE_URL = "http://localhost:8000"

# Variables to store request data and response
contact_data = {}
response_data = {}


@given(
    'I have a new contact with first name "{first_name}", last name "{last_name}", and phone number "{phone_number}"')
def create_contact_data(context, first_name, last_name, phone_number):
    context.contact_data = {
        "first_name": first_name,
        "last_name": last_name,
        "phone_number": phone_number
    }


@when('I make a POST request to "{endpoint}" endpoint')
def make_post_request(context, endpoint):
    response = requests.post(BASE_URL + endpoint, json=context.contact_data)
    context.response_data = {
        "status_code": response.status_code,
        "content": response.json()
    }


@then('I should receive a response with status code {status_code}')
def verify_status_code(context, status_code):
    assert context.response_data["status_code"] == int(status_code)


@then('the response should contain the created contact details')
def verify_created_contact_details(context):
    assert context.response_data["content"]["first_name"] == context.contact_data["first_name"]
    assert context.response_data["content"]["last_name"] == context.contact_data["last_name"]
    assert context.response_data["content"]["phone_number"] == context.contact_data["phone_number"]


@given('there are existing contacts in the database')
def existing_contacts_in_database(context):
    # Assuming there are already contacts in the database
    pass


@when('I make a GET request to "{endpoint}" endpoint')
def make_get_request(context, endpoint):
    response = requests.get(BASE_URL + endpoint)
    context.response_data = {
        "status_code": response.status_code,
        "content": response.json()
    }


@then('the response should contain a list of all contacts')
def verify_all_contacts(context):
    assert context.response_data["status_code"] == 200
    assert isinstance(context.response_data["content"], list)


@given('there is an existing contact with ID {contact_id} in the database')
def existing_contact_with_id(context, contact_id):
    response = requests.get(BASE_URL + f'/contacts/{contact_id}')
    context.contact_data = {
        "first_name": response.json()['first_name'],
        "last_name": response.json()['last_name'],
        "phone_number": response.json()['phone_number']
    }


@then('the response should contain details of the contact with ID {contact_id}')
def verify_contact_details(context, contact_id):
    assert context.response_data["status_code"] == 200
    assert context.response_data["content"]["id"] == int(contact_id)


@given('I want to update the contact with new phone number "{phone_number}"')
def update_contact_data(context, phone_number):
    context.contact_data["phone_number"] = phone_number


@when('I make a PUT request to "{endpoint}" endpoint')
def make_put_request(context, endpoint):
    response = requests.put(BASE_URL + endpoint, json=context.contact_data)
    context.response_data = {
        "status_code": response.status_code,
        "content": response.json()
    }


@then('the response should contain updated details of the contact with ID {contact_id}')
def verify_updated_contact_details(context, contact_id):
    assert context.response_data["status_code"] == 200
    assert context.response_data["content"]["id"] == int(contact_id)
    assert context.response_data["content"]["phone_number"] == context.contact_data["phone_number"]


@when('I make a DELETE request to "{endpoint}" endpoint')
def make_delete_request(context, endpoint):
    response = requests.delete(BASE_URL + endpoint)
    context.response_data = {
        "status_code": response.status_code
    }


@then('the contact with ID {contact_id} should be removed from the database')
def verify_contact_removed(context, contact_id):
    assert context.response_data["status_code"] == 204
