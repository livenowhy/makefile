import matplotlib.pyplot as plt
import numpy as np
import time
import pymysql as pmq



def fetch_img_name():
    imgid = int(time.time())
    imgid_path = '/usr/local/lib/python3.10/site-packages/superset/static/assets/images/matplotlib'
    img_name = '{imgid_path}/{imgid}.png'.format(imgid_path=imgid_path, imgid=imgid)
    return img_name, imgid

class MysqlTools(object):
    def __init__(self, host, port, user, password, database) -> None:
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.connection = self.connect_to_database()
        self.cursor = self.connection.cursor()

    def connect_to_database(self):
        try:
            connection = pmq.connect(
                host=self.host,
                user=self.user,
                port=self.port,
                password=self.password,
                db=self.database
            )
            return connection
        except Exception as e:
            print("连接失败：", e)
            return None

    def insert_data(self, width, height, imgid, atype):
        """
        插入数据
        """
        sql = "INSERT INTO superse_image (width, height, imgid, atype) VALUES (%(width)s, %(height)s, %(imgid)s, %(atype)s)"
        imginfo = {
                'width': width, 'height': height, 'imgid': imgid, 'atype': atype
            }
        
        try:
            self.cursor.execute(sql, imginfo)
            self.connection.commit()
            print("数据插入成功")
        except Exception as e:
            print("数据插入失败：", e)

class MatplotlibBase(object):
    def __init__(self) -> None:
        pass

    def regression_demo(self):
        """
        线性回归
        """
        img_name, imgid = fetch_img_name()

        # 假设x和y是你的数据点
        x = np.array([1, 2, 3, 4, 5])
        y = np.array([2, 3, 5, 7, 9])
        
        # 计算线性回归的斜率和截距
        slope, intercept = np.polyfit(x, y, 1)
        
        # 计算拟合线的y值
        line_y = slope * x + intercept
        
        # 绘制数据点
        plt.scatter(x, y)
        
        # 绘制线性回归线
        plt.plot(x, line_y, color='red')
        
        # 设置图表的标题和轴标签
        plt.title('Linear Regression')
        plt.xlabel('X')
        plt.ylabel('Y')
        
        # 显示图表
        # plt.show()
        # 保存图像到文件，这里以png格式为例
        plt.savefig(img_name)
        # 关闭图像窗口（可选）
        plt.close()

        mt = MysqlTools(host='192.168.140.101', port=8306, user='root', password='Qp9tb869zXu4kh7Gm9R', database='phoenix')
        mt.insert_data(height=300, width=300, imgid=imgid, atype='regression')
    

mb = MatplotlibBase()
mb.regression_demo()