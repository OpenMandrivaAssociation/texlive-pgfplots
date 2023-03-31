Name:		texlive-pgfplots
Version:	61719
Release:	2
Summary:	Create normal/logarithmic plots in two and three dimensions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/pgfplots
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfplots.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfplots.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfplots.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
PGFPlots draws high-quality function plots in normal or
logarithmic scaling with a user-friendly interface directly in
TeX. The user supplies axis labels, legend entries and the plot
coordinates for one or more plots and PGFPlots applies axis
scaling, computes any logarithms and axis ticks and draws the
plots, supporting line plots, scatter plots, piecewise constant
plots, bar plots, area plots, mesh-- and surface plots and some
more. Pgfplots is based on PGF/TikZ (pgf); it runs equally for
LaTeX/TeX/ConTeXt.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/scripts/pgfplots
%{_texmfdistdir}/tex/context/third/pgfplots
%{_texmfdistdir}/tex/generic/pgfplots
%{_texmfdistdir}/tex/latex/pgfplots
%{_texmfdistdir}/tex/plain/pgfplots
%doc %{_texmfdistdir}/doc/context/third/pgfplots
%doc %{_texmfdistdir}/doc/generic/pgfplots
%doc %{_texmfdistdir}/doc/latex/pgfplots
%doc %{_texmfdistdir}/doc/plain/pgfplots

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar scripts tex doc source %{buildroot}%{_texmfdistdir}
rm %{buildroot}%{_texmfdistdir}/source/latex/pgfplots/pgfplotstests.tar.bz2
rm %{buildroot}%{_texmfdistdir}/doc/latex/pgfplots/pgfplots.doc.src.tar.bz2
rm %{buildroot}%{_texmfdistdir}/source/context/third/pgfplots/pgfplotstests.context.tar.bz2
