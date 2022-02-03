class States:
    def __init__(self, state, capitol, region, houseseat, pop, covcases, covdeaths, vacrates, medincome, violentcrime):
        self.state = state
        self.capitol = capitol
        self.region = region
        self.houseseat = houseseat
        self.pop = pop
        self.covcases = covcases
        self.covdeaths = covdeaths
        self.vacrates = vacrates
        self.medincome = medincome
        self.violentcrime = violentcrime

    # will compare two states objects names
    def __gt__(self, state1):
        if self.get_state() > state1.get_state():
            print("state 1 bigger")
            return 1
        else:
            print("state 2 bigger")
            return 0

    # print state object as a string

    def __str__(self):
        print(f' State: {self.get_state()}, Capitol: {self.get_capitol()}, Region: {self.get_region()},'
              f' House Seats: {self.get_houseseat()}, Population: {self.pop}, Covid Cases: {self.get_covcases()},'
              f' Covid Deaths: {self.get_covdeaths()}, Vaccine Rates: {self.get_vacrates()},'
              f' Median Income: {self.medincome}, Violent Crime: {self.get_violentcrime()}')
        return 0

    # get/set state
    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    #  get/set capitol
    def get_capitol(self):
        return self.capitol

    def set_capitol(self, capitol):
        self.capitol = capitol

    # get/set Region
    def get_region(self):
        return self.region

    def set_region(self, region):
        self.region = region

    # get/set Houseseat
    def get_houseseat(self):
        return self.houseseat

    def set_houseseat(self, houseseat):
        self.houseseat = houseseat

    # get/set population
    def get_pop(self):
        return self.pop

    def set_pop(self, pop):
        self.pop = pop

    # get/set covid cases
    def get_covcases(self):
        return self.covcases

    def set_covcases(self, covcases):
        self.covcases = covcases

    # get/set covid deaths
    def get_covdeaths(self):
        return self.covdeaths

    def set_covdeaths(self, covdeaths):
        self.covdeaths = covdeaths

    # get/set vaccine rates
    def get_vacrates(self):
        return self.vacrates

    def set_vacrates(self, vacrates):
        self.vacrates = vacrates

    # get/set median incomes
    def get_vacrates(self):
        return self.vacrates

    def set_vacrates(self, vacrates):
        self.vacrates = vacrates

    # get/set violent crime
    def get_violentcrime(self):
        return self.violentcrime

    def set_violentcrime(self, violentcrime):
        self.violentcrime = violentcrime

    def getCFR(self):
        #print(float(self.get_covdeaths())/float(self.get_covcases()))
        return float(self.get_covdeaths())/float(self.get_covcases())
