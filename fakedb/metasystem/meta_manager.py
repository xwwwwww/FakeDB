from ..config import ROOT_DIR, META_SUFFIX
import pickle
import os
from .meta import DbMeta

class MetaManager:
    def __init__(self, fm):
        self.fm = fm
        self.db_dict = {}
        self.current_db = None # current DbMeta

    # def writeback_db(self, name):
    #     if name not in self.db_dict:
    #         raise Exception(f'database {name} does not exist!')
    #     path = f'{ROOT_DIR}/{name}/{name}{META_SUFFIX}'
    #     with open(path, 'wb') as f:
    #         pickle.dump(self.db_dict[name], f)

    def shutdown(self):
        self.writeback_alldbs()

    def get_indexes_description(self):
        assert self.current_db is not None
        return self.current_db.get_indexes_description()

    def get_databases_description(self):
        return ' '.join([name for name in self.db_dict])

    def writeback_alldbs(self):
        # for name in self.db_dict:
        #     self.writeback_db(name)
        path = f'{ROOT_DIR}/alldbs{META_SUFFIX}'
        with open(path, 'wb') as f:
            pickle.dump(self.db_dict, f)

    def load_alldbs(self):
        path = f'{ROOT_DIR}/alldbs{META_SUFFIX}'
        if os.path.exists(path):
            with open(path, 'rb') as f:
                self.db_dict = pickle.load(f)

    def create_db(self, name):
        if name in self.db_dict:
            raise Exception(f'database {name} exists!')
        self.db_dict[name] = DbMeta(name, [])

    def drop_db(self, name):
        if name not in self.db_dict:
            raise Exception(f'database {name} does not exist!')

        self.db_dict.pop(name)

    def use_db(self, name):
        if name not in self.db_dict:
            raise Exception(f'database {name} does not exist!')
        self.current_db = self.db_dict[name]

    def create_table(self, tablemeta):
        self.current_db.create_table(tablemeta)

    def drop_table(self, name):
        self.current_db.drop_table(name)

    def get_table(self, name):
        return self.current_db.get_table(name)
