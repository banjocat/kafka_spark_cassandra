# Personal learning excersise
  * How to connect the Kafka, Apache Spark and Cassandra
  * Using docker to connect all the services.
  * Use README driven development!

# Services
## kafka_producer
Adds up/down votes to a random list of uuids that are specificed in cassandara

## spark
Reads from kafka, creates counts and enters data into cassandra
To start need to enter container and execute

   spark-submit --packages org.apache.spark:spark-streaming-kafka_2.10:1.6.1 /code/consumer.py

## cassandra
Sets up simple table for inserting datak
