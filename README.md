# MathData-SoSe22

Material für die Vorlesung "Mathematische Methoden in der Datenanalyse" im SoSe 2022 an der Universität Osnabrück.

Das Skript ist unter [diesem Link](https://pbrdng.github.io/MathData-SoSe22/MathData.pdf) verfügbar (im Laufe der Vorlesung wird mehr Inhalt hinzugefügt werden).

---
## Vorlesungen

[1. Vorlesung](https://pbrdng.github.io/MathData-SoSe22/Vorlesungen/VL01.pdf):

  * Verschiedene Interpretationen einer `n × m` Matrix `A`.
  * Orthogonale Zerlegung von `ℝⁿ` und `ℝᵐ`.
  * Die Pseudo-Inverse.

[2. Vorlesung](https://pbrdng.github.io/MathData-SoSe22/Vorlesungen/VL02.pdf):

  * Die Singulärwertzerlegung.
  * Eindeutigkeit von Singulärwerten.

[3. Vorlesung](https://pbrdng.github.io/MathData-SoSe22/Vorlesungen/VL03.pdf):

  * Frequentistischer und Bayes'scher Wahrscheinlichkeitsbegriff.
  * Zufallsvariablen.
  * Bayes' Theorem.

[4. Vorlesung](https://pbrdng.github.io/MathData-SoSe22/Vorlesungen/VL04.pdf):

  * Bayes' Theorem für Dichten.
  * Erwartungswert und Varianz.
  * Normalverteilung

[5. Vorlesung](https://pbrdng.github.io/MathData-SoSe22/Vorlesungen/VL05.pdf):

  * Die Laplace Matrix.

[6. Vorlesung](https://pbrdng.github.io/MathData-SoSe22/Vorlesungen/VL06.pdf):

  * Das Spektrum eines Graphen.
  * Beziehung zwischen Struktur eines Graphen und dessen Spektrum.

[7. Vorlesung](https://pbrdng.github.io/MathData-SoSe22/Vorlesungen/VL07.pdf):

  * Eigenvektoren der Laplace Matrix.
  * Notebook 2.

[8. Vorlesung](https://pbrdng.github.io/MathData-SoSe22/Vorlesungen/VL08.pdf):

  * Durchmesser eines Graphen.
  * Spannbäume.
  * Definition Markov-Prozess.

[9. Vorlesung](https://pbrdng.github.io/MathData-SoSe22/Vorlesungen/VL09.pdf):

  * Übergangsmatrix.
  * Stationäre Verteilung.

[10. Vorlesung](https://pbrdng.github.io/MathData-SoSe22/Vorlesungen/VL10.pdf):

  * Beweis von Existenz und Eindeutigkeit stationärer Verteilungen.
  * Metropolis-Hastings Algorithmus.

[11. Vorlesung](https://pbrdng.github.io/MathData-SoSe22/Vorlesungen/VL11.pdf):

  * Beweis von Existenz und Eindeutigkeit stationärer Verteilungen.
  * Metropolis-Hastings Algorithmus.

[12. Vorlesung](https://pbrdng.github.io/MathData-SoSe22/Vorlesungen/VL12.pdf):

  * Was ist Maschinelles Lernen?
  * Daten, Modelle und Lernen.

[13. Vorlesung](https://pbrdng.github.io/MathData-SoSe22/Vorlesungen/VL13.pdf):

  * Lineare Regression.
  * Least-Squares, Ridge-Regression und MLE.

[14. Vorlesung](https://pbrdng.github.io/MathData-SoSe22/Vorlesungen/VL14.pdf):

  * Nicht-lineare Regression.
  * MAP und Bayes'scher Ansatz.

[15. Vorlesung](https://pbrdng.github.io/MathData-SoSe22/Vorlesungen/VL15.pdf):

  * Das Modell "Neuronales Netz".

[16. Vorlesung](https://pbrdng.github.io/MathData-SoSe22/Vorlesungen/VL16.pdf):

  * Support Vector Machines.
  * Primale und Duale SVMs.


[17. Vorlesung](https://pbrdng.github.io/MathData-SoSe22/Vorlesungen/VL17.pdf):

  * Kernels.
  
---

## Julia und Jupyter Notebooks

Dieses Repository enthält die [Jupyter Notebooks](https://github.com/PBrdng/MathData-SoSe22/tree/main/Notebooks) aus der Vorlesung.<br>

Um die Notebooks zu verwenden wie folgt vorgehen:

* Notebooks downloaden (per Klick auf den grünen
`Code` Button entweder als Zip File oder mit einem Git Client wie [Github Desktop](https://desktop.github.com) oder [Sublime](https://www.sublimemerge.com)).
* Die neueste Version von Julia [downloaden](https://julialang.org/downloads/)
* Julia starten.
* In Julia per `]` in den Package manager wechseln.
* `add IJulia` ausführen
* Den Package manager per Backslash verlassen.
* `using IJulia` ausführen
* `notebook()` ausführen

Dann sollte sich ein Browserfenster öffnen, in dem lokal gespeicherte Notebooks geöffnet werden können.

Ergänzendes Material aus der [Julia Academy](https://github.com/JuliaAcademy):

* [Introduction to Julia](https://github.com/JuliaAcademy/Introduction-to-Julia)

* [Data Science](https://github.com/JuliaAcademy/DataScience)

* [Foundations of Machine Learning](https://github.com/JuliaAcademy/Foundations-of-Machine-Learning)

* [Data Frames](https://github.com/JuliaAcademy/DataFrames)

---

## Literatur
Die folgenden Referenzen bieten zusätzliches Material zum Inhalt der Vorlesung.

### 1. Lineare Algebra

[The Fundamental Theorem of Linear Algebra](https://www.engineering.iastate.edu/~julied/classes/CE570/Notes/strangpaper.pdf), Gilbert Strang.

### 2. Wahrscheinlichkeitstheorie

[Wikipedia Artikel](https://en.wikipedia.org/wiki/Probability_theory)

[Basic Probability Theory](https://faculty.math.illinois.edu/~r-ash/BPT/BPT.pdf), Robert B. Ash.

### 3. Netzwerkanalyse

[Spectral Graph Theory](https://mathweb.ucsd.edu/~fan/research/revised.html)
(insbesondere Kapitel 1), Fan Chung.

[Spectral Graph Theory](https://resources.mpi-inf.mpg.de/departments/d1/teaching/ws11/SGT/) (insbesondere Vorlesung 5), Thomas Sauerwald and He Sun

[Graph Theory in the Information Age](https://mathweb.ucsd.edu/~fan/wp/graph.pdf), Fan Chung.

[Computer Science Theory for the Information Age](https://www.cs.cmu.edu/~venkatg/teaching/CStheory-infoage/) (insbesondere Notes 5), Venkatesan Guruswami and Ravi Kannan.

### 4. Maschinelles Lernen

[Mathematics for Machine Learning](https://mml-book.github.io/book/mml-book.pdf) (insbesondere Kapitel 8-12), Marc Peter Deisenroth, A. Aldo Faisal und Cheng Soon Ong.

[Neural Network Theory](http://www.pc-petersen.eu/Neural_Network_Theory.pdf), Philipp Christian Petersen

### 5. Matrizen und Tensoren

[Geometric Methods on Low-Rank Matrix and Tensor Manifolds](https://link.springer.com/content/pdf/10.1007%2F978-3-030-31351-7_9.pdf), André Uschmajew and Bart Vandereycken.

[Tensor Decompositions and Applications](https://www.kolda.net/publication/TensorReview.pdf),
Tamara G. Kolda und Brett W. Bader.

### 6. Topologische Datenanalyse

[Topological Data Analysis Spring 2020](https://www.few.vu.nl/~botnan/lecture_notes.pdf), Magnus Bakke Botnan.

[Topological Data Analysis](https://fugacci.github.io/home/notes.html), Ulderico Fugacci.
