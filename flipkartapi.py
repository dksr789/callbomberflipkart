import requests

# URL and headers
url = "https://2.rome.api.flipkart.com/api/7/user/otp/generate"
headers = {
    "Content-Type": "application/json",
    "Cookie": "T=clohebc7k3hvc0pe99yjxp1nq-BR1698942190736; SN=VI07F1AD64C9004EDA8E6B3D3BE7FFAC5D.TOK721B6B63FEB54130999E5C790A73D557.1698950564.LO; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImQ2Yjk5NDViLWZmYTEtNGD3C1B4C124C12FhNVCM91IZ2AK; s_cc=true; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; S=d1t16Jj8/PzMlTxhoPz9cLj9FQLCY6Z+oL2inhrIRYnAGn4/Kyxy+UubIi4LUblXSe/Ln+bN8IxQXEwYKrwVTAWOVmg==",
    "Origin": "https://www.flipkart.com",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0",
    "X-User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0 FKUA/website/42/website/Desktop",
    "Accept-Encoding": "gzip, deflate, br"
}

# Payload data
payload = {
    "loginId": "+918920512124"
}

try:
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        print("Request was successful.")
    else:
        print(f"Request failed with status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
    print(f"Response content: {response.content}")
