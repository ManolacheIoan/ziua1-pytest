# Day 18 - Postman for API Testing

## What I did
- Explored Postman interface for manual API testing
- Created a Collection with multiple requests (GET, POST)
- Added automated test scripts (JavaScript) for status code and 
  response body validation
- Exported collection as JSON, added to project

## Postman vs pytest+requests
- Postman: visual, GUI-based, good for quick exploration, manual 
  testing, and sharing API documentation with non-technical team members
- pytest+requests: code-based, better for CI/CD integration, version 
  control, and complex test logic
- Both use the same underlying HTTP concepts (status codes, headers, 
  JSON body validation)
- Postman collections can be exported and run via command line 
  (Newman) for CI/CD integration too
