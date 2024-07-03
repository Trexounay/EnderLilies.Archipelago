from typing import Dict, Tuple
from worlds.generic.Rules import CollectionRule, ItemRule
from .Names import names as el

def get_rules(p : int) -> Tuple[Dict[str, CollectionRule], Dict[str, ItemRule]]: 

	macros : Dict[str, CollectionRule] = {
#		               djump + silva + champion
		'3LEDGE'      : lambda s : s.has(el['djump'], p) and s.has(el['silva'], p) and s.has(el['champion'], p),
#		               djump + silva | djump + champion | silva + champion
		'2LEDGE'      : lambda s : s.has(el['djump'], p) and s.has(el['silva'], p) or s.has(el['djump'], p) and s.has(el['champion'], p) or s.has(el['silva'], p) and s.has(el['champion'], p),
#		               djump | silva | champion
		'LEDGE'       : lambda s : s.has(el['djump'], p) or s.has(el['silva'], p) or s.has(el['champion'], p),
#		               dodge + sinner
		'2HORIZONTAL' : lambda s : s.has(el['dodge'], p) and s.has(el['sinner'], p),
#		               dodge | sinner
		'HORIZONTAL'  : lambda s : s.has(el['dodge'], p) or s.has(el['sinner'], p),
#		               silva + djump + dodge
		'FULLSILVA'   : lambda s : s.has(el['silva'], p) and s.has(el['djump'], p) and s.has(el['dodge'], p),
#		               pierce + dash
		'CHARGE'      : lambda s : s.has(el['pierce'], p) and s.has(el['dash'], p),
#		               heal1 + heal2 + heal3
		'3HEAL'       : lambda s : s.has(el['heal1'], p) and s.has(el['heal2'], p) and s.has(el['heal3'], p),
	}

	locations_rules : Dict[str, CollectionRule] = {
#		                                                        Abyss01Top
		"The Abyss 01 - Silva's Blight-Stained Note 1"         : lambda s : s.can_reach(el['Abyss01Top'], 'Region', p),
#		                                                        Abyss01Bottom
		"The Abyss 01 - Furious Blight x100"                   : lambda s : s.can_reach(el['Abyss01Bottom'], 'Region', p),
#		                                                        Abyss01Top
		"The Abyss 01 To Verboten Domain 18"                   : lambda s : s.can_reach(el['Abyss01Top'], 'Region', p),
#		                                                        Abyss01Bottom | Abyss01Top + CHARGE + slam + swim + (2HORIZONTAL + LEDGE | FULLSILVA | 3LEDGE | silva + (dodge | djump) | champion + djump | claw + HORIZONTAL + LEDGE) + (hook | FULLSILVA | 3LEDGE | 2HORIZONTAL + LEDGE)
		"The Abyss 01 To The Abyss 02"                         : lambda s : s.can_reach(el['Abyss01Bottom'], 'Region', p) or s.can_reach(el['Abyss01Top'], 'Region', p) and macros['CHARGE'](s) and s.has(el['slam'], p) and s.has(el['swim'], p) and (macros['2HORIZONTAL'](s) and macros['LEDGE'](s) or macros['FULLSILVA'](s) or macros['3LEDGE'](s) or s.has(el['silva'], p) and (s.has(el['dodge'], p) or s.has(el['djump'], p)) or s.has(el['champion'], p) and s.has(el['djump'], p) or s.has(el['claw'], p) and macros['HORIZONTAL'](s) and macros['LEDGE'](s)) and (s.has(el['hook'], p) or macros['FULLSILVA'](s) or macros['3LEDGE'](s) or macros['2HORIZONTAL'](s) and macros['LEDGE'](s)),
#		                                                        Abyss02Top + claw + (2LEDGE | 2LEDGE + HORIZONTAL | 2HORIZONTAL + LEDGE | dodge + dash + LEDGE)
		"The Abyss 02 - Amulet Fragment"                       : lambda s : s.can_reach(el['Abyss02Top'], 'Region', p) and s.has(el['claw'], p) and (macros['2LEDGE'](s) or macros['2LEDGE'](s) and macros['HORIZONTAL'](s) or macros['2HORIZONTAL'](s) and macros['LEDGE'](s) or s.has(el['dodge'], p) and s.has(el['dash'], p) and macros['LEDGE'](s)),
#		                                                        Abyss02Top
		"The Abyss 02 - Silva's Blight-Stained Note 2"         : lambda s : s.can_reach(el['Abyss02Top'], 'Region', p),
#		                                                        Abyss02Top
		"The Abyss 02 - Fretia's Memoirs 5"                    : lambda s : s.can_reach(el['Abyss02Top'], 'Region', p),
#		                                                        Abyss02Top
		"The Abyss 02 - White Priestess' Earrings"             : lambda s : s.can_reach(el['Abyss02Top'], 'Region', p),
#		                                                        Abyss02Right | Abyss02Top
		"The Abyss 02 To The Abyss 03"                         : lambda s : s.can_reach(el['Abyss02Right'], 'Region', p) or s.can_reach(el['Abyss02Top'], 'Region', p),
#		                                                        Abyss02Top | Abyss02Right
		"The Abyss 02 To The Abyss 01"                         : lambda s : s.can_reach(el['Abyss02Top'], 'Region', p) or s.can_reach(el['Abyss02Right'], 'Region', p),
#		                                                        Abyss03Left
		"The Abyss 03 To The Abyss 02"                         : lambda s : s.can_reach(el['Abyss03Left'], 'Region', p),
#		                                                        Abyss04Top + mask + slam + hook + 3HEAL + dash
		"The Abyss 04 - Upper Stagnant Blight x100"            : lambda s : s.can_reach(el['Abyss04Top'], 'Region', p) and s.has(el['mask'], p) and s.has(el['slam'], p) and s.has(el['hook'], p) and macros['3HEAL'](s) and s.has(el['dash'], p),
#		                                                        Abyss04Top + mask + slam + hook + 3HEAL + dash
		"The Abyss 04 - Lower Stagnant Blight x100"            : lambda s : s.can_reach(el['Abyss04Top'], 'Region', p) and s.has(el['mask'], p) and s.has(el['slam'], p) and s.has(el['hook'], p) and macros['3HEAL'](s) and s.has(el['dash'], p),
#		                                                        Abyss04Top
		"The Abyss 04 To Verboten Domain 12"                   : lambda s : s.can_reach(el['Abyss04Top'], 'Region', p),
#		                                                        Abyss04Bottom | Abyss04Top + mask + swim + slam + hook + 3HEAL + dash
		"The Abyss 04 To The Abyss 05"                         : lambda s : s.can_reach(el['Abyss04Bottom'], 'Region', p) or s.can_reach(el['Abyss04Top'], 'Region', p) and s.has(el['mask'], p) and s.has(el['swim'], p) and s.has(el['slam'], p) and s.has(el['hook'], p) and macros['3HEAL'](s) and s.has(el['dash'], p),
#		                                                        Abyss05Top + swim
		"The Abyss 05 - Stone Tablet Fragment"                 : lambda s : s.can_reach(el['Abyss05Top'], 'Region', p) and s.has(el['swim'], p),
#		                                                        Abyss05Top + swim
		"The Abyss 05 - The Deathless Pact"                    : lambda s : s.can_reach(el['Abyss05Top'], 'Region', p) and s.has(el['swim'], p),
#		                                                        Abyss05Top + swim
		"The Abyss 05 To Verboten Domain 12"                   : lambda s : s.can_reach(el['Abyss05Top'], 'Region', p) and s.has(el['swim'], p),
#		                                                        Abyss05Top + swim
		"The Abyss 05 - Ancient Soul x2"                       : lambda s : s.can_reach(el['Abyss05Top'], 'Region', p) and s.has(el['swim'], p),
#		                                                        Abyss05Top
		"The Abyss 05 To The Abyss 04"                         : lambda s : s.can_reach(el['Abyss05Top'], 'Region', p),
#		                                                        Castle01Left | Castle01Right1 | Castle01Top | Castle01Right2
		"Ruined Castle 01 - Castle Town Maiden"                : lambda s : s.can_reach(el['Castle01Left'], 'Region', p) or s.can_reach(el['Castle01Right1'], 'Region', p) or s.can_reach(el['Castle01Top'], 'Region', p) or s.can_reach(el['Castle01Right2'], 'Region', p),
#		                                                        Castle01Right2 + (LEDGE | HORIZONTAL)
		"Ruined Castle 01 - Priestess' Doll"                   : lambda s : s.can_reach(el['Castle01Right2'], 'Region', p) and (macros['LEDGE'](s) or macros['HORIZONTAL'](s)),
#		                                                        Castle01Right1 | Castle01Top
		"Ruined Castle 01 - Decayed Crown"                     : lambda s : s.can_reach(el['Castle01Right1'], 'Region', p) or s.can_reach(el['Castle01Top'], 'Region', p),
#		                                                        Dog + CHARGE
		"Ruined Castle 01 - Stagnant Blight x100"              : lambda s : s.can_reach(el['Dog'], 'Location', p) and macros['CHARGE'](s),
#		                                                        Dog + CHARGE
		"Ruined Castle 01 - Furious Blight x100"               : lambda s : s.can_reach(el['Dog'], 'Location', p) and macros['CHARGE'](s),
#		                                                        Castle01Left | Dog
		"Ruined Castle 01 To Cliffside Hamlet 11"              : lambda s : s.can_reach(el['Castle01Left'], 'Region', p) or s.can_reach(el['Dog'], 'Location', p),
#		                                                        Castle01Right2 | Dog + (HORIZONTAL | LEDGE | dash)
		"Ruined Castle 01 To Ruined Castle 02 Lower"           : lambda s : s.can_reach(el['Castle01Right2'], 'Region', p) or s.can_reach(el['Dog'], 'Location', p) and (macros['HORIZONTAL'](s) or macros['LEDGE'](s) or s.has(el['dash'], p)),
#		                                                        Castle01Right1 | Castle01Top
		"Ruined Castle 01 To Ruined Castle 02 Upper"           : lambda s : s.can_reach(el['Castle01Right1'], 'Region', p) or s.can_reach(el['Castle01Top'], 'Region', p),
#		                                                        Castle01Right1 + claw
		"Ruined Castle 01 To Ruined Castle 10"                 : lambda s : s.can_reach(el['Castle01Right1'], 'Region', p) and s.has(el['claw'], p),
#		                                                        Castle02Top
		"Ruined Castle 02 - Amulet Fragment"                   : lambda s : s.can_reach(el['Castle02Top'], 'Region', p),
#		                                                        Castle02Top | Castle02Left2 + (hook | LEDGE | claw)
		"Ruined Castle 02 To Ruined Castle 05"                 : lambda s : s.can_reach(el['Castle02Top'], 'Region', p) or s.can_reach(el['Castle02Left2'], 'Region', p) and (s.has(el['hook'], p) or macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                        Castle02Top + hook
		"Ruined Castle 02 - Stagnant Blight x30"               : lambda s : s.can_reach(el['Castle02Top'], 'Region', p) and s.has(el['hook'], p),
#		                                                        Castle02Left2 | Castle02Left1 | Castle02Top | Castle02Bottom
		"Ruined Castle 02 To Ruined Castle 01 Lower"           : lambda s : s.can_reach(el['Castle02Left2'], 'Region', p) or s.can_reach(el['Castle02Left1'], 'Region', p) or s.can_reach(el['Castle02Top'], 'Region', p) or s.can_reach(el['Castle02Bottom'], 'Region', p),
#		                                                        Castle02Bottom | Castle02Left2
		"Ruined Castle 02 To Ruined Castle 04"                 : lambda s : s.can_reach(el['Castle02Bottom'], 'Region', p) or s.can_reach(el['Castle02Left2'], 'Region', p),
#		                                                        Castle02Left1 | Castle02Left2 + (claw + (djump | champion))
		"Ruined Castle 02 To Ruined Castle 01 Upper"           : lambda s : s.can_reach(el['Castle02Left1'], 'Region', p) or s.can_reach(el['Castle02Left2'], 'Region', p) and (s.has(el['claw'], p) and (s.has(el['djump'], p) or s.has(el['champion'], p))),
#		                                                        (Castle03Top1 | Castle03Top2) + (hook | claw | HORIZONTAL | dash | LEDGE)
		"Ruined Castle 03 - Amulet Fragment"                   : lambda s : (s.can_reach(el['Castle03Top1'], 'Region', p) or s.can_reach(el['Castle03Top2'], 'Region', p)) and (s.has(el['hook'], p) or s.has(el['claw'], p) or macros['HORIZONTAL'](s) or s.has(el['dash'], p) or macros['LEDGE'](s)),
#		                                                        (Castle03Top1 | Castle03Top2) + (hook | claw | LEDGE + HORIZONTAL)
		"Ruined Castle 03 - Stagnant Blight x30"               : lambda s : (s.can_reach(el['Castle03Top1'], 'Region', p) or s.can_reach(el['Castle03Top2'], 'Region', p)) and (s.has(el['hook'], p) or s.has(el['claw'], p) or macros['LEDGE'](s) and macros['HORIZONTAL'](s)),
#		                                                        Castle03Bottom | Castle03Top1 | Castle03Top2
		"Ruined Castle 03 To Ruined Castle 05"                 : lambda s : s.can_reach(el['Castle03Bottom'], 'Region', p) or s.can_reach(el['Castle03Top1'], 'Region', p) or s.can_reach(el['Castle03Top2'], 'Region', p),
#		                                                        (Castle03Top1 + claw + HORIZONTAL + 2LEDGE) | (Castle03Bottom + claw + (2HORIZONTAL + 2LEDGE | HORIZONTAL + 3LEDGE))
		"Ruined Castle 03 To Ruined Castle 11 Left"            : lambda s : (s.can_reach(el['Castle03Top1'], 'Region', p) and s.has(el['claw'], p) and macros['HORIZONTAL'](s) and macros['2LEDGE'](s)) or (s.can_reach(el['Castle03Bottom'], 'Region', p) and s.has(el['claw'], p) and (macros['2HORIZONTAL'](s) and macros['2LEDGE'](s)) and (macros['HORIZONTAL'](s) and macros['3LEDGE'](s))),
#		                                                        (Castle03Top2 + claw + HORIZONTAL + 2LEDGE) | (Castle03Bottom + claw + (2HORIZONTAL + 2LEDGE | HORIZONTAL + 3LEDGE))
		"Ruined Castle 03 To Ruined Castle 11 Right"           : lambda s : (s.can_reach(el['Castle03Top2'], 'Region', p) and s.has(el['claw'], p) and macros['HORIZONTAL'](s) and macros['2LEDGE'](s)) or (s.can_reach(el['Castle03Bottom'], 'Region', p) and s.has(el['claw'], p) and (macros['2HORIZONTAL'](s) and macros['2LEDGE'](s)) and (macros['HORIZONTAL'](s) and macros['3LEDGE'](s))),
#		                                                        Castle04Top
		"Ruined Castle 04 - Report from a Verboten Mage"       : lambda s : s.can_reach(el['Castle04Top'], 'Region', p),
#		                                                        Castle04Top | RuinedCastleCellar + (LEDGE | claw)
		"Ruined Castle 04 To Ruined Castle 02"                 : lambda s : s.can_reach(el['Castle04Top'], 'Region', p) or s.can_reach(el['RuinedCastleCellar'], 'Location', p) and (macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                        Castle05Bottom | Castle05Right | Castle05Left | Castle05Top
		"Ruined Castle 05 To Ruined Castle 02"                 : lambda s : s.can_reach(el['Castle05Bottom'], 'Region', p) or s.can_reach(el['Castle05Right'], 'Region', p) or s.can_reach(el['Castle05Left'], 'Region', p) or s.can_reach(el['Castle05Top'], 'Region', p),
#		                                                        Castle05Right | Castle05Bottom
		"Ruined Castle 05 To Ruined Castle 06"                 : lambda s : s.can_reach(el['Castle05Right'], 'Region', p) or s.can_reach(el['Castle05Bottom'], 'Region', p),
#		                                                        Castle05Left | Castle05Bottom
		"Ruined Castle 05 To Ruined Castle 08"                 : lambda s : s.can_reach(el['Castle05Left'], 'Region', p) or s.can_reach(el['Castle05Bottom'], 'Region', p),
#		                                                        Castle05Top
		"Ruined Castle 05 To Ruined Castle 03"                 : lambda s : s.can_reach(el['Castle05Top'], 'Region', p),
#		                                                        Castle06Top
		"Ruined Castle 06 - Royal Aegis Crest"                 : lambda s : s.can_reach(el['Castle06Top'], 'Region', p),
#		                                                        Castle06Top | Castle06Right
		"Ruined Castle 06 To Ruined Castle 12"                 : lambda s : s.can_reach(el['Castle06Top'], 'Region', p) or s.can_reach(el['Castle06Right'], 'Region', p),
#		                                                        Castle06Right | Castle06Top | Castle06Left
		"Ruined Castle 06 To Ruined Castle 07"                 : lambda s : s.can_reach(el['Castle06Right'], 'Region', p) or s.can_reach(el['Castle06Top'], 'Region', p) or s.can_reach(el['Castle06Left'], 'Region', p),
#		                                                        Castle06Right + claw
		"Ruined Castle 06 - Stagnant Blight x30"               : lambda s : s.can_reach(el['Castle06Right'], 'Region', p) and s.has(el['claw'], p),
#		                                                        Castle06Left | Castle06Top
		"Ruined Castle 06 To Ruined Castle 05"                 : lambda s : s.can_reach(el['Castle06Left'], 'Region', p) or s.can_reach(el['Castle06Top'], 'Region', p),
#		                                                        Castle07Right | Castle07Left
		"Ruined Castle 07 - Proof of Founding"                 : lambda s : s.can_reach(el['Castle07Right'], 'Region', p) or s.can_reach(el['Castle07Left'], 'Region', p),
#		                                                        Castle07Right | GuestChamber + (hook | 3LEDGE)
		"Ruined Castle 07 To Twin Spires 01"                   : lambda s : s.can_reach(el['Castle07Right'], 'Region', p) or s.can_reach(el['GuestChamber'], 'Location', p) and (s.has(el['hook'], p) or macros['3LEDGE'](s)),
#		                                                        Castle07Left | GuestChamber
		"Ruined Castle 07 To Ruined Castle 06"                 : lambda s : s.can_reach(el['Castle07Left'], 'Region', p) or s.can_reach(el['GuestChamber'], 'Location', p),
#		                                                        Castle08Top + claw + (LEDGE | HORIZONTAL)
		"Ruined Castle 08 - Chain of Sorcery"                  : lambda s : s.can_reach(el['Castle08Top'], 'Region', p) and s.has(el['claw'], p) and (macros['LEDGE'](s) or macros['HORIZONTAL'](s)),
#		                                                        Castle08Top
		"Ruined Castle 08 - Blightwreathed Blade"              : lambda s : s.can_reach(el['Castle08Top'], 'Region', p),
#		                                                        Castle08Top
		"Ruined Castle 08 - Stagnant Blight x10"               : lambda s : s.can_reach(el['Castle08Top'], 'Region', p),
#		                                                        Castle08Top
		"Ruined Castle 08 - Upper Stagnant Blight x10"         : lambda s : s.can_reach(el['Castle08Top'], 'Region', p),
#		                                                        Castle08Right
		"Ruined Castle 08 - Lower Stagnant Blight x10"         : lambda s : s.can_reach(el['Castle08Right'], 'Region', p),
#		                                                        Castle08Right | Castle08Top
		"Ruined Castle 08 To Ruined Castle 05"                 : lambda s : s.can_reach(el['Castle08Right'], 'Region', p) or s.can_reach(el['Castle08Top'], 'Region', p),
#		                                                        Castle08Top | Castle08Right + (claw | LEDGE | HORIZONTAL)
		"Ruined Castle 08 To Ruined Castle 09"                 : lambda s : s.can_reach(el['Castle08Top'], 'Region', p) or s.can_reach(el['Castle08Right'], 'Region', p) and (s.has(el['claw'], p) or macros['LEDGE'](s) or macros['HORIZONTAL'](s)),
#		                                                        Castle09Left + (2HORIZONTAL | claw + (2LEDGE | LEDGE + HORIZONTAL) | FULLSILVA | LEDGE + sinner | djump + dash + (silva | dodge))
		"Ruined Castle 09 - Furious Blight x30"                : lambda s : s.can_reach(el['Castle09Left'], 'Region', p) and (macros['2HORIZONTAL'](s) or s.has(el['claw'], p) and (macros['2LEDGE'](s) or macros['LEDGE'](s) and macros['HORIZONTAL'](s)) or macros['FULLSILVA'](s) or macros['LEDGE'](s) and s.has(el['sinner'], p) or s.has(el['djump'], p) and s.has(el['dash'], p) and (s.has(el['silva'], p) or s.has(el['dodge'], p))),
#		                                                        Castle09Right | Castle09Bottom
		"Ruined Castle 09 To Ruined Castle 11"                 : lambda s : s.can_reach(el['Castle09Right'], 'Region', p) or s.can_reach(el['Castle09Bottom'], 'Region', p),
#		                                                        Castle09Bottom | Castle09Right | Castle09Left
		"Ruined Castle 09 To Ruined Castle 08"                 : lambda s : s.can_reach(el['Castle09Bottom'], 'Region', p) or s.can_reach(el['Castle09Right'], 'Region', p) or s.can_reach(el['Castle09Left'], 'Region', p),
#		                                                        Castle09Left | Castle09Bottom
		"Ruined Castle 09 To Ruined Castle 10"                 : lambda s : s.can_reach(el['Castle09Left'], 'Region', p) or s.can_reach(el['Castle09Bottom'], 'Region', p),
#		                                                        Castle10Right | Castle10Bottom
		"Ruined Castle 10 - Julius' Book"                      : lambda s : s.can_reach(el['Castle10Right'], 'Region', p) or s.can_reach(el['Castle10Bottom'], 'Region', p),
#		                                                        MaelstromRemparts
		"Ruined Castle 10 - Stagnant Blight x30"               : lambda s : s.can_reach(el['MaelstromRemparts'], 'Location', p),
#		                                                        MaelstromRemparts
		"Ruined Castle 10 To Ruined Castle 09"                 : lambda s : s.can_reach(el['MaelstromRemparts'], 'Location', p),
#		                                                        MaelstromRemparts
		"Ruined Castle 10 To Ruined Castle 01"                 : lambda s : s.can_reach(el['MaelstromRemparts'], 'Location', p),
#		                                                        Castle11Right | Castle11Bottom2
		"Ruined Castle 11 To Ruined Castle 12"                 : lambda s : s.can_reach(el['Castle11Right'], 'Region', p) or s.can_reach(el['Castle11Bottom2'], 'Region', p),
#		                                                        Castle11Left | Castle11Bottom1
		"Ruined Castle 11 To Ruined Castle 09"                 : lambda s : s.can_reach(el['Castle11Left'], 'Region', p) or s.can_reach(el['Castle11Bottom1'], 'Region', p),
#		                                                        Castle11Top | Castle11Left + Castle11Right + LEDGE
		"Ruined Castle 11 To Ruined Castle 13"                 : lambda s : s.can_reach(el['Castle11Top'], 'Region', p) or s.can_reach(el['Castle11Left'], 'Region', p) and s.can_reach(el['Castle11Right'], 'Region', p) and macros['LEDGE'](s),
#		                                                        Castle11Bottom1 | Castle11Left
		"Ruined Castle 11 To Ruined Castle 03 Left"            : lambda s : s.can_reach(el['Castle11Bottom1'], 'Region', p) or s.can_reach(el['Castle11Left'], 'Region', p),
#		                                                        Castle11Bottom2 | Castle11Right
		"Ruined Castle 11 To Ruined Castle 03 Right"           : lambda s : s.can_reach(el['Castle11Bottom2'], 'Region', p) or s.can_reach(el['Castle11Right'], 'Region', p),
#		                                                        Castle12Bottom + (hook | (3LEDGE + claw + dodge))
		"Ruined Castle 12 - Chain of Sorcery"                  : lambda s : s.can_reach(el['Castle12Bottom'], 'Region', p) and (s.has(el['hook'], p) or (macros['3LEDGE'](s) and s.has(el['claw'], p) and s.has(el['dodge'], p))),
#		                                                        Castle12Bottom
		"Ruined Castle 12 - King of the First Age's Diary 1"   : lambda s : s.can_reach(el['Castle12Bottom'], 'Region', p),
#		                                                        Castle12Bottom
		"Ruined Castle 12 - King of the First Age's Diary 2"   : lambda s : s.can_reach(el['Castle12Bottom'], 'Region', p),
#		                                                        Castle12Bottom | Castle12Left + (hook + (claw | LEDGE | HORIZONTAL) | slam)
		"Ruined Castle 12 To Ruined Castle 06"                 : lambda s : s.can_reach(el['Castle12Bottom'], 'Region', p) or s.can_reach(el['Castle12Left'], 'Region', p) and (s.has(el['hook'], p) and (s.has(el['claw'], p) or macros['LEDGE'](s) or macros['HORIZONTAL'](s)) or s.has(el['slam'], p)),
#		                                                        Castle12Bottom + (hook | claw | HORIZONTAL)
		"Ruined Castle 12 - Stagnant Blight x30"               : lambda s : s.can_reach(el['Castle12Bottom'], 'Region', p) and (s.has(el['hook'], p) or s.has(el['claw'], p) or macros['HORIZONTAL'](s)),
#		                                                        Castle12Left | Castle12Bottom
		"Ruined Castle 12 To Ruined Castle 11"                 : lambda s : s.can_reach(el['Castle12Left'], 'Region', p) or s.can_reach(el['Castle12Bottom'], 'Region', p),
#		                                                        Castle12Right | Castle12Bottom + unlock
		"Ruined Castle 12 To Ruined Castle 21"                 : lambda s : s.can_reach(el['Castle12Right'], 'Region', p) or s.can_reach(el['Castle12Bottom'], 'Region', p) and s.has(el['unlock'], p),
#		                                                        Castle13Bottom + (silva + djump + claw | (FULLSILVA | 3LEDGE) + hook | 2LEDGE + hook + claw | LEDGE + HORIZONTAL + claw + hook)
		"Ruined Castle 13 - Amulet Gem"                        : lambda s : s.can_reach(el['Castle13Bottom'], 'Region', p) and (s.has(el['silva'], p) and s.has(el['djump'], p) and s.has(el['claw'], p) or (macros['FULLSILVA'](s) or macros['3LEDGE'](s)) and s.has(el['hook'], p) or macros['2LEDGE'](s) and s.has(el['hook'], p) and s.has(el['claw'], p) or macros['LEDGE'](s) and macros['HORIZONTAL'](s) and s.has(el['claw'], p) and s.has(el['hook'], p)),
#		                                                        Castle13Left | Castle13Bottom
		"Ruined Castle 13 To Ruined Castle 17"                 : lambda s : s.can_reach(el['Castle13Left'], 'Region', p) or s.can_reach(el['Castle13Bottom'], 'Region', p),
#		                                                        Castle13Bottom | Castle13Left | Castle13Right
		"Ruined Castle 13 To Ruined Castle 11"                 : lambda s : s.can_reach(el['Castle13Bottom'], 'Region', p) or s.can_reach(el['Castle13Left'], 'Region', p) or s.can_reach(el['Castle13Right'], 'Region', p),
#		                                                        Castle13Right | Castle13Bottom
		"Ruined Castle 13 To Ruined Castle 14"                 : lambda s : s.can_reach(el['Castle13Right'], 'Region', p) or s.can_reach(el['Castle13Bottom'], 'Region', p),
#		                                                        Castle14Left + hook
		"Ruined Castle 14 - Amulet Fragment"                   : lambda s : s.can_reach(el['Castle14Left'], 'Region', p) and s.has(el['hook'], p),
#		                                                        Castle14Left + CHARGE + (claw | LEDGE + HORIZONTAL)
		"Ruined Castle 14 - Stagnant Blight x100"              : lambda s : s.can_reach(el['Castle14Left'], 'Region', p) and macros['CHARGE'](s) and (s.has(el['claw'], p) or macros['LEDGE'](s) and macros['HORIZONTAL'](s)),
#		                                                        Castle14Left + (claw + (3LEDGE | FULLSILVA | sinner + 2LEDGE | silva + 2HORIZONTAL | dodge + dash + 2LEDGE))
		"Ruined Castle 14 - Furious Blight x800"               : lambda s : s.can_reach(el['Castle14Left'], 'Region', p) and (s.has(el['claw'], p) and (macros['3LEDGE'](s) or macros['FULLSILVA'](s) or s.has(el['sinner'], p) and macros['2LEDGE'](s) or s.has(el['silva'], p) and macros['2HORIZONTAL'](s) or s.has(el['dodge'], p) and s.has(el['dash'], p) and macros['2LEDGE'](s))),
#		                                                        Castle14Left | Castle14Top
		"Ruined Castle 14 To Ruined Castle 13"                 : lambda s : s.can_reach(el['Castle14Left'], 'Region', p) or s.can_reach(el['Castle14Top'], 'Region', p),
#		                                                        Castle14Top | Castle14Left + (LEDGE | hook)
		"Ruined Castle 14 To Ruined Castle 15"                 : lambda s : s.can_reach(el['Castle14Top'], 'Region', p) or s.can_reach(el['Castle14Left'], 'Region', p) and (macros['LEDGE'](s) or s.has(el['hook'], p)),
#		                                                        TowerAlcove
		"Ruined Castle 15 - Priestess' Wish"                   : lambda s : s.can_reach(el['TowerAlcove'], 'Location', p),
#		                                                        Castle15Bottom | Castle15Left
		"Ruined Castle 15 - Priestess' Castle Memo"            : lambda s : s.can_reach(el['Castle15Bottom'], 'Region', p) or s.can_reach(el['Castle15Left'], 'Region', p),
#		                                                        TowerAlcove + claw + (hook | FULLSILVA + sinner | 3LEDGE)
		"Ruined Castle 15 To Ruined Castle 16"                 : lambda s : s.can_reach(el['TowerAlcove'], 'Location', p) and s.has(el['claw'], p) and (s.has(el['hook'], p) or macros['FULLSILVA'](s) and s.has(el['sinner'], p) or macros['3LEDGE'](s)),
#		                                                        Castle15Bottom | TowerAlcove
		"Ruined Castle 15 To Ruined Castle 14"                 : lambda s : s.can_reach(el['Castle15Bottom'], 'Region', p) or s.can_reach(el['TowerAlcove'], 'Location', p),
#		                                                        Castle16Right
		"Ruined Castle 16 - One-Eyed Royal Aegis"              : lambda s : s.can_reach(el['Castle16Right'], 'Region', p),
#		                                                        Aegis
		"Ruined Castle 16 - 2nd Stagnant Blight x10"           : lambda s : s.can_reach(el['Aegis'], 'Location', p),
#		                                                        Aegis
		"Ruined Castle 16 - 5th Stagnant Blight x10"           : lambda s : s.can_reach(el['Aegis'], 'Location', p),
#		                                                        Aegis
		"Ruined Castle 16 - 9th Stagnant Blight x10"           : lambda s : s.can_reach(el['Aegis'], 'Location', p),
#		                                                        Aegis
		"Ruined Castle 16 - 1st Stagnant Blight x10"           : lambda s : s.can_reach(el['Aegis'], 'Location', p),
#		                                                        Aegis
		"Ruined Castle 16 - 8th Stagnant Blight x10"           : lambda s : s.can_reach(el['Aegis'], 'Location', p),
#		                                                        Aegis
		"Ruined Castle 16 - 3rd Stagnant Blight x10"           : lambda s : s.can_reach(el['Aegis'], 'Location', p),
#		                                                        Aegis
		"Ruined Castle 16 - 7th Stagnant Blight x10"           : lambda s : s.can_reach(el['Aegis'], 'Location', p),
#		                                                        Aegis
		"Ruined Castle 16 - 6th Stagnant Blight x10"           : lambda s : s.can_reach(el['Aegis'], 'Location', p),
#		                                                        Aegis
		"Ruined Castle 16 - 4th Stagnant Blight x10"           : lambda s : s.can_reach(el['Aegis'], 'Location', p),
#		                                                        Aegis + claw
		"Ruined Castle 16 - 10th Stagnant Blight x10"          : lambda s : s.can_reach(el['Aegis'], 'Location', p) and s.has(el['claw'], p),
#		                                                        Castle17Top | Aegis
		"Ruined Castle 16 To Ruined Castle 18"                 : lambda s : s.can_reach(el['Castle17Top'], 'Region', p) or s.can_reach(el['Aegis'], 'Location', p),
#		                                                        Castle16Right | Aegis + (2LEDGE | claw)
		"Ruined Castle 16 To Ruined Castle 15"                 : lambda s : s.can_reach(el['Castle16Right'], 'Region', p) or s.can_reach(el['Aegis'], 'Location', p) and (macros['2LEDGE'](s) or s.has(el['claw'], p)),
#		                                                        Castle17Right + (LEDGE | claw)
		"Ruined Castle 17 - Stagnant Blight x30"               : lambda s : s.can_reach(el['Castle17Right'], 'Region', p) and (macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                        Castle17Right
		"Ruined Castle 17 To Ruined Castle 13"                 : lambda s : s.can_reach(el['Castle17Right'], 'Region', p),
#		                                                        Castle17Right + LEDGE
		"Ruined Castle 17 To Ruined Castle 18"                 : lambda s : s.can_reach(el['Castle17Right'], 'Region', p) and macros['LEDGE'](s),
#		                                                        Castle18Right + CHARGE
		"Ruined Castle 18 - Amulet Fragment"                   : lambda s : s.can_reach(el['Castle18Right'], 'Region', p) and macros['CHARGE'](s),
#		                                                        Castle18Bottom + (claw | hook + LEDGE) + CHARGE
		"Ruined Castle 18 - King's Note 2"                     : lambda s : s.can_reach(el['Castle18Bottom'], 'Region', p) and (s.has(el['claw'], p) or s.has(el['hook'], p) and macros['LEDGE'](s)) and macros['CHARGE'](s),
#		                                                        Castle18Bottom + (claw | hook + LEDGE) + CHARGE
		"Ruined Castle 18 - Eldred's Ring"                     : lambda s : s.can_reach(el['Castle18Bottom'], 'Region', p) and (s.has(el['claw'], p) or s.has(el['hook'], p) and macros['LEDGE'](s)) and macros['CHARGE'](s),
#		                                                        Castle18Bottom + hook + LEDGE + CHARGE
		"Ruined Castle 18 - Furious Blight x100"               : lambda s : s.can_reach(el['Castle18Bottom'], 'Region', p) and s.has(el['hook'], p) and macros['LEDGE'](s) and macros['CHARGE'](s),
#		                                                        Castle18Right | Castle18Bottom + (claw | hook + LEDGE)
		"Ruined Castle 18 To Ruined Castle 19"                 : lambda s : s.can_reach(el['Castle18Right'], 'Region', p) or s.can_reach(el['Castle18Bottom'], 'Region', p) and (s.has(el['claw'], p) or s.has(el['hook'], p) and macros['LEDGE'](s)),
#		                                                        Castle18Bottom | Castle18Right + (claw | hook + LEDGE) | Castle18Top
		"Ruined Castle 18 To Ruined Castle 17"                 : lambda s : s.can_reach(el['Castle18Bottom'], 'Region', p) or s.can_reach(el['Castle18Right'], 'Region', p) and (s.has(el['claw'], p) or s.has(el['hook'], p) and macros['LEDGE'](s)) or s.can_reach(el['Castle18Top'], 'Region', p),
#		                                                        Castle19Right | Castle19Left
		"Ruined Castle 19 - King's Note 1"                     : lambda s : s.can_reach(el['Castle19Right'], 'Region', p) or s.can_reach(el['Castle19Left'], 'Region', p),
#		                                                        KingsChamber
		"Ruined Castle 19 To Ruined Castle 20"                 : lambda s : s.can_reach(el['KingsChamber'], 'Location', p),
#		                                                        KingsChamber
		"Ruined Castle 19 To Ruined Castle 18"                 : lambda s : s.can_reach(el['KingsChamber'], 'Location', p),
#		                                                        Castle20Left
		"Ruined Castle 20 - Knight Captain Julius"             : lambda s : s.can_reach(el['Castle20Left'], 'Region', p),
#		                                                        Julius
		"Ruined Castle 20 To Ruined Castle 19"                 : lambda s : s.can_reach(el['Julius'], 'Location', p),
#		                                                        Castle21Left
		"Ruined Castle 21 - King of the First Age's Diary 3"   : lambda s : s.can_reach(el['Castle21Left'], 'Region', p),
#		                                                        Castle21Left
		"Ruined Castle 21 - Stone Tablet Fragment"             : lambda s : s.can_reach(el['Castle21Left'], 'Region', p),
#		                                                        Castle21Left
		"Ruined Castle 21 To Ruined Castle 12"                 : lambda s : s.can_reach(el['Castle21Left'], 'Region', p),
#		                                                        Castle21Left
		"Ruined Castle 21 - Stagnant Blight x100"              : lambda s : s.can_reach(el['Castle21Left'], 'Region', p),
#		                                                        Cave01Bottom | Cave01Left
		"Catacombs 01 - Fretia's Ring"                         : lambda s : s.can_reach(el['Cave01Bottom'], 'Region', p) or s.can_reach(el['Cave01Left'], 'Region', p),
#		                                                        Cave01Bottom + (claw | djump | champion | silva + dodge)  | Cave01Left + 3LEDGE + 2HORIZONTAL
		"Catacombs 01 - Furious Blight x800"                   : lambda s : s.can_reach(el['Cave01Bottom'], 'Region', p) and (s.has(el['claw'], p) or s.has(el['djump'], p) or s.has(el['champion'], p) or s.has(el['silva'], p) and s.has(el['dodge'], p)) or s.can_reach(el['Cave01Left'], 'Region', p) and macros['3LEDGE'](s) and macros['2HORIZONTAL'](s),
#		                                                        BottomOfTheWell
		"Catacombs 01 To Catacombs 02"                         : lambda s : s.can_reach(el['BottomOfTheWell'], 'Location', p),
#		                                                        BottomOfTheWell
		"Catacombs 01 To Cliffside Hamlet 12"                  : lambda s : s.can_reach(el['BottomOfTheWell'], 'Location', p),
#		                                                        Cave02Right + (hook | claw + (HORIZONTAL | LEDGE + dash))
		"Catacombs 02 - Stagnant Blight x30"                   : lambda s : s.can_reach(el['Cave02Right'], 'Region', p) and (s.has(el['hook'], p) or s.has(el['claw'], p) and (macros['HORIZONTAL'](s) or macros['LEDGE'](s) and s.has(el['dash'], p))),
#		                                                        Cave02Right
		"Catacombs 02 - Stagnant Blight x10"                   : lambda s : s.can_reach(el['Cave02Right'], 'Region', p),
#		                                                        Cave02Right | Cave02Bottom | Cave02Top
		"Catacombs 02 To Catacombs 05"                         : lambda s : s.can_reach(el['Cave02Right'], 'Region', p) or s.can_reach(el['Cave02Bottom'], 'Region', p) or s.can_reach(el['Cave02Top'], 'Region', p),
#		                                                        Cave02Bottom | Cave02Right + slam
		"Catacombs 02 To Catacombs 07"                         : lambda s : s.can_reach(el['Cave02Bottom'], 'Region', p) or s.can_reach(el['Cave02Right'], 'Region', p) and s.has(el['slam'], p),
#		                                                        Cave02Right + claw + (FULLSILVA + dash | 3LEDGE | 2LEDGE + 2HORIZONTAL | silva + 2HORIZONTAL | silva + sinner + djump | dash + djump + champion + sinner)
		"Catacombs 02 To Catacombs 01"                         : lambda s : s.can_reach(el['Cave02Right'], 'Region', p) and s.has(el['claw'], p) and (macros['FULLSILVA'](s) and s.has(el['dash'], p) or macros['3LEDGE'](s) or macros['2LEDGE'](s) and macros['2HORIZONTAL'](s) or s.has(el['silva'], p) and macros['2HORIZONTAL'](s) or s.has(el['silva'], p) and s.has(el['sinner'], p) and s.has(el['djump'], p) or s.has(el['dash'], p) and s.has(el['djump'], p) and s.has(el['champion'], p) and s.has(el['sinner'], p)),
#		                                                        Cave03Left | Cave03Right | Cave03Top
		"Catacombs 03 - Defense of the Twin Spires 2"          : lambda s : s.can_reach(el['Cave03Left'], 'Region', p) or s.can_reach(el['Cave03Right'], 'Region', p) or s.can_reach(el['Cave03Top'], 'Region', p),
#		                                                        Cave03Right
		"Catacombs 03 - Fretia's Memoirs 4"                    : lambda s : s.can_reach(el['Cave03Right'], 'Region', p),
#		                                                        Cave03Left
		"Catacombs 03 To Catacombs 07"                         : lambda s : s.can_reach(el['Cave03Left'], 'Region', p),
#		                                                        Cave03Right
		"Catacombs 03 To Catacombs 08"                         : lambda s : s.can_reach(el['Cave03Right'], 'Region', p),
#		                                                        Charnel
		"Catacombs 03 To Catacombs 06"                         : lambda s : s.can_reach(el['Charnel'], 'Location', p),
#		                                                        Cave04Bottom
		"Catacombs 04 - Amulet Fragment"                       : lambda s : s.can_reach(el['Cave04Bottom'], 'Region', p),
#		                                                        Cave04Right | Cave04Bottom
		"Catacombs 04 To Catacombs 16"                         : lambda s : s.can_reach(el['Cave04Right'], 'Region', p) or s.can_reach(el['Cave04Bottom'], 'Region', p),
#		                                                        Cave04Bottom | Cave04Right
		"Catacombs 04 To Catacombs 05"                         : lambda s : s.can_reach(el['Cave04Bottom'], 'Region', p) or s.can_reach(el['Cave04Right'], 'Region', p),
#		                                                        Cave04Left | Cave04Bottom + unlock
		"Catacombs 04 To Catacombs 12"                         : lambda s : s.can_reach(el['Cave04Left'], 'Region', p) or s.can_reach(el['Cave04Bottom'], 'Region', p) and s.has(el['unlock'], p),
#		                                                        Cave05Bottom + (hook | LEDGE | dash | HORIZONTAL)
		"Catacombs 05 - Furious Blight x10"                    : lambda s : s.can_reach(el['Cave05Bottom'], 'Region', p) and (s.has(el['hook'], p) or macros['LEDGE'](s) or s.has(el['dash'], p) or macros['HORIZONTAL'](s)),
#		                                                        Cave05Left | Cave05Bottom
		"Catacombs 05 To Catacombs 02"                         : lambda s : s.can_reach(el['Cave05Left'], 'Region', p) or s.can_reach(el['Cave05Bottom'], 'Region', p),
#		                                                        Cave05Top | Cave05Bottom
		"Catacombs 05 To Catacombs 04"                         : lambda s : s.can_reach(el['Cave05Top'], 'Region', p) or s.can_reach(el['Cave05Bottom'], 'Region', p),
#		                                                        Cave05Bottom | Cave05Left | Cave05Right | Cave05Top
		"Catacombs 05 To Catacombs 06"                         : lambda s : s.can_reach(el['Cave05Bottom'], 'Region', p) or s.can_reach(el['Cave05Left'], 'Region', p) or s.can_reach(el['Cave05Right'], 'Region', p) or s.can_reach(el['Cave05Top'], 'Region', p),
#		                                                        Cave05Right | Cave05Bottom + (claw |  2LEDGE | 2HORIZONTAL | LEDGE + HORIZONTAL)
		"Catacombs 05 To Catacombs 10"                         : lambda s : s.can_reach(el['Cave05Right'], 'Region', p) or s.can_reach(el['Cave05Bottom'], 'Region', p) and (s.has(el['claw'], p) or macros['2LEDGE'](s) or macros['2HORIZONTAL'](s) or macros['LEDGE'](s) and macros['HORIZONTAL'](s)),
#		                                                        Cave06Top
		"Catacombs 06 - Fretia's Memoirs 2"                    : lambda s : s.can_reach(el['Cave06Top'], 'Region', p),
#		                                                        Cave06Top
		"Catacombs 06 - Fretia's Memoirs 1"                    : lambda s : s.can_reach(el['Cave06Top'], 'Region', p),
#		                                                        Cave06Top
		"Catacombs 06 - Kilteus' Ring"                         : lambda s : s.can_reach(el['Cave06Top'], 'Region', p),
#		                                                        Cave06Top | Cave06Bottom
		"Catacombs 06 To Catacombs 05"                         : lambda s : s.can_reach(el['Cave06Top'], 'Region', p) or s.can_reach(el['Cave06Bottom'], 'Region', p),
#		                                                        Cave06Bottom | Cave06Top
		"Catacombs 06 To Catacombs 03"                         : lambda s : s.can_reach(el['Cave06Bottom'], 'Region', p) or s.can_reach(el['Cave06Top'], 'Region', p),
#		                                                        Cave07Right | Cave07Top
		"Catacombs 07 - Elder Crypt Keeper"                    : lambda s : s.can_reach(el['Cave07Right'], 'Region', p) or s.can_reach(el['Cave07Top'], 'Region', p),
#		                                                        Spider + swim
		"Catacombs 07 - Stagnant Blight x10"                   : lambda s : s.can_reach(el['Spider'], 'Location', p) and s.has(el['swim'], p),
#		                                                        Spider + claw + hook + (FULLSILVA | 3LEDGE)
		"Catacombs 07 To Catacombs 02"                         : lambda s : s.can_reach(el['Spider'], 'Location', p) and s.has(el['claw'], p) and s.has(el['hook'], p) and (macros['FULLSILVA'](s) or macros['3LEDGE'](s)),
#		                                                        Spider
		"Catacombs 07 To Catacombs 03"                         : lambda s : s.can_reach(el['Spider'], 'Location', p),
#		                                                        Cave08Left + slam
		"Catacombs 08 - Amulet Fragment"                       : lambda s : s.can_reach(el['Cave08Left'], 'Region', p) and s.has(el['slam'], p),
#		                                                        Cave08Top | Cave08Left + (hook | LEDGE | dash | HORIZONTAL)
		"Catacombs 08 To Catacombs 09"                         : lambda s : s.can_reach(el['Cave08Top'], 'Region', p) or s.can_reach(el['Cave08Left'], 'Region', p) and (s.has(el['hook'], p) or macros['LEDGE'](s) or s.has(el['dash'], p) or macros['HORIZONTAL'](s)),
#		                                                        Cave08Left | Cave08Top | Cave08Right
		"Catacombs 08 To Catacombs 03"                         : lambda s : s.can_reach(el['Cave08Left'], 'Region', p) or s.can_reach(el['Cave08Top'], 'Region', p) or s.can_reach(el['Cave08Right'], 'Region', p),
#		                                                        Cave08Bottom | Cave08Left + swim + slam
		"Catacombs 08 To Catacombs 17"                         : lambda s : s.can_reach(el['Cave08Bottom'], 'Region', p) or s.can_reach(el['Cave08Left'], 'Region', p) and s.has(el['swim'], p) and s.has(el['slam'], p),
#		                                                        Cave08Right | Cave08Left
		"Catacombs 08 To Catacombs 11"                         : lambda s : s.can_reach(el['Cave08Right'], 'Region', p) or s.can_reach(el['Cave08Left'], 'Region', p),
#		                                                        Cave09Top + (claw | LEDGE)
		"Catacombs 09 - Amulet Fragment"                       : lambda s : s.can_reach(el['Cave09Top'], 'Region', p) and (s.has(el['claw'], p) or macros['LEDGE'](s)),
#		                                                        Cave09Top
		"Catacombs 09 - Chain of Sorcery"                      : lambda s : s.can_reach(el['Cave09Top'], 'Region', p),
#		                                                        Cave09Top | Cave09Bottom + (claw | LEDGE)
		"Catacombs 09 To Catacombs 10"                         : lambda s : s.can_reach(el['Cave09Top'], 'Region', p) or s.can_reach(el['Cave09Bottom'], 'Region', p) and (s.has(el['claw'], p) or macros['LEDGE'](s)),
#		                                                        Cave09Bottom | Cave09Top | Cave09Right
		"Catacombs 09 To Catacombs 08"                         : lambda s : s.can_reach(el['Cave09Bottom'], 'Region', p) or s.can_reach(el['Cave09Top'], 'Region', p) or s.can_reach(el['Cave09Right'], 'Region', p),
#		                                                        Cave09Right | Cave09Top + (sinner | dodge + (LEDGE | dash + claw) | djump + (champion | silva | dash) | claw + champion)
		"Catacombs 09 To Catacombs 21"                         : lambda s : s.can_reach(el['Cave09Right'], 'Region', p) or s.can_reach(el['Cave09Top'], 'Region', p) and (s.has(el['sinner'], p) or s.has(el['dodge'], p) and (macros['LEDGE'](s) or s.has(el['dash'], p) and s.has(el['claw'], p)) or s.has(el['djump'], p) and (s.has(el['champion'], p) or s.has(el['silva'], p) or s.has(el['dash'], p)) or s.has(el['claw'], p) and s.has(el['champion'], p)),
#		                                                        Cave10Left
		"Catacombs 10 - Amulet Fragment"                       : lambda s : s.can_reach(el['Cave10Left'], 'Region', p),
#		                                                        Cave10Bottom
		"Catacombs 10 - Stagnant Blight x10"                   : lambda s : s.can_reach(el['Cave10Bottom'], 'Region', p),
#		                                                        Cave10Right | Cave10Bottom
		"Catacombs 10 To Catacombs 23"                         : lambda s : s.can_reach(el['Cave10Right'], 'Region', p) or s.can_reach(el['Cave10Bottom'], 'Region', p),
#		                                                        Cave10Left | Cave10Bottom + (hook | 2LEDGE | 2HORIZONTAL | LEDGE + HORIZONTAL)
		"Catacombs 10 To Catacombs 05"                         : lambda s : s.can_reach(el['Cave10Left'], 'Region', p) or s.can_reach(el['Cave10Bottom'], 'Region', p) and (s.has(el['hook'], p) or macros['2LEDGE'](s) or macros['2HORIZONTAL'](s) or macros['LEDGE'](s) and macros['HORIZONTAL'](s)),
#		                                                        Cave10Bottom | Cave10Right | Cave10Top | Cave10Left
		"Catacombs 10 To Catacombs 09"                         : lambda s : s.can_reach(el['Cave10Bottom'], 'Region', p) or s.can_reach(el['Cave10Right'], 'Region', p) or s.can_reach(el['Cave10Top'], 'Region', p) or s.can_reach(el['Cave10Left'], 'Region', p),
#		                                                        Cave10Top | Cave10Bottom
		"Catacombs 10 To Catacombs 16"                         : lambda s : s.can_reach(el['Cave10Top'], 'Region', p) or s.can_reach(el['Cave10Bottom'], 'Region', p),
#		                                                        Cave11Left | Cave11Top | Cave11Right1 | Cave11Right2
		"Catacombs 11 - Silva's Note 2"                        : lambda s : s.can_reach(el['Cave11Left'], 'Region', p) or s.can_reach(el['Cave11Top'], 'Region', p) or s.can_reach(el['Cave11Right1'], 'Region', p) or s.can_reach(el['Cave11Right2'], 'Region', p),
#		                                                        Cave11Left + (LEDGE | HORIZONTAL | hook | dash)
		"Catacombs 11 - Stagnant Blight x10"                   : lambda s : s.can_reach(el['Cave11Left'], 'Region', p) and (macros['LEDGE'](s) or macros['HORIZONTAL'](s) or s.has(el['hook'], p) or s.has(el['dash'], p)),
#		                                                        Cave11Tip + swim
		"Catacombs 11 - Furious Blight x10"                    : lambda s : s.can_reach(el['Cave11Tip'], 'Location', p) and s.has(el['swim'], p),
#		                                                        Cave11Left | Cave11Tip + (hook | HORIZONTAL | LEDGE | claw)
		"Catacombs 11 To Catacombs 08"                         : lambda s : s.can_reach(el['Cave11Left'], 'Region', p) or s.can_reach(el['Cave11Tip'], 'Location', p) and (s.has(el['hook'], p) or macros['HORIZONTAL'](s) or macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                        Cave11Tip + claw
		"Catacombs 11 To Catacombs 13"                         : lambda s : s.can_reach(el['Cave11Tip'], 'Location', p) and s.has(el['claw'], p),
#		                                                        Cave11Right1 | Cave11Tip  + (hook | claw + (LEDGE | sinner | dodge + dash) | 2LEDGE | 2HORIZONTAL | LEDGE + HORIZONTAL)
		"Catacombs 11 To Catacombs 18"                         : lambda s : s.can_reach(el['Cave11Right1'], 'Region', p) or s.can_reach(el['Cave11Tip'], 'Location', p) and (s.has(el['hook'], p) or s.has(el['claw'], p) and (macros['LEDGE'](s) or s.has(el['sinner'], p) or s.has(el['dodge'], p) and s.has(el['dash'], p)) or macros['2LEDGE'](s) or macros['2HORIZONTAL'](s) or macros['LEDGE'](s) and macros['HORIZONTAL'](s)),
#		                                                        Cave12Right + (champion | silva)
		"Catacombs 12 - Stone Tablet Fragment"                 : lambda s : s.can_reach(el['Cave12Right'], 'Region', p) and (s.has(el['silva'], p) or s.has(el['champion'], p)),
#		                                                        Cave12Right
		"Catacombs 12 To Catacombs 04"                         : lambda s : s.can_reach(el['Cave12Right'], 'Region', p),
#		                                                        Cave13Top | Cave13Left | Cave13Right | Cave13Bottom
		"Catacombs 13 - Silva's Note 1"                        : lambda s : s.can_reach(el['Cave13Top'], 'Region', p) or s.can_reach(el['Cave13Left'], 'Region', p) or s.can_reach(el['Cave13Right'], 'Region', p) or s.can_reach(el['Cave13Bottom'], 'Region', p),
#		                                                        Ossuary + hook | Cave13Bottom + claw
		"Catacombs 13 - Furious Blight x30"                    : lambda s : s.can_reach(el['Ossuary'], 'Location', p) and s.has(el['hook'], p) or s.can_reach(el['Cave13Bottom'], 'Region', p) and s.has(el['claw'], p),
#		                                                        Cave13Left + (dash | LEDGE | HORIZONTAL)
		"Catacombs 13 - Furious Blight x10"                    : lambda s : s.can_reach(el['Cave13Left'], 'Region', p) and (s.has(el['dash'], p) or macros['LEDGE'](s) or macros['HORIZONTAL'](s)),
#		                                                        Ossuary
		"Catacombs 13 To Catacombs 11"                         : lambda s : s.can_reach(el['Ossuary'], 'Location', p),
#		                                                        Ossuary
		"Catacombs 13 To Catacombs 14"                         : lambda s : s.can_reach(el['Ossuary'], 'Location', p),
#		                                                        Cave13Left | Ossuary + (claw | 2LEDGE | sinner | LEDGE + HORIZONTAL)
		"Catacombs 13 To Catacombs 23"                         : lambda s : s.can_reach(el['Cave13Left'], 'Region', p) or s.can_reach(el['Ossuary'], 'Location', p) and (s.has(el['claw'], p) or macros['2LEDGE'](s) or s.has(el['sinner'], p) or macros['LEDGE'](s) and macros['HORIZONTAL'](s)),
#		                                                        Ossuary
		"Catacombs 13 To Catacombs 20"                         : lambda s : s.can_reach(el['Ossuary'], 'Location', p),
#		                                                        Cave14Right
		"Catacombs 14 - Stagnant Blight x10"                   : lambda s : s.can_reach(el['Cave14Right'], 'Region', p),
#		                                                        Cave14Bottom | Cave14Right | Cave14Left
		"Catacombs 14 To Catacombs 13"                         : lambda s : s.can_reach(el['Cave14Bottom'], 'Region', p) or s.can_reach(el['Cave14Right'], 'Region', p) or s.can_reach(el['Cave14Left'], 'Region', p),
#		                                                        Cave14Left | Cave14Bottom + LEDGE
		"Catacombs 14 To Catacombs 15"                         : lambda s : s.can_reach(el['Cave14Left'], 'Region', p) or s.can_reach(el['Cave14Bottom'], 'Region', p) and macros['LEDGE'](s),
#		                                                        Cave14Right | Cave14Bottom + (hook | claw | 2LEDGE | LEDGE + HORIZONTAL)
		"Catacombs 14 To Catacombs 22"                         : lambda s : s.can_reach(el['Cave14Right'], 'Region', p) or s.can_reach(el['Cave14Bottom'], 'Region', p) and (s.has(el['hook'], p) or s.has(el['claw'], p) or macros['2LEDGE'](s) or macros['LEDGE'](s) and macros['HORIZONTAL'](s)),
#		                                                        Cave15Right
		"Catacombs 15 - Defense of the Twin Spires 1"          : lambda s : s.can_reach(el['Cave15Right'], 'Region', p),
#		                                                        Cave15Right + slam
		"Catacombs 15 - Right Stagnant Blight x10"             : lambda s : s.can_reach(el['Cave15Right'], 'Region', p) and s.has(el['slam'], p),
#		                                                        Cave15Right | Cave15Left
		"Catacombs 15 - Left Stagnant Blight x10"              : lambda s : s.can_reach(el['Cave15Right'], 'Region', p) or s.can_reach(el['Cave15Left'], 'Region', p),
#		                                                        Cave15Right | Cave15Left + swim + (LEDGE | claw)
		"Catacombs 15 To Catacombs 14"                         : lambda s : s.can_reach(el['Cave15Right'], 'Region', p) or s.can_reach(el['Cave15Left'], 'Region', p) and s.has(el['swim'], p) and (macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                        Cave15Left | Cave15Right
		"Catacombs 15 To Catacombs 16"                         : lambda s : s.can_reach(el['Cave15Left'], 'Region', p) or s.can_reach(el['Cave15Right'], 'Region', p),
#		                                                        Cave16Right | Cave16Bottom | Cave16Left
		"Catacombs 16 - The Next White Priestess"              : lambda s : s.can_reach(el['Cave16Right'], 'Region', p) or s.can_reach(el['Cave16Bottom'], 'Region', p) or s.can_reach(el['Cave16Left'], 'Region', p),
#		                                                        GreatHall + (hook | claw + (2LEDGE | LEDGE + HORIZONTAL))
		"Catacombs 16 - Stagnant Blight x30"                   : lambda s : s.can_reach(el['GreatHall'], 'Location', p) and (s.has(el['hook'], p) or s.has(el['claw'], p) and (macros['2LEDGE'](s) or macros['LEDGE'](s) and macros['HORIZONTAL'](s))),
#		                                                        Cave16Right | GreatHall
		"Catacombs 16 To Catacombs 15"                         : lambda s : s.can_reach(el['Cave16Right'], 'Region', p) or s.can_reach(el['GreatHall'], 'Location', p),
#		                                                        Cave16Bottom
		"Catacombs 16 To Catacombs 10"                         : lambda s : s.can_reach(el['Cave16Bottom'], 'Region', p),
#		                                                        Cave16Left | GreatHall
		"Catacombs 16 To Catacombs 04"                         : lambda s : s.can_reach(el['Cave16Left'], 'Region', p) or s.can_reach(el['GreatHall'], 'Location', p),
#		                                                        Cave17Top + swim
		"Catacombs 17 - Ancient Soul x2"                       : lambda s : s.can_reach(el['Cave17Top'], 'Region', p) and s.has(el['swim'], p),
#		                                                        Cave17Top
		"Catacombs 17 To Catacombs 08"                         : lambda s : s.can_reach(el['Cave17Top'], 'Region', p),
#		                                                        Cave18Left1
		"Catacombs 18 - Holy Spring Water"                     : lambda s : s.can_reach(el['Cave18Left1'], 'Region', p),
#		                                                        Cave18Left1
		"Catacombs 18 To Catacombs 11 Upper"                   : lambda s : s.can_reach(el['Cave18Left1'], 'Region', p),
#		                                                        Cave18Left1 + swim
		"Catacombs 18 To Catacombs 11 Lower"                   : lambda s : s.can_reach(el['Cave18Left1'], 'Region', p) and s.has(el['swim'], p),
#		                                                        Cave19Top | Cave19Left
		"Catacombs 19 - Fallen Archer"                         : lambda s : s.can_reach(el['Cave19Top'], 'Region', p) or s.can_reach(el['Cave19Left'], 'Region', p),
#		                                                        Archer
		"Catacombs 19 - Priestess' Wish"                       : lambda s : s.can_reach(el['Archer'], 'Location', p),
#		                                                        Archer + (hook | LEDGE | HORIZONTAL)
		"Catacombs 19 - Chain of Sorcery"                      : lambda s : s.can_reach(el['Archer'], 'Location', p) and (s.has(el['hook'], p) or macros['LEDGE'](s) or macros['HORIZONTAL'](s)),
#		                                                        Cave19Top | Archer
		"Catacombs 19 To Catacombs 20"                         : lambda s : s.can_reach(el['Cave19Top'], 'Region', p) or s.can_reach(el['Archer'], 'Location', p),
#		                                                        Cave19Left | Cave19Top + (HORIZONTAL + LEDGE | claw | 2LEDGE)
		"Catacombs 19 To Catacombs 21"                         : lambda s : s.can_reach(el['Cave19Left'], 'Region', p) or s.can_reach(el['Cave19Top'], 'Region', p) and (macros['HORIZONTAL'](s) and macros['LEDGE'](s) or s.has(el['claw'], p) or macros['2LEDGE'](s)),
#		                                                        Cave20Top
		"Catacombs 20 - Amulet Fragment"                       : lambda s : s.can_reach(el['Cave20Top'], 'Region', p),
#		                                                        Cave20Top
		"Catacombs 20 - The Heirloom of Land's End"            : lambda s : s.can_reach(el['Cave20Top'], 'Region', p),
#		                                                        Cave20Top
		"Catacombs 20 - Stagnant Blight x10"                   : lambda s : s.can_reach(el['Cave20Top'], 'Region', p),
#		                                                        Cave20Top | Cave20Bottom + (hook | claw | LEDGE)
		"Catacombs 20 To Catacombs 22"                         : lambda s : s.can_reach(el['Cave20Top'], 'Region', p) or s.can_reach(el['Cave20Bottom'], 'Region', p) and (s.has(el['hook'], p) or s.has(el['claw'], p) or macros['LEDGE'](s)),
#		                                                        Cave20Bottom | Cave20Left | Cave20Top
		"Catacombs 20 To Catacombs 19"                         : lambda s : s.can_reach(el['Cave20Bottom'], 'Region', p) or s.can_reach(el['Cave20Left'], 'Region', p) or s.can_reach(el['Cave20Top'], 'Region', p),
#		                                                        Cave20Left | Cave20Bottom | Cave20Top
		"Catacombs 20 To Catacombs 13"                         : lambda s : s.can_reach(el['Cave20Left'], 'Region', p) or s.can_reach(el['Cave20Bottom'], 'Region', p) or s.can_reach(el['Cave20Top'], 'Region', p),
#		                                                        Cave21Right | Cave21Left
		"Catacombs 21 - White Priestess Statue"                : lambda s : s.can_reach(el['Cave21Right'], 'Region', p) or s.can_reach(el['Cave21Left'], 'Region', p),
#		                                                        Cave21Left | Cave21Right
		"Catacombs 21 To Catacombs 09"                         : lambda s : s.can_reach(el['Cave21Left'], 'Region', p) or s.can_reach(el['Cave21Right'], 'Region', p),
#		                                                        Cave21Right | Cave21Left
		"Catacombs 21 To Catacombs 19"                         : lambda s : s.can_reach(el['Cave21Right'], 'Region', p) or s.can_reach(el['Cave21Left'], 'Region', p),
#		                                                        Cave22Right
		"Catacombs 22 - Fretia's Memoirs 3"                    : lambda s : s.can_reach(el['Cave22Right'], 'Region', p),
#		                                                        Cave22Right | Cave22Bottom
		"Catacombs 22 To Twin Spires 02"                       : lambda s : s.can_reach(el['Cave22Right'], 'Region', p) or s.can_reach(el['Cave22Bottom'], 'Region', p),
#		                                                        Cave22Left | Cave22Bottom + (2LEDGE | hook | claw | LEDGE + HORIZONTAL)
		"Catacombs 22 To Catacombs 14"                         : lambda s : s.can_reach(el['Cave22Left'], 'Region', p) or s.can_reach(el['Cave22Bottom'], 'Region', p) and (macros['2LEDGE'](s) or s.has(el['hook'], p) or s.has(el['claw'], p) or macros['LEDGE'](s) and macros['HORIZONTAL'](s)),
#		                                                        Cave22Bottom | Cave22Right | Cave22Left
		"Catacombs 22 To Catacombs 20"                         : lambda s : s.can_reach(el['Cave22Bottom'], 'Region', p) or s.can_reach(el['Cave22Right'], 'Region', p) or s.can_reach(el['Cave22Left'], 'Region', p),
#		                                                        Cave23Right | Cave23Left
		"Catacombs 23 - Guardian Silva"                        : lambda s : s.can_reach(el['Cave23Right'], 'Region', p) or s.can_reach(el['Cave23Left'], 'Region', p),
#		                                                        Silva
		"Catacombs 23 - Unfinished Note"                       : lambda s : s.can_reach(el['Silva'], 'Location', p),
#		                                                        Silva
		"Catacombs 23 To Catacombs 13"                         : lambda s : s.can_reach(el['Silva'], 'Location', p),
#		                                                        Silva
		"Catacombs 23 To Catacombs 10"                         : lambda s : s.can_reach(el['Silva'], 'Location', p),
#		                                                        Church01Bottom | Church01Left | Church01Top
		"White Parish 01 To White Parish 02"                   : lambda s : s.can_reach(el['Church01Bottom'], 'Region', p) or s.can_reach(el['Church01Left'], 'Region', p) or s.can_reach(el['Church01Top'], 'Region', p),
#		                                                        Church01Left | Church01Bottom | Church01Top
		"White Parish 01 To White Parish 12"                   : lambda s : s.can_reach(el['Church01Left'], 'Region', p) or s.can_reach(el['Church01Bottom'], 'Region', p) or s.can_reach(el['Church01Top'], 'Region', p),
#		                                                        Church02Right
		"White Parish 02 - Amulet Fragment"                    : lambda s : s.can_reach(el['Church02Right'], 'Region', p),
#		                                                        Church02Right
		"White Parish 02 - Eleine's Letter"                    : lambda s : s.can_reach(el['Church02Right'], 'Region', p),
#		                                                        Church02Top | Church02Right + (djump | champion | silva + dodge)
		"White Parish 02 To White Parish 01"                   : lambda s : s.can_reach(el['Church02Top'], 'Region', p) or s.can_reach(el['Church02Right'], 'Region', p) and (s.has(el['djump'], p) or s.has(el['champion'], p) or s.has(el['silva'], p) and s.has(el['dodge'], p)),
#		                                                        Church02Right | Church02Top
		"White Parish 02 To White Parish 10"                   : lambda s : s.can_reach(el['Church02Right'], 'Region', p) or s.can_reach(el['Church02Top'], 'Region', p),
#		                                                        Church03Left
		"White Parish 03 - Guardian Siegrid"                   : lambda s : s.can_reach(el['Church03Left'], 'Region', p),
#		                                                        Church03Left | Church03Right
		"White Parish 03 To White Parish 05"                   : lambda s : s.can_reach(el['Church03Left'], 'Region', p) or s.can_reach(el['Church03Right'], 'Region', p),
#		                                                        Church03Right | Church03Left
		"White Parish 03 To White Parish 04"                   : lambda s : s.can_reach(el['Church03Right'], 'Region', p) or s.can_reach(el['Church03Left'], 'Region', p),
#		                                                        Church04Right | Church04Left
		"White Parish 04 - Groa's Letter"                      : lambda s : s.can_reach(el['Church04Right'], 'Region', p) or s.can_reach(el['Church04Left'], 'Region', p),
#		                                                        Church04Left | SaintsPassage
		"White Parish 04 To White Parish 03"                   : lambda s : s.can_reach(el['Church04Left'], 'Region', p) or s.can_reach(el['SaintsPassage'], 'Location', p),
#		                                                        Church04Right | SaintsPassage
		"White Parish 04 To White Parish 06"                   : lambda s : s.can_reach(el['Church04Right'], 'Region', p) or s.can_reach(el['SaintsPassage'], 'Location', p),
#		                                                        Church05Top | CathedralCloister + LEDGE
		"White Parish 05 - Soiled Prayer Beads"                : lambda s : s.can_reach(el['Church05Top'], 'Region', p) or s.can_reach(el['CathedralCloister'], 'Location', p) and macros['LEDGE'](s),
#		                                                        CathedralCloister
		"White Parish 05 To White Parish 11"                   : lambda s : s.can_reach(el['CathedralCloister'], 'Location', p),
#		                                                        CathedralCloister
		"White Parish 05 To White Parish 03"                   : lambda s : s.can_reach(el['CathedralCloister'], 'Location', p),
#		                                                        Church05Right | Church05Bottom | Church05Top
		"CathedralCloister"                                    : lambda s : s.can_reach(el['Church05Right'], 'Region', p) or s.can_reach(el['Church05Bottom'], 'Region', p) or s.can_reach(el['Church05Top'], 'Region', p),
#		                                                        CathedralCloister + claw
		"White Parish 05 To White Parish 09"                   : lambda s : s.can_reach(el['CathedralCloister'], 'Location', p) and s.has(el['claw'], p),
#		                                                        Church06Left | Church06Right
		"White Parish 06 To White Parish 04"                   : lambda s : s.can_reach(el['Church06Left'], 'Region', p) or s.can_reach(el['Church06Right'], 'Region', p),
#		                                                        Church06Right | Church06Left + (LEDGE | claw)
		"White Parish 06 To White Parish 07"                   : lambda s : s.can_reach(el['Church06Right'], 'Region', p) or s.can_reach(el['Church06Left'], 'Region', p) and (macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                        Church07Right
		"White Parish 07 - Cliffside Hamlet Youth"             : lambda s : s.can_reach(el['Church07Right'], 'Region', p),
#		                                                        Youth + slam
		"White Parish 07 - Chain of Sorcery"                   : lambda s : s.can_reach(el['Youth'], 'Location', p) and s.has(el['slam'], p),
#		                                                        Church07Left | Youth + (LEDGE | claw)
		"White Parish 07 To White Parish 06"                   : lambda s : s.can_reach(el['Church07Left'], 'Region', p) or s.can_reach(el['Youth'], 'Location', p) and (macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                        Church07Right | Church07Left + (LEDGE | claw) | Youth
		"White Parish 07 To White Parish 08"                   : lambda s : s.can_reach(el['Church07Right'], 'Region', p) or s.can_reach(el['Church07Left'], 'Region', p) and (macros['LEDGE'](s) or s.has(el['claw'], p)) or s.can_reach(el['Youth'], 'Location', p),
#		                                                        Crossroads + swim
		"White Parish 08 - Amulet Fragment"                    : lambda s : s.can_reach(el['Crossroads'], 'Location', p) and s.has(el['swim'], p),
#		                                                        Church08Top | Church08Bottom | Church08Left
		"White Parish 08 - The Parish Way 2"                   : lambda s : s.can_reach(el['Church08Top'], 'Region', p) or s.can_reach(el['Church08Bottom'], 'Region', p) or s.can_reach(el['Church08Left'], 'Region', p),
#		                                                        Crossroads
		"White Parish 08 To Cliffside Hamlet 01"               : lambda s : s.can_reach(el['Crossroads'], 'Location', p),
#		                                                        Crossroads
		"White Parish 08 To Witch's Thicket 01"                : lambda s : s.can_reach(el['Crossroads'], 'Location', p),
#		                                                        Crossroads
		"White Parish 08 To White Parish 07"                   : lambda s : s.can_reach(el['Crossroads'], 'Location', p),
#		                                                        Church09Bottom | Church09Top
		"White Parish 09 - Chief Guardian"                     : lambda s : s.can_reach(el['Church09Bottom'], 'Region', p) or s.can_reach(el['Church09Top'], 'Region', p),
#		                                                        Church09Bottom + CHARGE + (LEDGE + claw | 3LEDGE)
		"White Parish 09 - Vibrant Plume"                      : lambda s : s.can_reach(el['Church09Bottom'], 'Region', p) and macros['CHARGE'](s) and (macros['LEDGE'](s) and s.has(el['claw'], p) or macros['3LEDGE'](s)),
#		                                                        Chief
		"White Parish 09 - Furious Blight x30"                 : lambda s : s.can_reach(el['Chief'], 'Location', p),
#		                                                        Church09Bottom | Church09Top
		"White Parish 09 To White Parish 05"                   : lambda s : s.can_reach(el['Church09Bottom'], 'Region', p) or s.can_reach(el['Church09Top'], 'Region', p),
#		                                                        Chief
		"White Parish 09 To White Parish 01"                   : lambda s : s.can_reach(el['Chief'], 'Location', p),
#		                                                        Church09Bottom + hook
		"White Parish 09 To White Parish 14"                   : lambda s : s.can_reach(el['Church09Bottom'], 'Region', p) and s.has(el['hook'], p),
#		                                                        Church10Left | Church10Right
		"White Parish 10 - On the Blighted 1"                  : lambda s : s.can_reach(el['Church10Left'], 'Region', p) or s.can_reach(el['Church10Right'], 'Region', p),
#		                                                        Cellar
		"White Parish 10 - On the Blighted 2"                  : lambda s : s.can_reach(el['Cellar'], 'Location', p),
#		                                                        Church10Left | Cellar
		"White Parish 10 To White Parish 02"                   : lambda s : s.can_reach(el['Church10Left'], 'Region', p) or s.can_reach(el['Cellar'], 'Location', p),
#		                                                        Church10Right | Cellar
		"White Parish 10 To White Parish 11"                   : lambda s : s.can_reach(el['Church10Right'], 'Region', p) or s.can_reach(el['Cellar'], 'Location', p),
#		                                                        Church11Left
		"White Parish 11 - Amulet Fragment"                    : lambda s : s.can_reach(el['Church11Left'], 'Region', p),
#		                                                        Church11Top
		"White Parish 11 - The Parish Way 1"                   : lambda s : s.can_reach(el['Church11Top'], 'Region', p),
#		                                                        Church11Top | Church11Left
		"White Parish 11 To White Parish 05"                   : lambda s : s.can_reach(el['Church11Top'], 'Region', p) or s.can_reach(el['Church11Left'], 'Region', p),
#		                                                        Church11Left
		"White Parish 11 To White Parish 10"                   : lambda s : s.can_reach(el['Church11Left'], 'Region', p),
#		                                                        Church12Right
		"White Parish 12 - Statue Inscription"                 : lambda s : s.can_reach(el['Church12Right'], 'Region', p),
#		                                                        Church12Right | Start
		"White Parish 12 To White Parish 01"                   : lambda s : s.can_reach(el['Church12Right'], 'Region', p) or s.can_reach(el['Start'], 'Location', p),
#		                                                        Church12Bottom | Start + (unlock + ( djump | champion | silva + dodge | claw ))
		"White Parish 12 To White Parish 13"                   : lambda s : s.can_reach(el['Church12Bottom'], 'Region', p) or s.can_reach(el['Start'], 'Location', p) and (s.has(el['unlock'], p) and (s.has(el['djump'], p) or s.has(el['champion'], p) or s.has(el['silva'], p) and s.has(el['dodge'], p) or s.has(el['claw'], p))),
#		                                                        Church13Top
		"White Parish 13 - Restoring the Aegis Curio"          : lambda s : s.can_reach(el['Church13Top'], 'Region', p),
#		                                                        Church13Top
		"White Parish 13 To White Parish 12"                   : lambda s : s.can_reach(el['Church13Top'], 'Region', p),
#		                                                        Church14Bottom
		"White Parish 14 - Priestess' Wish"                    : lambda s : s.can_reach(el['Church14Bottom'], 'Region', p),
#		                                                        Church14Bottom
		"White Parish 14 - Lily's Note"                        : lambda s : s.can_reach(el['Church14Bottom'], 'Region', p),
#		                                                        Church14Bottom
		"White Parish 14 To White Parish 09"                   : lambda s : s.can_reach(el['Church14Bottom'], 'Region', p),
#		                                                        Forest01Top | Forest01Right + (LEDGE | claw)
		"Witch's Thicket 01 To White Parish 08"                : lambda s : s.can_reach(el['Forest01Top'], 'Region', p) or s.can_reach(el['Forest01Right'], 'Region', p) and (macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                        Forest01Right | Forest01Top
		"Witch's Thicket 01 To Witch's Thicket 02"             : lambda s : s.can_reach(el['Forest01Right'], 'Region', p) or s.can_reach(el['Forest01Top'], 'Region', p),
#		                                                        Forest02Left | Forest02Right2 + hook
		"Witch's Thicket 02 - Stagnant Blight x10"             : lambda s : s.can_reach(el['Forest02Left'], 'Region', p) or s.can_reach(el['Forest02Right2'], 'Region', p) and s.has(el['hook'], p),
#		                                                        Forest02Left | Forest02Right1
		"Witch's Thicket 02 To Witch's Thicket 01"             : lambda s : s.can_reach(el['Forest02Left'], 'Region', p) or s.can_reach(el['Forest02Right1'], 'Region', p),
#		                                                        Forest02Right1 | Forest02Left | Forest02Right2 + (claw | LEDGE)
		"Witch's Thicket 02 To Witch's Thicket 04"             : lambda s : s.can_reach(el['Forest02Right1'], 'Region', p) or s.can_reach(el['Forest02Left'], 'Region', p) or s.can_reach(el['Forest02Right2'], 'Region', p) and (s.has(el['claw'], p) or macros['LEDGE'](s)),
#		                                                        Forest02Right2 | Forest02Left
		"Witch's Thicket 02 To Witch's Thicket 03"             : lambda s : s.can_reach(el['Forest02Right2'], 'Region', p) or s.can_reach(el['Forest02Left'], 'Region', p),
#		                                                        Forest03Left + swim
		"Witch's Thicket 03 - Amulet Fragment"                 : lambda s : s.can_reach(el['Forest03Left'], 'Region', p) and s.has(el['swim'], p),
#		                                                        Forest03Left + swim
		"Witch's Thicket 03 - Chain of Sorcery"                : lambda s : s.can_reach(el['Forest03Left'], 'Region', p) and s.has(el['swim'], p),
#		                                                        Forest03Right | Forest03Left + (claw | LEDGE | HORIZONTAL)
		"Witch's Thicket 03 To Witch's Thicket 05"             : lambda s : s.can_reach(el['Forest03Right'], 'Region', p) or s.can_reach(el['Forest03Left'], 'Region', p) and (s.has(el['claw'], p) or macros['LEDGE'](s) or macros['HORIZONTAL'](s)),
#		                                                        Forest03Left | Forest03Right
		"Witch's Thicket 03 To Witch's Thicket 02"             : lambda s : s.can_reach(el['Forest03Left'], 'Region', p) or s.can_reach(el['Forest03Right'], 'Region', p),
#		                                                        Forest04Right
		"Witch's Thicket 04 - Amulet Fragment"                 : lambda s : s.can_reach(el['Forest04Right'], 'Region', p),
#		                                                        Forest04Left + (LEDGE | claw + HORIZONTAL)
		"Witch's Thicket 04 - Rusted Blue Ornament"            : lambda s : s.can_reach(el['Forest04Left'], 'Region', p) and (macros['LEDGE'](s) or s.has(el['claw'], p) and macros['HORIZONTAL'](s)),
#		                                                        Forest04Left + (slam + LEDGE)
		"Witch's Thicket 04 - Stagnant Blight x10"             : lambda s : s.can_reach(el['Forest04Left'], 'Region', p) and (s.has(el['slam'], p) and macros['LEDGE'](s)),
#		                                                        Forest04Right | Forest04Left +  (LEDGE | claw | HORIZONTAL + swim)
		"Witch's Thicket 04 To Witch's Thicket 05"             : lambda s : s.can_reach(el['Forest04Right'], 'Region', p) or s.can_reach(el['Forest04Left'], 'Region', p) and (macros['LEDGE'](s) or s.has(el['claw'], p) or macros['HORIZONTAL'](s) and s.has(el['swim'], p)),
#		                                                        Forest04Left | Forest04Right + (LEDGE | claw)
		"Witch's Thicket 04 To Witch's Thicket 02"             : lambda s : s.can_reach(el['Forest04Left'], 'Region', p) or s.can_reach(el['Forest04Right'], 'Region', p) and (macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                        Forest05Right | Forest05Left | Forest05Top
		"Witch's Thicket 05 - Coven Handbook"                  : lambda s : s.can_reach(el['Forest05Right'], 'Region', p) or s.can_reach(el['Forest05Left'], 'Region', p) or s.can_reach(el['Forest05Top'], 'Region', p),
#		                                                        Forest05Right | DryadLake
		"Witch's Thicket 05 To Witch's Thicket 07"             : lambda s : s.can_reach(el['Forest05Right'], 'Region', p) or s.can_reach(el['DryadLake'], 'Location', p),
#		                                                        Forest05Left | DryadLake
		"Witch's Thicket 05 To Witch's Thicket 03"             : lambda s : s.can_reach(el['Forest05Left'], 'Region', p) or s.can_reach(el['DryadLake'], 'Location', p),
#		                                                        Forest05Top | DryadLake + LEDGE
		"Witch's Thicket 05 To Witch's Thicket 04"             : lambda s : s.can_reach(el['Forest05Top'], 'Region', p) or s.can_reach(el['DryadLake'], 'Location', p) and macros['LEDGE'](s),
#		                                                        Forest06Bottom + LEDGE
		"Witch's Thicket 06 - Fungal Sorcerer"                 : lambda s : s.can_reach(el['Forest06Bottom'], 'Region', p) and macros['LEDGE'](s),
#		                                                        Forest06Bottom + LEDGE
		"Witch's Thicket 06 - Lover's Letter"                  : lambda s : s.can_reach(el['Forest06Bottom'], 'Region', p) and macros['LEDGE'](s),
#		                                                        Forest06Bottom + (hook | LEDGE + slam | 2LEDGE | LEDGE + HORIZONTAL)
		"Witch's Thicket 06 - Furious Blight x10"              : lambda s : s.can_reach(el['Forest06Bottom'], 'Region', p) and (s.has(el['hook'], p) or macros['LEDGE'](s) and s.has(el['slam'], p) or macros['2LEDGE'](s) or macros['LEDGE'](s) and macros['HORIZONTAL'](s)),
#		                                                        Forest06Bottom
		"Witch's Thicket 06 To Witch's Thicket 07"             : lambda s : s.can_reach(el['Forest06Bottom'], 'Region', p),
#		                                                        (Forest07Left | Forest07Bottom) + (LEDGE | hook | HORIZONTAL | claw)
		"Witch's Thicket 07 - Amulet Fragment"                 : lambda s : (s.can_reach(el['Forest07Left'], 'Region', p) or s.can_reach(el['Forest07Bottom'], 'Region', p)) and (macros['LEDGE'](s) or s.has(el['hook'], p) or macros['HORIZONTAL'](s) or s.has(el['claw'], p)),
#		                                                        Forest07Right + (hook | claw +  LEDGE)
		"Witch's Thicket 07 - Stagnant Blight x30"             : lambda s : s.can_reach(el['Forest07Right'], 'Region', p) and (s.has(el['hook'], p) or s.has(el['claw'], p) and macros['LEDGE'](s)),
#		                                                        Forest07Left | Forest07Right
		"Witch's Thicket 07 - Stagnant Blight x10"             : lambda s : s.can_reach(el['Forest07Left'], 'Region', p) or s.can_reach(el['Forest07Right'], 'Region', p),
#		                                                        Forest07Right | Forest07Left + (dodge + (LEDGE | dash)) | 2LEDGE | hook | sinner | djump + dash
		"Witch's Thicket 07 To Stockade 01"                    : lambda s : s.can_reach(el['Forest07Right'], 'Region', p) or s.can_reach(el['Forest07Left'], 'Region', p) and (s.has(el['dodge'], p) and (macros['LEDGE'](s) or s.has(el['dash'], p))) or macros['2LEDGE'](s) or s.has(el['hook'], p) or s.has(el['sinner'], p) or s.has(el['djump'], p) and s.has(el['dash'], p),
#		                                                        Forest07Bottom | Forest07Left
		"Witch's Thicket 07 To Witch's Thicket 08"             : lambda s : s.can_reach(el['Forest07Bottom'], 'Region', p) or s.can_reach(el['Forest07Left'], 'Region', p),
#		                                                        Forest07Left | Forest07Bottom + LEDGE | Forest07Right + (LEDGE | hook | HORIZONTAL | dash)
		"Witch's Thicket 07 To Witch's Thicket 05"             : lambda s : s.can_reach(el['Forest07Left'], 'Region', p) or s.can_reach(el['Forest07Bottom'], 'Region', p) and macros['LEDGE'](s) or s.can_reach(el['Forest07Right'], 'Region', p) and (macros['LEDGE'](s) or s.has(el['hook'], p) or macros['HORIZONTAL'](s) or s.has(el['dash'], p)),
#		                                                        Forest07Top | Forest07Left + LEDGE
		"Witch's Thicket 07 To Witch's Thicket 06"             : lambda s : s.can_reach(el['Forest07Top'], 'Region', p) or s.can_reach(el['Forest07Left'], 'Region', p) and macros['LEDGE'](s),
#		                                                        Forest08Top + (LEDGE | hook | claw + HORIZONTAL)
		"Witch's Thicket 08 - Manisa's Ring"                   : lambda s : s.can_reach(el['Forest08Top'], 'Region', p) and (macros['LEDGE'](s) or s.has(el['hook'], p) or s.has(el['claw'], p) and macros['HORIZONTAL'](s)),
#		                                                        ManisasRing + (2LEDGE | LEDGE + HORIZONTAL | claw + sinner | hook)
		"Witch's Thicket 08 - Cracked Familiar Stone"          : lambda s : s.can_reach(el['ManisasRing'], 'Location', p) and (macros['2LEDGE'](s) or macros['LEDGE'](s) and macros['HORIZONTAL'](s) or s.has(el['claw'], p) and s.has(el['sinner'], p) or s.has(el['hook'], p)),
#		                                                        Forest08Top + (LEDGE | HORIZONTAL | dash)
		"Witch's Thicket 08 - Furious Blight x10"              : lambda s : s.can_reach(el['Forest08Top'], 'Region', p) and (macros['LEDGE'](s) or macros['HORIZONTAL'](s) or s.has(el['dash'], p)),
#		                                                        Forest08Top | Forest08Right + (LEDGE | claw)
		"Witch's Thicket 08 To Witch's Thicket 07"             : lambda s : s.can_reach(el['Forest08Top'], 'Region', p) or s.can_reach(el['Forest08Right'], 'Region', p) and (macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                        Forest08Right | Forest08Top + (LEDGE | hook | claw)
		"Witch's Thicket 08 To Witch's Thicket 10"             : lambda s : s.can_reach(el['Forest08Right'], 'Region', p) or s.can_reach(el['Forest08Top'], 'Region', p) and (macros['LEDGE'](s) or s.has(el['hook'], p) or s.has(el['claw'], p)),
#		                                                        Forest10Left + swim + (LEDGE | claw)
		"Witch's Thicket 09 - Priestess' Wish"                 : lambda s : s.can_reach(el['Forest10Left'], 'Region', p) and s.has(el['swim'], p) and (macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                        Forest10Left + swim + (LEDGE | claw)
		"Witch's Thicket 09 - Tarnished Picture"               : lambda s : s.can_reach(el['Forest10Left'], 'Region', p) and s.has(el['swim'], p) and (macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                        Forest09Top | Forest09Left + swim
		"Witch's Thicket 09 To Witch's Thicket 10"             : lambda s : s.can_reach(el['Forest09Top'], 'Region', p) or s.can_reach(el['Forest09Left'], 'Region', p) and s.has(el['swim'], p),
#		                                                        (Forest09Top | Forest09Left) + swim
		"Witch's Thicket 09 - Furious Blight x10"              : lambda s : (s.can_reach(el['Forest09Top'], 'Region', p) or s.can_reach(el['Forest09Left'], 'Region', p)) and s.has(el['swim'], p),
#		                                                        Forest09Left | Forest09Top + swim + (LEDGE | claw)
		"Witch's Thicket 09 To Verboten Domain 02"             : lambda s : s.can_reach(el['Forest09Left'], 'Region', p) or s.can_reach(el['Forest09Top'], 'Region', p) and s.has(el['swim'], p) and (macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                        Forest10Bottom2 | WitchsHermitage
		"Witch's Thicket 10 To Witch's Thicket 11"             : lambda s : s.can_reach(el['Forest10Bottom2'], 'Region', p) or s.can_reach(el['WitchsHermitage'], 'Location', p),
#		                                                        Forest10Bottom1 | WitchsHermitage
		"Witch's Thicket 10 To Witch's Thicket 09"             : lambda s : s.can_reach(el['Forest10Bottom1'], 'Region', p) or s.can_reach(el['WitchsHermitage'], 'Location', p),
#		                                                        Forest10Bottom2 | Forest10Bottom1 | Forest10Left | Forest10Right
		"Witch's Thicket 10 - Sorcerer's Notes"                : lambda s : s.can_reach(el['Forest10Bottom2'], 'Region', p) or s.can_reach(el['Forest10Bottom1'], 'Region', p) or s.can_reach(el['Forest10Left'], 'Region', p) or s.can_reach(el['Forest10Right'], 'Region', p),
#		                                                        Forest10Left | WitchsHermitage
		"Witch's Thicket 10 To Witch's Thicket 08"             : lambda s : s.can_reach(el['Forest10Left'], 'Region', p) or s.can_reach(el['WitchsHermitage'], 'Location', p),
#		                                                        Forest10Right | WitchsHermitage
		"Witch's Thicket 10 To Witch's Thicket 12"             : lambda s : s.can_reach(el['Forest10Right'], 'Region', p) or s.can_reach(el['WitchsHermitage'], 'Location', p),
#		                                                        Forest11Top
		"Witch's Thicket 11 - Floral Sorceress"                : lambda s : s.can_reach(el['Forest11Top'], 'Region', p),
#		                                                        Forest11Top
		"Witch's Thicket 11 - Amulet Fragment"                 : lambda s : s.can_reach(el['Forest11Top'], 'Region', p),
#		                                                        Forest11Top
		"Witch's Thicket 11 - Chain of Sorcery"                : lambda s : s.can_reach(el['Forest11Top'], 'Region', p),
#		                                                        Forest11Right + (LEDGE | HORIZONTAL | dash)
		"Witch's Thicket 11 - Ruined Witch's Book"             : lambda s : s.can_reach(el['Forest11Right'], 'Region', p) and (macros['LEDGE'](s) or macros['HORIZONTAL'](s) or s.has(el['dash'], p)),
#		                                                        Forest11Top | Forest11Right
		"Witch's Thicket 11 To Witch's Thicket 10"             : lambda s : s.can_reach(el['Forest11Top'], 'Region', p) or s.can_reach(el['Forest11Right'], 'Region', p),
#		                                                        Forest11Right + (LEDGE + claw | hook | 2HORIZONTAL + (dash | djump | silva))
		"Witch's Thicket 11 - Stagnant Blight x30"             : lambda s : s.can_reach(el['Forest11Right'], 'Region', p) and (macros['LEDGE'](s) and s.has(el['claw'], p) or s.has(el['hook'], p) or macros['2HORIZONTAL'](s) and (s.has(el['dash'], p) or s.has(el['djump'], p) or s.has(el['silva'], p))),
#		                                                        Forest11Right + swim
		"Witch's Thicket 11 - Stagnant Blight x10"             : lambda s : s.can_reach(el['Forest11Right'], 'Region', p) and s.has(el['swim'], p),
#		                                                        Forest11Right | Forest11Top + swim
		"Witch's Thicket 11 To Witch's Thicket 14"             : lambda s : s.can_reach(el['Forest11Right'], 'Region', p) or s.can_reach(el['Forest11Top'], 'Region', p) and s.has(el['swim'], p),
#		                                                        Forest12Left + (LEDGE | claw | hook)
		"Witch's Thicket 12 - Amulet Fragment"                 : lambda s : s.can_reach(el['Forest12Left'], 'Region', p) and (macros['LEDGE'](s) or s.has(el['claw'], p) or s.has(el['hook'], p)),
#		                                                        Forest12Bottom | Forest12Right
		"Witch's Thicket 12 - Stagnant Blight x10"             : lambda s : s.can_reach(el['Forest12Bottom'], 'Region', p) or s.can_reach(el['Forest12Right'], 'Region', p),
#		                                                        Forest12Left | Forest12Bottom + (LEDGE | hook)
		"Witch's Thicket 12 To Witch's Thicket 10"             : lambda s : s.can_reach(el['Forest12Left'], 'Region', p) or s.can_reach(el['Forest12Bottom'], 'Region', p) and (macros['LEDGE'](s) or s.has(el['hook'], p)),
#		                                                        Forest12Bottom | Forest12Right  | Forest12Left + (LEDGE | hook)
		"Witch's Thicket 12 To Witch's Thicket 13"             : lambda s : s.can_reach(el['Forest12Bottom'], 'Region', p) or s.can_reach(el['Forest12Right'], 'Region', p) or s.can_reach(el['Forest12Left'], 'Region', p) and (macros['LEDGE'](s) or s.has(el['hook'], p)),
#		                                                        Forest12Right | Forest12Left + (claw + (djump | champion) | claw + LEDGE + (HORIZONTAL | dash) | silva + djump | LEDGE + sinner | 2LEDGE + HORIZONTAL) | Forest12Bottom + hook
		"Witch's Thicket 12 To Witch's Thicket 17"             : lambda s : s.can_reach(el['Forest12Right'], 'Region', p) or s.can_reach(el['Forest12Left'], 'Region', p) and (s.has(el['claw'], p) and (s.has(el['djump'], p) or s.has(el['champion'], p)) or s.has(el['claw'], p) and macros['LEDGE'](s) and (macros['HORIZONTAL'](s) or s.has(el['dash'], p)) or s.has(el['silva'], p) and s.has(el['djump'], p) or macros['LEDGE'](s) and s.has(el['sinner'], p) or macros['2LEDGE'](s) and macros['HORIZONTAL'](s)) or s.can_reach(el['Forest12Bottom'], 'Region', p) and s.has(el['hook'], p),
#		                                                        Forest13Top
		"Witch's Thicket 13 - Stagnant Blight x10"             : lambda s : s.can_reach(el['Forest13Top'], 'Region', p),
#		                                                        Forest13Top | Forest13Bottom
		"Witch's Thicket 13 To Witch's Thicket 12"             : lambda s : s.can_reach(el['Forest13Top'], 'Region', p) or s.can_reach(el['Forest13Bottom'], 'Region', p),
#		                                                        Forest13Bottom | Forest13Top + LEDGE
		"Witch's Thicket 13 To Witch's Thicket 14"             : lambda s : s.can_reach(el['Forest13Bottom'], 'Region', p) or s.can_reach(el['Forest13Top'], 'Region', p) and macros['LEDGE'](s),
#		                                                        Forest13Right | Forest13Top + claw + unlock + (LEDGE + HORIZONTAL | 2LEDGE)
		"Witch's Thicket 13 To Witch's Thicket 16"             : lambda s : s.can_reach(el['Forest13Right'], 'Region', p) or s.can_reach(el['Forest13Top'], 'Region', p) and s.has(el['claw'], p) and s.has(el['unlock'], p) and (macros['LEDGE'](s) and macros['HORIZONTAL'](s) or macros['2LEDGE'](s)),
#		                                                        Forest14Bottom | Forest14Top | Forest14Left
		"Witch's Thicket 14 - The Parish Way 3"                : lambda s : s.can_reach(el['Forest14Bottom'], 'Region', p) or s.can_reach(el['Forest14Top'], 'Region', p) or s.can_reach(el['Forest14Left'], 'Region', p),
#		                                                        CovenHalls
		"Witch's Thicket 14 To Witch's Thicket 15"             : lambda s : s.can_reach(el['CovenHalls'], 'Location', p),
#		                                                        CovenHalls
		"Witch's Thicket 14 To Witch's Thicket 13"             : lambda s : s.can_reach(el['CovenHalls'], 'Location', p),
#		                                                        Forest14Left | CovenHalls + swim
		"Witch's Thicket 14 To Witch's Thicket 11"             : lambda s : s.can_reach(el['Forest14Left'], 'Region', p) or s.can_reach(el['CovenHalls'], 'Location', p) and s.has(el['swim'], p),
#		                                                        Forest15Top
		"Witch's Thicket 15 - Dark Witch Eleine"               : lambda s : s.can_reach(el['Forest15Top'], 'Region', p),
#		                                                        Forest15Top
		"Witch's Thicket 15 To Witch's Thicket 14"             : lambda s : s.can_reach(el['Forest15Top'], 'Region', p),
#		                                                        Forest16Left
		"Witch's Thicket 16 - Eleine's Diary 3"                : lambda s : s.can_reach(el['Forest16Left'], 'Region', p),
#		                                                        Forest16Left
		"Witch's Thicket 16 - Stone Tablet Fragment"           : lambda s : s.can_reach(el['Forest16Left'], 'Region', p),
#		                                                        Forest16Left
		"Witch's Thicket 16 - Stagnant Blight x800"            : lambda s : s.can_reach(el['Forest16Left'], 'Region', p),
#		                                                        Forest16Left
		"Witch's Thicket 16 To Witch's Thicket 13"             : lambda s : s.can_reach(el['Forest16Left'], 'Region', p),
#		                                                        Forest17Left + (claw | LEDGE)
		"Witch's Thicket 17 - Amulet Gem"                      : lambda s : s.can_reach(el['Forest17Left'], 'Region', p) and (s.has(el['claw'], p) or macros['LEDGE'](s)),
#		                                                        Forest17Left + (claw | LEDGE + hook | silva + djump)
		"Witch's Thicket 17 - Eleine's Diary 2"                : lambda s : s.can_reach(el['Forest17Left'], 'Region', p) and (s.has(el['claw'], p) or macros['LEDGE'](s) and s.has(el['hook'], p) or s.has(el['silva'], p) and s.has(el['djump'], p)),
#		                                                        Forest17Left + (claw | LEDGE)
		"Witch's Thicket 17 - Spellbound Anklet"               : lambda s : s.can_reach(el['Forest17Left'], 'Region', p) and (s.has(el['claw'], p) or macros['LEDGE'](s)),
#		                                                        Forest17Left
		"Witch's Thicket 17 To Witch's Thicket 12"             : lambda s : s.can_reach(el['Forest17Left'], 'Region', p),
#		                                                        Forest17Left
		"Witch's Thicket 17 - Eleine's Diary 1"                : lambda s : s.can_reach(el['Forest17Left'], 'Region', p),
#		                                                        Fort01Left1 | Fort01Right + (LEDGE | hook)
		"Twin Spires 01 - Fallen Sentinel"                     : lambda s : s.can_reach(el['Fort01Left1'], 'Region', p) or s.can_reach(el['Fort01Right'], 'Region', p) and (macros['LEDGE'](s) or s.has(el['hook'], p)),
#		                                                        Fort01Left1
		"Twin Spires 01 - Furious Blight x30"                  : lambda s : s.can_reach(el['Fort01Left1'], 'Region', p),
#		                                                        Fort01Right | Fort01Left1 | Fort01Left2
		"Twin Spires 01 To Twin Spires 03"                     : lambda s : s.can_reach(el['Fort01Right'], 'Region', p) or s.can_reach(el['Fort01Left1'], 'Region', p) or s.can_reach(el['Fort01Left2'], 'Region', p),
#		                                                        Fort01Left2 | Fort01Right + swim
		"Twin Spires 01 To Cliffside Hamlet 15"                : lambda s : s.can_reach(el['Fort01Left2'], 'Region', p) or s.can_reach(el['Fort01Right'], 'Region', p) and s.has(el['swim'], p),
#		                                                        Fort01Left1 | Sentinel + hook
		"Twin Spires 01 To Ruined Castle 07"                   : lambda s : s.can_reach(el['Fort01Left1'], 'Region', p) or s.can_reach(el['Sentinel'], 'Location', p) and s.has(el['hook'], p),
#		                                                        Fort02Left
		"Twin Spires 02 - Stagnant Blight x10"                 : lambda s : s.can_reach(el['Fort02Left'], 'Region', p),
#		                                                        Fort02Right
		"Twin Spires 02 - Furious Blight x10"                  : lambda s : s.can_reach(el['Fort02Right'], 'Region', p),
#		                                                        Fort02Right | Fort02Left + (LEDGE + HORIZONTAL | 2HORIZONTAL | djump + (silva | champion))
		"Twin Spires 02 To Twin Spires 03"                     : lambda s : s.can_reach(el['Fort02Right'], 'Region', p) or s.can_reach(el['Fort02Left'], 'Region', p) and (macros['LEDGE'](s) and macros['HORIZONTAL'](s) or macros['2HORIZONTAL'](s) or s.has(el['djump'], p) and (s.has(el['silva'], p) or s.has(el['champion'], p))),
#		                                                        Fort02Left | Fort02Right + (LEDGE + HORIZONTAL | 2HORIZONTAL | 2LEDGE | sinner | dash + LEDGE | dash + dodge)
		"Twin Spires 02 To Catacombs 22"                       : lambda s : s.can_reach(el['Fort02Left'], 'Region', p) or s.can_reach(el['Fort02Right'], 'Region', p) and (macros['LEDGE'](s) and macros['HORIZONTAL'](s) or macros['2HORIZONTAL'](s) or macros['2LEDGE'](s) or s.has(el['sinner'], p) or s.has(el['dash'], p) and macros['LEDGE'](s) or s.has(el['dash'], p) and s.has(el['dodge'], p)),
#		                                                        Fort03Right | Fort03Left1 | Fort03Left2 | Fort03Top
		"Twin Spires 03 - Bloodied Note 1"                     : lambda s : s.can_reach(el['Fort03Right'], 'Region', p) or s.can_reach(el['Fort03Left1'], 'Region', p) or s.can_reach(el['Fort03Left2'], 'Region', p) or s.can_reach(el['Fort03Top'], 'Region', p),
#		                                                        BastionGates
		"Twin Spires 03 To Twin Spires 04"                     : lambda s : s.can_reach(el['BastionGates'], 'Location', p),
#		                                                        BastionGates + (hook | LEDGE)
		"Twin Spires 03 To Twin Spires 01"                     : lambda s : s.can_reach(el['BastionGates'], 'Location', p) and (s.has(el['hook'], p) or macros['LEDGE'](s)),
#		                                                        BastionGates
		"Twin Spires 03 To Twin Spires 02"                     : lambda s : s.can_reach(el['BastionGates'], 'Location', p),
#		                                                        BastionGates + claw
		"Twin Spires 03 To Twin Spires 05"                     : lambda s : s.can_reach(el['BastionGates'], 'Location', p) and s.has(el['claw'], p),
#		                                                        Fort04Left + (CHARGE + (LEDGE | claw | HORIZONTAL))
		"Twin Spires 04 - Stagnant Blight x100"                : lambda s : s.can_reach(el['Fort04Left'], 'Region', p) and (macros['CHARGE'](s) and (macros['LEDGE'](s) or s.has(el['claw'], p) or macros['HORIZONTAL'](s))),
#		                                                        Fort04Top | Fort04Left + LEDGE
		"Twin Spires 04 To Twin Spires 05"                     : lambda s : s.can_reach(el['Fort04Top'], 'Region', p) or s.can_reach(el['Fort04Left'], 'Region', p) and macros['LEDGE'](s),
#		                                                        Fort04Left | Fort04Top
		"Twin Spires 04 To Twin Spires 03"                     : lambda s : s.can_reach(el['Fort04Left'], 'Region', p) or s.can_reach(el['Fort04Top'], 'Region', p),
#		                                                        Fort05Right + LEDGE
		"Twin Spires 05 - Amulet Fragment"                     : lambda s : s.can_reach(el['Fort05Right'], 'Region', p) and macros['LEDGE'](s),
#		                                                        Fort05Bottom2 + (LEDGE + (hook | claw))
		"Twin Spires 05 - Chain of Sorcery"                    : lambda s : s.can_reach(el['Fort05Bottom2'], 'Region', p) and (macros['LEDGE'](s) and (s.has(el['hook'], p) or s.has(el['claw'], p))),
#		                                                        Fort05Bottom2 + LEDGE + slam  | Fort05Bottom1
		"Twin Spires 05 - Stagnant Blight x10"                 : lambda s : s.can_reach(el['Fort05Bottom2'], 'Region', p) and macros['LEDGE'](s) and s.has(el['slam'], p) or s.can_reach(el['Fort05Bottom1'], 'Region', p),
#		                                                        Fort05Bottom2 | Fort05Right
		"Twin Spires 05 To Twin Spires 04"                     : lambda s : s.can_reach(el['Fort05Bottom2'], 'Region', p) or s.can_reach(el['Fort05Right'], 'Region', p),
#		                                                        Fort05Right | Fort05Bottom2 + LEDGE
		"Twin Spires 05 To Twin Spires 06"                     : lambda s : s.can_reach(el['Fort05Right'], 'Region', p) or s.can_reach(el['Fort05Bottom2'], 'Region', p) and macros['LEDGE'](s),
#		                                                        Fort05Bottom1 | Fort05Bottom2 + LEDGE
		"Twin Spires 05 To Twin Spires 03"                     : lambda s : s.can_reach(el['Fort05Bottom1'], 'Region', p) or s.can_reach(el['Fort05Bottom2'], 'Region', p) and macros['LEDGE'](s),
#		                                                        Fort05Bottom2 + LEDGE + claw
		"Twin Spires 05 To Twin Spires 15"                     : lambda s : s.can_reach(el['Fort05Bottom2'], 'Region', p) and macros['LEDGE'](s) and s.has(el['claw'], p),
#		                                                        Fort06Right + (LEDGE +  claw)
		"Twin Spires 06 - Stagnant Blight x30"                 : lambda s : s.can_reach(el['Fort06Right'], 'Region', p) and (macros['LEDGE'](s) and s.has(el['claw'], p)),
#		                                                        Fort06Left | Fort06Bottom | Fort06Right + (LEDGE | HORIZONTAL | dash)
		"Twin Spires 06 To Twin Spires 05"                     : lambda s : s.can_reach(el['Fort06Left'], 'Region', p) or s.can_reach(el['Fort06Bottom'], 'Region', p) or s.can_reach(el['Fort06Right'], 'Region', p) and (macros['LEDGE'](s) or macros['HORIZONTAL'](s) or s.has(el['dash'], p)),
#		                                                        Fort06Right | Fort06Left + (LEDGE | HORIZONTAL | dash)
		"Twin Spires 06 To Twin Spires 07"                     : lambda s : s.can_reach(el['Fort06Right'], 'Region', p) or s.can_reach(el['Fort06Left'], 'Region', p) and (macros['LEDGE'](s) or macros['HORIZONTAL'](s) or s.has(el['dash'], p)),
#		                                                        Fort06Bottom | Fort06Left | Fort06Right
		"Twin Spires 06 To Twin Spires 10"                     : lambda s : s.can_reach(el['Fort06Bottom'], 'Region', p) or s.can_reach(el['Fort06Left'], 'Region', p) or s.can_reach(el['Fort06Right'], 'Region', p),
#		                                                        Fort07Bottom1 + (LEDGE | claw)
		"Twin Spires 07 - Stagnant Blight x10"                 : lambda s : s.can_reach(el['Fort07Bottom1'], 'Region', p) and (macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                        Fort07Right | Fort07Bottom1 | Fort07Top | Fort07Bottom2  + claw
		"Twin Spires 07 To Twin Spires 09 Left"                : lambda s : s.can_reach(el['Fort07Right'], 'Region', p) or s.can_reach(el['Fort07Bottom1'], 'Region', p) or s.can_reach(el['Fort07Top'], 'Region', p) or s.can_reach(el['Fort07Bottom2'], 'Region', p) and s.has(el['claw'], p),
#		                                                        Fort07Right | Fort07Top
		"Twin Spires 07 To Twin Spires 08"                     : lambda s : s.can_reach(el['Fort07Right'], 'Region', p) or s.can_reach(el['Fort07Top'], 'Region', p),
#		                                                        Fort07Left | Fort07Top + LEDGE
		"Twin Spires 07 To Twin Spires 06"                     : lambda s : s.can_reach(el['Fort07Left'], 'Region', p) or s.can_reach(el['Fort07Top'], 'Region', p) and macros['LEDGE'](s),
#		                                                        Fort07Top | Fort07Bottom1 | Fort07Left + (LEDGE | claw) | Fort07Right
		"Twin Spires 07 To Twin Spires 11"                     : lambda s : s.can_reach(el['Fort07Top'], 'Region', p) or s.can_reach(el['Fort07Bottom1'], 'Region', p) or s.can_reach(el['Fort07Left'], 'Region', p) and (macros['LEDGE'](s) or s.has(el['claw'], p)) or s.can_reach(el['Fort07Right'], 'Region', p),
#		                                                        Fort07Bottom2 | Fort07Bottom1 + claw
		"Twin Spires 07 To Twin Spires 09 Right"               : lambda s : s.can_reach(el['Fort07Bottom2'], 'Region', p) or s.can_reach(el['Fort07Bottom1'], 'Region', p) and s.has(el['claw'], p),
#		                                                        Fort08Left
		"Twin Spires 08 - Hoenir's Diary 3"                    : lambda s : s.can_reach(el['Fort08Left'], 'Region', p),
#		                                                        Fort08Left | SecondSpireChamber
		"Twin Spires 08 To Twin Spires 07"                     : lambda s : s.can_reach(el['Fort08Left'], 'Region', p) or s.can_reach(el['SecondSpireChamber'], 'Location', p),
#		                                                        Fort09Left
		"Twin Spires 09 - Note on the Castle Wall"             : lambda s : s.can_reach(el['Fort09Left'], 'Region', p),
#		                                                        Fort09Left + CHARGE
		"Twin Spires 09 - Snowdrop Bracelet"                   : lambda s : s.can_reach(el['Fort09Left'], 'Region', p) and macros['CHARGE'](s),
#		                                                        Fort09Top1
		"Twin Spires 09 - Stagnant Blight x10"                 : lambda s : s.can_reach(el['Fort09Top1'], 'Region', p),
#		                                                        Fort09Top2
		"Twin Spires 09 - Furious Blight x30"                  : lambda s : s.can_reach(el['Fort09Top2'], 'Region', p),
#		                                                        Fort09Right | Fort09Top1 + claw
		"Twin Spires 09 To Hinterlands 03"                     : lambda s : s.can_reach(el['Fort09Right'], 'Region', p) or s.can_reach(el['Fort09Top1'], 'Region', p) and s.has(el['claw'], p),
#		                                                        Fort09Left | Fort09Right | Fort09Top1 | Fort09Top2
		"Twin Spires 09 To Twin Spires 10"                     : lambda s : s.can_reach(el['Fort09Left'], 'Region', p) or s.can_reach(el['Fort09Right'], 'Region', p) or s.can_reach(el['Fort09Top1'], 'Region', p) or s.can_reach(el['Fort09Top2'], 'Region', p),
#		                                                        Fort09Top1 | Fort09Left + (LEDGE | hook)
		"Twin Spires 09 To Twin Spires 07 Left"                : lambda s : s.can_reach(el['Fort09Top1'], 'Region', p) or s.can_reach(el['Fort09Left'], 'Region', p) and (macros['LEDGE'](s) or s.has(el['hook'], p)),
#		                                                        Fort09Top2 | Fort09Right + LEDGE + claw
		"Twin Spires 09 To Twin Spires 07 Right"               : lambda s : s.can_reach(el['Fort09Top2'], 'Region', p) or s.can_reach(el['Fort09Right'], 'Region', p) and macros['LEDGE'](s) and s.has(el['claw'], p),
#		                                                        Courtyard + claw + LEDGE
		"Twin Spires 10 - Amulet Fragment"                     : lambda s : s.can_reach(el['Courtyard'], 'Location', p) and s.has(el['claw'], p) and macros['LEDGE'](s),
#		                                                        Fort10Right | Fort10Top
		"Twin Spires 10 - Bloodied Note 2"                     : lambda s : s.can_reach(el['Fort10Right'], 'Region', p) or s.can_reach(el['Fort10Top'], 'Region', p),
#		                                                        Courtyard
		"Twin Spires 10 To Twin Spires 09"                     : lambda s : s.can_reach(el['Courtyard'], 'Location', p),
#		                                                        Courtyard + claw + LEDGE
		"Twin Spires 10 To Twin Spires 06"                     : lambda s : s.can_reach(el['Courtyard'], 'Location', p) and s.has(el['claw'], p) and macros['LEDGE'](s),
#		                                                        slam + swim + (Fort11Stagnant | Fort11Bottom + (LEDGE + (sinner | dodge + claw) | 2LEDGE))
		"Twin Spires 11 - Ricorus' Ring"                       : lambda s : s.has(el['slam'], p) and s.has(el['swim'], p) and (s.can_reach(el['Fort11Stagnant'], 'Location', p) or s.can_reach(el['Fort11Bottom'], 'Region', p) and (macros['LEDGE'](s) and (s.has(el['sinner'], p) or s.has(el['dodge'], p) and s.has(el['claw'], p)) or macros['2LEDGE'](s))),
#		                                                        Fort11Top2 | Fort11Bottom + (LEDGE + (sinner | dodge + claw) | 2LEDGE) + (hook | 2LEDGE + claw | 3LEDGE)
		"Twin Spires 11 - Stagnant Blight x30"                 : lambda s : s.can_reach(el['Fort11Top2'], 'Region', p) or s.can_reach(el['Fort11Bottom'], 'Region', p) and (macros['LEDGE'](s) and (s.has(el['sinner'], p) or s.has(el['dodge'], p) and s.has(el['claw'], p)) or macros['2LEDGE'](s)) and (s.has(el['hook'], p) or macros['2LEDGE'](s) and s.has(el['claw'], p) or macros['3LEDGE'](s)),
#		                                                        Fort11Bottom | Fort11Left | Fort11Top1 | Fort11Top2
		"Twin Spires 11 To Twin Spires 07"                     : lambda s : s.can_reach(el['Fort11Bottom'], 'Region', p) or s.can_reach(el['Fort11Left'], 'Region', p) or s.can_reach(el['Fort11Top1'], 'Region', p) or s.can_reach(el['Fort11Top2'], 'Region', p),
#		                                                        Fort11Left | Fort11Bottom + LEDGE | Fort11Top1 + (HORIZONTAL | LEDGE | dash)
		"Twin Spires 11 To Twin Spires 12"                     : lambda s : s.can_reach(el['Fort11Left'], 'Region', p) or s.can_reach(el['Fort11Bottom'], 'Region', p) and macros['LEDGE'](s) or s.can_reach(el['Fort11Top1'], 'Region', p) and (macros['HORIZONTAL'](s) or macros['LEDGE'](s) or s.has(el['dash'], p)),
#		                                                        Fort11Top1 | Fort11Left + (claw | LEDGE | HORIZONTAL | dash)
		"Twin Spires 11 To Twin Spires 13 Left"                : lambda s : s.can_reach(el['Fort11Top1'], 'Region', p) or s.can_reach(el['Fort11Left'], 'Region', p) and (s.has(el['claw'], p) or macros['LEDGE'](s) or macros['HORIZONTAL'](s) or s.has(el['dash'], p)),
#		                                                        Fort11Top2 + claw | Fort11Stagnant + claw
		"Twin Spires 11 To Twin Spires 13 Right"               : lambda s : s.can_reach(el['Fort11Top2'], 'Region', p) and s.has(el['claw'], p) or s.can_reach(el['Fort11Stagnant'], 'Location', p) and s.has(el['claw'], p),
#		                                                        Fort12HP + CHARGE
		"Twin Spires 12 - Forsaken Fellwyrm"                   : lambda s : s.can_reach(el['Fort12HP'], 'Location', p) and macros['CHARGE'](s),
#		                                                        Fort12Top | Fort12Right  + (claw + (LEDGE + HORIZONTAL | 2LEDGE) | 3LEDGE)
		"Twin Spires 12 - Amulet Fragment"                     : lambda s : s.can_reach(el['Fort12Top'], 'Region', p) or s.can_reach(el['Fort12Right'], 'Region', p) and (s.has(el['claw'], p) and (macros['LEDGE'](s) and macros['HORIZONTAL'](s) or macros['2LEDGE'](s)) or macros['3LEDGE'](s)),
#		                                                        Fort12Right | Fort12Left
		"Twin Spires 12 To Twin Spires 11"                     : lambda s : s.can_reach(el['Fort12Right'], 'Region', p) or s.can_reach(el['Fort12Left'], 'Region', p),
#		                                                        Fort12Top + LEDGE + claw
		"Twin Spires 12 To Twin Spires 14"                     : lambda s : s.can_reach(el['Fort12Top'], 'Region', p) and macros['LEDGE'](s) and s.has(el['claw'], p),
#		                                                        Fort12Left | Fort12Right | Fort12Top
		"Twin Spires 12 To Twin Spires 16"                     : lambda s : s.can_reach(el['Fort12Left'], 'Region', p) or s.can_reach(el['Fort12Right'], 'Region', p) or s.can_reach(el['Fort12Top'], 'Region', p),
#		                                                        Fort13Left
		"Twin Spires 13 - Amulet Fragment"                     : lambda s : s.can_reach(el['Fort13Left'], 'Region', p),
#		                                                        Fort13Bottom1 + claw + LEDGE | Fort13Top
		"Twin Spires 13 - Chain of Sorcery"                    : lambda s : s.can_reach(el['Fort13Bottom1'], 'Region', p) and s.has(el['claw'], p) and macros['LEDGE'](s) or s.can_reach(el['Fort13Top'], 'Region', p),
#		                                                        Fort13Bottom1 | Fort13Bottom2 | Fort13Left | Fort13Top
		"Twin Spires 13 To Twin Spires 11 Left"                : lambda s : s.can_reach(el['Fort13Bottom1'], 'Region', p) or s.can_reach(el['Fort13Bottom2'], 'Region', p) or s.can_reach(el['Fort13Left'], 'Region', p) or s.can_reach(el['Fort13Top'], 'Region', p),
#		                                                        Fort13Bottom2 | Fort13Top | Fort13Bottom1
		"Twin Spires 13 To Twin Spires 11 Right"               : lambda s : s.can_reach(el['Fort13Bottom2'], 'Region', p) or s.can_reach(el['Fort13Top'], 'Region', p) or s.can_reach(el['Fort13Bottom1'], 'Region', p),
#		                                                        Fort13Left | Fort13Bottom1 + (LEDGE | claw)
		"Twin Spires 13 To Twin Spires 14"                     : lambda s : s.can_reach(el['Fort13Left'], 'Region', p) or s.can_reach(el['Fort13Bottom1'], 'Region', p) and (macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                        Fort13Top + claw + LEDGE | Fort13Bottom1 + claw + LEDGE
		"Twin Spires 13 To Twin Spires 19"                     : lambda s : s.can_reach(el['Fort13Top'], 'Region', p) and s.has(el['claw'], p) and macros['LEDGE'](s) or s.can_reach(el['Fort13Bottom1'], 'Region', p) and s.has(el['claw'], p) and macros['LEDGE'](s),
#		                                                        Fort14Right + hook + slam + unlock + swim
		"Twin Spires 14 - Writing on the Wall"                 : lambda s : s.can_reach(el['Fort14Right'], 'Region', p) and s.has(el['hook'], p) and s.has(el['slam'], p) and s.has(el['unlock'], p) and s.has(el['swim'], p),
#		                                                        Fort14Right + hook + slam + unlock + swim
		"Twin Spires 14 - Stone Tablet Fragment"               : lambda s : s.can_reach(el['Fort14Right'], 'Region', p) and s.has(el['hook'], p) and s.has(el['slam'], p) and s.has(el['unlock'], p) and s.has(el['swim'], p),
#		                                                        Fort14Bottom + CHARGE
		"Twin Spires 14 - Stagnant Blight x100"                : lambda s : s.can_reach(el['Fort14Bottom'], 'Region', p) and macros['CHARGE'](s),
#		                                                        Fort14Right + hook + slam + unlock + swim
		"Twin Spires 14 - Stagnant Blight x800"                : lambda s : s.can_reach(el['Fort14Right'], 'Region', p) and s.has(el['hook'], p) and s.has(el['slam'], p) and s.has(el['unlock'], p) and s.has(el['swim'], p),
#		                                                        Fort14Right | Fort14Left | Fort14Bottom
		"Twin Spires 14 - Furious Blight x10"                  : lambda s : s.can_reach(el['Fort14Right'], 'Region', p) or s.can_reach(el['Fort14Left'], 'Region', p) or s.can_reach(el['Fort14Bottom'], 'Region', p),
#		                                                        Fort14Left | Fort14Right + (dash | HORIZONTAL | LEDGE)
		"Twin Spires 14 To Twin Spires 15"                     : lambda s : s.can_reach(el['Fort14Left'], 'Region', p) or s.can_reach(el['Fort14Right'], 'Region', p) and (s.has(el['dash'], p) or macros['HORIZONTAL'](s) or macros['LEDGE'](s)),
#		                                                        Fort14Right | Fort14Left | Fort14Bottom
		"Twin Spires 14 To Twin Spires 13"                     : lambda s : s.can_reach(el['Fort14Right'], 'Region', p) or s.can_reach(el['Fort14Left'], 'Region', p) or s.can_reach(el['Fort14Bottom'], 'Region', p),
#		                                                        Fort14Bottom | Fort14Right | Fort14Left
		"Twin Spires 14 To Twin Spires 12"                     : lambda s : s.can_reach(el['Fort14Bottom'], 'Region', p) or s.can_reach(el['Fort14Right'], 'Region', p) or s.can_reach(el['Fort14Left'], 'Region', p),
#		                                                        Fort15Right2
		"Twin Spires 15 - Bloodied Note 3"                     : lambda s : s.can_reach(el['Fort15Right2'], 'Region', p),
#		                                                        Fort15Top + (hook | 2LEDGE)
		"Twin Spires 15 - Immortal's Crest"                    : lambda s : s.can_reach(el['Fort15Top'], 'Region', p) and (s.has(el['hook'], p) or macros['2LEDGE'](s)),
#		                                                        Fort15Right2 + claw | Fort15Top | Fort15Bottom
		"Twin Spires 15 - Stagnant Blight x30"                 : lambda s : s.can_reach(el['Fort15Right2'], 'Region', p) and s.has(el['claw'], p) or s.can_reach(el['Fort15Top'], 'Region', p) or s.can_reach(el['Fort15Bottom'], 'Region', p),
#		                                                        Fort15Right2 + LEDGE
		"Twin Spires 15 - Stagnant Blight x10"                 : lambda s : s.can_reach(el['Fort15Right2'], 'Region', p) and macros['LEDGE'](s),
#		                                                        Fort15Right2 | Fort15Right1 | Fort15Top | Fort15Bottom + LEDGE
		"Twin Spires 15 To Twin Spires 16 Upper"               : lambda s : s.can_reach(el['Fort15Right2'], 'Region', p) or s.can_reach(el['Fort15Right1'], 'Region', p) or s.can_reach(el['Fort15Top'], 'Region', p) or s.can_reach(el['Fort15Bottom'], 'Region', p) and macros['LEDGE'](s),
#		                                                        Fort15Right1 | Fort15Right2 + LEDGE
		"Twin Spires 15 To Twin Spires 14"                     : lambda s : s.can_reach(el['Fort15Right1'], 'Region', p) or s.can_reach(el['Fort15Right2'], 'Region', p) and macros['LEDGE'](s),
#		                                                        Fort15Bottom | Fort15Top
		"Twin Spires 15 To Twin Spires 05"                     : lambda s : s.can_reach(el['Fort15Bottom'], 'Region', p) or s.can_reach(el['Fort15Top'], 'Region', p),
#		                                                        Fort15Top | Fort15Right3 + LEDGE
		"Twin Spires 15 To Twin Spires 17"                     : lambda s : s.can_reach(el['Fort15Top'], 'Region', p) or s.can_reach(el['Fort15Right3'], 'Region', p) and macros['LEDGE'](s),
#		                                                        Fort15Right3 | Fort15Bottom + LEDGE | Fort15Right2
		"Twin Spires 15 To Twin Spires 16 Lower"               : lambda s : s.can_reach(el['Fort15Right3'], 'Region', p) or s.can_reach(el['Fort15Bottom'], 'Region', p) and macros['LEDGE'](s) or s.can_reach(el['Fort15Right2'], 'Region', p),
#		                                                        Fort16Left1 | Fort16Top | Fort16Left2 | Fort16Right
		"Twin Spires 16 - Monument Engraving"                  : lambda s : s.can_reach(el['Fort16Left1'], 'Region', p) or s.can_reach(el['Fort16Top'], 'Region', p) or s.can_reach(el['Fort16Left2'], 'Region', p) or s.can_reach(el['Fort16Right'], 'Region', p),
#		                                                        Fort16Left1
		"Twin Spires 16 To Twin Spires 15 Upper"               : lambda s : s.can_reach(el['Fort16Left1'], 'Region', p),
#		                                                        Fort16Top
		"Twin Spires 16 To Twin Spires 18"                     : lambda s : s.can_reach(el['Fort16Top'], 'Region', p),
#		                                                        Fort16Left2
		"Twin Spires 16 To Twin Spires 15 Lower"               : lambda s : s.can_reach(el['Fort16Left2'], 'Region', p),
#		                                                        Fort16Right
		"Twin Spires 16 To Twin Spires 12"                     : lambda s : s.can_reach(el['Fort16Right'], 'Region', p),
#		                                                        Fort17Bottom
		"Twin Spires 17 - Amulet Fragment"                     : lambda s : s.can_reach(el['Fort17Bottom'], 'Region', p),
#		                                                        Fort17Bottom
		"Twin Spires 17 To Twin Spires 15"                     : lambda s : s.can_reach(el['Fort17Bottom'], 'Region', p),
#		                                                        Fort17Right | Fort17Bottom
		"Twin Spires 17 To Twin Spires 18"                     : lambda s : s.can_reach(el['Fort17Right'], 'Region', p) or s.can_reach(el['Fort17Bottom'], 'Region', p),
#		                                                        Fort18Right + (claw + (sinner | dodge + LEDGE | 2LEDGE | djump + dash))
		"Twin Spires 18 - Amulet Gem"                          : lambda s : s.can_reach(el['Fort18Right'], 'Region', p) and (s.has(el['claw'], p) and (s.has(el['sinner'], p) or s.has(el['dodge'], p) and macros['LEDGE'](s) or macros['2LEDGE'](s) or s.has(el['djump'], p) and s.has(el['dash'], p))),
#		                                                        Fort18Bottom + (LEDGE | claw)
		"Twin Spires 18 - Chain of Sorcery"                    : lambda s : s.can_reach(el['Fort18Bottom'], 'Region', p) and (macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                        Fort18Left | Fort18Right
		"Twin Spires 18 To Twin Spires 17"                     : lambda s : s.can_reach(el['Fort18Left'], 'Region', p) or s.can_reach(el['Fort18Right'], 'Region', p),
#		                                                        Fort18Right | Fort18Left | Fort18Bottom
		"Twin Spires 18 To Twin Spires 19"                     : lambda s : s.can_reach(el['Fort18Right'], 'Region', p) or s.can_reach(el['Fort18Left'], 'Region', p) or s.can_reach(el['Fort18Bottom'], 'Region', p),
#		                                                        Fort18Bottom | Fort18Right
		"Twin Spires 18 To Twin Spires 16"                     : lambda s : s.can_reach(el['Fort18Bottom'], 'Region', p) or s.can_reach(el['Fort18Right'], 'Region', p),
#		                                                        Fort19Top
		"Twin Spires 19 - Ancient Dragon Claw"                 : lambda s : s.can_reach(el['Fort19Top'], 'Region', p),
#		                                                        Fort19Top + claw
		"Twin Spires 19 - Furious Blight x30"                  : lambda s : s.can_reach(el['Fort19Top'], 'Region', p) and s.has(el['claw'], p),
#		                                                        Fort19Left + slam
		"Twin Spires 19 - Furious Blight x10"                  : lambda s : s.can_reach(el['Fort19Left'], 'Region', p) and s.has(el['slam'], p),
#		                                                        Fort19Left | Fort19Top + LEDGE
		"Twin Spires 19 To Twin Spires 18"                     : lambda s : s.can_reach(el['Fort19Left'], 'Region', p) or s.can_reach(el['Fort19Top'], 'Region', p) and macros['LEDGE'](s),
#		                                                        Fort19Top | Fort19Left + LEDGE
		"Twin Spires 19 To Twin Spires 20"                     : lambda s : s.can_reach(el['Fort19Top'], 'Region', p) or s.can_reach(el['Fort19Left'], 'Region', p) and macros['LEDGE'](s),
#		                                                        Fort19Bottom | Fort19Top + claw
		"Twin Spires 19 To Twin Spires 13"                     : lambda s : s.can_reach(el['Fort19Bottom'], 'Region', p) or s.can_reach(el['Fort19Top'], 'Region', p) and s.has(el['claw'], p),
#		                                                        Fort20Bottom | MourningHall
		"Twin Spires 20 To Twin Spires 19"                     : lambda s : s.can_reach(el['Fort20Bottom'], 'Region', p) or s.can_reach(el['MourningHall'], 'Location', p),
#		                                                        Fort20Bottom | Fort20Top
		"MourningHall"                                         : lambda s : s.can_reach(el['Fort20Bottom'], 'Region', p) or s.can_reach(el['Fort20Top'], 'Region', p),
#		                                                        Fort20Top | MourningHall
		"Twin Spires 20 To Twin Spires 21"                     : lambda s : s.can_reach(el['Fort20Top'], 'Region', p) or s.can_reach(el['MourningHall'], 'Location', p),
#		                                                        Fort21Bottom
		"Twin Spires 21 - Ulv, the Mad Knight"                 : lambda s : s.can_reach(el['Fort21Bottom'], 'Region', p),
#		                                                        Ulv + (claw | (silva + djump + (champion | dodge)))
		"Twin Spires 21 - Priestess' Wish"                     : lambda s : s.can_reach(el['Ulv'], 'Location', p) and (s.has(el['claw'], p) or (s.has(el['silva'], p) and s.has(el['djump'], p) and (s.has(el['champion'], p) or s.has(el['dodge'], p)))),
#		                                                        Ulv + (claw | (silva + djump + (champion | dodge)))
		"Twin Spires 21 - White Priestess' Bastion Letter"     : lambda s : s.can_reach(el['Ulv'], 'Location', p) and (s.has(el['claw'], p) or (s.has(el['silva'], p) and s.has(el['djump'], p) and (s.has(el['champion'], p) or s.has(el['dodge'], p)))),
#		                                                        Fort21Bottom
		"Twin Spires 21 To Twin Spires 20"                     : lambda s : s.can_reach(el['Fort21Bottom'], 'Region', p),
#		                                                        Oubliette01Left + swim
		"Stockade 01 - Amulet Fragment"                        : lambda s : s.can_reach(el['Oubliette01Left'], 'Region', p) and s.has(el['swim'], p),
#		                                                        Oubliette01Left + swim
		"Stockade 01 - Stagnant Blight x10"                    : lambda s : s.can_reach(el['Oubliette01Left'], 'Region', p) and s.has(el['swim'], p),
#		                                                        Oubliette01Left | Oubliette01Right + swim
		"Stockade 01 To Witch's Thicket 07"                    : lambda s : s.can_reach(el['Oubliette01Left'], 'Region', p) or s.can_reach(el['Oubliette01Right'], 'Region', p) and s.has(el['swim'], p),
#		                                                        Oubliette01Right | Oubliette01Left + swim
		"Stockade 01 To Stockade 02"                           : lambda s : s.can_reach(el['Oubliette01Right'], 'Region', p) or s.can_reach(el['Oubliette01Left'], 'Region', p) and s.has(el['swim'], p),
#		                                                        Oubliette02Left | Oubliette02Right1 | Oubliette02Right2
		"Stockade 02 - Executioner's Vow"                      : lambda s : s.can_reach(el['Oubliette02Left'], 'Region', p) or s.can_reach(el['Oubliette02Right1'], 'Region', p) or s.can_reach(el['Oubliette02Right2'], 'Region', p),
#		                                                        Oubliette02Left | Aqueduct + (LEDGE | claw)
		"Stockade 02 To Stockade 01"                           : lambda s : s.can_reach(el['Oubliette02Left'], 'Region', p) or s.can_reach(el['Aqueduct'], 'Location', p) and (macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                        Oubliette02Right1 | Aqueduct
		"Stockade 02 To Stockade 05"                           : lambda s : s.can_reach(el['Oubliette02Right1'], 'Region', p) or s.can_reach(el['Aqueduct'], 'Location', p),
#		                                                        Oubliette02Right2 | Aqueduct
		"Stockade 02 To Stockade 04"                           : lambda s : s.can_reach(el['Oubliette02Right2'], 'Region', p) or s.can_reach(el['Aqueduct'], 'Location', p),
#		                                                        Oubliette03Left + swim
		"Stockade 03 - Right Stagnant Blight x10"              : lambda s : s.can_reach(el['Oubliette03Left'], 'Region', p) and s.has(el['swim'], p),
#		                                                        Oubliette03Left + swim
		"Stockade 03 - Left Stagnant Blight x10"               : lambda s : s.can_reach(el['Oubliette03Left'], 'Region', p) and s.has(el['swim'], p),
#		                                                        Oubliette03Left | Oubliette03Right + swim
		"Stockade 03 To Stockade 04"                           : lambda s : s.can_reach(el['Oubliette03Left'], 'Region', p) or s.can_reach(el['Oubliette03Right'], 'Region', p) and s.has(el['swim'], p),
#		                                                        Oubliette03Right | Oubliette03Left + swim | Oubliette03Top + (LEDGE | claw | swim)
		"Stockade 03 To Stockade 10"                           : lambda s : s.can_reach(el['Oubliette03Right'], 'Region', p) or s.can_reach(el['Oubliette03Left'], 'Region', p) and s.has(el['swim'], p) or s.can_reach(el['Oubliette03Top'], 'Region', p) and (macros['LEDGE'](s) or s.has(el['claw'], p) or s.has(el['swim'], p)),
#		                                                        Oubliette03Top | Oubliette03Right + hook
		"Stockade 03 To Stockade 05"                           : lambda s : s.can_reach(el['Oubliette03Top'], 'Region', p) or s.can_reach(el['Oubliette03Right'], 'Region', p) and s.has(el['hook'], p),
#		                                                        Oubliette03Right + CHARGE
		"Stockade 03 - Stagnant Blight x800"                   : lambda s : s.can_reach(el['Oubliette03Right'], 'Region', p) and macros['CHARGE'](s),
#		                                                        Oubliette04Left + (FULLSILVA | hook | 3LEDGE | sinner + silva + djump | silva + champion + dodge | 2HORIZONTAL + dash + LEDGE | djump + champion + HORIZONTAL)
		"Stockade 04 - Stagnant Blight x30"                    : lambda s : s.can_reach(el['Oubliette04Left'], 'Region', p) and (macros['FULLSILVA'](s) or s.has(el['hook'], p) or macros['3LEDGE'](s) or s.has(el['sinner'], p) and s.has(el['silva'], p) and s.has(el['djump'], p) or s.has(el['silva'], p) and s.has(el['champion'], p) and s.has(el['dodge'], p) or macros['2HORIZONTAL'](s) and s.has(el['dash'], p) and macros['LEDGE'](s) or s.has(el['djump'], p) and s.has(el['champion'], p) and macros['HORIZONTAL'](s)),
#		                                                        Oubliette04Right | Oubliette04Left
		"Stockade 04 - Furious Blight x10"                     : lambda s : s.can_reach(el['Oubliette04Right'], 'Region', p) or s.can_reach(el['Oubliette04Left'], 'Region', p),
#		                                                        Oubliette04Right | Oubliette04Left
		"Stockade 04 To Stockade 03"                           : lambda s : s.can_reach(el['Oubliette04Right'], 'Region', p) or s.can_reach(el['Oubliette04Left'], 'Region', p),
#		                                                        Oubliette04Right + (claw | hook | LEDGE) | Oubliette04Left
		"Stockade 04 To Stockade 02"                           : lambda s : s.can_reach(el['Oubliette04Right'], 'Region', p) and (s.has(el['claw'], p) or s.has(el['hook'], p) or macros['LEDGE'](s)) or s.can_reach(el['Oubliette04Left'], 'Region', p),
#		                                                        Oubliette051Bottom
		"Stockade 05_1 To Stockade 05"                         : lambda s : s.can_reach(el['Oubliette051Bottom'], 'Region', p),
#		                                                        Oubliette051Bottom
		"Stockade 05_1 - Furious Blight x10"                   : lambda s : s.can_reach(el['Oubliette051Bottom'], 'Region', p),
#		                                                        Oubliette052Bottom1 | Oubliette052Bottom2
		"Stockade 05_2 To Stockade 05 Left"                    : lambda s : s.can_reach(el['Oubliette052Bottom1'], 'Region', p) or s.can_reach(el['Oubliette052Bottom2'], 'Region', p),
#		                                                        Oubliette052Bottom1 + (LEDGE + claw + hook)
		"Stockade 05_2 - Stagnant Blight x10"                  : lambda s : s.can_reach(el['Oubliette052Bottom1'], 'Region', p) and (macros['LEDGE'](s) and s.has(el['claw'], p) and s.has(el['hook'], p)),
#		                                                        Oubliette052Bottom2 | Oubliette052Bottom1 + (LEDGE + claw + hook)
		"Stockade 05_2 To Stockade 05 Right"                   : lambda s : s.can_reach(el['Oubliette052Bottom2'], 'Region', p) or s.can_reach(el['Oubliette052Bottom1'], 'Region', p) and (macros['LEDGE'](s) and s.has(el['claw'], p) and s.has(el['hook'], p)),
#		                                                        Oubliette053Top
		"Stockade 05_3 - Chain of Sorcery"                     : lambda s : s.can_reach(el['Oubliette053Top'], 'Region', p),
#		                                                        Oubliette053Top
		"Stockade 05_3 To Stockade 05"                         : lambda s : s.can_reach(el['Oubliette053Top'], 'Region', p),
#		                                                        Oubliette05Top4
		"Stockade 05 - Amulet Gem"                             : lambda s : s.can_reach(el['Oubliette05Top4'], 'Region', p),
#		                                                        Oubliette05Top2 | Oubliette05Top1
		"Stockade 05 To Stockade 05_2 Left"                    : lambda s : s.can_reach(el['Oubliette05Top2'], 'Region', p) or s.can_reach(el['Oubliette05Top1'], 'Region', p),
#		                                                        Oubliette05Bottom2 | Oubliette05Left
		"Stockade 05 To Stockade 05_3"                         : lambda s : s.can_reach(el['Oubliette05Bottom2'], 'Region', p) or s.can_reach(el['Oubliette05Left'], 'Region', p),
#		                                                        Oubliette05Top3 | Oubliette05Top1
		"Stockade 05 To Stockade 07_2"                         : lambda s : s.can_reach(el['Oubliette05Top3'], 'Region', p) or s.can_reach(el['Oubliette05Top1'], 'Region', p),
#		                                                        Oubliette05Top1 | Oubliette05Left + LEDGE
		"Stockade 05 To Stockade 05_1"                         : lambda s : s.can_reach(el['Oubliette05Top1'], 'Region', p) or s.can_reach(el['Oubliette05Left'], 'Region', p) and macros['LEDGE'](s),
#		                                                        Oubliette05Bottom1 | Oubliette05Left
		"Stockade 05 To Stockade 07_1"                         : lambda s : s.can_reach(el['Oubliette05Bottom1'], 'Region', p) or s.can_reach(el['Oubliette05Left'], 'Region', p),
#		                                                        Oubliette05Top1 + CHARGE
		"Stockade 05 - Stagnant Blight x100"                   : lambda s : s.can_reach(el['Oubliette05Top1'], 'Region', p) and macros['CHARGE'](s),
#		                                                        Oubliette05Top4
		"Stockade 05 - Stagnant Blight x30"                    : lambda s : s.can_reach(el['Oubliette05Top4'], 'Region', p),
#		                                                        Oubliette05Left | Oubliette05Right | Oubliette05Top1
		"Stockade 05 To Stockade 02"                           : lambda s : s.can_reach(el['Oubliette05Left'], 'Region', p) or s.can_reach(el['Oubliette05Right'], 'Region', p) or s.can_reach(el['Oubliette05Top1'], 'Region', p),
#		                                                        Oubliette05Right | Oubliette05Top4 + slam
		"Stockade 05 To Stockade 06"                           : lambda s : s.can_reach(el['Oubliette05Right'], 'Region', p) or s.can_reach(el['Oubliette05Top4'], 'Region', p) and s.has(el['slam'], p),
#		                                                        Oubliette05Bottom3 | Oubliette05Left
		"Stockade 05 To Stockade 03"                           : lambda s : s.can_reach(el['Oubliette05Bottom3'], 'Region', p) or s.can_reach(el['Oubliette05Left'], 'Region', p),
#		                                                        Oubliette05Top4
		"Stockade 05 To Stockade 05_2 Right"                   : lambda s : s.can_reach(el['Oubliette05Top4'], 'Region', p),
#		                                                        Oubliette061Left
		"Stockade 06_1 - Hoenir's Diary 1"                     : lambda s : s.can_reach(el['Oubliette061Left'], 'Region', p),
#		                                                        Oubliette061Left | Cells
		"Stockade 06_1 To Stockade 07"                         : lambda s : s.can_reach(el['Oubliette061Left'], 'Region', p) or s.can_reach(el['Cells'], 'Location', p),
#		                                                        Oubliette062Bottom2 + swim
		"Stockade 06_2 - Executioner's Gloves"                 : lambda s : s.can_reach(el['Oubliette062Bottom2'], 'Region', p) and s.has(el['swim'], p),
#		                                                        Oubliette062Bottom2
		"Stockade 06_2 To Stockade 07"                         : lambda s : s.can_reach(el['Oubliette062Bottom2'], 'Region', p),
#		                                                        Oubliette063Left1
		"Stockade 06_3 - Chain of Sorcery"                     : lambda s : s.can_reach(el['Oubliette063Left1'], 'Region', p),
#		                                                        Oubliette063Left1
		"Stockade 06_3 To Stockade 07"                         : lambda s : s.can_reach(el['Oubliette063Left1'], 'Region', p),
#		                                                        Oubliette064Top
		"Stockade 06_4 - Stone Tablet Fragment"                : lambda s : s.can_reach(el['Oubliette064Top'], 'Region', p),
#		                                                        Oubliette064Top
		"Stockade 06_4 To Stockade 07"                         : lambda s : s.can_reach(el['Oubliette064Top'], 'Region', p),
#		                                                        Oubliette06Bottom
		"Stockade 06 - Amulet Fragment"                        : lambda s : s.can_reach(el['Oubliette06Bottom'], 'Region', p),
#		                                                        Oubliette06Bottom + hook
		"Stockade 06 - Chain of Sorcery"                       : lambda s : s.can_reach(el['Oubliette06Bottom'], 'Region', p) and s.has(el['hook'], p),
#		                                                        Oubliette06Bottom
		"Stockade 06 - Stagnant Blight x10"                    : lambda s : s.can_reach(el['Oubliette06Bottom'], 'Region', p),
#		                                                        Oubliette06Left | Oubliette06Bottom + hook
		"Stockade 06 To Stockade 05"                           : lambda s : s.can_reach(el['Oubliette06Left'], 'Region', p) or s.can_reach(el['Oubliette06Bottom'], 'Region', p) and s.has(el['hook'], p),
#		                                                        Oubliette06Right | Oubliette06Bottom + hook
		"Stockade 06 To Stockade 07"                           : lambda s : s.can_reach(el['Oubliette06Right'], 'Region', p) or s.can_reach(el['Oubliette06Bottom'], 'Region', p) and s.has(el['hook'], p),
#		                                                        Oubliette06Bottom | Oubliette06Right | Oubliette06Left
		"Stockade 06 To Stockade 10"                           : lambda s : s.can_reach(el['Oubliette06Bottom'], 'Region', p) or s.can_reach(el['Oubliette06Right'], 'Region', p) or s.can_reach(el['Oubliette06Left'], 'Region', p),
#		                                                        Oubliette071Top
		"Stockade 07_1 - Forbidden Text Scrap"                 : lambda s : s.can_reach(el['Oubliette071Top'], 'Region', p),
#		                                                        Oubliette071Top
		"Stockade 07_1 To Stockade 05"                         : lambda s : s.can_reach(el['Oubliette071Top'], 'Region', p),
#		                                                        Oubliette072Bottom
		"Stockade 07_2 - Hidden Test Subject"                  : lambda s : s.can_reach(el['Oubliette072Bottom'], 'Region', p),
#		                                                        Oubliette072Bottom
		"Stockade 07_2 To Stockade 05"                         : lambda s : s.can_reach(el['Oubliette072Bottom'], 'Region', p),
#		                                                        Oubliette07Right1 | Oubliette07Bottom1 + (hook | LEDGE)
		"Stockade 07 To Stockade 06_1"                         : lambda s : s.can_reach(el['Oubliette07Right1'], 'Region', p) or s.can_reach(el['Oubliette07Bottom1'], 'Region', p) and (s.has(el['hook'], p) or macros['LEDGE'](s)),
#		                                                        Oubliette07Left1 | Oubliette07Bottom1 + (hook + (LEDGE | HORIZONTAL) | silva + djump)
		"Stockade 07 To Stockade 06_3"                         : lambda s : s.can_reach(el['Oubliette07Left1'], 'Region', p) or s.can_reach(el['Oubliette07Bottom1'], 'Region', p) and (s.has(el['hook'], p) and (macros['LEDGE'](s) or macros['HORIZONTAL'](s)) or s.has(el['silva'], p) and s.has(el['djump'], p)),
#		                                                        Oubliette07Bottom2 | Oubliette07Bottom1
		"Stockade 07 To Stockade 06_2"                         : lambda s : s.can_reach(el['Oubliette07Bottom2'], 'Region', p) or s.can_reach(el['Oubliette07Bottom1'], 'Region', p),
#		                                                        Oubliette07Top | Oubliette07Left1 + unlock + (hook | claw + (3LEDGE | FULLSILVA))
		"Stockade 07 To Stockade 06_4"                         : lambda s : s.can_reach(el['Oubliette07Top'], 'Region', p) or s.can_reach(el['Oubliette07Left1'], 'Region', p) and s.has(el['unlock'], p) and (s.has(el['hook'], p) or s.has(el['claw'], p) and (macros['3LEDGE'](s) or macros['FULLSILVA'](s))),
#		                                                        Oubliette07Left2
		"Stockade 07 To Stockade 06"                           : lambda s : s.can_reach(el['Oubliette07Left2'], 'Region', p),
#		                                                        Oubliette07Right2 | Oubliette07Bottom1
		"Stockade 07 To Stockade 13"                           : lambda s : s.can_reach(el['Oubliette07Right2'], 'Region', p) or s.can_reach(el['Oubliette07Bottom1'], 'Region', p),
#		                                                        Oubliette07Bottom1 | Oubliette07Left1 | Oubliette07Left2 | Oubliette07Bottom2 | Oubliette07Right1 | Oubliette07Right2
		"Stockade 07 To Stockade 09"                           : lambda s : s.can_reach(el['Oubliette07Bottom1'], 'Region', p) or s.can_reach(el['Oubliette07Left1'], 'Region', p) or s.can_reach(el['Oubliette07Left2'], 'Region', p) or s.can_reach(el['Oubliette07Bottom2'], 'Region', p) or s.can_reach(el['Oubliette07Right1'], 'Region', p) or s.can_reach(el['Oubliette07Right2'], 'Region', p),
#		                                                        slam + (Oubliette08Top | Oubliette08Right + (hook | LEDGE | HORIZONTAL))
		"Stockade 08 - Lower Furious Blight x30"               : lambda s : s.has(el['slam'], p) and (s.can_reach(el['Oubliette08Top'], 'Region', p) or s.can_reach(el['Oubliette08Right'], 'Region', p) and (s.has(el['hook'], p) or macros['LEDGE'](s) or macros['HORIZONTAL'](s))),
#		                                                        Oubliette08Left + hook
		"Stockade 08 - Upper Furious Blight x30"               : lambda s : s.can_reach(el['Oubliette08Left'], 'Region', p) and s.has(el['hook'], p),
#		                                                        Oubliette08Right | Oubliette08Left + LEDGE
		"Stockade 08 To Stockade 11"                           : lambda s : s.can_reach(el['Oubliette08Right'], 'Region', p) or s.can_reach(el['Oubliette08Left'], 'Region', p) and macros['LEDGE'](s),
#		                                                        Oubliette08Left | Oubliette08Right | Oubliette08Top
		"Stockade 08 To Stockade 09"                           : lambda s : s.can_reach(el['Oubliette08Left'], 'Region', p) or s.can_reach(el['Oubliette08Right'], 'Region', p) or s.can_reach(el['Oubliette08Top'], 'Region', p),
#		                                                        Oubliette08Top | Oubliette08Right + hook
		"Stockade 08 To Stockade 13"                           : lambda s : s.can_reach(el['Oubliette08Top'], 'Region', p) or s.can_reach(el['Oubliette08Right'], 'Region', p) and s.has(el['hook'], p),
#		                                                        Oubliette09Top + claw
		"Stockade 09 - Right Amulet Fragment"                  : lambda s : s.can_reach(el['Oubliette09Top'], 'Region', p) and s.has(el['claw'], p),
#		                                                        Oubliette09Top + claw
		"Stockade 09 - Left Amulet Fragment"                   : lambda s : s.can_reach(el['Oubliette09Top'], 'Region', p) and s.has(el['claw'], p),
#		                                                        Oubliette09Top + swim
		"Stockade 09 - Stagnant Blight x30"                    : lambda s : s.can_reach(el['Oubliette09Top'], 'Region', p) and s.has(el['swim'], p),
#		                                                        Oubliette09Right | Oubliette09Top + swim + HORIZONTAL
		"Stockade 09 To Stockade 08"                           : lambda s : s.can_reach(el['Oubliette09Right'], 'Region', p) or s.can_reach(el['Oubliette09Top'], 'Region', p) and s.has(el['swim'], p) and macros['HORIZONTAL'](s),
#		                                                        Oubliette09Left | Oubliette09Top + swim
		"Stockade 09 To Stockade 10"                           : lambda s : s.can_reach(el['Oubliette09Left'], 'Region', p) or s.can_reach(el['Oubliette09Top'], 'Region', p) and s.has(el['swim'], p),
#		                                                        Oubliette09Top | Oubliette09Left
		"Stockade 09 To Stockade 07"                           : lambda s : s.can_reach(el['Oubliette09Top'], 'Region', p) or s.can_reach(el['Oubliette09Left'], 'Region', p),
#		                                                        Oubliette10Left1 | Oubliette10Right | Oubliette10Left2 | Oubliette10Top
		"Stockade 10 - Executioner's Missive"                  : lambda s : s.can_reach(el['Oubliette10Left1'], 'Region', p) or s.can_reach(el['Oubliette10Right'], 'Region', p) or s.can_reach(el['Oubliette10Left2'], 'Region', p) or s.can_reach(el['Oubliette10Top'], 'Region', p),
#		                                                        Oubliette10Right | DarkChamber
		"Stockade 10 To Stockade 09"                           : lambda s : s.can_reach(el['Oubliette10Right'], 'Region', p) or s.can_reach(el['DarkChamber'], 'Location', p),
#		                                                        Oubliette10Left1 | DarkChamber
		"Stockade 10 To Stockade 03"                           : lambda s : s.can_reach(el['Oubliette10Left1'], 'Region', p) or s.can_reach(el['DarkChamber'], 'Location', p),
#		                                                        Oubliette10Left2 | DarkChamber + CHARGE
		"Stockade 10 To Stockade 17"                           : lambda s : s.can_reach(el['Oubliette10Left2'], 'Region', p) or s.can_reach(el['DarkChamber'], 'Location', p) and macros['CHARGE'](s),
#		                                                        Oubliette10Top | DarkChamber
		"Stockade 10 To Stockade 06"                           : lambda s : s.can_reach(el['Oubliette10Top'], 'Region', p) or s.can_reach(el['DarkChamber'], 'Location', p),
#		                                                        Oubliette11Left1 + (LEDGE | dash | HORIZONTAL | hook) | Oubliette11Left2 + hook
		"Stockade 11 - Furious Blight x10"                     : lambda s : s.can_reach(el['Oubliette11Left1'], 'Region', p) and (macros['LEDGE'](s) or s.has(el['dash'], p) or macros['HORIZONTAL'](s) or s.has(el['hook'], p)) or s.can_reach(el['Oubliette11Left2'], 'Region', p) and s.has(el['hook'], p),
#		                                                        Oubliette11Right1 | Oubliette11Left1 | Oubliette11Top
		"Stockade 11 To Stockade 12"                           : lambda s : s.can_reach(el['Oubliette11Right1'], 'Region', p) or s.can_reach(el['Oubliette11Left1'], 'Region', p) or s.can_reach(el['Oubliette11Top'], 'Region', p),
#		                                                        Oubliette11Left2 | Oubliette11Left1 | Oubliette11Right1 | Oubliette11Top | Oubliette11Right2
		"Stockade 11 To Stockade 08"                           : lambda s : s.can_reach(el['Oubliette11Left2'], 'Region', p) or s.can_reach(el['Oubliette11Left1'], 'Region', p) or s.can_reach(el['Oubliette11Right1'], 'Region', p) or s.can_reach(el['Oubliette11Top'], 'Region', p) or s.can_reach(el['Oubliette11Right2'], 'Region', p),
#		                                                        Oubliette11Right2 | Oubliette11Left2
		"Stockade 11 To Stockade 14"                           : lambda s : s.can_reach(el['Oubliette11Right2'], 'Region', p) or s.can_reach(el['Oubliette11Left2'], 'Region', p),
#		                                                        Oubliette11Left1 | Oubliette11Left2 + hook | Oubliette11Right2 + (HORIZONTAL | LEDGE)
		"Stockade 11 To Stockade 13"                           : lambda s : s.can_reach(el['Oubliette11Left1'], 'Region', p) or s.can_reach(el['Oubliette11Left2'], 'Region', p) and s.has(el['hook'], p) or s.can_reach(el['Oubliette11Right2'], 'Region', p) and (macros['HORIZONTAL'](s) or macros['LEDGE'](s)),
#		                                                        Oubliette11Bottom | Oubliette11Left1 + slam
		"Stockade 11 To Stockade 13_2"                         : lambda s : s.can_reach(el['Oubliette11Bottom'], 'Region', p) or s.can_reach(el['Oubliette11Left1'], 'Region', p) and s.has(el['slam'], p),
#		                                                        Oubliette11Top | Oubliette11Left1 + claw + (FULLSILVA | (hook + (HORIZONTAL | LEDGE)))
		"Stockade 11 To Stockade 13_1"                         : lambda s : s.can_reach(el['Oubliette11Top'], 'Region', p) or s.can_reach(el['Oubliette11Left1'], 'Region', p) and s.has(el['claw'], p) and (macros['FULLSILVA'](s) or (s.has(el['hook'], p) and (macros['HORIZONTAL'](s) or macros['LEDGE'](s)))),
#		                                                        Oubliette12Left
		"Stockade 12 - Dark Executioner"                       : lambda s : s.can_reach(el['Oubliette12Left'], 'Region', p),
#		                                                        Oubliette12Left | Executioner
		"Stockade 12 To Stockade 11"                           : lambda s : s.can_reach(el['Oubliette12Left'], 'Region', p) or s.can_reach(el['Executioner'], 'Location', p),
#		                                                        Oubliette131Bottom
		"Stockade 13_1 - Aura's Ring"                          : lambda s : s.can_reach(el['Oubliette131Bottom'], 'Region', p),
#		                                                        Oubliette131Bottom
		"Stockade 13_1 To Stockade 11"                         : lambda s : s.can_reach(el['Oubliette131Bottom'], 'Region', p),
#		                                                        Oubliette132Top
		"Stockade 13_2 - Ancient Soul x1"                      : lambda s : s.can_reach(el['Oubliette132Top'], 'Region', p),
#		                                                        Oubliette132Top
		"Stockade 13_2 To Stockade 11"                         : lambda s : s.can_reach(el['Oubliette132Top'], 'Region', p),
#		                                                        Oubliette13Right + (claw + LEDGE | 2LEDGE | hook)
		"Stockade 13 - Chain of Sorcery"                       : lambda s : s.can_reach(el['Oubliette13Right'], 'Region', p) and (s.has(el['claw'], p) and macros['LEDGE'](s) or macros['2LEDGE'](s) or s.has(el['hook'], p)),
#		                                                        Oubliette13Left
		"Stockade 13 - Slip of Paper"                          : lambda s : s.can_reach(el['Oubliette13Left'], 'Region', p),
#		                                                        Oubliette13Left
		"Stockade 13 - Stagnant Blight x30"                    : lambda s : s.can_reach(el['Oubliette13Left'], 'Region', p),
#		                                                        Oubliette13Left + CHARGE + (LEDGE | HORIZONTAL | hook | dash | claw)
		"Stockade 13 - Stagnant Blight x100"                   : lambda s : s.can_reach(el['Oubliette13Left'], 'Region', p) and macros['CHARGE'](s) and (macros['LEDGE'](s) or macros['HORIZONTAL'](s) or s.has(el['hook'], p) or s.has(el['dash'], p) or s.has(el['claw'], p)),
#		                                                        Oubliette13Bottom | Oubliette13Right
		"Stockade 13 To Stockade 08"                           : lambda s : s.can_reach(el['Oubliette13Bottom'], 'Region', p) or s.can_reach(el['Oubliette13Right'], 'Region', p),
#		                                                        Oubliette13Right | Oubliette13Left
		"Stockade 13 To Stockade 11"                           : lambda s : s.can_reach(el['Oubliette13Right'], 'Region', p) or s.can_reach(el['Oubliette13Left'], 'Region', p),
#		                                                        Oubliette13Left | Oubliette13Right + (hook | LEDGE + claw + HORIZONTAL)
		"Stockade 13 To Stockade 07"                           : lambda s : s.can_reach(el['Oubliette13Left'], 'Region', p) or s.can_reach(el['Oubliette13Right'], 'Region', p) and (s.has(el['hook'], p) or macros['LEDGE'](s) and s.has(el['claw'], p) and macros['HORIZONTAL'](s)),
#		                                                        Oubliette14Left | Oubliette14Right
		"Stockade 14 - Hoenir's Diary 2"                       : lambda s : s.can_reach(el['Oubliette14Left'], 'Region', p) or s.can_reach(el['Oubliette14Right'], 'Region', p),
#		                                                        Oubliette14Left | ExecutionGrounds
		"Stockade 14 To Stockade 11"                           : lambda s : s.can_reach(el['Oubliette14Left'], 'Region', p) or s.can_reach(el['ExecutionGrounds'], 'Location', p),
#		                                                        Oubliette14Right | ExecutionGrounds
		"Stockade 14 To Stockade 15"                           : lambda s : s.can_reach(el['Oubliette14Right'], 'Region', p) or s.can_reach(el['ExecutionGrounds'], 'Location', p),
#		                                                        Oubliette15Left | Oubliette15Right
		"Stockade 15 - Hoenir, Keeper of the Abyss"            : lambda s : s.can_reach(el['Oubliette15Left'], 'Region', p) or s.can_reach(el['Oubliette15Right'], 'Region', p),
#		                                                        Oubliette15Left | Oubliette15Right
		"Stockade 15 To Stockade 14"                           : lambda s : s.can_reach(el['Oubliette15Left'], 'Region', p) or s.can_reach(el['Oubliette15Right'], 'Region', p),
#		                                                        Oubliette15Right | Oubliette15Left
		"Stockade 15 To Stockade 16"                           : lambda s : s.can_reach(el['Oubliette15Right'], 'Region', p) or s.can_reach(el['Oubliette15Left'], 'Region', p),
#		                                                        Oubliette16Right
		"Stockade 16 - Priestess' Wish"                        : lambda s : s.can_reach(el['Oubliette16Right'], 'Region', p),
#		                                                        Oubliette16Left
		"Stockade 16 - Stagnant Blight x10"                    : lambda s : s.can_reach(el['Oubliette16Left'], 'Region', p),
#		                                                        Oubliette16Left | Oubliette16Right
		"Stockade 16 To Stockade 15"                           : lambda s : s.can_reach(el['Oubliette16Left'], 'Region', p) or s.can_reach(el['Oubliette16Right'], 'Region', p),
#		                                                        Oubliette16Right | Oubliette16Left + (hook + (sinner + (LEDGE | dash | dodge) | silva + (djump | dodge | champion + dash) | djump + (dodge | champion)) | silva + djump + (claw | champion | dodge))
		"Stockade 16 To Hinterlands 01"                        : lambda s : s.can_reach(el['Oubliette16Right'], 'Region', p) or s.can_reach(el['Oubliette16Left'], 'Region', p) and (s.has(el['hook'], p) and (s.has(el['sinner'], p) and (macros['LEDGE'](s) or s.has(el['dash'], p) or s.has(el['dodge'], p)) or s.has(el['silva'], p) and (s.has(el['djump'], p) or s.has(el['dodge'], p) or s.has(el['champion'], p) and s.has(el['dash'], p)) or s.has(el['djump'], p) and (s.has(el['dodge'], p) or s.has(el['champion'], p))) or s.has(el['silva'], p) and s.has(el['djump'], p) and (s.has(el['claw'], p) or s.has(el['champion'], p) or s.has(el['dodge'], p))),
#		                                                        Oubliette17Right
		"Stockade 17 To Stockade 10"                           : lambda s : s.can_reach(el['Oubliette17Right'], 'Region', p),
#		                                                        Oubliette17Bottom | Oubliette17Right +  (CHARGE + slam + (dodge + claw | hook))
		"Stockade 17 To Verboten Domain 06"                    : lambda s : s.can_reach(el['Oubliette17Bottom'], 'Region', p) or s.can_reach(el['Oubliette17Right'], 'Region', p) and (macros['CHARGE'](s) and s.has(el['slam'], p) and (s.has(el['dodge'], p) and s.has(el['claw'], p) or s.has(el['hook'], p))),
#		                                                        Outside01Right | Outside01Left1 | Outside01Left2
		"Hinterlands 01 To Hinterlands 02"                     : lambda s : s.can_reach(el['Outside01Right'], 'Region', p) or s.can_reach(el['Outside01Left1'], 'Region', p) or s.can_reach(el['Outside01Left2'], 'Region', p),
#		                                                        Outside01Left1 | Outside01Right + claw + (djump | champion | 2LEDGE)
		"Hinterlands 01 To Hinterlands 03"                     : lambda s : s.can_reach(el['Outside01Left1'], 'Region', p) or s.can_reach(el['Outside01Right'], 'Region', p) and s.has(el['claw'], p) and (s.has(el['djump'], p) or s.has(el['champion'], p) or macros['2LEDGE'](s)),
#		                                                        Outside01Left2
		"Hinterlands 01 To Stockade 16"                        : lambda s : s.can_reach(el['Outside01Left2'], 'Region', p),
#		                                                        Outside02Left
		"Hinterlands 02 To Hinterlands 01"                     : lambda s : s.can_reach(el['Outside02Left'], 'Region', p),
#		                                                        Outside03Right + (claw + (2LEDGE | LEDGE + HORIZONTAL | champion))
		"Hinterlands 03 - King of the First Age's Torn Note 1" : lambda s : s.can_reach(el['Outside03Right'], 'Region', p) and (s.has(el['claw'], p) and (macros['2LEDGE'](s) or macros['LEDGE'](s) and macros['HORIZONTAL'](s) or s.has(el['champion'], p))),
#		                                                        Grotto
		"Hinterlands 03 - King of the First Age's Torn Note 2" : lambda s : s.can_reach(el['Grotto'], 'Location', p),
#		                                                        Outside03Right + swim
		"Hinterlands 03 - Nymphilia's Ring"                    : lambda s : s.can_reach(el['Outside03Right'], 'Region', p) and s.has(el['swim'], p),
#		                                                        Grotto
		"Hinterlands 03 - Stagnant Blight x100"                : lambda s : s.can_reach(el['Grotto'], 'Location', p),
#		                                                        Outside03Right | Outside03Top
		"Hinterlands 03 To Hinterlands 01"                     : lambda s : s.can_reach(el['Outside03Right'], 'Region', p) or s.can_reach(el['Outside03Top'], 'Region', p),
#		                                                        Outside03Top
		"Hinterlands 03 To Twin Spires 09"                     : lambda s : s.can_reach(el['Outside03Top'], 'Region', p),
#		                                                        Swamp04Bottom + unlock
		"Verboten Domain 04 - Verboten Champion"               : lambda s : s.can_reach(el['Swamp04Bottom'], 'Region', p) and s.has(el['unlock'], p),
#		                                                        Swamp04Left
		"Verboten Domain 04 - Chain of Sorcery"                : lambda s : s.can_reach(el['Swamp04Left'], 'Region', p),
#		                                                        Swamp04Bottom | Swamp04Left + LEDGE
		"Verboten Domain 04 To Verboten Domain 05"             : lambda s : s.can_reach(el['Swamp04Bottom'], 'Region', p) or s.can_reach(el['Swamp04Left'], 'Region', p) and macros['LEDGE'](s),
#		                                                        Swamp04Left | Swamp04Bottom + LEDGE
		"Verboten Domain 04 To Verboten Domain 3R"             : lambda s : s.can_reach(el['Swamp04Left'], 'Region', p) or s.can_reach(el['Swamp04Bottom'], 'Region', p) and macros['LEDGE'](s),
#		                                                        Swamp05Left + swim
		"Verboten Domain 05 - Furious Blight x100"             : lambda s : s.can_reach(el['Swamp05Left'], 'Region', p) and s.has(el['swim'], p),
#		                                                        Swamp05Top | Swamp05Right + (LEDGE | claw)
		"Verboten Domain 05 To Verboten Domain 04"             : lambda s : s.can_reach(el['Swamp05Top'], 'Region', p) or s.can_reach(el['Swamp05Right'], 'Region', p) and (macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                        Swamp05Right | Swamp05Top | Swamp05Left + (LEDGE | claw)
		"Verboten Domain 05 To Verboten Domain 06"             : lambda s : s.can_reach(el['Swamp05Right'], 'Region', p) or s.can_reach(el['Swamp05Top'], 'Region', p) or s.can_reach(el['Swamp05Left'], 'Region', p) and (macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                        Swamp05Bottom | Swamp05Left + swim + CHARGE
		"Verboten Domain 05 To Verboten Domain 07"             : lambda s : s.can_reach(el['Swamp05Bottom'], 'Region', p) or s.can_reach(el['Swamp05Left'], 'Region', p) and s.has(el['swim'], p) and macros['CHARGE'](s),
#		                                                        Swamp05Left | Swamp05Right
		"Verboten Domain 05 To Verboten Domain 09"             : lambda s : s.can_reach(el['Swamp05Left'], 'Region', p) or s.can_reach(el['Swamp05Right'], 'Region', p),
#		                                                        Swamp05Left + swim
		"Verboten Domain 05 - Stagnant Blight x30"             : lambda s : s.can_reach(el['Swamp05Left'], 'Region', p) and s.has(el['swim'], p),
#		                                                        Swamp06Left | Swamp06Top
		"Verboten Domain 06 - Verboten Domain Notice"          : lambda s : s.can_reach(el['Swamp06Left'], 'Region', p) or s.can_reach(el['Swamp06Top'], 'Region', p),
#		                                                        Swamp06Top
		"Verboten Domain 06 - Heretic's Mask"                  : lambda s : s.can_reach(el['Swamp06Top'], 'Region', p),
#		                                                        Swamp06Top
		"Verboten Domain 06 - Stagnant Blight x30"             : lambda s : s.can_reach(el['Swamp06Top'], 'Region', p),
#		                                                        Swamp06Left | Lab2
		"Verboten Domain 06 To Verboten Domain 05"             : lambda s : s.can_reach(el['Swamp06Left'], 'Region', p) or s.can_reach(el['Lab2'], 'Location', p),
#		                                                        Swamp06Top
		"Verboten Domain 06 To Stockade 17"                    : lambda s : s.can_reach(el['Swamp06Top'], 'Region', p),
#		                                                        Swamp07Right + claw
		"Verboten Domain 07 - Amulet Fragment"                 : lambda s : s.can_reach(el['Swamp07Right'], 'Region', p) and s.has(el['claw'], p),
#		                                                        Swamp07Left + (claw + LEDGE)
		"Verboten Domain 07 - Calivia's Ring"                  : lambda s : s.can_reach(el['Swamp07Left'], 'Region', p) and (s.has(el['claw'], p) and macros['LEDGE'](s)),
#		                                                        Swamp07Bottom | Swamp07Right + Swamp07Left + Swamp07Top
		"Verboten Domain 07 To Verboten Domain 16"             : lambda s : s.can_reach(el['Swamp07Bottom'], 'Region', p) or s.can_reach(el['Swamp07Right'], 'Region', p) and s.can_reach(el['Swamp07Left'], 'Region', p) and s.can_reach(el['Swamp07Top'], 'Region', p),
#		                                                        Swamp07Right
		"Verboten Domain 07 To Verboten Domain 05"             : lambda s : s.can_reach(el['Swamp07Right'], 'Region', p),
#		                                                        Swamp07Left
		"Verboten Domain 07 To Verboten Domain 08"             : lambda s : s.can_reach(el['Swamp07Left'], 'Region', p),
#		                                                        Swamp07Top
		"Verboten Domain 07 To Verboten Domain 3B"             : lambda s : s.can_reach(el['Swamp07Top'], 'Region', p),
#		                                                        Swamp08Right2 + swim
		"Verboten Domain 08 - Amulet Gem"                      : lambda s : s.can_reach(el['Swamp08Right2'], 'Region', p) and s.has(el['swim'], p),
#		                                                        Swamp08Right2 + swim
		"Verboten Domain 08 - Stagnant Blight x100"            : lambda s : s.can_reach(el['Swamp08Right2'], 'Region', p) and s.has(el['swim'], p),
#		                                                        Swamp08Right2 + swim
		"Verboten Domain 08 - Furious Blight x100"             : lambda s : s.can_reach(el['Swamp08Right2'], 'Region', p) and s.has(el['swim'], p),
#		                                                        Swamp08Right1 | Swamp08Right2 + (hook | (claw + (djump | champion | silva + dodge))) + (djump | HORIZONTAL)
		"Verboten Domain 08 To Verboten Domain 07"             : lambda s : s.can_reach(el['Swamp08Right1'], 'Region', p) or s.can_reach(el['Swamp08Right2'], 'Region', p) and (s.has(el['hook'], p) or (s.has(el['claw'], p) and (s.has(el['djump'], p) or s.has(el['champion'], p) or s.has(el['silva'], p) and s.has(el['dodge'], p)))) and (s.has(el['djump'], p) or macros['HORIZONTAL'](s)),
#		                                                        Swamp08Right2 | Swamp08Top | Swamp08Right1
		"Verboten Domain 08 To Verboten Domain 15"             : lambda s : s.can_reach(el['Swamp08Right2'], 'Region', p) or s.can_reach(el['Swamp08Top'], 'Region', p) or s.can_reach(el['Swamp08Right1'], 'Region', p),
#		                                                        Swamp08Top | Swamp08Right2 + LEDGE
		"Verboten Domain 08 To Verboten Domain 14"             : lambda s : s.can_reach(el['Swamp08Top'], 'Region', p) or s.can_reach(el['Swamp08Right2'], 'Region', p) and macros['LEDGE'](s),
#		                                                        Swamp09Right2 + (LEDGE | HORIZONTAL)
		"Verboten Domain 09 - Weathered Necklace"              : lambda s : s.can_reach(el['Swamp09Right2'], 'Region', p) and (macros['LEDGE'](s) or macros['HORIZONTAL'](s)),
#		                                                        Swamp09Right1 + (LEDGE + HORIZONTAL | 2LEDGE)
		"Verboten Domain 09 - Stagnant Blight x30"             : lambda s : s.can_reach(el['Swamp09Right1'], 'Region', p) and (macros['LEDGE'](s) and macros['HORIZONTAL'](s) or macros['2LEDGE'](s)),
#		                                                        Swamp09Bottom1 | Swamp09Right1 + CHARGE
		"Verboten Domain 09 To Verboten Domain 13 Left"        : lambda s : s.can_reach(el['Swamp09Bottom1'], 'Region', p) or s.can_reach(el['Swamp09Right1'], 'Region', p) and macros['CHARGE'](s),
#		                                                        Swamp09Right1 | Swamp09Right2 + (LEDGE | HORIZONTAL)
		"Verboten Domain 09 To Verboten Domain 03"             : lambda s : s.can_reach(el['Swamp09Right1'], 'Region', p) or s.can_reach(el['Swamp09Right2'], 'Region', p) and (macros['LEDGE'](s) or macros['HORIZONTAL'](s)),
#		                                                        Swamp09Bottom2 | Swamp09Right2
		"Verboten Domain 09 To Verboten Domain 13 Right"       : lambda s : s.can_reach(el['Swamp09Bottom2'], 'Region', p) or s.can_reach(el['Swamp09Right2'], 'Region', p),
#		                                                        Swamp09Right2 | Swamp09Right1
		"Verboten Domain 09 To Verboten Domain 05"             : lambda s : s.can_reach(el['Swamp09Right2'], 'Region', p) or s.can_reach(el['Swamp09Right1'], 'Region', p),
#		                                                        Swamp1Bottom | Swamp1Left
		"Verboten Domain 01 - Faden's Archives 3"              : lambda s : s.can_reach(el['Swamp1Bottom'], 'Region', p) or s.can_reach(el['Swamp1Left'], 'Region', p),
#		                                                        Swamp1Bottom | Lab1
		"Verboten Domain 01 To Verboten Domain 03"             : lambda s : s.can_reach(el['Swamp1Bottom'], 'Region', p) or s.can_reach(el['Lab1'], 'Location', p),
#		                                                        Swamp1Left | Lab1
		"Verboten Domain 01 To Verboten Domain 02"             : lambda s : s.can_reach(el['Swamp1Left'], 'Region', p) or s.can_reach(el['Lab1'], 'Location', p),
#		                                                        Swamp10Right
		"Verboten Domain 10 - Faden's Archives 4"              : lambda s : s.can_reach(el['Swamp10Right'], 'Region', p),
#		                                                        Lab3 + swim
		"Verboten Domain 10 - Stagnant Blight x30"             : lambda s : s.can_reach(el['Lab3'], 'Location', p) and s.has(el['swim'], p),
#		                                                        Swamp10Right | Lab3
		"Verboten Domain 10 To Verboten Domain 13"             : lambda s : s.can_reach(el['Swamp10Right'], 'Region', p) or s.can_reach(el['Lab3'], 'Location', p),
#		                                                        Swamp11Left + (LEDGE + HORIZONTAL | 2HORIZONTAL | silva + djump)
		"Verboten Domain 11 - Amulet Fragment"                 : lambda s : s.can_reach(el['Swamp11Left'], 'Region', p) and (macros['LEDGE'](s) and macros['HORIZONTAL'](s) or macros['2HORIZONTAL'](s) or s.has(el['silva'], p) and s.has(el['djump'], p)),
#		                                                        Swamp11Left
		"Verboten Domain 11 - Blighted Appendage"              : lambda s : s.can_reach(el['Swamp11Left'], 'Region', p),
#		                                                        Swamp11Bottom | Swamp11Left
		"Verboten Domain 11 To Verboten Domain 15"             : lambda s : s.can_reach(el['Swamp11Bottom'], 'Region', p) or s.can_reach(el['Swamp11Left'], 'Region', p),
#		                                                        Swamp11Left | Swamp11Bottom + (hook | claw | 2LEDGE) + (djump | champion | (silva + dodge))
		"Verboten Domain 11 To Verboten Domain 14"             : lambda s : s.can_reach(el['Swamp11Left'], 'Region', p) or s.can_reach(el['Swamp11Bottom'], 'Region', p) and (s.has(el['hook'], p) or s.has(el['claw'], p) or macros['2LEDGE'](s)) and (s.has(el['djump'], p) or s.has(el['champion'], p) or (s.has(el['silva'], p) and s.has(el['dodge'], p))),
#		                                                        Lab4 + slam
		"Verboten Domain 12 - Priestess' Wish"                 : lambda s : s.can_reach(el['Lab4'], 'Location', p) and s.has(el['slam'], p),
#		                                                        Swamp12Left | Swamp12Bottom | Swamp12TP
		"Verboten Domain 12 - Faden's Archives 2"              : lambda s : s.can_reach(el['Swamp12Left'], 'Region', p) or s.can_reach(el['Swamp12Bottom'], 'Region', p) or s.can_reach(el['Swamp12TP'], 'Region', p),
#		                                                        Swamp12Left | Lab4
		"Verboten Domain 12 To Verboten Domain 15"             : lambda s : s.can_reach(el['Swamp12Left'], 'Region', p) or s.can_reach(el['Lab4'], 'Location', p),
#		                                                        Swamp12Bottom | Lab4 + slam + unlock
		"Verboten Domain 12 To The Abyss 04"                   : lambda s : s.can_reach(el['Swamp12Bottom'], 'Region', p) or s.can_reach(el['Lab4'], 'Location', p) and s.has(el['slam'], p) and s.has(el['unlock'], p),
#		                                                        Swamp13Top2
		"Verboten Domain 13 - Amulet Fragment"                 : lambda s : s.can_reach(el['Swamp13Top2'], 'Region', p),
#		                                                        Swamp13Top1 + slam | Swamp13Top2 + CHARGE + slam
		"Verboten Domain 13 - Stagnant Blight x30"             : lambda s : s.can_reach(el['Swamp13Top1'], 'Region', p) and s.has(el['slam'], p) or s.can_reach(el['Swamp13Top2'], 'Region', p) and macros['CHARGE'](s) and s.has(el['slam'], p),
#		                                                        Swamp13Bottom + (hook | claw)
		"Verboten Domain 13 - Furious Blight x30"              : lambda s : s.can_reach(el['Swamp13Bottom'], 'Region', p) and (s.has(el['hook'], p) or s.has(el['claw'], p)),
#		                                                        Swamp13Left | Swamp13Top1 + slam | Swamp13Top2 + CHARGE + slam
		"Verboten Domain 13 To Verboten Domain 10"             : lambda s : s.can_reach(el['Swamp13Left'], 'Region', p) or s.can_reach(el['Swamp13Top1'], 'Region', p) and s.has(el['slam'], p) or s.can_reach(el['Swamp13Top2'], 'Region', p) and macros['CHARGE'](s) and s.has(el['slam'], p),
#		                                                        Swamp13Top1 | Swamp13Bottom + claw + 3LEDGE
		"Verboten Domain 13 To Verboten Domain 09 Left"        : lambda s : s.can_reach(el['Swamp13Top1'], 'Region', p) or s.can_reach(el['Swamp13Bottom'], 'Region', p) and s.has(el['claw'], p) and macros['3LEDGE'](s),
#		                                                        Swamp13Top2
		"Verboten Domain 13 To Verboten Domain 09 Right"       : lambda s : s.can_reach(el['Swamp13Top2'], 'Region', p),
#		                                                        Swamp13Bottom | slam + (Swamp13Top1 | Swamp13Left)
		"Verboten Domain 13 To Verboten Domain 14"             : lambda s : s.can_reach(el['Swamp13Bottom'], 'Region', p) or s.has(el['slam'], p) and (s.can_reach(el['Swamp13Top1'], 'Region', p) or s.can_reach(el['Swamp13Left'], 'Region', p)),
#		                                                        Swamp14Top | Swamp14Bottom + (LEDGE | claw | hook)
		"Verboten Domain 14 - Chain of Sorcery"                : lambda s : s.can_reach(el['Swamp14Top'], 'Region', p) or s.can_reach(el['Swamp14Bottom'], 'Region', p) and (macros['LEDGE'](s) or s.has(el['claw'], p) or s.has(el['hook'], p)),
#		                                                        Swamp14Top + (2LEDGE | hook)
		"Verboten Domain 14 - Stagnant Blight x100"            : lambda s : s.can_reach(el['Swamp14Top'], 'Region', p) and (macros['2LEDGE'](s) or s.has(el['hook'], p)),
#		                                                        Swamp14Top | Swamp14Bottom + claw + 3LEDGE
		"Verboten Domain 14 To Verboten Domain 13"             : lambda s : s.can_reach(el['Swamp14Top'], 'Region', p) or s.can_reach(el['Swamp14Bottom'], 'Region', p) and s.has(el['claw'], p) and macros['3LEDGE'](s),
#		                                                        Swamp14Right | Swamp14Top | Swamp14Bottom + (LEDGE | claw | hook)
		"Verboten Domain 14 To Verboten Domain 11"             : lambda s : s.can_reach(el['Swamp14Right'], 'Region', p) or s.can_reach(el['Swamp14Top'], 'Region', p) or s.can_reach(el['Swamp14Bottom'], 'Region', p) and (macros['LEDGE'](s) or s.has(el['claw'], p) or s.has(el['hook'], p)),
#		                                                        Swamp14Bottom | Swamp14Right
		"Verboten Domain 14 To Verboten Domain 08"             : lambda s : s.can_reach(el['Swamp14Bottom'], 'Region', p) or s.can_reach(el['Swamp14Right'], 'Region', p),
#		                                                        Swamp15Left + swim + mask
		"Verboten Domain 15 - Incompetent Sinner"              : lambda s : s.can_reach(el['Swamp15Left'], 'Region', p) and s.has(el['swim'], p) and s.has(el['mask'], p),
#		                                                        Swamp15Top
		"Verboten Domain 15 - Stagnant Blight x30"             : lambda s : s.can_reach(el['Swamp15Top'], 'Region', p),
#		                                                        Swamp15Top | Swamp15Right + (champion | djump | silva + dodge)
		"Verboten Domain 15 To Verboten Domain 11"             : lambda s : s.can_reach(el['Swamp15Top'], 'Region', p) or s.can_reach(el['Swamp15Right'], 'Region', p) and (s.has(el['champion'], p) or s.has(el['djump'], p) or s.has(el['silva'], p) and s.has(el['dodge'], p)),
#		                                                        Swamp15Left | Swamp15Right + LEDGE
		"Verboten Domain 15 To Verboten Domain 08"             : lambda s : s.can_reach(el['Swamp15Left'], 'Region', p) or s.can_reach(el['Swamp15Right'], 'Region', p) and macros['LEDGE'](s),
#		                                                        Swamp15Right | Swamp15Left + (claw | hook) | Swamp15Top
		"Verboten Domain 15 To Verboten Domain 12"             : lambda s : s.can_reach(el['Swamp15Right'], 'Region', p) or s.can_reach(el['Swamp15Left'], 'Region', p) and (s.has(el['claw'], p) or s.has(el['hook'], p)) or s.can_reach(el['Swamp15Top'], 'Region', p),
#		                                                        Swamp16Top | Swamp16Left
		"Verboten Domain 16 - Faden's Archives 1"              : lambda s : s.can_reach(el['Swamp16Top'], 'Region', p) or s.can_reach(el['Swamp16Left'], 'Region', p),
#		                                                        Swamp16Top | Lab5
		"Verboten Domain 16 To Verboten Domain 07"             : lambda s : s.can_reach(el['Swamp16Top'], 'Region', p) or s.can_reach(el['Lab5'], 'Location', p),
#		                                                        Swamp16Left | Lab5
		"Verboten Domain 16 To Verboten Domain 17"             : lambda s : s.can_reach(el['Swamp16Left'], 'Region', p) or s.can_reach(el['Lab5'], 'Location', p),
#		                                                        Swamp17Left | Swamp17Right
		"Verboten Domain 17 To Verboten Domain 18"             : lambda s : s.can_reach(el['Swamp17Left'], 'Region', p) or s.can_reach(el['Swamp17Right'], 'Region', p),
#		                                                        Swamp17Right | Swamp17Left
		"Verboten Domain 17 To Verboten Domain 16"             : lambda s : s.can_reach(el['Swamp17Right'], 'Region', p) or s.can_reach(el['Swamp17Left'], 'Region', p),
#		                                                        Faden
		"Verboten Domain 18 - Miriel's Blighted Letter"        : lambda s : s.can_reach(el['Faden'], 'Location', p),
#		                                                        Faden
		"Verboten Domain 18 - Faden's Archives 5"              : lambda s : s.can_reach(el['Faden'], 'Location', p),
#		                                                        Swamp18Right
		"Verboten Domain 18 - Faden, the Heretic"              : lambda s : s.can_reach(el['Swamp18Right'], 'Region', p),
#		                                                        Faden + claw + (3LEDGE | sinner + 2LEDGE | FULLSILVA | dodge + silva + champion | 2HORIZONTAL + champion + djump)
		"Verboten Domain 18 - Stagnant Blight x800"            : lambda s : s.can_reach(el['Faden'], 'Location', p) and s.has(el['claw'], p) and (macros['3LEDGE'](s) or s.has(el['sinner'], p) and macros['2LEDGE'](s) or macros['FULLSILVA'](s) or s.has(el['dodge'], p) and s.has(el['silva'], p) and s.has(el['champion'], p) or macros['2HORIZONTAL'](s) and s.has(el['champion'], p) and s.has(el['djump'], p)),
#		                                                        Swamp18Bottom | Faden + unlock
		"Verboten Domain 18 To The Abyss 01"                   : lambda s : s.can_reach(el['Swamp18Bottom'], 'Region', p) or s.can_reach(el['Faden'], 'Location', p) and s.has(el['unlock'], p),
#		                                                        Swamp18Right | Faden
		"Verboten Domain 18 To Verboten Domain 17"             : lambda s : s.can_reach(el['Swamp18Right'], 'Region', p) or s.can_reach(el['Faden'], 'Location', p),
#		                                                        Swamp2Top
		"Verboten Domain 02 - Furious Blight x10"              : lambda s : s.can_reach(el['Swamp2Top'], 'Region', p),
#		                                                        Swamp2Top + (claw | LEDGE + hook)
		"Verboten Domain 02 - Furious Blight x30"              : lambda s : s.can_reach(el['Swamp2Top'], 'Region', p) and (s.has(el['claw'], p) or macros['LEDGE'](s) and s.has(el['hook'], p)),
#		                                                        Swamp2Right | Swamp2Top + (dash | dodge)
		"Verboten Domain 02 To Verboten Domain 01"             : lambda s : s.can_reach(el['Swamp2Right'], 'Region', p) or s.can_reach(el['Swamp2Top'], 'Region', p) and (s.has(el['dash'], p) or s.has(el['dodge'], p)),
#		                                                        Swamp2Top | Swamp2Right
		"Verboten Domain 02 To Witch's Thicket 09"             : lambda s : s.can_reach(el['Swamp2Top'], 'Region', p) or s.can_reach(el['Swamp2Right'], 'Region', p),
#		                                                        Swamp3Top + LEDGE
		"Verboten Domain 03 - Amulet Fragment"                 : lambda s : s.can_reach(el['Swamp3Top'], 'Region', p) and macros['LEDGE'](s),
#		                                                        Swamp3Top
		"Verboten Domain 03 - Stagnant Blight x30"             : lambda s : s.can_reach(el['Swamp3Top'], 'Region', p),
#		                                                        Swamp3Left | Swamp3Bottom
		"Verboten Domain 03 To Verboten Domain 09"             : lambda s : s.can_reach(el['Swamp3Left'], 'Region', p) or s.can_reach(el['Swamp3Bottom'], 'Region', p),
#		                                                        Swamp3Top | Swamp3Left + LEDGE
		"Verboten Domain 03 To Verboten Domain 01"             : lambda s : s.can_reach(el['Swamp3Top'], 'Region', p) or s.can_reach(el['Swamp3Left'], 'Region', p) and macros['LEDGE'](s),
#		                                                        Swamp3Right | Swamp3Bottom | Swamp3Top
		"Verboten Domain 03 To Verboten Domain 04"             : lambda s : s.can_reach(el['Swamp3Right'], 'Region', p) or s.can_reach(el['Swamp3Bottom'], 'Region', p) or s.can_reach(el['Swamp3Top'], 'Region', p),
#		                                                        Swamp3Bottom | Swamp3Top | Swamp3Right
		"Verboten Domain 03 To Verboten Domain 07"             : lambda s : s.can_reach(el['Swamp3Bottom'], 'Region', p) or s.can_reach(el['Swamp3Top'], 'Region', p) or s.can_reach(el['Swamp3Right'], 'Region', p),
#		                                                        Village01Right | Village01Bottom
		"Cliffside Hamlet 01 To Cliffside Hamlet 02"           : lambda s : s.can_reach(el['Village01Right'], 'Region', p) or s.can_reach(el['Village01Bottom'], 'Region', p),
#		                                                        Village01Bottom | Village01Right
		"Cliffside Hamlet 01 To White Parish 08"               : lambda s : s.can_reach(el['Village01Bottom'], 'Region', p) or s.can_reach(el['Village01Right'], 'Region', p),
#		                                                        Village02Left
		"Cliffside Hamlet 02 - Amulet Fragment"                : lambda s : s.can_reach(el['Village02Left'], 'Region', p),
#		                                                        Village02Left + (djump + (silva | champion) | (djump | silva) + HORIZONTAL | hook)
		"Cliffside Hamlet 02 - Left Stagnant Blight x10"       : lambda s : s.can_reach(el['Village02Left'], 'Region', p) and (s.has(el['djump'], p) and (s.has(el['silva'], p) or s.has(el['champion'], p)) or (s.has(el['djump'], p) or s.has(el['silva'], p)) and macros['HORIZONTAL'](s) or s.has(el['hook'], p)),
#		                                                        (Village02Right | Village02Bottom | Village02Left + (LEDGE | claw)) + (2LEDGE | silva + dodge | hook)
		"Cliffside Hamlet 02 - Right Stagnant Blight x10"	   : lambda s: (s.can_reach(el['Village02Right'], 'Region', p) or s.can_reach(el['Village02Bottom'], 'Region', p) or (s.can_reach(el['Village02Left'], 'Region', p) and (macros['LEDGE'](s) or s.has(el['claw'], p)))) and (macros['2LEDGE'](s) or (s.has(el['silva'], p) and s.has(el['dodge'], p)) or s.has(el['hook'], p)),
#		                                                        Village02Right | Village02Bottom | Village02Left + (LEDGE | claw)
		"Cliffside Hamlet 02 To Cliffside Hamlet 03"           : lambda s : s.can_reach(el['Village02Right'], 'Region', p) or s.can_reach(el['Village02Bottom'], 'Region', p) or s.can_reach(el['Village02Left'], 'Region', p) and (macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                        Village02Left | Village02Bottom
		"Cliffside Hamlet 02 To Cliffside Hamlet 01"           : lambda s : s.can_reach(el['Village02Left'], 'Region', p) or s.can_reach(el['Village02Bottom'], 'Region', p),
#		                                                        Village02Bottom | Village02Right
		"Cliffside Hamlet 02 To Cliffside Hamlet 13"           : lambda s : s.can_reach(el['Village02Bottom'], 'Region', p) or s.can_reach(el['Village02Right'], 'Region', p),
#		                                                        slam + (Village03Right + (LEDGE | HORIZONTAL) | Village03Bottom1 + (LEDGE | claw))
		"Cliffside Hamlet 03 - Amulet Fragment"                : lambda s : s.has(el['slam'], p) and (s.can_reach(el['Village03Right'], 'Region', p) and (macros['LEDGE'](s) or macros['HORIZONTAL'](s)) or s.can_reach(el['Village03Bottom1'], 'Region', p) and (macros['LEDGE'](s) or s.has(el['claw'], p))),
#		                                                        Village03Right + (claw | hook | LEDGE | HORIZONTAL | dash)
		"Cliffside Hamlet 03 - Broken Music Box"               : lambda s : s.can_reach(el['Village03Right'], 'Region', p) and (s.has(el['claw'], p) or s.has(el['hook'], p) or macros['LEDGE'](s) or macros['HORIZONTAL'](s) or s.has(el['dash'], p)),
#		                                                        Village03Right + (LEDGE | HORIZONTAL | hook | dash) | Village03Bottom1 + (LEDGE | claw)
		"Cliffside Hamlet 03 - Stagnant Blight x10"            : lambda s : s.can_reach(el['Village03Right'], 'Region', p) and (macros['LEDGE'](s) or macros['HORIZONTAL'](s) or s.has(el['hook'], p) or s.has(el['dash'], p)) or s.can_reach(el['Village03Bottom1'], 'Region', p) and (macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                        slam + (Village03Right + (LEDGE | HORIZONTAL | hook | dash) | Village03Bottom1 + (LEDGE | claw))
		"Cliffside Hamlet 03 - Furious Blight x10"             : lambda s : s.has(el['slam'], p) and (s.can_reach(el['Village03Right'], 'Region', p) and (macros['LEDGE'](s) or macros['HORIZONTAL'](s) or s.has(el['hook'], p) or s.has(el['dash'], p)) or s.can_reach(el['Village03Bottom1'], 'Region', p) and (macros['LEDGE'](s) or s.has(el['claw'], p))),
#		                                                        Village03Bottom1 | Village03Right + (HORIZONTAL | LEDGE | hook | dash)
		"Cliffside Hamlet 03 To Cliffside Hamlet 02"           : lambda s : s.can_reach(el['Village03Bottom1'], 'Region', p) or s.can_reach(el['Village03Right'], 'Region', p) and (macros['HORIZONTAL'](s) or macros['LEDGE'](s) or s.has(el['hook'], p) or s.has(el['dash'], p)),
#		                                                        Village03Right | Village03Bottom1 + (LEDGE | claw)
		"Cliffside Hamlet 03 To Cliffside Hamlet 05"           : lambda s : s.can_reach(el['Village03Right'], 'Region', p) or s.can_reach(el['Village03Bottom1'], 'Region', p) and (macros['LEDGE'](s) or s.has(el['claw'], p)),
#		                                                        Village03Bottom2 | Village03Right + slam
		"Cliffside Hamlet 03 To Cliffside Hamlet 13"           : lambda s : s.can_reach(el['Village03Bottom2'], 'Region', p) or s.can_reach(el['Village03Right'], 'Region', p) and s.has(el['slam'], p),
#		                                                        Village041Bottom
		"Cliffside Hamlet 04_1 - Western Merchant"             : lambda s : s.can_reach(el['Village041Bottom'], 'Region', p),
#		                                                        Village041Bottom
		"Cliffside Hamlet 04_1 To Cliffside Hamlet 04"         : lambda s : s.can_reach(el['Village041Bottom'], 'Region', p),
#		                                                        Village04Top
		"Cliffside Hamlet 04 - Amulet Fragment"                : lambda s : s.can_reach(el['Village04Top'], 'Region', p),
#		                                                        Village04Right + (hook + (LEDGE | claw) | LEDGE + HORIZONTAL | 2LEDGE | LEDGE + claw)
		"Cliffside Hamlet 04 - Bloodstained Ribbon"            : lambda s : s.can_reach(el['Village04Right'], 'Region', p) and (s.has(el['hook'], p) and (macros['LEDGE'](s) or s.has(el['claw'], p)) or macros['LEDGE'](s) and macros['HORIZONTAL'](s) or macros['2LEDGE'](s) or macros['LEDGE'](s) and s.has(el['claw'], p)),
#		                                                        Village04Top | Village04Right
		"Cliffside Hamlet 04 To Cliffside Hamlet 04"           : lambda s : s.can_reach(el['Village04Top'], 'Region', p) or s.can_reach(el['Village04Right'], 'Region', p),
#		                                                        Village04Top
		"Cliffside Hamlet 04 - Stagnant Blight x10"            : lambda s : s.can_reach(el['Village04Top'], 'Region', p),
#		                                                        Village04Right | Village04Top
		"Cliffside Hamlet 04 To Cliffside Hamlet 05"           : lambda s : s.can_reach(el['Village04Right'], 'Region', p) or s.can_reach(el['Village04Top'], 'Region', p),
#		                                                        Village05Top | Village05Left | Village05Right
		"Cliffside Hamlet 05 - True Believer's Note"           : lambda s : s.can_reach(el['Village05Top'], 'Region', p) or s.can_reach(el['Village05Left'], 'Region', p) or s.can_reach(el['Village05Right'], 'Region', p),
#		                                                        Village05Top | CollapsedShack
		"Cliffside Hamlet 05 To Cliffside Hamlet 04"           : lambda s : s.can_reach(el['Village05Top'], 'Region', p) or s.can_reach(el['CollapsedShack'], 'Location', p),
#		                                                        Village05Left | CollapsedShack
		"Cliffside Hamlet 05 To Cliffside Hamlet 03"           : lambda s : s.can_reach(el['Village05Left'], 'Region', p) or s.can_reach(el['CollapsedShack'], 'Location', p),
#		                                                        Village05Right | CollapsedShack
		"Cliffside Hamlet 05 To Cliffside Hamlet 06"           : lambda s : s.can_reach(el['Village05Right'], 'Region', p) or s.can_reach(el['CollapsedShack'], 'Location', p),
#		                                                        Village06Left
		"Cliffside Hamlet 06 - Amulet Fragment"                : lambda s : s.can_reach(el['Village06Left'], 'Region', p),
#		                                                        Village06Right2 + (2LEDGE | LEDGE + claw | (silva | djump) + HORIZONTAL | champion + sinner)
		"Cliffside Hamlet 06 - Upper Stagnant Blight x10"      : lambda s : s.can_reach(el['Village06Right2'], 'Region', p) and (macros['2LEDGE'](s) or macros['LEDGE'](s) and s.has(el['claw'], p) or (s.has(el['silva'], p) or s.has(el['djump'], p)) and macros['HORIZONTAL'](s) or s.has(el['champion'], p) and s.has(el['sinner'], p)),
#		                                                        Village06Left + slam + (2LEDGE | LEDGE + claw | hook)
		"Cliffside Hamlet 06 - Left Stagnant Blight x10"       : lambda s : s.can_reach(el['Village06Left'], 'Region', p) and s.has(el['slam'], p) and (macros['2LEDGE'](s) or macros['LEDGE'](s) and s.has(el['claw'], p) or s.has(el['hook'], p)),
#		                                                        Village06Left + slam + (2LEDGE | LEDGE + claw | hook)
		"Cliffside Hamlet 06 - Right Stagnant Blight x10"      : lambda s : s.can_reach(el['Village06Left'], 'Region', p) and s.has(el['slam'], p) and (macros['2LEDGE'](s) or macros['LEDGE'](s) and s.has(el['claw'], p) or s.has(el['hook'], p)),
#		                                                        Village06Left + (LEDGE | hook)
		"Cliffside Hamlet 06 - Upper Furious Blight x10"       : lambda s : s.can_reach(el['Village06Left'], 'Region', p) and (macros['LEDGE'](s) or s.has(el['hook'], p)),
#		                                                        Village06Left + slam + (LEDGE | hook)
		"Cliffside Hamlet 06 - Lower Furious Blight x10"       : lambda s : s.can_reach(el['Village06Left'], 'Region', p) and s.has(el['slam'], p) and (macros['LEDGE'](s) or s.has(el['hook'], p)),
#		                                                        Village06Left | Village06Right2 + LEDGE + claw
		"Cliffside Hamlet 06 To Cliffside Hamlet 05"           : lambda s : s.can_reach(el['Village06Left'], 'Region', p) or s.can_reach(el['Village06Right2'], 'Region', p) and macros['LEDGE'](s) and s.has(el['claw'], p),
#		                                                        Village06Right1 | Village06Right2 + (LEDGE | HORIZONTAL)
		"Cliffside Hamlet 06 To Cliffside Hamlet 07"           : lambda s : s.can_reach(el['Village06Right1'], 'Region', p) or s.can_reach(el['Village06Right2'], 'Region', p) and (macros['LEDGE'](s) or macros['HORIZONTAL'](s)),
#		                                                        Village06Bottom | Village06Left + slam
		"Cliffside Hamlet 06 To Cliffside Hamlet 12"           : lambda s : s.can_reach(el['Village06Bottom'], 'Region', p) or s.can_reach(el['Village06Left'], 'Region', p) and s.has(el['slam'], p),
#		                                                        Village06Right2 | Village06Left + (hook | LEDGE) | Village06Right1
		"Cliffside Hamlet 06 To Cliffside Hamlet 08"           : lambda s : s.can_reach(el['Village06Right2'], 'Region', p) or s.can_reach(el['Village06Left'], 'Region', p) and (s.has(el['hook'], p) or macros['LEDGE'](s)) or s.can_reach(el['Village06Right1'], 'Region', p),
#		                                                        Village07Left
		"Cliffside Hamlet 07 - Chain of Sorcery"               : lambda s : s.can_reach(el['Village07Left'], 'Region', p),
#		                                                        Village07Left
		"Cliffside Hamlet 07 - Stagnant Blight x10"            : lambda s : s.can_reach(el['Village07Left'], 'Region', p),
#		                                                        Village07Left + (hook | 2LEDGE)
		"Cliffside Hamlet 07 - Furious Blight x10"             : lambda s : s.can_reach(el['Village07Left'], 'Region', p) and (s.has(el['hook'], p) or macros['2LEDGE'](s)),
#		                                                        Village07Left | Village07Right
		"Cliffside Hamlet 07 To Cliffside Hamlet 06"           : lambda s : s.can_reach(el['Village07Left'], 'Region', p) or s.can_reach(el['Village07Right'], 'Region', p),
#		                                                        Village07Right | Village07Left | Village07Top
		"Cliffside Hamlet 07 To Cliffside Hamlet 09"           : lambda s : s.can_reach(el['Village07Right'], 'Region', p) or s.can_reach(el['Village07Left'], 'Region', p) or s.can_reach(el['Village07Top'], 'Region', p),
#		                                                        Village07Top | Village07Right + (hook | LEDGE + sinner | djump + (dodge | silva | champion) | dodge + (silva | champion + dash))
		"Cliffside Hamlet 07 To Cliffside Hamlet 14"           : lambda s : s.can_reach(el['Village07Top'], 'Region', p) or s.can_reach(el['Village07Right'], 'Region', p) and (s.has(el['hook'], p) or macros['LEDGE'](s) and s.has(el['sinner'], p) or s.has(el['djump'], p) and (s.has(el['dodge'], p) or s.has(el['silva'], p) or s.has(el['champion'], p)) or s.has(el['dodge'], p) and (s.has(el['silva'], p) or s.has(el['champion'], p) and s.has(el['dash'], p))),
#		                                                        Village08Left
		"Cliffside Hamlet 08 - Headless Defender"              : lambda s : s.can_reach(el['Village08Left'], 'Region', p),
#		                                                        Village08Left
		"Cliffside Hamlet 08 - Amulet Fragment"                : lambda s : s.can_reach(el['Village08Left'], 'Region', p),
#		                                                        Village08Left + swim
		"Cliffside Hamlet 08 - Stagnant Blight x10"            : lambda s : s.can_reach(el['Village08Left'], 'Region', p) and s.has(el['swim'], p),
#		                                                        Village08Left | Village08Right
		"Cliffside Hamlet 08 To Cliffside Hamlet 06"           : lambda s : s.can_reach(el['Village08Left'], 'Region', p) or s.can_reach(el['Village08Right'], 'Region', p),
#		                                                        Village08Right | Village08Left
		"Cliffside Hamlet 08 To Cliffside Hamlet 09"           : lambda s : s.can_reach(el['Village08Right'], 'Region', p) or s.can_reach(el['Village08Left'], 'Region', p),
#		                                                        BridgeHead
		"Cliffside Hamlet 09 - Adherent's Letter"              : lambda s : s.can_reach(el['BridgeHead'], 'Location', p),
#		                                                        Village09Right1 | Village09Right2 | Village09Left1 | Village09Left2
		"Cliffside Hamlet 09 - Hamlet Request 1"               : lambda s : s.can_reach(el['Village09Right1'], 'Region', p) or s.can_reach(el['Village09Right2'], 'Region', p) or s.can_reach(el['Village09Left1'], 'Region', p) or s.can_reach(el['Village09Left2'], 'Region', p),
#		                                                        Village09Right1 | BridgeHead
		"Cliffside Hamlet 09 To Cliffside Hamlet 10"           : lambda s : s.can_reach(el['Village09Right1'], 'Region', p) or s.can_reach(el['BridgeHead'], 'Location', p),
#		                                                        Village09Right2 | BridgeHead + swim
		"Cliffside Hamlet 09 To Cliffside Hamlet 15"           : lambda s : s.can_reach(el['Village09Right2'], 'Region', p) or s.can_reach(el['BridgeHead'], 'Location', p) and s.has(el['swim'], p),
#		                                                        Village09Left1 | BridgeHead
		"Cliffside Hamlet 09 To Cliffside Hamlet 07"           : lambda s : s.can_reach(el['Village09Left1'], 'Region', p) or s.can_reach(el['BridgeHead'], 'Location', p),
#		                                                        Village09Left2 | BridgeHead
		"Cliffside Hamlet 09 To Cliffside Hamlet 08"           : lambda s : s.can_reach(el['Village09Left2'], 'Region', p) or s.can_reach(el['BridgeHead'], 'Location', p),
#		                                                        Village10Left | Village10Right
		"Cliffside Hamlet 10 - Gerrod, the Elder Warrior"      : lambda s : s.can_reach(el['Village10Left'], 'Region', p) or s.can_reach(el['Village10Right'], 'Region', p),
#		                                                        Gerrod
		"Cliffside Hamlet 10 To Cliffside Hamlet 09"           : lambda s : s.can_reach(el['Gerrod'], 'Location', p),
#		                                                        Gerrod
		"Cliffside Hamlet 10 To Cliffside Hamlet 11"           : lambda s : s.can_reach(el['Gerrod'], 'Location', p),
#		                                                        Village111Bottom + slam
		"Cliffside Hamlet 11_1 - Priestess' Wish"              : lambda s : s.can_reach(el['Village111Bottom'], 'Region', p) and s.has(el['slam'], p),
#		                                                        Village111Bottom
		"Cliffside Hamlet 11_1 To Cliffside Hamlet 11"         : lambda s : s.can_reach(el['Village111Bottom'], 'Region', p),
#		                                                        Village11Left
		"Cliffside Hamlet 11 - Hamlet Scrawl"                  : lambda s : s.can_reach(el['Village11Left'], 'Region', p),
#		                                                        Village11Left
		"Cliffside Hamlet 11 - Hamlet Request 2"               : lambda s : s.can_reach(el['Village11Left'], 'Region', p),
#		                                                        Village11Top | Village11Left
		"Cliffside Hamlet 11 To Cliffside Hamlet 11_1"         : lambda s : s.can_reach(el['Village11Top'], 'Region', p) or s.can_reach(el['Village11Left'], 'Region', p),
#		                                                        Village11Left
		"Cliffside Hamlet 11 - Furious Blight x10"             : lambda s : s.can_reach(el['Village11Left'], 'Region', p),
#		                                                        Village11Left | Village11Right + claw
		"Cliffside Hamlet 11 To Cliffside Hamlet 10"           : lambda s : s.can_reach(el['Village11Left'], 'Region', p) or s.can_reach(el['Village11Right'], 'Region', p) and s.has(el['claw'], p),
#		                                                        Village11Right | Village11Left + claw
		"Cliffside Hamlet 11 To Ruined Castle 01"              : lambda s : s.can_reach(el['Village11Right'], 'Region', p) or s.can_reach(el['Village11Left'], 'Region', p) and s.has(el['claw'], p),
#		                                                        Village12Left1
		"Cliffside Hamlet 12 - Stagnant Blight x10"            : lambda s : s.can_reach(el['Village12Left1'], 'Region', p),
#		                                                        Village12Top
		"Cliffside Hamlet 12 To Cliffside Hamlet 06"           : lambda s : s.can_reach(el['Village12Top'], 'Region', p),
#		                                                        Village12Left1 | Village12Right + Village12Top
		"Cliffside Hamlet 12 To Cliffside Hamlet 13"           : lambda s : s.can_reach(el['Village12Left1'], 'Region', p) or s.can_reach(el['Village12Right'], 'Region', p) and s.can_reach(el['Village12Top'], 'Region', p),
#		                                                        Village12Right | Village12Left1 + Village12Top + swim
		"Cliffside Hamlet 12 To Catacombs 01"                  : lambda s : s.can_reach(el['Village12Right'], 'Region', p) or s.can_reach(el['Village12Left1'], 'Region', p) and s.can_reach(el['Village12Top'], 'Region', p) and s.has(el['swim'], p),
#		                                                        Village12Left2 | Village12Left1 + CHARGE
		"Cliffside Hamlet 12 To Cliffside Hamlet 16"           : lambda s : s.can_reach(el['Village12Left2'], 'Region', p) or s.can_reach(el['Village12Left1'], 'Region', p) and macros['CHARGE'](s),
#		                                                        Village13Right + 2LEDGE | LEDGE + (dash | HORIZONTAL)
		"Cliffside Hamlet 13 - Amulet Gem"                     : lambda s : s.can_reach(el['Village13Right'], 'Region', p) and macros['2LEDGE'](s) or macros['LEDGE'](s) and (s.has(el['dash'], p) or macros['HORIZONTAL'](s)),
#		                                                        Village13Right
		"Cliffside Hamlet 13 - Chain of Sorcery"               : lambda s : s.can_reach(el['Village13Right'], 'Region', p),
#		                                                        Village13Left + swim
		"Cliffside Hamlet 13 - Giant's Ring"                   : lambda s : s.can_reach(el['Village13Left'], 'Region', p) and s.has(el['swim'], p),
#		                                                        Village13Left
		"Cliffside Hamlet 13 - Stagnant Blight x10"            : lambda s : s.can_reach(el['Village13Left'], 'Region', p),
#		                                                        Village13Top | Village13Right + LEDGE
		"Cliffside Hamlet 13 To Cliffside Hamlet 03"           : lambda s : s.can_reach(el['Village13Top'], 'Region', p) or s.can_reach(el['Village13Right'], 'Region', p) and macros['LEDGE'](s),
#		                                                        Village13Left | Village13Right
		"Cliffside Hamlet 13 To Cliffside Hamlet 02"           : lambda s : s.can_reach(el['Village13Left'], 'Region', p) or s.can_reach(el['Village13Right'], 'Region', p),
#		                                                        Village13Right | Village13Top
		"Cliffside Hamlet 13 To Cliffside Hamlet 12"           : lambda s : s.can_reach(el['Village13Right'], 'Region', p) or s.can_reach(el['Village13Top'], 'Region', p),
#		                                                        Village14Bottom + (LEDGE | hook)
		"Cliffside Hamlet 14 - Cliffside Hamlet Elder"         : lambda s : s.can_reach(el['Village14Bottom'], 'Region', p) and (macros['LEDGE'](s) or s.has(el['hook'], p)),
#		                                                        Elder + (slam + (hook | LEDGE + sinner | silva + (djump | dodge) | champion + (dash | claw) + (silva | djump)))
		"Cliffside Hamlet 14 - Stagnant Blight x30"            : lambda s : s.can_reach(el['Elder'], 'Location', p) and (s.has(el['slam'], p) and (s.has(el['hook'], p) or macros['LEDGE'](s) and s.has(el['sinner'], p) or s.has(el['silva'], p) and (s.has(el['djump'], p) or s.has(el['dodge'], p)) or s.has(el['champion'], p) and (s.has(el['dash'], p) or s.has(el['claw'], p)) and (s.has(el['silva'], p) or s.has(el['djump'], p)))),
#		                                                        Elder + (slam + (hook | 3LEDGE | FULLSILVA | claw + LEDGE) )
		"Cliffside Hamlet 14 - Furious Blight x30"             : lambda s : s.can_reach(el['Elder'], 'Location', p) and (s.has(el['slam'], p) and (s.has(el['hook'], p) or macros['3LEDGE'](s) or macros['FULLSILVA'](s) or s.has(el['claw'], p) and macros['LEDGE'](s))),
#		                                                        Village14Bottom
		"Cliffside Hamlet 14 To Cliffside Hamlet 07"           : lambda s : s.can_reach(el['Village14Bottom'], 'Region', p),
#		                                                        Village15Left + swim + (claw + (sinner + (djump | champion) | dodge + silva | 2LEDGE + HORIZONTAL) | hook + (2LEDGE | claw + (LEDGE | HORIZONTAL))) | Village15Right + claw + djump + silva
		"Cliffside Hamlet 15 - Stagnant Blight x800"           : lambda s : s.can_reach(el['Village15Left'], 'Region', p) and s.has(el['swim'], p) and (s.has(el['claw'], p) and (s.has(el['sinner'], p) and (s.has(el['djump'], p) or s.has(el['champion'], p)) or s.has(el['dodge'], p) and s.has(el['silva'], p) or macros['2LEDGE'](s) and macros['HORIZONTAL'](s)) or s.has(el['hook'], p) and (macros['2LEDGE'](s) or s.has(el['claw'], p) and (macros['LEDGE'](s) or macros['HORIZONTAL'](s)))) or s.can_reach(el['Village15Right'], 'Region', p) and s.has(el['claw'], p) and s.has(el['djump'], p) and s.has(el['silva'], p),
#		                                                        Village15Right + swim
		"Cliffside Hamlet 15 - Stagnant Blight x30"            : lambda s : s.can_reach(el['Village15Right'], 'Region', p) and s.has(el['swim'], p),
#		                                                        Village15Left + swim
		"Cliffside Hamlet 15 - Furious Blight x10"             : lambda s : s.can_reach(el['Village15Left'], 'Region', p) and s.has(el['swim'], p),
#		                                                        Village15Left | Village15Right + swim
		"Cliffside Hamlet 15 To Cliffside Hamlet 09"           : lambda s : s.can_reach(el['Village15Left'], 'Region', p) or s.can_reach(el['Village15Right'], 'Region', p) and s.has(el['swim'], p),
#		                                                        Village15Right | Village15Left + Village800
		"Cliffside Hamlet 15 To Twin Spires 01"                : lambda s : s.can_reach(el['Village15Right'], 'Region', p) or s.can_reach(el['Village15Left'], 'Region', p) and s.can_reach(el['Village800'], 'Location', p),
#		                                                        Village16Right
		"Cliffside Hamlet 16 - Faden's Letter"                 : lambda s : s.can_reach(el['Village16Right'], 'Region', p),
#		                                                        Village16Right
		"Cliffside Hamlet 16 - Stone Tablet Fragment"          : lambda s : s.can_reach(el['Village16Right'], 'Region', p),
#		                                                        Village16Right
		"Cliffside Hamlet 16 To Cliffside Hamlet 12"           : lambda s : s.can_reach(el['Village16Right'], 'Region', p),
#		                                                        True
		"Starting Spirit"                                      : lambda s : True,
		'Ending_A'                                             : lambda s : True,
		'Ending_B'                                             : lambda s : True,
		'Ending_C'                                             : lambda s : s.can_reach('Church_13', 'Region', p) and s.count(el['tablet'], p) >= 7,
	}

	items_rules : Dict[str, ItemRule] = {
		'Starting Spirit' : lambda item : item.player == p and item.name.startswith('Spirit.'),
	}

	return (locations_rules, items_rules)
