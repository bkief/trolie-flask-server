import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.forecast_proposal import ForecastProposal  # noqa: E501
from openapi_server.models.forecast_proposal_status import ForecastProposalStatus  # noqa: E501
from openapi_server.models.one_ofintegerstring import OneOfintegerstring  # noqa: E501
from openapi_server.models.problem import Problem  # noqa: E501
from openapi_server.models.real_time_proposal_status import RealTimeProposalStatus  # noqa: E501
from openapi_server.models.realtime_proposal import RealtimeProposal  # noqa: E501
from openapi_server.models.seasonal_rating_proposal import SeasonalRatingProposal  # noqa: E501
from openapi_server import util


def get_rating_forecast_proposal_status():  # noqa: E501
    """Obtain the status of the Ratings Provider&#39;s forecast proposal

     Used to obtain the status of the Ratings Forecast proposal. The response is implicitly restricted to the requesting Ratings Provider&#39;s obligation. Accordingly, the caller can use this endpoint to check the state of their proposal submission.  Note that the same status object is returned for each &#x60;patchRatingForecastProposal&#x60;, so this endpoint may seem redundant. However, an anticipated use case for this &#x60;GET&#x60; endpoint is to support supervisor processes that are setup by the client to independently ensure the provider&#39;s process for rating submission if functioning properly. For example, the Rating Provider might have one program responsible for producing and submitting Ratings Forecasts via &#x60;patchRatingForecastProposal&#x60;, while having a separate monitoring job that checks this endpoint regularly.  Clients SHOULD perform Conditional &#x60;GET&#x60; using the &#x60;If-None-Match&#x60; header and the &#x60;ETag&#x60; of a previous &#x60;GET&#x60; response to poll this endpoint. Rate limiting is done on a per Ratings Provider basis, so requests from independent clients used by the same provider count against the same quota.  # noqa: E501


    :rtype: Union[ForecastProposalStatus, Tuple[ForecastProposalStatus, int], Tuple[ForecastProposalStatus, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_real_time_proposal_status():  # noqa: E501
    """Obtain the status of the Ratings Provider&#39;s Real-Time proposals

     Used to obtain the status of real-time ratings proposals. The response is implicitly restricted to the requesting Ratings Provider&#39;s obligation. Accordingly, the caller can use this endpoint to check the state of their proposal submission.  Note that the same status object is returned for each &#x60;postRealTimeProposal&#x60;, so this endpoint may seem redundant. However, an anticipated use case for this &#x60;GET&#x60; endpoint is to support supervisor processes that are setup by the client to independently ensure the provider&#39;s process for rating submission if functioning properly. For example, the Rating Provider might have one program responsible for producing and submitting Ratings via &#x60;postRealTimeProposal&#x60;, while having a separate monitoring job that checks this endpoint regularly.  Clients SHOULD perform Conditional &#x60;GET&#x60; using the &#x60;If-None-Match&#x60; header and the &#x60;ETag&#x60; of a previous &#x60;GET&#x60; response to poll this endpoint. Rate limiting is done on a per Ratings Provider basis, so requests from independent clients used by the same provider count against the same quota.  # noqa: E501


    :rtype: Union[RealTimeProposalStatus, Tuple[RealTimeProposalStatus, int], Tuple[RealTimeProposalStatus, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_seasonal_proposal_for_provider(ratings_provider, monitoring_set=None, segment=None):  # noqa: E501
    """Obtain a specific rating proposal by ratings provider

    Obtain a specific rating proposal by ratings provider # noqa: E501

    :param ratings_provider: Identifier (typically NERC Id) of a ratings provider.   
    :type ratings_provider: str
    :param monitoring_set:  Only return ratings or limits for facilities of the associated &#x60;monitoring-set&#x60;. The identifier for a &#x60;monitoring-set&#x60; is pre-coordinated, but using the NERC id of the associated Ratings Provider is recommended. 
    :type monitoring_set: str
    :param segment: Only return limits for this segment.   
    :type segment: str

    :rtype: Union[SeasonalRatingProposal, Tuple[SeasonalRatingProposal, int], Tuple[SeasonalRatingProposal, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_seasonal_rating_proposal(monitoring_set=None, segment=None):  # noqa: E501
    """Get a Seasonal Rating Proposal

     Obtain the latest Seasonal Ratings the Ratings Provider has submitted.    Clients SHOULD perform Conditional &#x60;GET&#x60; using the &#x60;If-None-Match&#x60; header and the &#x60;ETag&#x60; of a previous &#x60;GET&#x60; response.  # noqa: E501

    :param monitoring_set:  Only return ratings or limits for facilities of the associated &#x60;monitoring-set&#x60;. The identifier for a &#x60;monitoring-set&#x60; is pre-coordinated, but using the NERC id of the associated Ratings Provider is recommended. 
    :type monitoring_set: str
    :param segment: Only return limits for this segment.   
    :type segment: str

    :rtype: Union[SeasonalRatingProposal, Tuple[SeasonalRatingProposal, int], Tuple[SeasonalRatingProposal, int, Dict[str, str]]
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


def patch_seasonal_proposal(seasonal_rating_proposal=None):  # noqa: E501
    """Update this Provider&#39;s Rating Proposal

    Update this Provider&#39;s Rating Proposal # noqa: E501

    :param seasonal_rating_proposal: 
    :type seasonal_rating_proposal: dict | bytes

    :rtype: Union[SeasonalRatingProposal, Tuple[SeasonalRatingProposal, int], Tuple[SeasonalRatingProposal, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        seasonal_rating_proposal = SeasonalRatingProposal.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_seasonal_proposal_by_provider(ratings_provider, seasonal_rating_proposal=None):  # noqa: E501
    """Update a given Provider&#39;s Rating Proposal

    Update a given Provider&#39;s Rating Proposal # noqa: E501

    :param ratings_provider: Identifier (typically NERC Id) of a ratings provider.   
    :type ratings_provider: str
    :param seasonal_rating_proposal: 
    :type seasonal_rating_proposal: dict | bytes

    :rtype: Union[SeasonalRatingProposal, Tuple[SeasonalRatingProposal, int], Tuple[SeasonalRatingProposal, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        seasonal_rating_proposal = SeasonalRatingProposal.from_dict(connexion.request.get_json())  # noqa: E501
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
