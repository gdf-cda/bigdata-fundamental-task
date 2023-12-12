from mrjob.job import MRJob
import csv

class MyMapReduceJob(MRJob):

    def mapper(self, _, line):
        # TODO: Implement your mapper logic here
        pass

    def reducer(self, key, values):
        # TODO: Implement your reducer logic here based on the task (sum, avg, min, max, etc.)
        pass

if __name__ == '__main__':
    MyMapReduceJob.run()
