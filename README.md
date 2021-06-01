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

<details open="open">
  <summary>Table of Contents</summary>
  </li>
    <li><a href="#description">Description</a>
    <li><a href="#discord-nitro">Discord Nitro</a></li>
    <li><a href="#how-it-works">How it works</a></li>
    </li>
    <li><a href="#features">Features</a></li>
    <li><a href="#python">Python version</a></li>
    <li><a href="#important">Disclaimer</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

### Versions
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

Please check out [versions](#versions) for more information/updates on features

### How to use
> Windows ⠀<img width="16" src="https://www.mijncomputerhulp.nl/wp-content/uploads/2019/05/microsoft-windows-22-logo-png-transparent.png">

- Open your command prompt
- Change directories to the downloaded folder
- Make sure to have all modules installed by using ``pip install -r requirements.txt``
- Run the ``main.py`` file by doing ``python main.py``
      
> Mac ⠀<img width="16" src="https://image.flaticon.com/icons/png/512/2/2235.png"> / Linux ⠀<img width="16" src="https://user-images.githubusercontent.com/78478073/120348722-bab6f900-c2fd-11eb-818d-24a576875768.png">
      
- Open your terminal
- Change directories to the downloaded folder
- Make sure to have all modules installed by using ``pip3 install -r requirements.txt``
- Run the ``main.py`` file by doing ``python3 main.py``

### Python
- This is coded in **python 3.9** which you can download [here](https://www.python.org/downloads/)

### Disclaimer

```diff
- I'm not responsible for any type of damage thats been caused by using my code
- This has been made for educational purposes and not to harm Discord or their users
- Use this at your own risk
```

### Contact

- <img width="16" src="https://i.redd.it/5zec9qw4ppy61.png"> [sem#4744](https://discord.com/)
- <img width="16" src="https://www.monalisaelburg.nl/media/Bladzy/Productset/productset/image/1/g/i/github.jpg"> [Github](https://github.com/semmoolenschot)
- <img width="16" src="https://demaasdijk-events.nl/wp-content/uploads/2019/06/instagram-png-instagram-png-logo-1455.png"> [Instagram](https://instagram.com/semmoolenschot)

