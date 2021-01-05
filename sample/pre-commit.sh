#!/bin/sh

echo "Testing Before Commit..."
python3 -c 'from sample.dir_01.handler import SampleCode; SampleCode("Joe").func_hello("Do not Share Food!")' || exit 1
echo "Testing Successful."
exit 0