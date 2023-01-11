import hmac
import hashlib
import base64
from app.log.LogAbstract import LogAbstract

class ServiceSecurity:

    def __init__(self, logger: LogAbstract):

        self.logger = logger

        # Client knows which are the registered API secrets
        self.dictionary_urls_APIS = {
            'djsnckvj': 'API_SECRET_CLIENT1',
            'wpeori': 'API_SECRET_CLIENT2',
            'zxbaandg': 'API_SECRET_CLIENT3'
        }

    def verify_webhook(self, url: str, payload: str, header_hmac: str):

        url_api_key = self.verify_url_api_key(url)

        if url_api_key is not None:
            if self.verify_hmac_signature(url_api_key, payload, header_hmac):
                return True
            else:
                error = "Webhook Signature is not valid"
                self.logger.error(f'{error}')
                raise Exception(error)
        else:
            error = "Webhook Url not found"
            self.logger.error(f'{error}')
            raise Exception(error)

    # Is this URL and api webhook registered in our systems ?
    # If yes, return the correspondent API SECRET KEY
    def verify_url_api_key(self, url_str) -> str:
        if url_str in self.dictionary_urls_APIS:
            return self.dictionary_urls_APIS[url_str]
        else:
            return None

    # Can the hmac signature be validated ?
    def verify_hmac_signature(self, api_secret_key: str, payload: str, header_hmac: str) -> bool:
        hmac_result = hmac.new(
            api_secret_key.encode('utf-8'),
            payload.encode('utf-8'),
            digestmod=hashlib.sha256)

        hmac_digest = hmac_result.digest()

        computed_mac = base64.b64encode(hmac_digest)
        expected_result = header_hmac.encode('utf-8')

        return hmac.compare_digest(computed_mac, expected_result)

