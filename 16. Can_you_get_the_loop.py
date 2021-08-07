'''
You are given a node that is the beginning of a linked list. This list always contains a tail and a loop.
Your objective is to determine the length of the loop.
For example in the following picture the tail's size is 3 and the loop size is 12:
# Use the `next' attribute to get the following node
node.next
'''

def loop_size(node):
    current = node
    i = 1
    #Добавляет объекту указанный атрибут. setattr(obj, name, value).
    #obj: Объект, который следует дополнить атрибутом.
    #name: Строка с именем атрибута. Можно указывать как имя нового, так и существующего атрибута.
    #value: Произвольное значение атрибута.
    setattr(current, "visited", True)
    setattr(current, "n", i)

    #Возвращает флаг, указывающий на то, содержит ли объект указанный атрибут. hasattr(obj, name) -> bool
    #obj: Объект, существование атрибута в котором нужно проверить.
    #name: Имя атрибута, существование которого требуется проверить.

    while not hasattr(current.next, "visited"):
        current = current.next
        setattr(current, "visited", True)
        i += 1
        setattr(current, "n", i)
    n = (i+1)-current.next.n
    return n

'''
-----BEST PRACTICES-----
#1
def loop_size(node):
    turtle, rabbit = node.next, node.next.next

    # Find a point in the loop.  Any point will do!
    # Since the rabbit moves faster than the turtle
    # and the kata guarantees a loop, the rabbit will
    # eventually catch up with the turtle.
    while turtle != rabbit:
        turtle = turtle.next
        rabbit = rabbit.next.next

    # The turtle and rabbit are now on the same node,
    # but we know that node is in a loop.  So now we
    # keep the turtle motionless and move the rabbit
    # until it finds the turtle again, counting the
    # nodes the rabbit visits in the mean time.
    count = 1
    rabbit = rabbit.next
    while turtle != rabbit:
        count += 1
        rabbit = rabbit.next

    # voila
    return count

#2
def loop_size(node):
    index = {}
    i = 0
    while True:
        if node in index:
            return i - index[node]
        index[node] = i
        node = node.next
        i += 1
'''