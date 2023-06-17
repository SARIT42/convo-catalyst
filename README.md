# ConvoCatalyst : Linguistic Profile Scraper & Ice-breaker
A LangChain powered LLM model that provides you a summary, interesting facts, topics of interest and an ice-breaker to help start a conversation with a person by scraping their LinkedIn profile (and Twitter profile ?).

## Working:
Getting Results for **Harrison Chase, founder & CEO - Langchain.**

Prompt:



Result: 



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
