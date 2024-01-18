# Payze Implementation

Support Group - https://t.me/+Ng1axYLNyBAyYTRi  <br>
This MVP project helps for implementing <a href="https://docs.payze.io/reference/getting-started">payze-doc</a>.

### API Endpoints <br>

- `/v1/accept/` Accept Card Token And Transaction Values from Front Side
- `/v1/success/` Call Back Success Endpoint
- `/v1/order/` Create a New Order with Specific Card ID
- `/v1/pay/` Pay the Order

- `/swagger/` Swagger for Testing Api Methods
- `/admin/` The Admin Panel for Managing Data

# Installation
* 1 - clone repo 
   - ```git clone https://github.com/Muhammadali-Akbarov/payze-sample```
* 2 - create a virtual environment and activate
  - ```pip3 install virtualenv```
  - ```virtualenv venv```
  - ```venv\Scripts\activate```(windows) or ```source venv/bin/activate```(unix-based systems)
* 3 - cd into project "cd payze-sample"
* 4 - Install dependencies
  - ```pip3 install -r requirements.txt```
* 5 - Set your environment variables
  - ```cp .env-sample .env```
* 6 - Run
  - ```python3 manage.py runserver```


# Web hook examples.
## adding card response. step-1
```
{
    ...
    "Source": "Card",
    "IdempotencyKey": "a9cd7946-ec5c-4c00-8e3f-3775fdf304ef",
    "Type": "AddCard",
    "PaymentId": "4C2B9520ADCB486CAC93F3269",
    "PaymentStatus": "Draft", // not final status
    "Token": "4C2B952xxxxxxxxxAC93F3269",
    "Amount": "0.00",
    "FinalAmount": "0.00",
    "Currency": "UZS",
    ...
}
```
## confirmation card response.
### Final payment status: (Captured, Rejected, Refunded, PartiallyRefunded)
### Card owner entity types: (Private, Corporate, Unknown)
### Card brand types: (Uzcard, Humo, MasterCard, Visa)
```
{
  ...
  "Source": "Card",
  "IdempotencyKey": "8ae858f6-c51d-4bcc-a911-e9ff614f9fa7",
  "PaymentId": "CF61AxxxxxxxxxxxxxF0CEBD0",
  "Type": "AddCard",
  "PaymentStatus": "Captured", // final status.
  "Amount": 1,
  "Token": "CF61AxxxxxxxxxxxxxF0CEBD0",
  "CardMask": "561468xxxxxx2832",
  "CardOwnerEntityType": "Corporate",
  "CardBrand": "Uzcard",
  "CardHolder": null,
  "ExpirationDate": "1226",
  "Payer": {
    "Phone": "998888351717",
    "FullName": "MY TAXI OPS"
  }
  ...
}
```