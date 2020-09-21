import xlrd
from xlutils.copy import copy
# #读取文件
# read_file = xlrd.open_workbook('C:\\Users\\zhao\\Desktop\\xiugai.xlsx',formatting_info=True)
# #参数注释：
# #file_path：文件路径，包含文件的全名称
# #formatting_info=True：保留Excel的原格式
#
# #将文件复制到内存
# write_data = copy(read_file)
#
# #读取复制后文件的sheet1
# write_save = write_data.get_sheet(0)
#
# #写入数据
# write_save.write(1,0,'v1alue')
# #参数注释：
# #x,y:写入目标格的位置坐标
# #value：写入数据
#
# #保存写入数据后的文件到原文件路径
# write_data.save('C:\\Users\\zhao\\Desktop\\xiugai.xlsx')
def ede(a,b,c,d):
    # 参数注释：
    # file_path：文件路径，包含文件的全名称
    # formatting_info=True：保留Excel的原格式
    read_file = xlrd.open_workbook(a, formatting_info=True)
    # 将文件复制到内存
    write_data = copy(read_file)
    # 读取复制后文件的sheet1
    write_save = write_data.get_sheet(0)
    # 写入数据
    write_save.write(b, c, d)
    # 保存写入数据后的文件到原文件路径
    write_data.save(a)


