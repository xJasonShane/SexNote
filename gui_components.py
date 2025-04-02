import tkinter as tk
from tkinter import ttk
from data_handler import DataHandler

class AddPartnerFrame(ttk.Frame):
    def __init__(self, parent, data_handler):
        super().__init__(parent)
        self.data_handler = data_handler
        self.main_app = parent.master.master if isinstance(parent.master, ttk.Frame) else parent.master
        self.create_widgets()

    def create_widgets(self):
        # 个人信息输入
        ttk.Label(self, text="姓名：").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = ttk.Entry(self)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self, text="年龄：").grid(row=1, column=0, padx=5, pady=5)
        self.age_entry = ttk.Entry(self)
        self.age_entry.grid(row=1, column=1, padx=5, pady=5)

        # 选择框
        self.married_var = tk.BooleanVar()
        ttk.Checkbutton(self, text="已婚", variable=self.married_var).grid(row=2, column=0)
        
        # 提交按钮
        ttk.Button(self, text="添加记录", command=self.add_partner).grid(row=5, columnspan=2)

    def add_partner(self):
        partner_data = {
            'name': self.name_entry.get(),
            'age': int(self.age_entry.get()),
            'married': self.married_var.get()
        }
        try:
            partner_id = self.data_handler.add_partner(partner_data)
            self.master.show_sex_record(partner_id)
        except ValueError as e:
            tk.messagebox.showerror("错误", str(e))

class SexRecordFrame(ttk.Frame):
    def __init__(self, parent, data_handler, partner_id):
        super().__init__(parent)
        self.data_handler = data_handler
        self.partner_id = partner_id
        self.create_widgets()
        self.main_app = parent.master.master if isinstance(parent.master, ttk.Frame) else parent.master

    def create_widgets(self):
        ttk.Label(self, text="性爱地点：").grid(row=0, column=0)
        self.location_entry = ttk.Entry(self)
        self.location_entry.grid(row=0, column=1)
        
        ttk.Button(self, text="保存记录", command=self.save_record).grid(row=1, column=0)
        ttk.Button(self, text="返回", command=lambda: self.master.show_add()).grid(row=1, column=1)

    def save_record(self):
        record_data = {
            'location': self.location_entry.get(),
            'protection': "无防护措施"
        }
        self.data_handler.add_record(self.partner_id, record_data)
        tk.messagebox.showinfo("成功", "记录已保存")
        self.master.show_add()