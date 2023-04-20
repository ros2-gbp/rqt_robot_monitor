%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/iron/.*$
%global __requires_exclude_from ^/opt/ros/iron/.*$

Name:           ros-iron-rqt-robot-monitor
Version:        1.0.5
Release:        3%{?dist}%{?release_suffix}
Summary:        ROS rqt_robot_monitor package

License:        BSD
URL:            http://wiki.ros.org/rqt_robot_monitor
Source0:        %{name}-%{version}.tar.gz

Requires:       python%{python3_pkgversion}-rospkg
Requires:       ros-iron-diagnostic-msgs
Requires:       ros-iron-python-qt-binding >= 0.2.19
Requires:       ros-iron-qt-gui
Requires:       ros-iron-qt-gui-py-common
Requires:       ros-iron-rclpy
Requires:       ros-iron-rqt-gui
Requires:       ros-iron-rqt-gui-py
Requires:       ros-iron-rqt-py-common
Requires:       ros-iron-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-iron-ros-workspace
BuildRequires:  ros-iron-rosidl-default-generators
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
rqt_robot_monitor displays diagnostics_agg topics messages that are published by
diagnostic_aggregator. rqt_robot_monitor is a direct port to rqt of
robot_monitor. All diagnostics are fall into one of three tree panes depending
on the status of diagnostics (normal, warning, error/stale). Status are shown in
trees to represent their hierarchy. Worse status dominates the higher level
status. Ex. 'Computer' category has 3 sub devices. 2 are green but 1 is error.
Then 'Computer' becomes error. You can look at the detail of each status by
double-clicking the tree nodes. Currently re-usable API to other pkgs are not
explicitly provided.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/iron"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/iron

%changelog
* Thu Apr 20 2023 Aaron Blasdel <ablasdel@gmail.com> - 1.0.5-3
- Autogenerated by Bloom

* Tue Mar 21 2023 Aaron Blasdel <ablasdel@gmail.com> - 1.0.5-2
- Autogenerated by Bloom

