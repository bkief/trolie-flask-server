from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.limit import Limit
from openapi_server.models.limit_value_set_inner import LimitValueSetInner
import re
from openapi_server import util

from openapi_server.models.limit import Limit  # noqa: E501
from openapi_server.models.limit_value_set_inner import LimitValueSetInner  # noqa: E501
import re  # noqa: E501

class RealtimeLimitItem(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, continuous_operating_limit=None, emergency_operating_limits=None, resource_id=None):  # noqa: E501
        """RealtimeLimitItem - a model defined in OpenAPI

        :param continuous_operating_limit: The continuous_operating_limit of this RealtimeLimitItem.  # noqa: E501
        :type continuous_operating_limit: Limit
        :param emergency_operating_limits: The emergency_operating_limits of this RealtimeLimitItem.  # noqa: E501
        :type emergency_operating_limits: List[LimitValueSetInner]
        :param resource_id: The resource_id of this RealtimeLimitItem.  # noqa: E501
        :type resource_id: str
        """
        self.openapi_types = {
            'continuous_operating_limit': Limit,
            'emergency_operating_limits': List[LimitValueSetInner],
            'resource_id': str
        }

        self.attribute_map = {
            'continuous_operating_limit': 'continuous-operating-limit',
            'emergency_operating_limits': 'emergency-operating-limits',
            'resource_id': 'resource-id'
        }

        self._continuous_operating_limit = continuous_operating_limit
        self._emergency_operating_limits = emergency_operating_limits
        self._resource_id = resource_id

    @classmethod
    def from_dict(cls, dikt) -> 'RealtimeLimitItem':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The realtime-limit-item of this RealtimeLimitItem.  # noqa: E501
        :rtype: RealtimeLimitItem
        """
        return util.deserialize_model(dikt, cls)

    @property
    def continuous_operating_limit(self) -> Limit:
        """Gets the continuous_operating_limit of this RealtimeLimitItem.


        :return: The continuous_operating_limit of this RealtimeLimitItem.
        :rtype: Limit
        """
        return self._continuous_operating_limit

    @continuous_operating_limit.setter
    def continuous_operating_limit(self, continuous_operating_limit: Limit):
        """Sets the continuous_operating_limit of this RealtimeLimitItem.


        :param continuous_operating_limit: The continuous_operating_limit of this RealtimeLimitItem.
        :type continuous_operating_limit: Limit
        """
        if continuous_operating_limit is None:
            raise ValueError("Invalid value for `continuous_operating_limit`, must not be `None`")  # noqa: E501

        self._continuous_operating_limit = continuous_operating_limit

    @property
    def emergency_operating_limits(self) -> List[LimitValueSetInner]:
        """Gets the emergency_operating_limits of this RealtimeLimitItem.

         A set of general limit or rating values, each mapped to the various limit bands defined by the Transmission Provider's operating manual. This typically consists of a \"normal\" limit, as well as limits for various levels of emergency conditions (typically 2-4) defined in the operations manual.   # noqa: E501

        :return: The emergency_operating_limits of this RealtimeLimitItem.
        :rtype: List[LimitValueSetInner]
        """
        return self._emergency_operating_limits

    @emergency_operating_limits.setter
    def emergency_operating_limits(self, emergency_operating_limits: List[LimitValueSetInner]):
        """Sets the emergency_operating_limits of this RealtimeLimitItem.

         A set of general limit or rating values, each mapped to the various limit bands defined by the Transmission Provider's operating manual. This typically consists of a \"normal\" limit, as well as limits for various levels of emergency conditions (typically 2-4) defined in the operations manual.   # noqa: E501

        :param emergency_operating_limits: The emergency_operating_limits of this RealtimeLimitItem.
        :type emergency_operating_limits: List[LimitValueSetInner]
        """
        if emergency_operating_limits is None:
            raise ValueError("Invalid value for `emergency_operating_limits`, must not be `None`")  # noqa: E501
        if emergency_operating_limits is not None and len(emergency_operating_limits) > 10:
            raise ValueError("Invalid value for `emergency_operating_limits`, number of items must be less than or equal to `10`")  # noqa: E501
        if emergency_operating_limits is not None and len(emergency_operating_limits) < 1:
            raise ValueError("Invalid value for `emergency_operating_limits`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._emergency_operating_limits = emergency_operating_limits

    @property
    def resource_id(self) -> str:
        """Gets the resource_id of this RealtimeLimitItem.

         Contains a unique identifier for an a power system resources, such as a transmission facility, segment, interface, etc.    # noqa: E501

        :return: The resource_id of this RealtimeLimitItem.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id: str):
        """Sets the resource_id of this RealtimeLimitItem.

         Contains a unique identifier for an a power system resources, such as a transmission facility, segment, interface, etc.    # noqa: E501

        :param resource_id: The resource_id of this RealtimeLimitItem.
        :type resource_id: str
        """
        if resource_id is None:
            raise ValueError("Invalid value for `resource_id`, must not be `None`")  # noqa: E501
        if resource_id is not None and len(resource_id) > 250:
            raise ValueError("Invalid value for `resource_id`, length must be less than or equal to `250`")  # noqa: E501
        if resource_id is not None and not re.search(r'^(.){0,250}$', resource_id):  # noqa: E501
            raise ValueError("Invalid value for `resource_id`, must be a follow pattern or equal to `/^(.){0,250}$/`")  # noqa: E501

        self._resource_id = resource_id
