from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from trolie-flask.models.base_model import Model
import re
from trolie-flask import util

import re  # noqa: E501

class DataProvenance(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, provider=None, last_updated=None, origin_id=None):  # noqa: E501
        """DataProvenance - a model defined in OpenAPI

        :param provider: The provider of this DataProvenance.  # noqa: E501
        :type provider: str
        :param last_updated: The last_updated of this DataProvenance.  # noqa: E501
        :type last_updated: datetime
        :param origin_id: The origin_id of this DataProvenance.  # noqa: E501
        :type origin_id: str
        """
        self.openapi_types = {
            'provider': str,
            'last_updated': datetime,
            'origin_id': str
        }

        self.attribute_map = {
            'provider': 'provider',
            'last_updated': 'last-updated',
            'origin_id': 'origin-id'
        }

        self._provider = provider
        self._last_updated = last_updated
        self._origin_id = origin_id

    @classmethod
    def from_dict(cls, dikt) -> 'DataProvenance':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The data-provenance of this DataProvenance.  # noqa: E501
        :rtype: DataProvenance
        """
        return util.deserialize_model(dikt, cls)

    @property
    def provider(self) -> str:
        """Gets the provider of this DataProvenance.

        Usually the NERC id of the entity.  # noqa: E501

        :return: The provider of this DataProvenance.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider: str):
        """Sets the provider of this DataProvenance.

        Usually the NERC id of the entity.  # noqa: E501

        :param provider: The provider of this DataProvenance.
        :type provider: str
        """
        if provider is None:
            raise ValueError("Invalid value for `provider`, must not be `None`")  # noqa: E501
        if provider is not None and len(provider) > 10:
            raise ValueError("Invalid value for `provider`, length must be less than or equal to `10`")  # noqa: E501
        if provider is not None and not re.search(r'^[A-Z\-]{3,10}$', provider):  # noqa: E501
            raise ValueError("Invalid value for `provider`, must be a follow pattern or equal to `/^[A-Z\-]{3,10}$/`")  # noqa: E501

        self._provider = provider

    @property
    def last_updated(self) -> datetime:
        """Gets the last_updated of this DataProvenance.

        RFC 3339 date-time string with a maximum of 10 digits in the fractional seconds component, i.e., nanosecond precision.  # noqa: E501

        :return: The last_updated of this DataProvenance.
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated: datetime):
        """Sets the last_updated of this DataProvenance.

        RFC 3339 date-time string with a maximum of 10 digits in the fractional seconds component, i.e., nanosecond precision.  # noqa: E501

        :param last_updated: The last_updated of this DataProvenance.
        :type last_updated: datetime
        """
        if last_updated is None:
            raise ValueError("Invalid value for `last_updated`, must not be `None`")  # noqa: E501
        if last_updated is not None and len(last_updated) > 35:
            raise ValueError("Invalid value for `last_updated`, length must be less than or equal to `35`")  # noqa: E501

        self._last_updated = last_updated

    @property
    def origin_id(self) -> str:
        """Gets the origin_id of this DataProvenance.

         Contains a unique identifier for an object.    # noqa: E501

        :return: The origin_id of this DataProvenance.
        :rtype: str
        """
        return self._origin_id

    @origin_id.setter
    def origin_id(self, origin_id: str):
        """Sets the origin_id of this DataProvenance.

         Contains a unique identifier for an object.    # noqa: E501

        :param origin_id: The origin_id of this DataProvenance.
        :type origin_id: str
        """
        if origin_id is not None and len(origin_id) > 250:
            raise ValueError("Invalid value for `origin_id`, length must be less than or equal to `250`")  # noqa: E501
        if origin_id is not None and not re.search(r'^(.){0,250}$', origin_id):  # noqa: E501
            raise ValueError("Invalid value for `origin_id`, must be a follow pattern or equal to `/^(.){0,250}$/`")  # noqa: E501

        self._origin_id = origin_id
