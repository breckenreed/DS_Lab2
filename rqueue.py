import hazelcast
import time

if __name__ == "__main__":
    hz = hazelcast.HazelcastClient(
        cluster_members=[
        "127.0.0.1:5701",
        "127.0.0.1:5702",
        "127.0.0.1:5703"
    ],
    lifecycle_listeners=[
        lambda state: print("New event appeared in lifecycle: ", state),
    ])

queue = hz.get_queue("QUEUE_ONE").blocking()

for i in range(20):
    value = queue.take()
    print("Current value taken from READ queue : ", value)
    time.sleep(1)

hz.shutdown()
