import requests


def get_response(url):
    """Send a GET request to the given URL and return the response object.

    Args:
        url (str): The URL to which the GET request should be sent.

    Returns:
        requests.Response: The response object returned by the requests.get call.

    Raises:
        requests.RequestException: An error occurred while making the GET request.
    """
    # Make a GET request to the provided URL.
    try:
        response = requests.get(url)
        # Ensure the response status code is 200 (OK).
        response.raise_for_status()
    except requests.RequestException as e:
        # Print the error and reraise if the request was unsuccessful.
        print(f"HTTP request failed: {e}")
        raise
    return response


def check_codegen(url="https://raeslab.org/webservices/codeGen/"):
    """Check if the CodeGen webservice is online by querying its status.

    Args:
        url (str): The URL of the CodeGen webservice to check. Defaults to raeslab's CodeGen service.

    Raises:
        ValueError: If the CodeGen service is not marked as 'online'.
    """
    # Obtain the response from the CodeGen webservice.
    response = get_response(url)

    # Extract JSON data from the response.
    data = response.json()
    # Raise an error if the status is not 'online'.
    if data['status'] != 'online':
        raise ValueError("CodeGen service is not online.")


def check_addressvalidation(url="https://raeslab.org/webservices/addressValidation/"):
    """Check if the AddressValidation webservice is accessible by making a GET request.

    Args:
        url (str): The URL of the AddressValidation webservice to check. Defaults to raeslab's service.
    """
    # Simply make a GET request to verify accessibility.
    get_response(url)


def check_medicalMS(url="https://raeslab.org/webservices/medicalMS/"):
    """Check if the MedicalMS webservice is accessible by making a GET request.

    Args:
        url (str): The URL of the MedicalMS webservice to check. Defaults to raeslab's service.
    """
    # Simply make a GET request to verify accessibility.
    get_response(url)


if __name__ == "__main__":
    # Check if the web services are operational by attempting to access them.
    check_codegen()
    check_addressvalidation()
    check_medicalMS()