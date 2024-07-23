from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from trolie-flask.models.base_model import Model
from trolie-flask.models.limit import Limit
from trolie-flask.models.limit_proposal_all_of_inputs_used import LimitProposalAllOfInputsUsed
from trolie-flask.models.limit_value_set_inner import LimitValueSetInner
from trolie-flask import util

from trolie-flask.models.limit import Limit  # noqa: E501
from trolie-flask.models.limit_proposal_all_of_inputs_used import LimitProposalAllOfInputsUsed  # noqa: E501
from trolie-flask.models.limit_value_set_inner import LimitValueSetInner  # noqa: E501

class LimitProposal(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, continuous_operating_limit=None, emergency_operating_limits=None, inputs_used=None):  # noqa: E501
        """LimitProposal - a model defined in OpenAPI

        :param continuous_operating_limit: The continuous_operating_limit of this LimitProposal.  # noqa: E501
        :type continuous_operating_limit: Limit
        :param emergency_operating_limits: The emergency_operating_limits of this LimitProposal.  # noqa: E501
        :type emergency_operating_limits: List[LimitValueSetInner]
        :param inputs_used: The inputs_used of this LimitProposal.  # noqa: E501
        :type inputs_used: List[LimitProposalAllOfInputsUsed]
        """
        self.openapi_types = {
            'continuous_operating_limit': Limit,
            'emergency_operating_limits': List[LimitValueSetInner],
            'inputs_used': List[LimitProposalAllOfInputsUsed]
        }

        self.attribute_map = {
            'continuous_operating_limit': 'continuous-operating-limit',
            'emergency_operating_limits': 'emergency-operating-limits',
            'inputs_used': 'inputs-used'
        }

        self._continuous_operating_limit = continuous_operating_limit
        self._emergency_operating_limits = emergency_operating_limits
        self._inputs_used = inputs_used

    @classmethod
    def from_dict(cls, dikt) -> 'LimitProposal':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The limit-proposal of this LimitProposal.  # noqa: E501
        :rtype: LimitProposal
        """
        return util.deserialize_model(dikt, cls)

    @property
    def continuous_operating_limit(self) -> Limit:
        """Gets the continuous_operating_limit of this LimitProposal.


        :return: The continuous_operating_limit of this LimitProposal.
        :rtype: Limit
        """
        return self._continuous_operating_limit

    @continuous_operating_limit.setter
    def continuous_operating_limit(self, continuous_operating_limit: Limit):
        """Sets the continuous_operating_limit of this LimitProposal.


        :param continuous_operating_limit: The continuous_operating_limit of this LimitProposal.
        :type continuous_operating_limit: Limit
        """
        if continuous_operating_limit is None:
            raise ValueError("Invalid value for `continuous_operating_limit`, must not be `None`")  # noqa: E501

        self._continuous_operating_limit = continuous_operating_limit

    @property
    def emergency_operating_limits(self) -> List[LimitValueSetInner]:
        """Gets the emergency_operating_limits of this LimitProposal.

         A set of general limit or rating values, each mapped to the various limit bands defined by the Transmission Provider's operating manual. This typically consists of a \"normal\" limit, as well as limits for various levels of emergency conditions (typically 2-4) defined in the operations manual.   # noqa: E501

        :return: The emergency_operating_limits of this LimitProposal.
        :rtype: List[LimitValueSetInner]
        """
        return self._emergency_operating_limits

    @emergency_operating_limits.setter
    def emergency_operating_limits(self, emergency_operating_limits: List[LimitValueSetInner]):
        """Sets the emergency_operating_limits of this LimitProposal.

         A set of general limit or rating values, each mapped to the various limit bands defined by the Transmission Provider's operating manual. This typically consists of a \"normal\" limit, as well as limits for various levels of emergency conditions (typically 2-4) defined in the operations manual.   # noqa: E501

        :param emergency_operating_limits: The emergency_operating_limits of this LimitProposal.
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
        """Gets the inputs_used of this LimitProposal.

         Optional list of quantities used as input to the ratings determination. The particular information exchange determines which values may be expected as well as the conventions used to represent those values. This property is included to prescribe a way to include these inputs.   # noqa: E501

        :return: The inputs_used of this LimitProposal.
        :rtype: List[LimitProposalAllOfInputsUsed]
        """
        return self._inputs_used

    @inputs_used.setter
    def inputs_used(self, inputs_used: List[LimitProposalAllOfInputsUsed]):
        """Sets the inputs_used of this LimitProposal.

         Optional list of quantities used as input to the ratings determination. The particular information exchange determines which values may be expected as well as the conventions used to represent those values. This property is included to prescribe a way to include these inputs.   # noqa: E501

        :param inputs_used: The inputs_used of this LimitProposal.
        :type inputs_used: List[LimitProposalAllOfInputsUsed]
        """
        if inputs_used is not None and len(inputs_used) > 50:
            raise ValueError("Invalid value for `inputs_used`, number of items must be less than or equal to `50`")  # noqa: E501
        if inputs_used is not None and len(inputs_used) < 1:
            raise ValueError("Invalid value for `inputs_used`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._inputs_used = inputs_used
