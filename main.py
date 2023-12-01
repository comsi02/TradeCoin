import datetime
import random
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id, "itme_price": item.price}

@app.get("/api/get_total_data")
def getTotalData():

    elf_buy_order_price = random.randint(100, 900)
    blur_buy_order_price = random.randint(100, 900)
    blur_sell_order_price = random.randint(100, 900)
    blur_benefit_rate = random.randint(1, 99) / 100
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    totalData = getTotalData()
    totalData['kokoko_today_trade_data']['today_buy'][0]['ELF']['buy_order_price'] = elf_buy_order_price
    totalData['kokoko_today_trade_data']['today_buy'][0]['ELF']['buy_time'] = time

    totalData['kokoko_today_trade_data']['today_sell'][0]['BLUR']['buy_order_price'] = blur_buy_order_price
    totalData['kokoko_today_trade_data']['today_sell'][0]['BLUR']['buy_time'] = time

    totalData['kokoko_today_trade_data']['today_sell'][0]['BLUR']['sell_order_price'] = blur_sell_order_price
    totalData['kokoko_today_trade_data']['today_sell'][0]['BLUR']['sell_time'] = time
    totalData['kokoko_today_trade_data']['today_sell'][0]['BLUR']['benefit_rate'] = blur_benefit_rate

    return totalData

def getTotalData():
    return {
        "basic_ticker_data": [
            {
                "TFUEL": {
                    "NOW_TICKER_PRICE": 73.2,
                    "RSI": 54.1,
                    "M_ENVELOP": 72.4,
                    "NOW_BB": 72.57,
                    "MDI": 15.5,
                    "UPDATE_TIME": "02:36:16",
                    "MIN60_VOL_DOWN": "DOWN"
                }
            },
            {
                "ELF": {
                    "NOW_TICKER_PRICE": 669.0,
                    "RSI": 60.5,
                    "M_ENVELOP": 661.2,
                    "NOW_BB": 664.23,
                    "MDI": 13.5,
                    "UPDATE_TIME": "02:36:15",
                    "MIN60_VOL_DOWN": "DOWN"
                }
            },
            {
                "SUI": {
                    "NOW_TICKER_PRICE": 797.0,
                    "RSI": 41.4,
                    "M_ENVELOP": 790.11,
                    "NOW_BB": 796.16,
                    "MDI": 18.2,
                    "UPDATE_TIME": "02:36:15",
                    "MIN60_VOL_DOWN": "DOWN"
                }
            },
            {
                "MINA": {
                    "NOW_TICKER_PRICE": 964.0,
                    "RSI": 36.7,
                    "M_ENVELOP": 956.31,
                    "NOW_BB": 963.21,
                    "MDI": 14.4,
                    "UPDATE_TIME": "02:36:15",
                    "MIN60_VOL_DOWN": "DOWN"
                }
            },
            {
                "XRP": {
                    "NOW_TICKER_PRICE": 808.0,
                    "RSI": 61.1,
                    "M_ENVELOP": 799.14,
                    "NOW_BB": 805.41,
                    "MDI": 7.2,
                    "UPDATE_TIME": "02:36:15",
                    "MIN60_VOL_DOWN": "DOWN"
                }
            },
            {
                "SOL": {
                    "NOW_TICKER_PRICE": 79680.0,
                    "RSI": 56.2,
                    "M_ENVELOP": 78742.16,
                    "NOW_BB": 79220.56,
                    "MDI": 25.3,
                    "UPDATE_TIME": "02:36:15",
                    "MIN60_VOL_DOWN": "DOWN"
                }
            },
            {
                "BLUR": {
                    "NOW_TICKER_PRICE": 670.0,
                    "RSI": 66.1,
                    "M_ENVELOP": 660.97,
                    "NOW_BB": 665.51,
                    "MDI": 17.5,
                    "UPDATE_TIME": "02:36:15",
                    "MIN60_VOL_DOWN": "UP"
                }
            },
            {
                "PUNDIX": {
                    "NOW_TICKER_PRICE": 678.0,
                    "RSI": 57.1,
                    "M_ENVELOP": 670.75,
                    "NOW_BB": 676.56,
                    "MDI": 16.8,
                    "UPDATE_TIME": "02:36:16",
                    "MIN60_VOL_DOWN": "UP"
                }
            },
            {
                "STX": {
                    "NOW_TICKER_PRICE": 921.0,
                    "RSI": 56.1,
                    "M_ENVELOP": 911.19,
                    "NOW_BB": 918.17,
                    "MDI": 28.3,
                    "UPDATE_TIME": "02:36:15",
                    "MIN60_VOL_DOWN": "DOWN"
                }
            },
            {
                "SNT": {
                    "NOW_TICKER_PRICE": 56.3,
                    "RSI": 51.2,
                    "M_ENVELOP": 55.67,
                    "NOW_BB": 56.0,
                    "MDI": 26.3,
                    "UPDATE_TIME": "02:36:15",
                    "MIN60_VOL_DOWN": "DOWN"
                }
            }
        ],
        "upbit_1_now_trade_data": {
            "buy_order_wait_data": [

            ],
            "buy_check_data": [

            ],
            "sell_check_data": [

            ]
        },
        "hihihi_now_trade_data": {
            "buy_order_wait_data": [

            ],
            "buy_check_data": [

            ],
            "sell_check_data": [

            ]
        },
        "kokoko_now_trade_data": {
            "buy_order_wait_data": [

            ],
            "buy_check_data": [

            ],
            "sell_check_data": [
                {
                    "PUNDIX": {
                        "state": "limit_selling",
                        "buy_logic": "LUCKY_B_LOGIC_EMA_test",
                        "buy_price": 677.0,
                        "now_ticker_price": 678.0,
                        "limit_price": 683.0,
                        "chage_rate_anal": 0.15,
                        "buy_elap_data": "82:12",
                        "sell_benefit_rate": 0.01,
                        "sell_loss_rate": -0.02
                    }
                },
                {
                    "ELF": {
                        "state": "limit_selling",
                        "buy_logic": "LUCKY_B_LOGIC_EMA_test",
                        "buy_price": 667.0,
                        "now_ticker_price": 669.0,
                        "limit_price": 673.0,
                        "chage_rate_anal": 0.3,
                        "buy_elap_data": "41:13",
                        "sell_benefit_rate": 0.01,
                        "sell_loss_rate": -0.02
                    }
                }
            ]
        },
        "upbit_1_total_benefit_data": {
            "today_benefit": 0.0,
            "yesterday_benefit": 0.8,
            "this_week_benefit": -1.8,
            "last_week_benefit": 4.2,
            "this_month_benefit": 1055.8,
            "last_month_benefit": -22.9
        },
        "hihihi_total_benefit_data": {
            "today_benefit": 0.0,
            "yesterday_benefit": 0.8,
            "this_week_benefit": -0.8,
            "last_week_benefit": -1.1,
            "this_month_benefit": 4.2,
            "last_month_benefit": 18.5
        },
        "kokoko_total_benefit_data": {
            "today_benefit": 1.5,
            "yesterday_benefit": 0.3,
            "this_week_benefit": 0.2,
            "last_week_benefit": 2.7,
            "this_month_benefit": 4.5,
            "last_month_benefit": -26.6
        },
        "upbit_1_today_trade_data": {
            "today_buy": [

            ],
            "today_sell": [

            ]
        },
        "hihihi_today_trade_data": {
            "today_buy": [

            ],
            "today_sell": [

            ]
        },
        "kokoko_today_trade_data": {
            "today_buy": [
                {
                    "ELF": {
                        "buy_order_funds": 18892.64847677,
                        "buy_order_price": 667.0,
                        "buy_time": "2023-12-01 01:54:58",
                        "buy_logic": "LUCKY_B_LOGIC_EMA_test"
                    }
                },
                {
                    "PUNDIX": {
                        "buy_order_funds": 18873.76056521,
                        "buy_order_price": 677.0,
                        "buy_time": "2023-12-01 01:13:58",
                        "buy_logic": "LUCKY_B_LOGIC_EMA_test"
                    }
                }
            ],
            "today_sell": [
                {
                    "BLUR": {
                        "buy_order_funds": 18797.61320934,
                        "buy_order_price": 658.0,
                        "buy_time": "2023-11-30 23:25:46",
                        "buy_logic": "LUCKY_B_LOGIC_EMA_test",
                        "sell_order_funds": 18969.02,
                        "sell_order_price": "664.0",
                        "sell_time": "2023-12-01 00:14:01",
                        "sell_logic": "매도(익절률: 1.0%)",
                        "benefit_rate": 0.91
                    }
                },
                {
                    "MINA": {
                        "buy_order_funds": 18720.90471354,
                        "buy_order_price": 977.0,
                        "buy_time": "2023-11-30 20:03:16",
                        "buy_logic": "LUCKY_B_LOGIC_EMA_test",
                        "sell_order_funds": 18893.359,
                        "sell_order_price": "986.0",
                        "sell_time": "2023-11-30 20:10:49",
                        "sell_logic": "매도(익절률: 1.0%)",
                        "benefit_rate": 0.92
                    }
                },
                {
                    "MINA": {
                        "buy_order_funds": 18645.11645472,
                        "buy_order_price": 984.0,
                        "buy_time": "2023-11-30 15:48:19",
                        "buy_logic": "LUCKY_B_LOGIC_EMA_test",
                        "sell_order_funds": 18815.651,
                        "sell_order_price": "993.0",
                        "sell_time": "2023-11-30 16:11:13",
                        "sell_logic": "매도(익절률: 1.0%)",
                        "benefit_rate": 0.91
                    }
                },
                {
                    "1INCH": {
                        "buy_order_funds": 0.0,
                        "buy_order_price": 469.0,
                        "buy_time": "2023-11-30 13:19:17",
                        "buy_logic": "LUCKY_B_LOGIC_EMA_test",
                        "sell_order_funds": 18493.723,
                        "sell_order_price": "461.0",
                        "sell_time": "2023-11-30 13:52:47",
                        "sell_logic": "매도(손절률: -2.0%)",
                        "benefit_rate": -1.71
                    }
                },
                {
                    "SOL": {
                        "buy_order_funds": 18731.277307,
                        "buy_order_price": 79630.0,
                        "buy_time": "2023-11-30 10:31:37",
                        "buy_logic": "LUCKY_B_LOGIC_EMA_test",
                        "sell_order_funds": 18917.108,
                        "sell_order_price": "80420.0",
                        "sell_time": "2023-11-30 11:34:56",
                        "sell_logic": "매도(익절률: 1.0%)",
                        "benefit_rate": 0.99
                    }
                },
                {
                    "PUNDIX": {
                        "buy_order_funds": 18652.42546801,
                        "buy_order_price": 739.0,
                        "buy_time": "2023-11-30 10:06:07",
                        "buy_logic": "LUCKY_B_LOGIC_EMA_test",
                        "sell_order_funds": 18829.106,
                        "sell_order_price": "746.0",
                        "sell_time": "2023-11-30 10:13:54",
                        "sell_logic": "매도(익절률: 1.0%)",
                        "benefit_rate": 0.95
                    }
                }
            ]
        }
    }
