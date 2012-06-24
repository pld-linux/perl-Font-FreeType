#
# TODO: check while tests fail (freetype expert needed)
#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Font
%define		pnam	FreeType
Summary:	Font::FreeType - read font files and render glyphs from Perl using FreeType2
Summary(pl):	Font::FreeType - odczyt plik�w font�w oraz rendering znak�w graficznych za pomoc� FreeType2
Name:		perl-Font-FreeType
Version:	0.03
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Font/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	47b9483c92f1b2df0bbb5258a6a596b2
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	freetype-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows Perl programs to conveniently read information from
font files. All the font access is done through the FreeType2 library,
which supports many formats. It can render images of characters with
high-quality hinting and antialiasing, extract metrics information,
and extract the outlines of characters in scalable formats like
TrueType.

%description -l pl
Modu� ten umo�liwia programom perlowym odczyt informacji z plik�w
font�w w wygodny spos�b. Ca�y dost�p do font�w odbywa sie poprzez
bibliotek� FreeType2, kt�ra wspiera wiele format�w. Umo�liwia
renderowanie obraz�w znak�w, wysokiej jako�ci hinting i antyaliasing,
pobieranie informacji o metryce oraz pobieranie zarys�w znak�w dla
format�w skalowalnych, takich jak TrueType.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorarch}/Font/*.pm
%{perl_vendorarch}/Font/FreeType
%dir %{perl_vendorarch}/auto/Font/FreeType
%attr(755,root,root) %{perl_vendorarch}/auto/Font/FreeType/*.so
%{perl_vendorarch}/auto/Font/FreeType/*.bs
%{_mandir}/man3/*
