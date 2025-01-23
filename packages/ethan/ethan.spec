Name: ethan
Version: 0.1.0
Release: 1
Summary: A simple ethan World for Bottlerocket
License: MIT
Source: none

Source1: ethan.go
Source2: ethan.service

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
A ethan World program in Go, installed on Bottlerocket.

%prep
echo "No prep needed."

%build
CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o ethan %{SOURCE1}

%install
echo "aaaaaaaaa"
mkdir -p %{buildroot}/usr/local/bin
install -m 0755 ethan %{buildroot}/usr/local/bin/ethan

mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/ethan.service

%post
systemctl enable ethan.service || true
systemctl start ethan.service || true

%preun
echo "No preun needed."


%postun
echo "No postun needed."


%files
/usr/local/bin/ethan
/usr/lib/systemd/system/ethan.service
