#!/usr/bin/env python

import distutils.core
import catkin_pkg.python_setup

d = catkin_pkg.python_setup.generate_distutils_setup(
	packages=['script_server_tutorial'],
	package_dir={'script_server_tutorial': 'ros/src'}
)

distutils.core.setup(**d)

