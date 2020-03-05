#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jeepney
Version  : 0.4.3
Release  : 12
URL      : https://files.pythonhosted.org/packages/74/24/9b720cc6b2a73c908896a0ed64cb49780dcfbf4964e23a725aa6323f4452/jeepney-0.4.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/74/24/9b720cc6b2a73c908896a0ed64cb49780dcfbf4964e23a725aa6323f4452/jeepney-0.4.3.tar.gz
Summary  : Low-level, pure Python DBus protocol wrapper.
Group    : Development/Tools
License  : MIT
Requires: jeepney-license = %{version}-%{release}
Requires: jeepney-python = %{version}-%{release}
Requires: jeepney-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
This is a low-level, pure Python DBus protocol client. It has an `I/O-free
<https://sans-io.readthedocs.io/>`__ core, and integration modules for different
event loops.

DBus is an inter-process communication system, mainly used in Linux.

`Jeepney docs on Readthedocs <https://jeepney.readthedocs.io/en/latest/>`__

This project is experimental, and there are a
number of `more mature Python DBus bindings <https://www.freedesktop.org/wiki/Software/DBusBindings/#python>`__.

%package license
Summary: license components for the jeepney package.
Group: Default

%description license
license components for the jeepney package.


%package python
Summary: python components for the jeepney package.
Group: Default
Requires: jeepney-python3 = %{version}-%{release}

%description python
python components for the jeepney package.


%package python3
Summary: python3 components for the jeepney package.
Group: Default
Requires: python3-core
Provides: pypi(jeepney)
Requires: pypi(testpath)

%description python3
python3 components for the jeepney package.


%prep
%setup -q -n jeepney-0.4.3
cd %{_builddir}/jeepney-0.4.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583435928
# -Werror is for werrorists
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
mkdir -p %{buildroot}/usr/share/package-licenses/jeepney
cp %{_builddir}/jeepney-0.4.3/LICENSE %{buildroot}/usr/share/package-licenses/jeepney/b2f7e71b77f14f21cd693e1c6fbe7236a8deac5f
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/jeepney/b2f7e71b77f14f21cd693e1c6fbe7236a8deac5f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
