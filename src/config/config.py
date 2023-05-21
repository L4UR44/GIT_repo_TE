imoprt os


class Config():

    @classmethod
    def get_property(name):        
    
        # def enviroment
        target = os.environ.get('TARGET', Config.DEFAULT_ENV)
        # target = os.environ['TARGET']

        # read the proper json file
        path_to_config = f"./env_config/{target}.json"
        with open(path_to_config) as f:
            config_from_json = json.load(f)

        # get the proerty name from parameter 'name
        value = config_from_json.get(name)

        return value