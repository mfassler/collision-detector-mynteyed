
Name:		mynteyed
Version:	2.3.9
Release:	1%{?dist}
Summary:	Mynteye D (depth) SDK and Utils

Group:		Development/Languages
License:	Apache
URL:		https://github.com/slightech/MYNT-EYE-S-SDK/

BuildRequires: cmake libusb-devel


%description
Library (and some utils) for the Mynt-Eye depth cameras


%prep
%setup -D -c -T -n slightech
if [ ! -d MYNT-EYE-D-SDK ]; then
	git clone https://github.com/slightech/MYNT-EYE-D-SDK.git
fi
cd MYNT-EYE-D-SDK
git checkout 3rdparty/eSPDI/linux/x64/lib*
git checkout master
git pull

###
### This is from:  https://github.com/slightech/MYNT-EYE-D-SDK/issues/13
cd 3rdparty/eSPDI/linux/x64
git checkout libeSPDI*
printf '\x02' | dd of=libeSPDI.so.3.0.24.05 bs=1 seek=145474 count=1 conv=notrunc
###



%build
cd MYNT-EYE-D-SDK
rm -rf build
mkdir build
cd build
cmake .. \
  -DCMAKE_BUILD_TYPE=RELEASE \
  -DCMAKE_INSTALL_PREFIX=/usr \

make %{?_smp_mflags}


%install
cd MYNT-EYE-D-SDK/build
make install DESTDIR=%{buildroot}

## TODO:  cmake files need to move "usr/lib/" to "usr/lib64"
cd %{buildroot}/usr
mv lib lib64
cd lib64
mv 3rdparty/* ./
rmdir 3rdparty
cd cmake/mynteyed
sed -i 's/\/usr\/lib\//\/usr\/lib64\//g' *.cmake


%files
#%doc
%{_includedir}/mynt*
%{_libdir}/lib*
%{_libdir}/cmake/*

%changelog

