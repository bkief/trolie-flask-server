import unittest

from flask import json

from trolie-flask.models.one_ofintegerstring import OneOfintegerstring  # noqa: E501
from trolie-flask.models.problem import Problem  # noqa: E501
from trolie-flask.models.season_instance import SeasonInstance  # noqa: E501
from trolie-flask.models.seasonal_rating_snapshot import SeasonalRatingSnapshot  # noqa: E501
from trolie-flask.test import BaseTestCase


class TestSeasonalRatingSnapshotsController(BaseTestCase):
    """SeasonalRatingSnapshotsController integration test stubs"""

    def test_get_season_instance(self):
        """Test case for get_season_instance

        Gets a single season instance.
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/seasonal-ratings/season-instances/{id}'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_season_instances(self):
        """Test case for get_season_instances

        Get Instances of Seasons
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/seasonal-ratings/season-instances',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_seasonal_ratings_snapshot(self):
        """Test case for get_seasonal_ratings_snapshot

        Get Seasonal Ratings
        """
        query_string = [('monitoring-set', 'X-AMPL'),
                        ('transmission-facility', '86753_1')]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/seasonal-ratings/snapshot',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
