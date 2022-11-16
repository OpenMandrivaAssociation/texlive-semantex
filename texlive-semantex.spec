Name:		texlive-semantex
Version:	64611
Release:	1
Summary:	Semantic, keyval-based mathematics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/semantex
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/semantex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/semantex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The SemanTeX package for LaTeX delivers a more semantic,
systematized way of writing mathematics, compared to the
classical math syntax in LaTeX. The system uses keyval syntax,
and the user can define their own keys and customize the system
down to the last detail. At the same time, care has been taken
to make the syntax as simple, natural, practical, and
lightweight as possible. Furthermore, the package has a
companion package, called stripsemantex, which allows you to
completely strip your documents of SemanTeX markup to prepare
them e.g. for publication. The package is still in beta, but is
considered feature-complete and more or less stable, so using
it at this point should be safe. Still, suggestions, ideas, and
bug reports are more than welcome!

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/semantex
%doc %{_texmfdistdir}/doc/latex/semantex

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
