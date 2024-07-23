import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from trolie-flask.models.forecast_limits_detailed_snapshot import ForecastLimitsDetailedSnapshot  # noqa: E501
from trolie-flask.models.forecast_limits_snapshot import ForecastLimitsSnapshot  # noqa: E501
from trolie-flask.models.one_ofintegerstring import OneOfintegerstring  # noqa: E501
from trolie-flask.models.problem import Problem  # noqa: E501
from trolie-flask.models.realtime_limits_detailed_snapshot import RealtimeLimitsDetailedSnapshot  # noqa: E501
from trolie-flask.models.realtime_limits_snapshot import RealtimeLimitsSnapshot  # noqa: E501
from trolie-flask import util


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
