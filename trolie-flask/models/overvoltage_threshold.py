from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from trolie-flask.models.base_model import Model
from trolie-flask import util


class OvervoltageThreshold(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, k_v_max=None):  # noqa: E501
        """OvervoltageThreshold - a model defined in OpenAPI

        :param k_v_max: The k_v_max of this OvervoltageThreshold.  # noqa: E501
        :type k_v_max: float
        """
        self.openapi_types = {
            'k_v_max': float
        }

        self.attribute_map = {
            'k_v_max': 'kV-max'
        }

        self._k_v_max = k_v_max

    @classmethod
    def from_dict(cls, dikt) -> 'OvervoltageThreshold':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The overvoltage-threshold of this OvervoltageThreshold.  # noqa: E501
        :rtype: OvervoltageThreshold
        """
        return util.deserialize_model(dikt, cls)

    @property
    def k_v_max(self) -> float:
        """Gets the k_v_max of this OvervoltageThreshold.


        :return: The k_v_max of this OvervoltageThreshold.
        :rtype: float
        """
        return self._k_v_max

    @k_v_max.setter
    def k_v_max(self, k_v_max: float):
        """Sets the k_v_max of this OvervoltageThreshold.


        :param k_v_max: The k_v_max of this OvervoltageThreshold.
        :type k_v_max: float
        """
        if k_v_max is None:
            raise ValueError("Invalid value for `k_v_max`, must not be `None`")  # noqa: E501
        if k_v_max is not None and k_v_max > 1100:  # noqa: E501
            raise ValueError("Invalid value for `k_v_max`, must be a value less than or equal to `1100`")  # noqa: E501
        if k_v_max is not None and k_v_max < 0:  # noqa: E501
            raise ValueError("Invalid value for `k_v_max`, must be a value greater than or equal to `0`")  # noqa: E501

        self._k_v_max = k_v_max
