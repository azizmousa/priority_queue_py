from priority_queue import PriorityQueue

pq = PriorityQueue();

pq.push("aziz", 4)
pq.push("mousa", 2)
pq.push("mah", 2)
pq.push("nor", 1)
pq.push("MG", 3)

pq.show()

pq.pop()

pq.show()

pq.pop()
pq.pop()
pq.pop()
pq.pop()
pq.pop()

pq.show()

pq.push("aziz")
pq.push("mousa")
pq.push("mah")

pq.show()

print(pq.front())