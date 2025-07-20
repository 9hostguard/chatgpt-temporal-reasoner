from real_time_processing.streaming_example import stream_data

def test_stream_data():
    data_source = ["Event A", "Event B", "Event C"]
    stream_data(data_source)