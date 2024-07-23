from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.conditional_value_set_inner import ConditionalValueSetInner
from openapi_server.models.limit import Limit
from openapi_server.models.limit_value_set_inner import LimitValueSetInner
from openapi_server.models.proposal_status import ProposalStatus
import re
from openapi_server import util

from openapi_server.models.conditional_value_set_inner import ConditionalValueSetInner  # noqa: E501
from openapi_server.models.limit import Limit  # noqa: E501
from openapi_server.models.limit_value_set_inner import LimitValueSetInner  # noqa: E501
from openapi_server.models.proposal_status import ProposalStatus  # noqa: E501
import re  # noqa: E501

class SeasonalProposalSeason(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, season_id=None, status=None, continuous_operating_limit=None, emergency_operating_limits=None, conditional_values=None):  # noqa: E501
        """SeasonalProposalSeason - a model defined in OpenAPI

        :param season_id: The season_id of this SeasonalProposalSeason.  # noqa: E501
        :type season_id: str
        :param status: The status of this SeasonalProposalSeason.  # noqa: E501
        :type status: ProposalStatus
        :param continuous_operating_limit: The continuous_operating_limit of this SeasonalProposalSeason.  # noqa: E501
        :type continuous_operating_limit: Limit
        :param emergency_operating_limits: The emergency_operating_limits of this SeasonalProposalSeason.  # noqa: E501
        :type emergency_operating_limits: List[LimitValueSetInner]
        :param conditional_values: The conditional_values of this SeasonalProposalSeason.  # noqa: E501
        :type conditional_values: List[ConditionalValueSetInner]
        """
        self.openapi_types = {
            'season_id': str,
            'status': ProposalStatus,
            'continuous_operating_limit': Limit,
            'emergency_operating_limits': List[LimitValueSetInner],
            'conditional_values': List[ConditionalValueSetInner]
        }

        self.attribute_map = {
            'season_id': 'season-id',
            'status': 'status',
            'continuous_operating_limit': 'continuous-operating-limit',
            'emergency_operating_limits': 'emergency-operating-limits',
            'conditional_values': 'conditional-values'
        }

        self._season_id = season_id
        self._status = status
        self._continuous_operating_limit = continuous_operating_limit
        self._emergency_operating_limits = emergency_operating_limits
        self._conditional_values = conditional_values

    @classmethod
    def from_dict(cls, dikt) -> 'SeasonalProposalSeason':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The seasonal-proposal-season of this SeasonalProposalSeason.  # noqa: E501
        :rtype: SeasonalProposalSeason
        """
        return util.deserialize_model(dikt, cls)

    @property
    def season_id(self) -> str:
        """Gets the season_id of this SeasonalProposalSeason.

         Contains a unique identifier for an object.    # noqa: E501

        :return: The season_id of this SeasonalProposalSeason.
        :rtype: str
        """
        return self._season_id

    @season_id.setter
    def season_id(self, season_id: str):
        """Sets the season_id of this SeasonalProposalSeason.

         Contains a unique identifier for an object.    # noqa: E501

        :param season_id: The season_id of this SeasonalProposalSeason.
        :type season_id: str
        """
        if season_id is not None and len(season_id) > 250:
            raise ValueError("Invalid value for `season_id`, length must be less than or equal to `250`")  # noqa: E501
        if season_id is not None and not re.search(r'^(.){0,250}$', season_id):  # noqa: E501
            raise ValueError("Invalid value for `season_id`, must be a follow pattern or equal to `/^(.){0,250}$/`")  # noqa: E501

        self._season_id = season_id

    @property
    def status(self) -> ProposalStatus:
        """Gets the status of this SeasonalProposalSeason.


        :return: The status of this SeasonalProposalSeason.
        :rtype: ProposalStatus
        """
        return self._status

    @status.setter
    def status(self, status: ProposalStatus):
        """Sets the status of this SeasonalProposalSeason.


        :param status: The status of this SeasonalProposalSeason.
        :type status: ProposalStatus
        """

        self._status = status

    @property
    def continuous_operating_limit(self) -> Limit:
        """Gets the continuous_operating_limit of this SeasonalProposalSeason.


        :return: The continuous_operating_limit of this SeasonalProposalSeason.
        :rtype: Limit
        """
        return self._continuous_operating_limit

    @continuous_operating_limit.setter
    def continuous_operating_limit(self, continuous_operating_limit: Limit):
        """Sets the continuous_operating_limit of this SeasonalProposalSeason.


        :param continuous_operating_limit: The continuous_operating_limit of this SeasonalProposalSeason.
        :type continuous_operating_limit: Limit
        """

        self._continuous_operating_limit = continuous_operating_limit

    @property
    def emergency_operating_limits(self) -> List[LimitValueSetInner]:
        """Gets the emergency_operating_limits of this SeasonalProposalSeason.

         A set of general limit or rating values, each mapped to the various limit bands defined by the Transmission Provider's operating manual. This typically consists of a \"normal\" limit, as well as limits for various levels of emergency conditions (typically 2-4) defined in the operations manual.   # noqa: E501

        :return: The emergency_operating_limits of this SeasonalProposalSeason.
        :rtype: List[LimitValueSetInner]
        """
        return self._emergency_operating_limits

    @emergency_operating_limits.setter
    def emergency_operating_limits(self, emergency_operating_limits: List[LimitValueSetInner]):
        """Sets the emergency_operating_limits of this SeasonalProposalSeason.

         A set of general limit or rating values, each mapped to the various limit bands defined by the Transmission Provider's operating manual. This typically consists of a \"normal\" limit, as well as limits for various levels of emergency conditions (typically 2-4) defined in the operations manual.   # noqa: E501

        :param emergency_operating_limits: The emergency_operating_limits of this SeasonalProposalSeason.
        :type emergency_operating_limits: List[LimitValueSetInner]
        """
        if emergency_operating_limits is not None and len(emergency_operating_limits) > 10:
            raise ValueError("Invalid value for `emergency_operating_limits`, number of items must be less than or equal to `10`")  # noqa: E501
        if emergency_operating_limits is not None and len(emergency_operating_limits) < 1:
            raise ValueError("Invalid value for `emergency_operating_limits`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._emergency_operating_limits = emergency_operating_limits

    @property
    def conditional_values(self) -> List[ConditionalValueSetInner]:
        """Gets the conditional_values of this SeasonalProposalSeason.

        List of alternative ratings for rating altering conditions on the segment.    # noqa: E501

        :return: The conditional_values of this SeasonalProposalSeason.
        :rtype: List[ConditionalValueSetInner]
        """
        return self._conditional_values

    @conditional_values.setter
    def conditional_values(self, conditional_values: List[ConditionalValueSetInner]):
        """Sets the conditional_values of this SeasonalProposalSeason.

        List of alternative ratings for rating altering conditions on the segment.    # noqa: E501

        :param conditional_values: The conditional_values of this SeasonalProposalSeason.
        :type conditional_values: List[ConditionalValueSetInner]
        """
        if conditional_values is not None and len(conditional_values) > 100:
            raise ValueError("Invalid value for `conditional_values`, number of items must be less than or equal to `100`")  # noqa: E501
        if conditional_values is not None and len(conditional_values) < 1:
            raise ValueError("Invalid value for `conditional_values`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._conditional_values = conditional_values
