import unittest

from flask import json

from trolie-flask.models.forecast_limits_detailed_snapshot import ForecastLimitsDetailedSnapshot  # noqa: E501
from trolie-flask.models.forecast_limits_snapshot import ForecastLimitsSnapshot  # noqa: E501
from trolie-flask.models.forecast_proposal import ForecastProposal  # noqa: E501
from trolie-flask.models.forecast_proposal_status import ForecastProposalStatus  # noqa: E501
from trolie-flask.models.one_ofintegerstring import OneOfintegerstring  # noqa: E501
from trolie-flask.models.problem import Problem  # noqa: E501
from trolie-flask.test import BaseTestCase


class TestForecastingController(BaseTestCase):
    """ForecastingController integration test stubs"""

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


if __name__ == '__main__':
    unittest.main()
