
# Pokemon Game

Welcome to the Pokemon Battle Game, a project developed during my participation in the Code First Girls Python & App course. This Python-based game allows you to engage in battles with the computer using Pokemon stats. You have the option to choose your own Pokemon or have the computer generate a random one for you. The winner is determined by the higher Pokemon stat, and the scores are recorded for each round based on your specified number of rounds.


## How to Play

1. Clone this repository to your local machine.
2. Open the file PokemonGame.py in your preferred Python IDE.
3. Run the file in your IDE.
4. Follow the prompts in the console to select your Pokémon or let the computer generate a random one.
5. Once both Pokémon have been selected, the game will commence.
6. Choose your Pokémon stat, and the winner is determined by the higher stat.
7. The game will continue for as many rounds as you specify, with each round's winner recorded.
8. After all rounds have been played, the final scores will be displayed.




## Pokemon API Reference

#### Get Random Pokemon

```http
  https://pokeapi.co/api/v2/pokemon/{random_id}/

```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `random_id` | `integer` | A random ID between 1 and 151 for a Pokémon. |

#### Get Pokemon by Name or ID

```http
  https://pokeapi.co/api/v2/pokemon/{name_or_id}/

```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name_or_id`      | `string` | Name or ID of the desired Pokémon. |

#### Note

Both endpoints return detailed information about a Pokémon, including its name, ID, height, weight, attack, and speed stats.

Ensure a stable internet connection while using these endpoints, as they rely on the PokeAPI.