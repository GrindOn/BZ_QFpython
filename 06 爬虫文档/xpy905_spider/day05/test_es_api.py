"""
使用单元测试，测试ES搜索引擎的RESTful接口
- requests
- unittest
"""

from unittest import TestCase, TestSuite, TextTestRunner

data = {

}


class TestIndex(TestCase):
    def setUp(self):
        print('--测试前的资源准备工作---')

    def test_a_add_index(self):
        print('--添加索引--')
        data['index_name'] = 'person_sos'

    def test_b_query_index(self):
        print('--查询索引--')

    def test_c_delete_index(self):
        print('--删除索引--')

    def tearDown(self):
        print('--测试后的资源回收工作---')


class TestDoc(TestCase):
    def test_a2_add_doc(self):
        print(f'-{data["index_name"]}-增加doc文档--')

    def test_a3_query_doc(self):
        print(f'-{data["index_name"]}-查询doc文档--')


if __name__ == '__main__':
    # 必须以普通的Python脚本运行

    suite = TestSuite()
    suite.addTest(TestIndex.test_a_add_index)
    suite.addTest(TestDoc.test_a2_add_doc)
    suite.addTest(TestDoc.test_a3_query_doc)

    TextTestRunner().run(suite)
