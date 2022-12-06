from taskmanager import db

class Category(db.Model):
    # schema for the category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False) # each value is unique and not NaN 
    
    # establish relationship between one table and the current one in the class which is written in lower
    # case as backref, where cascade deletes all with a related value that is deleted and lazy = True
    # means that when we query the db for categories, it can simultaneously identify any task linked to the categories.
    tasks = db.relationship("Task", backref="category", cascade="all, delete", lazy=True)

    def __repr__(self):
        # '__repr__' to represent itself in the form of a string
        # it means to represent the class object as a string
        return f'#{self.id} - Task: {self.task_name} | Urgent: {self.is_urgent}'


class Task(db.Model):
    # schema for the task model
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False) # string can have max 50 chars
    task_description = db.Column(db.Text, nullable=False) # text is much longer than string
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False) # ondelete="CASCADE" means that it deletes any associated rows in other tables if a column id is deleted and is found in a row

    def __repr__(self):
        # '__repr__' to represent itself in the form of a string
        return self