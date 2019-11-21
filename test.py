import active_learning
import collection
import oracle
import selector
import stop_criterias

data = [
    ([1,2,3,4],"text","A"),
    ([3,4,2,1],"text","B"),
    ([3,2,2,1],"text","A"),
    ([1,4,2,2],"text","B"),
    ([14,2,13,4],"text",None),
    ([3,42,1,21],"text",None),
    ([31,2,0,1],"text",None),
    ([1,4,0,2],"text",None)
]

L = collection.Index_Collection(data,[0,1,2,3])
U = collection.Index_Collection(data,[4,5,6,7])
new = [([14,2,13,4],"A")]
print(L.elements())
print(U.elements())
L.join(new)
U.remove(new)
print(L.elements())
print(U.elements())

ranks =  [
    #([1,2,3,4],"A",1),
    #([3,4,2,1],"B",1),
    #([3,2,2,1],"A",1),
    #([1,4,2,2],"B",1),
    ([14,2,13,4],"A",0.64),
    ([3,42,1,21],"A",0.22),
    ([31,2,0,1],"A",0.77),
    ([1,4,0,2],"A",0.1)
]


Oracle = oracle.Console_Oracle()
Selector = selector.Ramdom_Selector()
sc = stop_criterias.labelled

selected = Selector.select(ranks,L,U,2)
labelled = Oracle.label(selected,{"collection":U})
print(labelled)

L.join(labelled)
print(L.elements())