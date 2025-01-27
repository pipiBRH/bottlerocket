Name: ethan
Version: 0.1.0
Release: 1
Summary: A simple ethan World for Bottlerocket
License: MIT
Source: none

Source1: ethan
Source2: ethan.service

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
A ethan World program in Go, installed on Bottlerocket.

%prep
echo "No prep needed."

%build
echo "No build needed."

%install
install -d %{buildroot}%{_cross_bindir}
install -m 0755 %{SOURCE1} %{buildroot}%{_cross_bindir}

install -d %{buildroot}%{_cross_unitdir}
install -m 0644 %{SOURCE2} %{buildroot}%{_cross_unitdir}


%post
systemctl enable ethan.service || true
systemctl start ethan.service || true

%preun
echo "No preun needed."


%postun
echo "No postun needed."


%files
%{_cross_unitdir}/ethan.service
/x86_64-bottlerocket-linux-gnu/sys-root/usr/share/licenses/ethan/attribution.txt
%{_cross_bindir}/host-ctr/ethan

