import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)
from astropy.io import fits
from astropy.io import ascii
from astropy.table import unique, Table, QTable
##____________________________________________________________________________##
## The allthatglitters software suite was written Summer 2020 by Joni Marie   ##
## Clark Cunningham to ID eclipsing binaries within the obervational overlap  ##
## of the Transiting Exoplanet Survey Satelite (TESS) and the Apache Point    ##
## Observatory Galactic Evolution Experiment (APOGEE) whom meet a number of   ##
## criteria, and are fit for analysis.                                        ##
##____________________________________________________________________________##
##      INPUT:  gold_sample of Price-Whelan (2020): a list composed of targets##
##              from APOGEE DR16  binary systems that have unimodal posterior ##
##              samplings (i.e. the MCMC used to generate posterior sampling  ##
##              completed successfully and converged), no other Gaia sources  ##
##              near the primary that could contaminate the spectra, and a    ##
##              primary star mass from STARHORSE catalog of stellar parameters##
##              The gold_sample and is located at                             ##
##                                           http://adrian.pw/apogee-dr16.html##
##      INPUT:  Alloy_Out.txt which is the output from Alloy.py which has     ##
##              matched RA and DEC arguments to TIC IDs in TESS sectors 1-27  ##
##              The 2 minute observations are over 27 sectors, retrieved from:##
##                             https://tess.mit.edu/observations/target-lists/##
print('______________________[GoldDigger, Platinum.py]_________________________')
print('Welcome to Platinum.py a program used to import APOGEEGold data from the')
print(' sample (Pricew-Whelan 2020) after having been matched with TESS objects')
print(' via positional arguments RA, DEC via [AstroQuery.py]. This way we have ')
print(' the rest of the gold sample parameters for the APOGEE DR16 binaries.   ')
print('____________________________________________________________________________')

##=[INPUT]=====================[APOGEE GOLD SAMPLE]===========================##
Alloy_Out = np.loadtxt('Smelt/Alloy_Out.txt', comments='#', usecols=(0,1,2), unpack=True)
Pt = []
i = 0                                            #Empty list for results
Gold = Table.read('Dig/Ore/gold_sample.fits')    #Astropy reads  FITS file in as Table
colnames = ['APOGEE_ID', 'n_visits', 'APSTAR_ID', 'ASPCAP_ID', 'RA', 'DEC',
'FE_H', 'GAIA_SOURCE_ID', 'GAIA_PARALLAX', 'GAIA_PARALLAX_ERROR', 'GAIA_PMRA',
'GAIA_PMRA_ERROR', 'GAIA_PMDEC', 'GAIA_PMDEC_ERROR', 'GAIA_RADIAL_VELOCITY',
'GAIA_RADIAL_VELOCITY_ERROR',  'mass', 'mass_err']
def RoseGold(table, key_colnames):               #Defines APGold Sample
    colnames = ['APOGEE_ID', 'n_visits', 'APSTAR_ID', 'ASPCAP_ID', 'RA', 'DEC',
    'FE_H', 'GAIA_SOURCE_ID', 'GAIA_PARALLAX', 'GAIA_PARALLAX_ERROR', 'GAIA_PMRA',
    'GAIA_PMRA_ERROR', 'GAIA_PMDEC', 'GAIA_PMDEC_ERROR', 'GAIA_RADIAL_VELOCITY',
    'GAIA_RADIAL_VELOCITY_ERROR',  'mass', 'mass_err']
    for i, line in enumerate(Alloy_Out):
        if np.any(Gold['RA']) == np.any(Alloy_Out[1]) and np.any(Gold['DEC']) == np.any(Alloy_Out[2]):
            print('match located at line', i)
        i=i+1
RoseGold(Gold, colnames)
