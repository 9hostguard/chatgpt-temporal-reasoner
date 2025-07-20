from visualization.dashboard_example import plot_events

def test_plot_events():
    """Test the plot_events function with sample data."""
    events = [
        {'timestamp': 1, 'label': 'Event A'},
        {'timestamp': 2, 'label': 'Event B'},
        {'timestamp': 3, 'label': 'Event C'}
    ]
    # Note: In a real test, we'd mock plt.show() to avoid displaying the plot
    plot_events(events)