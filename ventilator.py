import zmq

context = zmq.Context()

sender = context.socket(zmq.PUSH)
sender.bind("tcp://*:15677")

sender.send(" [ventilator] send.",flags=zmq.NOBLOCK)
print "ok"