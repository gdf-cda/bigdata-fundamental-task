from mrjob.job import MRJob
import csv

class CSVMapReduceJob(MRJob):

    def mapper(self, _, line):
        # Use csv.reader to safely parse the CSV line
        reader = csv.reader([line])
        for row in reader:
            # Assuming the field to count is the first field
            yield row[0], 1

    def reducer(self, key, values):
        # Sum up all counts for each key
        total = sum(values)
        yield key, total

if __name__ == '__main__':
    CSVMapReduceJob.run()
