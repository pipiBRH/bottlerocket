Name: bottlerocket-ethan
Version: 0.1.0
Release: 1
Summary: A simple ethan World for Bottlerocket
License: MIT
Source: none

Source1: ethan
Source2: ethan.service


%description
A ethan World program in Go, installed on Bottlerocket.

%prep
echo "No prep needed."

%build
echo "No build needed."

%install
install -d %{buildroot}/usr/bin
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ethan

install -d %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/ethan.service


%post
echo "post needed."

%preun
echo "No preun needed."


%postun
echo "No postun needed."


%files
/usr/bin/ethan
/usr/lib/systemd/system/ethan.service
/x86_64-bottlerocket-linux-gnu/sys-root/usr/share/licenses/ethan/attribution.txt
