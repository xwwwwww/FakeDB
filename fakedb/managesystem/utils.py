import os



from ..config import TABLE_SUFFIX, INDEX_SUFFIX
from ..config import ROOT_DIR



def get_db_dir(name):
    '''返回数据库的存储目录(一个文件夹)'''
    return f"{ROOT_DIR}/{name}"


def get_db_tables(name):
    '''返回数据库下的所有表名'''
    db_dir = get_db_dir(name)
    tables = []
    for file in os.listdir(db_dir):
        if file.endswith(TABLE_SUFFIX):
            tables.append(file)
    assert len(set(tables)) == len(tables) # 无重名的表
    return tables
        

def get_table_related_files(db, table):
    '''返回数据库相关的所有文件, 包括.table, .index'''
    output = []
    for suffix in [TABLE_SUFFIX, INDEX_SUFFIX]:
        file = f'{ROOT_DIR}/{db}/{table}{suffix}'
        if os.path.exists(file):
            output.append(file)
    return output