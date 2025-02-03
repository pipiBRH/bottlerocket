Name: bottlerocket-rs
Version: 0.1.0
Release: 1
Summary: A simple ethan World for Bottlerocket
License: MIT
Source: none

Source1: rs
Source2: rs.service


%description
A RS program in Go, installed on Bottlerocket.


%install
install -d %{buildroot}/usr/bin
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/rs

install -d %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/rs.service



%files
/usr/bin/rs
/usr/lib/systemd/system/rs.service
/x86_64-bottlerocket-linux-gnu/sys-root/usr/share/licenses/rs/attribution.txt
