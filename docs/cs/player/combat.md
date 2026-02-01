# Boj

Nejprve se určí pořadí boje. Poté každý účastník může provést pohyb a jednu akci ve svém kole. Akce mohou být použity k útoku na protivníka, seslání kouzla, vyzvednutí uloženého předmětu, pomoci spojenci, provedení druhého pohybu nebo jakékoli jiné rozumné akce. Boj je navržen jako rychlý a smrtelný, takže se mu vyhnout může být nejlepší volba.

## Iniciativa

Postavy hodí záchranný hod na OBR. Ti, kteří uspějí, jednají před protivníky, ti, kteří selžou, jednají po nich. Toto pořadí je udržováno po celou dobu boje.

**Překvapení:** pokud jedna strana překvapí druhou, ignoruj hod na iniciativu. Prostě zaútočí první.

*„Je-li to blízko, praštím to. Je-li to daleko, přiblížím se."*

— Garruk Marn, Bojovník

## Pohyb a vzdálenosti

Pohyb a vzdálenosti se sledují pomocí tří abstraktních dosahů: Blízko, Vzdáleně a Daleko. Používají se k výpočtu relativních pozic všech postav vůči sobě navzájem. Některé zbraně jsou účinné pouze Blízko, zatímco jiné jsou lepší Vzdáleně.

- **Blízko:** zbraně na blízko; některé střelné zbraně fungují. Méně než 10 metrů.
- **Vzdáleně:** střelné zbraně. Více než 10 metrů.
- **Daleko:** fungují pouze určité zbraně, jako dlouhé luky. Přibližně 60 metrů.

## Hod na zásah

Postavy hodí počet k6 dle hodnoty HZ své zbraně, upraveným dovednostmi povolání nebo omezeními, a snaží se hodit co nejvíce jedniček. Pokud pravidla uvádějí například „+1 na zásah", znamená to, že postava hodí jednu k6 navíc. Podobně „-2 na zásah" znamená, že hodí o dvě k6 méně.

**Důležité:** každé povolání má specializované zbraně — při používání jakékoli jiné má postava -1 na zásah.

- **Slabý zásah:** padne jedna 1 — protivník ztratí body životů rovné poškození zbraně (mínus jeho hodnota Obrany).
- **Silný zásah:** padnou dvě 1 — protivník ztratí body životů rovné dvojnásobnému poškození zbraně (mínus jeho hodnota Obrany).
- **Smrtící úder:** padnou tři a více 1 — protivník je okamžitě eliminován a odstraněn ze hry!
- **Minutí:** nepadne žádná 1.
- **Kritický neúspěch:** padnou dvě nebo více 6, aniž by padla jakákoli 1 — postava zasáhne spojence za k8 poškození NEBO označí používání na neseném předmětu. Volba je na ní. (Pokud kriticky selže protivník, Vypravěč určí odpovídající důsledek.)

**Poznámka:** pokud hráčská postava obdrží Smrtící úder, není okamžitě zabita. Místo toho její body životů klesnou na nulu a musí hodit na tabulku Smrti. Hodně štěstí.

**Důležité:** kdykoli má útok speciální efekt jako Jakýkoli zásah, Silný zásah nebo Smrtící úder (například Druidova bestí podoba nebo většina tvorů v bestiáři), tento efekt nastane navíc k běžným bojovým důsledkům. „Jakýkoli zásah" znamená, že efekt nastane při Slabém zásahu, Silném zásahu i Smrtícím úderu.

#### Pokerové kostky

Některé dovednosti a Legendární zbraně mají efekty, které se spouští, když padnou „pokerové výsledky" v hodech na zásah.

- **Pár:** dvě kostky ukazují stejné číslo.
- **Trojice:** tři kostky se stejným číslem.
- **Poker:** čtyři kostky ukazují stejné číslo.
- **Full house:** kombinace páru a trojice ve stejném hodu.
- **Postupka:** řada po sobě jdoucích čísel ve stejném hodu.

## Výhoda nebo nevýhoda

Postavy mohou mít výhodu nebo nevýhodu v závislosti na herních okolnostech („Mám výšku!"). Vypravěč může volně rozhodovat, kdykoli to považuje za vhodné. Výhoda uděluje +1 na zásah, zatímco nevýhoda uděluje -1 na zásah.

**Boj dvěma zbraněmi:** postava provede druhý hod na zásah, ale má nevýhodu na oba útoky.

**Vlastnosti:** pokud chce Vypravěč přidat postavám další nuance, může rozhodnout, že ti s OBR 13+ mají základní výhodu na útoky na dálku a ti se SÍL 13+ mají základní výhodu na útoky na blízko. Naopak OBR nebo SÍL 7 a méně uděluje základní nevýhodu na útočení.

## Zranitelnost

Ti, kteří se pokusí zaměřit zranitelnou postavu nebo protivníka, mají výhodu na svůj hod na zásah. Zranitelné postavy nebo protivníci mohou hodit záchranný hod na začátku svého kola. Při úspěchu se zotaví a jednají normálně. Při neúspěchu platí tyto efekty:

- **Na zemi:** stráví kolo vstáváním. Příští kolo jedná normálně.
- **Znehybněný:** kolo je promarněno (opakuj záchranný hod příští kolo). Paralýzu a chycení řeš stejně.
- **Omráčený:** kolo je promarněno (opakuj záchranný hod příští kolo s výhodou).
- **Oslepený:** může provést jednu akci (žádný pohyb), ale všechny hody na zásah mají postih -2. Opakuj záchranný hod příští kolo.

**Poznámka:** spící cíle mohou být eliminovány bez hodu.

### Útěk

Postavy mohou utéct z boje hodem záchranného hodu na OBR, pokud nejsou pomalejší než jejich protivníci. Při neúspěchu mohou protivníci okamžitě provést hod na zásah navíc proti nim.

## Smrt

Pokud postava ztratí všechny body životů NEBO obdrží čtvrtý stav Zraněný, musí hodit k8 na tabulku Smrti. Pokud se to stane mimo boj, hodí okamžitě. Pokud se to stane během bitvy, je odložena stranou, počká na konec boje a pak hodí. Pokud celá parta zemře, všechny postavy jsou považovány za mrtvé.

| k8 | Výsledek |
|----|----------|
| 1 | **Zážitek blízké smrti:** vstaň s plnými body životů a +1 k jedné vlastnosti dle výběru. |
| 2 | **Knockaut:** okamžitě se zotav s k4 body životů. |
| 3 | **Bezvědomí:** v bezvědomí na k3 hodin. |
| 4 | **Bolest:** nevýhoda na všechny záchranné hody po zbytek sezení. |
| 5 | **Jizva:** trvale ztratí 1 CHA. |
| 6 | **Hrozná rána:** obdrží stav Těžké zranění. Nelze odstranit z inventáře, ledaže zázrakem nebo magickým léčením. |
| 7 | **Zmrzačení:** levý nebo pravý ruční slot inventáře je znehodnocen — označ ho X. Nelze používat obouruční předměty. K zotavení je nutné najít umělou paži. |
| 8 | **Smrt!** |

**Poznámka:** stavy Zraněný nejsou odstraněny hodem na tabulku Smrti. Postavy musí splnit podmínky jejich odstranění. Jakékoli Zranění nad čtvrté vždy spouští hod na tabulku Smrti.

## Zotavení

Existují tři způsoby, jak si postavy mohou odpočinout a zotavit se. Zotavení obnoví body životů a odstraní stavy takto:

- **Krátký odpočinek:** stráví jeden tah odpočinkem a obnoví k4 bodů životů.
- **Dlouhý odpočinek:** stráví jednu hlídku jedením a spánkem a obnoví k4+4 bodů životů.
- **Plný odpočinek:** stráví týden v bezpečném a známém prostředí a obnoví všechny body životů a odstraní většinu dlouhodobých stavů.

## Příklad boje

**Vypravěč:** Vy dva dorazíte k rozbité kapli. Na oltáři stále hoří svíce, vzduch páchne krví a železem. Pohne se postava — rytíř v zrezivělé plátovce, promáčklá helma, táhne za sebou velký meč: „Znesvěcujete posvátnou půdu."

**Tess:** Oh, my rozhodně utíkáme.

**Rook:** Ne, počkej — podívej se na tu čepel. To je relikvie z kované oceli. Cennější než naše životy.

**Tess:** (vzdychne) Fajn. Kryju tě. Vytáhnu svůj krátký luk.

**Vypravěč:** Rytíř se pomalu zvedá, klouby skřípou v tichu. Máte náskok. Co uděláte?

**Rook:** Vrazím dovnitř a seknu ho sekerou do nohy — zkusím ho srazit dřív, než stihne přetáhnout tím mečem.

**Vypravěč:** Hoď na zásah. Tvá sekera má HZ 5.

**Rook:** (hodí 5 kostek) 1, 1, 3, 4, 6. Dvě jedničky!

**Vypravěč:** Silný zásah. Tvá sekera se zakousne do holeně s křupnutím. Jaké má tvá zbraň POŠ?

**Rook:** 4.

**Vypravěč:** Silný zásah znamená dvojnásobné poškození zbraně — celkem 8. Jiskry létají, rytíř padá na jedno koleno, z kloubů vytéká černý olej.

**Tess:** Vystřelím mu šíp do hlavy. HZ 5. (hodí) 1, 3, 4, 4, 6 — jedna jednička.

**Vypravěč:** Slabý zásah. Šíp prorazí hledí. Vykřikne, pak divoce sekne mečem. Rooku, nechám tě hodit záchranný hod na OBR, abys uhnul tomu meči, díky tomu šípu.

**Rook:** (hodí) 12 — neúspěch.

**Vypravěč:** Je to velký meč (hodí 6 kostek). 1, 1, 1, 4, 5, 6. SMRTÍCÍÍÍ ÚÚÚDERRR!

**Rook:** Okamžitě označím používání na helmě, abych to snížil na Silný zásah. Kurňa.

**Tess:** Upustím luk a popadnu ze země hořící svíci. Nacpu mu ji do otevřeného hledí — oheň do obličeje má tendenci zkazit den komukoliv.

**Vypravěč:** Riskantní, ale chytré — hoď záchranný hod na OBR, jestli udržíš nervy takhle zblízka.

**Tess:** (hodí) 7 — úspěch.

**Vypravěč:** Vosk se rozstříkne po jeho helmě. Pod hledím vzplanou plameny. Rytíř zaječí a zapotácí se. Pach hořící smoly plní vzduch, relikvie s řinčením dopadne na kamennou podlahu. V kapli opět zavládlo ticho.
