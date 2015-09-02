import datetime
import struct

class BinaryParser(object):
    def __init__(self, verbose):
        self.verbose = verbose

    def parse_input_string(self, serv_timestamp, data):
        if self.verbose:
            print '\nbinary parcer: start processing \npacket={}'.format(data)
        sensor_data_length = struct.unpack('!B', data[:1])[0]
        data = data[1:]
        timestamp  = struct.unpack('!Q', data[:8])[0]
        try: 
            date = datetime.datetime.fromtimestamp(timestamp)
            date_today = datetime.datetime.now()
            timedelta = date_today - date
            if timedelta.days > 1:
                raise Exception('timedelta too big')
        except Exception as e:
            print e
            if self.verbose:
                print 'binary parcer: invalid timestamp = {}. instead use {}'.format(timestamp, serv_timestamp)
            timestamp = serv_timestamp

        if self.verbose:
            print 'binary parcer: timestamp = {}'.format(timestamp)

        data = data[8:]
        sensor_data_length = min(int(len(data) / 12), sensor_data_length)

        if self.verbose:
            print 'binary parcer: sensor data length = {}'.format(sensor_data_length)

        if sensor_data_length > 0:
            if self.verbose:
                print 'binary parcer: start sensor data parsing '
            result = [timestamp, [], [], [], [], [], []]    
            for offset in xrange(sensor_data_length):
                for index in xrange(6):
                    current_chunk = data[offset * 12 + index * 2: offset * 12 + index * 2 + 2]
                    current_chunk_int_repr = struct.unpack('!h', current_chunk)[0]
                    result[index + 1].append(current_chunk_int_repr)
            if self.verbose:
                print 'binary parcer: stop parsing. result={}'.format(result)   
            return result
        else:
            if self.verbose:
                print 'binary parcer: stop processing. Packet length < 12 byte\n'