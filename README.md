<p align="center">
<img width="300" height="150" alt="Screenshot 2021-04-18 at 19 06 39" src="https://user-images.githubusercontent.com/78478073/120325661-2bebb180-c2e8-11eb-9a08-8ead7fc9b042.JPG">
</p>
  <p align="center">
    Generate Discord Nitro codes and check the validation
    <br />
    <a href="https://github.com/semmoolenschot/Discord-Nitro-generator"><strong>Explore»</strong></a
    <br />
      ·
      <a href="https://github.com/semmoolenschot/Discord-Nitro-Generator/releases/tag/1.0.1"><strong> Latest version»</strong></a>
    <br />
    <a href="https://github.com/semmoolenschot/Discord-Nitro-generator/issues">Report Bug</a>
    ·
    <a href="https://github.com/semmoolenschot/Discord-Nitro-generator/issues">Request Feature</a>
  

---

### Table of Contents
- [Description](#description)
- [How to use](#how-to-use)
- [Contact](#contact)
      
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#description">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#description">Description</a>
      <ul>
        <li><a href="#discord-nitro">Discord Nitro</a></li>
        <li><a href="#how-it-works">How it works</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>
      
|⠀| Original | 1.0.1 | 1.0.2 |
| --------- | ----- | ----- | ----- |
| **Generate** | ✅ | ✅ | ✅ |
| **Check** | ✅ | ✅ | ✅ |
| **Check & Generate at the same time** | ⠀ | ✅ | ✅ |
| **Auto claim (PATCHED)** | ⠀ | ❌ | ❌ |
| **Discord webhook** | ⠀ | ⠀ | ✅ |

- [Original](https://github.com/semmoolenschot/Discord-Nitro-Generator)
- [1.0.1](https://github.com/semmoolenschot/Discord-Nitro-Generator/releases/tag/1.0.1)
- [1.0.2](https://github.com/semmoolenschot/Discord-Nitro-Generator/releases/tag/1.0.2)

Don't forget to leave a star ⭐
      


# Description

### Discord Nitro

- Discord Nitro is the premium subscription tier on the most popular gaming chat service in the world. It comes with global access to custom emojis from all the channels you're part of, a custom Discord number tag, animated avatars, and server boosts for your favorite communities.

- Discord also has the option to gift the Nitro subscription. Once you paid you get a shareable link that will allow other users to claim the subscription. You simply provide this link to the person you want to give Nitro to.

- A Discord Nitro gift link will look like this for an example: *https://discord.com/gifts/drOs7uHeX8YcnyXtVMo* (19 digits)

- Keep in mind that all codes created by Discord will expire after 48 hours if they haven't been claimed yet.

### How it works

- It generates possible Nitro codes in a loop and checks their validation by using [requests](https://pypi.org/project/requests/) to get a response from ```https://discordapp.com/api/v6/entitlements/gift-codes/___________________?with_application=false&with_subscription_plan=true```. With that response we can see whether the code is valid or not. If the code is valid it will break the loop and send the code to a webhook (if given), but if it's invalid it will continue generating and checking.


<img width="572" alt="Screenshot 2021-04-18 at 19 06 39" src="https://user-images.githubusercontent.com/78478073/115154085-573c7900-a079-11eb-9c96-18ecddd5fffa.png">

### Features
- Generate possible Nitro codes
- Check the validation of the generated codes
- Send valid codes in a Discord webhook
- Automatically claim the valid code (**patched**)

### How to use
> Windows ⠀<img width="16" src="https://www.mijncomputerhulp.nl/wp-content/uploads/2019/05/microsoft-windows-22-logo-png-transparent.png">
      
      
- Run the ``main.py`` file using ``python3 main.py``
- Once done you will get a menu with multiple options such as *generate, check or reset*

- Also make sure to have all modules installed by using ``pip3 install -r requirements.txt``

- This is coded in **python 3.9** which you can download [here](https://www.python.org/downloads/)
      
> Mac ⠀<img width="16" src="https://image.flaticon.com/icons/png/512/2/2235.png"> ⠀/ ⠀Linux ⠀<img width="16" src="https://1000logos.net/wp-content/uploads/2017/03/LINUX-LOGO.png">

### Important
- **I'm not responsible for any type of damage thats been caused by using my code**

### Contact

- <img width="16" src="https://i.redd.it/5zec9qw4ppy61.png"> [sem#4744](https://discord.com/)
- <img width="16" src="https://www.monalisaelburg.nl/media/Bladzy/Productset/productset/image/1/g/i/github.jpg"> [Github](https://github.com/semmoolenschot)
- <img width="16" src="https://demaasdijk-events.nl/wp-content/uploads/2019/06/instagram-png-instagram-png-logo-1455.png"> [Instagram](https://instagram.com/semmoolenschot)

