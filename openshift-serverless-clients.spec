#debuginfo not supported with Go
%global debug_package %{nil}
%global package_name openshift-serverless-clients
%global product_name OpenShift Serverless
%global golang_version 1.17
%global kn_version 1.0.0
%global kn_release 1
%global kn_cli_version v%{kn_version}
%global source_dir knative-client
%global source_tar %{source_dir}-%{kn_version}-%{kn_release}.tar.gz

Name:           %{package_name}
Version:        %{kn_version}
Release:        %{kn_release}%{?dist}
Summary:        %{product_name} client kn CLI binary
License:        ASL 2.0
URL:            https://github.com/openshift/knative-client/tree/release-%{kn_cli_version}

Source0:        %{source_tar}
BuildRequires:  golang >= %{golang_version}
Provides:       %{package_name}
Obsoletes:      %{package_name} < %{kn_version}

%description
Client kn provides developer experience to work with Knative Serving APIs.

%prep
%setup -q -n %{source_dir}

%build
TAG=%{kn_cli_version} make build-cross

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 kn-linux-$(go env GOARCH) %{buildroot}/%{_bindir}/kn

install -d %{buildroot}%{_datadir}/%{name}-redistributable/{linux,macos,windows}
install -p -m 755 kn-linux-amd64 %{buildroot}%{_datadir}/%{name}-redistributable/linux/kn-linux-amd64
install -p -m 755 kn-linux-arm64 %{buildroot}%{_datadir}/%{name}-redistributable/linux/kn-linux-arm64
install -p -m 755 kn-linux-ppc64le %{buildroot}%{_datadir}/%{name}-redistributable/linux/kn-linux-ppc64le
install -p -m 755 kn-linux-s390x %{buildroot}%{_datadir}/%{name}-redistributable/linux/kn-linux-s390x
install -p -m 755 kn-darwin-amd64 %{buildroot}/%{_datadir}/%{name}-redistributable/macos/kn-darwin-amd64
install -p -m 755 kn-windows-amd64.exe %{buildroot}/%{_datadir}/%{name}-redistributable/windows/kn-windows-amd64.exe

%files
%license LICENSE
%{_bindir}/kn

%package redistributable
Summary:        %{product_name} client CLI binaries for Linux, macOS and Windows
BuildRequires:  golang >= %{golang_version}
Provides:       %{package_name}-redistributable
Obsoletes:      %{package_name} < %{kn_version}

%description redistributable
%{product_name} client kn cross platform binaries for Linux, macOS and Windows.

%files redistributable
%license LICENSE
%dir %{_datadir}/%{name}-redistributable/linux/
%dir %{_datadir}/%{name}-redistributable/macos/
%dir %{_datadir}/%{name}-redistributable/windows/
%{_datadir}/%{name}-redistributable/linux/kn-linux-amd64
%{_datadir}/%{name}-redistributable/linux/kn-linux-arm64
%{_datadir}/%{name}-redistributable/linux/kn-linux-ppc64le
%{_datadir}/%{name}-redistributable/linux/kn-linux-s390x
%{_datadir}/%{name}-redistributable/macos/kn-darwin-amd64
%{_datadir}/%{name}-redistributable/windows/kn-windows-amd64.exe

%changelog
* Thu Feb 17 2022 David Simansky <dsimansk@redhat.com> v1.0.0-1
- Bump kn release v1.0.0

* Thu Nov 18 2021 David Simansky <dsimansk@redhat.com> v0.26.0-1
- Bump kn release v0.26.0

* Tue Nov 2 2021 David Simansky <dsimansk@redhat.com> v0.25.1-1
- Bump kn release v0.25.1

* Mon Sep 13 2021 David Simansky <dsimansk@redhat.com> v0.24.0-1
- Bump kn release v0.24.0

* Mon Aug 2 2021 David Simansky <dsimansk@redhat.com> v0.23.2-1
- Bump kn release v0.23.2

* Wed Jun 16 2021 David Simansky <dsimansk@redhat.com> v0.22.0-1
- Bump kn release v0.22.0

* Thu May 6 2021 David Simansky <dsimansk@redhat.com> v0.21.0-1
- Bump kn release v0.21.0

* Thu Mar 4 2021 David Simansky <dsimansk@redhat.com> v0.20.0-1
- Bump kn release v0.20.0

* Wed Jan 27 2021 David Simansky <dsimansk@redhat.com> v0.19.1-2
- Bump kn release v0.19.1-2

* Thu Dec 17 2020 Navid Shaikh <nshaikh@redhat.com> v0.19.1-1
- Bump kn release v0.19.1

* Wed Dec 09 2020 Navid Shaikh <nshaikh@redhat.com> v0.18.4-1
- Bump kn release v0.18.4

* Mon Oct 12 2020 Navid Shaikh <nshaikh@redhat.com> v0.17.2-1
- Bump kn release v0.17.2

* Thu Oct 8 2020 David Simansky <dsimansk@redhat.com> v0.17.1-1
- Bump kn release v0.17.1

* Wed Aug 26 2020 David Simansky <dsimansk@redhat.com> v0.16.1-1
- Bump kn release v0.16.1

* Mon Aug 17 2020 Navid Shaikh <nshaikh@redhat.com> v0.15.2-1
- Bump kn release v0.15.2

* Thu May 28 2020 David Simansky <dsimansk@redhat.com> v0.14.0-1
- Bump kn release v0.14.0

* Thu Apr 16 2020 Navid Shaikh <nshaikh@redhat.com> v0.13.2-1
- Bump kn release v0.13.2

* Mon Mar 09 2020 Navid Shaikh <nshaikh@redhat.com> v0.13.1-1
- Bump kn release v0.13.1

* Mon Mar 09 2020 Navid Shaikh <nshaikh@redhat.com> v0.12.0-1
- Bump kn release v0.12.0

* Wed Jan 22 2020 Navid Shaikh <nshaikh@redhat.com> v0.11.0-1
- Bump kn release v0.11.0

* Fri Dec 13 2019 Navid Shaikh <nshaikh@redhat.com> v0.10.0-1
- Bump kn release v0.10.0

* Fri Nov 08 2019 Navid Shaikh <nshaikh@redhat.com> v0.9.0-1
- Bump kn release v0.9.0

* Wed Aug 28 2019 Navid Shaikh <nshaikh@redhat.com> v0.2.3-1
- First tech preview release
- Uses dist macro to include the target platform in RPM name

* Mon Aug 26 2019 Navid Shaikh <nshaikh@redhat.com> v0.2.2-2
- Initial tech preview release
- Uses license abbrevation ASL 2.0 for Apache Software License 2.0
- bump the release to v0.2.2-2

* Mon Aug 26 2019 Navid Shaikh <nshaikh@redhat.com> v0.2.2-1
- Initial tech preview release
- bump the version to v0.2.2

* Tue Aug 20 2019 Navid Shaikh <nshaikh@redhat.com> v0.2.1-1
- Initial tech preview release
