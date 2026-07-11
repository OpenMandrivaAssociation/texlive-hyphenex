%global tl_name hyphenex
%global tl_revision 57387

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	US English hyphenation exceptions file
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/digests/tugboat/hyphenex
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphenex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphenex.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Exceptions for American English hyphenation patterns are occasionally
published in the TeX User Group journal TUGboat. This bundle provides
alternative Perl and Bourne shell scripts to convert the source of such
an article into an exceptions file, together with a recent copy of the
article and machine-readable files.

