


class User:
    def __init__(self, first_name, last_name, dob, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.email = email
        self.password = password

    
    def from_dict(cls, data):
        return cls(
            first_name = data.get('firstName'),
            last_name = data.get('lastName'),
            dpb = data.get('dob'),
            email = data.get('email'),
            password = data.get('password')
        )
    
    def to_dict(self):
        return {
            'firstName': self.first_name,
            'lastName': self.last_name,
            'dob': self.dob,
            'email': self.email,
            'password': self.password
        }
        