from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.limit import Limit
from openapi_server.models.limit_proposal_all_of_inputs_used import LimitProposalAllOfInputsUsed
from openapi_server.models.limit_value_set_inner import LimitValueSetInner
from openapi_server import util

from openapi_server.models.limit import Limit  # noqa: E501
from openapi_server.models.limit_proposal_all_of_inputs_used import LimitProposalAllOfInputsUsed  # noqa: E501
from openapi_server.models.limit_value_set_inner import LimitValueSetInner  # noqa: E501

class Proposal(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, period_start=None, period_end=None, continuous_operating_limit=None, emergency_operating_limits=None, inputs_used=None):  # noqa: E501
        """Proposal - a model defined in OpenAPI

        :param period_start: The period_start of this Proposal.  # noqa: E501
        :type period_start: datetime
        :param period_end: The period_end of this Proposal.  # noqa: E501
        :type period_end: datetime
        :param continuous_operating_limit: The continuous_operating_limit of this Proposal.  # noqa: E501
        :type continuous_operating_limit: Limit
        :param emergency_operating_limits: The emergency_operating_limits of this Proposal.  # noqa: E501
        :type emergency_operating_limits: List[LimitValueSetInner]
        :param inputs_used: The inputs_used of this Proposal.  # noqa: E501
        :type inputs_used: List[LimitProposalAllOfInputsUsed]
        """
        self.openapi_types = {
            'period_start': datetime,
            'period_end': datetime,
            'continuous_operating_limit': Limit,
            'emergency_operating_limits': List[LimitValueSetInner],
            'inputs_used': List[LimitProposalAllOfInputsUsed]
        }

        self.attribute_map = {
            'period_start': 'period-start',
            'period_end': 'period-end',
            'continuous_operating_limit': 'continuous-operating-limit',
            'emergency_operating_limits': 'emergency-operating-limits',
            'inputs_used': 'inputs-used'
        }

        self._period_start = period_start
        self._period_end = period_end
        self._continuous_operating_limit = continuous_operating_limit
        self._emergency_operating_limits = emergency_operating_limits
        self._inputs_used = inputs_used

    @classmethod
    def from_dict(cls, dikt) -> 'Proposal':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The proposal of this Proposal.  # noqa: E501
        :rtype: Proposal
        """
        return util.deserialize_model(dikt, cls)

    @property
    def period_start(self) -> datetime:
        """Gets the period_start of this Proposal.

         RFC 3339 date-time string with *no fractional seconds component* that designates a start or end to an operating period (such as an hour) that starts at a specified time. This will frequently be at the start of an hour, but may be finer-grained, such as every 30 minutes, should the Clearinghouse Provider choose.  If the Transmission Provider is operating in EST, these are valid and equivalent values:  * 2023-01-01T06:00Z * 2023-01-01T01:00-5:00 * 2023-01-01T00:00-6:00 * 2023-01-01T11:30+5:30  The server should uniformly represent date-times in the operational time zone of the Clearinghouse Provider.   # noqa: E501

        :return: The period_start of this Proposal.
        :rtype: datetime
        """
        return self._period_start

    @period_start.setter
    def period_start(self, period_start: datetime):
        """Sets the period_start of this Proposal.

         RFC 3339 date-time string with *no fractional seconds component* that designates a start or end to an operating period (such as an hour) that starts at a specified time. This will frequently be at the start of an hour, but may be finer-grained, such as every 30 minutes, should the Clearinghouse Provider choose.  If the Transmission Provider is operating in EST, these are valid and equivalent values:  * 2023-01-01T06:00Z * 2023-01-01T01:00-5:00 * 2023-01-01T00:00-6:00 * 2023-01-01T11:30+5:30  The server should uniformly represent date-times in the operational time zone of the Clearinghouse Provider.   # noqa: E501

        :param period_start: The period_start of this Proposal.
        :type period_start: datetime
        """
        if period_start is None:
            raise ValueError("Invalid value for `period_start`, must not be `None`")  # noqa: E501
        if period_start is not None and len(period_start) > 25:
            raise ValueError("Invalid value for `period_start`, length must be less than or equal to `25`")  # noqa: E501

        self._period_start = period_start

    @property
    def period_end(self) -> datetime:
        """Gets the period_end of this Proposal.

         RFC 3339 date-time string with *no fractional seconds component* that designates a start or end to an operating period (such as an hour) that starts at a specified time. This will frequently be at the start of an hour, but may be finer-grained, such as every 30 minutes, should the Clearinghouse Provider choose.  If the Transmission Provider is operating in EST, these are valid and equivalent values:  * 2023-01-01T06:00Z * 2023-01-01T01:00-5:00 * 2023-01-01T00:00-6:00 * 2023-01-01T11:30+5:30  The server should uniformly represent date-times in the operational time zone of the Clearinghouse Provider.   # noqa: E501

        :return: The period_end of this Proposal.
        :rtype: datetime
        """
        return self._period_end

    @period_end.setter
    def period_end(self, period_end: datetime):
        """Sets the period_end of this Proposal.

         RFC 3339 date-time string with *no fractional seconds component* that designates a start or end to an operating period (such as an hour) that starts at a specified time. This will frequently be at the start of an hour, but may be finer-grained, such as every 30 minutes, should the Clearinghouse Provider choose.  If the Transmission Provider is operating in EST, these are valid and equivalent values:  * 2023-01-01T06:00Z * 2023-01-01T01:00-5:00 * 2023-01-01T00:00-6:00 * 2023-01-01T11:30+5:30  The server should uniformly represent date-times in the operational time zone of the Clearinghouse Provider.   # noqa: E501

        :param period_end: The period_end of this Proposal.
        :type period_end: datetime
        """
        if period_end is None:
            raise ValueError("Invalid value for `period_end`, must not be `None`")  # noqa: E501
        if period_end is not None and len(period_end) > 25:
            raise ValueError("Invalid value for `period_end`, length must be less than or equal to `25`")  # noqa: E501

        self._period_end = period_end

    @property
    def continuous_operating_limit(self) -> Limit:
        """Gets the continuous_operating_limit of this Proposal.


        :return: The continuous_operating_limit of this Proposal.
        :rtype: Limit
        """
        return self._continuous_operating_limit

    @continuous_operating_limit.setter
    def continuous_operating_limit(self, continuous_operating_limit: Limit):
        """Sets the continuous_operating_limit of this Proposal.


        :param continuous_operating_limit: The continuous_operating_limit of this Proposal.
        :type continuous_operating_limit: Limit
        """
        if continuous_operating_limit is None:
            raise ValueError("Invalid value for `continuous_operating_limit`, must not be `None`")  # noqa: E501

        self._continuous_operating_limit = continuous_operating_limit

    @property
    def emergency_operating_limits(self) -> List[LimitValueSetInner]:
        """Gets the emergency_operating_limits of this Proposal.

         A set of general limit or rating values, each mapped to the various limit bands defined by the Transmission Provider's operating manual. This typically consists of a \"normal\" limit, as well as limits for various levels of emergency conditions (typically 2-4) defined in the operations manual.   # noqa: E501

        :return: The emergency_operating_limits of this Proposal.
        :rtype: List[LimitValueSetInner]
        """
        return self._emergency_operating_limits

    @emergency_operating_limits.setter
    def emergency_operating_limits(self, emergency_operating_limits: List[LimitValueSetInner]):
        """Sets the emergency_operating_limits of this Proposal.

         A set of general limit or rating values, each mapped to the various limit bands defined by the Transmission Provider's operating manual. This typically consists of a \"normal\" limit, as well as limits for various levels of emergency conditions (typically 2-4) defined in the operations manual.   # noqa: E501

        :param emergency_operating_limits: The emergency_operating_limits of this Proposal.
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
    def inputs_used(self) -> List[LimitProposalAllOfInputsUsed]:
        """Gets the inputs_used of this Proposal.

         Optional list of quantities used as input to the ratings determination. The particular information exchange determines which values may be expected as well as the conventions used to represent those values. This property is included to prescribe a way to include these inputs.   # noqa: E501

        :return: The inputs_used of this Proposal.
        :rtype: List[LimitProposalAllOfInputsUsed]
        """
        return self._inputs_used

    @inputs_used.setter
    def inputs_used(self, inputs_used: List[LimitProposalAllOfInputsUsed]):
        """Sets the inputs_used of this Proposal.

         Optional list of quantities used as input to the ratings determination. The particular information exchange determines which values may be expected as well as the conventions used to represent those values. This property is included to prescribe a way to include these inputs.   # noqa: E501

        :param inputs_used: The inputs_used of this Proposal.
        :type inputs_used: List[LimitProposalAllOfInputsUsed]
        """
        if inputs_used is not None and len(inputs_used) > 50:
            raise ValueError("Invalid value for `inputs_used`, number of items must be less than or equal to `50`")  # noqa: E501
        if inputs_used is not None and len(inputs_used) < 1:
            raise ValueError("Invalid value for `inputs_used`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._inputs_used = inputs_used
