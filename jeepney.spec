#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jeepney
Version  : 0.4
Release  : 5
URL      : https://files.pythonhosted.org/packages/16/1d/74adf3b164a8d19a60d0fcf706a751ffa2a1eaa8e5bbb1b6705c92a05263/jeepney-0.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/16/1d/74adf3b164a8d19a60d0fcf706a751ffa2a1eaa8e5bbb1b6705c92a05263/jeepney-0.4.tar.gz
Summary  : Low-level, pure Python DBus protocol wrapper.
Group    : Development/Tools
License  : MIT
Requires: jeepney-python3
Requires: jeepney-license
Requires: jeepney-python
BuildRequires : buildreq-distutils3

%description
This is a low-level, pure Python DBus protocol client. It has an `I/O-free
<https://sans-io.readthedocs.io/>`__ core, and integration modules for different
event loops.

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

%description python3
python3 components for the jeepney package.


%prep
%setup -q -n jeepney-0.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1537796300
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/jeepney
cp LICENSE %{buildroot}/usr/share/doc/jeepney/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/jeepney/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
