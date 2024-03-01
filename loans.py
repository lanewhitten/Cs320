race_lookup = {
    "1": "American Indian or Alaska Native",
    "2": "Asian",
    "3": "Black or African American",
    "4": "Native Hawaiian or Other Pacific Islander",
    "5": "White",
    "21": "Asian Indian",
    "22": "Chinese",
    "23": "Filipino",
    "24": "Japanese",
    "25": "Korean",
    "26": "Vietnamese",
    "27": "Other Asian",
    "41": "Native Hawaiian",
    "42": "Guamanian or Chamorro",
    "43": "Samoan",
    "44": "Other Pacific Islander"
}

class Applicant:
    def __init__(self, age, race):
        self.age = age
        self.race = set()
        for r in race:
            try:
                self.race.add(race_lookup[r])
            except KeyError:
                pass
    def __repr__(self):
        self.race = list(self.race)
        return f"Applicant('{self.age}','{self.race}')"
    
    def lower_age(self):
        age = self.age.replace("<","")
        age = age.replace(">","")
        age = age.split("-")[0]
        return int(age)
    def __lt__(self, other):
        return self.lower_age() < other.lower_age()


class Loan:
    def __init__(self, values):
        try:
            self.loan_amount = float (values["loan_amount"])
        except KeyError:
            self.loan_amount = -1
        
        try:
            self.interest_rate = float(values["interest_rate"])
        except KeyError:
            self.interest_rate = -1
        
        try:
            self.property_value = float(values["property_value"])
        except:
            self.property_value = -1
        
        applicants_race = []
        applicants_race.append(Applicant(values["applicant_age"], values["applicant_race-1"]))
        if values["co-applicant_age"] != "9999":
            applicants_race.append(Applicant(values["co-applicant_age"], values["co-applicant_race-1"]))
        self.applicants = applicants_race
        
        self.applicants = values["applicants"]

    def __str__(self):
        return f"<Loan: {self.interest_rate}% on ${self.property_value} with {len(self.applicants)} applicant(s)>"
    
    def __repr__(self):
        return f"<Loan: {self.interest_rate}% on ${self.property_value} with {len(self.applicants)} applicant(s)>"
    
    def yearly_amounts(self, yearly_payment):
        assert self.interest_rate > 0
        assert self.loan_amount > 0
        amt = self.loan_amount

        while amt > 0:
            yield amt
            amt = amt + (self.interest_rate/100 * amt) 
            amt = amt - yearly_payment

class Bank:
    def __init__(self, name, loans):
        self.name = name
        self.loans = []
    #todo finish init
    def __len__(self):
        return len(self.loans)
    
    def __getitem__(self, index):
        return self.loans[index]