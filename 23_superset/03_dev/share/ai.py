import vanna
from vanna.remote import VannaDefault
api_key = "1ee4491892614379bae807977289bda9"

vanna_model_name = "icbc"
vn = VannaDefault(model=vanna_model_name, api_key=api_key)
vn.connect_to_mysql(host='192.168.140.101', dbname='phoenix', user='root', password='Qp9tb869zXu4kh7Gm9R', port=8306)