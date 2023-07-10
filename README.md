# Payze Implementation

This MVP project helps for implementing <a href="https://docs.payze.io/reference/getting-started">payze-doc</a>.

### API Endpoints <br>

### Call Back endpoints
- `/v1/pay/` Pay the Order
- `/v1/success/` Call Back Success Endpoint
- `/v1/accept/` Accept Card Token And Transacion Values from Front Side
- `/v1/order/` Create a New Order with Specific Card ID
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
