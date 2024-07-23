from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class OvervoltageThresholdPu(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, voltage_pu_max=None, base_k_v=None):  # noqa: E501
        """OvervoltageThresholdPu - a model defined in OpenAPI

        :param voltage_pu_max: The voltage_pu_max of this OvervoltageThresholdPu.  # noqa: E501
        :type voltage_pu_max: float
        :param base_k_v: The base_k_v of this OvervoltageThresholdPu.  # noqa: E501
        :type base_k_v: float
        """
        self.openapi_types = {
            'voltage_pu_max': float,
            'base_k_v': float
        }

        self.attribute_map = {
            'voltage_pu_max': 'voltage-pu-max',
            'base_k_v': 'base-kV'
        }

        self._voltage_pu_max = voltage_pu_max
        self._base_k_v = base_k_v

    @classmethod
    def from_dict(cls, dikt) -> 'OvervoltageThresholdPu':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The overvoltage-threshold-pu of this OvervoltageThresholdPu.  # noqa: E501
        :rtype: OvervoltageThresholdPu
        """
        return util.deserialize_model(dikt, cls)

    @property
    def voltage_pu_max(self) -> float:
        """Gets the voltage_pu_max of this OvervoltageThresholdPu.


        :return: The voltage_pu_max of this OvervoltageThresholdPu.
        :rtype: float
        """
        return self._voltage_pu_max

    @voltage_pu_max.setter
    def voltage_pu_max(self, voltage_pu_max: float):
        """Sets the voltage_pu_max of this OvervoltageThresholdPu.


        :param voltage_pu_max: The voltage_pu_max of this OvervoltageThresholdPu.
        :type voltage_pu_max: float
        """
        if voltage_pu_max is None:
            raise ValueError("Invalid value for `voltage_pu_max`, must not be `None`")  # noqa: E501
        if voltage_pu_max is not None and voltage_pu_max > 2:  # noqa: E501
            raise ValueError("Invalid value for `voltage_pu_max`, must be a value less than or equal to `2`")  # noqa: E501
        if voltage_pu_max is not None and voltage_pu_max < 0:  # noqa: E501
            raise ValueError("Invalid value for `voltage_pu_max`, must be a value greater than or equal to `0`")  # noqa: E501

        self._voltage_pu_max = voltage_pu_max

    @property
    def base_k_v(self) -> float:
        """Gets the base_k_v of this OvervoltageThresholdPu.


        :return: The base_k_v of this OvervoltageThresholdPu.
        :rtype: float
        """
        return self._base_k_v

    @base_k_v.setter
    def base_k_v(self, base_k_v: float):
        """Sets the base_k_v of this OvervoltageThresholdPu.


        :param base_k_v: The base_k_v of this OvervoltageThresholdPu.
        :type base_k_v: float
        """
        if base_k_v is not None and base_k_v > 1100:  # noqa: E501
            raise ValueError("Invalid value for `base_k_v`, must be a value less than or equal to `1100`")  # noqa: E501
        if base_k_v is not None and base_k_v < 0:  # noqa: E501
            raise ValueError("Invalid value for `base_k_v`, must be a value greater than or equal to `0`")  # noqa: E501

        self._base_k_v = base_k_v