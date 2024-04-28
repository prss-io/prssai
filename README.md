<p>
  <a href="https://prss.io"><img src="https://github.com/prss-io/prssai/assets/25509135/e2eca5d6-27c3-4c72-9e50-d1843e8e909a" width="200" /></a>
  <blockquote>PRSS AI Companion & Autoblogger. Research & Create articles for <a href="https://github.com/hodgef/PRSS" target="_blank">PRSS Site Creator</a>.</blockquote>

  ### 📦 Setup
  - Install <a href="https://www.docker.com/products/docker-desktop/" target="_blank">Docker Desktop</a> and <a href="https://github.com/ollama/ollama" target="_blank">Ollama</a>
  - Install <a href="https://prss.io/" target="_blank">PRSS Site Creator</a> (for GUI management and enhanced features)
  - `ollama pull dolphin-mistral:7b-v2.2.1` or <a href="https://github.com/ollama/ollama?tab=readme-ov-file#model-library" target="_blank">choose another model</a> according to your preference.
  - Clone this repository
  - Rename <a href="https://github.com/prss-io/prssai/blob/master/app/example.env" target="_blank">`./app/example.env`</a> to `./app/.env` and edit accordingly.
  - Open a terminal and run `./install` from the `./bin` directory.

  ### ✳️ Usage in PRSS
  > The prssai features have been introduced as of PRSS version 1.9.0. To enable it, install it from the PRSS "Addons" page.
  
  #### Batch generate articles (autoblogging)
  Specify a number of topics for the AI to write about. Once complete, you will be able to review the returned text, discard entries, and transform the remaining texts to blog posts in one click.

  ![image](https://github.com/prss-io/prssai/assets/25509135/da990026-cc5b-4550-a1e2-40e6683a3660)
  
  ![image](https://github.com/prss-io/prssai/assets/25509135/ab1fe1ce-6d1c-4e38-8273-72234a4e6854)

  #### Prompt

  Ask the model anything. It will have memory of the previous conversations and articles generated. To forget the history, prompt it with "erase history". The memory is stored locally in the [`prssai_redis` container](https://github.com/prss-io/prssai/blob/master/docker-compose.yml#L12).

  ![image](https://github.com/prss-io/prssai/assets/25509135/886f85a9-e60e-4315-b921-7ad7716ed52c)

  ### ✴️ Usage in Terminal
  To run the following commands, you must do so from the `./bin` directory after setup.

  #### article
  Generates an article based on the parameters set in your `./app/.env` file.
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
