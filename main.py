#!/usr/bin/env python3
import pgpubsub

pubsub = pgpubsub.connect(user='testuser', database='dump')

pubsub.listen('ci_jobs_status_channel')

for e in pubsub.events():
    print(e.payload)