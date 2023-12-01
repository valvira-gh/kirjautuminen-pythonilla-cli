class Main:
    """ DOCSTRING Main-luokasta
    Tämä luokka vastaa sovelluksen käynnistämisestä ja keskeisten
    komponenttien hallinnasta. Se sisältää päämetodit sovelluksen
    toiminnan aloittamisesta, suorituksen ohjaamiseen ja tarvittaessa
    sovelluksen sulkemiseen.
    
    Ominaisuudet:
    -- attribute1: Selitys attribuutista
    -- attribute2:  Toisen attribuutin selitys.
    
    Metodit:
    -- run(): Käynnistää sovelluksen päätoiminnot.
    """
    
    def __int__(self):
        """"""
    
    def run(self):
        # Metodi, joka käynnistää sovelluksen päätoiminnalisuuden
        print("Sovellus käynnistyy.")
    
    def exit(self):
        pass


# Voit lisätä muita metodeja tarpeen mukaan

def main() -> object:
    main_instanssi = Main()
    main_instanssi.run()


if __name__ == '__main__':
    main()
