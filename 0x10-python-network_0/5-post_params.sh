#!/bin/bash
# Check if URL argument is provided
curl -sS --compressed -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
