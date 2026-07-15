from basyx.aas import model
from basyx.aas.adapter import aasx


# create the AAS containing AssetInformation
asset_inforamtion = model.AssetInformation(
    asset_kind=model.AssetKind.TYPE,
    global_asset_id='https://www.afriso.com/de/produkte/haustechnik/leckanzeiger-leckueberwachungssysteme-und-leckschutzauskleidungen/zubehoer-ersatzteile-leckanzeiger-leckueberwachungssysteme-und-leckschutzauskleidungen/lag-14-er/40642-signalteil-lag-14-er'
)

# create the Asset AdministrationShell
identifier = 'url'
ass = model.AssetAdministrationShell(
    
    id_short=LAG14ER,
    display_name=[
        model.LangStringNameType(language="en", text="LAG14ER"),
        model.LangStringNameType(language="de", text="LAG14ER")
    ]
    
    #identifiable
    id_=
    discription= ,
    administartion= ,
    submodel= ,
    derived_from= ,
)


# create the Submodel object






print("AAS Environment exported")