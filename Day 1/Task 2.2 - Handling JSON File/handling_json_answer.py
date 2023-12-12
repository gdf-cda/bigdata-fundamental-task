from mrjob.job import MRJob
import json

class JSONMapReduceJob(MRJob):

    def mapper(self, _, line):
        # Parse the line as JSON
        record = json.loads(line)
        # Yield the category field value
        yield record['category'], 1

    def reducer(self, key, values):
        # Sum up all counts for each category
        total = sum(values)
        yield key, total

if __name__ == '__main__':
    JSONMapReduceJob.run()
