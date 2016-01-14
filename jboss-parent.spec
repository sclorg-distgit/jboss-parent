%global pkg_name jboss-parent
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:                 %{?scl_prefix}%{pkg_name}
Version:              6
Release:              12.9%{?dist}
Summary:              JBoss Parent POM
License:              LGPLv2+
URL:                  http://www.jboss.org/

# git clone git://github.com/jboss/jboss-parent-pom.git
# cd jboss-parent-pom/ && git archive --format=tar --prefix=jboss-parent-6/ 6 | xz > jboss-parent-6.tar.xz
Source0:              %{pkg_name}-%{version}.tar.xz
# Removing unavailable deps
Patch0:               %{pkg_name}-%{version}-deps.patch
BuildArch:            noarch

BuildRequires:        %{?scl_prefix_java_common}javapackages-tools
BuildRequires:        %{?scl_prefix_java_common}maven-local
BuildRequires:        %{?scl_prefix}maven-install-plugin
BuildRequires:        %{?scl_prefix}maven-javadoc-plugin
BuildRequires:        %{?scl_prefix}maven-release-plugin
BuildRequires:        %{?scl_prefix}maven-resources-plugin
BuildRequires:        %{?scl_prefix}maven-enforcer-plugin


%description
The Project Object Model files for JBoss packages.

%prep
%setup -q -n %{pkg_name}-%{version}
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%patch0 -p1
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%dir %{_mavenpomdir}/%{pkg_name}
%doc README.md

%changelog
* Thu Jan 15 2015 Michal Srb <msrb@redhat.com> - 6-12.9
- Fix directory ownership

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 6-12.8
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 6-12.7
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 6-12.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 6-12.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 6-12.4
- Mass rebuild 2014-02-18

* Fri Feb 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 6-12.3
- SCL-ize requires and build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 6-12.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 6-12.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 6-12
- Mass rebuild 2013-12-27

* Mon Aug 26 2013 Michal Srb <msrb@redhat.com> - 6-11
- Migrate away from mvn-rpmbuild (Resolves: #997506)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 6-9
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 19 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 6-7
- Simplify requires since they are only in depManagement

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 12 2011 Alexander Kurtakov <akurtako@redhat.com> 6-5
- Add missing BR.

* Tue Sep 20 2011 Marek Goldmann <mgoldman@redhat.com> 6-4
- Removed unavailable deps from POM

* Mon Aug 29 2011 Marek Goldmann <mgoldman@redhat.com> 6-3
- Added maven-surefire-provider-junit requires

* Thu Jul 28 2011 Marek Goldmann <mgoldman@redhat.com> 6-2
- Added build section
- Removed unnecessary sections and BR's

* Mon Jul 18 2011 Marek Goldmann <mgoldman@redhat.com> 6-1
- Upstream release: 6.

* Tue Jun 07 2011 Marek Goldmann <mgoldman@redhat.com> 6-0.1.beta2
- Initial packaging
