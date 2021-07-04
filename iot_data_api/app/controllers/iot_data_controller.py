import connexion
import six

from app.models.entry import Entry  # noqa: E501
from app.models.error import Error  # noqa: E501
from app import util


def create_iot_data_entry(body):  # noqa: E501
    """Create new iot data entry (sensorId, temperature, humidity)

     # noqa: E501

    :param body: 
    :type body: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = [Entry.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'
