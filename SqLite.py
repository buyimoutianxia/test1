import sqlite3;

conn = sqlite3.connect('test.db');
c = conn.cursor();

c.execute('create table user(id char(20), name varchar(20))');

c.execute("insert into user(id,name) values('10','xyz')");

c.close();

conn.commit();

conn.close();