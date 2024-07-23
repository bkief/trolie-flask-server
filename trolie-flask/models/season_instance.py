from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
import re
from openapi_server import util

import re  # noqa: E501

class SeasonInstance(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, season=None, id=None, effective_time=None, active=None):  # noqa: E501
        """SeasonInstance - a model defined in OpenAPI

        :param season: The season of this SeasonInstance.  # noqa: E501
        :type season: str
        :param id: The id of this SeasonInstance.  # noqa: E501
        :type id: str
        :param effective_time: The effective_time of this SeasonInstance.  # noqa: E501
        :type effective_time: datetime
        :param active: The active of this SeasonInstance.  # noqa: E501
        :type active: bool
        """
        self.openapi_types = {
            'season': str,
            'id': str,
            'effective_time': datetime,
            'active': bool
        }

        self.attribute_map = {
            'season': 'season',
            'id': 'id',
            'effective_time': 'effective-time',
            'active': 'active'
        }

        self._season = season
        self._id = id
        self._effective_time = effective_time
        self._active = active

    @classmethod
    def from_dict(cls, dikt) -> 'SeasonInstance':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The season-instance of this SeasonInstance.  # noqa: E501
        :rtype: SeasonInstance
        """
        return util.deserialize_model(dikt, cls)

    @property
    def season(self) -> str:
        """Gets the season of this SeasonInstance.

         Contains a unique identifier for an object.    # noqa: E501

        :return: The season of this SeasonInstance.
        :rtype: str
        """
        return self._season

    @season.setter
    def season(self, season: str):
        """Sets the season of this SeasonInstance.

         Contains a unique identifier for an object.    # noqa: E501

        :param season: The season of this SeasonInstance.
        :type season: str
        """
        if season is not None and len(season) > 250:
            raise ValueError("Invalid value for `season`, length must be less than or equal to `250`")  # noqa: E501
        if season is not None and not re.search(r'^(.){0,250}$', season):  # noqa: E501
            raise ValueError("Invalid value for `season`, must be a follow pattern or equal to `/^(.){0,250}$/`")  # noqa: E501

        self._season = season

    @property
    def id(self) -> str:
        """Gets the id of this SeasonInstance.

         Contains a unique identifier for an object.    # noqa: E501

        :return: The id of this SeasonInstance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this SeasonInstance.

         Contains a unique identifier for an object.    # noqa: E501

        :param id: The id of this SeasonInstance.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if id is not None and len(id) > 250:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `250`")  # noqa: E501
        if id is not None and not re.search(r'^(.){0,250}$', id):  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a follow pattern or equal to `/^(.){0,250}$/`")  # noqa: E501

        self._id = id

    @property
    def effective_time(self) -> datetime:
        """Gets the effective_time of this SeasonInstance.

         RFC 3339 date-time string with *no fractional seconds component* that designates a start or end to an operating period (such as an hour) that starts at a specified time. This will frequently be at the start of an hour, but may be finer-grained, such as every 30 minutes, should the Clearinghouse Provider choose.  If the Transmission Provider is operating in EST, these are valid and equivalent values:  * 2023-01-01T06:00Z * 2023-01-01T01:00-5:00 * 2023-01-01T00:00-6:00 * 2023-01-01T11:30+5:30  The server should uniformly represent date-times in the operational time zone of the Clearinghouse Provider.   # noqa: E501

        :return: The effective_time of this SeasonInstance.
        :rtype: datetime
        """
        return self._effective_time

    @effective_time.setter
    def effective_time(self, effective_time: datetime):
        """Sets the effective_time of this SeasonInstance.

         RFC 3339 date-time string with *no fractional seconds component* that designates a start or end to an operating period (such as an hour) that starts at a specified time. This will frequently be at the start of an hour, but may be finer-grained, such as every 30 minutes, should the Clearinghouse Provider choose.  If the Transmission Provider is operating in EST, these are valid and equivalent values:  * 2023-01-01T06:00Z * 2023-01-01T01:00-5:00 * 2023-01-01T00:00-6:00 * 2023-01-01T11:30+5:30  The server should uniformly represent date-times in the operational time zone of the Clearinghouse Provider.   # noqa: E501

        :param effective_time: The effective_time of this SeasonInstance.
        :type effective_time: datetime
        """
        if effective_time is not None and len(effective_time) > 25:
            raise ValueError("Invalid value for `effective_time`, length must be less than or equal to `25`")  # noqa: E501

        self._effective_time = effective_time

    @property
    def active(self) -> bool:
        """Gets the active of this SeasonInstance.

        Set to true if this season is currently active  # noqa: E501

        :return: The active of this SeasonInstance.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active: bool):
        """Sets the active of this SeasonInstance.

        Set to true if this season is currently active  # noqa: E501

        :param active: The active of this SeasonInstance.
        :type active: bool
        """
        if active is None:
            raise ValueError("Invalid value for `active`, must not be `None`")  # noqa: E501

        self._active = active
