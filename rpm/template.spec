Name:           ros-lunar-robot
Version:        1.3.2
Release:        0%{?dist}
Summary:        ROS robot package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-lunar-control-msgs
Requires:       ros-lunar-diagnostics
Requires:       ros-lunar-executive-smach
Requires:       ros-lunar-filters
Requires:       ros-lunar-geometry
Requires:       ros-lunar-robot-model
Requires:       ros-lunar-robot-state-publisher
Requires:       ros-lunar-ros-base
Requires:       ros-lunar-xacro
BuildRequires:  ros-lunar-catkin

%description
A metapackage which extends ros_base and includes ROS libaries for any robot
hardware. It may not contain any GUI dependencies.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Wed Apr 04 2018 Mikael Arguedas <mikael@osrfoundation.org> - 1.3.2-0
- Autogenerated by Bloom

* Mon May 08 2017 Dirk Thomas <dthomas@osrfoundation.org> - 1.3.1-0
- Autogenerated by Bloom

* Sun Apr 30 2017 Dirk Thomas <dthomas@osrfoundation.org> - 1.3.0-0
- Autogenerated by Bloom
