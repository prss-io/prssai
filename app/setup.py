import ollama
import redis
import prssai
import browser
import dotenv

from os import environ

dotenv.load_dotenv()

ollama_scheme = environ.get("ollama_scheme")
ollama_host = environ.get("ollama_host")
ollama_port = environ.get("ollama_port")
ollama_model = environ.get("ollama_model")

redis_host = environ.get("redis_host")
redis_port = environ.get("redis_port")

chrome_host = environ.get("chrome_host")
chrome_port = environ.get("chrome_port")

system_prompt = environ.get("system_prompt")
search_follow_links = bool(environ.get("search_follow_links"))
persist_memory = bool(environ.get("persist_memory"))

res_word_count = environ.get("res_word_count")
res_format = environ.get("res_format")
res_seo_keywords = environ.get("res_seo_keywords")

client = prssai.PRSSAI(
  ollama=ollama.Client(host=f'{ollama_scheme}://{ollama_host}:{ollama_port}'),
  redis=redis.Redis(host=redis_host, port=redis_port, db=0, decode_responses=True),
  browser=browser.Browser(chrome_host=chrome_host, chrome_port=chrome_port, search_follow_links=search_follow_links),
  model=ollama_model,
  system_prompt=system_prompt,
  persist_memory=persist_memory,
  res_word_count=res_word_count,
  res_format=res_format,
  res_seo_keywords=res_seo_keywords
)