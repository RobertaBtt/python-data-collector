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

        try:
            app.service_security().verify_webhook(url, data, header_hmac)
            return "Url and signature are valid"
        except Exception as ex:
            return "error: " + str(ex)




flask_app.run(
        host='0.0.0.0',
        port=8080
)
