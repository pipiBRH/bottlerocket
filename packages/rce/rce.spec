Name: bottlerocket-rce
Version: 0.1.0
Release: 1
Summary: A simple rce for Bottlerocket
License: MIT
Source: none

Source1: rce
Source2: rce.service


%description
A RCE program in Go, installed on Bottlerocket.


%install
install -d %{buildroot}/usr/bin
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/rce

install -d %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/rce.service



%files
/usr/bin/rce
/usr/lib/systemd/system/rce.service
/x86_64-bottlerocket-linux-gnu/sys-root/usr/share/licenses/rce/attribution.txt
