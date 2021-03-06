from cryptoxlib.clients.bitforex.BitforexClient import BitforexClient
from cryptoxlib.clients.liquid.LiquidClient import LiquidClient
from cryptoxlib.clients.bibox.BiboxClient import BiboxClient
from cryptoxlib.clients.bibox_europe.BiboxEuropeClient import BiboxEuropeClient
from cryptoxlib.clients.bitpanda.BitpandaClient import BitpandaClient
from cryptoxlib.clients.binance.BinanceClient import BinanceClient
from cryptoxlib.clients.bitvavo.BitvavoClient import BitvavoClient
from cryptoxlib.clients.btse.BtseClient import BtseClient
from cryptoxlib.clients.aax.AAXClient import AAXClient


class CryptoXLib(object):
    @staticmethod
    def create_bitforex_client(api_key: str, sec_key: str) -> BitforexClient:
        return BitforexClient(api_key, sec_key)

    @staticmethod
    def create_liquid_client(api_key: str, sec_key: str) -> LiquidClient:
        return LiquidClient(api_key, sec_key)

    @staticmethod
    def create_bibox_client(api_key: str, sec_key: str) -> BiboxClient:
        return BiboxClient(api_key, sec_key)

    @staticmethod
    def create_bibox_europe_client(api_key: str, sec_key: str) -> BiboxEuropeClient:
        return BiboxEuropeClient(api_key, sec_key)

    @staticmethod
    def create_bitpanda_client(api_key: str) -> BitpandaClient:
        return BitpandaClient(api_key)

    @staticmethod
    def create_binance_client(api_key: str, sec_key: str) -> BinanceClient:
        return BinanceClient(api_key, sec_key)

    @staticmethod
    def create_bitvavo_client(api_key: str, sec_key: str) -> BitvavoClient:
        return BitvavoClient(api_key, sec_key)

    @staticmethod
    def create_btse_client(api_key: str, sec_key: str) -> BtseClient:
        return BtseClient(api_key, sec_key)

    @staticmethod
    def create_aax_client(api_key: str, sec_key: str) -> AAXClient:
        return AAXClient(api_key, sec_key)