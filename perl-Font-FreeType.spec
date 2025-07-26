#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Font
%define		pnam	FreeType
Summary:	Font::FreeType - read font files and render glyphs from Perl using FreeType2
Summary(pl.UTF-8):	Font::FreeType - odczyt plików fontów oraz rendering znaków graficznych za pomocą FreeType2
Name:		perl-Font-FreeType
Version:	0.16
Release:	6
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Font/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	01b17b1844c7369084288bb6c70b9021
URL:		https://metacpan.org/dist/Font-FreeType
BuildRequires:	freetype-devel >= 2
BuildRequires:	perl-Devel-CheckLib
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.64
BuildRequires:	perl-File-Which
%if %{with tests}
BuildRequires:	perl-Test-Warnings
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows Perl programs to conveniently read information from
font files. All the font access is done through the FreeType2 library,
which supports many formats. It can render images of characters with
high-quality hinting and antialiasing, extract metrics information,
and extract the outlines of characters in scalable formats like
TrueType.

%description -l pl.UTF-8
Moduł ten umożliwia programom perlowym odczyt informacji z plików
fontów w wygodny sposób. Cały dostęp do fontów odbywa sie poprzez
bibliotekę FreeType2, która wspiera wiele formatów. Umożliwia
renderowanie obrazów znaków, wysokiej jakości hinting i antyaliasing,
pobieranie informacji o metryce oraz pobieranie zarysów znaków dla
formatów skalowalnych, takich jak TrueType.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
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
%dir %{perl_vendorarch}/Font
%{perl_vendorarch}/Font/FreeType.pm
%{perl_vendorarch}/Font/FreeType
%dir %{perl_vendorarch}/auto/Font
%dir %{perl_vendorarch}/auto/Font/FreeType
%attr(755,root,root) %{perl_vendorarch}/auto/Font/FreeType/FreeType.so
%{_mandir}/man3/Font::FreeType*.3pm*
