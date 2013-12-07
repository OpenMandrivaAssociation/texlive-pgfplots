# revision 31822
# category Package
# catalog-ctan /graphics/pgf/contrib/pgfplots
# catalog-date 2013-10-03 20:59:17 +0200
# catalog-license gpl
# catalog-version 1.9
Name:		texlive-pgfplots
Version:	1.9
Release:	5
Summary:	Create normal/logarithmic plots in two and three dimensions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/pgfplots
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfplots.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfplots.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfplots.source.tar.xz
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
%{_texmfdistdir}/scripts/pgfplots/matlab2pgfplots.m
%{_texmfdistdir}/scripts/pgfplots/matlab2pgfplots.sh
%{_texmfdistdir}/scripts/pgfplots/pgf2pdf.sh
%{_texmfdistdir}/scripts/pgfplots/pgfplots.py
%{_texmfdistdir}/tex/context/third/pgfplots/t-pgfplots.tex
%{_texmfdistdir}/tex/context/third/pgfplots/t-pgfplotstable.tex
%{_texmfdistdir}/tex/generic/pgfplots/libs/pgflibrarypgfplots.surfshading.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/libs/pgfplotslibrary.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/libs/tikzlibrarypgfplots.colormaps.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/libs/tikzlibrarypgfplots.dateplot.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/libs/tikzlibrarypgfplots.external.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/libs/tikzlibrarypgfplots.groupplots.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/libs/tikzlibrarypgfplots.patchplots.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/libs/tikzlibrarypgfplots.polar.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/libs/tikzlibrarypgfplots.smithchart.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/libs/tikzlibrarypgfplots.statistics.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/libs/tikzlibrarypgfplots.ternary.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/libs/tikzlibrarypgfplots.units.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/liststructure/pgfplotsarray.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/liststructure/pgfplotsdeque.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/liststructure/pgfplotsliststructure.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/liststructure/pgfplotsliststructureext.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/liststructure/pgfplotsmatrix.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/lua/pgfplots.lua
%{_texmfdistdir}/tex/generic/pgfplots/numtable/pgfplotstable.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/numtable/pgfplotstable.coltype.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/numtable/pgfplotstableshared.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldpgfsupp_loader.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldpgfsupp_misc.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldpgfsupp_pgfcoreexternal.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldpgfsupp_pgfcoreimage.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldpgfsupp_pgfcorelayers.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldpgfsupp_pgfcorescopes.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldpgfsupp_pgfkeys.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldpgfsupp_pgfkeysfiltered.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldpgfsupp_pgflibraryfpu.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldpgfsupp_pgflibraryplothandlers.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldpgfsupp_pgfmanual.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldpgfsupp_pgfmanual.pdflinks.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldpgfsupp_pgfmanual.prettyprinter.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldpgfsupp_pgfmathfloat.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldpgfsupp_tikzexternal.sty
%{_texmfdistdir}/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldpgfsupp_tikzexternalshared.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldpgfsupp_tikzlibraryexternal.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/oldpgfplotscompatib/tikzlibrarydateplot.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/pgfplots.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/pgfplots.errorbars.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/pgfplots.markers.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/pgfplots.paths.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/pgfplots.revision.tex
%{_texmfdistdir}/tex/generic/pgfplots/pgfplots.scaling.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/pgfplotscoordprocessing.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/pgfplotscore.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/pgfplotsmeshplothandler.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/pgfplotsplothandlers.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/pgfplotsstackedplots.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/pgfplotsticks.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/sys/pgflibrarypgfplots.surfshading.pgfsys-dvipdfmx.def
%{_texmfdistdir}/tex/generic/pgfplots/sys/pgflibrarypgfplots.surfshading.pgfsys-dvips.def
%{_texmfdistdir}/tex/generic/pgfplots/sys/pgflibrarypgfplots.surfshading.pgfsys-pdftex.def
%{_texmfdistdir}/tex/generic/pgfplots/sys/pgflibrarypgfplots.surfshading.pgfsys-xetex.def
%{_texmfdistdir}/tex/generic/pgfplots/sys/pgfplotssysgeneric.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/test/pgfplots.assert.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/test/pgfplots.assert.sty
%{_texmfdistdir}/tex/generic/pgfplots/util/pgfplotsbinary.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/util/pgfplotsbinary.data.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/util/pgfplotscolor.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/util/pgfplotscolormap.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/util/pgfplotsutil.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/util/pgfplotsutil.verb.code.tex
%{_texmfdistdir}/tex/latex/pgfplots/bugtracker.sty
%{_texmfdistdir}/tex/latex/pgfplots/libs/tikzlibrarypgfplots.clickable.code.tex
%{_texmfdistdir}/tex/latex/pgfplots/libs/tikzlibrarypgfplotsclickable.code.tex
%{_texmfdistdir}/tex/latex/pgfplots/pgfplots.sty
%{_texmfdistdir}/tex/latex/pgfplots/pgfplotstable.sty
%{_texmfdistdir}/tex/latex/pgfplots/pgfregressiontest.sty
%{_texmfdistdir}/tex/plain/pgfplots/pgfplots.tex
%{_texmfdistdir}/tex/plain/pgfplots/pgfplotstable.tex
%doc %{_texmfdistdir}/doc/context/third/pgfplots/pgfplotsexample-context.pdf
%doc %{_texmfdistdir}/doc/context/third/pgfplots/pgfplotsexample-context.tex
%doc %{_texmfdistdir}/doc/generic/pgfplots/README
%doc %{_texmfdistdir}/doc/latex/pgfplots/TeX-programming-notes.pdf
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplotsexample.pdf
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplotsexample.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplotstable.pdf
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplotstodo.pdf
%doc %{_texmfdistdir}/doc/plain/pgfplots/pgfplotsexample-plain.pdf
%doc %{_texmfdistdir}/doc/plain/pgfplots/pgfplotsexample-plain.tex
#- source
%doc %{_texmfdistdir}/source/context/third/pgfplots/pgfplotstests.context.tar.bz2
%doc %{_texmfdistdir}/source/latex/pgfplots/pgfplotstests.tar.bz2

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar scripts tex doc source %{buildroot}%{_texmfdistdir}
rm %{buildroot}%{_texmfdistdir}/doc/latex/pgfplots/pgfplots.doc.src.tar.bz2
rm %{buildroot}%{_texmfdistdir}/doc/latex/pgfplots/pgfplots.pdf
