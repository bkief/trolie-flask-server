import unittest

from flask import json

from trolie-flask.models.forecast_limits_detailed_snapshot import ForecastLimitsDetailedSnapshot  # noqa: E501
from trolie-flask.models.forecast_limits_snapshot import ForecastLimitsSnapshot  # noqa: E501
from trolie-flask.models.one_ofintegerstring import OneOfintegerstring  # noqa: E501
from trolie-flask.models.problem import Problem  # noqa: E501
from trolie-flask.models.realtime_limits_detailed_snapshot import RealtimeLimitsDetailedSnapshot  # noqa: E501
from trolie-flask.models.realtime_limits_snapshot import RealtimeLimitsSnapshot  # noqa: E501
from trolie-flask.test import BaseTestCase


class TestOperatingSnapshotsController(BaseTestCase):
    """OperatingSnapshotsController integration test stubs"""

    def test_get_limits_forecast_snapshot(self):
        """Test case for get_limits_forecast_snapshot

        Limits Forecast Snapshot
        """
        query_string = [('offset-period-start', '2013-10-20T19:20:30+01:00'),
                        ('period-end', '2013-10-20T19:20:30+01:00'),
                        ('monitoring-set', 'X-AMPL'),
                        ('transmission-facility', '86753_1')]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/limits/forecast-snapshot',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_real_time_limits(self):
        """Test case for get_real_time_limits

        Limits Real Time Snapshot
        """
        query_string = [('monitoring-set', 'X-AMPL'),
                        ('transmission-facility', '86753_1')]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/limits/realtime-snapshot',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
