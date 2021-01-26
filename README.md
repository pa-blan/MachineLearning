# MachineLearning Demonstrator

### Anleitung Demonstrator für Machine learning: ###
Der Verwendete und geschriebene Code befindet sich im Order "Code" 

1. Anaconda herunterladen und starten https://www.anaconda.com/distribution/ (Python Distribution)
2. Da in den benötigten Bibliotheken C Code hinterlegt ist benötigt man einen C/C++ Compiler, funktioniert über Visual Studio IDE oder über Visual Studio Express, C/C++ Umgebung muss aber separat geruntergeladen werden
2. Neue Python 3.7 Umgebung auf Anaconda anlegen und für folgende Schritte verwenden
3. pyAudio Bibliotek installieren 
4. Anleitung auf github Represetory ausführen https://github.com/jsingh811/pyAudioProcessing
	git clone git@github.com:jsingh811/pyAudioProcessing.git
	cd C:\Users\Benutzer\pyAudioProcessing
	pip install -e .
	pip install -r requirements/requirements.txt
5. In Angelegten Order gehen, wahrscheinlich auf C:\Users\Benutzer\pyAudioProcessing
6. Unter C:\Users\Benutzer\pyAudioProcessing\data_samples\training Inhalt löschen und zwei Ordner mit Bezeichnung "links" und "rechts" anlegen
7. Unter C:\Users\Benutzer\pyAudioProcessing\data_samples\testing Inhalt löschen und einen Ordner mit Bezeichnung "test" anlegen
8. Aus diesem Ordner die Ordner "App", "plt", "qt" und "Sonstiges" in das Verzeichnis C:\Users\Benutzer\pyAudioProcessing kopieren
9. An der Applikation das Mikrofon via Klinkenkabel an eine Mikrofonbuchse anschließen, evtl wird externe Soundkarte benötigt
10. In Verzeichnis die Dartei Main.py Ausführen
11. Drei Buttons werden in einer GUI angezeicht, "Aufnehmen" dient dazu um die Trainingsdaten aufzunehmen (jeweils 10x je 10 Sekunden nach rechts und links), der Fortschritt wird in der kommandozeile ausgegeben, "Einlernen" nimmt die Trainingsdaten und trainiert die SVM , via "Testen" kann ein neues Soundfile aufgenommen werden und validiert werden, ob nach rechts oder links gedreht wurde
12. Jetzt sind Sie Fertig.



