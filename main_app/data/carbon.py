
def get_carbon_value_old():
    return {
            "Transport routier: Véhicules à essence": 2.307,
            "Transport aérien: AvGas": 2.365,
            "Électricité": 0.22,
            "Chauffage": 1.54,
            "Viandes fraîches et congelées: Boeuf": 32.5,
            "Poulet": 7,
            "Poisson élevé": 13,
            "Laits et oeufs": 1.6,
            "Fromage": 13,
            "Fruits et Légumes": 1.1,
            "Produits céréaliers: Blé tendre": 0.655,
            "Boissons alcoolisées": 1.7,
            "Autres boissons et tabac": 0.8,
            "Papier": 0.919,
            "Produits chimiques": 11
    }
def get_carbon_value():
    carbon_emission_dict = {
        # Transport et voyage
        "Transport routier: Véhicules à essence": 2.307,
        "Transport aérien": 1.92,
        "Pièces de véhicules automobiles": 1.25,
        "Hôtels": 0.833,
        # Services alimentaires
        "Viandes fraîches et congelées: Boeuf": 32.5,
        "Poulet et oeufs": 2.3,
        "Fruits et légumes": 4.63,
        "Produits laitiers": 3.83,
        "Produits de boulangerie congelés": 1.48,
        "Restauration": 0.86,
        "Chocolat et Cacao": 1.74,
        "Café torréfié": 2.67,
        "Boissons alcoolisées": 1.7,
        "Autres boissons et tabac": 0.8,
        "Nourriture pour chiens et chats": 2.08,
        # Services individuels et à domicile
        "Services bancaires": 0.295,
        "Collèges, universités": 0.326,
        "Docteurs et dentistes": 0.187,
        "Services électriques": 10.3,
        "Raccords de plomberie": 0.929,
        # Services d'achat commercial
        "Commerce de détails": 0.48,
        "Textile fabriqué": 0.955,
        "Chaussures sauf caoutchouc": 1.65,
        "Meubles de maison": 1.35,
        "Mine de plomb et art": 1.27,
        "Instruments musicaux": 0.527,
        "Autres électroniques": 0.752,
        # Soin personnel
        "Mise en forme physique": 0.746,
        "Salon de beauté et barbier": 0.527,
        "Savon et autres": 1.12
    }
    return carbon_emission_dict

def get_categories_lists():
    categories_lists_dict = {
        # Transport et voyage
        "Transport routier: Véhicules à essence": "https://www.pagesjaunes.ca/search/si/1/Stations-services/Quebec+QC",
        "Transport aérien": "https://fr.wikipedia.org/wiki/Liste_des_a%C3%A9roports_internationaux_au_Canada",
        "Pièces de véhicules automobiles": "https://www.pagesjaunes.ca/search/si/1/Accessoires+et+pi%C3%A8ces+d%27autos+neuves/Quebec+QC",
        "Hôtels": "https://en.wikipedia.org/wiki/List_of_hotels_in_Canada",
        # Services alimentaires
        "Viandes fraîches et congelées: Boeuf": "https://www.pagesjaunes.ca/search/si/1/Boucheries/Montr%C3%A9al%2C%20QC",
        "Poulet et oeufs": "https://www.pagesjaunes.ca/search/si/1/Poulet%20Et%20Oeufs/Montr%C3%A9al,%20QC",
        "Fruits et légumes": "https://www.pagesjaunes.ca/search/si/1/Magasins+de+fruits+et+l%C3%A9gumes/Montreal+QC",
        "Produits laitiers": "https://www.pagesjaunes.ca/search/si/1/produits%20laitiers/Montreal%20QC",
        "Produits de boulangerie congelés": "https://www.pagesjaunes.ca/search/si/1/Produits%20de%20boulangerie%20congel%C3%A9s/Montreal%20QC",
        "Restauration": "https://www.pagesjaunes.ca/search/si/1/restaurants/Quebec+QC",
        "Chocolat et Cacao": "https://www.pagesjaunes.ca/search/si/1/Chocolat%20et%20Cacao/Montreal%20QC",
        "Café torréfié": "https://www.pagesjaunes.ca/search/si/1/Caf%C3%A9s/Montr%C3%A9al,%20QC",
        "Boissons alcoolisées": "https://en.wikipedia.org/wiki/List_of_breweries_in_Quebec",
        "Autres boissons et tabac": "https://www.pagesjaunes.ca/search/si/1/D%C3%A9panneurs/Montreal+QC",
        "Nourriture pour chiens et chats": "https://www.pagesjaunes.ca/search/si/1/nourriture%20pour%20chien%20et%20chat/Montreal%20QC",
        # Services individuels et à domicile
        "Services bancaires": "https://www.pagesjaunes.ca/search/si/1/Banques/Montreal+QC",
        "Collèges, universités": "https://www.pagesjaunes.ca/search/si/1/coll%C3%A8ges%20et%20universit%C3%A9s/Montreal%20QC",
        "Docteurs et dentistes": "https://www.pagesjaunes.ca/search/si/1/Docteurs%20et%20dentistes/Montreal%20QC",
        "Services électriques": "https://www.pagesjaunes.ca/search/si/1/Services%20%C3%A9lectriques/Montreal%20QC",
        "Raccords de plomberie": "https://www.pagesjaunes.ca/search/si/1/Raccords%20de%20plomberie/Montreal%20QC",
        # Services d'achat commercial
        "Commerce de détails": "https://www.pagesjaunes.ca/search/si/1/Commerce%20de%20d%C3%A9tails/Quebec%20QC",
        "Textile fabriqué": "https://www.pagesjaunes.ca/search/si/1/magasins%20de%20v%C3%AAtements/Montr%C3%A9al,%20QC",
        "Chaussures sauf caoutchouc": "https://www.pagesjaunes.ca/search/si/1/magasins%20de%20chaussures/Montr%C3%A9al,%20QC",
        "Meubles de maison": "https://www.pagesjaunes.ca/search/si/1/Meubles%20de%20maison/Montr%C3%A9al,%20QC",
        "Mine de plomb et art": "https://www.pagesjaunes.ca/search/si/1/magasins%20d'art/Montr%C3%A9al,%20QC",
        "Instruments musicaux": "https://www.pagesjaunes.ca/search/si/1/Magasins+d%27instruments+de+musique/Montreal+QC",
        "Autres électroniques": "https://www.pagesjaunes.ca/search/si/1/Magasins%20d'%C3%A9lectroniques/Montreal%20QC",
        # Soin personnel
        "Mise en forme physique": "https://www.pagesjaunes.ca/search/si/1/salle%20de%20sport/Montr%C3%A9al,%20QC",
        "Salon de beauté et barbier": "https://www.pagesjaunes.ca/search/si/1/coiffeur%20barbier/Montr%C3%A9al,%20QC",
        "Savon et autres": "https://www.pagesjaunes.ca/search/si/1/savon%20et%20autre/Montr%C3%A9al,%20QC"
    }
    return categories_lists_dict