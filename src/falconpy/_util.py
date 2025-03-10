"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

_util - Internal utilities library

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>
"""
import base64
import functools
# pylint: disable=E0401  # Pylint might not have these in our path
import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning
from ._version import _TITLE, _VERSION
from ._result import Result
urllib3.disable_warnings(InsecureRequestWarning)

# Restrict requests to only allowed HTTP methods
_ALLOWED_METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'UPDATE']
# Default user-agent string
_USER_AGENT = f"{_TITLE}/{str(_VERSION)}"


def validate_payload(validator: dict, params: dict, required: list = None) -> bool:
    """
    Validates parameters and body payloads sent to the API.
    """
    # Repurposed with permission from https://github.com/yaleman/crowdstrike_api
    #                                          __
    #                                         ( (\
    #                                          \ =\
    #                                         __\_ `--\
    #                                        (____))(  \----
    #                                        (____)) _     Thanks
    #                                        (____))       James!
    #                                        (____))____/----
    if required:
        for key in required:
            if key not in params:
                raise ValueError(f"Argument {key} must be specified.")

    for key in params:
        if key not in validator:
            raise ValueError(f"{key} is not a valid argument.")
        if not isinstance(params[key], validator[key]):
            raise TypeError(f"{key} is not the valid type. Should be: {validator[key]}, was {type(params[key])}")

    return True


def parse_id_list(id_list) -> str:
    """
    Converts a list of IDs to a comma-delimited string.
    """
    if isinstance(id_list, list):
        returned = ""
        for string in id_list:
            if len(returned) > 1:
                returned += ","
            returned += str(string)
    else:
        returned = id_list

    return returned


def generate_b64cred(client_id: str, client_secret: str) -> str:
    """
    base64 encodes passed client_id and client_secret for authorization headers.
    """
    cred = "{}:{}".format(client_id, client_secret)
    b64_byt = base64.b64encode(cred.encode("ascii"))
    encoded = b64_byt.decode("ascii")

    return encoded


def force_default(defaults: list, default_types: list = None):
    """
    This function forces default values and is designed to decorate other functions.

    defaults = list of values to default
    default_types = list of types to default the values to

    Example: @force_default(defaults=["parameters], default_types=["dict"])
    """
    if not default_types:
        default_types = []

    def wrapper(func):
        """Inner wrapper."""

        @functools.wraps(func)
        def factory(*args, **kwargs):
            """
            This method is a factory and runs through arguments passed to the called function,
            setting defaults on values within the **kwargs dictionary when necessary
            as specified in our "defaults" list that is passed to the parent wrapper.
            """
            element_count = 0   # Tracker so we can retrieve matching data types
            # Loop through every element specified in our defaults list
            for element in defaults:
                if element in kwargs:
                    # It exists but it's a NoneType
                    if kwargs.get(element) is None:
                        kwargs[element] = get_default(default_types, element_count)
                else:
                    # Not present whatsoever
                    kwargs[element] = get_default(default_types, element_count)
                # Increment our tracker for our sibling default_types list
                element_count += 1
            return func(*args, **kwargs)
        return factory
    return wrapper


def service_request(caller: object = None, **kwargs) -> object:  # May return dict or object datatypes
    """
    Checks for token expiration, refreshing if possible and then performs the request.
    """
    if caller:
        try:
            if caller.auth_object:
                if caller.auth_object.token_expired():
                    auth_response = caller.auth_object.token()
                    if auth_response["status_code"] == 201:
                        caller.headers['Authorization'] = 'Bearer {}'.format(auth_response['body']['access_token'])
                    else:
                        caller.headers['Authorization'] = 'Bearer '
        except AttributeError:
            pass

        try:
            proxy = caller.proxy
        except AttributeError:
            proxy = None

        try:
            timeout = caller.timeout
        except AttributeError:
            timeout = None

    returned = perform_request(proxy=proxy, timeout=timeout, **kwargs)

    return returned


@force_default(defaults=["headers"], default_types=["dict"])
def perform_request(endpoint: str = "", headers: dict = None, **kwargs) -> object:  # May return dict or object datatypes
    """
    Leverages the requests library to perform the requested CrowdStrike OAuth2 API operation.

    method: str - HTTP method to use when communicating with the API
        - Example: GET, POST, PATCH, DELETE or UPDATE
    endpoint: str - API endpoint, do not include the URL base
        - Example: /oauth2/revoke
    headers: dict - HTTP headers to send to the API
        - Example: {"AdditionalHeader": "AdditionalValue"}
    params: dict - HTTP query string parameters to send to the API
        - Example: {"limit": 1, "sort": "state.asc"}
    body: dict - HTTP body payload to send to the API
        - Example: {"ids": "123456789abcdefg,987654321zyxwvutsr"}
    verify: bool - Enable / Disable SSL certificate checks
        - Example: True
    data - Encoded data to send to the API
        - Example: PAYLOAD = open(FILENAME, 'rb').read()
    files: list - List of files to upload
        - Example: [('file',('testfile2.jpg',open('testfile2.jpg','rb'),'image/jpeg'))]
    body_validator: dict - Dictionary containing payload to be validated for the requested operation (key / datatype)
        - Example: { "limit": int, "offset": int, "filter": str}
    body_required: list - List of payload parameters required by the requested operation
        - Example: ["ids"]
    proxy: dict - Dictionary containing a list of proxies to use for requests
        - Example: {"https": "https://myproxy.com:4000", "http": "http://myhttpproxy:80"}
    timeout: float or tuple
        Float representing the global timeout for requests or a tuple containing the connect / read timeouts.
        - Example: 30
        - Example: (5.05, 25)
    """
    method = kwargs.get("method", "GET")
    body = kwargs.get("body", None)
    body_validator = kwargs.get("body_validator", None)
    perform = True
    if method.upper() in _ALLOWED_METHODS:
        # Validate parameters
        # 05.21.21/JSH - Param validation is now handled by the updated args_to_params method

        # Validate body payload
        if body_validator:
            try:
                validate_payload(body_validator, body, kwargs.get("body_required", None))
            except ValueError as err:
                returned = generate_error_result(message=f"{str(err)}")
                perform = False
            except TypeError as err:
                returned = generate_error_result(message=f"{str(err)}")
                perform = False

        # Perform the request
        if perform:
            headers["User-Agent"] = _USER_AGENT  # Force all requests to pass the User-Agent identifier
            try:
                response = requests.request(method.upper(), endpoint, params=kwargs.get("params", None),
                                            headers=headers, json=kwargs.get("body", None), data=kwargs.get("data", None),
                                            files=kwargs.get("files", []), verify=kwargs.get("verify", True),
                                            proxies=kwargs.get("proxy", None), timeout=kwargs.get("timeout", None)
                                            )

                if response.headers.get('content-type') == "application/json":
                    returned = Result()(response.status_code, response.headers, response.json())
                else:
                    returned = response.content
            except Exception as err:  # pylint: disable=W0703  # General catch-all for anything coming out of requests
                returned = generate_error_result(message=f"{str(err)}")
    else:
        returned = generate_error_result(message="Invalid API operation specified.", code=405)

    return returned


def generate_error_result(message: str = "An error has occurred. Check your payloads and try again.", code: int = 500) -> dict:
    """
    Normalized error messaging handler.
    """
    return Result()(status_code=code, headers={}, body={"errors": [{"message": f"{message}"}], "resources": []})


def generate_ok_result(message: str = "Request returned with success", code: int = 200) -> dict:
    """
    Normalized OK messaging handler.
    """
    return Result()(status_code=code, headers={}, body={"message": message, "resources": []})


def get_default(types: list, position: int):
    """
    I determine the requested default data type and return it.
    """
    default_value_names = ["list", "str", "int", "dict", "bool"]
    default_value_types = [[], "", 0, {}, False]
    value_count = 0
    retval = {}  # Default to dictionary data type as that is our most often used
    for type_ in default_value_names:
        try:
            if type_ in types[position]:
                retval = default_value_types[value_count]
        except IndexError:
            # Data type not specified, fall back to dictionary
            pass
        value_count += 1

    return retval


def calc_url_from_args(target_url: str, passed_args: dict) -> str:
    """
    This function reviews arguments passed to the Uber class command method and updates the target URL accordingly.
    """
    if "ids" in passed_args:
        id_list = str(parse_id_list(passed_args['ids'])).replace(",", "&ids=")
        target_url = target_url.format(id_list)
    if "action_name" in passed_args:
        delim = "&" if "?" in target_url else "?"
        # Additional action_name restrictions?
        target_url = f"{target_url}{delim}action_name={str(passed_args['action_name'])}"
    if "partition" in passed_args:
        target_url = target_url.format(str(passed_args['partition']))
    if "file_name" in passed_args:
        delim = "&" if "?" in target_url else "?"
        target_url = f"{target_url}{delim}file_name={str(passed_args['file_name'])}"

    return target_url


def args_to_params(payload: dict, passed_arguments: dict, endpoints: list, epname: str) -> dict:
    """
    This function reviews arguments passed to the function against arguments accepted by the endpoint.
    If a valid argument is passed, it is added and returned as part of the payload dictionary.

    This function will convert passed comma-delimited strings to list data types when necessary.
    """
    for arg in passed_arguments:
        eps = [ep[5] for ep in endpoints if epname in ep[0]][0]
        try:
            argument = [param for param in eps if param["name"] == arg][0]
            if argument:
                arg_name = argument["name"]
                if argument["type"] == "array":
                    if isinstance(passed_arguments[arg_name], (str)):
                        passed_arguments[arg_name] = passed_arguments[arg_name].split(",")
                # More data type validation can go here
                payload[arg_name] = passed_arguments[arg_name]
        except IndexError:
            # Unrecognized argument
            pass

    return payload


def process_service_request(calling_object: object,
                            endpoints: list,
                            operation_id: str,
                            **kwargs
                            ):
    """
    Performs a request originating from a service class module.
    Calculates the target_url based upon the provided operation ID and endpoint list.

    PARAMETERS:
        endpoints: list - List of service class endpoints, defined as Endpoints in a service class. [required]
        operation_id: The name of the operation ID. Normally this is also the function name from the service class. [required]
        method: HTTP method to execute. GET, POST, PATCH, DELETE, PUT accepted. Defaults to GET.
        keywords: Dictionary of kwargs that were passed to the function within the service class.
        params: Dictionary of parameters passed to the service class function.
        headers: Dictionary of headers passed to and calculated by the service class function.
        body: Dictionary representing the body payload passed to the service class function.
        data: Dictionary representing the data payload passed to the service class function.
        files: List of files to be uploaded.
    """
    # ID replacement happening at the end of this statement planned for removal in v0.5.6+
    # (after all classes have been updated to no longer need it and it has been removed from the _endpoints module)
    target_url = f"{calling_object.base_url}{[ep[2] for ep in endpoints if operation_id in ep[0]][0]}".replace("?ids={}", "")
    # Retrieve our keyword arguments
    passed_keywords = kwargs.get("keywords", None)
    passed_params = kwargs.get("params", None)
    parameter_payload = None
    if passed_keywords or passed_params:
        parameter_payload = args_to_params(passed_params, passed_keywords, endpoints, operation_id)
    passed_headers = kwargs.get("headers", None) if kwargs.get("headers", None) else calling_object.headers
    new_keywords = {
        "caller": calling_object,
        "method": kwargs.get("method", "GET"),  # Default to GET.
        "endpoint": target_url,
        "verify": calling_object.ssl_verify,
        "headers": passed_headers,
        "params": parameter_payload,
        "body": kwargs.get("body", None),
        "data": kwargs.get("data", None),
        "files": kwargs.get("files", None)
    }

    return service_request(**new_keywords)
