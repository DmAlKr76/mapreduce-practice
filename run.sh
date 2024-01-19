export MR_OUTPUT=/user/root/output-data

hadoop fs -rm -r $MR_OUTPUT

hadoop jar "$HADOOP_MAPRED_HOME"/hadoop-streaming.jar \
-Dmapred.job.name='Home work job' \
-Dmapred.reduce.tasks=1 \
-Dmapreduce.map.memory.mb=1024 \
-file /tmp/mapreduce/mapper.py -mapper /tmp/mapreduce/mapper.py \
-file /tmp/mapreduce/reducer.py -reducer /tmp/mapreduce/reducer.py \
-input /user/root/2020/2020 -output $MR_OUTPUT


hadoop fs -cat /user/root/output-data/part-00000* > result.csv