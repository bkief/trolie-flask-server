import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from trolie-flask.models.one_ofintegerstring import OneOfintegerstring  # noqa: E501
from trolie-flask.models.problem import Problem  # noqa: E501
from trolie-flask.models.season_instance import SeasonInstance  # noqa: E501
from trolie-flask.models.seasonal_rating_snapshot import SeasonalRatingSnapshot  # noqa: E501
from trolie-flask import util


def get_season_instance(id):  # noqa: E501
    """Gets a single season instance.

    Gets a single season instance. # noqa: E501

    :param id: ID of the associated object 
    :type id: str

    :rtype: Union[SeasonInstance, Tuple[SeasonInstance, int], Tuple[SeasonInstance, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_season_instances():  # noqa: E501
    """Get Instances of Seasons

    Seasonal ratings are always bound against season instances, with effective dates. # noqa: E501


    :rtype: Union[List[SeasonInstance], Tuple[List[SeasonInstance], int], Tuple[List[SeasonInstance], int, Dict[str, str]]
    """
    return 'do some magic!'


def get_seasonal_ratings_snapshot(monitoring_set=None, transmission_facility=None):  # noqa: E501
    """Get Seasonal Ratings

    Retrieve the nominal and seasonal ratings. # noqa: E501

    :param monitoring_set:  Only return ratings or limits for facilities of the associated &#x60;monitoring-set&#x60;. The identifier for a &#x60;monitoring-set&#x60; is pre-coordinated, but using the NERC id of the associated Ratings Provider is recommended. 
    :type monitoring_set: str
    :param transmission_facility: Only return limits for this transmission facility.   
    :type transmission_facility: str

    :rtype: Union[SeasonalRatingSnapshot, Tuple[SeasonalRatingSnapshot, int], Tuple[SeasonalRatingSnapshot, int, Dict[str, str]]
    """
    return 'do some magic!'
