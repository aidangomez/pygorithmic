# pygorithmic-trading (In Development)
A QuestTrade API wrapper designed to streamline the development of investment algorithms.

##Install
######Dependancies:
`sudo pip install py-dateutil numpy requests`
######Connect your Questrade Tokens (Optional †)
† - Only if you wish to use the framework with your own raw data.

**Steps:**
- Go to http://www.questrade.com/api/documentation/getting-started and read.
- Register two separate applications; one for market calls and one for account calls (make sure you have set the appropriate authority rights for each application).
- As in *Authorizing your app to access the API* from Questrade's getting started page, fetch your access and refresh tokens using the url: `https://login.questrade.com/oauth2/token?grant_type=refresh_token&refresh_token=<refresh_token>`
- Create the tokens directory entitled *questrade-tokens*: `mkdir questrade-tokens`
- Within `questrade-tokens` create two files `account-tokens.txt` and `market-tokens.txt` each formatted to the specifications below (**ensure** that you've placed the correct tokens associated with the `account` or `market` applications you created earlier)
```
<access token>
<refresh token>
<api address>
```

######Debugging:
If you are not running market/account requests frequently enough, refresh tokens will expire.

######To see and example:
In root dir, run: `python3 demo.py`

View demo.py and you will see the actions it takes are the following:
- create a **Database**
- fill Database with price data using *populate-database* functionality
- pass data along with a sample algorithm to *algo-tester* and print the results of the test
