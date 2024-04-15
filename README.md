<p>
  <img src="https://github.com/prss-io/prssai/assets/25509135/e2eca5d6-27c3-4c72-9e50-d1843e8e909a" width="200" />
  <blockquote>PRSS AI Companion. Research & Create articles for <a href="https://github.com/hodgef/PRSS">PRSS Site Creator</a>.</blockquote>

  ### 📦 Setup
  - Install [Docker Desktop](https://www.docker.com/products/docker-desktop/) and [Ollama](https://github.com/ollama/ollama)
  - Install [PRSS Site Creator](https://prss.io/) (for GUI management and enhanced features)
  - `ollama pull dolphin-mistral:7b-v2.2.1` or [choose another model](https://ollama.com/) according to your preference.
  - Clone this repository
  - Rename `example.env` to `.env` and edit accordingly.

  ### ✳️ Usage in PRSS
  _Coming soon!_

  ### ✴️ Usage in Terminal
  To run the following commands, you must do so from the `./bin` directory after running `./install` at that location.

  #### article
  Generates an article based on the parameters set in your `.env` file.
  ```bash
  ./article [topic of your article]
  ```
  ![article2](https://github.com/prss-io/prssai/assets/25509135/38068568-1cda-481b-8ecb-35d1c98e43e4)

  This command can also load text files as reference. Path is relative to the container, so use the `./app/files` directory for this feature.

  ![article3](https://github.com/prss-io/prssai/assets/25509135/00102a4d-d5d1-4fed-a014-e7286a0a7d08)



  #### prompt
  Ask any question to the model. Useful for asking follow-up questions about the article or revised sentences.
  ```bash
  ./prompt [your question]
  ```
  ![articleb](https://github.com/prss-io/prssai/assets/25509135/d2c92652-7514-46a8-a103-57c2fda5baee)



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
  <p><a href="https://prss.io"><img src="https://github.com/prss-io/prssai/assets/25509135/a0f1a975-50a0-4d2f-962c-3d5b462fe091" width="130" /></a></p>
</div>
