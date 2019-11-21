from random import choices
class Selector:
    def select(self,ranks,labelled,unlabelled,b):
        #ranks: [(item,class,rank)]
        pass

class Ramdom_Selector(Selector):
    def select(self,ranks,labelled,unlabelled,b):
        return [e[0] for e in choices(ranks,k=b)]
