import zmq

context = zmq.Context()

receiver = context.socket(zmq.PULL)
receiver.connect("tcp://localhost:15677")

sender = context.socket(zmq.PUSH)
sender.connect("tcp://localhost:15678")

while True:
    s = receiver.recv()

    print "receive:"+str(s)
