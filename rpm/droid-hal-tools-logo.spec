Name:    droid-hal-tools-logo	
Version: 0.0.1
Release: 1
Summary: splash.img creation tool	

Group:   System
License: MIT	
Source:	 %{name}-%{version}.tar.bz2

Requires: python-imaging	

%description
%{summary}

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin/
install -D -m 755 logo_gen.py %{buildroot}/usr/bin/

%files
%defattr(-,root,root,-)
/usr/bin/logo_gen.py

