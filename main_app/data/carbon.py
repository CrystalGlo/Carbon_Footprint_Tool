# main_app.data.carbon.py
#
# File used to store data about carbon foot print for individual category
#
# Information in this file are not 100% accurate. Estimated by the guardian https://www.theguardian.com/environment/green-living-blog/2010/nov/12/carbon-footprint-spending-pound
#
#
#
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
#the guardian values
def get_carbon_value():
    return {
            "Professional services": 0.160,
            "Car payment": 0.720,
            "Supermarket": 0.930,
            "Gas station": 1.7,
            "Travel": 4.7,
            "Electricity": 0.22,
            "Bar": 1.7
    }