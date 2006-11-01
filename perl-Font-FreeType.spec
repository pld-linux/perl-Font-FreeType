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
Summary(pl):	Font::FreeType - odczyt plików fontów oraz rendering znaków graficznych za pomoc± FreeType2
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
Modu³ ten umo¿liwia programom perlowym odczyt informacji z plików
fontów w wygodny sposób. Ca³y dostêp do fontów odbywa sie poprzez
bibliotekê FreeType2, która wspiera wiele formatów. Umo¿liwia
renderowanie obrazów znaków, wysokiej jako¶ci hinting i antyaliasing,
pobieranie informacji o metryce oraz pobieranie zarysów znaków dla
formatów skalowalnych, takich jak TrueType.

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
