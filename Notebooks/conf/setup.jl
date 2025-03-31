using Pkg

# die nachfolgenden Environments werden im Ordner Notebooks/conf/ generiert.
# pro Paket wird immer eine feste Version festlegt, damit nur getestete Versionen
# verwendet werden. 
# es wird außerdem für jedes Paket in einem Kommentar der Link zum Paket hinterlegt
# damit etwaige Changes in den Sources eingesehen werden können, falls nötig. Unter
# Anderem ist in der Regel eine Project.toml pro Github Repository vorhanden, in dem
# die Version und deren Abhängigkeiten aufgeführt werden.

confPath = @__DIR__

# 01-julia_basics
Pkg.activate(joinpath(confPath, "01-julia_basics"))
Pkg.add(PackageSpec(name="Plots", version="1.40.9")) # https://github.com/JuliaPlots/Plots.jl

# 02-networks
Pkg.activate(joinpath(confPath, "02-networks"))
Pkg.add(PackageSpec(name="JSON3", version="1.14.1")) # https://github.com/quinnj/JSON3.jl
Pkg.add(PackageSpec(name="Plots", version="1.40.9")) # https://github.com/JuliaPlots/Plots.jl
Pkg.add(PackageSpec(name="GraphPlot", version="0.6.1")) # https://github.com/JuliaGraphs/GraphPlot.jl
Pkg.add(PackageSpec(name="Graphs", version="1.12.0")) # https://github.com/JuliaGraphs/Graphs.jl
Pkg.add(PackageSpec(name="Compose", version="0.9.2")) # https://github.com/GiovineItalia/Compose.jl
Pkg.add(PackageSpec(name="Cairo", version="1.1.1")) # https://github.com/GiovineItalia/Compose.jl
Pkg.add(PackageSpec(name="Fontconfig", version="0.4.0")) # https://github.com/JuliaGraphics/Fontconfig.jl
Pkg.add(PackageSpec(name="Images", version="0.26.2")) # https://github.com/JuliaImages/Images.jl
Pkg.add(PackageSpec(name="IJulia", version="1.26.0")) # https://github.com/JuliaLang/IJulia.jl

# 03-page_rank
# Achtung: Colors ist von GraphPlot abhängig, daher muss hier die korrekte Version gewählt werden
Pkg.activate(joinpath(confPath, "03-page_rank"))
Pkg.add(PackageSpec(name="Plots", version="1.40.9")) # https://github.com/JuliaPlots/Plots.jl
Pkg.add(PackageSpec(name="GraphPlot", version="0.6.1")) # https://github.com/JuliaGraphs/GraphPlot.jl
Pkg.add(PackageSpec(name="Graphs", version="1.12.0")) # https://github.com/JuliaGraphs/Graphs.jl
Pkg.add(PackageSpec(name="CSV", version="0.10.15")) # https://github.com/JuliaData/CSV.jl
Pkg.add(PackageSpec(name="Colors", version="0.12.0")) # https://github.com/JuliaGraphics/Colors.jl
Pkg.add(PackageSpec(name="DataFrames", version="1.7.0")) # https://github.com/JuliaData/DataFrames.jl
Pkg.add(PackageSpec(name="FileIO", version="1.17.0")) # https://github.com/JuliaIO/FileIO.jl
Pkg.add(PackageSpec(name="LinearAlgebra", version="1.12.0")) # https://github.com/JuliaLang/LinearAlgebra.jl
Pkg.add(PackageSpec(name="SparseArrays", version="1.12.0")) # https://github.com/JuliaSparse/SparseArrays.jl
Pkg.add(PackageSpec(name="VegaDatasets", version="2.1.1")) # https://github.com/queryverse/VegaDatasets.jl
Pkg.add(PackageSpec(name="VegaLite", version="3.3.0")) # https://github.com/queryverse/VegaLite.jl

# 04-regression
Pkg.activate(joinpath(confPath, "04-regression"))
Pkg.add(PackageSpec(name="Plots", version="1.40.9")) # https://github.com/JuliaPlots/Plots.jl
Pkg.add(PackageSpec(name="CSV", version="0.10.15")) # https://github.com/JuliaData/CSV.jl
Pkg.add(PackageSpec(name="Optim", version="1.11.0")) # https://github.com/JuliaNLSolvers/Optim.jl
Pkg.add(PackageSpec(name="RDatasets", version="0.7.7")) # https://github.com/JuliaStats/RDatasets.jl
Pkg.add(PackageSpec(name="StatsBase", version="0.34.4")) # https://github.com/JuliaStats/StatsBase.jl

# 05-classification
Pkg.activate(joinpath(confPath, "05-classification"))
Pkg.add(PackageSpec(name="Plots", version="1.40.9")) # https://github.com/JuliaPlots/Plots.jl
Pkg.add(PackageSpec(name="CSV", version="0.10.15")) # https://github.com/JuliaData/CSV.jl
Pkg.add(PackageSpec(name="Images", version="0.26.2")) # https://github.com/JuliaImages/Images.jl
Pkg.add(PackageSpec(name="Flux", version="0.16.3")) # https://github.com/FluxML/Flux.jl
Pkg.add(PackageSpec(name="ImageCore", version="0.10.5")) # https://github.com/JuliaImages/ImageCore.jl
Pkg.add(PackageSpec(name="JuMP", version="1.25.0")) # https://github.com/jump-dev/JuMP.jl
Pkg.add(PackageSpec(name="MLDatasets", version="0.7.18")) # https://github.com/JuliaML/MLDatasets.jl
Pkg.add(PackageSpec(name="NLopt", version="1.1.3")) # https://github.com/jump-dev/NLopt.jl

# 06-pca
Pkg.activate(joinpath(confPath, "06-pca"))
Pkg.add(PackageSpec(name="Plots", version="1.40.9")) # https://github.com/JuliaPlots/Plots.jl
Pkg.add(PackageSpec(name="CSV", version="0.10.15")) # https://github.com/JuliaData/CSV.jl
Pkg.add(PackageSpec(name="Images", version="0.26.2")) # https://github.com/JuliaImages/Images.jl
Pkg.add(PackageSpec(name="ImageCore", version="0.10.5")) # https://github.com/JuliaImages/ImageCore.jl
Pkg.add(PackageSpec(name="MLDatasets", version="0.7.18")) # https://github.com/JuliaML/MLDatasets.jl
Pkg.add(PackageSpec(name="Distributions", version="0.25.118")) # https://github.com/JuliaStats/Distributions.jl
Pkg.add(PackageSpec(name="StatsBase", version="0.34.4")) # https://github.com/JuliaStats/StatsBase.jl

# 07-tda
Pkg.activate(joinpath(confPath, "07-tda"))
Pkg.add(PackageSpec(name="Plots", version="1.40.9")) # https://github.com/JuliaPlots/Plots.jl
Pkg.add(PackageSpec(name="CSV", version="0.10.15")) # https://github.com/JuliaData/CSV.jl
Pkg.add(PackageSpec(name="DelimitedFiles", version="1.9.0")) # https://github.com/JuliaData/DelimitedFiles.jl
Pkg.add(PackageSpec(name="Ripserer", version="0.16.12")) # https://github.com/mtsch/Ripserer.jl
Pkg.add(PackageSpec(name="TSne", version="1.3.0")) # https://github.com/lejon/TSne.jl
Pkg.add(PackageSpec(name="StatsBase", version="0.34.4")) # https://github.com/JuliaStats/StatsBase.jl
Pkg.add(PackageSpec(name="PlotlyJS", version="0.18.5")) # https://github.com/JuliaPlots/PlotlyJS.jl