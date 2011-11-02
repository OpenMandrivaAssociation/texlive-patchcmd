Name:		texlive-patchcmd
Version:	1.03
Release:	1
Summary:	Change the definition of an existing command
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/patchcmd
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/patchcmd.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/patchcmd.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/patchcmd.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The patchcmd package provides a command \patchcommand that can
be used to add material at the beginning and/or the end of the
replacement text of an existing macro. It works for macros with
any number of normal arguments, including those that were
defined with \DeclareRobustCommand.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/patchcmd/patchcmd.sty
%doc %{_texmfdistdir}/doc/latex/patchcmd/patchcmd.pdf
#- source
%doc %{_texmfdistdir}/source/latex/patchcmd/patchcmd.dtx
%doc %{_texmfdistdir}/source/latex/patchcmd/patchcmd.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
