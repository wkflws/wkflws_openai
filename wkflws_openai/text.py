import json
from typing import Any
import sys

import openai


async def generate_text(
    message: dict[str, Any],
    context: dict[str, Any],
) -> dict[str, Any]:
    """Generate a text response based on the input."""
    # All debugging information MUST be output in stderr. you can just use the logging
    # module or if you are a die hard print debugger use this instead:
    # print("My debug!", file=sys.stderr)

    engine = message.get("engine", "davinci")
    try:
        prompt = message["prompt"]
    except KeyError:
        raise ValueError("Required 'prompt' parameter missing.") from None

    try:
        openai.api_key = context["Task"]["openai_api_key"]
    except KeyError:
        raise ValueError("Required 'openai_api_key' credential missing.") from None

    try:
        openai.organization = context["Task"]["openai_organization_id"]
    except KeyError:
        raise ValueError("Required 'openai_organization_id' missing.") from None

    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        max_tokens=300,
        stop=["\nHuman"],
    )
    return response


if __name__ == "__main__":
    import asyncio
    import sys

    # message is the input to your function. This is the output from the previous
    # function plus any transformations the user defined in their workflow. Parameters
    # should be documented in the parameters.json file so they can be used in the UI.
    try:
        message = json.loads(sys.argv[1])
    except IndexError:
        raise ValueError("missing required `message` argument") from None

    # this contains some contextual information about the workflow and the current
    # state. required secrets should be defined in the README so users can write their
    # lookup class with this node's unique requirements in mind.
    try:
        context = json.loads(sys.argv[2])
    except IndexError:
        raise ValueError("missing `context` argument") from None

    output = asyncio.run(generate_text(message, context))

    # Non-zero exit codes indicate to the executor there was an unrecoverable error and
    # workflow execution should terminate.
    if output is None:
        sys.exit(1)

    # The output of your function is input for a potential next state. It must be in
    # JSON format and be the only thing output on stdout. This value is picked up by the
    # executor and processed.
    print(json.dumps(output))
