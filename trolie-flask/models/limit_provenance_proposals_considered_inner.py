from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.data_provenance import DataProvenance
from openapi_server.models.limit import Limit
from openapi_server.models.limit_proposal_all_of_inputs_used import LimitProposalAllOfInputsUsed
from openapi_server.models.limit_value_set_inner import LimitValueSetInner
import re
from openapi_server import util

from openapi_server.models.data_provenance import DataProvenance  # noqa: E501
from openapi_server.models.limit import Limit  # noqa: E501
from openapi_server.models.limit_proposal_all_of_inputs_used import LimitProposalAllOfInputsUsed  # noqa: E501
from openapi_server.models.limit_value_set_inner import LimitValueSetInner  # noqa: E501
import re  # noqa: E501

class LimitProvenanceProposalsConsideredInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, period_start=None, period_end=None, continuous_operating_limit=None, emergency_operating_limits=None, inputs_used=None, source=None, proposal_disposition=None, resource_id=None):  # noqa: E501
        """LimitProvenanceProposalsConsideredInner - a model defined in OpenAPI

        :param period_start: The period_start of this LimitProvenanceProposalsConsideredInner.  # noqa: E501
        :type period_start: datetime
        :param period_end: The period_end of this LimitProvenanceProposalsConsideredInner.  # noqa: E501
        :type period_end: datetime
        :param continuous_operating_limit: The continuous_operating_limit of this LimitProvenanceProposalsConsideredInner.  # noqa: E501
        :type continuous_operating_limit: Limit
        :param emergency_operating_limits: The emergency_operating_limits of this LimitProvenanceProposalsConsideredInner.  # noqa: E501
        :type emergency_operating_limits: List[LimitValueSetInner]
        :param inputs_used: The inputs_used of this LimitProvenanceProposalsConsideredInner.  # noqa: E501
        :type inputs_used: List[LimitProposalAllOfInputsUsed]
        :param source: The source of this LimitProvenanceProposalsConsideredInner.  # noqa: E501
        :type source: DataProvenance
        :param proposal_disposition: The proposal_disposition of this LimitProvenanceProposalsConsideredInner.  # noqa: E501
        :type proposal_disposition: str
        :param resource_id: The resource_id of this LimitProvenanceProposalsConsideredInner.  # noqa: E501
        :type resource_id: str
        """
        self.openapi_types = {
            'period_start': datetime,
            'period_end': datetime,
            'continuous_operating_limit': Limit,
            'emergency_operating_limits': List[LimitValueSetInner],
            'inputs_used': List[LimitProposalAllOfInputsUsed],
            'source': DataProvenance,
            'proposal_disposition': str,
            'resource_id': str
        }

        self.attribute_map = {
            'period_start': 'period-start',
            'period_end': 'period-end',
            'continuous_operating_limit': 'continuous-operating-limit',
            'emergency_operating_limits': 'emergency-operating-limits',
            'inputs_used': 'inputs-used',
            'source': 'source',
            'proposal_disposition': 'proposal-disposition',
            'resource_id': 'resource-id'
        }

        self._period_start = period_start
        self._period_end = period_end
        self._continuous_operating_limit = continuous_operating_limit
        self._emergency_operating_limits = emergency_operating_limits
        self._inputs_used = inputs_used
        self._source = source
        self._proposal_disposition = proposal_disposition
        self._resource_id = resource_id

    @classmethod
    def from_dict(cls, dikt) -> 'LimitProvenanceProposalsConsideredInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The limit_provenance_proposals_considered_inner of this LimitProvenanceProposalsConsideredInner.  # noqa: E501
        :rtype: LimitProvenanceProposalsConsideredInner
        """
        return util.deserialize_model(dikt, cls)

    @property
    def period_start(self) -> datetime:
        """Gets the period_start of this LimitProvenanceProposalsConsideredInner.

         RFC 3339 date-time string with *no fractional seconds component* that designates a start or end to an operating period (such as an hour) that starts at a specified time. This will frequently be at the start of an hour, but may be finer-grained, such as every 30 minutes, should the Clearinghouse Provider choose.  If the Transmission Provider is operating in EST, these are valid and equivalent values:  * 2023-01-01T06:00Z * 2023-01-01T01:00-5:00 * 2023-01-01T00:00-6:00 * 2023-01-01T11:30+5:30  The server should uniformly represent date-times in the operational time zone of the Clearinghouse Provider.   # noqa: E501

        :return: The period_start of this LimitProvenanceProposalsConsideredInner.
        :rtype: datetime
        """
        return self._period_start

    @period_start.setter
    def period_start(self, period_start: datetime):
        """Sets the period_start of this LimitProvenanceProposalsConsideredInner.

         RFC 3339 date-time string with *no fractional seconds component* that designates a start or end to an operating period (such as an hour) that starts at a specified time. This will frequently be at the start of an hour, but may be finer-grained, such as every 30 minutes, should the Clearinghouse Provider choose.  If the Transmission Provider is operating in EST, these are valid and equivalent values:  * 2023-01-01T06:00Z * 2023-01-01T01:00-5:00 * 2023-01-01T00:00-6:00 * 2023-01-01T11:30+5:30  The server should uniformly represent date-times in the operational time zone of the Clearinghouse Provider.   # noqa: E501

        :param period_start: The period_start of this LimitProvenanceProposalsConsideredInner.
        :type period_start: datetime
        """
        if period_start is None:
            raise ValueError("Invalid value for `period_start`, must not be `None`")  # noqa: E501
        if period_start is not None and len(period_start) > 25:
            raise ValueError("Invalid value for `period_start`, length must be less than or equal to `25`")  # noqa: E501

        self._period_start = period_start

    @property
    def period_end(self) -> datetime:
        """Gets the period_end of this LimitProvenanceProposalsConsideredInner.

         RFC 3339 date-time string with *no fractional seconds component* that designates a start or end to an operating period (such as an hour) that starts at a specified time. This will frequently be at the start of an hour, but may be finer-grained, such as every 30 minutes, should the Clearinghouse Provider choose.  If the Transmission Provider is operating in EST, these are valid and equivalent values:  * 2023-01-01T06:00Z * 2023-01-01T01:00-5:00 * 2023-01-01T00:00-6:00 * 2023-01-01T11:30+5:30  The server should uniformly represent date-times in the operational time zone of the Clearinghouse Provider.   # noqa: E501

        :return: The period_end of this LimitProvenanceProposalsConsideredInner.
        :rtype: datetime
        """
        return self._period_end

    @period_end.setter
    def period_end(self, period_end: datetime):
        """Sets the period_end of this LimitProvenanceProposalsConsideredInner.

         RFC 3339 date-time string with *no fractional seconds component* that designates a start or end to an operating period (such as an hour) that starts at a specified time. This will frequently be at the start of an hour, but may be finer-grained, such as every 30 minutes, should the Clearinghouse Provider choose.  If the Transmission Provider is operating in EST, these are valid and equivalent values:  * 2023-01-01T06:00Z * 2023-01-01T01:00-5:00 * 2023-01-01T00:00-6:00 * 2023-01-01T11:30+5:30  The server should uniformly represent date-times in the operational time zone of the Clearinghouse Provider.   # noqa: E501

        :param period_end: The period_end of this LimitProvenanceProposalsConsideredInner.
        :type period_end: datetime
        """
        if period_end is None:
            raise ValueError("Invalid value for `period_end`, must not be `None`")  # noqa: E501
        if period_end is not None and len(period_end) > 25:
            raise ValueError("Invalid value for `period_end`, length must be less than or equal to `25`")  # noqa: E501

        self._period_end = period_end

    @property
    def continuous_operating_limit(self) -> Limit:
        """Gets the continuous_operating_limit of this LimitProvenanceProposalsConsideredInner.


        :return: The continuous_operating_limit of this LimitProvenanceProposalsConsideredInner.
        :rtype: Limit
        """
        return self._continuous_operating_limit

    @continuous_operating_limit.setter
    def continuous_operating_limit(self, continuous_operating_limit: Limit):
        """Sets the continuous_operating_limit of this LimitProvenanceProposalsConsideredInner.


        :param continuous_operating_limit: The continuous_operating_limit of this LimitProvenanceProposalsConsideredInner.
        :type continuous_operating_limit: Limit
        """
        if continuous_operating_limit is None:
            raise ValueError("Invalid value for `continuous_operating_limit`, must not be `None`")  # noqa: E501

        self._continuous_operating_limit = continuous_operating_limit

    @property
    def emergency_operating_limits(self) -> List[LimitValueSetInner]:
        """Gets the emergency_operating_limits of this LimitProvenanceProposalsConsideredInner.

         A set of general limit or rating values, each mapped to the various limit bands defined by the Transmission Provider's operating manual. This typically consists of a \"normal\" limit, as well as limits for various levels of emergency conditions (typically 2-4) defined in the operations manual.   # noqa: E501

        :return: The emergency_operating_limits of this LimitProvenanceProposalsConsideredInner.
        :rtype: List[LimitValueSetInner]
        """
        return self._emergency_operating_limits

    @emergency_operating_limits.setter
    def emergency_operating_limits(self, emergency_operating_limits: List[LimitValueSetInner]):
        """Sets the emergency_operating_limits of this LimitProvenanceProposalsConsideredInner.

         A set of general limit or rating values, each mapped to the various limit bands defined by the Transmission Provider's operating manual. This typically consists of a \"normal\" limit, as well as limits for various levels of emergency conditions (typically 2-4) defined in the operations manual.   # noqa: E501

        :param emergency_operating_limits: The emergency_operating_limits of this LimitProvenanceProposalsConsideredInner.
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
        """Gets the inputs_used of this LimitProvenanceProposalsConsideredInner.

         Optional list of quantities used as input to the ratings determination. The particular information exchange determines which values may be expected as well as the conventions used to represent those values. This property is included to prescribe a way to include these inputs.   # noqa: E501

        :return: The inputs_used of this LimitProvenanceProposalsConsideredInner.
        :rtype: List[LimitProposalAllOfInputsUsed]
        """
        return self._inputs_used

    @inputs_used.setter
    def inputs_used(self, inputs_used: List[LimitProposalAllOfInputsUsed]):
        """Sets the inputs_used of this LimitProvenanceProposalsConsideredInner.

         Optional list of quantities used as input to the ratings determination. The particular information exchange determines which values may be expected as well as the conventions used to represent those values. This property is included to prescribe a way to include these inputs.   # noqa: E501

        :param inputs_used: The inputs_used of this LimitProvenanceProposalsConsideredInner.
        :type inputs_used: List[LimitProposalAllOfInputsUsed]
        """
        if inputs_used is not None and len(inputs_used) > 50:
            raise ValueError("Invalid value for `inputs_used`, number of items must be less than or equal to `50`")  # noqa: E501
        if inputs_used is not None and len(inputs_used) < 1:
            raise ValueError("Invalid value for `inputs_used`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._inputs_used = inputs_used

    @property
    def source(self) -> DataProvenance:
        """Gets the source of this LimitProvenanceProposalsConsideredInner.


        :return: The source of this LimitProvenanceProposalsConsideredInner.
        :rtype: DataProvenance
        """
        return self._source

    @source.setter
    def source(self, source: DataProvenance):
        """Sets the source of this LimitProvenanceProposalsConsideredInner.


        :param source: The source of this LimitProvenanceProposalsConsideredInner.
        :type source: DataProvenance
        """
        if source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    @property
    def proposal_disposition(self) -> str:
        """Gets the proposal_disposition of this LimitProvenanceProposalsConsideredInner.

         Despite a proposal being accepted by TROLIE, the downstream Clearinghouse logic may still disqualify a proposal. This might occur if, for example, the upper and lower reasonability limits are not aligned between TROLIE and the Clearinghouse.  To aid troubleshooting, the specification requires that TROLIE instances explicitly indicate if the proposal was `Used` in the determination of the limit or was `Rejected`.   # noqa: E501

        :return: The proposal_disposition of this LimitProvenanceProposalsConsideredInner.
        :rtype: str
        """
        return self._proposal_disposition

    @proposal_disposition.setter
    def proposal_disposition(self, proposal_disposition: str):
        """Sets the proposal_disposition of this LimitProvenanceProposalsConsideredInner.

         Despite a proposal being accepted by TROLIE, the downstream Clearinghouse logic may still disqualify a proposal. This might occur if, for example, the upper and lower reasonability limits are not aligned between TROLIE and the Clearinghouse.  To aid troubleshooting, the specification requires that TROLIE instances explicitly indicate if the proposal was `Used` in the determination of the limit or was `Rejected`.   # noqa: E501

        :param proposal_disposition: The proposal_disposition of this LimitProvenanceProposalsConsideredInner.
        :type proposal_disposition: str
        """
        allowed_values = ["Used", "Rejected"]  # noqa: E501
        if proposal_disposition not in allowed_values:
            raise ValueError(
                "Invalid value for `proposal_disposition` ({0}), must be one of {1}"
                .format(proposal_disposition, allowed_values)
            )

        self._proposal_disposition = proposal_disposition

    @property
    def resource_id(self) -> str:
        """Gets the resource_id of this LimitProvenanceProposalsConsideredInner.

         Contains a unique identifier for an a power system resources, such as a transmission facility, segment, interface, etc.    # noqa: E501

        :return: The resource_id of this LimitProvenanceProposalsConsideredInner.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id: str):
        """Sets the resource_id of this LimitProvenanceProposalsConsideredInner.

         Contains a unique identifier for an a power system resources, such as a transmission facility, segment, interface, etc.    # noqa: E501

        :param resource_id: The resource_id of this LimitProvenanceProposalsConsideredInner.
        :type resource_id: str
        """
        if resource_id is not None and len(resource_id) > 250:
            raise ValueError("Invalid value for `resource_id`, length must be less than or equal to `250`")  # noqa: E501
        if resource_id is not None and not re.search(r'^(.){0,250}$', resource_id):  # noqa: E501
            raise ValueError("Invalid value for `resource_id`, must be a follow pattern or equal to `/^(.){0,250}$/`")  # noqa: E501

        self._resource_id = resource_id