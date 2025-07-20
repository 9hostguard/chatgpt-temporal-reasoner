import matplotlib.pyplot as plt

def plot_events(events):
    """
    Plot events on a timeline.
    Args:
        events (list of dict): List of events with timestamps and labels.
    """
    timestamps = [event['timestamp'] for event in events]
    labels = [event['label'] for event in events]

    plt.plot(timestamps, labels, marker='o')
    plt.title("Event Timeline")
    plt.xlabel("Timestamp")
    plt.ylabel("Event")
    plt.show()