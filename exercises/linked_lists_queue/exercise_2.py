from collections import Counter
import random
import heapq

few_events = [{
   'event_type': f'{int(random.random() * 100)}',
   'data': f'{random.random() * 10000}'
} for _ in range(1000)]
# many_events = [{
#    'event_type': f'{int(random.random() * 10000)}',
#    'data': f'{random.random() * 10000}'
# } for _ in range(10000000)]

def print_least_common(events):
    counter = Counter((x['event_type'] for x in events))
    least_frequent_events = sorted(counter, key=lambda x: counter[x])
    for event_type in least_frequent_events[:20]:
        print(f'Event {event_type} occured {counter[event_type]} times.')

def print_least_common_heap(events):
   counter = Counter((x['event_type'] for x in events))
   tuples = [(v, k) for (k, v) in counter.items()]
   pass
   # Solution
   # heapq.heapify(tuples)
   # for _ in range(20):
   #    count, event_type = heapq.heappop(tuples)
   #    print(f'Event {event_type} occured {count} times.')


print("Sorted:")
print_least_common(few_events)
# print("Priority queue")
# print_least_common_heap(few_events)
