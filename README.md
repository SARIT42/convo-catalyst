# ConvoCatalyst : LinkedIn Insights & Ice-breakers
A LangChain powered LLM model that provides you a summary, interesting facts, topics of interest and an ice-breaker to help start a conversation with a person by scraping their LinkedIn profile (and Twitter profile ?).

## Working:
Getting Results for **Harrison Chase, founder & CEO - Langchain.**

### Input:

`name = "Harrison Chase"`

> Note: If the model scrapes the profile of another person with same name rather than the person you are looking for : Try providing a bit of unique detail into the name. For eg:
> 
> if "Harrison Chase" does not get you desired results , try something like "Harrison Chase LangChain" 

### Scraping and Prompt:

Given name of person, use lookup agent with the help of the tool `get_profile_url()` (SerpAPI) to find out the person's `linkedin_profile_url`.

Passing the `linkedin_profile_url` as the input down here to the `{information}` placeholder as prompt template to our langchain powered llm model.


```

    summary_template = """
        given the Linkedin information {information} about a person, i want you to create:
        1. a short summary
        2. an interesting fact about them
        3. A potential topic of interest. Keep it short.
        4. 1 creative ice-breaker to open a conversation with them.
        """
```


### Result: 

![image](https://github.com/SARIT42/convo-catalyst/assets/77446629/d140a89a-197c-4d1c-8d7d-a507c848b757)

The most interesting and mindblowing thing here is the demonstration of the thought process of the **agent** which basically acts as a brain to the model for the steps it needs to take to reach desired output. 

Also, the results seemed pretty convincing! LangChain is cool! 




## Run the Project

### Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`PYTHONPATH=/{YOUR_PATH_TO_PROJECT}/ice_breaker`

`OPENAI_API_KEY`

`PROXYCURL_API_KEY`

`SERPAPI_API_KEY`

`TWITTER_API_KEY`

`TWITTER_API_SECRET`

`TWITTER_ACCESS_TOKEN`

`TWITTER_ACCESS_SECRET`

[twitter scraping is not implemented now due to issues with twitter api, not allowing certain api calls in some countries/regions]


### Run Locally

Clone the project

```bash
  git clone https://github.com/SARIT42/convo-catalyst.git
```

Go to the project directory

```bash
  cd ice_breaker
```

Use a pipenv environment.

Install dependencies

```bash
  pipenv install
```

run the icebreaker.py file.

```bash
  pipenv run app.py
```


## Twitter Scraping.

Getting the following error:

`tweepy.errors.Forbidden: 403 Forbidden When authenticating requests to the Twitter API v2 endpoints, you must use keys and tokens from a Twitter developer App that is attached to a Project. You can create a project via the developer portal.`

which to my knowledge, as i figured out was because of some twitter api policy changes applicable to certain regions/countries. So nothing much can be done on the developer side ig. 

This halts the twitter account information scraping but the implementation code for the `twitter_lookup_agent` and the tweets processing in `twitter.py` has been provided in the respective sections. 

Any help in resolving the above issue is highly appreciated. 


