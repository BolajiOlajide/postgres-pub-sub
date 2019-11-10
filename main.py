#!/usr/bin/env python3
import pgpubsub

pubsub = pgpubsub.connect(user="testuser", database="dump")

pubsub.listen("ci_jobs_status_channel")

try:
    for e in pubsub.events():
        message = f"""
    ---------------------------------------
    Payload: {e.payload}

    channel: {e.channel}

    PID: {e.pid}
    ---------------------------------------
    """
        print(message)
except:
    pubsub.unlisten("channel2")
    print("I dont want to run deaf. I've stopped listening")
