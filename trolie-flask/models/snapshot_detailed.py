from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.limit import Limit
from openapi_server.models.limit_provenance_overrides_inner import LimitProvenanceOverridesInner
from openapi_server.models.limit_provenance_proposals_considered_inner import LimitProvenanceProposalsConsideredInner
from openapi_server.models.limit_value_set_inner import LimitValueSetInner
from openapi_server import util

from openapi_server.models.limit import Limit  # noqa: E501
from openapi_server.models.limit_provenance_overrides_inner import LimitProvenanceOverridesInner  # noqa: E501
from openapi_server.models.limit_provenance_proposals_considered_inner import LimitProvenanceProposalsConsideredInner  # noqa: E501
from openapi_server.models.limit_value_set_inner import LimitValueSetInner  # noqa: E501

class SnapshotDetailed(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, period_start=None, period_end=None, continuous_operating_limit=None, emergency_operating_limits=None, proposals_considered=None, temporary_aar_exceptions=None, overrides=None, additional_data=None):  # noqa: E501
        """SnapshotDetailed - a model defined in OpenAPI

        :param period_start: The period_start of this SnapshotDetailed.  # noqa: E501
        :type period_start: datetime
        :param period_end: The period_end of this SnapshotDetailed.  # noqa: E501
        :type period_end: datetime
        :param continuous_operating_limit: The continuous_operating_limit of this SnapshotDetailed.  # noqa: E501
        :type continuous_operating_limit: Limit
        :param emergency_operating_limits: The emergency_operating_limits of this SnapshotDetailed.  # noqa: E501
        :type emergency_operating_limits: List[LimitValueSetInner]
        :param proposals_considered: The proposals_considered of this SnapshotDetailed.  # noqa: E501
        :type proposals_considered: List[LimitProvenanceProposalsConsideredInner]
        :param temporary_aar_exceptions: The temporary_aar_exceptions of this SnapshotDetailed.  # noqa: E501
        :type temporary_aar_exceptions: List[str]
        :param overrides: The overrides of this SnapshotDetailed.  # noqa: E501
        :type overrides: List[LimitProvenanceOverridesInner]
        :param additional_data: The additional_data of this SnapshotDetailed.  # noqa: E501
        :type additional_data: object
        """
        self.openapi_types = {
            'period_start': datetime,
            'period_end': datetime,
            'continuous_operating_limit': Limit,
            'emergency_operating_limits': List[LimitValueSetInner],
            'proposals_considered': List[LimitProvenanceProposalsConsideredInner],
            'temporary_aar_exceptions': List[str],
            'overrides': List[LimitProvenanceOverridesInner],
            'additional_data': object
        }

        self.attribute_map = {
            'period_start': 'period-start',
            'period_end': 'period-end',
            'continuous_operating_limit': 'continuous-operating-limit',
            'emergency_operating_limits': 'emergency-operating-limits',
            'proposals_considered': 'proposals-considered',
            'temporary_aar_exceptions': 'temporary-aar-exceptions',
            'overrides': 'overrides',
            'additional_data': 'additional-data'
        }

        self._period_start = period_start
        self._period_end = period_end
        self._continuous_operating_limit = continuous_operating_limit
        self._emergency_operating_limits = emergency_operating_limits
        self._proposals_considered = proposals_considered
        self._temporary_aar_exceptions = temporary_aar_exceptions
        self._overrides = overrides
        self._additional_data = additional_data

    @classmethod
    def from_dict(cls, dikt) -> 'SnapshotDetailed':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The snapshot-detailed of this SnapshotDetailed.  # noqa: E501
        :rtype: SnapshotDetailed
        """
        return util.deserialize_model(dikt, cls)

    @property
    def period_start(self) -> datetime:
        """Gets the period_start of this SnapshotDetailed.

         RFC 3339 date-time string with *no fractional seconds component* that designates a start or end to an operating period (such as an hour) that starts at a specified time. This will frequently be at the start of an hour, but may be finer-grained, such as every 30 minutes, should the Clearinghouse Provider choose.  If the Transmission Provider is operating in EST, these are valid and equivalent values:  * 2023-01-01T06:00Z * 2023-01-01T01:00-5:00 * 2023-01-01T00:00-6:00 * 2023-01-01T11:30+5:30  The server should uniformly represent date-times in the operational time zone of the Clearinghouse Provider.   # noqa: E501

        :return: The period_start of this SnapshotDetailed.
        :rtype: datetime
        """
        return self._period_start

    @period_start.setter
    def period_start(self, period_start: datetime):
        """Sets the period_start of this SnapshotDetailed.

         RFC 3339 date-time string with *no fractional seconds component* that designates a start or end to an operating period (such as an hour) that starts at a specified time. This will frequently be at the start of an hour, but may be finer-grained, such as every 30 minutes, should the Clearinghouse Provider choose.  If the Transmission Provider is operating in EST, these are valid and equivalent values:  * 2023-01-01T06:00Z * 2023-01-01T01:00-5:00 * 2023-01-01T00:00-6:00 * 2023-01-01T11:30+5:30  The server should uniformly represent date-times in the operational time zone of the Clearinghouse Provider.   # noqa: E501

        :param period_start: The period_start of this SnapshotDetailed.
        :type period_start: datetime
        """
        if period_start is None:
            raise ValueError("Invalid value for `period_start`, must not be `None`")  # noqa: E501
        if period_start is not None and len(period_start) > 25:
            raise ValueError("Invalid value for `period_start`, length must be less than or equal to `25`")  # noqa: E501

        self._period_start = period_start

    @property
    def period_end(self) -> datetime:
        """Gets the period_end of this SnapshotDetailed.

         RFC 3339 date-time string with *no fractional seconds component* that designates a start or end to an operating period (such as an hour) that starts at a specified time. This will frequently be at the start of an hour, but may be finer-grained, such as every 30 minutes, should the Clearinghouse Provider choose.  If the Transmission Provider is operating in EST, these are valid and equivalent values:  * 2023-01-01T06:00Z * 2023-01-01T01:00-5:00 * 2023-01-01T00:00-6:00 * 2023-01-01T11:30+5:30  The server should uniformly represent date-times in the operational time zone of the Clearinghouse Provider.   # noqa: E501

        :return: The period_end of this SnapshotDetailed.
        :rtype: datetime
        """
        return self._period_end

    @period_end.setter
    def period_end(self, period_end: datetime):
        """Sets the period_end of this SnapshotDetailed.

         RFC 3339 date-time string with *no fractional seconds component* that designates a start or end to an operating period (such as an hour) that starts at a specified time. This will frequently be at the start of an hour, but may be finer-grained, such as every 30 minutes, should the Clearinghouse Provider choose.  If the Transmission Provider is operating in EST, these are valid and equivalent values:  * 2023-01-01T06:00Z * 2023-01-01T01:00-5:00 * 2023-01-01T00:00-6:00 * 2023-01-01T11:30+5:30  The server should uniformly represent date-times in the operational time zone of the Clearinghouse Provider.   # noqa: E501

        :param period_end: The period_end of this SnapshotDetailed.
        :type period_end: datetime
        """
        if period_end is None:
            raise ValueError("Invalid value for `period_end`, must not be `None`")  # noqa: E501
        if period_end is not None and len(period_end) > 25:
            raise ValueError("Invalid value for `period_end`, length must be less than or equal to `25`")  # noqa: E501

        self._period_end = period_end

    @property
    def continuous_operating_limit(self) -> Limit:
        """Gets the continuous_operating_limit of this SnapshotDetailed.


        :return: The continuous_operating_limit of this SnapshotDetailed.
        :rtype: Limit
        """
        return self._continuous_operating_limit

    @continuous_operating_limit.setter
    def continuous_operating_limit(self, continuous_operating_limit: Limit):
        """Sets the continuous_operating_limit of this SnapshotDetailed.


        :param continuous_operating_limit: The continuous_operating_limit of this SnapshotDetailed.
        :type continuous_operating_limit: Limit
        """
        if continuous_operating_limit is None:
            raise ValueError("Invalid value for `continuous_operating_limit`, must not be `None`")  # noqa: E501

        self._continuous_operating_limit = continuous_operating_limit

    @property
    def emergency_operating_limits(self) -> List[LimitValueSetInner]:
        """Gets the emergency_operating_limits of this SnapshotDetailed.

         A set of general limit or rating values, each mapped to the various limit bands defined by the Transmission Provider's operating manual. This typically consists of a \"normal\" limit, as well as limits for various levels of emergency conditions (typically 2-4) defined in the operations manual.   # noqa: E501

        :return: The emergency_operating_limits of this SnapshotDetailed.
        :rtype: List[LimitValueSetInner]
        """
        return self._emergency_operating_limits

    @emergency_operating_limits.setter
    def emergency_operating_limits(self, emergency_operating_limits: List[LimitValueSetInner]):
        """Sets the emergency_operating_limits of this SnapshotDetailed.

         A set of general limit or rating values, each mapped to the various limit bands defined by the Transmission Provider's operating manual. This typically consists of a \"normal\" limit, as well as limits for various levels of emergency conditions (typically 2-4) defined in the operations manual.   # noqa: E501

        :param emergency_operating_limits: The emergency_operating_limits of this SnapshotDetailed.
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
    def proposals_considered(self) -> List[LimitProvenanceProposalsConsideredInner]:
        """Gets the proposals_considered of this SnapshotDetailed.

         The forecast proposals provided by the Ratings Providers during the Forecast Window for this limits snapshot.   # noqa: E501

        :return: The proposals_considered of this SnapshotDetailed.
        :rtype: List[LimitProvenanceProposalsConsideredInner]
        """
        return self._proposals_considered

    @proposals_considered.setter
    def proposals_considered(self, proposals_considered: List[LimitProvenanceProposalsConsideredInner]):
        """Sets the proposals_considered of this SnapshotDetailed.

         The forecast proposals provided by the Ratings Providers during the Forecast Window for this limits snapshot.   # noqa: E501

        :param proposals_considered: The proposals_considered of this SnapshotDetailed.
        :type proposals_considered: List[LimitProvenanceProposalsConsideredInner]
        """
        if proposals_considered is None:
            raise ValueError("Invalid value for `proposals_considered`, must not be `None`")  # noqa: E501
        if proposals_considered is not None and len(proposals_considered) > 10:
            raise ValueError("Invalid value for `proposals_considered`, number of items must be less than or equal to `10`")  # noqa: E501

        self._proposals_considered = proposals_considered

    @property
    def temporary_aar_exceptions(self) -> List[str]:
        """Gets the temporary_aar_exceptions of this SnapshotDetailed.

         The temporary AAR exceptions for the facility that were active when this snapshot was generated.   # noqa: E501

        :return: The temporary_aar_exceptions of this SnapshotDetailed.
        :rtype: List[str]
        """
        return self._temporary_aar_exceptions

    @temporary_aar_exceptions.setter
    def temporary_aar_exceptions(self, temporary_aar_exceptions: List[str]):
        """Sets the temporary_aar_exceptions of this SnapshotDetailed.

         The temporary AAR exceptions for the facility that were active when this snapshot was generated.   # noqa: E501

        :param temporary_aar_exceptions: The temporary_aar_exceptions of this SnapshotDetailed.
        :type temporary_aar_exceptions: List[str]
        """
        if temporary_aar_exceptions is not None and len(temporary_aar_exceptions) > 10:
            raise ValueError("Invalid value for `temporary_aar_exceptions`, number of items must be less than or equal to `10`")  # noqa: E501

        self._temporary_aar_exceptions = temporary_aar_exceptions

    @property
    def overrides(self) -> List[LimitProvenanceOverridesInner]:
        """Gets the overrides of this SnapshotDetailed.


        :return: The overrides of this SnapshotDetailed.
        :rtype: List[LimitProvenanceOverridesInner]
        """
        return self._overrides

    @overrides.setter
    def overrides(self, overrides: List[LimitProvenanceOverridesInner]):
        """Sets the overrides of this SnapshotDetailed.


        :param overrides: The overrides of this SnapshotDetailed.
        :type overrides: List[LimitProvenanceOverridesInner]
        """
        if overrides is not None and len(overrides) > 10:
            raise ValueError("Invalid value for `overrides`, number of items must be less than or equal to `10`")  # noqa: E501
        if overrides is not None and len(overrides) < 0:
            raise ValueError("Invalid value for `overrides`, number of items must be greater than or equal to `0`")  # noqa: E501

        self._overrides = overrides

    @property
    def additional_data(self) -> object:
        """Gets the additional_data of this SnapshotDetailed.

         Implementors may use this object to provide freeform extensions with additional traceability / provenance data to be included with the limit. Schema of this object is out of scope of the TROLIE specification.   # noqa: E501

        :return: The additional_data of this SnapshotDetailed.
        :rtype: object
        """
        return self._additional_data

    @additional_data.setter
    def additional_data(self, additional_data: object):
        """Sets the additional_data of this SnapshotDetailed.

         Implementors may use this object to provide freeform extensions with additional traceability / provenance data to be included with the limit. Schema of this object is out of scope of the TROLIE specification.   # noqa: E501

        :param additional_data: The additional_data of this SnapshotDetailed.
        :type additional_data: object
        """

        self._additional_data = additional_data
