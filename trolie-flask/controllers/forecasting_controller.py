import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.forecast_limits_detailed_snapshot import ForecastLimitsDetailedSnapshot  # noqa: E501
from openapi_server.models.forecast_limits_snapshot import ForecastLimitsSnapshot  # noqa: E501
from openapi_server.models.forecast_proposal import ForecastProposal  # noqa: E501
from openapi_server.models.forecast_proposal_status import ForecastProposalStatus  # noqa: E501
from openapi_server.models.one_ofintegerstring import OneOfintegerstring  # noqa: E501
from openapi_server.models.problem import Problem  # noqa: E501
from openapi_server import util


def get_limits_forecast_snapshot(offset_period_start=None, period_end=None, monitoring_set=None, transmission_facility=None):  # noqa: E501
    """Limits Forecast Snapshot

     Obtain the Limits Forecast the Transmission Provider is currently using in Operations, relative to the current time.   This operation uses media types to control verbosity of the data fetched. The default media type, &#x60;application/vnd.trolie.forecast-limits-snapshot.v1+json&#x60;, simply includes the rating data. For applications that need it, the media type &#x60;application/vnd.trolie.forecast-limits-detailed-snapshot.v1+json&#x60; may be requested, which also references the source proposals used to generate the snapshot, as well as reporting data from the ratings clearing process.  Clients SHOULD perform Conditional &#x60;GET&#x60; using the &#x60;If-None-Match&#x60; header and the &#x60;ETag&#x60; of a previous &#x60;GET&#x60; response to poll this endpoint. Rate limiting is done on a per Ratings Provider basis, so requests from independent clients used by the same provider count against the same quota.      # noqa: E501

    :param offset_period_start: Rather than return the entire forecast from the beginning, i.e., the next operating period, instead return a subset of the forecast starting with the period starting at &#x60;offset-period-start&#x60;. 
    :type offset_period_start: str
    :param period_end: Specifies the end of a period for which a filter specifies.  Periods will only be returned that start prior to this time.
    :type period_end: str
    :param monitoring_set:  Only return ratings or limits for facilities of the associated &#x60;monitoring-set&#x60;. The identifier for a &#x60;monitoring-set&#x60; is pre-coordinated, but using the NERC id of the associated Ratings Provider is recommended. 
    :type monitoring_set: str
    :param transmission_facility: Only return limits for this transmission facility.   
    :type transmission_facility: str

    :rtype: Union[ForecastLimitsSnapshot, Tuple[ForecastLimitsSnapshot, int], Tuple[ForecastLimitsSnapshot, int, Dict[str, str]]
    """
    offset_period_start = util.deserialize_datetime(offset_period_start)
    period_end = util.deserialize_datetime(period_end)
    return 'do some magic!'


def get_rating_forecast_proposal_status():  # noqa: E501
    """Obtain the status of the Ratings Provider&#39;s forecast proposal

     Used to obtain the status of the Ratings Forecast proposal. The response is implicitly restricted to the requesting Ratings Provider&#39;s obligation. Accordingly, the caller can use this endpoint to check the state of their proposal submission.  Note that the same status object is returned for each &#x60;patchRatingForecastProposal&#x60;, so this endpoint may seem redundant. However, an anticipated use case for this &#x60;GET&#x60; endpoint is to support supervisor processes that are setup by the client to independently ensure the provider&#39;s process for rating submission if functioning properly. For example, the Rating Provider might have one program responsible for producing and submitting Ratings Forecasts via &#x60;patchRatingForecastProposal&#x60;, while having a separate monitoring job that checks this endpoint regularly.  Clients SHOULD perform Conditional &#x60;GET&#x60; using the &#x60;If-None-Match&#x60; header and the &#x60;ETag&#x60; of a previous &#x60;GET&#x60; response to poll this endpoint. Rate limiting is done on a per Ratings Provider basis, so requests from independent clients used by the same provider count against the same quota.  # noqa: E501


    :rtype: Union[ForecastProposalStatus, Tuple[ForecastProposalStatus, int], Tuple[ForecastProposalStatus, int, Dict[str, str]]
    """
    return 'do some magic!'


def patch_rating_forecast_proposal(forecast_proposal=None):  # noqa: E501
    """Submit a Forecast Proposal

     In every Forecast Window, a new area-wide Forecast Proposal is created on the TROLIE server of the Clearinghouse Provider. Each Ratings Provider then &#x60;PATCH&#x60;es the area-wide proposal with the forecasts for their respective Ratings Obligations. Any unmet Ratings Obligations will result in the Clearinghouse Provider using an appropriate Recourse Rating for those unmet obligations.  For Ratings Providers with a natural split in their Ratings Obligations, e.g., geographic or control areas, the &#x60;PATCH&#x60; semantics afford the ability to submit multiple Forecast Proposals containing just proposals for the relevant resources, if they choose to do so. This affordance can also be leveraged to split a large proposal into one or more parts in cases where that is advantageous from a performance or reliable delivery perspective.  # noqa: E501

    :param forecast_proposal: 
    :type forecast_proposal: dict | bytes

    :rtype: Union[ForecastProposalStatus, Tuple[ForecastProposalStatus, int], Tuple[ForecastProposalStatus, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        forecast_proposal = ForecastProposal.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
