import unittest

from flask import json

from openapi_server.models.one_ofintegerstring import OneOfintegerstring  # noqa: E501
from openapi_server.models.problem import Problem  # noqa: E501
from openapi_server.models.temporary_rating import TemporaryRating  # noqa: E501
from openapi_server.test import BaseTestCase


class TestTemporarySeasonalRatingsController(BaseTestCase):
    """TemporarySeasonalRatingsController integration test stubs"""

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_create_temporary_seasonal_rating(self):
        """Test case for create_temporary_seasonal_rating

        Create a new temporary temporary seasonal rating 
        """
        temporary_rating = {"resource-id":"segmentX","start-time":"2025-07-12T16:00:00-07:00","end-time":"2025-07-13T12:00:00-07:00","continuous-operating-limit":{"mva":160},"emergency-operating-limits":[{"duration-name":"emergency","limit":{"mva":165}},{"duration-name":"load-shed","limit":{"mva":170}}],"reason":"Free-form text reason."}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/vnd.trolie.temporary-seasonal-rating.v1+json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/temporary-seasonal-ratings',
            method='POST',
            headers=headers,
            data=json.dumps(temporary_rating),
            content_type='application/vnd.trolie.temporary-seasonal-rating.v1+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_temporary_seasonal_rating(self):
        """Test case for delete_temporary_seasonal_rating

        Delete a specific temporary seasonal rating by its Id.
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/temporary-seasonal-ratings/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_temporary_seasonal_rating(self):
        """Test case for get_temporary_seasonal_rating

        Obtain a specific temporary seasonal rating by Id.
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/temporary-seasonal-ratings/{id}'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_temporary_seasonal_ratings(self):
        """Test case for get_temporary_seasonal_ratings

        Get Temporary Seasonal Ratings
        """
        query_string = [('period-start', '2013-10-20T19:20:30+01:00'),
                        ('period-end', '2013-10-20T19:20:30+01:00'),
                        ('monitoring-set', 'X-AMPL'),
                        ('segment', '3d5e54d7-534e-49f7-9379-98bddacd96a1')]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/temporary-seasonal-ratings',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_update_temporary_seasonal_rating(self):
        """Test case for update_temporary_seasonal_rating

        Updates an existing Temporary Seasonal Rating.
        """
        temporary_rating = {"id":"46f7212b-1633-4c30-ba71-c6e987b2ded7","resource-id":"segmentX","start-time":"2025-07-12T16:00:00-07:00","end-time":"2025-07-13T12:00:00-07:00","continuous-operating-limit":{"mva":160},"emergency-operating-limits":[{"duration-name":"emergency","limit":{"mva":165}},{"duration-name":"load-shed","limit":{"mva":170}}],"reason":"Free-form text reason."}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/vnd.trolie.temporary-seasonal-rating.v1+json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/temporary-seasonal-ratings/{id}'.format(id='id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(temporary_rating),
            content_type='application/vnd.trolie.temporary-seasonal-rating.v1+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
