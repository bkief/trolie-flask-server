import sys
from setuptools import setup, find_packages

NAME = "trolie-flask"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion>=2.0.2",
    "swagger-ui-bundle>=0.0.2",
    "python_dateutil>=2.6.0"
]

setup(
    name=NAME,
    version=VERSION,
    description="Transmission Ratings and Operating Limits Information Exchange (TROLIE)",
    author_email="maintainers@trolie.energy",
    url="",
    keywords=["OpenAPI", "Transmission Ratings and Operating Limits Information Exchange (TROLIE)"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
     Pursuant to FERC Order 881, Transmission Providers are required to support Ambient Adjusted Ratings (AARs) for most Transmission Facilities in their footprint.  In this context, Transmission Providers refers roughly to the FERC definition of Transmission Provider as any public utility that owns, operates, or controls facilities used for the transmission of electric energy in interstate commerce.  This could be said to apply to any entity that operates the transmission grid, including ISOs.  For the purpose of this API, Transmission Provider may be assumed to be more generic- it is really any entity that can receive AARs.  This API specification supports the information exchange necessary to coordinate forecasted and base facility ratings between a Transmission Provider and Ratings Providers.  The Transmission Provider is assumed to be the host of this information exchange.  A Ratings Provider is defined by this specification to be any entity that has pre-coordinated with the Transmission Provider hosting this information exchange to be the entity responsible for providing AARs on some set of Transmission Facilities known to the Transmission Provider. That pre-coordination is out-of-scope for this specification.  The language of this API makes a strict distinction between the terms rating and limit.  A limit is a validated value that is actively used to make operational decisions on the power grid.  This could be limits used by the EMS or real-time market in real-time, or it could be forecast limits used by look-ahead processes such as EMS study applications or the day-ahead market.  A rating, in contrast, is a calculated value from some process that is input to TROLIE (and by extension operating power systems at large) and may be selected for use as a limit after validation and dependent on operating conditions, time frame and the operational decisions being made.  Seasonal ratings, forecast rating proposals, and real-time rating proposals are all examples of ratings.  &lt;img src&#x3D;\&quot;images/TROLIE Ratings Provider interactions.excalidraw.png\&quot; alt&#x3D;\&quot;TROLIE Interactions by Ratings Provider\&quot; /&gt; 
    """
)

