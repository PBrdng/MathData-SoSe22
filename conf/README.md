# Über dieses Verzeichnis
Die Environments werden in den Unterverzeichnissen gespeichert. Die Project.toml gibt die direkt verwendeten Pakete an. Die Manifest.toml enthält Versionen und Abhängigkeiten. Die setup.jl dient der Erzeugung dieser Environments.

## setup.jl
Pro Environment werden Pakete via *Pkg.add* hinzugefügt. Jeder Aufruf gibt exakte Paketversionen an und ist von einem Kommentar zum jeweiligen Github-Repository gefolgt.

Beispiel: Hinzufügen von *Plots* der Version *1.40.9* vom Repository https://github.com/JuliaPlots/Plots.jl
```julia
Pkg.add(PackageSpec(name="Plots", version="1.40.9")) # https://github.com/JuliaPlots/Plots.jl
```

## Paketversionen
In der Regel können die neusten Versionen von Paketen verwendet werden. Aber: Gelegentlich ändern sich Schnittstellen (wie z.B. Parameter von Methoden). Damit sichergestellt wird, dass die Notebooks auch in mehreren Jahren genau so funktionieren, wie beim letzten Test der Notebooks, werden nicht die neusten Paketversionen verwendet, sondern stattdessen exakt angegebene Paketversionen.

## Bekannte Probleme
Das Notebook *03-page_rank* verwendet Paket *Colors* der Version *0.12.0*, weil dies kompatibel mit Paket *GraphPlot* der Version *0.6.1* ist. Es scheint, als wäre diese *GraphPlot* Version auch mit *Colors* der Version *0.13.0* kompatibel, aber beim Testen ist dies fehlgeschlagen.

## Update-Prozess
Folgender Pseudocode könnte verwendet werden:
```
foreach e in environments
    foreach p in e.packages
        prüfe den Link des Repositories
        aktualisiere die Paketversion in setup.jl
        führe setup.jl aus
        führe das zugehörige Notebook aus
        if Notebook funktioniert nicht
            roll back
        end
    end
end
```
*Pkg* gibt mit der Methode *status* Informationen über potentiell aktualisierbare Pakete aus. Beim Ausführen von *setup.jl* werden außerdem Informationen zu potentiellen Aktualisierungen ausgegeben. Letztlich muss allerdings individuell geprüft werden, ob neuere/die neuste Version eines Pakets geeignet ist.