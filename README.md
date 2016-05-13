# kafka_spark_cassandra
Tech demo of Kafka, spark and cassandra

## Purpose
To learn how to connect the Kafka, Apache Spark and Cassandra
Using docker to connect all the services.

# Services
## kafka_producer
Adds up/down votes to a random list of uuids that are specificed in cassandara

## spark_consumer
Reads from kafka, creates counts and enters data into cassandra

## cassandra
Sets up simple table for inserting datak
