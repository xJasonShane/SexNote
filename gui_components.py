import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, font
from datetime import datetime
from tkinter import messagebox
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
        ttk.Label(self, text="婚姻状态：").grid(row=6, column=0, padx=5, pady=5)
        self.marriage_var = tk.StringVar()
        ttk.Combobox(self, textvariable=self.marriage_var, values=["未婚","已婚","离异"]).grid(row=6, column=1, padx=5, pady=5)
        
        ttk.Label(self, text="恋爱状态：").grid(row=6, column=2, padx=5, pady=5)
        self.relationship_var = tk.StringVar()
        ttk.Combobox(self, textvariable=self.relationship_var, values=["单身","恋爱中","暧昧"]).grid(row=6, column=3, padx=5, pady=5)
        
        ttk.Label(self, text="处女状态：").grid(row=7, column=0, padx=5, pady=5)
        self.virgin_var = tk.StringVar()
        ttk.Combobox(self, textvariable=self.virgin_var, values=["是","否"]).grid(row=7, column=1, padx=5, pady=5)
        
        ttk.Label(self, text="育子状态：").grid(row=7, column=2, padx=5, pady=5)
        self.child_var = tk.StringVar()
        ttk.Combobox(self, textvariable=self.child_var, values=["有","无"]).grid(row=7, column=3, padx=5, pady=5)
        
        # 提交按钮
        ttk.Button(self, text="添加记录", command=self.add_partner).grid(row=8, columnspan=2)

    def add_partner(self):
        # 验证必填字段
        name = self.name_entry.get().strip()
        age = self.age_entry.get().strip()
        if not name or not age:
            messagebox.showerror("错误", "姓名和年龄是必填项")
            return
            
        try:
            age_int = int(age)
        except ValueError:
            messagebox.showerror("错误", "年龄必须是数字")
            return
            
        partner_data = {
            'name': name,
            'age': age_int,
            'bust': self.bust_entry.get(),
            'type': self.type_entry.get(),
            'note': self.note_entry.get(),
            'date': self.date_entry.get(),
            'married': self.marriage_var.get(),
            'in_love': self.relationship_var.get(),
            'is_virgin': self.virgin_var.get(),
            'has_child': self.child_var.get(),
            'created_at': datetime.now().isoformat(),
            'last_updated': None
        }
        try:
            partner_id = self.data_handler.add_partner(partner_data)
            if hasattr(self.main_app, 'show_sex_record'):
                self.main_app.show_sex_record(partner_id)
            else:
                messagebox.showinfo("提示", "记录添加成功")
        except ValueError as e:
            messagebox.showerror("错误", str(e))

    def create_widgets(self):
        # 查询条件区域
        query_frame = ttk.Frame(self)
        query_frame.pack(fill="x", padx=5, pady=5)
        
        # 第一行：基本信息查询
        ttk.Label(query_frame, text="姓名：").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = ttk.Entry(query_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(query_frame, text="年龄：").grid(row=0, column=2, padx=5, pady=5)
        self.age_entry = ttk.Entry(query_frame)
        self.age_entry.grid(row=0, column=3, padx=5, pady=5)
        
        ttk.Label(query_frame, text="胸围：").grid(row=0, column=4, padx=5, pady=5)
        self.bust_entry = ttk.Entry(query_frame)
        self.bust_entry.grid(row=0, column=5, padx=5, pady=5)
        
        ttk.Label(query_frame, text="户型：").grid(row=0, column=6, padx=5, pady=5)
        self.type_entry = ttk.Entry(query_frame)
        self.type_entry.grid(row=0, column=7, padx=5, pady=5)
        
        # 第二行：日期范围
        ttk.Label(query_frame, text="登记日期从：").grid(row=1, column=0, padx=5, pady=5)
        from tkcalendar import DateEntry
        self.start_date_entry = DateEntry(query_frame, date_pattern='y-mm-dd')
        self.start_date_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(query_frame, text="到：").grid(row=1, column=2, padx=5, pady=5)
        self.end_date_entry = DateEntry(query_frame, date_pattern='y-mm-dd')
        self.end_date_entry.grid(row=1, column=3, padx=5, pady=5)
        
        # 第三行：状态选择
        ttk.Label(query_frame, text="婚姻状态：").grid(row=2, column=0, padx=5, pady=5)
        self.marriage_var = tk.StringVar()
        ttk.Combobox(query_frame, textvariable=self.marriage_var, values=["未婚","已婚","离异"]).grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(query_frame, text="恋爱状态：").grid(row=2, column=2, padx=5, pady=5)
        self.relationship_var = tk.StringVar()
        ttk.Combobox(query_frame, textvariable=self.relationship_var, values=["单身","恋爱中","暧昧"]).grid(row=2, column=3, padx=5, pady=5)
        
        ttk.Label(query_frame, text="处女状态：").grid(row=2, column=4, padx=5, pady=5)
        self.virgin_var = tk.StringVar()
        ttk.Combobox(query_frame, textvariable=self.virgin_var, values=["是","否"]).grid(row=2, column=5, padx=5, pady=5)
        
        ttk.Label(query_frame, text="育子状态：").grid(row=2, column=6, padx=5, pady=5)
        self.child_var = tk.StringVar()
        ttk.Combobox(query_frame, textvariable=self.child_var, values=["有","无"]).grid(row=2, column=7, padx=5, pady=5)
        
        # 查询按钮
        ttk.Button(query_frame, text="查询", command=self.search).grid(row=1, column=4, columnspan=2, pady=5)
        
        # 结果显示区域
        result_frame = ttk.Frame(self)
        result_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        # 结果显示表格
        self.tree = ttk.Treeview(result_frame, columns=("name", "age", "bust", "type", "date", "note", "married", "in_love", "is_virgin", "has_child"), show="headings")
        self.tree.pack(fill="both", expand=True)
        
        self.tree.heading("name", text="姓名")
        self.tree.heading("age", text="年龄")
        self.tree.heading("bust", text="胸围")
        self.tree.heading("type", text="户型")
        self.tree.heading("date", text="登记日期")
        self.tree.heading("note", text="备注")
        self.tree.heading("married", text="婚姻状态")
        self.tree.heading("in_love", text="恋爱状态")
        self.tree.heading("is_virgin", text="处女状态")
        self.tree.heading("has_child", text="育子状态")

    def search(self):
        # 清空当前表格
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # 获取查询条件
        query_params = {}
        
        # 处理查询参数
        name = self.name_entry.get()
        if name:
            query_params['name'] = name
            
        age = self.age_entry.get()
        if age:
            try:
                query_params['age'] = int(age)
            except ValueError:
                pass
                
        bust = self.bust_entry.get()
        if bust:
            query_params['bust'] = bust
            
        type_ = self.type_entry.get()
        if type_:
            query_params['type'] = type_
            
        # 处理日期范围
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()
        if start_date and end_date:
            query_params['start_date'] = start_date
            query_params['end_date'] = end_date
            
        # 处理状态查询
        if self.marriage_var.get():
            query_params['married'] = self.marriage_var.get()
        if self.relationship_var.get():
            query_params['in_love'] = self.relationship_var.get()
        if self.virgin_var.get():
            query_params['is_virgin'] = self.virgin_var.get()
        if self.child_var.get():
            query_params['has_child'] = self.child_var.get()
            
        # 查询数据
        results = self.data_handler.query_partners(query_params, self.current_page, self.page_size)
        
        # 显示结果
        for partner in results:
            self.tree.insert('', 'end', values=(
                partner.get('name', ''),
                partner.get('age', ''),
                partner.get('bust', ''),
                partner.get('type', ''),
                partner.get('date', ''),
                partner.get('note', ''),
                partner.get('married', ''),
                partner.get('in_love', ''),
                partner.get('is_virgin', ''),
                partner.get('has_child', '')
            ))

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
        
        # 版本信息和GitHub链接
        info_frame = ttk.Frame(self)
        info_frame.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        
        ttk.Label(info_frame, text=f"版本号: {config['version']}").grid(row=0, column=0, padx=15)
        ttk.Label(info_frame, text=f"作者: {config['author']}").grid(row=0, column=1, padx=15)
        
        ttk.Label(info_frame, text="GitHub: ").grid(row=0, column=2, padx=5)
        github_link = ttk.Label(info_frame, text=config['github_url'], foreground="blue")
        github_link.grid(row=0, column=3, padx=5)
        github_link.bind("<Button-1>", lambda e: self.open_github())
        


    def open_github(self):
        import webbrowser
        import json
        with open('config.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
        webbrowser.open(config['github_url'])


class QueryFrame(ttk.Frame):
    def __init__(self, parent, data_handler):
        super().__init__(parent)
        self.data_handler = data_handler
        self.current_page = 1
        self.page_size = 10
        self.create_widgets()

    def create_widgets(self):
        # 查询条件区域
        query_frame = ttk.Frame(self)
        query_frame.pack(fill="x", padx=5, pady=5)
        
        # 第一行：基本信息查询
        ttk.Label(query_frame, text="姓名：").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = ttk.Entry(query_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(query_frame, text="年龄：").grid(row=0, column=2, padx=5, pady=5)
        self.age_entry = ttk.Entry(query_frame)
        self.age_entry.grid(row=0, column=3, padx=5, pady=5)
        
        ttk.Label(query_frame, text="胸围：").grid(row=0, column=4, padx=5, pady=5)
        self.bust_entry = ttk.Entry(query_frame)
        self.bust_entry.grid(row=0, column=5, padx=5, pady=5)
        
        ttk.Label(query_frame, text="户型：").grid(row=0, column=6, padx=5, pady=5)
        self.type_entry = ttk.Entry(query_frame)
        self.type_entry.grid(row=0, column=7, padx=5, pady=5)
        
        # 第二行：日期范围
        ttk.Label(query_frame, text="登记日期从：").grid(row=1, column=0, padx=5, pady=5)
        from tkcalendar import DateEntry
        self.start_date_entry = DateEntry(query_frame, date_pattern='y-mm-dd')
        self.start_date_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(query_frame, text="到：").grid(row=1, column=2, padx=5, pady=5)
        self.end_date_entry = DateEntry(query_frame, date_pattern='y-mm-dd')
        self.end_date_entry.grid(row=1, column=3, padx=5, pady=5)
        
        # 第三行：状态选择
        ttk.Label(query_frame, text="婚姻状态：").grid(row=2, column=0, padx=5, pady=5)
        self.marriage_var = tk.StringVar()
        ttk.Combobox(query_frame, textvariable=self.marriage_var, values=["未婚","已婚","离异"]).grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(query_frame, text="恋爱状态：").grid(row=2, column=2, padx=5, pady=5)
        self.relationship_var = tk.StringVar()
        ttk.Combobox(query_frame, textvariable=self.relationship_var, values=["单身","恋爱中","暧昧"]).grid(row=2, column=3, padx=5, pady=5)
        
        ttk.Label(query_frame, text="处女状态：").grid(row=2, column=4, padx=5, pady=5)
        self.virgin_var = tk.StringVar()
        ttk.Combobox(query_frame, textvariable=self.virgin_var, values=["是","否"]).grid(row=2, column=5, padx=5, pady=5)
        
        ttk.Label(query_frame, text="育子状态：").grid(row=2, column=6, padx=5, pady=5)
        self.child_var = tk.StringVar()
        ttk.Combobox(query_frame, textvariable=self.child_var, values=["有","无"]).grid(row=2, column=7, padx=5, pady=5)
        
        # 查询按钮
        ttk.Button(query_frame, text="查询", command=self.search).grid(row=1, column=4, columnspan=2, pady=5)
        
        # 结果显示区域
        result_frame = ttk.Frame(self)
        result_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        # 结果显示表格
        self.tree = ttk.Treeview(result_frame, columns=("name", "age", "bust", "type", "date", "note", "married", "in_love", "is_virgin", "has_child"), show="headings")
        self.tree.pack(fill="both", expand=True)
        
        self.tree.heading("name", text="姓名")
        self.tree.heading("age", text="年龄")
        self.tree.heading("bust", text="胸围")
        self.tree.heading("type", text="户型")
        self.tree.heading("date", text="登记日期")
        self.tree.heading("note", text="备注")
        self.tree.heading("married", text="婚姻状态")
        self.tree.heading("in_love", text="恋爱状态")
        self.tree.heading("is_virgin", text="处女状态")
        self.tree.heading("has_child", text="育子状态")

    def search(self):
        # 清空当前表格
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # 获取查询条件
        query_params = {}
        
        # 处理查询参数
        name = self.name_entry.get()
        if name:
            query_params['name'] = name
            
        age = self.age_entry.get()
        if age:
            try:
                query_params['age'] = int(age)
            except ValueError:
                pass
                
        bust = self.bust_entry.get()
        if bust:
            query_params['bust'] = bust
            
        type_ = self.type_entry.get()
        if type_:
            query_params['type'] = type_
            
        # 处理日期范围
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()
        if start_date and end_date:
            query_params['start_date'] = start_date
            query_params['end_date'] = end_date
            
        # 处理状态查询
        if self.marriage_var.get():
            query_params['married'] = self.marriage_var.get()
        if self.relationship_var.get():
            query_params['in_love'] = self.relationship_var.get()
        if self.virgin_var.get():
            query_params['is_virgin'] = self.virgin_var.get()
        if self.child_var.get():
            query_params['has_child'] = self.child_var.get()
            
        # 查询数据
        results = self.data_handler.query_partners(query_params, self.current_page, self.page_size)
        
        # 显示结果
        for partner in results:
            self.tree.insert('', 'end', values=(
                partner.get('name', ''),
                partner.get('age', ''),
                partner.get('bust', ''),
                partner.get('type', ''),
                partner.get('date', ''),
                partner.get('note', ''),
                partner.get('married', ''),
                partner.get('in_love', ''),
                partner.get('is_virgin', ''),
                partner.get('has_child', '')
            ))

class StatsFrame(ttk.Frame):
    def __init__(self, parent, data_handler):
        super().__init__(parent)
        self.data_handler = data_handler
        self.create_widgets()

    def create_widgets(self):
        # 创建图表选择区域
        chart_frame = ttk.Frame(self)
        chart_frame.pack(fill="x", padx=5, pady=5)
        
        ttk.Label(chart_frame, text="选择图表类型:").pack(side="left", padx=5)
        
        self.chart_var = tk.StringVar(value="bar")
        ttk.Radiobutton(chart_frame, text="柱状图", variable=self.chart_var, value="bar").pack(side="left", padx=5)
        ttk.Radiobutton(chart_frame, text="饼图", variable=self.chart_var, value="pie").pack(side="left", padx=5)
        
        # 创建统计按钮
        ttk.Button(chart_frame, text="生成统计", command=self.generate_stats).pack(side="left", padx=5)
        
        # 创建图表显示区域
        self.figure = None
        self.canvas = None
        
    def generate_stats(self):
        # 获取所有伴侣数据
        partners = self.data_handler.get_all_partners()
        
        if not partners:
            return
            
        # 根据选择生成不同类型的图表
        chart_type = self.chart_var.get()
        
        if chart_type == "bar":
            self.generate_bar_chart(partners)
        elif chart_type == "pie":
            self.generate_pie_chart(partners)
            
    def generate_bar_chart(self, partners):
        # 清除之前的图表
        if self.canvas:
            self.canvas.get_tk_widget().destroy()
            
        # 创建柱状图
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
        
        names = [p['name'] for p in partners]
        ages = [p['age'] for p in partners]
        
        self.figure = plt.figure(figsize=(8, 4))
        ax = self.figure.add_subplot(111)
        ax.bar(names, ages)
        ax.set_title('年龄分布')
        ax.set_xlabel('姓名')
        ax.set_ylabel('年龄')
        
        # 在Tkinter中显示图表
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill="both", expand=True)
        
    def generate_pie_chart(self, partners):
        # 清除之前的图表
        if self.canvas:
            self.canvas.get_tk_widget().destroy()
            
        # 创建饼图
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
        
        # 统计婚姻状态
        marriage_counts = {
            '未婚': 0,
            '已婚': 0,
            '离异': 0
        }
        
        for p in partners:
            status = p.get('married', '未婚')
            marriage_counts[status] += 1
            
        labels = list(marriage_counts.keys())
        sizes = list(marriage_counts.values())
        
        self.figure = plt.figure(figsize=(8, 4))
        ax = self.figure.add_subplot(111)
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.set_title('婚姻状态分布')
        
        # 在Tkinter中显示图表
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill="both", expand=True)




    def create_widgets(self):
        # 查询条件区域
        query_frame = ttk.Frame(self)
        query_frame.pack(fill="x", padx=5, pady=5)
        
        # 第一行：基本信息查询
        ttk.Label(query_frame, text="姓名：").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = ttk.Entry(query_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(query_frame, text="年龄：").grid(row=0, column=2, padx=5, pady=5)
        self.age_entry = ttk.Entry(query_frame)
        self.age_entry.grid(row=0, column=3, padx=5, pady=5)
        
        ttk.Label(query_frame, text="胸围：").grid(row=0, column=4, padx=5, pady=5)
        self.bust_entry = ttk.Entry(query_frame)
        self.bust_entry.grid(row=0, column=5, padx=5, pady=5)
        
        ttk.Label(query_frame, text="户型：").grid(row=0, column=6, padx=5, pady=5)
        self.type_entry = ttk.Entry(query_frame)
        self.type_entry.grid(row=0, column=7, padx=5, pady=5)
        
        # 第二行：日期范围
        ttk.Label(query_frame, text="登记日期从：").grid(row=1, column=0, padx=5, pady=5)
        from tkcalendar import DateEntry
        self.start_date_entry = DateEntry(query_frame, date_pattern='y-mm-dd')
        self.start_date_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(query_frame, text="到：").grid(row=1, column=2, padx=5, pady=5)
        self.end_date_entry = DateEntry(query_frame, date_pattern='y-mm-dd')
        self.end_date_entry.grid(row=1, column=3, padx=5, pady=5)
        
        # 第三行：状态选择
        ttk.Label(query_frame, text="婚姻状态：").grid(row=2, column=0, padx=5, pady=5)
        self.married_var = tk.StringVar(value="全部")
        ttk.Combobox(query_frame, textvariable=self.married_var, values=["全部", "已婚", "未婚"]).grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(query_frame, text="恋爱状态：").grid(row=2, column=2, padx=5, pady=5)
        self.love_var = tk.StringVar(value="全部")
        ttk.Combobox(query_frame, textvariable=self.love_var, values=["全部", "恋爱中", "单身"]).grid(row=2, column=3, padx=5, pady=5)
        
        ttk.Label(query_frame, text="处女状态：").grid(row=2, column=4, padx=5, pady=5)
        self.virgin_var = tk.StringVar(value="全部")
        ttk.Combobox(query_frame, textvariable=self.virgin_var, values=["全部", "是", "否"]).grid(row=2, column=5, padx=5, pady=5)
        
        ttk.Label(query_frame, text="育子状态：").grid(row=2, column=6, padx=5, pady=5)
        self.child_var = tk.StringVar(value="全部")
        ttk.Combobox(query_frame, textvariable=self.child_var, values=["全部", "是", "否"]).grid(row=2, column=7, padx=5, pady=5)
        
        # 查询按钮
        ttk.Button(query_frame, text="查询", command=self.search).grid(row=3, column=0, pady=10)
        ttk.Button(query_frame, text="重置", command=self.reset).grid(row=3, column=1, pady=10)
        ttk.Button(query_frame, text="删除", command=self.delete_selected).grid(row=3, column=2, pady=10)
        
        # 结果显示区域
        result_frame = ttk.Frame(self)
        result_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        # 分页控制
        page_frame = ttk.Frame(result_frame)
        page_frame.pack(side="bottom", fill="x", pady=5)
        
        ttk.Button(page_frame, text="上一页", command=self.prev_page).pack(side="left", padx=5)
        ttk.Button(page_frame, text="下一页", command=self.next_page).pack(side="left", padx=5)
        
        # 结果显示表格
        self.tree = ttk.Treeview(result_frame, columns=("name", "age", "bust", "type", "date", "note", "married", "in_love", "is_virgin", "has_child"), show="headings")
        self.tree.pack(fill="both", expand=True)
        
        self.tree.heading("name", text="姓名")
        self.tree.heading("age", text="年龄")
        self.tree.heading("bust", text="胸围")
        self.tree.heading("type", text="户型")
        self.tree.heading("date", text="登记日期")
        self.tree.heading("note", text="备注")
        self.tree.heading("married", text="婚姻状态")
        self.tree.heading("in_love", text="恋爱状态")
        self.tree.heading("is_virgin", text="处女状态")
        self.tree.heading("has_child", text="育子状态")
        

    
    def search(self):
        # 检查所有查询条件是否为空或为'全部'
        all_empty = True
        query_params = {
            "name": self.name_entry.get(),
            "age": self.age_entry.get(),
            "bust": self.bust_entry.get(),
            "type": self.type_entry.get(),
            "start_date": self.start_date_entry.get(),
            "end_date": self.end_date_entry.get(),
            "married": self.married_var.get(),
            "in_love": self.love_var.get(),
            "is_virgin": self.virgin_var.get(),
            "has_child": self.child_var.get()
        }
        
        for value in query_params.values():
            if value and value != "全部":
                all_empty = False
                break
                
        if all_empty:
            # 如果所有条件都为空或为'全部'，则获取所有数据
            results = self.data_handler.get_all_partners()
        else:
            # 否则执行正常查询
            # 过滤掉空值和'全部'的查询条件
            filtered_params = {k: v for k, v in query_params.items() if v and v != "全部"}
            results = self.data_handler.query_partners(filtered_params, self.current_page, self.page_size)
            
        if not results:
            tk.messagebox.showinfo("提示", "查询结果为空")
        else:
            self.display_results(results)
    
    def auto_resize_columns(self):
        for col in self.tree["columns"]:
            self.tree.column(col, width=100, minwidth=50, stretch=True)
        # 自动调整列宽以适应内容
        for col in self.tree["columns"]:
            self.tree.column(col, width=tk.font.Font().measure(col.title()))
            for item in self.tree.get_children():
                cell_value = self.tree.set(item, col)
                if cell_value:
                    self.tree.column(col, width=max(
                        self.tree.column(col, "width"),
                        tk.font.Font().measure(cell_value)
                    ))
            
    def display_results(self, results):
        # 清空当前显示
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # 添加新结果
        for partner in results:
            self.tree.insert("", "end", values=(
                partner["name"],
                partner["age"],
                partner["bust"],
                partner["type"],
                partner["date"],
                partner.get("note", ""),
                partner.get("married", ""),
                partner.get("in_love", ""),
                partner.get("is_virgin", ""),
                partner.get("has_child", "")
            ))
        
        # 设置列宽自适应
        self.auto_resize_columns()
        # 确保treeview填充父容器
        self.tree.pack(fill='both', expand=True)
        self.tree.bind("<Configure>", lambda e: self.auto_resize_columns())
    
    def prev_page(self):
        if self.current_page > 1:
            self.current_page -= 1
            self.search()
    
    def next_page(self):
        self.current_page += 1
        self.search()
        
    def reset(self):
        """重置所有筛选条件"""
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.bust_entry.delete(0, tk.END)
        self.type_entry.delete(0, tk.END)
        self.start_date_entry.set_date(None)
        self.end_date_entry.set_date(None)
        self.married_var.set("全部")
        self.love_var.set("全部")
        self.virgin_var.set("全部")
        self.child_var.set("全部")
        
    def delete_selected(self):
        """删除选中的记录"""
        selected_item = self.tree.selection()
        if not selected_item:
            tk.messagebox.showwarning("警告", "请先选择要删除的记录")
            return
            
        item = self.tree.item(selected_item)
        partner_name = item['values'][0]
        
        if tk.messagebox.askyesno("确认", f"确定要删除 {partner_name} 的记录吗？"):
            self.data_handler.delete_partner(partner_name)
            self.search()
            tk.messagebox.showinfo("提示", "删除成功")

class SexRecordFrame(ttk.Frame):
    def __init__(self, parent, data_handler, partner_id):
        super().__init__(parent)
        self.data_handler = data_handler
        self.partner_id = partner_id
        self.create_widgets()
        self.main_app = parent.master if isinstance(parent.master, tk.Tk) else parent.master.master

    def create_widgets(self):
        # 获取伴侣信息
        partner = self.data_handler.get_partner(self.partner_id)
        
        # 显示伴侣基本信息
        info_frame = ttk.Frame(self)
        info_frame.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
        
        ttk.Label(info_frame, text=f"姓名: {partner['name']}").grid(row=0, column=0, sticky="w")
        ttk.Label(info_frame, text=f"年龄: {partner['age']}").grid(row=0, column=1, sticky="w")
        ttk.Label(info_frame, text=f"胸围: {partner['bust']}").grid(row=1, column=0, sticky="w")
        ttk.Label(info_frame, text=f"户型: {partner['type']}").grid(row=1, column=1, sticky="w")
        
        # 性爱记录输入区域
        record_frame = ttk.Frame(self)
        record_frame.grid(row=1, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
        
        # 性爱地点输入框
        ttk.Label(record_frame, text="性爱地点：").grid(row=0, column=0, sticky="w")
        self.location_entry = ttk.Entry(record_frame)
        self.location_entry.grid(row=0, column=1, sticky="ew")
        
        # 性爱日期选择框
        ttk.Label(record_frame, text="性爱日期：").grid(row=1, column=0, sticky="w")
        from tkcalendar import DateEntry
        self.date_entry = DateEntry(record_frame, date_pattern='y-mm-dd')
        self.date_entry.grid(row=1, column=1, sticky="ew")
        
        # 是否高潮选择框
        ttk.Label(record_frame, text="是否高潮：").grid(row=2, column=0, sticky="w")
        self.orgasm_var = tk.StringVar()
        self.orgasm_combobox = ttk.Combobox(record_frame, textvariable=self.orgasm_var, values=["是", "否"])
        self.orgasm_combobox.grid(row=2, column=1, sticky="ew")
        
        # 防护措施选择框
        ttk.Label(record_frame, text="防护措施：").grid(row=3, column=0, sticky="w")
        self.protection_var = tk.StringVar()
        self.protection_combobox = ttk.Combobox(record_frame, textvariable=self.protection_var, values=["无防护措施", "避孕套", "药物", "其他"])
        self.protection_combobox.grid(row=3, column=1, sticky="ew")
        
        # 历史记录显示区域
        history_frame = ttk.Frame(self)
        history_frame.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
        
        # 历史记录表格
        self.history_tree = ttk.Treeview(history_frame, columns=("date", "location", "orgasm", "protection"), show="headings")
        self.history_tree.pack(fill="both", expand=True)
        
        self.history_tree.heading("date", text="日期")
        self.history_tree.heading("location", text="地点")
        self.history_tree.heading("orgasm", text="是否高潮")
        self.history_tree.heading("protection", text="防护措施")
        
        # 加载历史记录
        self.load_history()
        
        # 按钮区域
        button_frame = ttk.Frame(self)
        button_frame.grid(row=3, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
        
        ttk.Button(button_frame, text="添加记录", command=self.save_record).grid(row=0, column=0, padx=5)
        ttk.Button(button_frame, text="返回", command=lambda: self.main_app.show_add()).grid(row=0, column=1, padx=5)

    def load_history(self):
        """加载历史记录数据"""
        records = self.data_handler.get_records(self.partner_id)
        
        # 清空当前表格
        for item in self.history_tree.get_children():
            self.history_tree.delete(item)
        
        # 添加历史记录
        for record in records:
            self.history_tree.insert("", "end", values=(
                record.get('date', ''),
                record.get('location', ''),
                record.get('orgasm', ''),
                record.get('protection', '')
            ))
    
    def save_record(self):
        """保存新记录"""
        record_data = {
            'location': self.location_entry.get(),
            'date': self.date_entry.get(),
            'orgasm': self.orgasm_var.get(),
            'protection': self.protection_var.get()
        }
        
        # 验证必填字段
        if not record_data['location'] or not record_data['date']:
            messagebox.showerror("错误", "地点和日期是必填项")
            return
            
        self.data_handler.add_record(self.partner_id, record_data)
        messagebox.showinfo("成功", "记录已保存")
        
        # 清空输入框
        self.location_entry.delete(0, tk.END)
        self.date_entry.set_date(None)
        self.orgasm_var.set("")
        self.protection_var.set("")
        
        # 刷新历史记录
        self.load_history()
        
        # 返回主界面
        self.main_app.show_add()