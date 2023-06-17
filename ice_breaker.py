# gives us a template for prompts

from langchain import PromptTemplate
# chat models can be said (as of now) as large llm models to leverage our job
from langchain.chat_models import ChatOpenAI
# LLMChain provide us chains feature.Chains basically allow us to combine different components to create a coherent app.
from langchain.chains import LLMChain


from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent


# DEBUG NOTE FOR SELF: openai account free credits 5$, enough. if model unble to progress check.
# also, 3 rpm
# 4000 tpm


def ice_break(name: str):
    summary_template = """
        given the Linkedin information {information} about a person, i want you to create:
        1. a short summary
        2. an interesting fact about them
        3. A potential topic of interest. keep it short.
        4. 1 creative ice-breaker to open a conversation with them.
        """

    summary_prompt_template = PromptTemplate(input_variables=["information"],
                                             template=summary_template)

    llm = ChatOpenAI(temperature=1, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_profile_url = linkedin_lookup_agent(name=name)

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)

    result = chain.run(information=linkedin_data)

    print(result)


if __name__ == '__main__':
    ice_break(name="Harrison Chase")
    pass

    # print(scrape_user_tweets(username="sarit_rath42"))

# tweepy.errors.Forbidden: 403 Forbidden When authenticating requests to the Twitter API v2 endpoints, you must use
# keys and tokens from a Twitter developer App that is attached to a Project. You can create a project via the
# developer portal.


