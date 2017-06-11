#
# TODO: check why tests fail (freetype expert needed)
#
# Conditional build:
%bcond_with	tests	# do perform "make test" (fails with recent freetype versions)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Font
%define		pnam	FreeType
Summary:	Font::FreeType - read font files and render glyphs from Perl using FreeType2
Summary(pl.UTF-8):	Font::FreeType - odczyt plików fontów oraz rendering znaków graficznych za pomocą FreeType2
Name:		perl-Font-FreeType
Version:	0.03
Release:	13
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Font/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	47b9483c92f1b2df0bbb5258a6a596b2
Patch0:		%{name}-gcc4.patch
URL:		http://search.cpan.org/dist/Font-FreeType/
BuildRequires:	freetype-devel >= 2
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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
%patch0 -p1

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
