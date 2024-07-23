import unittest

from flask import json

from openapi_server.models.forecast_proposal import ForecastProposal  # noqa: E501
from openapi_server.models.forecast_proposal_status import ForecastProposalStatus  # noqa: E501
from openapi_server.models.one_ofintegerstring import OneOfintegerstring  # noqa: E501
from openapi_server.models.problem import Problem  # noqa: E501
from openapi_server.models.real_time_proposal_status import RealTimeProposalStatus  # noqa: E501
from openapi_server.models.realtime_proposal import RealtimeProposal  # noqa: E501
from openapi_server.models.seasonal_rating_proposal import SeasonalRatingProposal  # noqa: E501
from openapi_server.test import BaseTestCase


class TestRatingProposalsController(BaseTestCase):
    """RatingProposalsController integration test stubs"""

    def test_get_rating_forecast_proposal_status(self):
        """Test case for get_rating_forecast_proposal_status

        Obtain the status of the Ratings Provider's forecast proposal
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/rating-proposals/forecast',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_real_time_proposal_status(self):
        """Test case for get_real_time_proposal_status

        Obtain the status of the Ratings Provider's Real-Time proposals
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/rating-proposals/realtime',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_seasonal_proposal_for_provider(self):
        """Test case for get_seasonal_proposal_for_provider

        Obtain a specific rating proposal by ratings provider
        """
        query_string = [('monitoring-set', 'X-AMPL'),
                        ('segment', '3d5e54d7-534e-49f7-9379-98bddacd96a1')]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/rating-proposals/seasonal/{ratings_provider}'.format(ratings_provider='ratings_provider_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_seasonal_rating_proposal(self):
        """Test case for get_seasonal_rating_proposal

        Get a Seasonal Rating Proposal
        """
        query_string = [('monitoring-set', 'X-AMPL'),
                        ('segment', '3d5e54d7-534e-49f7-9379-98bddacd96a1')]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/rating-proposals/seasonal',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_rating_forecast_proposal(self):
        """Test case for patch_rating_forecast_proposal

        Submit a Forecast Proposal
        """
        forecast_proposal = {"proposal-header":{"source":{"last-updated":"2025-10-31T15:05:43.044267100-07:00","provider":"UTILITY-A","origin-id":"5aeacb25-9b65-4738-8a00-ac10afa63640"},"begins":"2025-11-01T01:00:00-05:00","default-emergency-durations":[{"name":"lte","duration-minutes":240},{"name":"ste","duration-minutes":30},{"name":"dal","duration-minutes":15}],"power-system-resources":[{"resource-id":"8badf00d","alternate-identifiers":[{"name":"segmentX","authority":"TO-NERC-ID"},{"name":"LINE1 SEG-X","authority":"RC-NERC-ID","mrid":"8badf00d"}]}]},"ratings":[{"resource-id":"8badf00d","periods":[{"period-start":"2025-11-01T01:00:00-05:00","period-end":"2025-11-01T02:00:00-05:00","continuous-operating-limit":{"mva":160},"emergency-operating-limits":[{"duration-name":"lte","limit":{"mva":165}},{"duration-name":"ste","limit":{"mva":170}},{"duration-name":"dal","limit":{"mva":170}}]},{"period-start":"2025-11-01T01:00:00-06:00","period-end":"2025-11-02T02:00:00-06:00","continuous-operating-limit":{"mva":160},"emergency-operating-limits":[{"duration-name":"lte","limit":{"mva":165}},{"duration-name":"ste","limit":{"mva":170}},{"duration-name":"dal","limit":{"mva":170}}]}]}]}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/vnd.trolie.rating-forecast-proposal.v1+json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/rating-proposals/forecast',
            method='PATCH',
            headers=headers,
            data=json.dumps(forecast_proposal),
            content_type='application/vnd.trolie.rating-forecast-proposal.v1+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_patch_seasonal_proposal(self):
        """Test case for patch_seasonal_proposal

        Update this Provider's Rating Proposal
        """
        seasonal_rating_proposal = {"ratings":[{"resource-id":"segmentX","seasons":[{"season-id":"fall","continuous-operating-limit":{"mva":160},"emergency-operating-limits":[{"duration-name":"lte","limit":{"mva":165}},{"duration-name":"ste","limit":{"mva":170}},{"duration-name":"dal","limit":{"mva":170}}]}]}]}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/vnd.trolie.seasonal-rating-proposal.v1+json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/rating-proposals/seasonal',
            method='PATCH',
            headers=headers,
            data=json.dumps(seasonal_rating_proposal),
            content_type='application/vnd.trolie.seasonal-rating-proposal.v1+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_patch_seasonal_proposal_by_provider(self):
        """Test case for patch_seasonal_proposal_by_provider

        Update a given Provider's Rating Proposal
        """
        seasonal_rating_proposal = {"ratings":[{"resource-id":"segmentX","seasons":[{"season-id":"fall","continuous-operating-limit":{"mva":160},"emergency-operating-limits":[{"duration-name":"lte","limit":{"mva":165}},{"duration-name":"ste","limit":{"mva":170}},{"duration-name":"dal","limit":{"mva":170}}]}]}]}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/vnd.trolie.seasonal-rating-proposal.v1+json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/rating-proposals/seasonal/{ratings_provider}'.format(ratings_provider='ratings_provider_example'),
            method='PATCH',
            headers=headers,
            data=json.dumps(seasonal_rating_proposal),
            content_type='application/vnd.trolie.seasonal-rating-proposal.v1+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_real_time_proposal(self):
        """Test case for post_real_time_proposal

        Submit Real-Time Rating Proposal
        """
        realtime_proposal = {"proposal-header":{"source":{"last-updated":"2025-10-31T15:05:43.044267100-07:00","provider":"UTILITY-A","origin-id":"5aeacb25-9b65-4738-8a00-ac10afa63640"},"default-emergency-durations":[{"name":"lte","duration-minutes":240},{"name":"ste","duration-minutes":30},{"name":"dal","duration-minutes":15}],"power-system-resources":[{"resource-id":"8badf00d","alternate-identifiers":[{"name":"segmentX","authority":"TO-NERC-ID"},{"name":"LINE1 SEG-X","authority":"RC-NERC-ID","mrid":"8badf00d"}]}]},"ratings":[{"resource-id":"8badf00d","continuous-operating-limit":{"mva":160},"emergency-operating-limits":[{"duration-name":"lte","limit":{"mva":165}},{"duration-name":"ste","limit":{"mva":170}},{"duration-name":"dal","limit":{"mva":170}}]}]}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/vnd.trolie.rating-realtime-proposal.v1+json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/rating-proposals/realtime',
            method='POST',
            headers=headers,
            data=json.dumps(realtime_proposal),
            content_type='application/vnd.trolie.rating-realtime-proposal.v1+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
