from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from trolie-flask.models.base_model import Model
from trolie-flask.models.data_provenance import DataProvenance
from trolie-flask.models.emergency_durations_inner import EmergencyDurationsInner
from trolie-flask.models.names import Names
from trolie-flask import util

from trolie-flask.models.data_provenance import DataProvenance  # noqa: E501
from trolie-flask.models.emergency_durations_inner import EmergencyDurationsInner  # noqa: E501
from trolie-flask.models.names import Names  # noqa: E501

class CommonHeader(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, source=None, default_emergency_durations=None, power_system_resources=None):  # noqa: E501
        """CommonHeader - a model defined in OpenAPI

        :param source: The source of this CommonHeader.  # noqa: E501
        :type source: DataProvenance
        :param default_emergency_durations: The default_emergency_durations of this CommonHeader.  # noqa: E501
        :type default_emergency_durations: List[EmergencyDurationsInner]
        :param power_system_resources: The power_system_resources of this CommonHeader.  # noqa: E501
        :type power_system_resources: List[Names]
        """
        self.openapi_types = {
            'source': DataProvenance,
            'default_emergency_durations': List[EmergencyDurationsInner],
            'power_system_resources': List[Names]
        }

        self.attribute_map = {
            'source': 'source',
            'default_emergency_durations': 'default-emergency-durations',
            'power_system_resources': 'power-system-resources'
        }

        self._source = source
        self._default_emergency_durations = default_emergency_durations
        self._power_system_resources = power_system_resources

    @classmethod
    def from_dict(cls, dikt) -> 'CommonHeader':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The common-header of this CommonHeader.  # noqa: E501
        :rtype: CommonHeader
        """
        return util.deserialize_model(dikt, cls)

    @property
    def source(self) -> DataProvenance:
        """Gets the source of this CommonHeader.


        :return: The source of this CommonHeader.
        :rtype: DataProvenance
        """
        return self._source

    @source.setter
    def source(self, source: DataProvenance):
        """Sets the source of this CommonHeader.


        :param source: The source of this CommonHeader.
        :type source: DataProvenance
        """
        if source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    @property
    def default_emergency_durations(self) -> List[EmergencyDurationsInner]:
        """Gets the default_emergency_durations of this CommonHeader.

        Defines the durations in minutes used for emergency limits.  # noqa: E501

        :return: The default_emergency_durations of this CommonHeader.
        :rtype: List[EmergencyDurationsInner]
        """
        return self._default_emergency_durations

    @default_emergency_durations.setter
    def default_emergency_durations(self, default_emergency_durations: List[EmergencyDurationsInner]):
        """Sets the default_emergency_durations of this CommonHeader.

        Defines the durations in minutes used for emergency limits.  # noqa: E501

        :param default_emergency_durations: The default_emergency_durations of this CommonHeader.
        :type default_emergency_durations: List[EmergencyDurationsInner]
        """
        if default_emergency_durations is None:
            raise ValueError("Invalid value for `default_emergency_durations`, must not be `None`")  # noqa: E501
        if default_emergency_durations is not None and len(default_emergency_durations) > 10:
            raise ValueError("Invalid value for `default_emergency_durations`, number of items must be less than or equal to `10`")  # noqa: E501
        if default_emergency_durations is not None and len(default_emergency_durations) < 1:
            raise ValueError("Invalid value for `default_emergency_durations`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._default_emergency_durations = default_emergency_durations

    @property
    def power_system_resources(self) -> List[Names]:
        """Gets the power_system_resources of this CommonHeader.

        Collection of power system resource names  # noqa: E501

        :return: The power_system_resources of this CommonHeader.
        :rtype: List[Names]
        """
        return self._power_system_resources

    @power_system_resources.setter
    def power_system_resources(self, power_system_resources: List[Names]):
        """Sets the power_system_resources of this CommonHeader.

        Collection of power system resource names  # noqa: E501

        :param power_system_resources: The power_system_resources of this CommonHeader.
        :type power_system_resources: List[Names]
        """
        if power_system_resources is None:
            raise ValueError("Invalid value for `power_system_resources`, must not be `None`")  # noqa: E501
        if power_system_resources is not None and len(power_system_resources) > 50000:
            raise ValueError("Invalid value for `power_system_resources`, number of items must be less than or equal to `50000`")  # noqa: E501
        if power_system_resources is not None and len(power_system_resources) < 0:
            raise ValueError("Invalid value for `power_system_resources`, number of items must be greater than or equal to `0`")  # noqa: E501

        self._power_system_resources = power_system_resources
