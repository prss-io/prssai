<p>
  
  <h1>prssai</h1>
  <blockquote>PRSS AI Companion. Research & Create articles for PRSS Site Creator</blockquote>

  ### 📦 Installation
  - Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
  - Install [Ollama](https://github.com/ollama/ollama)
  - `ollama pull dolphin-mistral:7b-v2.2.1` or [choose another model](https://ollama.com/) according to your system specs.
  - Clone this repository
  - Rename `example.env` to `.env` and edit accordingly.
  - Open a terminal in the `./bin` directory. and run `./install`.
  - Open another terminal in the same location and run your desired commands.

  ### ✳️ Commands

  #### article
  Generates an article based on the parameters set in your `.env` file.
  ```bash
  ./article [topic of your article]
  ```
  ![article2](https://github.com/prss-io/prssai/assets/25509135/38068568-1cda-481b-8ecb-35d1c98e43e4)

  #### prompt
  Ask any question to the model. Useful for asking follow-up questions about the article or revised sentences.
  ```bash
  ./prompt [your question]
  ```

  #### shell
  Enter the `sh` shell for the python container.
  ```bash
  ./shell
  ```

  #### flushdb
  Erases the model's memory about previous conversations and research.
  ```bash
  ./flushdb
  ```

  #### start
  Starts the docker containers (chrome, worker, redis).
  ```bash
  ./start
  ```

  #### restart
  Restarts the docker containers.
  ```bash
  ./restart
  ```

  #### stop
  Stops the docker containers.
  ```bash
  ./stop
  ```

  #### uninstall
  Uninstalls the docker containers.
  ```bash
  ./uninstall
  ```
</p>

<div align="right">
  <br />
  <p><a href="https://prss.io"><img src="https://i.imgur.com/5OQD7eL.png" width="130" /></a></p>
</div>
