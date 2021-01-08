class Seeder():

    _seeds_list = []

    def runner(self, name):
        self._seeds_list.append(name)

    def get_list(self):
        return self._seeds_list
