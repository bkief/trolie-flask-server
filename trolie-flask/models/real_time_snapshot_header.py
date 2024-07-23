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

class RealTimeSnapshotHeader(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, last_updated=None, snapshot_provenance=None, power_system_resources=None, default_emergency_durations=None):  # noqa: E501
        """RealTimeSnapshotHeader - a model defined in OpenAPI

        :param last_updated: The last_updated of this RealTimeSnapshotHeader.  # noqa: E501
        :type last_updated: datetime
        :param snapshot_provenance: The snapshot_provenance of this RealTimeSnapshotHeader.  # noqa: E501
        :type snapshot_provenance: DataProvenance
        :param power_system_resources: The power_system_resources of this RealTimeSnapshotHeader.  # noqa: E501
        :type power_system_resources: List[Names]
        :param default_emergency_durations: The default_emergency_durations of this RealTimeSnapshotHeader.  # noqa: E501
        :type default_emergency_durations: List[EmergencyDurationsInner]
        """
        self.openapi_types = {
            'last_updated': datetime,
            'snapshot_provenance': DataProvenance,
            'power_system_resources': List[Names],
            'default_emergency_durations': List[EmergencyDurationsInner]
        }

        self.attribute_map = {
            'last_updated': 'last-updated',
            'snapshot_provenance': 'snapshot-provenance',
            'power_system_resources': 'power-system-resources',
            'default_emergency_durations': 'default-emergency-durations'
        }

        self._last_updated = last_updated
        self._snapshot_provenance = snapshot_provenance
        self._power_system_resources = power_system_resources
        self._default_emergency_durations = default_emergency_durations

    @classmethod
    def from_dict(cls, dikt) -> 'RealTimeSnapshotHeader':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The real-time-snapshot-header of this RealTimeSnapshotHeader.  # noqa: E501
        :rtype: RealTimeSnapshotHeader
        """
        return util.deserialize_model(dikt, cls)

    @property
    def last_updated(self) -> datetime:
        """Gets the last_updated of this RealTimeSnapshotHeader.

        RFC 3339 date-time string with a maximum of 10 digits in the fractional seconds component, i.e., nanosecond precision.  # noqa: E501

        :return: The last_updated of this RealTimeSnapshotHeader.
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated: datetime):
        """Sets the last_updated of this RealTimeSnapshotHeader.

        RFC 3339 date-time string with a maximum of 10 digits in the fractional seconds component, i.e., nanosecond precision.  # noqa: E501

        :param last_updated: The last_updated of this RealTimeSnapshotHeader.
        :type last_updated: datetime
        """
        if last_updated is None:
            raise ValueError("Invalid value for `last_updated`, must not be `None`")  # noqa: E501
        if last_updated is not None and len(last_updated) > 35:
            raise ValueError("Invalid value for `last_updated`, length must be less than or equal to `35`")  # noqa: E501

        self._last_updated = last_updated

    @property
    def snapshot_provenance(self) -> DataProvenance:
        """Gets the snapshot_provenance of this RealTimeSnapshotHeader.


        :return: The snapshot_provenance of this RealTimeSnapshotHeader.
        :rtype: DataProvenance
        """
        return self._snapshot_provenance

    @snapshot_provenance.setter
    def snapshot_provenance(self, snapshot_provenance: DataProvenance):
        """Sets the snapshot_provenance of this RealTimeSnapshotHeader.


        :param snapshot_provenance: The snapshot_provenance of this RealTimeSnapshotHeader.
        :type snapshot_provenance: DataProvenance
        """
        if snapshot_provenance is None:
            raise ValueError("Invalid value for `snapshot_provenance`, must not be `None`")  # noqa: E501

        self._snapshot_provenance = snapshot_provenance

    @property
    def power_system_resources(self) -> List[Names]:
        """Gets the power_system_resources of this RealTimeSnapshotHeader.

        Collection of power system resource names  # noqa: E501

        :return: The power_system_resources of this RealTimeSnapshotHeader.
        :rtype: List[Names]
        """
        return self._power_system_resources

    @power_system_resources.setter
    def power_system_resources(self, power_system_resources: List[Names]):
        """Sets the power_system_resources of this RealTimeSnapshotHeader.

        Collection of power system resource names  # noqa: E501

        :param power_system_resources: The power_system_resources of this RealTimeSnapshotHeader.
        :type power_system_resources: List[Names]
        """
        if power_system_resources is None:
            raise ValueError("Invalid value for `power_system_resources`, must not be `None`")  # noqa: E501
        if power_system_resources is not None and len(power_system_resources) > 50000:
            raise ValueError("Invalid value for `power_system_resources`, number of items must be less than or equal to `50000`")  # noqa: E501
        if power_system_resources is not None and len(power_system_resources) < 0:
            raise ValueError("Invalid value for `power_system_resources`, number of items must be greater than or equal to `0`")  # noqa: E501

        self._power_system_resources = power_system_resources

    @property
    def default_emergency_durations(self) -> List[EmergencyDurationsInner]:
        """Gets the default_emergency_durations of this RealTimeSnapshotHeader.

        Defines the durations in minutes used for emergency limits.  # noqa: E501

        :return: The default_emergency_durations of this RealTimeSnapshotHeader.
        :rtype: List[EmergencyDurationsInner]
        """
        return self._default_emergency_durations

    @default_emergency_durations.setter
    def default_emergency_durations(self, default_emergency_durations: List[EmergencyDurationsInner]):
        """Sets the default_emergency_durations of this RealTimeSnapshotHeader.

        Defines the durations in minutes used for emergency limits.  # noqa: E501

        :param default_emergency_durations: The default_emergency_durations of this RealTimeSnapshotHeader.
        :type default_emergency_durations: List[EmergencyDurationsInner]
        """
        if default_emergency_durations is not None and len(default_emergency_durations) > 10:
            raise ValueError("Invalid value for `default_emergency_durations`, number of items must be less than or equal to `10`")  # noqa: E501
        if default_emergency_durations is not None and len(default_emergency_durations) < 1:
            raise ValueError("Invalid value for `default_emergency_durations`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._default_emergency_durations = default_emergency_durations
