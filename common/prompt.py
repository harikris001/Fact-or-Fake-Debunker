import pathway as pw
from datetime import datetime
from common.openaiapi_helper import openai_chat_completion


def prompt(index, embedded_query, user_query):

    @pw.udf
    def build_prompt(local_indexed_data, query):
        docs_str = "\n".join(local_indexed_data)
        print(docs_str)
        prompt = f"This is True information: \n {docs_str} \n and check whether the query below is *Fact* or *Fake* based on true info. Keep the style similar to the enthusiastic and engaging manner often seen in shows like 'You Have Been Warned' or 'Outrageous Acts of Science.' Always say final verdict first, i.e whether query is FACT or FAKE. Always answer in maximum 10 sentences. Query is: {query}"
        return prompt
    
    query_context = embedded_query + index.get_nearest_items(embedded_query.vector, k=3, collapse_rows=True).select(local_indexed_data_list=pw.this.chunk).promise_universe_is_equal_to(embedded_query)



    prompt = query_context.select(
        prompt=build_prompt(pw.this.local_indexed_data_list, user_query)
    )

    return prompt.select(
        query_id=pw.this.id,
        result=openai_chat_completion(pw.this.prompt),
    )
