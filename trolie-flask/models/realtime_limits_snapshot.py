from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from trolie-flask.models.base_model import Model
from trolie-flask.models.real_time_snapshot_header import RealTimeSnapshotHeader
from trolie-flask.models.realtime_limit_item import RealtimeLimitItem
from trolie-flask import util

from trolie-flask.models.real_time_snapshot_header import RealTimeSnapshotHeader  # noqa: E501
from trolie-flask.models.realtime_limit_item import RealtimeLimitItem  # noqa: E501

class RealtimeLimitsSnapshot(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, snapshot_header=None, limits=None):  # noqa: E501
        """RealtimeLimitsSnapshot - a model defined in OpenAPI

        :param snapshot_header: The snapshot_header of this RealtimeLimitsSnapshot.  # noqa: E501
        :type snapshot_header: RealTimeSnapshotHeader
        :param limits: The limits of this RealtimeLimitsSnapshot.  # noqa: E501
        :type limits: List[RealtimeLimitItem]
        """
        self.openapi_types = {
            'snapshot_header': RealTimeSnapshotHeader,
            'limits': List[RealtimeLimitItem]
        }

        self.attribute_map = {
            'snapshot_header': 'snapshot-header',
            'limits': 'limits'
        }

        self._snapshot_header = snapshot_header
        self._limits = limits

    @classmethod
    def from_dict(cls, dikt) -> 'RealtimeLimitsSnapshot':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The realtime-limits-snapshot of this RealtimeLimitsSnapshot.  # noqa: E501
        :rtype: RealtimeLimitsSnapshot
        """
        return util.deserialize_model(dikt, cls)

    @property
    def snapshot_header(self) -> RealTimeSnapshotHeader:
        """Gets the snapshot_header of this RealtimeLimitsSnapshot.


        :return: The snapshot_header of this RealtimeLimitsSnapshot.
        :rtype: RealTimeSnapshotHeader
        """
        return self._snapshot_header

    @snapshot_header.setter
    def snapshot_header(self, snapshot_header: RealTimeSnapshotHeader):
        """Sets the snapshot_header of this RealtimeLimitsSnapshot.


        :param snapshot_header: The snapshot_header of this RealtimeLimitsSnapshot.
        :type snapshot_header: RealTimeSnapshotHeader
        """

        self._snapshot_header = snapshot_header

    @property
    def limits(self) -> List[RealtimeLimitItem]:
        """Gets the limits of this RealtimeLimitsSnapshot.

        Real-time limits  # noqa: E501

        :return: The limits of this RealtimeLimitsSnapshot.
        :rtype: List[RealtimeLimitItem]
        """
        return self._limits

    @limits.setter
    def limits(self, limits: List[RealtimeLimitItem]):
        """Sets the limits of this RealtimeLimitsSnapshot.

        Real-time limits  # noqa: E501

        :param limits: The limits of this RealtimeLimitsSnapshot.
        :type limits: List[RealtimeLimitItem]
        """
        if limits is not None and len(limits) > 50000:
            raise ValueError("Invalid value for `limits`, number of items must be less than or equal to `50000`")  # noqa: E501
        if limits is not None and len(limits) < 0:
            raise ValueError("Invalid value for `limits`, number of items must be greater than or equal to `0`")  # noqa: E501

        self._limits = limits
