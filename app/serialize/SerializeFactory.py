from . import SerializeJSON
from . import SerializeYAML
from . import SerializeXML

# This class is the Abstract Factory for the serializer,
# because the input of the service may differ in the format,
# and this application is ready to adapt to different formats.
#
# Registry / Service container of the Classes that
# can adapt to different data sources or services (XML, JSON, YAML, CSV ecc)


SERIALIZERS_DICT = dict()


def register():
    """Register a Service Class that can adapt to different data sources"""
    SERIALIZERS_DICT["JSON"] = SerializeJSON.SerializeJSON
    SERIALIZERS_DICT["XML"] = SerializeXML.SerializeXML
    SERIALIZERS_DICT["YAML"] = SerializeYAML.SerializeYAML


class SerializeFactory:

    def __init__(self):
        register()

    def get_serializer(self, service_type):
        return SERIALIZERS_DICT[service_type]