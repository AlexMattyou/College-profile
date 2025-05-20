install link: https://archive.apache.org/dist/hbase/1.4.9/

setup HBASE_HOME 

create 2 folders: Zookeeper, Hfiles

hbase-site.xml:
```
<property>
    <name>hbase.rootdir</name>
    <value>C:\Hfile</value>
</property>
<property>
    <name>hbase.zookeeper.property.dataDir</name>
    <value>C:\zookeeper</value>
</property>
    <property>
    <name>hbase.cluster.distributed</name>
<value>false</value>
</property>
<property>
    <name>hbase.rootdir</name>
    <value>hdfs://localhost:9820/hbase</value>
</property>
```
