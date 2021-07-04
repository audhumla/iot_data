import connexion
import six

from app.models.entry import Entry  # noqa: E501
from app.models.error import Error  # noqa: E501
from app import util


def get_healthz():  # noqa: E501
    """Return the state of the application
    """
    return '{ status: "OK" }'
