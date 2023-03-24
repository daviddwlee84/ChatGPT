import arxiv
from FreeGptApi import FreeGPT

api = FreeGPT()


def summarize_top_query(query: str, result_count: int = 3):
    search = arxiv.Search(
        query=query,
        max_results=result_count,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    prompts = []

    for i, result in enumerate(search.results()):
        prompts.append(f'Paper {i + 1}.')
        prompts.append(result.title)
        prompts.append(result.summary)
        prompts.append('')

    prompts.append(
        f'Please give short summarize for each of the above papers:')
    prompt = '\n'.join(prompts)

    print(prompt)
    # import ipdb
    # ipdb.set_trace()

    return api.simple_call(prompt)


if __name__ == '__main__':
    print(summarize_top_query('prompt'))
