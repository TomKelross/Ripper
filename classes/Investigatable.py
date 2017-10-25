from fuzzywuzzy import process


class Investigatable(object):
    def __init__(self, name="Strange item", description="Something seems off about this"):
        self.name = name
        self.description = description

    def __repr__(self):
        return "<Investigatable {}>".format(self.name)
    
    def investigate(self):
        return self.description


class InvestigatableManager(object):
    def __init__(self, list_of_investigatable):
        self.investigatable = list_of_investigatable

    def get_investigatable(self, name):
        for Investigatable in self.investigatable:
            if Investigatable.name == name:
                return Investigatable
        return False

    def get_investigatable_fuzzy(self, fuzzy_name):
        all_investigatable = self.investigatable
        names_of_all_investigatable = [investigtable.get_name() for investigtable in all_investigatable]
        best_guess = process.extract(fuzzy_name, names_of_all_investigatable, limit=1)
        certainty = best_guess[0][1]
        if certainty > 50:
            return self.get_investigtable(best_guess[0][0])
        else:
            return False
