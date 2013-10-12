# revision 29349
# category Package
# catalog-ctan /info/digests/tugboat/hyphenex
# catalog-date 2012-05-16 13:34:59 +0200
# catalog-license other-free
# catalog-version undef
Name:		texlive-hyphenex
Version:	20120516
Release:	1
Summary:	Generate a hyphenation exceptions file
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/digests/tugboat/hyphenex
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphenex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphenex.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Exceptions for American English hyphenation patterns are
occasionally published in the TeX User Group magazine TUGboat.
This bundle provides alternative Perl and Bourne shell scripts
to convert the source of such an article into an exceptions
file, together with a recent copy of the article and its
translation.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/hyphenex/ushyphex.tex
#- source
%doc %{_texmfdistdir}/source/generic/hyphenex/GNUmakefile
%doc %{_texmfdistdir}/source/generic/hyphenex/README
%doc %{_texmfdistdir}/source/generic/hyphenex/hyphenex.pl
%doc %{_texmfdistdir}/source/generic/hyphenex/hyphenex.sh
%doc %{_texmfdistdir}/source/generic/hyphenex/tb0hyf.pdf
%doc %{_texmfdistdir}/source/generic/hyphenex/tb0hyf.tex
%doc %{_texmfdistdir}/source/generic/hyphenex/test.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex source %{buildroot}%{_texmfdistdir}
