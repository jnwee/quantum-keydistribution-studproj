# Anleitung zur Einrichtung einer Virtuellen Umgebung für BB84-Simulation

Diese Anleitung beschreibt, wie eine virtuelle Python-Umgebung eingerichtet wird, die für die BB84-Simulation mit Jupyter Notebook verwendet werden kann. Alternativ wird auch erklärt, wie Sie die Umgebung in Visual Studio Code nutzen können.

## Voraussetzungen
- Python 3.9 oder höher ist installiert.
- Pip (Python Package Installer) ist verfügbar.
- Optional: Visual Studio Code (VS Code).

---

## 1. Virtuelle Umgebung erstellen

1. Öffnen Sie ein Terminal oder eine Kommandozeile.
2. Navigieren Sie zu dem Verzeichnis, in dem Sie die virtuelle Umgebung erstellen möchten.
3. Führen Sie folgenden Befehl aus:

   ```bash
   python3 -m venv quantum-venv
   ```

4. Aktivieren Sie die virtuelle Umgebung:
   - **Linux/macOS:**
     ```bash
     source quantum-venv/bin/activate
     ```
   - **Windows:**
     ```bash
     quantum-venv\Scripts\activate
     ```

   Nach der Aktivierung wird der Name der Umgebung (z. B. `(quantum-venv)`) vor Ihrer Eingabeaufforderung angezeigt.

---

## 2. Abhängigkeiten installieren

1. Stellen Sie sicher, dass die virtuelle Umgebung aktiviert ist.
2. Installieren Sie die benötigten Python-Bibliotheken:

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

   Die Datei `requirements.txt` muss sich im selben Verzeichnis befinden.

---

## 3. Jupyter Notebook starten

1. Stellen Sie sicher, dass die virtuelle Umgebung aktiviert ist.
2. Starten Sie Jupyter Notebook:

   ```bash
   jupyter notebook
   ```

3. Öffnen Sie die Datei `bb84_simulation.ipynb` im Jupyter Notebook.

---

## 4. Visual Studio Code (optional)

1. Installieren Sie die Erweiterung **"Python"** in VS Code, falls noch nicht geschehen.
2. Öffnen Sie VS Code und navigieren Sie zu Ihrem Projektverzeichnis.
3. Wählen Sie unten rechts die Python-Umgebung **`quantum-venv`** aus:
   - Klicken Sie auf den Python-Interpreter unten links in der Statusleiste.
   - Wählen Sie die virtuelle Umgebung `quantum-venv` aus der Liste aus.

4. Installieren Sie die Abhängigkeiten in VS Code:
   - Öffnen Sie ein Terminal in VS Code (**Ansicht > Terminal**).
   - Führen Sie folgenden Befehl aus:
     ```bash
     pip install --upgrade pip
     pip install -r requirements.txt
     ```

5. Öffnen Sie die Datei `bb84_simulation.ipynb`:
   - Installieren Sie die Erweiterung **"Jupyter"**, falls noch nicht geschehen.
   - Öffnen Sie die Notebook-Datei und stellen Sie sicher, dass der Kernel `quantum-venv` ausgewählt ist.

---

## 5. Deaktivieren der virtuellen Umgebung

Wenn Sie mit der Arbeit fertig sind, können Sie die virtuelle Umgebung deaktivieren, indem Sie folgenden Befehl ausführen:

```bash
deactivate
```

---

### Hinweise
- Bei Problemen mit den Abhängigkeiten überprüfen Sie die Python-Version und stellen Sie sicher, dass alle Pakete in der `requirements.txt` korrekt installiert wurden.
- Verwenden Sie für eine bessere Entwicklungsumgebung VS Code mit den entsprechenden Erweiterungen.
