Name:		texlive-hyphenex
Version:	57387
Release:	2
Summary:	Generate a hyphenation exceptions file
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/digests/tugboat/hyphenex
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphenex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphenex.source.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex source %{buildroot}%{_texmfdistdir}
