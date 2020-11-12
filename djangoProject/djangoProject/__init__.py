import pymysql

pymysql.version_info = (1, 4, 13, "final", 0)
pymysql.install_as_MySQLdb() # 使用pymysql 代替mysqldb連接數據庫
