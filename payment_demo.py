from instamojo_wrapper import Instamojo

API_KEY="INSTAMOJO_API_KEY"   #TEST
AUTH_TOKEN="=INSTAMOJO_AUTH_TOKEN" # TEST
api = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/')

response = api.payment_request_create(
    amount='11',
    purpose='Testing',
    send_email=True,
    email="subodhthore317@gmail.com",
    redirect_url="http://localhost:8000/handle_redirects"
    )
# print the long URL of the payment request.
print(response['payment_request']['longurl']) #
