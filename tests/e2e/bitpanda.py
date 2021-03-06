import unittest
import os
import logging
import datetime

from cryptoxlib.CryptoXLib import CryptoXLib
from cryptoxlib.clients.bitpanda import enums
from cryptoxlib.Pair import Pair
from cryptoxlib.clients.bitpanda.exceptions import BitpandaRestException

from CryptoXLibTest import CryptoXLibTest

api_key = os.environ['BITPANDAAPIKEY']


class BitpandaRestApi(CryptoXLibTest):
    @classmethod
    def initialize(cls) -> None:
        cls.client = CryptoXLib.create_bitpanda_client(api_key)
        cls.print_logs = True
        cls.log_level = logging.DEBUG

    def check_positive_response(self, response):
        return str(response['status_code'])[0] == '2'

    async def test_get_time(self):
        response = await self.client.get_time()
        self.assertTrue(self.check_positive_response(response))

    async def test_get_account_balances(self):
        response = await self.client.get_account_balances()
        self.assertTrue(self.check_positive_response(response))

    async def test_get_account_orders(self):
        response = await self.client.get_account_orders()
        self.assertTrue(self.check_positive_response(response))

    async def test_get_account_order(self):
        with self.assertRaises(BitpandaRestException) as cm:
            await self.client.get_account_order("1")
        e = cm.exception

        self.assertEqual(e.status_code, 400)

    async def test_create_market_order(self):
        with self.assertRaises(BitpandaRestException) as cm:
            await self.client.create_market_order(Pair("BTC", "EUR"), enums.OrderSide.BUY, "100000")
        e = cm.exception

        self.assertEqual(e.status_code, 422)

    async def test_create_limit_order(self):
        with self.assertRaises(BitpandaRestException) as cm:
            await self.client.create_limit_order(Pair("BTC", "EUR"), enums.OrderSide.BUY, "10000", "1")
        e = cm.exception

        self.assertEqual(e.status_code, 422)

    async def test_create_stop_limit_order(self):
        with self.assertRaises(BitpandaRestException) as cm:
            await self.client.create_stop_limit_order(Pair("BTC", "EUR"), enums.OrderSide.BUY, "10000", "1", "1")
        e = cm.exception

        self.assertEqual(e.status_code, 422)

    async def test_delete_account_order(self):
        with self.assertRaises(BitpandaRestException) as cm:
            await self.client.delete_account_order("1")
        e = cm.exception

        self.assertEqual(e.status_code, 404)

    async def test_get_account_order_trades(self):
        with self.assertRaises(BitpandaRestException) as cm:
            await self.client.get_account_order_trades("1")
        e = cm.exception

        self.assertEqual(e.status_code, 400)

    async def test_get_account_trades(self):
        response = await self.client.get_account_trades()
        self.assertTrue(self.check_positive_response(response))

    async def test_get_account_trade(self):
        with self.assertRaises(BitpandaRestException) as cm:
            await self.client.get_account_trade("1")
        e = cm.exception

        self.assertEqual(e.status_code, 400)

    async def test_get_account_trading_volume(self):
        response = await self.client.get_account_trading_volume()
        self.assertTrue(self.check_positive_response(response))

    async def test_get_currencies(self):
        response = await self.client.get_currencies()
        self.assertTrue(self.check_positive_response(response))

    async def test_find_order(self):
        response = await self.client.get_candlesticks(Pair("BTC", "EUR"), enums.TimeUnit.DAYS, "1",
                                  datetime.datetime.now() - datetime.timedelta(days = 7), datetime.datetime.now())
        self.assertTrue(self.check_positive_response(response))

    async def test_get_account_fees(self):
        response = await self.client.get_account_fees()
        self.assertTrue(self.check_positive_response(response))

    async def test_get_instruments(self):
        response = await self.client.get_instruments()
        self.assertTrue(self.check_positive_response(response))

    async def test_get_order_book(self):
        response = await self.client.get_order_book(Pair("BTC", "EUR"))
        self.assertTrue(self.check_positive_response(response))


if __name__ == '__main__':
    unittest.main()