#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Compile-time configuration for Jane Street libraries
Summary(pl.UTF-8):	Konfiguracja z czasu kompilacji dla bibliotek Jane Street
Name:		ocaml-jst-config
Version:	0.14.1
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/jst-config/tags
Source0:	https://github.com/janestreet/jst-config/archive/v%{version}/jst-config-%{version}.tar.gz
# Source0-md5:	ca0d970356cc99b0a5660058a93ff589
URL:		https://github.com/janestreet/jst-config
BuildRequires:	ocaml >= 1:4.04.2
BuildRequires:	ocaml-base-devel >= 0.14
BuildRequires:	ocaml-base-devel < 0.15
BuildRequires:	ocaml-dune >= 2.0.0
BuildRequires:	ocaml-ppx_assert-devel >= 0.14
BuildRequires:	ocaml-ppx_assert-devel < 0.15
BuildRequires:	ocaml-stdio-devel >= 0.14
BuildRequires:	ocaml-stdio-devel < 0.15
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
Defines compile-time constants used in Jane Street libraries such as
Base, Core, and Async.

This package contains files needed to run bytecode executables using
jst-config library.

%description -l pl.UTF-8
Biblioteka definiująca stałe używane w bibliotekach Jane Street,
takich jak Base, Core i Async.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki jst-config.

%package devel
Summary:	Compile-time configuration for Jane Street libraries - development part
Summary(pl.UTF-8):	Konfiguracja z czasu kompilacji dla bibliotek Jane Street - część programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-base-devel >= 0.14
Requires:	ocaml-ppx_assert-devel >= 0.14
Requires:	ocaml-stdio-devel >= 0.14

%description devel
This package contains files needed to develop OCaml programs using
jst-config library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki jst-config.

%prep
%setup -q -n jst-config-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/jst-config/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/jst-config

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.md
%dir %{_libdir}/ocaml/jst-config
%{_libdir}/ocaml/jst-config/META
%{_libdir}/ocaml/jst-config/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/jst-config/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/jst-config/rt-flags
%{_libdir}/ocaml/jst-config/*.cmi
%{_libdir}/ocaml/jst-config/*.cmt
%{_libdir}/ocaml/jst-config/*.h
%if %{with ocaml_opt}
%{_libdir}/ocaml/jst-config/config_h.a
%{_libdir}/ocaml/jst-config/*.cmx
%{_libdir}/ocaml/jst-config/*.cmxa
%endif
%{_libdir}/ocaml/jst-config/dune-package
%{_libdir}/ocaml/jst-config/opam
