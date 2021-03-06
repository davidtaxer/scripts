#!/bin/bash

if grep "127.0.0.1" /etc/hosts; then
  echo "Everything ok"
else
  echo "Error! 127.0.0.1 is not ok"
fi
