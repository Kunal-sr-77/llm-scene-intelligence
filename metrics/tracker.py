class MetricsTracker:
    def __init__(self):
        self.total = 0
        self.correct = 0
        self.error_counts = {}

    def update(self, errors):
        self.total += 1

        if not errors:
            self.correct += 1
        else:
            for error in errors:
                error_type = error["type"]
                if error_type not in self.error_counts:
                    self.error_counts[error_type] = 0
                self.error_counts[error_type] += 1

    def report(self):
        accuracy = (self.correct / self.total) * 100 if self.total > 0 else 0

        return {
            "total_samples": self.total,
            "correct_outputs": self.correct,
            "accuracy": round(accuracy, 2),
            "error_distribution": self.error_counts
        } 