# Anleitung zur Einrichtung einer virtuellen Python-Umgebung

## Voraussetzungen
- **Python 3.12.1** ist installiert (falls nicht, bitte installieren).
- **pip** (Python Package Installer) ist verfügbar.
- **Jupyter** oder **Visual Studio Code**

> **Hinweis:** Die folgenden Schritte funktionieren grundsätzlich auf Windows, Linux und macOS. Achte jeweils auf die ggf. abweichende Schreibweise der Befehle (z. B. `python3` statt `python` unter Linux/macOS).

---

## 1. Virtuelle Umgebung aktivieren

1. **Terminal/Kommandozeile öffnen**  
   - Unter Windows: „Eingabeaufforderung“ oder „PowerShell“.  
   - Unter Linux/macOS: beliebiges Terminal.

2. **Zum gewünschten Projektordner wechseln**, z. B.:  
   ```bash
   git clone git@github.com:jnwee/quantum-keydistribution-studproj.git
   cd quantum-keydistribution-studproj
   ```

3. **Virtuelle Umgebung aktivieren**:  
   - **Linux/macOS**:
     ```bash
     source quantum_env/bin/activate
     ```
   - **Windows**:
     ```bash
     .\quantum_env\bin\Activate.ps1
     ```

   Wenn alles klappt, erscheint der Name `(quantum_env)` oder ähnlich in deinem Terminal.
---

## 2. Abhängigkeiten installieren

1. **Vergewissere dich, dass die Umgebung aktiv ist** (siehe oben).  
2. Installiere die in deiner Projekt-Datei `requirements.txt` genannten Bibliotheken:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
   > Achte darauf, dass sich die `requirements.txt` im selben Verzeichnis befindet.

Diese Schritte stellen sicher, dass alle benötigten Python-Pakete (z. B. Qiskit, NumPy, Pandas etc.) in der exakt gleichen Version installiert werden. Damit verhält sich dein Projekt **unabhängig vom Betriebssystem** überall gleich.

---

## 3. Jupyter Notebook starten

1. **Stelle sicher, dass die Umgebung aktiv ist.**  
2. Starte Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
3. Öffne dann deine Notebook-Datei (z. B. `e91/e91_simulation.ipynb`).  

> Alternativ kannst du in der Notebook-Datei auch direkt auf den Kernel `quantum_env` wechseln.

---

## 4. Visual Studio Code

Wenn du VS Code verwenden möchtest, gehe wie folgt vor:

1. **Python-Erweiterung** installieren, falls noch nicht geschehen (im VS Code Extension Marketplace).
2. Projektordner in VS Code **öffnen**.
3. **Virtuelle Umgebung** als Interpreter auswählen:
   - Unten rechts in der Statusleiste auf die aktuell ausgewählte Python-Version klicken.
   - `quantum_env` aus der Liste wählen.
4. **Abhängigkeiten installieren** (innerhalb von VS Code):
   - Terminal in VS Code öffnen (**Ansicht → Terminal**).
   - Sicherstellen, dass du dich in der aktivierten Umgebung befindest (notfalls aktivieren wie in Schritt 1).
   - Dann wie gewohnt:
     ```bash
     pip install --upgrade pip
     pip install -r requirements.txt
     ```
5. **Notebook (.ipynb) öffnen**:
   - Ggf. Erweiterung „Jupyter“ installieren.
   - Notebook-Datei öffnen und in der Kernel-Auswahl auf `quantum_env` umstellen.

---

## 5. Deaktivieren der virtuellen Umgebung

Wenn du die Umgebung nicht mehr brauchst oder zum System-Python zurückkehren willst:

```bash
deactivate
```