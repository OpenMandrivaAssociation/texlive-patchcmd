Name:		texlive-patchcmd
Version:	41379
Release:	2
Summary:	Change the definition of an existing command
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/patchcmd
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/patchcmd.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/patchcmd.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/patchcmd.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The patchcmd package provides a command \patchcommand that can
be used to add material at the beginning and/or the end of the
replacement text of an existing macro. It works for macros with
any number of normal arguments, including those that were
defined with \DeclareRobustCommand.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/patchcmd
%doc %{_texmfdistdir}/doc/latex/patchcmd
#- source
%doc %{_texmfdistdir}/source/latex/patchcmd

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
