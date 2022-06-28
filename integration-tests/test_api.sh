#!/bin/bash
set -e # Any subsequent commands which fail will cause the shell script to exit immediately

make build-api  # force build so the api starts fast
docker-compose -f docker-compose.api.yaml up -d  # run detached so we can continue
sleep 5
RESPONSE=$(curl -X POST localhost:5000/template -d 'some message')
make down

EXPECTED_RESPONSE="[App ver 0.0.1] Received POST request: 'some message'"
if [ "$RESPONSE" == "$EXPECTED_RESPONSE" ]; then
    echo "Returned correct response: \"$RESPONSE\""
    echo "Integration test finished successfully!"
else
    echo "Integration test failed!"
    echo "The expected and actual response are different: \"$EXPECTED_RESPONSE\" vs. \"$RESPONSE\"" >&2
    exit 1
fi
