class States:
    """
    This class manages the data of the csv file and 
    breaks a state into 10 different properties and 
    calcualtes 3 more. Also includes getters and
    setters. A few other functions using magic methods
    in python plus an init/constructor.
    """

    def __init__(self, state, capitol, region, houseseat, pop, covcases, covdeaths, vacrates, medincome, violentcrime):
        self.state = state
        self.capitol = capitol
        self.region = region
        self.houseseat = houseseat
        self.pop = pop
        self.covcases = covcases
        self.covdeaths = covdeaths
        self.vacrates = float(vacrates) / 100
        self.medincome = int(medincome)
        self.violentcrime = float(violentcrime)
        self.caseRate = (float(covcases) / float(pop)) * 100000
        self.deathRate = (float(covdeaths) / float(pop)) * 100000
        self.CFR = self.get_deathRate() / self.get_caseRate()

    def get_CFR(self):
        """
        A getter for CFR that returns self.CFR
        :param: self - acts as this. like in java
        :return self.CFR
        """
        return self.CFR

    def get_caseRate(self):
        """
        A getter for caseRate that returns self.caseRate
        :param: self - acts as this. like in java
        :return self.caseRate
        """
        return self.caseRate

    def set_caseRate(self, caseRate):
        """
        A setter for caseRate that returns nothing
        but sets the attribute equal to its this.
        java equivalent
        :param: self - acts as this. like in java
        :return self.caseRate
        """
        self.caseRate = caseRate

    def get_deathRate(self):
        """
        A getter for deathRate that returns self.deathRate
        :param: self - acts as this. like in java
        :return self.deathRate
        """
        return self.deathRate

    def set_deathRate(self, deathRate):
        """
        A setter for death rate that returns nothing
        but sets the attribute equal to its this.
        java equivalent
        :param: null
        :return self.deathRate
        """
        self.deathRate = deathRate

    # will compare two states objects names
    def __gt__(self, state1):
        """
        Override dunded method for greater than 
        with 2 paremeters that are compared by the 
        object state names 
        :param: self
        :param: state1 - state object 
        :return 1 if bigger
        :return 0 if smaller
        """
        if self.get_state() > state1.get_state():
            print("state 1 bigger")
            return 1
        else:
            print("state 2 bigger")
            return 0

    # print state object as a string

    def __str__(self):
        """
        Performs a simpel print statment using f
        print format. 
        :param: self
        :return 0
        """
        print(f'{"Name:":25s} {self.state:15s} \n{"Median Income":15s} {self.medincome:15.0f} \n'
              f'{"VCR":15s} {self.violentcrime:15.1f}\n{"CFR":19s}{self.CFR:15.6f}\n'
              f'{"Case Rate":14s}{self.caseRate:20.2f} \n{"Death Rate":9s} {self.deathRate:21.2f}\n'
              f'{"FVR":17s}{self.vacrates:14.3f}\n')

        return 0

    # get/set state
    def get_state(self):
        """
        A getter for state that returns self.state
        :param: self - acts as this. like in java
        :return self.state
        """
        return self.state

    def set_state(self, state):
        """
        A setter for state that returns nothing
        but sets the attribute equal to its this.
        java equivalent
        :param: null
        :return self.state
        """
        self.state = state

    #  get/set capitol
    def get_capitol(self):
        """
        A getter for capitol that returns self.capitol
        :param: self - acts as this. like in java
        :return self.capitol
        """
        return self.capitol

    def set_capitol(self, capitol):
        """
        A setter for capitol that returns nothing
        but sets the attribute equal to its this.
        java equivalent
        :param: null
        :return self.capitol
        """
        self.capitol = capitol

    # get/set Region
    def get_region(self):
        """
        A getter for region that returns self.region
        :param: self - acts as this. like in java
        :return self.region
        """
        return self.region

    def set_region(self, region):
        """
        A setter for reguon that returns nothing
        but sets the attribute equal to its this.
        java equivalent
        :param: null
        :return self.region
        """
        self.region = region

    # get/set Houseseat
    def get_houseseat(self):
        """
        A getter for houseSeats that returns self.houseSeats
        :param: self - acts as this. like in java
        :return self.houseSeats
        """
        return self.houseseat

    def set_houseseat(self, houseseat):
        """
        A setter for house seats that returns nothing
        but sets the attribute equal to its this.
        java equivalent
        :param: null
        :return self.houseat
        """
        self.houseseat = houseseat

    # get/set population
    def get_pop(self):
        """
        A getter for population that returns self.population
        :param: self - acts as this. like in java
        :return self.pop
        """
        return self.pop

    def set_pop(self, pop):
        """
        A setter for population that returns nothing
        but sets the attribute equal to its this.
        java equivalent
        :param: null
        :return self.pop
        """
        self.pop = pop

    # get/set covid cases
    def get_covcases(self):
        """
        A getter for covid cases that returns self.covcases
        :param: self - acts as this. like in java
        :return self.covcases
        """
        return self.covcases

    def set_covcases(self, covcases):
        """
        A setter for covid cases that returns nothing
        but sets the attribute equal to its this.
        java equivalent
        :param: null
        :return self.covcases
        """
        self.covcases = covcases

    # get/set covid deaths
    def get_covdeaths(self):
        """
        A getter for covid deaths that returns self.covdeaths
        :param: self - acts as this. like in java
        :return self.covdeaths
        """
        return self.covdeaths

    def set_covdeaths(self, covdeaths):
        """
        A setter for covid deaths that returns nothing
        but sets the attribute equal to its this.
        java equivalent
        :param: null
        :return self.covdeaths
        """
        self.covdeaths = covdeaths

    # get/set vaccine rates
    def get_vacrates(self):
        """
        A getter for vaccine rates that returns self.vacrates
        :param: self - acts as this. like in java
        :return self.vacrates
        """
        return self.vacrates

    def set_vacrates(self, vacrates):
        """
        A setter for vaccine rates that returns nothing
        but sets the attribute equal to its this.
        java equivalent
        :param: null
        :return self.vacrates
        """
        self.vacrates = vacrates

    # get/set median incomes
    def get_medInc(self):
        """
        A getter for median income that returns self.medincome
        :param: self - acts as this. like in java
        :return self.medincome
        """
        return self.medincome

    def set_medInc(self, medincome):
        """
        A setter for median income that returns nothing
        but sets the attribute equal to its this.
        java equivalent
        :param: null
        :return self.medincome
        """

        self.medincome = medincome

    # get/set violent crime
    def get_violentcrime(self):
        """
        A getter for violent crime that returns self.violentcrime
        :param: self - acts as this. like in java
        :return self.violentcrime
        """
        return self.violentcrime

    def set_violentcrime(self, violentcrime):
        """
        A setter for violent crime that returns nothing
        but sets the attribute equal to its this.
        java equivalent
        :param: null
        :return self.violentcrime
        """

        self.violentcrime = violentcrime
