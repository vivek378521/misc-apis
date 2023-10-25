## Currently deployed at
`https://misc-apis.vercel.app/docs`

# IP Address Conversion API

This FastAPI project provides two endpoints for converting IP addresses to numeric representations and vice versa. You can use these endpoints to convert IP addresses to numeric values or convert numeric values back to IP addresses.

## Endpoints

### Convert IP Address to Number

- **HTTP Method**: GET
- **Endpoint**: `/convert_ip_to_number/`
- **Request Format**: None (Client's IP address is automatically used)
- **Response Format**:
  - `ip_address`: The client's IP address in the dotted-decimal format.
  - `ip_as_number`: The numeric representation of the IP address.

**Usage**:

- Make a GET request to `/convert_ip_to_number/`.
- The API will automatically use the client's IP address to convert it to a numeric representation.

### Convert Number to IP Address

- **HTTP Method**: POST
- **Endpoint**: `/convert_number_to_ip/`
- **Request Format**:
  - `ip_as_number`: The numeric representation of the IP address to convert.
- **Response Format**:
  - `ip_address`: The converted IP address in the dotted-decimal format.
  - `ip_as_number`: The provided numeric representation.

**Usage**:

- Make a POST request to `/convert_number_to_ip/`.
- Include the `ip_as_number` field in the request's JSON body to specify the numeric representation to convert.
- The API will convert the numeric value to an IP address.

## Error Handling

- The API handles errors such as invalid IP addresses and out-of-range numeric values, returning appropriate error responses.

## Running the API

- To run the API, execute the following command:

```shell
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python main.py
```

