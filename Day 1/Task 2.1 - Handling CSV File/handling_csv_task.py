from mrjob.job import MRJob

class MyMapReduceJob(MRJob):

    def mapper(self, _, line):
        # TODO: Write your mapper code here.
        # Split the line into fields using CSV parsing.
        # Yield key-value pairs.
        pass

    def reducer(self, key, values):
        # TODO: Write your reducer code here.
        # Process the values for each key.
        # Yield the results.
        pass

if __name__ == '__main__':
    MyMapReduceJob.run()
