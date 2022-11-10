from msilib.schema import LaunchCondition
import random

def randomword(original):
    randomised = ''.join(random.sample(original, len(original)))
    print(randomised)
    return original
randomword("spaghetti bolognese")
randomword("meervoudigepersoonlijkheidsstoornissen")
randomword("arbeidsongeschiktheidsverzekeringsmaatschappij")
