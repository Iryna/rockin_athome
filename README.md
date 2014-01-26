rockin_athome
=============

Care-O-bot 3 installation for the the RoCKIn camp 2014

## pre-requisite:

		sudo apt-get install python-rosinstall python-setuptools git python-usb ros-hydro-pr2-mechanism-diagnostics

- set up your working environment (.bashrc)
 
		export ROBOT=cob3-1
		export ROBOT_ENV=ipa-apartment


## Installation

- in your <catkin_workspace>/src directory

		git clone https://github.com/mas-group/rockin_athome.git
		cd rockin_athome 
		rosinstall ../ /opt/ros/hydro ./repository.rosinstall
		cd ..
		catkin_make

