import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class Tugas:
    def __init__(self, deskripsi, prioritas, tenggat_waktu=None, selesai=False, catatan="", checklist=None):
        self.deskripsi = deskripsi
        self.prioritas = prioritas
        self.tenggat_waktu = datetime.strptime(tenggat_waktu, "%Y-%m-%d %H:%M") if tenggat_waktu else None
        self.selesai = selesai
        self.catatan = catatan
        self.checklist = checklist if checklist else []

class AplikasiToDolist:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List azhars App")
        self.root.configure(bg="blue")  

        self.tugas_list = []
        
        self.deskripsi_entry = tk.Entry(root, width=30)
        self.prioritas_entry = tk.Entry(root, width=10)
        self.tenggat_waktu_entry = tk.Entry(root, width=20)
        self.catatan_entry = tk.Entry(root, width=30)
        self.checklist_entry = tk.Entry(root, width=30)

        self.tugas_listbox = tk.Listbox(root, height=15, width=50)
        self.tugas_listbox.bind("<<ListboxSelect>>", self.tampilkan_tugas_terpilih)

        self.buat_tombol = tk.Button(root, text="Tambahkan Tugas", command=self.tambah_tugas)
        self.tampilkan_tugas_button = tk.Button(root, text="Tampilkan Tugas", command=self.tampilkan_tugas)
        self.tampilkan_tugas_prioritas_button = tk.Button(root, text="Tampilkan Tugas Prioritas Tinggi", command=self.tampilkan_tugas_prioritas)
        self.tandai_selesai_button = tk.Button(root, text="Tandai Selesai", command=self.tandai_selesai)
        self.tambah_catatan_button = tk.Button(root, text="Tambahkan Catatan", command=self.tambah_catatan)
        self.tambah_checklist_button = tk.Button(root, text="Tambahkan Checklist", command=self.tambah_checklist)
        self.hapus_tugas_button = tk.Button(root, text="Hapus Tugas", command=self.hapus_tugas)

        self.aturlah_antarmuka()

    def aturlah_antarmuka(self):
        tk.Label(self.root, text="Deskripsi Tugas:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.deskripsi_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.root, text="Prioritas (1-3):").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.prioritas_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.root, text="Tenggat Waktu (YYYY-MM-DD HH:MM):").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.tenggat_waktu_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.root, text="Catatan:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.catatan_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.root, text="Checklist Item:").grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.checklist_entry.grid(row=4, column=1, padx=5, pady=5)

        self.buat_tombol.grid(row=5, column=0, columnspan=2, pady=10)
        self.tampilkan_tugas_button.grid(row=6, column=0, columnspan=2, pady=5)
        self.tampilkan_tugas_prioritas_button.grid(row=7, column=0, columnspan=2, pady=5)
        self.tandai_selesai_button.grid(row=8, column=0, columnspan=2, pady=5)
        self.tambah_catatan_button.grid(row=9, column=0, columnspan=2, pady=5)
        self.tambah_checklist_button.grid(row=10, column=0, columnspan=2, pady=5)
        self.hapus_tugas_button.grid(row=11, column=0, columnspan=2, pady=5)

        self.tugas_listbox.grid(row=0, column=2, rowspan=12, padx=10, pady=10)

    def tambah_tugas(self):
        deskripsi = self.deskripsi_entry.get()
        prioritas = int(self.prioritas_entry.get())
        tenggat_waktu = self.tenggat_waktu_entry.get()
        catatan = self.catatan_entry.get()
        checklist_item = self.checklist_entry.get()

        tugas = Tugas(deskripsi, prioritas, tenggat_waktu, catatan=catatan, checklist=[checklist_item])
        self.tugas_list.append(tugas)
        self.reset_input_fields()
        messagebox.showinfo("Sukses", "Tugas berhasil ditambahkan!")

    def tampilkan_tugas(self):
        self.tugas_listbox.delete(0, tk.END)
        for i, tugas in enumerate(self.tugas_list, 1):
            status_selesai = "Selesai" if tugas.selesai else "Belum Selesai"
            self.tugas_listbox.insert(tk.END, f"{i}. {tugas.deskripsi} - Prioritas: {tugas.prioritas}, Tenggat Waktu: {tugas.tenggat_waktu}, Status: {status_selesai}")

    def tampilkan_tugas_prioritas(self):
        self.tugas_listbox.delete(0, tk.END)
        prioritas_tinggi = [tugas for tugas in self.tugas_list if tugas.prioritas == 3]
        if prioritas_tinggi:
            for i, tugas in enumerate(prioritas_tinggi, 1):
                status_selesai = "Selesai" if tugas.selesai else "Belum Selesai"
                self.tugas_listbox.insert(tk.END, f"{i}. {tugas.deskripsi} - Tenggat Waktu: {tugas.tenggat_waktu}, Status: {status_selesai}")
        else:
            self.tugas_listbox.insert(tk.END, "Tidak ada tugas dengan prioritas tinggi.")

    def tampilkan_tugas_terpilih(self, event):
        indeks_terpilih = self.tugas_listbox.curselection()
        if indeks_terpilih:
            indeks_terpilih = int(indeks_terpilih[0])
            tugas_terpilih = self.tugas_list[indeks_terpilih]
            messagebox.showinfo("Detail Tugas", f"{tugas_terpilih.deskripsi}\nPrioritas: {tugas_terpilih.prioritas}\nTenggat Waktu: {tugas_terpilih.tenggat_waktu}\nCatatan: {tugas_terpilih.catatan}\nChecklist: {', '.join(tugas_terpilih.checklist)}")
        else:
            messagebox.showinfo("Detail Tugas", "Pilih tugas terlebih dahulu.")

    def tandai_selesai(self):
        indeks_terpilih = self.tugas_listbox.curselection()
        if indeks_terpilih:
            indeks_terpilih = int(indeks_terpilih[0])
            self.tugas_list[indeks_terpilih].selesai = True
            self.tampilkan_tugas()
            messagebox.showinfo("Sukses", "Tugas berhasil ditandai sebagai selesai.")
        else:
            messagebox.showinfo("Tandai Selesai", "Pilih tugas terlebih dahulu.")

    def tambah_catatan(self):
        indeks_terpilih = self.tugas_listbox.curselection()
        if indeks_terpilih:
            indeks_terpilih = int(indeks_terpilih[0])
            catatan = self.catatan_entry.get()
            self.tugas_list[indeks_terpilih].catatan += f"\n{catatan}"
            self.tampilkan_tugas()
            messagebox.showinfo("Sukses", "Catatan berhasil ditambahkan.")
        else:
            messagebox.showinfo("Tambah Catatan", "Pilih tugas terlebih dahulu.")

    def tambah_checklist(self):
        indeks_terpilih = self.tugas_listbox.curselection()
        if indeks_terpilih:
            indeks_terpilih = int(indeks_terpilih[0])
            checklist_item = self.checklist_entry.get()
            self.tugas_list[indeks_terpilih].checklist.append(checklist_item)
            self.tampilkan_tugas()
            messagebox.showinfo("Sukses", "Checklist berhasil ditambahkan.")
        else:
            messagebox.showinfo("Tambah Checklist", "Pilih tugas woyyy!!.")

    def hapus_tugas(self):
        indeks_terpilih = self.tugas_listbox.curselection()
        if indeks_terpilih:
            indeks_terpilih = int(indeks_terpilih[0])
            del self.tugas_list[indeks_terpilih]
            self.tampilkan_tugas()
            messagebox.showinfo("Sukses", "Tugas berhasil dihapus.")
        else:
            messagebox.showinfo("Hapus Tugas", "Pilih tugas terlebih dahulu.")

    def reset_input_fields(self):
        self.deskripsi_entry.delete(0, tk.END)
        self.prioritas_entry.delete(0, tk.END)
        self.tenggat_waktu_entry.delete(0, tk.END)
        self.catatan_entry.delete(0, tk.END)
        self.checklist_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    aplikasi = AplikasiToDolist(root)

    root.mainloop()