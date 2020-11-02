Name:    droid-hal-tools-logo
Version: 0.0.1
Release: 1
Summary: splash.img creation tool
License: MIT
Source:	 %{name}-%{version}.tar.bz2
Requires: python3-imaging

%description
%{summary}

%prep
%autosetup

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -D -m 755 logo_gen.py %{buildroot}%{_bindir}

%files
%defattr(-,root,root,-)
%{_bindir}/logo_gen.py

