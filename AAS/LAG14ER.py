from basyx.aas import model
from basyx.aas.adapter import aasx


# create the AAS containing AssetInformation
asset_inforamtion = model.AssetInformation(
    asset_kind=model.AssetKind.TYPE,
    global_asset_id='https://www.afriso.com/de/produkte/haustechnik/leckanzeiger-leckueberwachungssysteme-und-leckschutzauskleidungen/zubehoer-ersatzteile-leckanzeiger-leckueberwachungssysteme-und-leckschutzauskleidungen/lag-14-er/40642-signalteil-lag-14-er'
)

# create the Asset AdministrationShell
# TODO : model.MultiLanguageNameType() need english name?
ass = model.AssetAdministrationShell(
    asset_information=asset_inforamtion,
    id_short='LAG14ER',
    display_name=model.MultiLanguageNameType(
        {"en": "LAG14ER", "de": "LAG14ER"}
    ),
    id_='https://www.afriso.com/aas/LAG14ER',
    description=model.MultiLanguageTextType(
        {"de": "Steuergerät LAG-14 ER / Leckanzeiger"}
    ),
    administration=model.AdministrativeInformation(
        version='1',
        revision='0'
    ),
    submodel={
        model.ModelReference((model.Key(model.KeyTypes.SUBMODEL, 'https://www.afriso.com/submodel/nameplate/LAG14ER'),), model.Submodel),
        model.ModelReference((model.Key(model.KeyTypes.SUBMODEL, 'https://www.afriso.com/submodel/handover/LAG14ER'),), model.Submodel),
        model.ModelReference((model.Key(model.KeyTypes.SUBMODEL, 'https://www.afriso.com/submodel/techdata/LAG14ER'),), model.Submodel),
        model.ModelReference((model.Key(model.KeyTypes.SUBMODEL, 'https://www.afriso.com/submodel/carbon/LAG14ER'),), model.Submodel),
        model.ModelReference((model.Key(model.KeyTypes.SUBMODEL, 'https://www.afriso.com/submodel/maintenance/LAG14ER'),), model.Submodel),
    },
    derived_from=None,
)

# create the Submodel object






print("AAS Environment exported")