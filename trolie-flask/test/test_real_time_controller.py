import unittest

from flask import json

from trolie-flask.models.one_ofintegerstring import OneOfintegerstring  # noqa: E501
from trolie-flask.models.problem import Problem  # noqa: E501
from trolie-flask.models.real_time_proposal_status import RealTimeProposalStatus  # noqa: E501
from trolie-flask.models.realtime_limits_detailed_snapshot import RealtimeLimitsDetailedSnapshot  # noqa: E501
from trolie-flask.models.realtime_limits_snapshot import RealtimeLimitsSnapshot  # noqa: E501
from trolie-flask.models.realtime_proposal import RealtimeProposal  # noqa: E501
from trolie-flask.test import BaseTestCase


class TestRealTimeController(BaseTestCase):
    """RealTimeController integration test stubs"""

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
