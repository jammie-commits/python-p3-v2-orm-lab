class Review:
    all_reviews = {}  # Dictionary to store reviews (replace with database access)

    def __init__(self, year, summary, employee_id, id=None):
        self.year = year
        self.summary = summary
        self.employee_id = employee_id
        self.id = id

    @classmethod
    def create(cls, year, summary, employee_id):
        """Creates a new Review instance and saves it."""
        review = cls(year, summary, employee_id)
        review.save()
        return review

    def save(self):
        """Saves the Review object to the dictionary or database."""
        self.all_reviews[self.id or self._get_new_id()] = self

    @classmethod
    def _get_new_id(cls):
        """Generates a new unique ID for the Review object."""
        # Implement logic to generate a unique ID (e.g., incrementing counter)
        # This is a placeholder for real ID generation
        new_id = len(cls.all_reviews) + 1
        return new_id

    @classmethod
    def instance_from_db(cls, row):
        """Returns a Review instance from a dictionary row."""
        id, year, summary, employee_id = row
        review = cls.all_reviews.get(id)
        if not review:
            review = cls(year, summary, employee_id, id)
            review.save()  # Cache the newly created instance
        return review

    @classmethod
    def find_by_id(cls, id):
        """Returns a Review instance for the given ID or None."""
        row = cls.all_reviews.get(id)
        return cls.instance_from_db(row) if row else None

    def update(self):
        """Updates the Review object's corresponding row in the dictionary."""
        self.save()  # Update the dictionary with the current object state

    def delete(self):
        """Deletes the Review object from the dictionary and sets its ID to None."""
        del self.all_reviews[self.id]
        self.id = None

    @classmethod
    def get_all(cls):
        """Returns a list of all Review instances."""
        return [cls.instance_from_db(row) for row in cls.all_reviews.values()]
