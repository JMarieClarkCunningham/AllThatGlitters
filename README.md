##  [                           AllThatGlitters                            ]  ##
## The AllThatGlitters Repository contains the software suite GoldDigger:     ##
##    Written by Joni Marie Clark Cunningham in Summer of 2020 to cross match ##    
##    the APOGEE Gold sample to TESS Sectors and arrive at a final TESS/APOGEE## 
##    overlap containing well characterized binaries for analysis presented   ##
##    in Cunningham et al. (2020b).                                           ##

##  [                     AllThatGlitters > GoldDigger                     ]  ##
##  [                         Dig > Panning_Gold.py                        ]  ##
## 
##      INPUT:  gold_sample of Price-Whelan (2020): a list composed of targets##
##              from APOGEE DR16  binary systems that have unimodal posterior ##
##              samplings (i.e. the MCMC used to generate posterior sampling  ##
##              completed successfully and converged), no other Gaia sources  ##
##              near the primary that could contaminate the spectra, and a    ##
##              primary star mass from STARHORSE catalog of stellar parameters##
##              The gold sample is located at                                 ##
##                                           http://adrian.pw/apogee-dr16.html##
##      OUTPUT: sample containing 980 APOGETESSGold (H<14,T< 14,n_visit>3) is ##
##              cross referenced to the TESS Sectors to determine which may   ##
##              have 2 minute cadence observations, and thus, light curves!   ##
##              The 2 minute observations are over 27 sectors, retrieved from:##
##                             https://tess.mit.edu/observations/target-lists/##

##  [                         Smelt > AstroQuery.py                        ]  ##
 
##      INPUT:  sample containing 980 APOGETESSGold (H<14,T< 14,n_visit>3) out##
##              from Panning_Gold.py. This should contain RA, Dec, of systems ##
##              for the positional argument cross matching through the MAST   ##
##              portal. Requires: astroquery.mast > Catalogs                  ##
##                  https://astroquery.readthedocs.io/en/latest/mast/mast.html##
##      OUTPUT: sample containing all matches from the MAST query and position##
##              arguments [RA, DEC]. It is important to know that this OUTPUT ##
##              may have more rows than your INPUT, as duplicate observations ##
##              are possible in overlapping fields of view like TESS, and if  ##
##              there is more than one positional argument match corresponding##
##              to different observations (i.e. target is in a crowded part of##
##              the sky from the telescope's field of view) to mitigate, the  ##
##              brightest H band luminosity target is selected, and matched   ##
##              with the same H band luminosity recorded in the APOGEE gold.  ##

##  [                            Ingots > Platinum.py                       ] ##

##  [IN PROGRESS]: Final phase of GoldDigger software suite, used to          ##         
##                 statistically evaluate the final overlap sample, collect   ##
##                 relevant datas from multiple files, catalogs, portals.     ##
##      INPUT:  sample containing the overlap between Telescopes and Surveys  ##
##              with positional arguments, identifiers, which is then used to ##
##              query, retireve, and plot photometric (and maybe IR spectra   ##
##              soon too, though that may be a sub module) obeservations.     ##
##      OUTPUT: light curves! spectra! maybe someday RV curves - WOW!         ##
