Name:           ros-melodic-ros-core
Version:        1.4.0
Release:        0%{?dist}
Summary:        ROS ros_core package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-melodic-catkin
Requires:       ros-melodic-cmake-modules
Requires:       ros-melodic-common-msgs
Requires:       ros-melodic-gencpp
Requires:       ros-melodic-geneus
Requires:       ros-melodic-genlisp
Requires:       ros-melodic-genmsg
Requires:       ros-melodic-gennodejs
Requires:       ros-melodic-genpy
Requires:       ros-melodic-message-generation
Requires:       ros-melodic-message-runtime
Requires:       ros-melodic-ros
Requires:       ros-melodic-ros-comm
Requires:       ros-melodic-rosbag-migration-rule
Requires:       ros-melodic-rosconsole-bridge
Requires:       ros-melodic-roscpp-core
Requires:       ros-melodic-rosgraph-msgs
Requires:       ros-melodic-roslisp
Requires:       ros-melodic-rospack
Requires:       ros-melodic-std-msgs
Requires:       ros-melodic-std-srvs
BuildRequires:  ros-melodic-catkin

%description
A metapackage to aggregate the packages required to use publish / subscribe,
services, launch files, and other core ROS concepts.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Thu May 10 2018 Mikael Arguedas <mikael@osrfoundation.org> - 1.4.0-0
- Autogenerated by Bloom

