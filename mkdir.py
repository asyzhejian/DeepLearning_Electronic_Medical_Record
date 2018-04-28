#Auther HJ
import os
import shutil
import xlrd
import string

### 创建多层目录
def mkdirs(patient_id,visit_id):
    path='d:/python/test/'+str(patient_id)+'_'+str(visit_id)
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 创建目录操作函数
        os.makedirs(path)
        # 如果不存在则创建目录
        print(path + ' 创建成功')
        return path
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return path
#mkdirs(1000210130,1)