#!/bin/bash
# Check if URL argument is provided
curl -sS --compressed -H "X-School-User-Id: 98" "$1"
