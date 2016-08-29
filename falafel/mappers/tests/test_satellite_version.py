from falafel.tests import context_wrap
from falafel.mappers.satellite_version import get_sat_version

installed_rpms_5 = """
satellite-branding-5.5.0.22-1.el6sat.noarch                 Wed May 18 14:50:17 2016
satellite-doc-indexes-5.6.0-2.el6sat.noarch                 Wed May 18 14:47:49 2016
satellite-repo-5.6.0.3-1.el6sat.noarch                      Wed May 18 14:37:34 2016
satellite-schema-5.6.0.10-1.el6sat.noarch                   Wed May 18 14:53:03 2016
satyr-0.16-2.el6.x86_64                                     Wed May 18 14:16:08 2016
scdb-1.15.8-1.el6sat.noarch                                 Wed May 18 14:48:14 2016
scl-utils-20120927-27.el6_6.x86_64                          Wed May 18 14:18:16 2016
SDL-1.2.14-6.el6.x86_64                                     Wed May 18 14:16:25 2016
"""

installed_rpms_61 = """
foreman-1.7.2.53-1.el7sat.noarch                            Wed May 18 14:16:25 2016
scl-utils-20120927-27.el6_6.x86_64                          Wed May 18 14:18:16 2016
SDL-1.2.14-6.el6.x86_64                                     Wed May 18 14:16:25 2016
satellite-installer-6.2.0.11-1.el7sat.noarch                Wed May 18 14:16:25 2016
"""

installed_rpms_62 = """
foreman-1.11.0.53-1.el7sat.noarch                           Wed May 18 14:16:25 2016
scl-utils-20120927-27.el7_6.x86_64                          Wed May 18 14:18:16 2016
SDL-1.2.14-6.el7.x86_64                                     Wed May 18 14:16:25 2016
satellite-installer-6.2.0.11-1.el7sat.noarch                Wed May 18 14:16:25 2016
"""

installed_rpms_60 = """
foreman-1.6.0.53-1.el6sat.noarch                            Wed May 18 14:16:25 2016
scl-utils-20120927-27.el6_6.x86_64                          Wed May 18 14:18:16 2016
SDL-1.2.14-6.el6.x86_64                                     Wed May 18 14:16:25 2016
"""

satellite_version = """
COMMAND> cat /usr/share/foreman/lib/satellite/version.rb

module Satellite
  VERSION = "6.1.3"
end
"""

no_sat = """
scdb-1.15.8-1.el6sat.noarch                                 Wed May 18 14:48:14 2016
scl-utils-20120927-27.el6_6.x86_64                          Wed May 18 14:18:16 2016
SDL-1.2.14-6.el6.x86_64                                     Wed May 18 14:16:25 2016
"""


def test_get_sat5_version():
    result = get_sat_version(context_wrap(installed_rpms_5, path=''))
    assert result == "5.6.0.10-1.el6sat.noarch"


def test_get_sat6_version():
    result = get_sat_version(context_wrap(satellite_version, path='satellite_version'))
    assert result == "6.1.3"

    result = get_sat_version(context_wrap(installed_rpms_60, path=''))
    assert result == "6.0.8"

    result = get_sat_version(context_wrap(installed_rpms_61, path=''))
    assert result == "6.1.7"

    result = get_sat_version(context_wrap(installed_rpms_62, path='satellite'))
    assert result == "6.2.0.11-1.el7sat.noarch"


def test_get_no_sat_version():
    result = get_sat_version(context_wrap(no_sat, path='satellite_version'))
    assert result is None

    result = get_sat_version(context_wrap(satellite_version, path='satellite'))
    assert result is None
