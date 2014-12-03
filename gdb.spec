#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x92EDB04BFF325CF3 (brobecker@adacore.com)
#
%define keepstatic 1
Name     : gdb
Version  : 8.0
Release  : 54
URL      : http://ftp.gnu.org/gnu/gdb/gdb-8.0.tar.xz
Source0  : http://ftp.gnu.org/gnu/gdb/gdb-8.0.tar.xz
Source99 : http://ftp.gnu.org/gnu/gdb/gdb-8.0.tar.xz.sig
Summary  : zlib compression library
Group    : Development/Tools
License  : BSL-1.0 GFDL-1.1 GPL-1.0+ GPL-2.0 GPL-2.0+ GPL-3.0 GPL-3.0+ LGPL-2.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0 Public-Domain
Requires: gdb-bin
Requires: gdb-data
Requires: gdb-doc
BuildRequires : binutils-dev
BuildRequires : bison
BuildRequires : dejagnu
BuildRequires : expat-dev
BuildRequires : expect
BuildRequires : flex
BuildRequires : gcc-libgcc32
BuildRequires : glibc-dev32
BuildRequires : glibc-staticdev
BuildRequires : go
BuildRequires : libxslt-bin
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
BuildRequires : zlib-dev
Patch1: curses.patch

%description
This directory contains various GNU compilers, assemblers, linkers,
debuggers, etc., plus their support routines, definitions, and documentation.

%package bin
Summary: bin components for the gdb package.
Group: Binaries
Requires: gdb-data

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
Requires: gdb-bin
Requires: gdb-data
Provides: gdb-devel

%description dev
dev components for the gdb package.


%package doc
Summary: doc components for the gdb package.
Group: Documentation

%description doc
doc components for the gdb package.


%prep
%setup -q -n gdb-8.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1496604760
%configure  --enable-static  --with-separate-debug-dir=/usr/lib/debug --enable-tui --enable-targets=%{_arch}-unknown-linux-gnu,%{_arch}-generic-linux-gnu  --target=%{_arch}-generic-linux-gnu %{_arch}-generic-linux-gnu --with-python=yes --enable-plugins --disable-rpath --with-system-zlib --with-intel-pt PYTHON=/usr/bin/python3 --with-python=/usr/bin/python3
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1496604760
rm -rf %{buildroot}
%make_install
## make_install_append content
rm -f %{buildroot}/usr/share/locale/*/LC_MESSAGES/bfd.mo
rm -f %{buildroot}/usr/share/locale/*/LC_MESSAGES/opcodes.mo
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gcore
/usr/bin/gdb
/usr/bin/gdbserver

%files data
%defattr(-,root,root,-)
/usr/share/gdb/python/gdb/FrameDecorator.py
/usr/share/gdb/python/gdb/FrameDecorator.pyc
/usr/share/gdb/python/gdb/FrameDecorator.pyo
/usr/share/gdb/python/gdb/FrameIterator.py
/usr/share/gdb/python/gdb/FrameIterator.pyc
/usr/share/gdb/python/gdb/FrameIterator.pyo
/usr/share/gdb/python/gdb/__init__.py
/usr/share/gdb/python/gdb/__init__.pyc
/usr/share/gdb/python/gdb/__init__.pyo
/usr/share/gdb/python/gdb/command/__init__.py
/usr/share/gdb/python/gdb/command/__init__.pyc
/usr/share/gdb/python/gdb/command/__init__.pyo
/usr/share/gdb/python/gdb/command/explore.py
/usr/share/gdb/python/gdb/command/explore.pyc
/usr/share/gdb/python/gdb/command/explore.pyo
/usr/share/gdb/python/gdb/command/frame_filters.py
/usr/share/gdb/python/gdb/command/frame_filters.pyc
/usr/share/gdb/python/gdb/command/frame_filters.pyo
/usr/share/gdb/python/gdb/command/pretty_printers.py
/usr/share/gdb/python/gdb/command/pretty_printers.pyc
/usr/share/gdb/python/gdb/command/pretty_printers.pyo
/usr/share/gdb/python/gdb/command/prompt.py
/usr/share/gdb/python/gdb/command/prompt.pyc
/usr/share/gdb/python/gdb/command/prompt.pyo
/usr/share/gdb/python/gdb/command/type_printers.py
/usr/share/gdb/python/gdb/command/type_printers.pyc
/usr/share/gdb/python/gdb/command/type_printers.pyo
/usr/share/gdb/python/gdb/command/unwinders.py
/usr/share/gdb/python/gdb/command/unwinders.pyc
/usr/share/gdb/python/gdb/command/unwinders.pyo
/usr/share/gdb/python/gdb/command/xmethods.py
/usr/share/gdb/python/gdb/command/xmethods.pyc
/usr/share/gdb/python/gdb/command/xmethods.pyo
/usr/share/gdb/python/gdb/frames.py
/usr/share/gdb/python/gdb/frames.pyc
/usr/share/gdb/python/gdb/frames.pyo
/usr/share/gdb/python/gdb/function/__init__.py
/usr/share/gdb/python/gdb/function/__init__.pyc
/usr/share/gdb/python/gdb/function/__init__.pyo
/usr/share/gdb/python/gdb/function/as_string.py
/usr/share/gdb/python/gdb/function/as_string.pyc
/usr/share/gdb/python/gdb/function/as_string.pyo
/usr/share/gdb/python/gdb/function/caller_is.py
/usr/share/gdb/python/gdb/function/caller_is.pyc
/usr/share/gdb/python/gdb/function/caller_is.pyo
/usr/share/gdb/python/gdb/function/strfns.py
/usr/share/gdb/python/gdb/function/strfns.pyc
/usr/share/gdb/python/gdb/function/strfns.pyo
/usr/share/gdb/python/gdb/printer/__init__.py
/usr/share/gdb/python/gdb/printer/__init__.pyc
/usr/share/gdb/python/gdb/printer/__init__.pyo
/usr/share/gdb/python/gdb/printer/bound_registers.py
/usr/share/gdb/python/gdb/printer/bound_registers.pyc
/usr/share/gdb/python/gdb/printer/bound_registers.pyo
/usr/share/gdb/python/gdb/printing.py
/usr/share/gdb/python/gdb/printing.pyc
/usr/share/gdb/python/gdb/printing.pyo
/usr/share/gdb/python/gdb/prompt.py
/usr/share/gdb/python/gdb/prompt.pyc
/usr/share/gdb/python/gdb/prompt.pyo
/usr/share/gdb/python/gdb/types.py
/usr/share/gdb/python/gdb/types.pyc
/usr/share/gdb/python/gdb/types.pyo
/usr/share/gdb/python/gdb/unwinder.py
/usr/share/gdb/python/gdb/unwinder.pyc
/usr/share/gdb/python/gdb/unwinder.pyo
/usr/share/gdb/python/gdb/xmethod.py
/usr/share/gdb/python/gdb/xmethod.pyc
/usr/share/gdb/python/gdb/xmethod.pyo
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
/usr/share/gdb/system-gdbinit/elinos.pyc
/usr/share/gdb/system-gdbinit/elinos.pyo
/usr/share/gdb/system-gdbinit/wrs-linux.py
/usr/share/gdb/system-gdbinit/wrs-linux.pyc
/usr/share/gdb/system-gdbinit/wrs-linux.pyo

%files dev
%defattr(-,root,root,-)
%exclude /usr/include/ansidecl.h
%exclude /usr/include/bfd.h
%exclude /usr/include/bfdlink.h
%exclude /usr/include/dis-asm.h
%exclude /usr/include/plugin-api.h
%exclude /usr/include/symcat.h
/usr/include/gdb/jit-reader.h
/usr/lib64/*.a
/usr/lib64/libinproctrace.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*
%exclude /usr/share/info/bfd.info
