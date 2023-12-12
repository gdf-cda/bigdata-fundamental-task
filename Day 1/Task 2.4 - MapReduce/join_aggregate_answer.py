class AggregationMapReduceJob(MRJob):

    def mapper(self, _, line):
        # Determine the type of input and parse
        if ',' in line:
            user_id, _ = line.split(',')
            yield user_id, ('name', 1)
        elif line.startswith('{') and line.endswith('}'):
            record = json.loads(line)
            yield record['user_id'], ('email', 1)
        else:
            element = ET.fromstring(line)
            user_id = element.find('user_id').text
            yield user_id, ('phone', 1)

    def reducer(self, user_id, values):
        email_count = 0
        phone_count = 0
        for value_type, _ in values:
            if value_type == 'email':
                email_count += 1
            elif value_type == 'phone':
                phone_count += 1

        yield user_id, {'email_count': email_count, 'phone_count': phone_count}

if __name__ == '__main__':
    AggregationMapReduceJob.run()