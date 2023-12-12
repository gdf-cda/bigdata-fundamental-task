from mrjob.job import MRJob
import json

class MyMapReduceJob(MRJob):

    def mapper(self, _, line):
        # TODO: Parse the JSON line and process it.
        # Convert the line to a JSON object.
        # Yield key-value pairs based on your task.
        pass

    def reducer(self, key, values):
        # TODO: Process the values for each key.
        # Aggregate, summarize, or transform the values.
        # Yield the results.
        pass

if __name__ == '__main__':
    MyMapReduceJob.run()
