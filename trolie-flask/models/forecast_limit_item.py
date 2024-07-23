from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.snapshot_slim import SnapshotSlim
import re
from openapi_server import util

from openapi_server.models.snapshot_slim import SnapshotSlim  # noqa: E501
import re  # noqa: E501

class ForecastLimitItem(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, resource_id=None, periods=None):  # noqa: E501
        """ForecastLimitItem - a model defined in OpenAPI

        :param resource_id: The resource_id of this ForecastLimitItem.  # noqa: E501
        :type resource_id: str
        :param periods: The periods of this ForecastLimitItem.  # noqa: E501
        :type periods: List[SnapshotSlim]
        """
        self.openapi_types = {
            'resource_id': str,
            'periods': List[SnapshotSlim]
        }

        self.attribute_map = {
            'resource_id': 'resource-id',
            'periods': 'periods'
        }

        self._resource_id = resource_id
        self._periods = periods

    @classmethod
    def from_dict(cls, dikt) -> 'ForecastLimitItem':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The forecast-limit-item of this ForecastLimitItem.  # noqa: E501
        :rtype: ForecastLimitItem
        """
        return util.deserialize_model(dikt, cls)

    @property
    def resource_id(self) -> str:
        """Gets the resource_id of this ForecastLimitItem.

         Contains a unique identifier for an a power system resources, such as a transmission facility, segment, interface, etc.    # noqa: E501

        :return: The resource_id of this ForecastLimitItem.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id: str):
        """Sets the resource_id of this ForecastLimitItem.

         Contains a unique identifier for an a power system resources, such as a transmission facility, segment, interface, etc.    # noqa: E501

        :param resource_id: The resource_id of this ForecastLimitItem.
        :type resource_id: str
        """
        if resource_id is None:
            raise ValueError("Invalid value for `resource_id`, must not be `None`")  # noqa: E501
        if resource_id is not None and len(resource_id) > 250:
            raise ValueError("Invalid value for `resource_id`, length must be less than or equal to `250`")  # noqa: E501
        if resource_id is not None and not re.search(r'^(.){0,250}$', resource_id):  # noqa: E501
            raise ValueError("Invalid value for `resource_id`, must be a follow pattern or equal to `/^(.){0,250}$/`")  # noqa: E501

        self._resource_id = resource_id

    @property
    def periods(self) -> List[SnapshotSlim]:
        """Gets the periods of this ForecastLimitItem.


        :return: The periods of this ForecastLimitItem.
        :rtype: List[SnapshotSlim]
        """
        return self._periods

    @periods.setter
    def periods(self, periods: List[SnapshotSlim]):
        """Sets the periods of this ForecastLimitItem.


        :param periods: The periods of this ForecastLimitItem.
        :type periods: List[SnapshotSlim]
        """
        if periods is None:
            raise ValueError("Invalid value for `periods`, must not be `None`")  # noqa: E501
        if periods is not None and len(periods) > 240:
            raise ValueError("Invalid value for `periods`, number of items must be less than or equal to `240`")  # noqa: E501

        self._periods = periods
