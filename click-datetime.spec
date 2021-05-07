#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : click-datetime
Version  : 0.2.0
Release  : 14
URL      : https://github.com/click-contrib/click-datetime/archive/0.2.0.tar.gz
Source0  : https://github.com/click-contrib/click-datetime/archive/0.2.0.tar.gz
Summary  : Datetime type support for click.
Group    : Development/Tools
License  : Python-2.0
Requires: click-datetime-python = %{version}-%{release}
Requires: click-datetime-python3 = %{version}-%{release}
Requires: click
Requires: wheel
BuildRequires : buildreq-distutils3
BuildRequires : click
BuildRequires : wheel

%description
# Click Datetime (in progress)
Click support for Python's Datetime types to allow developers to easy parse date strings as
parameters to Python commandline tools.

%package python
Summary: python components for the click-datetime package.
Group: Default
Requires: click-datetime-python3 = %{version}-%{release}

%description python
python components for the click-datetime package.


%package python3
Summary: python3 components for the click-datetime package.
Group: Default
Requires: python3-core
Provides: pypi(click_datetime)
Requires: pypi(click)

%description python3
python3 components for the click-datetime package.


%prep
%setup -q -n click-datetime-0.2.0
cd %{_builddir}/click-datetime-0.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583520926
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
