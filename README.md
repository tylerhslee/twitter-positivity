# Twitter Positivity
REST API for performing sentiment analysis on tweets.

# API Endpoints
## `GET` /score
### Parameters
#### URI Parameters
| Field | Data Type | Required | Description |
| handle | string | Yes | Twitter handle of the user |

#### Example Request
```bash
GET http://localhost:8080/score/?handle=TaylorSwift13
```

#### Example Response
```
{
	"handle": TaylorSwift13,
	"score": 2.0
}
```
