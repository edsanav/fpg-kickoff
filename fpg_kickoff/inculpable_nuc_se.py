from typing import Dict


class Nuke:
    def __init__(self, config):
        self.config = config

    def launch(self):
        if self.config.get("safety_mechanism"):
            return "Safety mechanism is on! All good!"
        return """WHOOOOOOOOOOPS!
     _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____"""


def crazy_getter(config: Dict, key: str) -> str:
    return config.pop(key)


def main():
    super_secure_config = {
        "safety_mechanism": True,
        "sync_filters": {"target": {"select_all": True}},
        "other_stuff": True,
    }
    my_awesome_nuke = Nuke(super_secure_config)
    safety_mechanism = crazy_getter(super_secure_config, "safety_mechanism")
    if safety_mechanism:
        print("Safety mechanism is on, it's safe to execute nuke launch system...")
        print(my_awesome_nuke.launch())


if __name__ == "__main__":
    main()
