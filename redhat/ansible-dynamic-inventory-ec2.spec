Summary: Ansible dynamic inventory script and config for Amazon EC2
Name: ansible-dynamic-inventory-ec2
Version: 2.4
Release: 2
License: GPL-3.0
Source: .
URL: https://github.com/appuio/ansible-dynamic-inventory-ec2
Vendor: VSHN AG
Packager: Gabriel Mainberger <gabriel.mainberger@vshn.ch>
Requires: ansible >= 2.4
Requires: python-boto >= 2.24.0

%package config
Summary: Config file for the Ansible dynamic inventory script
Group: Development/Libraries

%description
Specific script for the dynamic inventoy of Amazon EC2, which is part of the source release, but not in the standard RPM

%description config
Config file for the EC2 inventory script

%prep
%setup -cT
cp -v -R -a %SOURCE0/* .

%build
make 'PYTHON_SITELIB_DIR=%{python_sitelib}' 'SYSCONFDIR=%{_sysconfdir}'

%install
%make_install 'PYTHON_SITELIB_DIR=%{python_sitelib}' 'SYSCONFDIR=%{_sysconfdir}'

%files
%{python_sitelib}/ansible/contrib/inventory/*

%config(noreplace) %{_sysconfdir}/ansible/ec2.ini

%changelog
* Wed Mar 15 2018 Gabriel Mainberger <gabriel.mainberger@vshn.ch> 2.4-2
- Fixed file execution permission on ec2.py

* Mon Mar 12 2018 Gabriel Mainberger <gabriel.mainberger@vshn.ch> 2.4-1
- Initial release for Red Hat

# vim: set sw=2 sts=2 et :
