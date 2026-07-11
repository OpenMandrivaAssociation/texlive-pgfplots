%global tl_name pgfplots
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.18.2
Release:	%{tl_revision}.1
Summary:	Create normal/logarithmic plots in two and three dimensions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/pgfplots
License:	gpl3+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfplots.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfplots.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfplots.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(pgf)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
PGFPlots draws high-quality function plots in normal or logarithmic
scaling with a user-friendly interface directly in TeX. The user
supplies axis labels, legend entries and the plot coordinates for one or
more plots and PGFPlots applies axis scaling, computes any logarithms
and axis ticks and draws the plots, supporting line plots, scatter
plots, piecewise constant plots, bar plots, area plots, mesh-- and
surface plots and some more. Pgfplots is based on PGF/TikZ (PGF); it
runs equally for LaTeX/TeX/ConTeXt.

