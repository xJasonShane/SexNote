import tkinter as tk
from tkinter import ttk, messagebox
from data_handler import DataHandler

class AddPartnerFrame(ttk.Frame):
    def __init__(self, parent, data_handler):
        super().__init__(parent)
        self.data_handler = data_handler
        self.main_app = parent.master if isinstance(parent.master, tk.Tk) else parent.master.master
        self.create_widgets()

    def create_widgets(self):
        # 个人信息输入
        ttk.Label(self, text="姓名：").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = ttk.Entry(self)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self, text="年龄：").grid(row=1, column=0, padx=5, pady=5)
        self.age_entry = ttk.Entry(self)
        self.age_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self, text="胸围：").grid(row=2, column=0, padx=5, pady=5)
        self.bust_entry = ttk.Entry(self)
        self.bust_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(self, text="户型：").grid(row=3, column=0, padx=5, pady=5)
        self.type_entry = ttk.Entry(self)
        self.type_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(self, text="备注：").grid(row=4, column=0, padx=5, pady=5)
        self.note_entry = ttk.Entry(self)
        self.note_entry.grid(row=4, column=1, padx=5, pady=5)

        ttk.Label(self, text="登记日期：").grid(row=5, column=0, padx=5, pady=5)
        from tkcalendar import DateEntry
        self.date_entry = DateEntry(self, date_pattern='y-mm-dd')
        self.date_entry.grid(row=5, column=1, padx=5, pady=5)

        # 选择框
        self.married_var = tk.BooleanVar()
        ttk.Checkbutton(self, text="已婚", variable=self.married_var).grid(row=6, column=0)
        
        self.love_var = tk.BooleanVar()
        ttk.Checkbutton(self, text="恋爱", variable=self.love_var).grid(row=6, column=1)
        
        self.virgin_var = tk.BooleanVar()
        ttk.Checkbutton(self, text="处女", variable=self.virgin_var).grid(row=7, column=0)
        
        self.child_var = tk.BooleanVar()
        ttk.Checkbutton(self, text="育子", variable=self.child_var).grid(row=7, column=1)
        
        # 提交按钮
        ttk.Button(self, text="添加记录", command=self.add_partner).grid(row=8, columnspan=2)

    def add_partner(self):
        partner_data = {
            'name': self.name_entry.get(),
            'age': int(self.age_entry.get()),
            'bust': self.bust_entry.get(),
            'type': self.type_entry.get(),
            'note': self.note_entry.get(),
            'date': self.date_entry.get(),
            'married': self.married_var.get(),
            'in_love': self.love_var.get(),
            'is_virgin': self.virgin_var.get(),
            'has_child': self.child_var.get()
        }
        try:
            partner_id = self.data_handler.add_partner(partner_data)
            self.main_app.show_sex_record(partner_id)
        except ValueError as e:
            messagebox.showerror("错误", str(e))

class SettingsFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()
        self.main_app = parent.master if isinstance(parent.master, tk.Tk) else parent.master.master

    def create_widgets(self):
        # 从配置文件读取设置信息
        import json
        with open('config.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        # 版本信息
        ttk.Label(self, text=f"版本号: {config['version']}").pack(pady=5)
        ttk.Label(self, text=f"作者: {config['author']}").pack(pady=5)
        
        # GitHub链接
        github_frame = ttk.Frame(self)
        github_frame.pack(pady=5)
        ttk.Label(github_frame, text="GitHub: ").pack(side="left")
        github_link = ttk.Label(github_frame, text=config['github_url'], foreground="blue")
        github_link.pack(side="left")
        github_link.bind("<Button-1>", lambda e: self.open_github())
        


    def open_github(self):
        import webbrowser
        import json
        with open('config.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
        webbrowser.open(config['github_url'])


class SexRecordFrame(ttk.Frame):
    def __init__(self, parent, data_handler, partner_id):
        super().__init__(parent)
        self.data_handler = data_handler
        self.partner_id = partner_id
        self.create_widgets()
        self.main_app = parent.master if isinstance(parent.master, tk.Tk) else parent.master.master

    def create_widgets(self):
        # 性爱地点输入框
        ttk.Label(self, text="性爱地点：").grid(row=0, column=0)
        self.location_entry = ttk.Entry(self)
        self.location_entry.grid(row=0, column=1)
        
        # 性爱日期选择框
        ttk.Label(self, text="性爱日期：").grid(row=1, column=0)
        self.date_entry = ttk.Entry(self)
        self.date_entry.grid(row=1, column=1)
        
        # 是否高潮选择框
        ttk.Label(self, text="是否高潮：").grid(row=2, column=0)
        self.orgasm_var = tk.StringVar()
        self.orgasm_combobox = ttk.Combobox(self, textvariable=self.orgasm_var, values=["是", "否"])
        self.orgasm_combobox.grid(row=2, column=1)
        
        # 防护措施选择框
        ttk.Label(self, text="防护措施：").grid(row=3, column=0)
        self.protection_var = tk.StringVar()
        self.protection_combobox = ttk.Combobox(self, textvariable=self.protection_var, values=["无防护措施", "避孕套", "药物", "其他"])
        self.protection_combobox.grid(row=3, column=1)
        
        # 按钮区域
        ttk.Button(self, text="添加记录", command=self.save_record).grid(row=4, column=0)
        ttk.Button(self, text="返回", command=lambda: self.master.show_add()).grid(row=4, column=1)

    def save_record(self):
        record_data = {
            'location': self.location_entry.get(),
            'date': self.date_entry.get(),
            'orgasm': self.orgasm_var.get(),
            'protection': self.protection_var.get()
        }
        self.data_handler.add_record(self.partner_id, record_data)
        messagebox.showinfo("成功", "记录已保存")
        self.main_app.show_add()