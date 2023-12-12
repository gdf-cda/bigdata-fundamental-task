from mrjob.job import MRJob
import json
import xml.etree.ElementTree as ET

class AggregationMapReduceJob(MRJob):

    def mapper(self, _, line):
        # TODO: Parse the line based on file type (CSV, JSON, XML)
        # TODO: Yield key-value pairs
        pass

    def reducer(self, key, values):
        # TODO: Implement aggregation logic here
        # For example, count the number of emails and phone numbers for each user
        pass

if __name__ == '__main__':
    AggregationMapReduceJob.run()