# revision 28094
# category Package
# catalog-ctan /graphics/pgf/contrib/pgfplots
# catalog-date 2012-10-26 15:30:09 +0200
# catalog-license gpl
# catalog-version 1.7
Name:		texlive-pgfplots
Version:	1.7
Release:	2
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
%{_texmfdistdir}/tex/generic/pgfplots/pgfplots.multiaxis.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/pgfplots.paths.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/pgfplots.revision.tex
%{_texmfdistdir}/tex/generic/pgfplots/pgfplots.scaling.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/pgfplotscoordprocessing.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/pgfplotscore.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/pgfplotsmeshplothandler.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/pgfplotsplothandlers.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/pgfplotsstackedplots.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/pgfplotsticks.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/sys/pgflibrarypgfplots.surfshading.pgfsys-dvips.def
%{_texmfdistdir}/tex/generic/pgfplots/sys/pgflibrarypgfplots.surfshading.pgfsys-pdftex.def
%{_texmfdistdir}/tex/generic/pgfplots/sys/pgfplotssysgeneric.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/util/pgfplotsbinary.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/util/pgfplotsbinary.data.code.tex
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
%doc %{_texmfdistdir}/doc/context/third/pgfplots/pgfplotsexample.pdf
%doc %{_texmfdistdir}/doc/context/third/pgfplots/pgfplotsexample.tex
%doc %{_texmfdistdir}/doc/generic/pgfplots/README
%doc %{_texmfdistdir}/doc/latex/pgfplots/ChangeLog
%doc %{_texmfdistdir}/doc/latex/pgfplots/Makefile
%doc %{_texmfdistdir}/doc/latex/pgfplots/TeX-programming-notes.pdf
%doc %{_texmfdistdir}/doc/latex/pgfplots/TeX-programming-notes.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/figures/external1.gnuplot
%doc %{_texmfdistdir}/doc/latex/pgfplots/figures/external1.png
%doc %{_texmfdistdir}/doc/latex/pgfplots/figures/external2.pdf
%doc %{_texmfdistdir}/doc/latex/pgfplots/figures/pgfplots-surface-cutoff.png
%doc %{_texmfdistdir}/doc/latex/pgfplots/figures/pgfplotsclickable-fig1.png
%doc %{_texmfdistdir}/doc/latex/pgfplots/figures/pgfplotsclickable-fig2.png
%doc %{_texmfdistdir}/doc/latex/pgfplots/figures/pgfplotsclickable-fig3.png
%doc %{_texmfdistdir}/doc/latex/pgfplots/figures/pgfplotsclickable-fig4.png
%doc %{_texmfdistdir}/doc/latex/pgfplots/figures/pgfplotsclickable-log-snap0.png
%doc %{_texmfdistdir}/doc/latex/pgfplots/figures/pgfplotsclickable-log-snap1.png
%doc %{_texmfdistdir}/doc/latex/pgfplots/figures/pgfplotsclickable-log-snap2.png
%doc %{_texmfdistdir}/doc/latex/pgfplots/figures/pgfplotsclickable-logcode-snap0.png
%doc %{_texmfdistdir}/doc/latex/pgfplots/figures/pgfplotsclickable-logcode-snap1.png
%doc %{_texmfdistdir}/doc/latex/pgfplots/figures/pgfplotsclickable-scatter0.png
%doc %{_texmfdistdir}/doc/latex/pgfplots/figures/pgfplotsclickable-scatter1.png
%doc %{_texmfdistdir}/doc/latex/pgfplots/figures/pgfplotsclickable-scatter2.png
%doc %{_texmfdistdir}/doc/latex/pgfplots/figures/pgfplotsclickable.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/gallery/Makefile
%doc %{_texmfdistdir}/doc/latex/pgfplots/gallery/extractexamples.pl
%doc %{_texmfdistdir}/doc/latex/pgfplots/gallery/gallery.css
%doc %{_texmfdistdir}/doc/latex/pgfplots/gnuplot/pgfplots_DoG.gnuplot
%doc %{_texmfdistdir}/doc/latex/pgfplots/gnuplot/pgfplots_DoG.table
%doc %{_texmfdistdir}/doc/latex/pgfplots/gnuplot/pgfplots_exp
%doc %{_texmfdistdir}/doc/latex/pgfplots/gnuplot/pgfplots_exp.gnuplot
%doc %{_texmfdistdir}/doc/latex/pgfplots/gnuplot/pgfplots_exp.table
%doc %{_texmfdistdir}/doc/latex/pgfplots/gnuplot/pgfplots_exp.vrs
%doc %{_texmfdistdir}/doc/latex/pgfplots/gnuplot/pgfplots_filesuffix.gnuplot
%doc %{_texmfdistdir}/doc/latex/pgfplots/gnuplot/pgfplots_filesuffix.table
%doc %{_texmfdistdir}/doc/latex/pgfplots/gnuplot/pgfplots_gnuplot_ppp.gnuplot
%doc %{_texmfdistdir}/doc/latex/pgfplots/gnuplot/pgfplots_gnuplot_ppp.table
%doc %{_texmfdistdir}/doc/latex/pgfplots/gnuplot/pgfplots_parable.gnuplot
%doc %{_texmfdistdir}/doc/latex/pgfplots/gnuplot/pgfplots_parable.table
%doc %{_texmfdistdir}/doc/latex/pgfplots/gnuplot/pgfplots_pow2.gnuplot
%doc %{_texmfdistdir}/doc/latex/pgfplots/gnuplot/pgfplots_pow2.table
%doc %{_texmfdistdir}/doc/latex/pgfplots/gnuplot/pgfplots_sin.gnuplot
%doc %{_texmfdistdir}/doc/latex/pgfplots/gnuplot/pgfplots_sin.table
%doc %{_texmfdistdir}/doc/latex/pgfplots/gnuplot/pgfplots_tangens.gnuplot
%doc %{_texmfdistdir}/doc/latex/pgfplots/gnuplot/pgfplots_tangens.table
%doc %{_texmfdistdir}/doc/latex/pgfplots/gpl-3.0.txt
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfmanual-en-macros.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots-macros.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.basic.reference.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.bib
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.figlist
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.importexport.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.install.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.intro.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.libs.clickable.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.libs.colormaps.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.libs.dateplot.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.libs.external.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.libs.groupplot.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.libs.patchplots.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.libs.polar.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.libs.smithchart.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.libs.ternary.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.libs.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.libs.units.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.makefile
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.mst
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.pdf
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.preamble.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.preliminaries.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.reference.2dplots.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.reference.3dconfiguration.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.reference.3dplots.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.reference.alignment.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.reference.axis-addplot.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.reference.axisdescription.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.reference.closingplots.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.reference.coordfiltering.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.reference.errorbars.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.reference.gridoptions-axiscoordinates.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.reference.layers.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.reference.linefitting.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.reference.markers-meta.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.reference.miscellaneous.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.reference.numberformatting.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.reference.preliminaryoptions.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.reference.scaling.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.reference.specifyrange.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.reference.styleoptions.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.reference.symbolic-transformations.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.reference.symbolic.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.reference.technicalinternals.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.reference.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.reference.tickoptions.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.reference.tikzinteroperability.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.reference.transformations.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.resources.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.testplot
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.testtable
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.testtable2.dat
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.timeseries.dat
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.title_abstract_intro.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.titlepage.pdf
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.titlepage.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.titlepage_contourtmp0.dat
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.titlepage_contourtmp0.script
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots.titlepage_contourtmp0.table
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots_contourtmp0.dat
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots_contourtmp0.script
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots_contourtmp0.table
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots_contourtmp1.dat
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots_contourtmp1.script
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots_contourtmp1.table
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplots_ocg_copy.sty
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplotsexample.pdf
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplotsexample.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplotstable.example1.csv
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplotstable.example1.dat
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplotstable.example2.dat
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplotstable.example3.dat
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplotstable.example4.dat
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplotstable.example5.dat
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplotstable.mst
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplotstable.pdf
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplotstable.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplotstodo.pdf
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfplotstodo.tex
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfshell_cos.sh
%doc %{_texmfdistdir}/doc/latex/pgfplots/pgfshell_replot.sh
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/FokkerDrI_layer_0.facetIdx.dat
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/FokkerDrI_layer_0.patches.dat
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/FokkerDrI_layer_0.vertices.dat
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/accounts.dat
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/first3d.dat
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/group-1.dat
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/newexperiment1.dat
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/newexperiment2.dat
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/newexperiment3.dat
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/oldexperiment1.dat
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/oldexperiment2.dat
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/oldexperiment3.dat
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/ou.dat
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/patchexample_conn.dat
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/patchexample_verts.dat
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/pgfplots.randn.dat
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/pgfplots_scatterdata1.dat
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/pgfplots_scatterdata1_latent.dat
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/pgfplots_scatterdata2.dat
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/pgfplots_scatterdata2_latent.dat
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/pgfplots_scatterdata3.dat
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/pgfplots_scatterdata4.dat
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/pgfplotscontourmatlabexample.dat
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/pgfplotscontourmatlabexample.m
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/pgfplotsexample4.dat
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/pgfplotsexample4_grid.dat
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/pgfplotsternary.example1.dat
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/plotgraphics1.m
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/plotgraphics3.m
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/plotgraphics3.png
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/plotgraphics3.seed
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/plotgraphics3d.png
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/plotgraphics3d.png.dat
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/plotgraphics3dsurf.png
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/plotgraphics3dsurfmatlab.png
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/plotgraphics3withaxis.png
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/plotgraphics_gimpmeasure.png
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/risingdrop3d.m
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/risingdrop3d.png
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/risingdrop3d_coord.dat
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/risingdrop3d_vel.dat
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/risingdrop3dwithaxis.png
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/scattercl.dat
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/smithchart_data.dat
%doc %{_texmfdistdir}/doc/latex/pgfplots/plotdata/ternary_data.txt
%doc %{_texmfdistdir}/doc/latex/pgfplots/texmf.cnf
%doc %{_texmfdistdir}/doc/latex/pgfplots/todo.archive.txt
%doc %{_texmfdistdir}/doc/plain/pgfplots/pgfplotsexample.pdf
%doc %{_texmfdistdir}/doc/plain/pgfplots/pgfplotsexample.tex
#- source
%doc %{_texmfdistdir}/source/context/third/pgfplots/pgfplotstests.tar.bz2
%doc %{_texmfdistdir}/source/latex/pgfplots/pgfplotstests.tar.bz2

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar scripts tex doc source %{buildroot}%{_texmfdistdir}
