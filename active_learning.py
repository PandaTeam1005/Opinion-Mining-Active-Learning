class Active_Learning:
    def __init_(self,oracle,selector,labelled,unlabelled,classifier,stop_criteria):
        self.L = labelled
        self.U = unlabelled
        self.stop_criteria = stop_criteria
        self.Selector = selector
        self.Classifier = classifier
        self.Oracle = oracle

    def __single_iteration(self,b=5):
        #For each unlabelled example, assign a value to indicate its informativeness
        ranked = self.Classifier.classify(self.L,self.U)
        selected = self.Selector.select(ranked) 
        new_labelled = self.Oracle.label(selected)
        self.L.join(new_labelled)
        self.U.remove(new_labelled)

    def learning_loop(self):
        while not self.stop_criteria():
            self.__single_iteration()
        

