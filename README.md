# wkflws_openai
This node provides actions to use the OpenAI system.

## wkflws_openai.text
Generate text responses from a prompt.

### Parameters
The following parameters are available.
| name | required | description |
|-|-|-|
| `prompt`| ✅ | The prompt to send to OpenAI. |
| `engine` | ❌  | The OpenAI text engine to use. Defaults to `davinci`. |

### Context Properities
The following context properties are required for this node.
| name | required | description |
|-|-|-|
| `openai_api_key` | ✅ | Your API token to OpenAI. |
| `openai_organization_id` | ✅ | Your OpenAI organization id. This is required for some OpenAI API calls. |

### Example Input
```json
{
  "engine": "davinci",
  "prompt": "Sam is a chatbot that reluctantly answers questions with sarcastic responses:\n\nWhat days is today?"
}

```

### Example Output
```json
{
  "id": "cmpl-5Ihefjk6ciTWNQVt7A0GMn1pjTuEI",
  "object": "text_completion",
  "created": 1655139397,
  "model": "davinci",
  "choices": [
    {
      "text": " Tuesday\n\nWhy does the chicken cross the road? To get away from you",
      "index": 0,
      "logprobs": null,
      "finish_reason": "length"
    }
  ]
}
```
