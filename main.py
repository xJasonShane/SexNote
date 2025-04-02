import tkinter as tk
from tkinter import ttk
from data_handler import DataHandler
from gui_components import AddPartnerFrame, SexRecordFrame, QueryFrame, StatsFrame

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SexNote")
        
        # 获取屏幕尺寸并计算窗口大小和位置
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = int(screen_width * 0.6)
        window_height = int(screen_height * 0.6)
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        self.data_handler = DataHandler()
        
        # 创建导航栏
        self.nav_frame = ttk.Frame(self)
        self.nav_frame.pack(side="top", fill="x")
        
        self.tabs = {
            "add": ttk.Button(self.nav_frame, text="添加记录", command=self.show_add),
            "query": ttk.Button(self.nav_frame, text="查询记录", command=self.show_query),
            "stats": ttk.Button(self.nav_frame, text="数据统计", command=self.show_stats),
            "settings": ttk.Button(self.nav_frame, text="软件设置", command=self.show_settings)
        }
        
        for btn in self.tabs.values():
            btn.pack(side="left", padx=5)
        
        # 主内容区域
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill="both", expand=True)
        
        # 默认显示添加记录界面
        self.show_add()

    def show_add(self):
        # 清空当前界面组件
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        # 创建新界面并指定父容器为main_frame
        AddPartnerFrame(self.main_frame, self.data_handler).pack(fill='both', expand=True)

    def show_query(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        QueryFrame(self.main_frame, self.data_handler).pack(fill='both', expand=True)

    def show_stats(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        StatsFrame(self.main_frame, self.data_handler).pack(fill='both', expand=True)

    def show_settings(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        from gui_components import SettingsFrame
        SettingsFrame(self.main_frame).pack(fill='both', expand=True)

    def show_sex_record(self, partner_id):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        SexRecordFrame(self.main_frame, self.data_handler, partner_id).pack(fill='both', expand=True)
        
if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()