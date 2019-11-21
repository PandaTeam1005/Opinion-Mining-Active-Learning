class Oracle:
    def label(self,elements,info):
        pass
class Console_Oracle(Oracle):
    def label(self,elements,info):
        collection = info["collection"]
        return [(e,input(collection.item_text(e))) for e in elements]