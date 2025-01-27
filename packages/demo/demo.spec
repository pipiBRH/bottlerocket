Name: demo
Version: 0.1.0
Release: 1
Summary: A simple demo World for Bottlerocket
License: MIT
Source: none

Source1: demo
Source2: demo.service

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
A demo World program in Go, installed on Bottlerocket.

%prep
echo "No prep needed."

%build
echo "No build needed."

%install
install -d %{buildroot}/usr/local/bin
install -m 0755 %{SOURCE1} %{buildroot}/usr/local/bin/demo

install -d %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/demo.service


%post
systemctl enable demo.service || true
systemctl start demo.service || true

%preun
echo "No preun needed."


%postun
echo "No postun needed."


%files
/usr/local/bin/demo
/usr/lib/systemd/system/demo.service
/x86_64-bottlerocket-linux-gnu/sys-root/usr/share/licenses/demo/attribution.txt
