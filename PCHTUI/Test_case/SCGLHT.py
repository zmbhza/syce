import os
import time,random
import pytest
from Params import index as i
from Params.index import Comm
r = Comm()
from Params import params as p
class Test_jiou():
    def setup_class(self):
        """登录后台"""
        s = p.get_value('登录')
        r.input_data('xpath',s['账号输入框'],'17611520838')
        r.input_data('xpath',s['密码输入框'],'a123456')
        r.click('xpath',s['登录按钮点击'])
        s = p.get_value('商品品牌')                                     #'阿萨德 '+' '+o+' '+y
        r.click('xpath',s['点击商品管理目录'])
        r.click('xpath',s['点击商品管理按钮'])
    def test_SCGL(self):
        print('开始')
    def test_SPGL_SPGL_01(self):
        """新增商品"""
        o = p.rdm(4)
        global y
        y = p.rdm(6)
        global s
        s = p.get_value('商品品牌')
        r.click('xpath',s['点击新增商品'])
        p.list(s['点击一级分类'],s['选择一级分类'],'日用百货')
        p.list(s['点击二级分类'],s['选择二级分类'],'家居日用')
        p.list(s['点击三级分类'],s['选择三级分类'],'护发素')
        r.input_data('xpath',s['品牌输入'],'as')
        i.mouse_click('品牌')
        r.input_data('xpath',s['型号'],o)
        r.input_data('xpath',s['商品名称'],'测试'+y)
        r.input_data('xpath',s['包装规格1'],p.rdm(2))
        p.list(s['包装规格2点击'],s['包装规格2选择'],'个')
        p.list(s['包装规则3点击'],s['包装规格3选择'],'个')
        r.click('xpath',s['上传图片'])
        p.win_click(r'C:\Users\zhao\Desktop','Png.jpg')
        time.sleep(0.5)
        p.focus(s['下一步'])
        r.click('xpath',s['下一步'])
        r.click('xpath',s['扩展属性下一步'])
        p.list(s['点击库存销售单位'],s['选择库存销售单位'],'个')
        r.input_data('xpath',s['最小起订量'],p.rdm(2))
        p.list(s['发货省会点击'],s['发货省会选择'],'湖北省')
        p.list(s['发货城市点击'],s['发货城市选择'],'武汉市')
        p.list(s['是否含运费点击'],s['是否含运费选择'],'是')
        p.list(s['是否支持账期支付点击'],s['是否支持账期支付选择'],'是')
        r.input_data('xpath',s['发货时间'],'0')
        r.click('xpath',s['销售属性下一步'])
        r.input_data('xpath',s['促销价'],p.rdm(2))
        r.input_data('xpath', s['零售价'],p.rdm(3))
        r.input_data('xpath',s['批发商价'],p.rdm(2))
        r.click('xpath',s['提交审核'])
        time.sleep(5)
        p.sql('%'+'测试'+y,'测试'+y,'测试','新增商品查询')
        print('新增商品结束')
    # def test_SPGL_SPGL_02(self):
    #     """商品审核"""
    #     pass
    # def test_SPGL_SPGL_03(self):
    #     """商品删除"""
    #     #s = p.get_value('商品品牌')
    #     r.click('xpath',s['未审核删除按钮'])
    #     r.click('xpath',s['确认删除按钮'])
    #     time.sleep(5)
    # def test_SPGL_SPGL_04(self):
    #     """上下架"""
    #     #s = p.get_value('商品品牌')
    #     r.click('xpath', s['点击商品管理目录'])
    #     r.click('xpath', s['点击商品管理按钮'])
    #     r.click('xpath',s['查询按钮'])
    #     i.up_down()
    #     time.sleep(10)
    # def test_SPGL_SPGL_05(self):
    #     """导入批量修改"""
    #     #s = p.get_value('商品品牌')
    #     r.click('xpath', s['点击商品管理目录'])
    #     r.click('xpath', s['点击商品管理按钮'])
    #     r.click('xpath',s['导入批量修改'])
    #     #r.click('xpath',s['选择文件'])
    #     time.sleep(20)
    #     r.click('xapth',s['批量修改上传确定'])
    #     time.sleep(20)
    # def test_SPGL_SPGL_06(self):
    #     """商品导出"""
    #     r.click('xpath',s['导出按钮'])
    #     time.sleep(10)
    # def test_SPGL_SPGL_07(self):
    #     """自定义显示列"""


    def teardown_class(self):
        print('所有case执行结束')
if __name__ == '__main__':
    pytest.main(['-s','-q',r'C:\Users\zhao\PycharmProjects\UIAMS\Test_case\SCGLHT.py','--alluredir','./report','--clean-alluredir'])
    os.system('allure generate report/ -o report/html --clean')
