# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from app.models.entry import Entry
from app.models.error import Error
from app.test import BaseTestCase


class TestPetsController(BaseTestCase):
    """PetsController integration test stubs"""

    def test_create_iot_data_entry(self):
        """Test case for create_iot_data_entry

        Create new iot data entry (sensorId, temperature, humidity)
        """
        body = [Entry()]
        response = self.client.open(
            '/data',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
