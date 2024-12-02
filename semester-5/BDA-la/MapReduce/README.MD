

To compile Java file: 
`javac -classpath "C:/hadoop-2.8.0/share/hadoop/common/*;C:/hadoop-2.8.0/share/hadoop/mapreduce/*;C:/hadoop-2.8.0/share/hadoop/hdfs/*" -d . <filename>.java`

To convert 3 class into jar file:
`jar -cvf <filename>.jar *.class`

To run MapReduce Job:
`hadoop jar <filename>.jar <main_class> <input_dir> <output_dir>`

commands: hadoop fs <command>
```
-mkdir : make dir
-rmdir : remove dir
-ls : list
-put : copy
-cat: show
-rm: remove
```
