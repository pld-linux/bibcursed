# TODO:
# - fix makefile to build it TheRightWay(TM)
Summary:	Maintain BibTeX files
Name:		bibcursed
Version:	2.0.0
Release:	1
License:	GPL v2
Group:		Daemons
Source0:	http://dl.sourceforge.net/bibcursed/%{name}_%{version}.tar.gz
# Source0-md5:	2579457724f17c23cdac408e4271f2d9
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

%prep
%setup  -q -n %{name}

%build
%{__cc} %{rpmcflags} -I%{_includedir}/ncurses -lncurses -o %{name} bibcursed.c

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
