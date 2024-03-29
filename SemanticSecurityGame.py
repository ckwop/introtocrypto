class SemanticSecurityGame:
    
    def __init__(self, cryptoScheme, challenger):
        self.cryptoScheme = cryptoScheme
        self.challenger = challenger
        self.numberOfTrials = 0
        self.numberOfSuccesses = 0

    def runGame(self, maximumTrials):
        from random import randint
        while self.numberOfTrials < maximumTrials:
            m1, m2 = self.challenger.getMessages(self.numberOfTrials)
            choice = randint(0, 1)

            plainText = m2
            if choice == 0:
                plainText = m1

            cipherText = self.cryptoScheme.encrypt(plainText)

            result = self.challenger.challenge(cipherText, self.numberOfTrials)

            if result == choice:
                self.numberOfSuccesses = self.numberOfSuccesses + 1
            
            self.numberOfTrials =  self.numberOfTrials + 1
        
        return { "Trials": self.numberOfTrials, "Wins" : self.numberOfSuccesses }
            