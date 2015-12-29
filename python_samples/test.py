#!/usr/bin/env python

import random

dataList = [
    {
        "firstName": "Richard",
        "lastName": "Tzeng",
        "address":
        {
            "street": "123 B Street",
            "city": "San Francisco",
            "state": "CA",
            "zip": "94107"
        },
        "email": "rtzeng@okl.com",
        "orders": [ 1, 2, 3, 4, 5],
        "returns":
        [
            {
                "orderNum": 12345,
                "item_sku": 12345,
                "cost": 1234.45
            },
            {
                "orderNum": 12345,
                "item_sku": 12345,
                "cost": 1234.45
            },
            {
                "orderNum": 12345,
                "item_sku": 12345,
                "cost": 1234.45
            }
        ]
    },
    {
        "firstName": "Richard",
        "lastName": "Tzeng",
        "address":
        {
            "street": "123 B Street",
            "city": "San Francisco",
            "state": "CA",
            "zip": "94107"
        },
        "email": "rtzeng@okl.com",
        "orders": [ 1, 2, 3, 4, 5],
        "returns":
        [
            {
                "orderNum": 12345,
                "item_sku": 12345,
                "cost": 1234.45
            },
            {
                "orderNum": 12345,
                "item_sku": 12345,
                "cost": 1234.45
            },
            {
                "orderNum": 12345,
                "item_sku": 12345,
                "cost": 1234.45
            }
        ]
    },
    {
        "firstName": "Richard",
        "lastName": "Tzeng",
        "address":
        {
            "street": "123 B Street",
            "city": "San Francisco",
            "state": "CA",
            "zip": "94107"
        },
        "email": "rtzeng@okl.com",
        "orders": [ 1, 2, 3, 4, 5],
        "returns":
        [
            {
                "orderNum": 12345,
                "item_sku": 12345,
                "cost": 1234.45
            },
            {
                "orderNum": 12345,
                "item_sku": 12345,
                "cost": 1234.45
            },
            {
                "orderNum": 12345,
                "item_sku": 12345,
                "cost": 1234.45
            }
        ]
    },
    {
        "firstName": "Richard",
        "lastName": "Tzeng",
        "address":
        {
            "street": "123 B Street",
            "city": "San Francisco",
            "state": "CA",
            "zip": "94107"
        },
        "email": "rtzeng@okl.com",
        "orders": [ 1, 2, 3, 4, 5],
        "returns":
        [
            {
                "orderNum": 12345,
                "item_sku": 12345,
                "cost": 1234.45
            },
            {
                "orderNum": 12345,
                "item_sku": 12345,
                "cost": 1234.45
            },
            {
                "orderNum": 12345,
                "item_sku": 12345,
                "cost": 1234.45
            }
        ]
    },
]

codeWarDict = {
    "username": "some_user",
    "name": "Some Person",
    "honor": 544,
    "clan": "some clan",
    "leaderboardPosition": 134,
    "skills": [
        "ruby",
        "c#",
        ".net",
        "javascript",
        "coffeescript",
        "nodejs",
        "rails"
    ],
    "ranks": {
        "overall": {
            "rank": -3,
            "name": "3 kyu",
            "color": "blue",
            "score": 2116
        },
        "languages": {
            "javascript": {
                "rank": -3,
                "name": "3 kyu",
                "color": "blue",
                "score": 1819
            },
            "ruby": {
                "rank": -4,
                "name": "4 kyu",
                "color": "blue",
                "score": 1005
            },
            "coffeescript": {
                "rank": -4,
                "name": "4 kyu",
                "color": "blue",
                "score": 870
            }
        }
    },
    "codeChallenges": {
        "totalAuthored": 3,
        "totalCompleted": 230
    }
}

# print codeWarDict.items()
for cust in dataList:
    for key in cust:
        if key == 'returns':
            for x in range(len(cust[key])):
                print key, cust[key][x]

print len(dataList)
