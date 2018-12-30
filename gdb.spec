#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x92EDB04BFF325CF3 (brobecker@adacore.com)
#
%define keepstatic 1
Name     : gdb
Version  : 8.2
Release  : 144
URL      : https://mirrors.kernel.org/gnu/gdb/gdb-8.2.tar.xz
Source0  : https://mirrors.kernel.org/gnu/gdb/gdb-8.2.tar.xz
Source99 : https://mirrors.kernel.org/gnu/gdb/gdb-8.2.tar.xz.sig
Summary  : zlib compression library
Group    : Development/Tools
License  : BSL-1.0 GFDL-1.1 GPL-1.0+ GPL-2.0 GPL-2.0+ GPL-3.0 GPL-3.0+ LGPL-2.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0 Public-Domain
Requires: gdb-bin
Requires: gdb-license
Requires: gdb-data
Requires: gdb-man
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
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : sed
BuildRequires : tcl
BuildRequires : texinfo
BuildRequires : xz-dev
Patch1: cve-2017-9778.patch

%description
This directory contains various GNU compilers, assemblers, linkers,
debuggers, etc., plus their support routines, definitions, and documentation.

%package bin
Summary: bin components for the gdb package.
Group: Binaries
Requires: gdb-data = %{version}-%{release}
Requires: gdb-license = %{version}-%{release}
Requires: gdb-man = %{version}-%{release}

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

%description dev
dev components for the gdb package.


%package doc
Summary: doc components for the gdb package.
Group: Documentation
Requires: gdb-man = %{version}-%{release}

%description doc
doc components for the gdb package.


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


%prep
%setup -q -n gdb-8.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1539106974
export CFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure  --enable-static  --with-separate-debug-dir=/usr/lib/debug --enable-tui --enable-targets=%{_arch}-unknown-linux-gnu,%{_arch}-generic-linux-gnu  --target=%{_arch}-generic-linux-gnu %{_arch}-generic-linux-gnu --with-python=yes --enable-plugins --disable-rpath --with-system-zlib --with-intel-pt PYTHON=/usr/bin/python3 --with-python=yes
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1539106974
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/gdb
cp COPYING %{buildroot}/usr/share/doc/gdb/COPYING
cp COPYING.LIB %{buildroot}/usr/share/doc/gdb/COPYING.LIB
cp COPYING3 %{buildroot}/usr/share/doc/gdb/COPYING3
cp COPYING3.LIB %{buildroot}/usr/share/doc/gdb/COPYING3.LIB
cp bfd/COPYING %{buildroot}/usr/share/doc/gdb/bfd_COPYING
cp gdb/COPYING %{buildroot}/usr/share/doc/gdb/gdb_COPYING
cp include/COPYING %{buildroot}/usr/share/doc/gdb/include_COPYING
cp include/COPYING3 %{buildroot}/usr/share/doc/gdb/include_COPYING3
cp libiberty/COPYING.LIB %{buildroot}/usr/share/doc/gdb/libiberty_COPYING.LIB
cp libiberty/copying-lib.texi %{buildroot}/usr/share/doc/gdb/libiberty_copying-lib.texi
cp readline/COPYING %{buildroot}/usr/share/doc/gdb/readline_COPYING
cp sim/arm/COPYING %{buildroot}/usr/share/doc/gdb/sim_arm_COPYING
cp sim/ppc/COPYING %{buildroot}/usr/share/doc/gdb/sim_ppc_COPYING
cp sim/ppc/COPYING.LIB %{buildroot}/usr/share/doc/gdb/sim_ppc_COPYING.LIB
cp zlib/contrib/dotzlib/LICENSE_1_0.txt %{buildroot}/usr/share/doc/gdb/zlib_contrib_dotzlib_LICENSE_1_0.txt
%make_install
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
%exclude /usr/include/ansidecl.h
%exclude /usr/include/bfd.h
%exclude /usr/include/bfdlink.h
%exclude /usr/include/diagnostics.h
%exclude /usr/include/dis-asm.h
%exclude /usr/include/plugin-api.h
%exclude /usr/include/symcat.h
/usr/include/gdb/jit-reader.h
/usr/lib64/*.a
/usr/lib64/libinproctrace.so

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/info/*
%exclude /usr/share/info/bfd.info
/usr/share/doc/gdb/libiberty_copying-lib.texi

%files license
%defattr(0644,root,root,0755)
/usr/share/doc/gdb/COPYING
/usr/share/doc/gdb/COPYING.LIB
/usr/share/doc/gdb/COPYING3
/usr/share/doc/gdb/COPYING3.LIB
/usr/share/doc/gdb/bfd_COPYING
/usr/share/doc/gdb/gdb_COPYING
/usr/share/doc/gdb/include_COPYING
/usr/share/doc/gdb/include_COPYING3
/usr/share/doc/gdb/libiberty_COPYING.LIB
/usr/share/doc/gdb/readline_COPYING
/usr/share/doc/gdb/sim_arm_COPYING
/usr/share/doc/gdb/sim_ppc_COPYING
/usr/share/doc/gdb/sim_ppc_COPYING.LIB
/usr/share/doc/gdb/zlib_contrib_dotzlib_LICENSE_1_0.txt

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gcore.1
/usr/share/man/man1/gdb-add-index.1
/usr/share/man/man1/gdb.1
/usr/share/man/man1/gdbserver.1
/usr/share/man/man5/gdbinit.5
