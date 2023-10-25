from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def hello_world():
    return {"message": "Welcome to my APIs, go to docs"}


@app.get("/convert_ip_to_number/", response_model=None)
def convert_ip_to_number(request: Request):
    try:
        client_ip = request.client.host
        octets = client_ip.split(".")  # Split the address into octets
        if len(octets) != 4:
            return HTTPException(
                detail="Invalid IPv4 address", status_code=400
            )

        decimal_values = [
            int(octet) for octet in octets
        ]  # Convert octets to integers
        decimal_representation = (
            (decimal_values[0] << 24)
            | (decimal_values[1] << 16)
            | (decimal_values[2] << 8)
            | decimal_values[3]
        )
        return {
            "ip_address": client_ip,
            "ip_as_number": decimal_representation,
        }
    except Exception as e:
        return HTTPException(detail=str(e), status_code=400)


class IPConversionRequest(BaseModel):
    ip_as_number: int


class NumberConversionResponse(BaseModel):
    ip_address: str
    ip_as_number: int


@app.post("/convert_number_to_ip/", response_model=NumberConversionResponse)
def convert_number_to_ip(data: IPConversionRequest):
    try:
        ip_as_number = data.ip_as_number

        if (
            not 0 <= ip_as_number <= 0xFFFFFFFF
        ):  # Check if the number is within the valid range for an IPv4 address
            raise ValueError("Invalid numerical value")

        # Extract the four octets using bit masking and right shifts
        octet1 = (ip_as_number >> 24) & 0xFF
        octet2 = (ip_as_number >> 16) & 0xFF
        octet3 = (ip_as_number >> 8) & 0xFF
        octet4 = ip_as_number & 0xFF

        # Create the IPv4 address string by joining the octets with periods
        ip_address = f"{octet1}.{octet2}.{octet3}.{octet4}"

        return {"ip_address": ip_address, "ip_as_number": data.ip_as_number}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
