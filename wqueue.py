import hazelcast
import time

if __name__ == "__main__":
    hz = hazelcast.HazelcastClient( 
        cluster_members=[
        "172.24.0.2:5701",
        "172.24.0.3:5701",
        "172.24.0.4:5701"
    ],
    lifecycle_listeners=[
        lambda state: print("Event appeared in lifecycle: ", state),
    ])

queue = hz.get_queue("queue").blocking()

for i in range(25):
    queue.put(i)
    print("Write queue current value: ", i)
    time.sleep(1)

hz.shutdown()
