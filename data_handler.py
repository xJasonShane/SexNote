import json
import os
from datetime import datetime

class DataHandler:
    def __init__(self):
        self.data_file = 'data.json'
        self.data = {
            'partners': [],
            'records': [],
            'settings': {
                'version': '1.0.0',
                'author': '开发者名称',
                'github': 'https://github.com/username/SexNote'
            }
        }
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r', encoding='utf-8') as f:
                self.data = json.load(f)

    def save_data(self):
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)

    def add_partner(self, partner_data):
        # 数据验证示例
        if not isinstance(partner_data.get('age'), int):
            raise ValueError("年龄必须为整数")
        
        partner_data['id'] = len(self.data['partners']) + 1
        self.data['partners'].append(partner_data)
        self.save_data()
        return partner_data['id']

    def add_record(self, partner_id, record_data):
        record_data['partner_id'] = partner_id
        record_data['date'] = datetime.now().isoformat()
        self.data['records'].append(record_data)
        self.save_data()

    def get_settings(self):
        return self.data['settings']