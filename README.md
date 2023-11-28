# Webservices Health Check

This repository contains a Python script designed to check the operational status of various webservices. The script makes HTTP GET requests to predefined service endpoints and evaluates whether each service is online and functioning as expected.

## Description

The script provided in this repository focuses on checking the following services:

- **CodeGen**: A webservice that requires validation of its operational status to ensure it is marked as 'online'.
- **AddressValidation**: A simple webservice for address validation that the script checks for accessibility.
- **MedicalMS**: A webservice related to medical management systems, also checked for accessibility.

The health check is performed by sending GET requests to these services' URLs and evaluating their response. If the response status code is not 200 (indicating HTTP success), or if the expected JSON response for a service's operational status does not indicate the service is 'online', an error is raised and logged.

## Workflow Integration

This script is designed to be part of a GitHub Actions workflow that runs on a daily schedule. The workflow ensures that any prolonged outage of the monitored webservices is promptly detected and reported, as services should not be down for more than a day without notice.

## Usage

To use the script:

1. Make sure you have Python installed on your system.
2. Install the `requests` library, which can be done using `pip`:

```commandline
pip install -r requirements.txt
```

3. Run the script manually using the Python interpreter:

```commandline
python test_webservices.py
```

Alternatively, the provided GitHub Actions workflow will execute the script on a daily basis when set up in a GitHub repository.

## Contributing

Feel free to fork the repository, submit pull requests, or report any issues you encounter while using this health check script.