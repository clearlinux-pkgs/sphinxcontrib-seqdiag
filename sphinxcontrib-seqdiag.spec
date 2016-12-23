#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sphinxcontrib-seqdiag
Version  : 0.8.5
Release  : 11
URL      : https://pypi.python.org/packages/source/s/sphinxcontrib-seqdiag/sphinxcontrib-seqdiag-0.8.5.tar.gz
Source0  : https://pypi.python.org/packages/source/s/sphinxcontrib-seqdiag/sphinxcontrib-seqdiag-0.8.5.tar.gz
Summary  : Sphinx "seqdiag" extension
Group    : Development/Tools
License  : BSD-2-Clause
Requires: sphinxcontrib-seqdiag-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
=====================
sphinxcontrib-seqdiag
=====================
.. image:: https://travis-ci.org/blockdiag/sphinxcontrib-seqdiag.svg?branch=master
:target: https://travis-ci.org/blockdiag/sphinxcontrib-seqdiag

%package python
Summary: python components for the sphinxcontrib-seqdiag package.
Group: Default

%description python
python components for the sphinxcontrib-seqdiag package.


%prep
%setup -q -n sphinxcontrib-seqdiag-0.8.5

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
