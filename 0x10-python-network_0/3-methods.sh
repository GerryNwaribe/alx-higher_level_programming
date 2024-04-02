#!/bin/bash
# Check if URL argument is provided
curl -sS --head "$1" | grep -i '^Allow:' | sed 's/Allow: //i'
