<p align=center>
  <img src="https://github.com/betty2310/jp2enAi/blob/main/assets/logo.png?raw=true" width="150" />
</p>
<p align=center>
  <b>Make wjbu great again!</b>
</p>
<p align=center>
  <a href="https://github.com/betty2310/jp2enAi/wiki"><img alt="wiki" src="https://img.shields.io/badge/doc-reference-blue"></a>
  <a href="https://github.com/betty2310/jp2enAi/blob/master/LICENSE"><img alt="license" src="https://img.shields.io/badge/license-MIT-green.svg"></a>
  <a href="https://github.com/betty2310/FOMATEM/search?l=python"><img alt="language" src="https://img.shields.io/badge/language-python-orange.svg"></a>
</p>

------
# Installation 

Run the following commands to install the dependencies and run the app. 

> **Note**
>  You may need to type `python3/pip3` instead of `python/pip` depending on your setup.

```bash
git clone https://github.com/betty2310/jp2enAi
cd jp2enAi
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

Create your own `.env` file by copying the `.env.example` file.

```bash
cp .env.example .env
```

After that, copy your secret [OpenAI API](https://beta.openai.com/account/api-keys) key and set it as the `OPENAI_API_KEY` in your newly created `.env` file.

Run the web app by:
```python 
flask run
```
Congratualtion, open http://localhost:5000 in your browser 🎊!


# Usage

![](./assets/web.png)

In web, just type keywork you need, press `generate!` and done 🚀.

# Limitations

# Disclaimers
This is not an official OpenAI product. This is a personal project and is not affiliated with OpenAI in any way. Don't sue me.

# Credits
+ This wouldn't be possible without OpenAI's [ChatGPT](https://chat.openai.com/chat) 🔥
+ Project inspired by [stackexplain](https://github.com/shobrook/stackexplain).

# License

MIT © [Betty](https://github.com/betty2310)

If you found this project interesting, please consider following me on [twitter](https://twitter.com/_betty2310)
