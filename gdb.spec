#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x92EDB04BFF325CF3 (brobecker@adacore.com)
#
%define keepstatic 1
Name     : gdb
Version  : 10.2
Release  : 297
URL      : https://mirrors.kernel.org/gnu/gdb/gdb-10.2.tar.xz
Source0  : https://mirrors.kernel.org/gnu/gdb/gdb-10.2.tar.xz
Source1  : https://mirrors.kernel.org/gnu/gdb/gdb-10.2.tar.xz.sig
Summary  : zlib compression library
Group    : Development/Tools
License  : BSL-1.0 GFDL-1.1 GPL-1.0+ GPL-2.0 GPL-2.0+ GPL-3.0 GPL-3.0+ LGPL-2.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0 Public-Domain
Requires: gdb-bin = %{version}-%{release}
Requires: gdb-data = %{version}-%{release}
Requires: gdb-info = %{version}-%{release}
Requires: gdb-license = %{version}-%{release}
Requires: gdb-man = %{version}-%{release}
BuildRequires : binutils-dev
BuildRequires : bison
BuildRequires : buildreq-golang
BuildRequires : dejagnu
BuildRequires : expat-dev
BuildRequires : expect
BuildRequires : flex
BuildRequires : gcc-libgcc32
BuildRequires : gettext
BuildRequires : gfortran
BuildRequires : glibc-dev32
BuildRequires : glibc-locale
BuildRequires : glibc-staticdev
BuildRequires : libxslt-bin
BuildRequires : mpfr-dev
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(zlib)
BuildRequires : processor-trace-dev
BuildRequires : procps-ng
BuildRequires : python3-dev
BuildRequires : sed
BuildRequires : tcl
BuildRequires : texinfo
BuildRequires : xz-dev

%description
This directory contains various GNU compilers, assemblers, linkers,
debuggers, etc., plus their support routines, definitions, and documentation.

%package bin
Summary: bin components for the gdb package.
Group: Binaries
Requires: gdb-data = %{version}-%{release}
Requires: gdb-license = %{version}-%{release}

%description bin
bin components for the gdb package.


%package data
Summary: data components for the gdb package.
Group: Data

%description data
data components for the gdb package.


%package dev
Summary: dev components for the gdb package.
Group: Development
Requires: gdb-bin = %{version}-%{release}
Requires: gdb-data = %{version}-%{release}
Provides: gdb-devel = %{version}-%{release}
Requires: gdb = %{version}-%{release}

%description dev
dev components for the gdb package.


%package info
Summary: info components for the gdb package.
Group: Default

%description info
info components for the gdb package.


%package license
Summary: license components for the gdb package.
Group: Default

%description license
license components for the gdb package.


%package man
Summary: man components for the gdb package.
Group: Default

%description man
man components for the gdb package.


%package staticdev
Summary: staticdev components for the gdb package.
Group: Default
Requires: gdb-dev = %{version}-%{release}

%description staticdev
staticdev components for the gdb package.


%prep
%setup -q -n gdb-10.2
cd %{_builddir}/gdb-10.2

%build
## build_prepend content
export LDFLAGS="-Wl,--whole-archive /usr/lib64/haswell/libpython3.9.so -Wl,--no-whole-archive"
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1619383922
unset LD_AS_NEEDED
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -fzero-call-used-regs=used "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -fzero-call-used-regs=used "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -fzero-call-used-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -fzero-call-used-regs=used "
%configure  --disable-rpath \
--enable-plugins \
--enable-static \
--enable-targets=%{_arch}-unknown-linux-gnu \
--enable-tui \
--target=%{_arch}-generic-linux-gnu \
--with-intel-pt \
--with-python=yes \
--with-separate-debug-dir=/usr/lib/debug \
--with-system-zlib \
PYTHON=/usr/bin/python3
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1619383922
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gdb
cp %{_builddir}/gdb-10.2/COPYING %{buildroot}/usr/share/package-licenses/gdb/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1
cp %{_builddir}/gdb-10.2/COPYING.LIB %{buildroot}/usr/share/package-licenses/gdb/0e8e850b0580fbaaa0872326cb1b8ad6adda9b0d
cp %{_builddir}/gdb-10.2/COPYING3 %{buildroot}/usr/share/package-licenses/gdb/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/gdb-10.2/COPYING3.LIB %{buildroot}/usr/share/package-licenses/gdb/e7d563f52bf5295e6dba1d67ac23e9f6a160fab9
cp %{_builddir}/gdb-10.2/bfd/COPYING %{buildroot}/usr/share/package-licenses/gdb/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/gdb-10.2/gdb/COPYING %{buildroot}/usr/share/package-licenses/gdb/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/gdb-10.2/include/COPYING %{buildroot}/usr/share/package-licenses/gdb/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1
cp %{_builddir}/gdb-10.2/include/COPYING3 %{buildroot}/usr/share/package-licenses/gdb/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/gdb-10.2/libiberty/COPYING.LIB %{buildroot}/usr/share/package-licenses/gdb/597bf5f9c0904bd6c48ac3a3527685818d11246d
cp %{_builddir}/gdb-10.2/libiberty/copying-lib.texi %{buildroot}/usr/share/package-licenses/gdb/79747e6fe064f75103cb65ef01a06c650c39994e
cp %{_builddir}/gdb-10.2/readline/readline/COPYING %{buildroot}/usr/share/package-licenses/gdb/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/gdb-10.2/sim/arm/COPYING %{buildroot}/usr/share/package-licenses/gdb/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/gdb-10.2/sim/ppc/COPYING %{buildroot}/usr/share/package-licenses/gdb/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/gdb-10.2/sim/ppc/COPYING.LIB %{buildroot}/usr/share/package-licenses/gdb/5fb362ef1680e635fe5fb212b55eef4db9ead48f
cp %{_builddir}/gdb-10.2/zlib/contrib/dotzlib/LICENSE_1_0.txt %{buildroot}/usr/share/package-licenses/gdb/892b34f7865d90a6f949f50d95e49625a10bc7f0
%make_install
## Remove excluded files
rm -f %{buildroot}/usr/share/info/bfd.info
rm -f %{buildroot}/usr/share/locale/fi/LC_MESSAGES/opcodes.mo
rm -f %{buildroot}/usr/share/locale/fi/LC_MESSAGES/bfd.mo
rm -f %{buildroot}/usr/include/bfdlink.h
rm -f %{buildroot}/usr/include/bfd.h
rm -f %{buildroot}/usr/include/ansidecl.h
rm -f %{buildroot}/usr/include/dis-asm.h
rm -f %{buildroot}/usr/include/plugin-api.h
rm -f %{buildroot}/usr/include/symcat.h
rm -f %{buildroot}/usr/include/diagnostics.h
rm -f %{buildroot}/usr/include/bfd_stdint.h
rm -f %{buildroot}/usr/include/ctf-api.h
rm -f %{buildroot}/usr/include/ctf.h
## install_append content
rm -f %{buildroot}/usr/share/locale/*/LC_MESSAGES/bfd.mo
rm -f %{buildroot}/usr/share/locale/*/LC_MESSAGES/opcodes.mo
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gcore
/usr/bin/gdb
/usr/bin/gdb-add-index
/usr/bin/gdbserver

%files data
%defattr(-,root,root,-)
/usr/share/gdb/python/gdb/FrameDecorator.py
/usr/share/gdb/python/gdb/FrameIterator.py
/usr/share/gdb/python/gdb/__init__.py
/usr/share/gdb/python/gdb/command/__init__.py
/usr/share/gdb/python/gdb/command/explore.py
/usr/share/gdb/python/gdb/command/frame_filters.py
/usr/share/gdb/python/gdb/command/pretty_printers.py
/usr/share/gdb/python/gdb/command/prompt.py
/usr/share/gdb/python/gdb/command/type_printers.py
/usr/share/gdb/python/gdb/command/unwinders.py
/usr/share/gdb/python/gdb/command/xmethods.py
/usr/share/gdb/python/gdb/frames.py
/usr/share/gdb/python/gdb/function/__init__.py
/usr/share/gdb/python/gdb/function/as_string.py
/usr/share/gdb/python/gdb/function/caller_is.py
/usr/share/gdb/python/gdb/function/strfns.py
/usr/share/gdb/python/gdb/printer/__init__.py
/usr/share/gdb/python/gdb/printer/bound_registers.py
/usr/share/gdb/python/gdb/printing.py
/usr/share/gdb/python/gdb/prompt.py
/usr/share/gdb/python/gdb/types.py
/usr/share/gdb/python/gdb/unwinder.py
/usr/share/gdb/python/gdb/xmethod.py
/usr/share/gdb/syscalls/aarch64-linux.xml
/usr/share/gdb/syscalls/amd64-linux.xml
/usr/share/gdb/syscalls/arm-linux.xml
/usr/share/gdb/syscalls/freebsd.xml
/usr/share/gdb/syscalls/gdb-syscalls.dtd
/usr/share/gdb/syscalls/i386-linux.xml
/usr/share/gdb/syscalls/mips-n32-linux.xml
/usr/share/gdb/syscalls/mips-n64-linux.xml
/usr/share/gdb/syscalls/mips-o32-linux.xml
/usr/share/gdb/syscalls/netbsd.xml
/usr/share/gdb/syscalls/ppc-linux.xml
/usr/share/gdb/syscalls/ppc64-linux.xml
/usr/share/gdb/syscalls/s390-linux.xml
/usr/share/gdb/syscalls/s390x-linux.xml
/usr/share/gdb/syscalls/sparc-linux.xml
/usr/share/gdb/syscalls/sparc64-linux.xml
/usr/share/gdb/system-gdbinit/elinos.py
/usr/share/gdb/system-gdbinit/wrs-linux.py

%files dev
%defattr(-,root,root,-)
/usr/include/gdb/jit-reader.h
/usr/lib64/libinproctrace.so

%files info
%defattr(0644,root,root,0755)
/usr/share/info/annotate.info
/usr/share/info/gdb.info
/usr/share/info/gdb.info-1
/usr/share/info/gdb.info-2
/usr/share/info/gdb.info-3
/usr/share/info/gdb.info-4
/usr/share/info/gdb.info-5
/usr/share/info/gdb.info-6
/usr/share/info/gdb.info-7
/usr/share/info/gdb.info-8
/usr/share/info/stabs.info

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gdb/0e8e850b0580fbaaa0872326cb1b8ad6adda9b0d
/usr/share/package-licenses/gdb/597bf5f9c0904bd6c48ac3a3527685818d11246d
/usr/share/package-licenses/gdb/5fb362ef1680e635fe5fb212b55eef4db9ead48f
/usr/share/package-licenses/gdb/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1
/usr/share/package-licenses/gdb/79747e6fe064f75103cb65ef01a06c650c39994e
/usr/share/package-licenses/gdb/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/gdb/892b34f7865d90a6f949f50d95e49625a10bc7f0
/usr/share/package-licenses/gdb/e7d563f52bf5295e6dba1d67ac23e9f6a160fab9

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gcore.1
/usr/share/man/man1/gdb-add-index.1
/usr/share/man/man1/gdb.1
/usr/share/man/man1/gdbserver.1
/usr/share/man/man5/gdbinit.5

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libbfd.a
/usr/lib64/libctf-nobfd.a
/usr/lib64/libctf.a
/usr/lib64/libopcodes.a
