# import os
# import tkinter as tk
# from tkinter import filedialog, messagebox, ttk

# class OMSIFovUpdater:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("OMSI 2 FOV Manager - בחירה מרובה")
#         self.root.geometry("600x650")
        
#         self.bus_data = [] # רשימה לשמירת נתיבי הקבצים
        
#         # כותרת
#         tk.Label(root, text="ניהול FOV לאוטובוסים ב-OMSI 2", font=("Arial", 14, "bold")).pack(pady=10)

#         # כפתור טעינה
#         tk.Button(root, text="1. טען את תיקיית OMSI 2", command=self.load_omsi, bg="#2196F3", fg="white").pack(pady=5)

#         # פריים לרשימה עם סרגל גלילה
#         frame = tk.Frame(root)
#         frame.pack(pady=10, fill=tk.BOTH, expand=True, padx=20)
        
#         self.tree = ttk.Treeview(frame, columns=("Bus", "File"), show="headings", selectmode="extended")
#         self.tree.heading("Bus", text="שם האוטובוס (תיקייה)")
#         self.tree.heading("File", text="קובץ .bus")
#         self.tree.column("Bus", width=250)
#         self.tree.column("File", width=250)
        
#         scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
#         self.tree.configure(yscrollcommand=scrollbar.set)
        
#         self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
#         scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

#         # הגדרות FOV
#         fov_frame = tk.Frame(root)
#         fov_frame.pack(pady=10)
#         tk.Label(fov_frame, text="FOV חדש:").pack(side=tk.LEFT)
#         self.fov_entry = tk.Entry(fov_frame, width=10)
#         self.fov_entry.insert(0, "75")
#         self.fov_entry.pack(side=tk.LEFT, padx=5)

#         # כפתורי פעולה
#         btn_frame = tk.Frame(root)
#         btn_frame.pack(pady=10)
        
#         tk.Button(btn_frame, text="בחר הכל", command=self.select_all).pack(side=tk.LEFT, padx=5)
#         tk.Button(btn_frame, text="בטל בחירה", command=self.deselect_all).pack(side=tk.LEFT, padx=5)
        
#         tk.Button(root, text="עדכן FOV לאוטובוסים שנבחרו", command=self.apply_changes, 
#                   bg="#4CAF50", fg="white", font=("Arial", 11, "bold"), pady=10).pack(pady=10, fill=tk.X, padx=100)

#     def load_omsi(self):
#         folder = filedialog.askdirectory(title="בחר את תיקיית OMSI 2 הראשית")
#         if not folder: return
        
#         vehicles_path = os.path.join(folder, "Vehicles")
#         if not os.path.exists(vehicles_path):
#             messagebox.showerror("שגיאה", "תיקיית Vehicles לא נמצאה!")
#             return

#         # ניקוי רשימה קיימת
#         for item in self.tree.get_children():
#             self.tree.delete(item)
#         self.bus_data.clear()

#         # סריקה
#         for root_dir, _, files in os.walk(vehicles_path):
#             for file in files:
#                 if file.endswith(".bus"):
#                     folder_name = os.path.basename(root_dir)
#                     item_id = self.tree.insert("", tk.END, values=(folder_name, file))
#                     self.bus_data.append({'id': item_id, 'path': os.path.join(root_dir, file)})

#     def select_all(self):
#         self.tree.selection_set(self.tree.get_children())

#     def deselect_all(self):
#         self.tree.selection_remove(self.tree.get_children())

#     def apply_changes(self):
#         selected_items = self.tree.selection()
#         if not selected_items:
#             messagebox.showwarning("אזהרה", "אנא בחר לפחות אוטובוס אחד מהרשימה (ניתן להשתמש ב-Ctrl או Shift)")
#             return

#         new_fov = self.fov_entry.get()
#         count = 0
        
#         for item_id in selected_items:
#             # מציאת הנתיב המתאים ל-ID שנבחר
#             file_path = next(item['path'] for item in self.bus_data if item['id'] == item_id)
            
#             if self.update_file(file_path, new_fov):
#                 count += 1
        
#         messagebox.showinfo("סיום", f"עודכנו {count} קבצים בהצלחה!")

#     def update_file(self, file_path, new_fov):
#         try:
#             with open(file_path, 'r', encoding='latin-1') as f:
#                 lines = f.readlines()

#             changed = False
#             for i in range(len(lines)):
#                 if "3: Blick nach vorne" in lines[i]:
#                     target_line = i + 6 # שורה 6 לפי המבנה שלך
#                     if target_line < len(lines):
#                         lines[target_line] = f"{new_fov}\n"
#                         changed = True
#                         break

#             if changed:
#                 with open(file_path, 'w', encoding='latin-1') as f:
#                     f.writelines(lines)
#                 return True
#         except:
#             return False
#         return False

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = OMSIFovUpdater(root)
#     root.mainloop() 


# import os
# import shutil
# import tkinter as tk
# from tkinter import filedialog, messagebox, ttk

# class OMSIFovUpdater:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("OMSI 2 FOV Manager - עם גיבוי ותצוגה מקדימה")
#         self.root.geometry("800x700")
        
#         self.bus_data = [] # שמירת נתונים

#         # כותרת
#         tk.Label(root, text="ניהול FOV עם גיבוי אוטומטי", font=("Arial", 14, "bold")).pack(pady=10)

#         # כפתור טעינה
#         tk.Button(root, text="טען את תיקיית OMSI 2", command=self.load_omsi, bg="#2196F3", fg="white", padx=10).pack(pady=5)

#         # פריים לרשימה
#         frame = tk.Frame(root)
#         frame.pack(pady=10, fill=tk.BOTH, expand=True, padx=20)
        
#         # הוספת עמודה ל-FOV נוכחי
#         self.tree = ttk.Treeview(frame, columns=("Bus", "File", "CurrentFOV"), show="headings", selectmode="extended")
#         self.tree.heading("Bus", text="שם האוטובוס")
#         self.tree.heading("File", text="קובץ .bus")
#         self.tree.heading("CurrentFOV", text="FOV נוכחי")
        
#         self.tree.column("Bus", width=200)
#         self.tree.column("File", width=200)
#         self.tree.column("CurrentFOV", width=100, anchor="center")
        
#         scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
#         self.tree.configure(yscrollcommand=scrollbar.set)
        
#         self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
#         scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

#         # הגדרות FOV
#         fov_frame = tk.Frame(root)
#         fov_frame.pack(pady=10)
#         tk.Label(fov_frame, text="FOV חדש להגדרה:").pack(side=tk.LEFT)
#         self.fov_entry = tk.Entry(fov_frame, width=10)
#         self.fov_entry.insert(0, "75")
#         self.fov_entry.pack(side=tk.LEFT, padx=5)

#         # כפתורי פעולה
#         btn_frame = tk.Frame(root)
#         btn_frame.pack(pady=10)
#         tk.Button(btn_frame, text="בחר הכל", command=self.select_all).pack(side=tk.LEFT, padx=5)
#         tk.Button(btn_frame, text="בטל בחירה", command=self.deselect_all).pack(side=tk.LEFT, padx=5)
        
#         tk.Button(root, text="גבה ועדכן אוטובוסים נבחרים", command=self.apply_changes, 
#                   bg="#4CAF50", fg="white", font=("Arial", 11, "bold"), pady=10).pack(pady=10, fill=tk.X, padx=150)

#     def get_current_fov(self, file_path):
#         """פונקציה שקוראת את ה-FOV הנוכחי מהקובץ"""
#         try:
#             with open(file_path, 'r', encoding='latin-1') as f:
#                 lines = f.readlines()
#             for i in range(len(lines)):
#                 if "3: Blick nach vorne" in lines[i]:
#                     target_line = i + 6
#                     if target_line < len(lines):
#                         return lines[target_line].strip()
#         except:
#             pass
#         return "N/A"

#     def load_omsi(self):
#         folder = filedialog.askdirectory(title="בחר את תיקיית OMSI 2 הראשית")
#         if not folder: return
        
#         vehicles_path = os.path.join(folder, "Vehicles")
#         if not os.path.exists(vehicles_path):
#             messagebox.showerror("שגיאה", "תיקיית Vehicles לא נמצאה!")
#             return

#         for item in self.tree.get_children():
#             self.tree.delete(item)
#         self.bus_data.clear()

#         for root_dir, _, files in os.walk(vehicles_path):
#             for file in files:
#                 if file.endswith(".bus"):
#                     full_path = os.path.join(root_dir, file)
#                     current_fov = self.get_current_fov(full_path)
#                     folder_name = os.path.basename(root_dir)
                    
#                     item_id = self.tree.insert("", tk.END, values=(folder_name, file, current_fov))
#                     self.bus_data.append({'id': item_id, 'path': full_path})

#     def select_all(self):
#         self.tree.selection_set(self.tree.get_children())

#     def deselect_all(self):
#         self.tree.selection_remove(self.tree.get_children())

#     def apply_changes(self):
#         selected_items = self.tree.selection()
#         if not selected_items:
#             messagebox.showwarning("אזהרה", "בחר אוטובוסים מהרשימה")
#             return

#         new_fov = self.fov_entry.get()
#         count = 0
        
#         for item_id in selected_items:
#             file_path = next(item['path'] for item in self.bus_data if item['id'] == item_id)
            
#             # --- שלב הגיבוי ---
#             bus_dir = os.path.dirname(file_path)
#             bk_dir = os.path.join(bus_dir, "BK")
            
#             if not os.path.exists(bk_dir):
#                 os.makedirs(bk_dir)
            
#             bk_file_path = os.path.join(bk_dir, os.path.basename(file_path))
            
#             # מעתיק לגיבוי רק אם הקובץ עוד לא קיים שם (כדי לא לדרוס את הגיבוי המקורי)
#             if not os.path.exists(bk_file_path):
#                 shutil.copy2(file_path, bk_file_path)
            
#             # --- שלב העדכון ---
#             if self.update_file(file_path, new_fov):
#                 count += 1
#                 # עדכון התצוגה בטבלה
#                 self.tree.set(item_id, column="CurrentFOV", value=new_fov)
        
#         messagebox.showinfo("סיום", f"עודכנו {count} קבצים.\nגיבויים נשמרו בתיקיות BK הפנימיות.")

#     def update_file(self, file_path, new_fov):
#         try:
#             with open(file_path, 'r', encoding='latin-1') as f:
#                 lines = f.readlines()

#             changed = False
#             for i in range(len(lines)):
#                 if "3: Blick nach vorne" in lines[i]:
#                     target_line = i + 6
#                     if target_line < len(lines):
#                         lines[target_line] = f"{new_fov}\n"
#                         changed = True
#                         break

#             if changed:
#                 with open(file_path, 'w', encoding='latin-1') as f:
#                     f.writelines(lines)
#                 return True
#         except:
#             return False
#         return False

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = OMSIFovUpdater(root)
#     root.mainloop()

# import os
# import shutil
# import tkinter as tk
# from tkinter import filedialog, messagebox, ttk

# class OMSIFovUpdater:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("OMSI 2 FOV Manager - Advanced Backup & Restore")
#         self.root.geometry("900x750")
#         self.bus_data = []

#         tk.Label(root, text="ניהול FOV עם מערכת שחזור (Restore)", font=("Arial", 14, "bold")).pack(pady=10)
#         tk.Button(root, text="טען את תיקיית OMSI 2", command=self.load_omsi, bg="#2196F3", fg="white").pack(pady=5)

#         # טבלה
#         frame = tk.Frame(root)
#         frame.pack(pady=10, fill=tk.BOTH, expand=True, padx=20)
#         self.tree = ttk.Treeview(frame, columns=("Bus", "File", "CurrentFOV", "HasBackup"), show="headings", selectmode="extended")
#         self.tree.heading("Bus", text="שם האוטובוס")
#         self.tree.heading("File", text="קובץ .bus")
#         self.tree.heading("CurrentFOV", text="FOV")
#         self.tree.heading("HasBackup", text="גיבוי קיים?")
        
#         self.tree.column("CurrentFOV", width=80, anchor="center")
#         self.tree.column("HasBackup", width=100, anchor="center")
        
#         scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
#         self.tree.configure(yscrollcommand=scrollbar.set)
#         self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
#         scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

#         # הגדרות FOV
#         fov_frame = tk.Frame(root)
#         fov_frame.pack(pady=10)
#         tk.Label(fov_frame, text="FOV חדש:").pack(side=tk.LEFT)
#         self.fov_entry = tk.Entry(fov_frame, width=10)
#         self.fov_entry.insert(0, "75")
#         self.fov_entry.pack(side=tk.LEFT, padx=5)

#         # כפתורים
#         btn_frame = tk.Frame(root)
#         btn_frame.pack(pady=10)
#         tk.Button(btn_frame, text="בחר הכל", command=self.select_all).pack(side=tk.LEFT, padx=5)
        
#         actions_frame = tk.Frame(root)
#         actions_frame.pack(pady=10)
#         tk.Button(actions_frame, text="עדכן וגבה נבחרים", command=self.apply_changes, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), width=20).pack(side=tk.LEFT, padx=10)
#         tk.Button(actions_frame, text="שחזר מגיבוי (Restore)", command=self.restore_backup, bg="#f44336", fg="white", font=("Arial", 10, "bold"), width=20).pack(side=tk.LEFT, padx=10)

#     def get_info(self, file_path):
#         fov = "N/A"
#         has_bk = "❌"
#         try:
#             with open(file_path, 'r', encoding='latin-1') as f:
#                 lines = f.readlines()
#             for i, line in enumerate(lines):
#                 if "3: Blick nach vorne" in line:
#                     fov = lines[i+6].strip()
#                     break
            
#             bk_path = os.path.join(os.path.dirname(file_path), "BK", os.path.basename(file_path) + ".bk")
#             if os.path.exists(bk_path):
#                 has_bk = "✅"
#         except: pass
#         return fov, has_bk

#     def load_omsi(self):
#         folder = filedialog.askdirectory(title="בחר את תיקיית OMSI 2")
#         if not folder: return
#         vehicles_path = os.path.join(folder, "Vehicles")
        
#         for item in self.tree.get_children(): self.tree.delete(item)
#         self.bus_data.clear()

#         for root_dir, _, files in os.walk(vehicles_path):
#             # טיפול בקבצי .backup ישנים - העברה ל-BK
#             bk_dir = os.path.join(root_dir, "BK")
#             for f in files:
#                 if f.endswith(".backup"):
#                     if not os.path.exists(bk_dir): os.makedirs(bk_dir)
#                     old_backup_path = os.path.join(root_dir, f)
#                     new_backup_place = os.path.join(bk_dir, f)
#                     if not os.path.exists(new_backup_place):
#                         shutil.move(old_backup_path, new_backup_place)
#                     else:
#                         os.remove(old_backup_path) # אם כבר קיים ב-BK, מוחק את המקור

#             # טעינת קבצי ה-bus לטבלה
#             for f in files:
#                 if f.endswith(".bus"):
#                     path = os.path.join(root_dir, f)
#                     fov, has_bk = self.get_info(path)
#                     item_id = self.tree.insert("", tk.END, values=(os.path.basename(root_dir), f, fov, has_bk))
#                     self.bus_data.append({'id': item_id, 'path': path})

#     def apply_changes(self):
#         selected = self.tree.selection()
#         new_fov = self.fov_entry.get()
#         for item_id in selected:
#             file_path = next(b['path'] for b in self.bus_data if b['id'] == item_id)
#             bk_dir = os.path.join(os.path.dirname(file_path), "BK")
#             if not os.path.exists(bk_dir): os.makedirs(bk_dir)
            
#             bk_file = os.path.join(bk_dir, os.path.basename(file_path) + ".bk")
#             if not os.path.exists(bk_file):
#                 shutil.copy2(file_path, bk_file) # יצירת גיבוי .bk ראשוני
            
#             if self.update_file(file_path, new_fov):
#                 self.tree.set(item_id, "CurrentFOV", new_fov)
#                 self.tree.set(item_id, "HasBackup", "✅")
#         messagebox.showinfo("הצלחה", "הקבצים עודכנו וגובו לתיקיית BK בפורמט .bk")

#     def restore_backup(self):
#         selected = self.tree.selection()
#         if not selected: return
        
#         count = 0
#         for item_id in selected:
#             file_path = next(b['path'] for b in self.bus_data if b['id'] == item_id)
#             bk_file = os.path.join(os.path.dirname(file_path), "BK", os.path.basename(file_path) + ".bk")
            
#             if os.path.exists(bk_file):
#                 shutil.copy2(bk_file, file_path) # החזרת הגיבוי למקור
#                 fov, _ = self.get_info(file_path)
#                 self.tree.set(item_id, "CurrentFOV", fov)
#                 count += 1
        
#         messagebox.showinfo("שחזור", f"שוחזרו {count} קבצים מהגיבוי המקורי.")

#     def update_file(self, file_path, new_fov):
#         try:
#             with open(file_path, 'r', encoding='latin-1') as f: lines = f.readlines()
#             for i, line in enumerate(lines):
#                 if "3: Blick nach vorne" in line:
#                     lines[i+6] = f"{new_fov}\n"
#                     with open(file_path, 'w', encoding='latin-1') as f: f.writelines(lines)
#                     return True
#         except: return False
#         return False

#     def select_all(self): self.tree.selection_set(self.tree.get_children())

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = OMSIFovUpdater(root)
#     root.mainloop()

import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class OMSIFovUpdater:
    def __init__(self, root):
        self.root = root
        self.root.title("OMSI 2 FOV Manager - Advanced Edition")
        self.root.geometry("900x750")
        self.bus_data = []

        # Header UI
        header_frame = tk.Frame(root, bg="#2c3e50", pady=10)
        header_frame.pack(fill=tk.X)
        tk.Label(header_frame, text="OMSI 2 FOV Manager", font=("Arial", 16, "bold"), fg="white", bg="#2c3e50").pack()

        btn_load = tk.Button(root, text="Load OMSI 2 Directory", command=self.load_omsi, bg="#3498db", fg="white", font=("Arial", 10, "bold"))
        btn_load.pack(pady=10)

        # Table UI
        frame = tk.Frame(root)
        frame.pack(pady=10, fill=tk.BOTH, expand=True, padx=20)
        
        style = ttk.Style()
        style.configure("Treeview", rowheight=25)
        
        self.tree = ttk.Treeview(frame, columns=("Bus", "File", "CurrentFOV", "HasBackup"), show="headings", selectmode="extended")
        self.tree.heading("Bus", text="Bus Folder")
        self.tree.heading("File", text="Bus File (.bus)")
        self.tree.heading("CurrentFOV", text="Current FOV")
        self.tree.heading("HasBackup", text="Backup Status")
        
        self.tree.column("Bus", width=250)
        self.tree.column("File", width=200)
        self.tree.column("CurrentFOV", width=100, anchor="center")
        self.tree.column("HasBackup", width=120, anchor="center")

        # Separator row styling
        self.tree.tag_configure('separator', background='#ecf0f1')

        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Control Panel
        control_panel = tk.LabelFrame(root, text=" Actions & Settings ", padx=10, pady=10)
        control_panel.pack(pady=20, padx=20, fill=tk.X)

        tk.Label(control_panel, text="New FOV Value:").grid(row=0, column=0, padx=5)
        self.fov_entry = tk.Entry(control_panel, width=8)
        self.fov_entry.insert(0, "75")
        self.fov_entry.grid(row=0, column=1, padx=5)

        tk.Button(control_panel, text="Select All", command=self.select_all).grid(row=0, column=2, padx=10)
        
        tk.Button(control_panel, text="Update & Backup", command=self.apply_changes, bg="#27ae60", fg="white", width=18, font=("Arial", 9, "bold")).grid(row=0, column=3, padx=5)
        tk.Button(control_panel, text="Restore Original", command=self.restore_backup, bg="#e74c3c", fg="white", width=18, font=("Arial", 9, "bold")).grid(row=0, column=4, padx=5)

    def get_info(self, file_path):
        """Checks if FOV section exists and returns the value and backup status."""
        try:
            with open(file_path, 'r', encoding='latin-1') as f:
                lines = f.readlines()
            for i, line in enumerate(lines):
                if "3: Blick nach vorne" in line:
                    # Validating that the FOV line (6 rows down) exists
                    if i + 6 < len(lines):
                        fov = lines[i+6].strip()
                        bk_path = os.path.join(os.path.dirname(file_path), "BK", os.path.basename(file_path) + ".bk")
                        status = "✅ BK Ready" if os.path.exists(bk_path) else "❌ No Backup"
                        return fov, status
            return None, None 
        except:
            return None, None

    def load_omsi(self):
        """Scans the directory, handles legacy .backup files, and populates the table."""
        folder = filedialog.askdirectory(title="Select OMSI 2 Main Directory")
        if not folder: return
        vehicles_path = os.path.join(folder, "Vehicles")
        
        if not os.path.exists(vehicles_path):
            messagebox.showerror("Error", "Vehicles folder not found in the selected path!")
            return

        # Clear existing table data
        for item in self.tree.get_children(): self.tree.delete(item)
        self.bus_data.clear()

        last_folder = ""
        
        # Sorting directories alphabetically
        try:
            all_dirs = sorted(os.listdir(vehicles_path))
        except:
            return

        for d in all_dirs:
            d_path = os.path.join(vehicles_path, d)
            if not os.path.isdir(d_path): continue
            
            # Sub-scan for legacy .backup files to clean the folder
            for f in os.listdir(d_path):
                if f.endswith(".backup"):
                    bk_dir = os.path.join(d_path, "BK")
                    if not os.path.exists(bk_dir): os.makedirs(bk_dir)
                    old_path = os.path.join(d_path, f)
                    new_path = os.path.join(bk_dir, f)
                    if not os.path.exists(new_path):
                        shutil.move(old_path, new_path)
                    else:
                        os.remove(old_path)

            # Loading .bus files
            for f in os.listdir(d_path):
                if f.endswith(".bus"):
                    full_path = os.path.join(d_path, f)
                    fov, status = self.get_info(full_path)
                    
                    # Only show files that have the FOV section
                    if fov:
                        # Insert visual separator (HR) between different bus folders
                        if last_folder != "" and last_folder != d:
                            self.tree.insert("", tk.END, values=("---", "---", "---", "---"), tags=('separator',))
                        
                        item_id = self.tree.insert("", tk.END, values=(d, f, fov, status))
                        self.bus_data.append({'id': item_id, 'path': full_path})
                        last_folder = d

    def apply_changes(self):
        """Saves current state to .bk and applies new FOV value."""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Selection Required", "Please select at least one bus from the list.")
            return

        new_fov = self.fov_entry.get()
        updated_count = 0

        for item_id in selected:
            vals = self.tree.item(item_id, 'values')
            if vals[0] == "---": continue 
            
            file_path = next(b['path'] for b in self.bus_data if b['id'] == item_id)
            bk_dir = os.path.join(os.path.dirname(file_path), "BK")
            if not os.path.exists(bk_dir): os.makedirs(bk_dir)
            
            # Create .bk file only if it doesn't exist (preserving original state)
            bk_file = os.path.join(bk_dir, os.path.basename(file_path) + ".bk")
            if not os.path.exists(bk_file):
                shutil.copy2(file_path, bk_file)
            
            if self.update_file_fov(file_path, new_fov):
                self.tree.set(item_id, "CurrentFOV", new_fov)
                self.tree.set(item_id, "HasBackup", "✅ BK Ready")
                updated_count += 1

        messagebox.showinfo("Success", f"Updated {updated_count} files successfully!")

    def restore_backup(self):
        """Restores the original .bus file from the saved .bk file."""
        selected = self.tree.selection()
        if not selected: return
        
        restored_count = 0
        for item_id in selected:
            vals = self.tree.item(item_id, 'values')
            if vals[0] == "---": continue
            
            file_path = next(b['path'] for b in self.bus_data if b['id'] == item_id)
            bk_file = os.path.join(os.path.dirname(file_path), "BK", os.path.basename(file_path) + ".bk")
            
            if os.path.exists(bk_file):
                shutil.copy2(bk_file, file_path)
                fov, _ = self.get_info(file_path)
                self.tree.set(item_id, "CurrentFOV", fov)
                restored_count += 1
        
        messagebox.showinfo("Restore", f"Restored {restored_count} files to their original state.")

    def update_file_fov(self, file_path, new_fov):
        """Finds the FOV line and overwrites it."""
        try:
            with open(file_path, 'r', encoding='latin-1') as f:
                lines = f.readlines()
            
            for i, line in enumerate(lines):
                if "3: Blick nach vorne" in line:
                    lines[i+6] = f"{new_fov}\n"
                    with open(file_path, 'w', encoding='latin-1') as f:
                        f.writelines(lines)
                    return True
        except:
            return False
        return False

    def select_all(self):
        """Selects all items in the list, skipping separators."""
        all_items = self.tree.get_children()
        to_select = [i for i in all_items if self.tree.item(i, 'values')[0] != "---"]
        self.tree.selection_set(to_select)

if __name__ == "__main__":
    root = tk.Tk()
    app = OMSIFovUpdater(root)
    root.mainloop()