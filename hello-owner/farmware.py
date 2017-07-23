#!/usr/bin/env python

import json
import os


send_message = {
  "kind": "send_message",
  "args": {
    "message": "Hello owner!",
    "message_type": "success"
  },
  "body": [
    {
      "kind": "channel",
      "args": {
        "channel_name": "toast"
      }
    }
  ]
}
print(os.environ['BEGIN_CELERYSCRIPT'] + json.dumps(send_message))
