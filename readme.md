# 🚌 OMSI 2 FOV Manager

A lightweight, safe, and automated utility for managing the Field of View (FOV) across all your OMSI 2 bus collections.

## 📝 Project Summary (Developer/Agent Notes)
This tool is a specialized **Python-GUI** application designed to automate the modification of `.bus` files in the OMSI 2 simulation environment. 

### Core Logic:
* **Target Identification:** Scans for the `3: Blick nach vorne (std)` camera block.
* **Offset Modification:** Edits the value exactly **6 lines** below the target header (the FOV parameter).
* **Safe Encoding:** Uses `latin-1` to ensure compatibility with German characters and prevent file corruption.
* **Intelligent Backup:** * Creates a `BK` subfolder for every vehicle folder.
    * Renames original files to `.bk` to distinguish them from standard game backups.
    * **Primary Safeguard:** It will *never* overwrite an existing `.bk` file, ensuring the original factory settings are preserved forever.

---

## 🚀 Installation

1. **Install Python:** Ensure [Python 3.x](https://www.python.org/) is installed on your system.
2. **Download:** Save the `omsi_fov_manager.py` script to your computer.
3. **No Dependencies:** This script uses only standard libraries (`tkinter`, `os`, `shutil`). No extra installation is required.

---

## 🛠 How to Use

### 1. Load the Game Path
Launch the script and click **"Load OMSI 2 Directory"**. Select your main folder (e.g., `C:\Steam\steamapps\common\OMSI 2`).

### 2. View and Filter
The tool automatically hides any files that do not contain the standard driver camera block. The list is sorted by folder name, with visual separators (`---`) between different bus models.

### 3. Update FOV
* **Select** the buses you want to change (use `Ctrl` or `Shift` for multiple selections).
* Enter the desired value in **New FOV Value** (Common values: 65, 75, 80).
* Click **"Update & Backup"**.

### 4. Restore
If you want to revert to the original view, select the bus and click **"Restore Original"**. The tool will fetch the `.bk` file from the `BK` folder and put it back.

---

## 📁 File Structure
The tool organizes your vehicle folders as follows:

```text
Vehicles/
└── [Bus_Folder]/
    ├── [Bus_Name].bus (Modified FOV)
    └── BK/
        ├── [Bus_Name].bus.bk     (Your original backup - PROTECTED)
        └── [Bus_Name].bus.backup (Legacy game backups moved here)