# Web Narrator
A sandbox environment for experimenting with Claude AI and Elevenlabs that will describe a provided website.

### Prerequisites
- Anthropic account to have access to Claude API Key. Check out Anthropic API reference below.
- Elevenlabs account to have access to Elevenlabs voices. Check out Elevenlabs API reference below.

## Getting started

### Create .env file

Add the following to your .env file
```bash
ANTHROPIC_API_KEY=replace-with-your-public-key
ELEVENLABS_API_KEY=replace-with-your-public-key
```

### Install dependencies
```commandline
python3 -m pip install virtualenv
python3 -m virtualenv venv
source venv/bin/activate
```

Then, install the dependencies:
```
pip install -r requirements.txt
```


## Built With
* [Anthropic API][anthropiclink] - The AI used for script generation.
* [Elevenlabs][elevenlabslink] - The audio/speech generation used.
## Authors

* **Namae Conde** - *Initial work* - [namaeconde][githublink]

[githublink]: https://github.com/namaeconde
[anthropiclink]: https://docs.anthropic.com/claude/reference/getting-started-with-the-api
[elevenlabslink]: https://elevenlabs.io/docs/introduction