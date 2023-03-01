Name: argagg
Version: 0.4.6
Release: 1
Source0: https://github.com/vietjtnguyen/argagg/archive/%{version}/%{name}-%{version}.tar.gz
Summary: Argument Aggregator, a C++ command line argument/option parser
URL: https://github.com/vietjtnguyen/argagg
License: GPL
Group: Development/C++
BuildRequires: cmake
BuildRequires: ninja
BuildArch: noarch

%description
This is yet another C++ command line argument/option parser. It was written as a
simple and idiomatic alternative to other frameworks like getopt, Boost program
options, TCLAP, and others. The goal is to achieve the majority of argument
parsing needs in a simple manner with an easy to use API. It operates as a
single pass over all arguments, recognizing flags prefixed by - (short) or --
(long) and aggregating them into easy to access structures with lots of
convenience functions. It defers processing types until you access them, so the
result structures end up just being pointers into the original command line
argument C-strings.

%prep
%autosetup -p1
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%check
cd build
ctest -V

%files
%{_includedir}/*
%doc %{_docdir}/argagg
