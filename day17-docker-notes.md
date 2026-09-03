# Day 17 - Docker Containerization

## What I did
- Cleaned up auto-generated test artifacts from version control
- Created a Dockerfile to containerize the test project
- Generated requirements.txt with exact dependency versions
- Built and ran the project inside an isolated Docker container

## Why this matters
Containerizing tests ensures they run identically regardless of 
the host machine's configuration - solving the "works on my 
machine" problem. This is the same principle used when Jenkins 
runs tests inside its own container (Day 9), but here I built 
the custom image myself instead of using a pre-made one.
