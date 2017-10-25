from fuzzywuzzy import process


class Investigatable(object):
    def __init__(self, name="Strange item", description="Something seems off about this"):
        self.name = name
        self.description = description

    def __repr__(self):
        return "<Investigatable {}>".format(self.name)
    
    def investigate(self):
        return self.description

    def get_name(self):
        return self.name


class InvestigatableManager(object):
    def __init__(self, list_of_investigatable):
        self.investigatables = list_of_investigatable

    def get_investigatable(self, name):
        for Investigatable in self.investigatables:
            if Investigatable.name == name:
                return Investigatable
        return False

    def get_investigatable_fuzzy(self, fuzzy_name, search_space=False):
        if search_space:
            all_investigatables = search_space
        else:
            all_investigatables = self.investigatables

        names_of_all_investigatable = [investigatable.get_name() for investigatable in all_investigatables]
        best_guess = process.extract(fuzzy_name, names_of_all_investigatable, limit=1)
        certainty = best_guess[0][1]
        if certainty > 50:
            return self.get_investigatable(best_guess[0][0])
        else:
            return False
