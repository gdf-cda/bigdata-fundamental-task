from mrjob.job import MRJob
import csv

class MyMapReduceJob(MRJob):

    def mapper(self, _, line):
        # Parse the line as CSV
        category, value = line.split(',')
        yield category, int(value)

    def reducer(self, category, values):
        values_list = list(values)
        total_sum = sum(values_list)
        total_count = len(values_list)
        average = total_sum / total_count if total_count else 0
        min_value = min(values_list)
        max_value = max(values_list)
        
        yield category, {'sum': total_sum, 'average': average, 'min': min_value, 'max': max_value}

if __name__ == '__main__':
    MyMapReduceJob.run()
