import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.one_ofintegerstring import OneOfintegerstring  # noqa: E501
from openapi_server.models.problem import Problem  # noqa: E501
from openapi_server.models.temporary_rating import TemporaryRating  # noqa: E501
from openapi_server import util


def create_temporary_aar_exception(temporary_rating=None):  # noqa: E501
    """Create a new temporary AAR Exception

    Create a new temporary AAR Exception # noqa: E501

    :param temporary_rating: 
    :type temporary_rating: dict | bytes

    :rtype: Union[TemporaryRating, Tuple[TemporaryRating, int], Tuple[TemporaryRating, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        temporary_rating = TemporaryRating.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_temporary_aar_exception(id):  # noqa: E501
    """Delete a specific temporary AAR Exception by Id.

    Delete a specific temporary AAR Exception by Id. # noqa: E501

    :param id: ID of the associated object 
    :type id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_temporary_aar_exception(id):  # noqa: E501
    """Obtain a specific temporary AAR exception by Id.

    Obtain a specific temporary AAR exception by Id. # noqa: E501

    :param id: ID of the associated object 
    :type id: str

    :rtype: Union[TemporaryRating, Tuple[TemporaryRating, int], Tuple[TemporaryRating, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_temporary_aar_exceptions(period_start=None, period_end=None, monitoring_set=None, segment=None):  # noqa: E501
    """Temporary AAR Exceptions

    Search for Temporary AAR Exceptions.  Will return any Temporary AAR Exceptions that overlap with the  start/end period.   Clients SHOULD perform Conditional &#x60;GET&#x60; using the &#x60;If-None-Match&#x60; header and the &#x60;ETag&#x60; of a previous &#x60;GET&#x60; response.  # noqa: E501

    :param period_start: Defines the start of an applicable operating period.   
    :type period_start: str
    :param period_end: Specifies the end of a period for which a filter specifies.  Periods will only be returned that start prior to this time.
    :type period_end: str
    :param monitoring_set:  Only return ratings or limits for facilities of the associated &#x60;monitoring-set&#x60;. The identifier for a &#x60;monitoring-set&#x60; is pre-coordinated, but using the NERC id of the associated Ratings Provider is recommended. 
    :type monitoring_set: str
    :param segment: Only return limits for this segment.   
    :type segment: str

    :rtype: Union[List[TemporaryRating], Tuple[List[TemporaryRating], int], Tuple[List[TemporaryRating], int, Dict[str, str]]
    """
    period_start = util.deserialize_datetime(period_start)
    period_end = util.deserialize_datetime(period_end)
    return 'do some magic!'


def update_temporary_aar_exception(id, temporary_rating=None):  # noqa: E501
    """Updates an existing Temporary AAR Exception.

    Updates an existing Temporary AAR Exception. # noqa: E501

    :param id: ID of the associated object 
    :type id: str
    :param temporary_rating: 
    :type temporary_rating: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        temporary_rating = TemporaryRating.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
