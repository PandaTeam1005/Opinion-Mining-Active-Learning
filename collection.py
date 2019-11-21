#a collection item must have a propery text for the oracle to classif
from hashlib import sha256
class Collection:
    def join(self,new_elements):
        pass
    def remove(self,old_elements):
        pass
    def len(self):
        pass
    def get_items(self,selected):
        pass
    def elements(self):
        pass
    def item_text(self,item):
        pass
    def item_class(self,item):
        pass
    def item_vector(self,item):
        pass
    

#probably Index_Collection must have an inverse index dict (using hash or something) to get index given the item
class Index_Collection(Collection):
    def __init__(self,data,indexs):
        #data must be a list of tuples (vector,string,class)
        #index: index of data that belongs to the collection
        self.data = data
        self.items = set(indexs)
        self.inverse_index = {data[i][0]:i for i in range(len(data))}
    
    def elements(self):
        return [self.item_vector(self.data[i]) for i in self.items]
    
    def join(self,new_elements):
        #the type of new elemesent must_be [(vector,class)]
        
        new_elements_indx = self._inverse_indxs([elem[0] for elem in new_elements])
        self.items = self.items.union(new_elements_indx)
        for i in new_elements:
            self.data[i][2] = new_elements[2]
        #update the class
        
    
    def remove(self,old_elements):
        #old_elements are [(vector,class)]
        old_elements_indx = self._inverse_indxs([elem[0] for elem in old_elements])
        self.items = self.items.difference(old_elements_indx)
    
    def len(self):
        return len(self.items)

    def get_items(self,selected):
        #check if selected are indexs
        if len(selected) > 0 and type(selected[0]!=int):
            selected = self._inverse_indxs(selected)
        return [self.data[i] if i in self.items else None for i in selected]
    
    def _inverse_indxs(self,elements):
        return [self.inverse_index[e] for e in elements]
    
    def _item_prop(self,item,prop):
        if not type(item)==int:
            item = self.inverse_index[item]
        return self.data[item][prop]

    def item_vector(self,item):
        return self._item_prop(item,0)
    def item_text(self,item):
        return self._item_prop(item,1)
    def item_class(self,item):
        return self._item_prop(item,2)

    