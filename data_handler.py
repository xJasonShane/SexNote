import json
import os
from datetime import datetime

class DataHandler:
    def __init__(self):
        self.data_file = 'data.json'
        self.data = {
            'metadata': {
                'version': self.get_config_version(),
                'created_at': datetime.now().isoformat(),
                'last_updated': None
            },
            'partners': [],
            'records': [],
            'settings': {
                'author': '开发者名称',
                'github': 'https://github.com/username/SexNote'
            }
        }
        self.load_data()
        
    def get_config_version(self):
        try:
            with open('config.json', 'r', encoding='utf-8') as f:
                config = json.load(f)
                return config.get('version', '1.1.0')
        except (FileNotFoundError, json.JSONDecodeError):
            return '1.1.0'

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r', encoding='utf-8') as f:
                self.data = json.load(f)

    def save_data(self):
        self.data['metadata']['last_updated'] = datetime.now().isoformat()
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
        
    def get_partner(self, partner_id):
        """
        根据ID获取partner信息
        :param partner_id: 要查找的partner ID
        :return: 匹配的partner字典或None
        """
        for partner in self.data['partners']:
            if partner.get('id') == partner_id:
                return partner
        return None
        
    def get_all_partners(self):
        """
        获取所有partner信息
        :return: partners列表
        """
        return self.data['partners']
        
    def query_partners(self, query_params, page=1, page_size=10):
        """
        根据查询参数筛选伙伴数据并返回分页结果
        :param query_params: 查询参数字典，支持name、age、bust、type、note和日期范围条件
        :param page: 当前页码
        :param page_size: 每页数量
        :return: 分页后的结果列表
        """
        filtered = self.data['partners']
        
        # 如果没有查询条件，返回所有数据
        if not query_params:
            start = (page - 1) * page_size
            end = start + page_size
            return filtered[start:end]
            

        
    def delete_partner(self, partner_name):
        """
        根据伴侣名称删除记录
        :param partner_name: 要删除的伴侣名称
        """
        self.data['partners'] = [p for p in self.data['partners'] if p.get('name') != partner_name]
        # 同时删除相关记录
        self.data['records'] = [r for r in self.data['records'] if r.get('partner_name') != partner_name]
        self.save_data()
        
    def get_records(self, partner_id):
        """
        根据partner_id获取相关记录
        :param partner_id: 要查询的partner ID
        :return: 匹配的记录列表
        """
        return [r for r in self.data['records'] if r.get('partner_id') == partner_id]