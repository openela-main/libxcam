Name:		libxcam
Version:	1.2.0
Release:	1%{?dist}
Summary:	libXCam is a project for extended camera features and focus on image quality improvement and video analysis.

License:        ASL 2.0	
URL:		https://github.com/01org/libxcam/
#Source0:	Git source at: https://github.com/01org/libxcam/archive/release_%{version}.tar.gz
Source0:        %{name}-%{version}.tar.gz

BuildRequires: autoconf, automake, libtool
BuildRequires: ocl-icd-devel, beignet-devel, beignet
BuildRequires: libdrm, libdrm-devel

ExclusiveArch: x86_64 %{ix86}

%description
libXCam is a project for extended camera features 
and focus on image quality improvement and video analysis. 
There are lots features supported in image pre-processing, 
image post-processing and smart analysis. This library 
makes GPU/CPU/ISP working together to improve image quality. 
OpenCL is used to improve performance in different platforms.

%prep
%autosetup -n %{name}-release_%{version} 
autoreconf -vif

%build
%configure --disable-static 


%install
rm -rf $RPM_BUILD_ROOT
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%{_includedir}/xcam
%{_libdir}/libxcam*.so*
%{_libdir}/pkgconfig/libxcam.pc

%changelog
* Mon Jan 21 2019 Josef Ridky <jridky@redhat.com> -1.2.0-1
- exlclude arch to 32 an 64 bit arch (due beignet)

* Mon Nov 06 2017 Josef Ridky <jridky@redhat.com> -1.0.0-1
- Initial commit
