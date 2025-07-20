import time

def stream_data(data_source):
    """
    Simulate streaming data for temporal reasoning.
    Args:
        data_source (list): A list of data points to stream.
    """
    for data_point in data_source:
        print(f"Processing: {data_point}")
        time.sleep(1)  # Simulate real-time stream