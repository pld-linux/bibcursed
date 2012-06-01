# TODO:
# - fix makefile to build it TheRightWay(TM)
Summary:	Maintain BibTeX files
Summary(pl.UTF-8):	Zarządzanie plikami BibTeXa
Name:		bibcursed
Version:	2.0.1
Release:	1
License:	GPL v2
Group:		Daemons
Source0:	http://dl.sourceforge.net/bibcursed/%{name}_%{version}.tgz
# Source0-md5:	7645b7b7e3ff558d673a1ed6e2ebe99e
URL:		http://sourceforge.net/projects/bibcursed/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bibcursed is a simple curses-based editor for BibTeX bibliography
files, especially useful for those who have to maintain a large number
of references for a major piece of documentation, like a PhD thesis.
It performs everyday functions such as adding, removing and viewing
reference entries. Intelligent prompting for fields is used when
adding entries so that authors do not have to rely on memory for
knowing which fields can and cannot be used for different entry types.

%description -l pl.UTF-8
Bibcursed to prosty oparty o curses edytor do plików bibliografii
BibTeXa, przydatny szczególnie dla tych, którzy muszą utrzymywać dużą
liczbę odniesień w większej części dokumentacji, jak na przykład
pracach dyplomowych. Program wykonuje codzienne funkcje, takie jak
dodawanie, usuwanie i przeglądanie wpisów z odniesieniami. Przy
dodawaniu wpisów używane są inteligentne pytania dla pól, przez co
autorzy nie muszą polegać na swojej pamięci, żeby wiedzieć, które pola
mogą, a które nie mogą być użyte dla różnych rodzajów wpisów.

%prep
%setup -q -n %{name}

%build
%{__cc} %{rpmcflags} -I/usr/include/ncurses -lncurses -o %{name} bibcursed.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README INSTALL
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
