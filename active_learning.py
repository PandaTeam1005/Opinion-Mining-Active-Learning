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
        #must return something like: [(item,class,rank)] where item must be vector or docmnt representation

        selected = self.Selector.select(ranked,self.L,self.U,b) #return selected items (must be vectors) [vectors]
        #selected = self.U.get_items(selected) 
        new_labelled = self.Oracle.label(selected) #must_return (vector,class)
        
        self.L.join(new_labelled)
        self.U.remove(new_labelled)

    def learning_loop(self):
        while not self.stop_criteria(self.L,self.U):
            self.__single_iteration()
        

