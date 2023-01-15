from flask import Flask, request
from app.DependencyContainer import DependencyContainer

app = DependencyContainer()

app_name = app.config_conf().get('APP', 'name')


flask_app = Flask(__name__)


@flask_app.route('/')
def landing():
    return app_name


@flask_app.route('/webhook/<url>', methods=['POST'])
def webhook(url):

    if request.method == 'POST':

        data = request.data.decode()
        header_hmac = request.headers.get('Hmac-SHA256')
        content_type = request.headers.get('Content-Type')

        try:
            print('verify webhook disabled')
            app.service_security().verify_webhook(url, data, header_hmac)
        except Exception as ex:
            return "We won't parse your data since your signature is not valid - Details: " + str(ex) + "\n"

        try:
            serializer = app.serialize_factory().get_serializer(content_type)
            serializer.validate_json_string(data)

            # return "Url, signature and payload schema are valid. We are going to process the data \n"
        except Exception as ex:
            return "Json payload is not valid - Details: " + str(ex)

        try:
            data_dictionary = serializer.deserialize_string(data)
        except Exception as ex:
            return "An error in deserializing the string"

        try:
            data_transaction = serializer.extract_transaction_data(data_dictionary)
        except Exception as ex:
            return str(ex)

        try:
            app.service_breaze().save_transaction(data_transaction)
        except Exception as ex:
            return str(ex)

        return "Job processed"

flask_app.run(
        host='0.0.0.0',
        port=8080
)
