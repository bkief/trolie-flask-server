import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from trolie-flask.models.one_ofintegerstring import OneOfintegerstring  # noqa: E501
from trolie-flask.models.problem import Problem  # noqa: E501
from trolie-flask.models.real_time_proposal_status import RealTimeProposalStatus  # noqa: E501
from trolie-flask.models.realtime_limits_detailed_snapshot import RealtimeLimitsDetailedSnapshot  # noqa: E501
from trolie-flask.models.realtime_limits_snapshot import RealtimeLimitsSnapshot  # noqa: E501
from trolie-flask.models.realtime_proposal import RealtimeProposal  # noqa: E501
from trolie-flask import util


def get_real_time_limits(monitoring_set=None, transmission_facility=None):  # noqa: E501
    """Limits Real Time Snapshot

     Obtain the System Operating Limits in-use by the Transmission Provider.  Clients SHOULD perform Conditional &#x60;GET&#x60; using the &#x60;If-None-Match&#x60; header and the &#x60;ETag&#x60; of a previous &#x60;GET&#x60; response to poll this endpoint. Rate limiting is done on a per Ratings Provider basis, so requests from independent clients used by the same provider count against the same quota.  # noqa: E501

    :param monitoring_set:  Only return ratings or limits for facilities of the associated &#x60;monitoring-set&#x60;. The identifier for a &#x60;monitoring-set&#x60; is pre-coordinated, but using the NERC id of the associated Ratings Provider is recommended. 
    :type monitoring_set: str
    :param transmission_facility: Only return limits for this transmission facility.   
    :type transmission_facility: str

    :rtype: Union[RealtimeLimitsSnapshot, Tuple[RealtimeLimitsSnapshot, int], Tuple[RealtimeLimitsSnapshot, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_real_time_proposal_status():  # noqa: E501
    """Obtain the status of the Ratings Provider&#39;s Real-Time proposals

     Used to obtain the status of real-time ratings proposals. The response is implicitly restricted to the requesting Ratings Provider&#39;s obligation. Accordingly, the caller can use this endpoint to check the state of their proposal submission.  Note that the same status object is returned for each &#x60;postRealTimeProposal&#x60;, so this endpoint may seem redundant. However, an anticipated use case for this &#x60;GET&#x60; endpoint is to support supervisor processes that are setup by the client to independently ensure the provider&#39;s process for rating submission if functioning properly. For example, the Rating Provider might have one program responsible for producing and submitting Ratings via &#x60;postRealTimeProposal&#x60;, while having a separate monitoring job that checks this endpoint regularly.  Clients SHOULD perform Conditional &#x60;GET&#x60; using the &#x60;If-None-Match&#x60; header and the &#x60;ETag&#x60; of a previous &#x60;GET&#x60; response to poll this endpoint. Rate limiting is done on a per Ratings Provider basis, so requests from independent clients used by the same provider count against the same quota.  # noqa: E501


    :rtype: Union[RealTimeProposalStatus, Tuple[RealTimeProposalStatus, int], Tuple[RealTimeProposalStatus, int, Dict[str, str]]
    """
    return 'do some magic!'


def post_real_time_proposal(realtime_proposal=None):  # noqa: E501
    """Submit Real-Time Rating Proposal

     At the discretion of the TROLIE server owner, Ratings Providers use  this endpoint to submit ratings within the current hour.   These are assumed to be real-time ratings, based on measurements of ambient conditions as opposed to forecasts.  These ratings will be  used by Transmission Providers in real-time grid operations processes,  such as state estimator and real-time markets.  The clearinghouse for real-time ratings may be run more frequently than the one for forecast ratings to adapt to real-world  conditions.    These ratings may be either AARs or DLRs.    The API mechanics are different than forecasts, as there is no implicitly created time window to modify.  Ratings providers simply &#x60;POST&#x60; new values as they are measured and computed.    Rules for usage however are similar to forecasts; real-time proposals do not have to contain every resource for which the Ratings Provider is responsible.  Data may be broken into batches across the Rating Provider&#39;s footprint.    Status of the real-time proposals also includes an indication of incomplete obligations, much like forecast.  However, the meaning of this is somewhat different, as it simply indicates  data that is either completely missing, or is considered stale by the Clearinghouse Provider, likely due to simply not receiving a value within a reasonable period, such as an hour.    # noqa: E501

    :param realtime_proposal: 
    :type realtime_proposal: dict | bytes

    :rtype: Union[RealTimeProposalStatus, Tuple[RealTimeProposalStatus, int], Tuple[RealTimeProposalStatus, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        realtime_proposal = RealtimeProposal.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
