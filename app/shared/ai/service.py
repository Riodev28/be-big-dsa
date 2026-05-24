from .ai import AI


class AIService:
    def __init__(self, client: AI):
        self.client: AI = client

    async def explain_temporal_complexity(
        self, time_complexity: str, max_loop_depth: int, recursive: bool
    ) -> str:
        prompt = f"""
            You are an expert computer science educator. Analyze the following time complexity result 
            and explain it clearly to a developer.

            ## Complexity Analysis Result
            - **Time Complexity**: {time_complexity}
            - **Max Loop Depth**: {max_loop_depth}
            - **Is Recursive**: {recursive}

            ## Your Task
            Explain in 2-3 short paragraphs:
            1. What {time_complexity} means in plain terms
            2. Why the code was classified with this notation based on the analysis details above
            3. What practical impact this has on performance (e.g. how it behaves with large inputs)

            ## Rules
            - Be direct and concise, no fluff
            - Use simple analogies when helpful
            - Avoid unnecessary jargon
            - Target audience: mid-level developer
        """

        response = await self.client.create_response(
            model="llama-3.3-70b-versatile", prompt=prompt
        )

        return self.client.first_content(response)
