# Discord Nitro Generator

### Table of Contents
- [Description](#description)
- [How to use](#how-to-use)
- [Contact](#contact)

---

## Description

#### Nitro

- Discord Nitro is the premium subscription tier on the most popular gaming chat service in the world. It comes with global access to custom emojis from all the channels you're part of, a custom **Discord** number tag, animated avatars, and server boosts for your favorite communities.

- Discord also has the option to gift the Nitro subscription. Once you paid you get a shareable link that will allow other users to claim the subscription. You simply provide this link to the person you want to give Nitro to.

- A Discord Nitro gift link will look like this for an example: *https://discord.com/gifts/drOs7uHeX8YcnyXtVMo* (19 digits)

- Keep in mind that all codes created by Discord will expire after 48 hours if they haven't been claimed yet.

#### Technologies

- Using the tool you can create tons of 19 digit codes that will be put in *codes.txt*
- After creating all the codes it will combind them into a URL and check if they're valid using the Discord API. (bruteforce)

It will stop checking once it finds a valid code in *codes.txt*

---

## How to use

Run the ``main.py`` file using ``python3 main.py``
Once done you will get a menu with multiple options such as *generate, check or reset*

Also make sure to have all modules installed by using ``pip3 install -r requirements.txt``

---

See the [open issues](https://github.com/semmoolenschot/Discord-Nitro-generator/issues) for a list of proposed features (and known issues).

