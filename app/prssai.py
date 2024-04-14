

import json
import hashlib
from colorist import Color, BgColor, BrightColor

class PRSSAI:
  def __init__(self, ollama, redis, browser, model, system_prompt, persist_memory, res_word_count, res_format, res_seo_keywords):
    self.command = None
    self.ollama = ollama
    self.redis = redis
    self.browser = browser
    self.model = model
    self.system_prompt = system_prompt
    self.persist_memory = persist_memory
    self.res_word_count=res_word_count,
    self.res_format=res_format,
    self.res_seo_keywords=res_seo_keywords

  def get_context(self) -> list[int]:
    ctx = self.redis.get('prssai_context')
    return json.loads(ctx) if ctx else []
  
  def set_context(self, ctx: list[int]):
    self.redis.set('prssai_context', json.dumps(ctx), ex=60 * 60 * 24 * 7)

    if self.persist_memory:
        self.redis.bgsave()
  
  def clear_context(self):
    self.redis.delete('prssai_context')

  def clear_db(self):
    self.echo("Memory", f"Okay. I've forgotten everything!")
    self.redis.flushdb()

  def get_command_memo(self) -> str:
    h = hashlib.new('sha1')
    h.update(self.command.encode())
    memo_id = h.hexdigest()
    memo = self.redis.get(f'command_{memo_id}')
    if memo:
      self.echo("Memory", f"Found research memo for this command: {memo_id}")
    return json.loads(memo) if memo else ""
  
  def set_command_memo(self, content: str):
    h = hashlib.new('sha1')
    h.update(self.command.encode())
    memo_id = h.hexdigest()
    self.echo("Memory", f"Saved command research memo as {memo_id}")
    self.redis.set(f'command_{memo_id}', json.dumps(content), ex=60 * 60 * 24 * 7)

    if self.persist_memory:
        self.redis.bgsave()

  def parse_content(self, content: str, remember: bool) -> str:
    file_content = ""
    if content.startswith("./"):
      with open(content, 'r') as file:
        file_content = file.read()
        self.echo("Loader", f"\"{content}\" is being remembered.")
        return f"Refer to this research in the future: {file_content}"
    elif remember:
      return f"Refer to this research in the future: {content}"
    else:
      self.echo("Prompt", content)
      return content

  def echo(self, action: str, content: str):
    prefix = f"\n{Color.YELLOW} ● prssai {Color.OFF}"
    action_output = ""
    if action == "Loader":
      action_output = f"{BgColor.GREEN}{Color.BLACK} {action} {Color.OFF}"
    if action == "Memory":
      action_output = f"{BgColor.GREEN}{Color.BLACK} {action} {Color.OFF}"
    else:
      action_output = f"{BgColor.CYAN}{Color.BLACK} {action} {Color.OFF}"

    print(f"{prefix}{action_output}{BgColor.OFF} {BrightColor.CYAN}{content}{BrightColor.OFF}\n")

  def generate(self, content, remember=False):
    prompt = self.parse_content(content, remember)
    ctx = self.get_context()
    response = self.ollama.generate(model=self.model, prompt=prompt, system=self.system_prompt, context=ctx)
    self.set_context(response['context'])
    print(response['response'])
    return response['response']
  
  def run(self, command):
    try:
      self.command = command

      # fetch existing research, if any
      if not self.get_command_memo():
        # research information about the subject
        research = self.browser.search(self.command)

        # save research in memory to prevent searching again
        self.set_command_memo(research)

        # talk to model about research
        self.generate(research, True)

      # generate prompt with desired output and constraints
      format = ''.join(self.res_format)
      word_count = ''.join(self.res_word_count)
      seo_keywords = self.res_seo_keywords
      self.generate(f"""
        Create a {format} on the following topic "{self.command}".
        The resulting text must have {word_count} words and start with a headline.
        Important: the text should also contain one of the following words: {seo_keywords}
      """)
    except Exception:
      self.redis.close()