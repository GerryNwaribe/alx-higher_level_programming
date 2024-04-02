#!/bin/bash
# bash sript
curl -sI $1 | grep "Content-Length" | cut -d " " -f2