from adaptive_learning.feedback_loop import feedback_loop

class MockModel:
    """Mock model for testing purposes."""
    def __init__(self):
        self.updates = []
    
    def update(self, feedback):
        """Mock update method."""
        self.updates.append(feedback)

def test_feedback_loop():
    """Test the feedback loop functionality."""
    model = MockModel()
    feedback_data = ["feedback1", "feedback2", "feedback3"]
    
    updated_model = feedback_loop(model, feedback_data)
    
    assert len(updated_model.updates) == 3
    assert updated_model.updates == feedback_data