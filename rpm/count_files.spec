Name:		count_files
Version:	1.0
Release:	1%{?dist}
Summary:	Script to count files in /etc
License:	MIT
BuildArch:	noarch
Requires:	bash findutils coreutils
Source0:	count_files.sh

%description
This package provides a Bash script that counts files in /etc and its subdirectories.

%prep

%build

%install
install -D -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/count_files

%files
%{_bindir}/count_files

%changelog
* Mon Oct 20 2025 Mykola Babko <babko.mykola@stu.cn.ua> - 1.0-1
- Initial build
