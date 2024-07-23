from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from trolie-flask.models.base_model import Model
from trolie-flask.models.data_provenance import DataProvenance
from trolie-flask.models.forecast_proposal_status_proposal_validation_errors_inner import ForecastProposalStatusProposalValidationErrorsInner
from trolie-flask.models.names import Names
from trolie-flask import util

from trolie-flask.models.data_provenance import DataProvenance  # noqa: E501
from trolie-flask.models.forecast_proposal_status_proposal_validation_errors_inner import ForecastProposalStatusProposalValidationErrorsInner  # noqa: E501
from trolie-flask.models.names import Names  # noqa: E501

class RealTimeProposalStatus(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, incomplete_obligation_count=None, incomplete_obligations=None, invalid_proposal_count=None, proposal_validation_errors=None, ratings_provider=None):  # noqa: E501
        """RealTimeProposalStatus - a model defined in OpenAPI

        :param incomplete_obligation_count: The incomplete_obligation_count of this RealTimeProposalStatus.  # noqa: E501
        :type incomplete_obligation_count: int
        :param incomplete_obligations: The incomplete_obligations of this RealTimeProposalStatus.  # noqa: E501
        :type incomplete_obligations: List[Names]
        :param invalid_proposal_count: The invalid_proposal_count of this RealTimeProposalStatus.  # noqa: E501
        :type invalid_proposal_count: int
        :param proposal_validation_errors: The proposal_validation_errors of this RealTimeProposalStatus.  # noqa: E501
        :type proposal_validation_errors: List[ForecastProposalStatusProposalValidationErrorsInner]
        :param ratings_provider: The ratings_provider of this RealTimeProposalStatus.  # noqa: E501
        :type ratings_provider: DataProvenance
        """
        self.openapi_types = {
            'incomplete_obligation_count': int,
            'incomplete_obligations': List[Names],
            'invalid_proposal_count': int,
            'proposal_validation_errors': List[ForecastProposalStatusProposalValidationErrorsInner],
            'ratings_provider': DataProvenance
        }

        self.attribute_map = {
            'incomplete_obligation_count': 'incomplete-obligation-count',
            'incomplete_obligations': 'incomplete-obligations',
            'invalid_proposal_count': 'invalid-proposal-count',
            'proposal_validation_errors': 'proposal-validation-errors',
            'ratings_provider': 'ratings-provider'
        }

        self._incomplete_obligation_count = incomplete_obligation_count
        self._incomplete_obligations = incomplete_obligations
        self._invalid_proposal_count = invalid_proposal_count
        self._proposal_validation_errors = proposal_validation_errors
        self._ratings_provider = ratings_provider

    @classmethod
    def from_dict(cls, dikt) -> 'RealTimeProposalStatus':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The real-time-proposal-status of this RealTimeProposalStatus.  # noqa: E501
        :rtype: RealTimeProposalStatus
        """
        return util.deserialize_model(dikt, cls)

    @property
    def incomplete_obligation_count(self) -> int:
        """Gets the incomplete_obligation_count of this RealTimeProposalStatus.

         The number of facilities for this provider whose Ratings Obligation has not been met in this forecast window. This number may be larger than the size of `incomplete-facilities`, since the latter has a pre-defined upper bound for performance and application security reasons.  ⚠️ **The Ratings Provider should check that this value is zero when they believe they have completed their submission process.️** ⚠️   # noqa: E501

        :return: The incomplete_obligation_count of this RealTimeProposalStatus.
        :rtype: int
        """
        return self._incomplete_obligation_count

    @incomplete_obligation_count.setter
    def incomplete_obligation_count(self, incomplete_obligation_count: int):
        """Sets the incomplete_obligation_count of this RealTimeProposalStatus.

         The number of facilities for this provider whose Ratings Obligation has not been met in this forecast window. This number may be larger than the size of `incomplete-facilities`, since the latter has a pre-defined upper bound for performance and application security reasons.  ⚠️ **The Ratings Provider should check that this value is zero when they believe they have completed their submission process.️** ⚠️   # noqa: E501

        :param incomplete_obligation_count: The incomplete_obligation_count of this RealTimeProposalStatus.
        :type incomplete_obligation_count: int
        """
        if incomplete_obligation_count is None:
            raise ValueError("Invalid value for `incomplete_obligation_count`, must not be `None`")  # noqa: E501
        if incomplete_obligation_count is not None and incomplete_obligation_count > 50000:  # noqa: E501
            raise ValueError("Invalid value for `incomplete_obligation_count`, must be a value less than or equal to `50000`")  # noqa: E501
        if incomplete_obligation_count is not None and incomplete_obligation_count < 0:  # noqa: E501
            raise ValueError("Invalid value for `incomplete_obligation_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._incomplete_obligation_count = incomplete_obligation_count

    @property
    def incomplete_obligations(self) -> List[Names]:
        """Gets the incomplete_obligations of this RealTimeProposalStatus.

         Indicates which Ratings Obligations have not been fulfilled. The size of this set is bounded and may be less than the actual count of unfulfilled Obligations indicated in `incomplete-obligation-count`. The intended use case for this set is debugging and troubleshooting.   # noqa: E501

        :return: The incomplete_obligations of this RealTimeProposalStatus.
        :rtype: List[Names]
        """
        return self._incomplete_obligations

    @incomplete_obligations.setter
    def incomplete_obligations(self, incomplete_obligations: List[Names]):
        """Sets the incomplete_obligations of this RealTimeProposalStatus.

         Indicates which Ratings Obligations have not been fulfilled. The size of this set is bounded and may be less than the actual count of unfulfilled Obligations indicated in `incomplete-obligation-count`. The intended use case for this set is debugging and troubleshooting.   # noqa: E501

        :param incomplete_obligations: The incomplete_obligations of this RealTimeProposalStatus.
        :type incomplete_obligations: List[Names]
        """
        if incomplete_obligations is None:
            raise ValueError("Invalid value for `incomplete_obligations`, must not be `None`")  # noqa: E501
        if incomplete_obligations is not None and len(incomplete_obligations) > 10:
            raise ValueError("Invalid value for `incomplete_obligations`, number of items must be less than or equal to `10`")  # noqa: E501
        if incomplete_obligations is not None and len(incomplete_obligations) < 0:
            raise ValueError("Invalid value for `incomplete_obligations`, number of items must be greater than or equal to `0`")  # noqa: E501

        self._incomplete_obligations = incomplete_obligations

    @property
    def invalid_proposal_count(self) -> int:
        """Gets the invalid_proposal_count of this RealTimeProposalStatus.

         The number of `resource-forecast-proposal` objects that have been determined to be *invalid* during this Forecast Window for the current Ratings Provider. This count is provided for troubleshooting, establishing trends, and triggering alerts.   # noqa: E501

        :return: The invalid_proposal_count of this RealTimeProposalStatus.
        :rtype: int
        """
        return self._invalid_proposal_count

    @invalid_proposal_count.setter
    def invalid_proposal_count(self, invalid_proposal_count: int):
        """Sets the invalid_proposal_count of this RealTimeProposalStatus.

         The number of `resource-forecast-proposal` objects that have been determined to be *invalid* during this Forecast Window for the current Ratings Provider. This count is provided for troubleshooting, establishing trends, and triggering alerts.   # noqa: E501

        :param invalid_proposal_count: The invalid_proposal_count of this RealTimeProposalStatus.
        :type invalid_proposal_count: int
        """
        if invalid_proposal_count is None:
            raise ValueError("Invalid value for `invalid_proposal_count`, must not be `None`")  # noqa: E501
        if invalid_proposal_count is not None and invalid_proposal_count > 50000:  # noqa: E501
            raise ValueError("Invalid value for `invalid_proposal_count`, must be a value less than or equal to `50000`")  # noqa: E501
        if invalid_proposal_count is not None and invalid_proposal_count < 0:  # noqa: E501
            raise ValueError("Invalid value for `invalid_proposal_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._invalid_proposal_count = invalid_proposal_count

    @property
    def proposal_validation_errors(self) -> List[ForecastProposalStatusProposalValidationErrorsInner]:
        """Gets the proposal_validation_errors of this RealTimeProposalStatus.

        The most recent validation errors  # noqa: E501

        :return: The proposal_validation_errors of this RealTimeProposalStatus.
        :rtype: List[ForecastProposalStatusProposalValidationErrorsInner]
        """
        return self._proposal_validation_errors

    @proposal_validation_errors.setter
    def proposal_validation_errors(self, proposal_validation_errors: List[ForecastProposalStatusProposalValidationErrorsInner]):
        """Sets the proposal_validation_errors of this RealTimeProposalStatus.

        The most recent validation errors  # noqa: E501

        :param proposal_validation_errors: The proposal_validation_errors of this RealTimeProposalStatus.
        :type proposal_validation_errors: List[ForecastProposalStatusProposalValidationErrorsInner]
        """
        if proposal_validation_errors is None:
            raise ValueError("Invalid value for `proposal_validation_errors`, must not be `None`")  # noqa: E501
        if proposal_validation_errors is not None and len(proposal_validation_errors) > 50:
            raise ValueError("Invalid value for `proposal_validation_errors`, number of items must be less than or equal to `50`")  # noqa: E501
        if proposal_validation_errors is not None and len(proposal_validation_errors) < 0:
            raise ValueError("Invalid value for `proposal_validation_errors`, number of items must be greater than or equal to `0`")  # noqa: E501

        self._proposal_validation_errors = proposal_validation_errors

    @property
    def ratings_provider(self) -> DataProvenance:
        """Gets the ratings_provider of this RealTimeProposalStatus.


        :return: The ratings_provider of this RealTimeProposalStatus.
        :rtype: DataProvenance
        """
        return self._ratings_provider

    @ratings_provider.setter
    def ratings_provider(self, ratings_provider: DataProvenance):
        """Sets the ratings_provider of this RealTimeProposalStatus.


        :param ratings_provider: The ratings_provider of this RealTimeProposalStatus.
        :type ratings_provider: DataProvenance
        """
        if ratings_provider is None:
            raise ValueError("Invalid value for `ratings_provider`, must not be `None`")  # noqa: E501

        self._ratings_provider = ratings_provider
