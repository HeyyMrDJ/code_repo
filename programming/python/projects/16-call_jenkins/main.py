'Simple program for calling jenkins jobs and passing in parameters'
import requests
from requests.auth import HTTPBasicAuth
import typer


URI = 'http://jenkins:8080/job/test_script/buildWithParameters?token=test'


def call_jenkins(user_name: str, api_key: str, script_user_name: str):
    'Function to make HTTP request to jenkins server'
    pay_load = {'my_name': script_user_name}
    basic = HTTPBasicAuth(user_name, api_key)

    dank = requests.get(URI, auth=basic, params=pay_load)

    return dank


def main(
    user_name: str,
    api_key: str,
    script_user_name: str = typer.Argument('World')
        ):

    'Main Function'
    response = call_jenkins(user_name, api_key, script_user_name)
    if response.status_code == 201:
        print("Successfully started job")
    else:
        print("Uknown error occured with job")


if __name__ == "__main__":
    typer.run(main)
