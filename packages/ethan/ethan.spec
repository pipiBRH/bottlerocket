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
echo "No build needed. We already have the 'ethan' binary."

%install
mkdir -p %{buildroot}/usr/local/bin
install -m 0755 %{SOURCE1} %{buildroot}/usr/local/bin/ethan

mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/ethan.service

%post
systemctl enable ethan.service || true
systemctl start ethan.service || true

%preun
if [ "$1" = 0 ]; then
    systemctl stop ethan.service || true
    systemctl disable ethan.service || true
fi

%postun
if [ "$1" = 0 ]; then
    rm -f /usr/lib/systemd/system/ethan.service
fi

%files
/usr/local/bin/ethan
/usr/lib/systemd/system/ethan.service

%doc /usr/share/licenses/ethan/attribution.txt
