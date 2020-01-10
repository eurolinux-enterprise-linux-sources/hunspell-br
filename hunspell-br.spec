Name: hunspell-br
Summary: Breton hunspell dictionaries
Epoch: 1
Version: 0.8
Release: 4%{?dist}
Group: Applications/Text
URL: http://www.drouizig.org/
Source: http://extensions.services.openoffice.org/e-files/2207/6/dict-br_0.8.oxt
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv2+
BuildArch: noarch

Requires: hunspell

%description
Breton hunspell dictionaries.

%prep
%setup -q -c -n hunspell-br-%{version}

%build
chmod -x dictionaries/*

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/br_FR.* $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSES-en.txt package-description.txt
%{_datadir}/myspell/*

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 17 2011 Caolán McNamara <caolanm@redhat.com> - 1:0.8-1
- latest version

* Thu Jun 23 2011 Caolán McNamara <caolanm@redhat.com> - 1:0.7-1
- latest version

* Fri Mar 18 2011 Caolán McNamara <caolanm@redhat.com> - 1:0.5-1
- latest version

* Fri Feb 19 2010 Caolan McNamara <caolanm@redhat.com> - 1:0.3-1
- latest version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 16 2009 Caolan McNamara <caolanm@redhat.com> - 1:0.2-1
- latest version

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20030417-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Oct 13 2008 Caolan McNamara <caolanm@redhat.com> - 0.20030417-1
- initial version
