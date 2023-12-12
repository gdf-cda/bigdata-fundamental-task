from mrjob.job import MRJob
import xml.etree.ElementTree as ET

class XMLMapReduceJob(MRJob):

    def mapper(self, _, line):
        # Parse the line as XML
        element = ET.fromstring(line)
        # Assuming the element name we are interested in is 'category'
        category = element.find('category').text
        yield category, 1

    def reducer(self, key, values):
        # Sum up all counts for each category
        total = sum(values)
        yield key, total

if __name__ == '__main__':
    XMLMapReduceJob.run()
