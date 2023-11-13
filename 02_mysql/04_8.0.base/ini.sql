/* 以下允许 root 外网登陆 */
DELETE FROM mysql.user ;
CREATE USER 'root'@'%' IDENTIFIED BY 'Qp9tb869zXu4kh7Gm9R' ;
GRANT ALL ON *.* TO 'root'@'%' WITH GRANT OPTION ;
FLUSH PRIVILEGES ;