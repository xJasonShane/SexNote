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
            
        # 应用查询条件
        if query_params.get('name'):
            filtered = [p for p in filtered if query_params['name'].lower() in p.get('name', '').lower()]
        if query_params.get('age'):
            try:
                age = int(query_params['age'])
                filtered = [p for p in filtered if p.get('age') == age]
            except ValueError:
                pass
        if query_params.get('bust'):
            filtered = [p for p in filtered if query_params['bust'].lower() in p.get('bust', '').lower()]
        if query_params.get('type'):
            filtered = [p for p in filtered if query_params['type'].lower() in p.get('type', '').lower()]
        if query_params.get('note'):
            filtered = [p for p in filtered if query_params['note'].lower() in p.get('note', '').lower()]
        if query_params.get('start_date') and query_params.get('end_date'):
            filtered = [p for p in filtered if query_params['start_date'] <= p.get('date', '') <= query_params['end_date']]
        if query_params.get('married') and query_params['married'] != "全部":
            filtered = [p for p in filtered if p.get('married') == query_params['married']]
        if query_params.get('in_love') and query_params['in_love'] != "全部":
            filtered = [p for p in filtered if p.get('in_love') == query_params['in_love']]
        if query_params.get('is_virgin') and query_params['is_virgin'] != "全部":
            filtered = [p for p in filtered if p.get('is_virgin') == query_params['is_virgin']]
        if query_params.get('has_child') and query_params['has_child'] != "全部":
            filtered = [p for p in filtered if p.get('has_child') == query_params['has_child']]
            
        # 计算分页
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
        
        # 应用查询条件
        if query_params.get('name'):
            filtered = [p for p in filtered if query_params['name'].lower() in p.get('name', '').lower()]
        if query_params.get('age'):
            try:
                age = int(query_params['age'])
                filtered = [p for p in filtered if p.get('age') == age]
            except ValueError:
                pass
        if query_params.get('bust'):
            filtered = [p for p in filtered if query_params['bust'].lower() in p.get('bust', '').lower()]
        if query_params.get('type'):
            filtered = [p for p in filtered if query_params['type'].lower() in p.get('type', '').lower()]
        if query_params.get('note'):
            filtered = [p for p in filtered if query_params['note'].lower() in p.get('note', '').lower()]
        if query_params.get('start_date') and query_params.get('end_date'):
            filtered = [p for p in filtered if query_params['start_date'] <= p.get('date', '') <= query_params['end_date']]
        if query_params.get('married') and query_params['married'] != "全部":
            filtered = [p for p in filtered if p.get('married') == query_params['married']]
        if query_params.get('in_love') and query_params['in_love'] != "全部":
            filtered = [p for p in filtered if p.get('in_love') == query_params['in_love']]
        if query_params.get('is_virgin') and query_params['is_virgin'] != "全部":
            filtered = [p for p in filtered if p.get('is_virgin') == query_params['is_virgin']]
        if query_params.get('has_child') and query_params['has_child'] != "全部":
            filtered = [p for p in filtered if p.get('has_child') == query_params['has_child']]
            
        # 计算分页
        start = (page - 1) * page_size
        end = start + page_size
        return filtered[start:end]