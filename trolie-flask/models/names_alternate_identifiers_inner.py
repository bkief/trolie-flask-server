from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from trolie-flask.models.base_model import Model
import re
from trolie-flask import util

import re  # noqa: E501

class NamesAlternateIdentifiersInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, authority=None, mrid=None):  # noqa: E501
        """NamesAlternateIdentifiersInner - a model defined in OpenAPI

        :param name: The name of this NamesAlternateIdentifiersInner.  # noqa: E501
        :type name: str
        :param authority: The authority of this NamesAlternateIdentifiersInner.  # noqa: E501
        :type authority: str
        :param mrid: The mrid of this NamesAlternateIdentifiersInner.  # noqa: E501
        :type mrid: str
        """
        self.openapi_types = {
            'name': str,
            'authority': str,
            'mrid': str
        }

        self.attribute_map = {
            'name': 'name',
            'authority': 'authority',
            'mrid': 'mrid'
        }

        self._name = name
        self._authority = authority
        self._mrid = mrid

    @classmethod
    def from_dict(cls, dikt) -> 'NamesAlternateIdentifiersInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The names_alternate_identifiers_inner of this NamesAlternateIdentifiersInner.  # noqa: E501
        :rtype: NamesAlternateIdentifiersInner
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this NamesAlternateIdentifiersInner.

         Contains a unique identifier for an object.    # noqa: E501

        :return: The name of this NamesAlternateIdentifiersInner.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this NamesAlternateIdentifiersInner.

         Contains a unique identifier for an object.    # noqa: E501

        :param name: The name of this NamesAlternateIdentifiersInner.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 250:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `250`")  # noqa: E501
        if name is not None and not re.search(r'^(.){0,250}$', name):  # noqa: E501
            raise ValueError("Invalid value for `name`, must be a follow pattern or equal to `/^(.){0,250}$/`")  # noqa: E501

        self._name = name

    @property
    def authority(self) -> str:
        """Gets the authority of this NamesAlternateIdentifiersInner.

        Usually the NERC id of the entity.  # noqa: E501

        :return: The authority of this NamesAlternateIdentifiersInner.
        :rtype: str
        """
        return self._authority

    @authority.setter
    def authority(self, authority: str):
        """Sets the authority of this NamesAlternateIdentifiersInner.

        Usually the NERC id of the entity.  # noqa: E501

        :param authority: The authority of this NamesAlternateIdentifiersInner.
        :type authority: str
        """
        if authority is not None and len(authority) > 10:
            raise ValueError("Invalid value for `authority`, length must be less than or equal to `10`")  # noqa: E501
        if authority is not None and not re.search(r'^[A-Z\-]{3,10}$', authority):  # noqa: E501
            raise ValueError("Invalid value for `authority`, must be a follow pattern or equal to `/^[A-Z\-]{3,10}$/`")  # noqa: E501

        self._authority = authority

    @property
    def mrid(self) -> str:
        """Gets the mrid of this NamesAlternateIdentifiersInner.

         Contains a unique identifier for an object.    # noqa: E501

        :return: The mrid of this NamesAlternateIdentifiersInner.
        :rtype: str
        """
        return self._mrid

    @mrid.setter
    def mrid(self, mrid: str):
        """Sets the mrid of this NamesAlternateIdentifiersInner.

         Contains a unique identifier for an object.    # noqa: E501

        :param mrid: The mrid of this NamesAlternateIdentifiersInner.
        :type mrid: str
        """
        if mrid is not None and len(mrid) > 250:
            raise ValueError("Invalid value for `mrid`, length must be less than or equal to `250`")  # noqa: E501
        if mrid is not None and not re.search(r'^(.){0,250}$', mrid):  # noqa: E501
            raise ValueError("Invalid value for `mrid`, must be a follow pattern or equal to `/^(.){0,250}$/`")  # noqa: E501

        self._mrid = mrid
