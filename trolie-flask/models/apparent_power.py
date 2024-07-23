from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from trolie-flask.models.base_model import Model
from trolie-flask import util


class ApparentPower(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, mva=None):  # noqa: E501
        """ApparentPower - a model defined in OpenAPI

        :param mva: The mva of this ApparentPower.  # noqa: E501
        :type mva: float
        """
        self.openapi_types = {
            'mva': float
        }

        self.attribute_map = {
            'mva': 'mva'
        }

        self._mva = mva

    @classmethod
    def from_dict(cls, dikt) -> 'ApparentPower':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The apparent-power of this ApparentPower.  # noqa: E501
        :rtype: ApparentPower
        """
        return util.deserialize_model(dikt, cls)

    @property
    def mva(self) -> float:
        """Gets the mva of this ApparentPower.


        :return: The mva of this ApparentPower.
        :rtype: float
        """
        return self._mva

    @mva.setter
    def mva(self, mva: float):
        """Sets the mva of this ApparentPower.


        :param mva: The mva of this ApparentPower.
        :type mva: float
        """
        if mva is None:
            raise ValueError("Invalid value for `mva`, must not be `None`")  # noqa: E501
        if mva is not None and mva > 10000:  # noqa: E501
            raise ValueError("Invalid value for `mva`, must be a value less than or equal to `10000`")  # noqa: E501
        if mva is not None and mva < 1:  # noqa: E501
            raise ValueError("Invalid value for `mva`, must be a value greater than or equal to `1`")  # noqa: E501

        self._mva = mva
