class RoverModel:
    def __init__(self, name, launch_date, landing_date, status, max_date):
        self.name = name
        self.launch_date = launch_date
        self.landing_date = landing_date
        self.status = status
        self.max_date = max_date

    @classmethod
    def from_json(cls, json_body):
        data = json_body['photo_manifest']
        return cls(data['name'], data['launch_date'], data['landing_date'], data['status'], data['max_date'])
