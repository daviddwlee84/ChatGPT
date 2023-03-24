from typing import Callable, Any
import requests
import time


class FreeGPT():
    def __init__(self, endpoint='https://chatgpt-api.shn.hk/v1/') -> None:
        self.endpoint = endpoint

    def call(self, query: str, model: str = 'gpt-3.5-turbo') -> dict:
        """
        'List three best activities to do in Bali'
        {'id': 'chatcmpl-6xSZPzvK3G3TvqmTPFKEQc5T0yPvJ', 'object': 'chat.completion', 'created': 1679629195, 'model': 'gpt-3.5-turbo-0301', 'usage': {'prompt_tokens': 16, 'completion_tokens': 185, 'total_tokens': 201}, 'choices': [{'message': {'role': 'assistant', 'content': '1. Visit Uluwatu Temple and watch the Kecak Dance at sunset. This iconic Balinese temple is located on a cliff overlooking the Indian Ocean and is known for its stunning sunsets. The Kecak Dance is a traditional Balinese dance performance that takes place in the temple courtyard.\n\n2. Take a full-day tour of the rice terraces and water temples. Bali is famous for its beautiful rice terraces, and you can take a tour of them to learn about rice farming in Bali. The Tirta Empul temple is also a must-visit, as it is a Hindu water temple where locals go to purify themselves.\n\n3. Swim with Manta Rays. Bali is home to a variety of marine life, including Manta Rays. You can take a day trip to Nusa Penida Island to swim with these magnificent creatures. This experience is definitely a once in a lifetime opportunity.'}, 'finish_reason': 'stop', 'index': 0}]}

        TODO: multi-turn conversation
        """

        # https://www.geeksforgeeks.org/python-requests-post-request-with-headers-and-body/

        header = {
            "Content-Type": "application/json"
        }

        data = {
            'model': model,
            'messages': [{
                'role': 'user',
                'content': query
            }]
        }

        response = requests.post(self.endpoint, headers=header, json=data)

        if response.status_code != 200:
            print('Failed to request the API')
            return {}

        return response.json()

    def simple_call(self, query: str, model: str = 'gpt-3.5-turbo') -> str:
        response = self.call(query, model)
        # TODO: maybe more than 1 choices?!
        return response['choices'][0]['message']['content']


def latency_wrapper(func: Callable[[Any], Any], *args, **kwargs):
    """
    https://stackoverflow.com/questions/51697368/how-to-measure-latency-of-a-python-script
    https://realpython.com/python-kwargs-and-args/
    """
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()
    print('Latency:', end - start, 'sec')
    return result


if __name__ == '__main__':
    api = FreeGPT()
    response = latency_wrapper(
        api.call, 'List three best activities to do in Bali')
    print(response)
    result = latency_wrapper(
        api.simple_call, 'Simply explain the Wilson Score calculation.')
    print(result)

    import ipdb
    ipdb.set_trace()
