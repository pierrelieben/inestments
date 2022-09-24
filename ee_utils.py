from easy_equities_client.clients import EasyEquitiesClient 

import json
import pandas as pd
import os

client = EasyEquitiesClient()


if os.path.exists('config/login_details.json'):
    with open('config/login_details.json', 'r') as login:
        login_details = json.load(login)
        
    client.login(username=login_details['username'], password=login_details['password'])

    # List accounts
    accounts = client.accounts.list()
    """
    [
        Account(id='12345', name='EasyEquities ZAR', trading_currency_id='2'),
        Account(id='12346', name='TFSA', trading_currency_id='3'),
        ...
    ]
    """



    # Get account holdings
    holdings = client.accounts.holdings(accounts[0].id)

    """
    [
        {
            "name": "CoreShares Global DivTrax ETF",
            "contract_code": "EQU.ZA.GLODIV",
            "purchase_value": "R2 000.00",
            "current_value": "R3 000.00",
            "current_price": "R15.50",
            "img": "https://resources.easyequities.co.za/logos/EQU.ZA.GLODIV.png",
            "view_url": "/AccountOverview/GetInstrumentDetailAction/?IsinCode=ZAE000254249",
            "isin": "ZAE000254249"
        },
        ...
    ]
    """
    # Optionally include number of shares for each holding (creates another API call for each holding)
    holdings = client.accounts.holdings(accounts[0].id, include_shares=True)
    """
    [
        {
            "name": "CoreShares Global DivTrax ETF",
            "contract_code": "EQU.ZA.GLODIV",
            "purchase_value": "R2 000.00",
            "current_value": "R3 000.00",
            "current_price": "R15.50",
            "img": "https://resources.easyequities.co.za/logos/EQU.ZA.GLODIV.png",
            "view_url": "/AccountOverview/GetInstrumentDetailAction/?IsinCode=ZAE000254249",
            "isin": "ZAE000254249",
            "shares": "200.123"
        },
        ...
    ]
    """

    # Get account valuations
    valuations = client.accounts.valuations(accounts[0].id)
    """
    {
        "TopSummary": {
            "AccountValue": 300000.50,
            "AccountCurrency": "ZAR",
            "AccountNumber": "EE123456-111111",
            "AccountName": "EasyEquities ZAR",
            "PeriodMovements": [
                {
                    "ValueMoveLabel": "Profit & Loss Value",
                    "ValueMove": "R5 000.00",
                    "PercentageMoveLabel": "Profit & Loss",
                    "PercentageMove": "15.00%",
                    "PeriodMoveHeader": "Movement on Current Holdings:"
                }
            ]
        },
        "NetInterestOnCashItems": [
            {
                "Label": "Total Interest on Free Cash",
                "Value": "R10.55"
            },
            ...
        ],
        "AccrualSummaryItems": [
            {
                "Label": "Net Accrual",
                "Value": "R2.00"
            },
            ...
        ],
        ...
    }
    """

    # Get account transactions
    transactions = client.accounts.transactions(accounts[0].id)
    """
    [
        {
            "TransactionId": 0,
            "DebitCredit": 200.00,
            "Comment": "Account Balance Carried Forward",
            "TransactionDate": "2020-07-21T01:00:00",
            "LogId": 123456789,
            "ActionId": 0,
            "Action": "Account Balance Carried Forward",
            "ContractCode": ""
        },
            {
            "TransactionId": 0,
            "DebitCredit": 50.00,
            "Comment": "CoreShares Global DivTrax ETF-Foreign Dividends @15.00",
            "TransactionDate": "2020-11-19T14:30:00",
            "LogId": 123456790,
            "ActionId": 122,
            "Action": "Foreign Dividend",
            "ContractCode": "EQU.ZA.GLODIV"
        },
        ...
    ]
    """

    # Get historical data for an equity/instrument
    from easy_equities_client.instruments.types import Period
    historical_prices = client.instruments.historical_prices('EQU.ZA.SYGJP', Period.ONE_MONTH)
    """
    {
        "chartData": {
            "Dataset": [
                41.97,
                42.37,
                ...
            ],
            "Labels": [
                "25 Jun 21",
                "28 Jun 21",
                ...
            ],
            "TradingCurrencySymbol": "R",
            ...
        }
    }
    """